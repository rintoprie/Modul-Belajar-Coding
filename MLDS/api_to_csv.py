# get data from http rest api then download as csv file

import requests
import pandas as pd
from io import StringIO

def download_csv_from_api(url, filename="data.csv"):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        # Assuming the API returns data that can be directly converted to a DataFrame.
        # Adjust the parsing logic based on the API's response format.
        data = response.text
        df = pd.read_csv(StringIO(data))  # Or pd.read_json(), etc.

        df.to_csv(filename, index=False)
        print(f"Data successfully downloaded and saved to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading data from the API: {e}")
    except pd.errors.EmptyDataError:
        print("Error: The API response is empty.")
    except pd.errors.ParserError:
        print("Error: Could not parse the API response as CSV.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# example usage:
api_url = "your_api_endpoint_here" # Replace with your actual API endpoint
download_csv_from_api(api_url, "my_data.csv")
