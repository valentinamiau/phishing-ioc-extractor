# Phishing IOC Extractor

This project simulates phishing email triage by extracting Indicators of Compromise (IOCs) from suspicious email content.

## Overview
The tool analyzes a phishing email and automatically extracts:
- URLs
- Domains
- IP addresses

This mirrors early-stage analysis performed by Threat Intelligence and SOC analysts.

## Why This Matters
Phishing remains one of the most common initial access vectors.  
Analysts must quickly extract and assess indicators to:
- Identify malicious infrastructure
- Correlate with other alerts
- Support incident response

This project demonstrates how simple automation can reduce manual effort during phishing investigations.

## How It Works
1. A phishing email is provided as input
2. The script scans the text using pattern matching
3. Indicators are extracted and grouped by type
4. Results are printed in a clear, analyst-friendly format

## Files
- `extract_iocs.py` – Core IOC extraction logic  
- `sample_phishing_email.txt` – Sample phishing email  
- `README.md` – Project documentation  

## Usage
```bash
python extract_iocs.py
