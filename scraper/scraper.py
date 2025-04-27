import requests
from bs4 import BeautifulSoup
import json
import os
import time

# Direct menu links for non-Zomato Lucknow restaurants
restaurant_urls = [
    "https://barbequenation.com/restaurants/lucknow/rivarsidemall",
    "https://kitchentfs.com/order/kitchen-the-food-stop-lucknow",
    "https://www.eazydiner.com/lucknow/azrak-saraca-lucknow-indian-specialty-restaurant-saraca-lucknow-661453/menu",
    "https://www.ihcltata.com/content/dam/vivanta/hotels/VBT-Gomti_Nagar_Lucknow/documents/sahib-cafe-menu-taj-mahal-lucknow.pdf",
    "https://www.lemontreehotels.com/uploads/hoteldine/10_49_2024_01_49_47Citrus%20Cafe%20Menu%20opt%201.pdf",
    "https://skyhiltoninn.com/menu/",
    "https://dineoutlucknow.com/menu/"
]

def scrape_restaurant_data(url):
    """Scrape and return structured data for a given restaurant menu URL."""
    data = {
        'url': url,
        'name': None,
        'location': None,
        'menu_items': [],
        'special_features': {'vegetarian_options': 'No', 'gluten_free': 'No'},
        'operating_hours': None,
        'contact_info': None
    }
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()

        # PDFs will not parse via BeautifulSoup; just store URL
        if resp.headers.get('Content-Type', '').startswith('application/pdf'):
            return data

        soup = BeautifulSoup(resp.text, 'html.parser')
        text = soup.get_text(" ", strip=True)

        # 1. Name & Location
        h1 = soup.find('h1')
        if h1: data['name'] = h1.get_text(strip=True)
        for p in soup.find_all('p'):
            txt = p.get_text(strip=True)
            if 'Lucknow' in txt:
                data['location'] = txt
                break

        # 2. Menu items (generic catch-all for divs/lis with “menu” in class)
        for sec in soup.find_all(['div', 'li'], class_=lambda c: c and 'menu' in c.lower()):
            nm = sec.find(['h2','h3','h4'])
            ds = sec.find('p')
            pr = sec.find('span', class_=lambda c: c and 'price' in c.lower())
            if nm:
                data['menu_items'].append({
                    'name': nm.get_text(strip=True),
                    'description': ds.get_text(strip=True) if ds else None,
                    'price': pr.get_text(strip=True) if pr else None
                })

        # 3. Special features
        if 'vegetarian' in text.lower(): data['special_features']['vegetarian_options'] = 'Yes'
        if 'gluten-free' in text.lower() or 'gluten free' in text.lower():
            data['special_features']['gluten_free'] = 'Yes'

        # 4. Operating hours
        for p in soup.find_all('p'):
            t = p.get_text(strip=True).lower()
            if any(x in t for x in ['am','pm','open']):
                data['operating_hours'] = p.get_text(strip=True)
                break

        # 5. Contact info
        for tag in soup.stripped_strings:
            if tag.startswith('Phone') or '@' in tag or tag.replace('-', '').isdigit():
                data['contact_info'] = tag
                break

    except Exception as e:
        print(f"[Error] {url} → {e}")
    return data


def main():
    os.makedirs('data', exist_ok=True)
    all_data = []
    for url in restaurant_urls:
        print(f"Scraping: {url}")
        entry = scrape_restaurant_data(url)
        all_data.append(entry)
        time.sleep(2)  # polite pause

    out_path = os.path.join('data', 'restaurant_data.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=4, ensure_ascii=False)

    print(f"\nDone! Saved {len(all_data)} entries to {out_path}")


if __name__ == "__main__":
    main()
