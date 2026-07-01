from apify_client import ApifyClient
import pandas as pd

# Your Apify token
client = ApifyClient("")

# Run input
run_input = {
    "searchStringsArray": [
        "construction company in dubai"
    ],
    "maxCrawledPlacesPerSearch": 50,
}

# Correct actor
run = client.actor(
    "nwua9Gu5YrADL7ZDj"
).call(run_input=run_input)

# Read dataset
items = client.dataset(
    run["defaultDatasetId"]
).list_items().items

rows = []

for i in items:

    rows.append({
        "Company": i.get("title"),
        "Address": i.get("address"),
        "Phone": i.get("phone"),
        "Website": i.get("website"),
        "Rating": i.get("totalScore")
    })

df = pd.DataFrame(rows)

df.to_csv(
    "construction_dubai_companies.csv",
    index=False
)

print(df.head())