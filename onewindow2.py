import requests
from bs4 import BeautifulSoup
import json

# Define the URL and fetch the page
url = 'https://www.4icu.org/de/universities/'
page = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(page.text, 'html.parser')

# Initialize an empty list to store the university data
universities = []

# Locate the container that holds the university details
# Modify the selector based on actual page structure
university_rows = soup.find_all('tr')

# Iterate over the rows and extract details
for row in university_rows[1:]:  # Skipping the first row if it's a header
    try:
        # Extract the university name and URL
        name_tag = row.find('a')
        if name_tag and name_tag.get('href'):
            name = name_tag.text.strip()
            university_url = name_tag.get('href')
            if not university_url.startswith('http'):
                university_url = f"https://www.4icu.org{university_url}"
        else:
            continue  # Skip this row if no name or URL is found
        
        # Extract the university logo URL
        logo_tag = row.find('img')
        if logo_tag and logo_tag.get('src'):
            logo_src = f"https://www.4icu.org{logo_tag.get('src')}"
        else:
            logo_src = None

        # Dummy data for location, type, and established year
        location = {
            "country": "Germany",  # Adjust according to the actual country
            "state": "Baden-Wurttemberg",  # Adjust according to the actual state
            "city": "Stuttgart"  # Adjust according to the actual city
        }
        type_of_uni = "public"  # Modify as per actual data
        established_year = "1829"  # Modify as per actual data

        # Dummy contact data
        contact = {
            "facebook": "https://www.facebook.com/Universitaet.Stuttgart",  # Modify as per actual data
            "twitter": "https://twitter.com/Uni_Stuttgart",  # Modify as per actual data
            "instagram": "https://www.instagram.com/unistuttgart",  # Modify as per actual data
            "officialWebsite": university_url,
            "linkedin": "https://www.linkedin.com/school/universit%C3%A4t-stuttgart/",  # Modify as per actual data
            "youtube": "https://www.youtube.com/@uni_stuttgart"  # Modify as per actual data
        }

        # Store the university data
        universities.append({
            "name": name,
            "location": location,
            "logoSrc": logo_src,
            "type": type_of_uni,
            "establishedYear": established_year,
            "contact": contact
        })

    except Exception as e:
        print(f"Error processing row: {e}")

# Save the extracted data to a JSON file
with open('universities.json', 'w') as f:
    json.dump(universities, f, indent=4)

print("Data saved to universities.json")
