import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_ENDPOINT = "https://api.ebird.org/v2/"

# Set up the headers with your API key
headers = {
    "X-eBirdApiToken": API_KEY
}

def get_regions(subreg_type, parent_reg_name):
    # Make the GET request to the eBird API
    response = requests.get(API_ENDPOINT + f"ref/region/list/{subreg_type}/{parent_reg_name}", headers=headers)

    # Check the response status and print the data
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        # print(data)
        return data
    else:
        print(f"Error: {response.status_code}, {response.text}") 

def get_region_hotspots(reg_code):
    response = requests.get(API_ENDPOINT + f"ref/hotspot/{reg_code}", headers=headers, params= {"fmt":"json"})

    # Check the response status and print the data
    if response.status_code == 200:
        # print(response.text)
        data = response.json()  # Parse the JSON response
        # print(data)
        return data
    else:
        print(f"Error: {response.status_code}, {response.text}") 


get_region_hotspots("US-NY")