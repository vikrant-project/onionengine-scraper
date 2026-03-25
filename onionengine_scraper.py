import requests
from bs4 import BeautifulSoup

def search_onionengine():
    query = input("Enter what you want to search: ")

    url = "https://onionengine.io/scrape.php"

    params = {
        "q": query,
        "page": 1
    }

    headers = {
        "user-agent": "Mozilla/5.0"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        print("Request failed")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    print("\n🔍 Real Onion Results:\n")

    results = soup.find_all("a")

    count = 0

    for link in results:
        href = link.get("href")
        text = link.get_text(strip=True)

        if href and ".onion" in href:
            print(f"{count+1}. {text if text else 'No Title'}")
            print(f"   {href}\n")
            count += 1

        if count >= 10:
            break

    if count == 0:
        print("No results found")

if __name__ == "__main__":
    search_onionengine()
