# Property Details Scraper

A Python script to scrape property details from the PropertyPro website. This script fetches information such as property titles, locations, prices, and more from specified pages.

## Features

- Fetches property details including:
  - Title
  - Location
  - Date added
  - Price
  - Bed and Bath details
  - Perks
  - Image URLs
- Saves the extracted data to a CSV file for easy access.

## Requirements

- Python 3.7
- `pandas`
- `beautifulsoup4`
- `lxml` (or any other HTML parser)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Adeyemi0/property-details-scraper.git
   cd property-details-scraper
 ```

2. Install the required packages:
   ```bash
   pip install pandas beautifulsoup4 lxml
```

## Usage

```bash
df = fetch_property_details('https://www.propertypro.ng/property-for-sale?page=', 0, 2)
df.head()
```

