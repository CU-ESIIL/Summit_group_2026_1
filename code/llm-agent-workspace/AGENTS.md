# AGENTS.md

## Repository Purpose

Template for pulling research article pdfs and assessing them to output a CSV file with categories filled in for particular types of information extracted from each article.
See **TASKS.md** for a plain-English description of the pipeline.

---

## Core Steps

1. **Use text files for downloaded research articles to extract patterns per the input/output specifications.**


## After It Runs

1. **Append to `PROMPT_ACTION_LOG.md`** — date, user's exact prompt, model name, actions taken.

---

## Directory Structure

```
scripts/                          Helper scripts
inputs/                           Original CSV file with all journals published in Environmental Data Science journal as of 5/13/26.
outputs/                          Output CSV file with analyzed data
```

---

## Input Requirements

Text files are located at /home/jovyan/data-store/home/shared/esiil/Innovation_Summit_2026/Group_1/extracted_text/

---

## Output Requirements


One row per file: Create a separate line in an output CSV file for each text file (article) assessed.

Output columns for each text file:

JSON STRUCTURE:
    {{
      "relevance": "Relevant",
      "doi": "string",
      "plant_host": "Full Latin Name",
      "fungal_taxon": "Full Latin Name",
      "tissue": "leaf, root, etc.",
      "presence_absence": "Present",
      "primary_guild": "Endophytic, Pathogenic, Mutualistic, Saprotrophic, Mycorrhizal, or Unknown",
      "interaction_notes": "Specific context",
      "biome": "string",
      "country": "string",
      "doc_type": "Full-Text or Abstract"
    }}

---

## Failure Handling

