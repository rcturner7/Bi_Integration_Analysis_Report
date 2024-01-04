import os
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'keyfile.json'

# Create a BigQuery client
client = bigquery.Client()

# Run a query
query = """
    SELECT name, SUM(number) as total_people
    FROM `bigquery-public-data.usa_names.usa_1910_2013`
    WHERE state = 'TX'
    GROUP BY name, state
    ORDER BY total_people DESC
    LIMIT 20
"""
query_job = client.query(query)

# Print the results
for row in query_job:
    print(f"{row.name}: {row.total_people}")
