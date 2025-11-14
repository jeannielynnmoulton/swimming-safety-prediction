import json
import os

import requests
import pandas as pd


print("The datasets available to us are: ")
datasets_response_json = requests.get("https://oxfordrivers.ceh.ac.uk/getDatasets").json()
datasets_df = pd.DataFrame(datasets_response_json)
available_dataset_summary = datasets_df["id"]
print(available_dataset_summary)
# this dataset id list might be useful for iterating over data later
dataset_id_list = available_dataset_summary.values.tolist()

print("The determinands available to us are: ")
determinands_response_json = requests.get("https://oxfordrivers.ceh.ac.uk/getDeterminands").json()
determinands_df = pd.DataFrame(determinands_response_json["features"])
print(determinands_df)
available_determinands_summary = determinands_df[["name", "datasets"]]
print(available_determinands_summary)
print("The datasets that include ecoli are: ")
ecoli_datasets = available_determinands_summary[available_determinands_summary["name"].str.contains("coli", case=False, na=False)]["datasets"]
print(ecoli_datasets.values)


def get_all_datasets_as_json(datasets: list) -> list:
    """Makes a new directory "data" in the root of the repository. Extracts datasets from
    https://oxfordrivers.ceh.ac.uk/getSites?datasetID=X for dataset X for all datasets provided
    in the arguments. Saves a file of the data in json format

    This function should only be run once. It will overwrite data.
    Returns a list of paths to json files created."""

    dir = "data"
    if not os.path.exists(dir):
        os.mkdir(dir)
    print("Getting all datasets and storing as csv...")
    responses = {}
    files = []
    for id in dataset_id_list:
        responses[id] = requests.get("https://oxfordrivers.ceh.ac.uk/getSites?datasetID={0}".format(id)).json()
        file = "data/data_{0}.json".format(id)
        files.append(file)
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(responses[id], f, ensure_ascii=False, indent=4)
    print(files)
    return files

data_files = get_all_datasets_as_json(dataset_id_list)


