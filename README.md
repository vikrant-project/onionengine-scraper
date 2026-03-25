# 🧅 OnionEngine Scraper

A Python-based tool to scrape search results from OnionEngine using reverse-engineered backend endpoints. This tool bypasses frontend JavaScript and directly fetches real search data efficiently.

---

## 📦 Repository

👉 https://github.com/vikrant-project/onionengine-scraper.git

---

## 🚀 Features

* 🔍 Search OnionEngine directly from terminal
* ⚡ Fast scraping (no browser / Selenium required)
* 🧠 Uses reverse-engineered API (`scrape.php`)
* 🧅 Extracts `.onion` links
* 🧹 Clean and minimal output
* 🛠️ Easy to extend (Tor, multi-page, export, etc.)

---

## 📁 File Structure

```
onionengine-scraper/
│── onionengine_scraper.py
│── README.md
│── requirements.txt (optional)
```

---

## ⚙️ Requirements

* Python 3.x
* pip

Install dependencies:

```bash
pip install requests beautifulsoup4
```

---

## ▶️ How to Run

```bash
python3 onionengine_scraper.py
```

Then enter your query:

```
Enter what you want to search: chatbox
```

Output:

```
🔍 Real Onion Results:

1. Example Title
   http://example.onion

2. Another Result
   http://xyz.onion
```

---

## 🧠 How It Works (Code Explanation)

### 1. User Input

```python
query = input("Enter what you want to search: ")
```

Takes dynamic search input from user.

---

### 2. Target Endpoint (IMPORTANT)

```python
url = "https://onionengine.io/scrape.php"
```

Instead of scraping `/search`, this tool directly hits the backend API:

* `/search` → empty HTML shell
* `/scrape.php` → actual results

---

### 3. Sending Request

```python
response = requests.get(url, params={"q": query, "page": 1})
```

* Sends GET request with query
* Mimics browser behavior

---

### 4. Parsing HTML

```python
soup = BeautifulSoup(response.text, "html.parser")
```

Converts raw HTML into navigable structure.

---

### 5. Extracting Onion Links

```python
if href and ".onion" in href:
```

Filters only:

* Valid links
* Onion domains

---

### 6. Output

Displays:

* Title
* Onion URL

---

## ❓ Why Use This Tool?

### ✅ Problem

* OnionEngine uses **JavaScript rendering**
* Normal scraping returns **empty results**
* Most beginners fail here

---

### ✅ Solution

This tool:

* Reverse engineers backend calls
* Bypasses frontend restrictions
* Fetches real data directly

---

## 🎯 Importance

* 🧅 Useful for **Dark Web research / OSINT**
* ⚡ Faster than browser automation tools
* 🧠 Demonstrates **real-world scraping techniques**
* 🔍 Helps understand **hidden APIs behind websites**

---

## ⚖️ Comparison with Other Methods

| Method           | Speed  | Complexity | Reliability |
| ---------------- | ------ | ---------- | ----------- |
| requests (basic) | ❌      | ✅ Easy     | ❌ Fails     |
| Selenium         | ❌ Slow | ❌ Hard     | ✅ Works     |
| This Tool        | ✅ Fast | ✅ Medium   | ✅ Best      |

---

### 🆚 vs Selenium

* ❌ Selenium: heavy, slow, needs browser
* ✅ This: lightweight, fast, direct API

---

### 🆚 vs Raw Scraping

* ❌ Raw scraping: no results (JS problem)
* ✅ This: bypasses JS

---

## 🔥 Advanced Improvements (Future Scope)

* 🔁 Multi-page scraping
* 🌐 Tor proxy integration
* 💾 Export to JSON / CSV
* 🖥️ CLI arguments (`-q chatbox`)
* 📊 Data analysis / filtering

---

## ⚠️ Disclaimer

* This tool is for **educational and research purposes only**
* Do not use for illegal activities
* Access `.onion` links responsibly

---

## 🙌 Contribution

Pull requests are welcome.
Feel free to improve parsing, add features, or optimize performance.

---

## ⭐ Support

If you found this useful, consider starring the repo ⭐

---
