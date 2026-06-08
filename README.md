# Automated Outreach Pipeline
Demo Video : https://drive.google.com/file/d/1GWg7qkcjFyfPwvA9HuXwIaP_SykfkX2L/view

Portfolio: https://afreed.online

## Overview

This project automates the process of finding prospects, collecting contact information, and sending personalized outreach emails.

The pipeline integrates multiple services to streamline lead generation and email outreach, reducing manual effort and improving efficiency.

---

## How It Works

### Step 1: Company Discovery

The system searches for relevant companies using Ocean.io and identifies potential prospects based on the required criteria.

### Step 2: Contact Discovery

For each company, the system uses Prospeo to find professional contact information such as business email addresses.

### Step 3: Outreach Preparation

The collected lead data is processed and prepared for outreach campaigns.

### Step 4: Email Delivery

The system sends outreach emails through Brevo's email infrastructure.

### Step 5: Automation

The entire workflow is orchestrated through the main pipeline, allowing multiple prospects to be processed automatically.

---

## Services Used

* Ocean.io – Company discovery
* Prospeo – Contact and email discovery
* Brevo – Email delivery
* Eazyreach – Outreach workflow integration

---

## Project Structure

```text
automated-outreach-pipeline/
│
├── main.py
├── ocean.py
├── prospeo.py
├── eazyreach.py
├── brevo_mail.py
├── test_prospeo.py
├── requirements.txt
└── README.md
```

### File Descriptions

#### main.py

Main entry point that executes the outreach pipeline.

#### ocean.py

Handles company discovery and prospect identification.

#### prospeo.py

Handles contact enrichment and email discovery.

#### eazyreach.py

Manages outreach workflow and lead processing.

#### brevo_mail.py

Responsible for sending emails through Brevo.

#### test_prospeo.py

Contains testing and validation utilities.

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file and add the required API credentials.

Example:

```env
BREVO_API_KEY=your_api_key
PROSPEO_API_KEY=your_api_key
OCEAN_API_KEY=your_api_key
```

Do not commit API keys or sensitive credentials to GitHub.

---

## Running the Project

Execute:

```bash
python main.py
```

The pipeline will:

1. Discover companies
2. Retrieve contact information
3. Process outreach data
4. Send emails through Brevo

---

## Features

* Automated lead discovery
* Contact enrichment
* Outreach automation
* Email campaign support
* Modular architecture
* Secure API key management

---

## Security

Sensitive credentials are stored in environment variables and are excluded from version control using `.gitignore`.

---

## Assignment Submission

This project was developed as part of the SDE Intern Assignment for Vocallabs/Subspace.
