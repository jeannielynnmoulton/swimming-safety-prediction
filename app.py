# Example usage to store all getSites data in data files
import get_data
import load_getSites_data
from get_data import get_dataset_ids, get_sites_as_json, get_sites_datafile_locations
from load_getSites_data import get_sites_json_to_dataframe

# data set ids from https://oxfordrivers.ceh.ac.uk/getDatasets
dataset_id_list = get_dataset_ids()

# getSites data to json
# assuming we have getSites data in data directory, so this is commented out
# sites_data_files = get_sites_as_json(dataset_id_list)
sites_info = get_sites_datafile_locations(dataset_id_list, "site_data")
sites = list(sites_info.keys())
sites_data_files = list(sites_info.values())
sites_data = get_sites_as_json(dataset_id_list)

#getSites data to pandas
getSites_dfs = get_sites_json_to_dataframe(sites_data_files) # this is a dict of 448 dataframes, e.g.
# data/data_thames_initiative.json -> DataFrame[....]
# here is an example printed
print(getSites_dfs["site_data/data_thames_initiative.json"])
print(getSites_dfs["site_data/data_fft.json"])

