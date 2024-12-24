# NGWA Scrapper

## Table of Contents

1. [Overview](#overview)
2. [Scripts](#scripts)
   - [ngwaLinks.py](#ngwalinks.py)
   - [ngwData.py](#ngwdatapy)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
   - [Step 1: Scraping Links](#step-1-scraping-links)
   - [Step 2: Scraping Data](#step-2-scraping-data)
6. [Outputs](#outputs)
7. [Code Details](#code-details)
   - [ngwaLinks.py](#code-details-ngwalinkspy)
   - [ngwData.py](#code-details-ngwdatapy)
8. [Error Handling](#error-handling)
9. [Notes](#notes)
10. [Disclaimer](#disclaimer)
11. [Conclusion](#conclusion)

## Overview

This project is designed to automate the process of collecting and analyzing business listing data from the NGWS website. The scraping process is split into two scripts:

1. `ngwaLinks.py`: Collects URLs of listings from paginated search result pages.
2. `ngwData.py`: Extracts detailed information for each listing from the collected URLs.

## Scripts

### ngwaLinks.py

**Purpose:**
Scrapes listing links from paginated search results on the NGWS website.

**Features:**
- Visits each page in the paginated search results.
- Extracts and saves listing links to a CSV file.

**Output:**
- `path/links.csv`: Contains URLs of all extracted listings.

### ngwData.py

**Purpose:**
Extracts detailed data for each listing, including geolocation, contact details, and multimedia information.

**Features:**
- Scrapes details such as:
  - Listing title and description
  - Logo and images
  - Address (with latitude and longitude using Geopy)
  - Contact information (phone, fax, email)
  - Website and social media links
  - Categories and amenities
  - Video links
- Saves data into CSV files.

**Output:**
- `path/data.csv`: Contains detailed data for each listing.
- `path/contacts1.csv`: Contains contact information for each listing.

## Requirements

- Python 3.7 or above
- Libraries:
  - Selenium
  - Geopy
  - Pandas
- ChromeDriver compatible with your Chrome browser version

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NGWA-Scrapper.git
   cd your-repo-name
   ```

2. **Install dependencies:**
   ```bash
   pip install selenium geopy pandas
   ```

3. **Set up ChromeDriver:**
   - Download [ChromeDriver](https://sites.google.com/chromium.org/driver/).
   - Update the `service` path in both scripts (default is `C:/chromedriver.exe`) to match your system's ChromeDriver location.

## Usage

### Step 1: Scraping Links

Run the `ngwaLinks.py` script to scrape listing URLs:
```bash
python ngwaLinks.py
```

**Output:**
- The script saves all extracted links to `path/links.csv`.

### Step 2: Scraping Data

Run the `ngwData.py` script to extract detailed information for each listing:
```bash
python ngwData.py
```

**Output:**
- The script reads URLs from `path/links.csv` and saves listing data to:
  - `path/data.csv`
  - `path/contacts1.csv`

## Outputs

1. **links.csv:**
   - Columns: `Link`
   - Contains URLs of business listings.

2. **data.csv:**
   - Columns:
     - Listing ID
     - Title
     - Description
     - Logo
     - Address, Latitude, Longitude
     - Phone, Fax, Website
     - Social media links (Facebook, Instagram, Twitter, YouTube, LinkedIn)
     - Categories, Amenities, Images
     - Video Link

3. **contacts1.csv:**
   - Columns:
     - My ID
     - Contact Type
     - Name
     - Email Type
     - Email

## Code Details

### Code Details: ngwaLinks.py

1. **Initialization:**
   - Sets up the ChromeDriver service and initializes the browser.
2. **land_required_page(url):**
   - Navigates to the specified URL.
3. **get_links():**
   - Extracts listing links using XPath.
   - Saves links to `links.csv`.

### Code Details: ngwData.py

1. **Initialization:**
   - Sets up the ChromeDriver service and initializes the browser.
   - Uses Geopy's ArcGIS for geolocation services.
2. **Methods for Scraping:**
   - `land_required_page(url)`: Opens the listing page.
   - `get_title()`: Extracts the listing title.
   - `get_description()`: Extracts the description.
   - `get_logo()`: Extracts the logo URL.
   - `get_address()`: Extracts the address and geolocation (latitude, longitude).
   - `get_contacts()`: Extracts contact details (phone, fax).
   - `get_website()`: Extracts the website URL.
   - `get_social_links()`: Extracts social media links.
   - `get_other_contacts(my_id)`: Extracts additional contacts.
   - `get_video_link()`: Extracts video links.
   - `get_images()`: Extracts image URLs.
   - `get_amenities()`: Extracts categories and amenities.
3. **move_into_file():**
   - Saves scraped data to `data.csv` and `contacts1.csv`.

## Error Handling

1. Each data extraction step includes exception handling to ensure script continuity.
2. Missing data entries are recorded as "N/A".
3. Logs errors in extraction for debugging.

## Notes

- The file paths (`path/`) must be updated to match your desired save locations.
- Implicit waits are used to ensure elements load properly.
- The scripts rely on the current HTML structure of the NGWS website. If the structure changes, the scripts may need updates.

## Disclaimer

This project is intended for educational purposes only. Ensure compliance with the NGWS website's terms of service before using the scripts.

## Conclusion

The NGWA Data Scraping project provides an automated solution for extracting comprehensive business listing data from the NGWS website. By breaking the scraping process into two distinct scripts, the project ensures modularity and clarity. This documentation outlines the installation, usage, and code structure to enable users to seamlessly set up and execute the scripts. Future updates may involve adding functionality for dynamic website handling or optimizing performance. Ensure ethical and responsible use of this tool in accordance with applicable regulations and website policies.

