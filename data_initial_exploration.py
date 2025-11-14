import json
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