# Automated Company Search and CSV Generator

## Project Overview

This project automates collecting company details instead of manually searching through Google Maps, LinkedIn, and websites.

The system searches for businesses using Apify and exports the collected information into a CSV file.

Example use case:

* Search: `construction company in Chennai`
* Collect:

  * Company Name
  * Address
  * Phone Number
  * Website
  * Rating
* Save automatically into CSV

---

## Features

* Automated company search
* Collect business details
* Export results to CSV
* Replace manual copy-paste work
* Easy to modify for any business category

---

## Technologies Used

* Python
* Apify API
* Pandas

---

## Installation

Install required packages:

```bash
pip install apify-client pandas
```

---

## Project Structure

```plaintext
project/
│
├── app.py
├── README.md
├── construction_companies.csv
```

---

## Configuration

Open `app.py`

Replace:

```python
client = ApifyClient("YOUR_APIFY_API_KEY")
```

with:

```python
client = ApifyClient("YOUR_ACTUAL_API_KEY")
```

---

## Run the Project

Open terminal:

```bash
cd C:\BW\project
```

Run:

```bash
python app.py
```

---

## Example Search

Inside code:

```python
run_input = {
    "searchStringsArray": [
        "construction company in Chennai"
    ]
}
```

Change to:

```python
"interior company in Salem"
```

or

```python
"software company in Bangalore"
```

---

## Output

Generated CSV:

```plaintext
construction_companies.csv
```

Example:

| Company | Address | Phone | Website | Rating |
| ------- | ------- | ----- | ------- | ------ |

---

## Workflow

```plaintext
User Search
     ↓
Apify API
     ↓
Business Search
     ↓
Collect Data
     ↓
Pandas DataFrame
     ↓
CSV Export
```

---

## Future Improvements

* Streamlit Dashboard
* Multi-city search
* LinkedIn integration
* Email extraction
* Duplicate removal
* Download CSV from UI

---

## Author

Srinivas
