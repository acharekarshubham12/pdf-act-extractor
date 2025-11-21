# Universal Credit Act – AI PDF Analyzer

A modular AI agent pipeline that extracts, summarizes, and analyses legislative documents.

This project was built in **48 hours** as part of an AI internship assignment.

## Overview & Goal

Design a small yet production-minded AI agent workflow that:

- Reads and extracts text from a PDF
- Cleans and prepares the document
- Summarises the Act using LLMs
- Extracts key legislative sections
- Performs rule-based compliance checks
- Generates clean structured JSON reports

**Focus:** clear architecture · readable code · modular pipeline · real-world use-case

## Tech Stack

| Component           | Tool / Library            |
|---------------------|---------------------------|
| Language            | Python 3.10+              |
| PDF Processing      | PyPDF2                    |
| AI Model            | OpenAI GPT (API)          |
| Environment         | `.env` + `python-dotenv`  |
| Output              | Structured JSON           |
| Version Control     | Git & GitHub              |

## Features

### 1. PDF Text Extraction
- Extracts all pages using PyPDF2
- Normalizes and cleans text
- Saves raw extracted content → `extracted.json`

### 2. LLM Summaries
- Generates high-quality 5–10 bullet summary
- Covers purpose, scope, definitions, obligations, eligibility & enforcement

### 3. Structured JSON Extraction
Produces machine-readable sections and saves as → **`act_structured.json`**


### 4. 6-Rule Legislative Compliance Check

Boolean evaluation of essential legislative elements:

| # | Rule                                        | Status   |
|---|---------------------------------------------|----------|
| 1 | Key terms are clearly defined               | Yes/No   |
| 2 | Eligibility criteria present                | Yes/No   |
| 3 | Authority responsibilities specified        | Yes/No   |
| 4 | Penalties / enforcement mechanisms present  | Yes/No   |
| 5 | Entitlement & payment structure included    | Yes/No   |
| 6 | Record-keeping requirements specified       | Yes/No   |

**Final report saved as** → `final_report.json`

## Workflow
<img width="499" height="523" alt="_- visual selection" src="https://github.com/user-attachments/assets/1bfbdfa0-89c4-41ef-aa7b-6981a305c576" />


## Project Structure

```bash
pdf-act-extractor/
├── extract_text.py               # PDF → raw cleaned text
├── summarize_and_extract.py      # LLM summary + structured JSON
├── rule_checks.py                # 6-rule compliance checks
├── requirements.txt
├── .env.example
├── Universal_Credit_Act_2025.pdf # Input document
├── extracted.json                # Raw extracted text
├── act_structured.json           # Structured sections
└── final_report.json             # Final combined report
```

## Installation
```bash
git clone https://github.com/yourusername/pdf-act-extractor.git
cd pdf-act-extractor
pip install -r requirements.txt
```
## Environment Setup
Create a .env file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
```
## How to Run
```bash
# Step 1: Extract text from PDF
python extract_text.py

# Step 2: Generate summary + structured JSON (uses OpenAI)
python summarize_and_extract.py

# Step 3: Run compliance checks & generate final report
python rule_checks.py
```
## Sample Outputs

- `extracted.json` → Clean raw text from the Act  
- `act_structured.json` → Machine-readable legislative sections  
- `final_report.json` → Full summary + structured data + compliance matrix

## What I Learned

- End-to-end PDF to AI processing pipelines
- Writing clean, modular, and reusable Python scripts
- Prompt engineering for reliable structured JSON output from LLMs
- Secure API key management (`.env` + `.gitignore`)
- Removing secrets from Git history
- Building production-ready code under tight deadlines

## Future Improvements

- [ ] Add Streamlit / Gradio web UI
- [ ] Support batch processing of multiple PDFs
- [ ] Add fallback to other models (Claude, Llama 3, Grok, etc.)
- [ ] Semantic search with embeddings
- [ ] OCR support for scanned documents
- [ ] Dockerize the entire project
- [ ] Add GitHub Actions CI/CD


