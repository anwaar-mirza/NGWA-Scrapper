# NGWA-Scrapper

This project contains two Python scripts, `ngwData.py` and `ngwaLinks.py`, designed to scrape data from the NGWS website using Selenium.

## Table of Contents

- [Overview](#overview)
- [Scripts](#scripts)
  - [ngwaLinks.py](#ngwalinks.py)
  - [ngwData.py](#ngwdatapy)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Outputs](#outputs)
- [Notes](#notes)

## Overview

The project automates data collection from the NGWS website. It consists of two scripts:
1. `ngwaLinks.py`: Collects links from paginated listing pages.
2. `ngwData.py`: Extracts detailed data for each listing from the collected links.

Both scripts leverage the Selenium library to interact with the website and perform scraping tasks.

## Scripts

### ngwaLinks.py

**Purpose**:  
Scrapes listing links from paginated search results on the NGWS website.

**Main Features**:
- Navigates through paginated search result pages.
- Extracts links from each page and saves them to a CSV file (`links.csv`).

**Output**:
- A CSV file containing all extracted links (`path/links.csv`).

---

### ngwData.py

**Purpose**:  
Scrapes detailed information from individual listing pages.

**Main Features**:
- Extracts details such as:
  - Listing Title
  - Description
  - Logo URL
  - Address (with geolocation details)
  - Contact information (Phone, Fax, Email)
  - Website
  - Social media links (Facebook, Instagram, Twitter, YouTube, LinkedIn)
  - Video links
  - Images
  - Amenities
  - Categories
- Saves the extracted data to a CSV file (`data.csv`).
- Saves detailed contact information to another CSV file (`contacts1.csv`).

**Output**:
- A CSV file containing listing details (`path/data.csv`).
- A CSV file containing contact details (`path/contacts1.csv`).

---

## Requirements

- Python 3.7 or above
- Selenium
- Geopy
- Pandas
- ChromeDriver

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NGWA-Scrapper.git
   cd your-repo-name
   ```
2. Install the required Python libraries:
   ```bash
   pip install selenium geopy pandas
   ```
3. Download and set up ChromeDriver:
   - [Download ChromeDriver](https://sites.google.com/chromium.org/driver/)
   - Update the `service` path in the scripts (`C:/chromedriver.exe`) to the location of ChromeDriver on your system.

---

## Usage

### Step 1: Scrape Links

Run the `ngwaLinks.py` script to scrape listing links:
```bash
python ngwaLinks.py
```
The script will save all scraped links to `path/links.csv`.

### Step 2: Scrape Listing Data

Run the `ngwData.py` script to scrape data for the listings:
```bash
python ngwData.py
```
The script will read links from `path/links.csv` and extract detailed information, saving it to `path/data.csv` and `path/contacts1.csv`.

---

## Outputs

- **links.csv**: Contains listing URLs extracted from paginated pages.
- **data.csv**: Contains detailed information for each listing, including geolocation, social media links, and categories.
- **contacts1.csv**: Contains detailed contact information for each listing.

---

## Notes

- Ensure the website structure has not changed, as the scripts rely on specific HTML element paths (`XPath`).
- Update `path/` in the scripts to specify the desired save location for CSV files.
- For large-scale scraping, consider handling rate limits or delays to avoid being blocked.

---

## Disclaimer

This project is intended for educational purposes only. Ensure compliance with the NGWS website's terms of service before running the scripts.
```

Let me know if you need additional details or edits!
