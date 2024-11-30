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
        return data
    else:
        print(f"Error: {response.status_code}, {response.text}") 

def get_region_hotspots(reg_code):
    response = requests.get(API_ENDPOINT + f"ref/hotspot/{reg_code}", headers=headers, params= {"fmt":"json"})

    # Check the response status and print the data
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        return data
    else:
        print(f"Error: {response.status_code}, {response.text}") 

def get_region_observations(reg_code, days_back = 30, locId = []):
    response = requests.get(API_ENDPOINT + f"data/obs/{reg_code}/recent", headers=headers,params={"back":days_back, "hotspot":True, "r": locId})

    # Check the response status and print the data
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        return data
    else:
        print(f"Error: {response.status_code}, {response.text}") 

def get_region_observations_by_species(reg_code, species, days_back = 30, locId = []):
    response = requests.get(API_ENDPOINT + f"data/obs/{reg_code}/recent/{species}", headers=headers, params={"back":days_back, "hotspot":True, "r":locId})
    # Check the response status and print the data
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        return data
    else:
        print(f"Error: {response.status_code}, {response.text}") 

# def get_hotspot_observations()
# get_region_observations_by_species("US-NY-061", "cedwax")
# get_regions("country", "world")
# print(get_region_observations("sdfjjl",locId = ["L191107"]) == get_region_observations("dfjhsk",locId = ["L191107"]))
# print(get_region_observations_by_species("US-NY", "cedwax") == get_region_observations_by_species_2("US-NY", "cedwax"))

