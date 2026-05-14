import os
import kaggle

def download_kaggle_dataset():
    # The identifier from the Kaggle URL
    dataset_name = "austinreese/craigslist-carstrucks-data"
    
    # Directory where you want to save the data
    download_path = "./craigslist_data"
    
    # Create the directory if it doesn't exist
    os.makedirs(download_path, exist_ok=True)
    
    print(f"Authenticating and downloading '{dataset_name}'...")
    print("This is a large dataset, please wait...")
    
    try:
        # Download and automatically unzip the files
        kaggle.api.dataset_download_files(
            dataset_name, 
            path=download_path, 
            unzip=True
        )
        print(f"Success! Dataset extracted to: {os.path.abspath(download_path)}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure your kaggle.json file is placed in the correct ~/.kaggle/ directory.")

if __name__ == "__main__":
    download_kaggle_dataset()