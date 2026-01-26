---
title: Portfolio App
emoji: 😻
colorFrom: red
colorTo: red
sdk: docker
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

###### What Each Key File Will Do
excel/loader.py
* Open Excel
* List sheet names
* Return DataFrames
excel/scanner.py
* Extract sample rows
* Convert rows → text
* Feed AI classifiers
ai/classifier.py
* Classify sheet as:
    * PNL
    * BALANCE_SHEET
    * CASH_FLOW
    * UNKNOWN
excel/extractor.py
* Extract rows → normalized rows
* Never uses AI
db/writer.py
* Insert company
* Insert financial statements
* Handles transactions

###### Visual Sequence 
Upload Excel
   ↓
Store file + metadata
   ↓
Load Excel sheets
   ↓
Classify sheets (AI)
   ↓
Detect headers (AI)
   ↓
Extract tables (code)
   ↓
Normalize labels (AI)
   ↓
Extract company info (AI)
   ↓
Insert into MySQL
   ↓
Return response

