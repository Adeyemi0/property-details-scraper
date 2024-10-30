import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

def fetch_property_details(base_url, start_page, end_page):
    """
    Fetch property details from a specified range of pages.

    Parameters:
    base_url (str): The base URL of the property listings.
    start_page (int): The starting page number.
    end_page (int): The ending page number.

    Returns:
    pd.DataFrame: A DataFrame containing property details.
    """
    # Initialize lists to store the extracted data
    titles, locations, dates, prices, bed_bath, perks, image_urls = [], [], [], [], [], [], []

    # Loop through the specified range of pages
    for page in range(start_page, end_page + 1):
        url = f"{base_url}{page}"
        print(f"Fetching data from {url}...")
        try:
            html = urlopen(url)
            bso = soup(html.read(), 'html.parser')

            # Extract property titles, locations, and bed/bath details
            for div in bso.find_all('div', class_='pl-title'):
                title = div.find('h3/a')
                titles.append(title.text.strip() if title else None)

                location = div.find('p')
                locations.append(location.text.strip() if location else None)

            # Extract dates
            dates.extend([date.text.strip() for date in bso.find_all('p', class_='date-added')])

            # Extract prices and bed/bath details
            for price_div in bso.find_all('div', class_='pl-price'):
                price = price_div.find('h3')
                prices.append(price.text.strip() if price else None)

                bed_bath_detail = price_div.find('h6')
                bed_bath.append(bed_bath_detail.text.strip() if bed_bath_detail else None)

            # Extract property perks
            for div in bso.find_all('div', class_='pl-badge-left'):
                ul = div.find('ul')
                perks.append(", ".join(li.text.strip() for li in ul.find_all('li')) if ul else None)

            # Extract image URLs
            image_urls.extend([img['src'] for img in bso.find_all('img') if 'src' in img.attrs])

        except Exception as e:
            print(f"Error fetching data from {url}: {e}")
            continue

    # Create a DataFrame
    max_length = max(len(titles), len(locations), len(dates), len(prices), len(bed_bath), len(perks), len(image_urls))
    
    # Adjust the lengths of the lists
    titles += [None] * (max_length - len(titles))
    locations += [None] * (max_length - len(locations))
    dates += [None] * (max_length - len(dates))
    prices += [None] * (max_length - len(prices))
    bed_bath += [None] * (max_length - len(bed_bath))
    perks += [None] * (max_length - len(perks))
    image_urls += [None] * (max_length - len(image_urls))

    data = {
        'Title': titles,
        'Location': locations,
        'Date': dates,
        'Price': prices,
        'Bed and Bath': bed_bath,
        'Perks': perks,
        'Image URL': image_urls
    }
    
    df = pd.DataFrame(data)
    
    # Save to CSV file
    df.to_csv('property_details.csv', index=False)

    return df
