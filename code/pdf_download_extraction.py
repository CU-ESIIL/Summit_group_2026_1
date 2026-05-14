import pandas as pd
import requests
import os
import time
import glob
import fitz  # PyMuPDF
from bs4 import BeautifulSoup
import urllib.parse

def scrape_publisher_pdf_link(doi):
    """
    Follows the DOI to the publisher's page and attempts to scrape the PDF link.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    doi_url = f"https://doi.org/{doi}"
    
    try:
        session = requests.Session()
        response = session.get(doi_url, headers=headers, allow_redirects=True, timeout=15)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Cambridge Core specific HTML pattern
            for link in soup.find_all('a', href=True):
                href = link['href']
                if '/core/services/aop-cambridge-core/content/view/' in href and href.endswith('.pdf'):
                    return urllib.parse.urljoin(response.url, href)
                
            # Generic fallback for other publishers: look for standard PDF text
            for link in soup.find_all('a', href=True):
                text = link.text.strip().upper()
                href = link['href']
                if 'DOWNLOAD PDF' in text or text == 'PDF':
                    if '.pdf' in href.lower() or 'download' in href.lower():
                        return urllib.parse.urljoin(response.url, href)
                        
    except Exception as e:
        print(f"Scraping failed for {doi}: {e}")
        
    return None

def download_pdfs_from_csv(csv_path, doi_column, output_dir, email):
    """
    Reads a CSV of DOIs and downloads the corresponding Open Access PDFs.
    """
    df = pd.read_csv(csv_path)
    dois = df[doi_column].dropna().unique()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Found {len(dois)} unique DOIs. Starting download...")

    for doi in dois:
        doi_clean = str(doi).strip()
        url = f"https://api.unpaywall.org/v2/{doi_clean}?email={email}"
        pdf_url = None
        
        try:
            # First attempt: Unpaywall
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                oa_location = data.get('best_oa_location', {})
                if oa_location and oa_location.get('url_for_pdf'):
                    pdf_url = oa_location['url_for_pdf']
            
            # Second attempt: Direct Scrape Fallback
            if not pdf_url:
                print(f"Unpaywall missed {doi_clean}. Attempting direct publisher scrape...")
                pdf_url = scrape_publisher_pdf_link(doi_clean)
                
            # Download execution
            if pdf_url:
                pdf_response = requests.get(pdf_url, headers={"User-Agent": "Mozilla/5.0"}, stream=True)
                if pdf_response.status_code == 200:
                    safe_doi = doi_clean.replace('/', '_')
                    file_path = os.path.join(output_dir, f"{safe_doi}.pdf")
                    
                    with open(file_path, 'wb') as f:
                        for chunk in pdf_response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    print(f"Success: Downloaded {doi_clean}")
                else:
                    print(f"Failed: Could not fetch PDF file for {doi_clean} (HTTP {pdf_response.status_code})")
            else:
                print(f"Failed: No PDF link found anywhere for {doi_clean}")

            time.sleep(1)
            
        except Exception as e:
            print(f"Error processing {doi_clean}: {e}")

def convert_pdfs_to_text(pdf_dir, text_dir):
    """
    Converts a directory of PDF files into machine-readable text files.
    """
    if not os.path.exists(text_dir):
        os.makedirs(text_dir)

    pdf_files = glob.glob(os.path.join(pdf_dir, '*.pdf'))
    print(f"\nFound {len(pdf_files)} PDFs to convert. Starting extraction...")

    for pdf_path in pdf_files:
        base_name = os.path.basename(pdf_path).replace('.pdf', '.txt')
        txt_path = os.path.join(text_dir, base_name)

        try:
            doc = fitz.open(pdf_path)
            text_content = []
            
            for page in doc:
                text_content.append(page.get_text())
                
            full_text = "\n".join(text_content)

            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(full_text)

            print(f"Converted: {os.path.basename(pdf_path)}")
            doc.close()
            
        except Exception as e:
            print(f"Error converting {pdf_path}: {e}")

if __name__ == "__main__":
    CSV_FILENAME = "Scoping Review Sheet - citations_reviewed.csv"
    DOI_COLUMN_NAME = "DOI"
    PDF_OUTPUT_DIRECTORY = "downloaded_pdfs"
    TEXT_OUTPUT_DIRECTORY = "extracted_text"
    USER_EMAIL = "your.email@example.com"  # Update this

    download_pdfs_from_csv(
        csv_path=CSV_FILENAME,
        doi_column=DOI_COLUMN_NAME,
        output_dir=PDF_OUTPUT_DIRECTORY,
        email=USER_EMAIL
    )

    convert_pdfs_to_text(
        pdf_dir=PDF_OUTPUT_DIRECTORY,
        text_dir=TEXT_OUTPUT_DIRECTORY
    )