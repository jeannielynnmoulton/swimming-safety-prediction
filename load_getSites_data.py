import json

import pandas as pd


def get_sites_json_to_dataframe(data_files: list) -> dict:
    """Loads data in json files as pandas dataframes. Returns id to dataframe dict"""
    # Load your JSON file (replace with your file path)
    dfs = {}
    for data_file in data_files:
        with open(data_file, "r") as f:
            data = json.load(f)

        # Extract list of features
        features = data["features"]

        # Flatten each feature into a simple dictionary
        rows = []
        for feat in features:
            props = feat["properties"]
            geom = feat["geometry"]

            rows.append({
                "id": props.get("id"),
                "name": props.get("name"),
                "wiski_id": props.get("wiski_id"),
                "measures": props.get("measures"),
                "lon": geom["coordinates"][0],
                "lat": geom["coordinates"][1]
            })

        df = pd.DataFrame(rows)
        df.head()
        dfs[data_file] = df
    return dfs
