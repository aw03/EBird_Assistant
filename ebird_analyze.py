import ebird_api
import pandas as pd

def sub_regions_dataframe(parent_reg = "world"):
    sub_reg_type = "country" if parent_reg == "world" else "subnational1" if parent_reg.count("-") == 0 else "subnational2"
    
    regions_df = pd.DataFrame(ebird_api.get_regions(sub_reg_type,parent_reg))
    return regions_df

def region_hotspots_dataframe(region):
    hotspots_df = pd.DataFrame(ebird_api.get_region_hotspots(region))
    return hotspots_df

def hot_spot_observations_dataframe(locId):
    if type(locId) is not list or len(locId) == 0:
        print("returned empty")
        return pd.DataFrame()
    if len(locId) > 10:
        print("too many hotspots selected: max 10")
    hotspot_obervations_df = pd.DataFrame(ebird_api.get_region_observations("world", locId=locId[:10]))
    return hotspot_obervations_df

def hot_spot_observations_by_species_dataframe(locId,species):
    if type(locId) is not list or len(locId) == 0:
        print("returned empty")
        return pd.DataFrame()
    if len(locId) > 10:
        print("too many hotspots selected: max 10")
    hotspot_obervations_df = pd.DataFrame(ebird_api.get_region_observations_by_species("world",species, locId=locId[:10]))
    return hotspot_obervations_df

def region_observations_dataframe(region):
    observations_df = pd.DataFrame(ebird_api.get_region_observations(region))
    return observations_df

def region_observations_by_species_dataframe(region,species):
    observations_df = pd.DataFrame(ebird_api.get_region_observations_by_species(region,species=species))
    return observations_df


# sub_regions_dataframe("US-MA")
# region_hotspots_dataframe("US-NY-061")
# hot_spot_observations_dataframe(["L191107"])
# hot_spot_observations_by_species_dataframe(["L191107"],species="cedwax")
# nyreg = region_observations_dataframe("US-NY")
# print(nyreg)
# print(len(nyreg))
# print(nyreg["speciesCode"].nunique())
# print(nyreg[["comName",'howMany']])
# print(nyreg.loc[nyreg["speciesCode"] == "cedwax"]['howMany'])

# print(region_observations_by_species_dataframe("US-NY","cedwax")["howMany"])