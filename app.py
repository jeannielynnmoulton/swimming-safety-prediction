import datetime
import json
import os.path

import pandas as pd
import requests
from matplotlib import pyplot as plt

##### DATASET EXTRACTION #####
datasets_url = "https://oxfordrivers.ceh.ac.uk/getDatasets"
datasets_dir = "dataset_data"
datasets_json_file = os.path.join(datasets_dir, "datasets.json")

def get_datasets_as_json():
    datasets_response_json = requests.get(datasets_url).json()
    if not os.path.exists(datasets_dir):
        os.mkdir(datasets_dir)
    with open(datasets_json_file, 'w', encoding='utf-8') as f:
        json.dump(datasets_response_json, f, ensure_ascii=False, indent=4)

def get_datasets_as_pandas(display = False):
    """
    #   Column            Non-Null Count  Dtype
    ---  ------            --------------  -----
     0   id                11 non-null     object
     1   name              11 non-null     object
     2   icon              11 non-null     object
     3   selected          0 non-null      object
     4   color             11 non-null     object
     5   addToMap          11 non-null     bool
     6   group             11 non-null     object
     7   type              11 non-null     object
     8   tooltip           11 non-null     object
     9   pane              1 non-null      object
     10  zIndex            1 non-null      float64
     11  metadata.name     11 non-null     object
     12  metadata.source   10 non-null     object
     13  metadata.type     11 non-null     object
     14  metadata.graph    11 non-null     bool
     15  metadata.map      11 non-null     bool
     16  metadata.licence  8 non-null      object
     17  metadata.page     2 non-null      object
    """
    if not os.path.exists(datasets_json_file):
        get_datasets_as_json()
    with open(datasets_json_file) as f:
        datasets_response_json = json.load(f)
    df = pd.json_normalize(datasets_response_json)
    if display:
        print(df.info())
        print(df)
    return df

##### DETERMINAND EXTRACTION #####
determinands_url = "https://oxfordrivers.ceh.ac.uk/getDeterminands"
determinands_dir = "determinands_data"
determinands_json_file = os.path.join(determinands_dir, "determinands.json")

def get_determinands_as_json():
    determinands_response_json = requests.get(determinands_url).json()
    if not os.path.exists(determinands_dir):
        os.mkdir(determinands_dir)
    with open(determinands_json_file, 'w', encoding='utf-8') as f:
        json.dump(determinands_response_json, f, ensure_ascii=False, indent=4)

def get_determinands_as_pandas(display = False):
    """
    """
    if not os.path.exists(determinands_json_file):
        get_determinands_as_json()
    with open(determinands_json_file) as f:
        determinands_response_json = json.load(f)
    df = pd.json_normalize(determinands_response_json["features"])
    if display:
        print(df.info())
        print(df)
    return df

##### SITES EXTRACTION #####
sites_url = "https://oxfordrivers.ceh.ac.uk/getSites?datasetID={0}" # requires using .format("XXX")
sites_dir = "sites_data"
sites_json_file_base = os.path.join(sites_dir, "sites_{0}.json") # requires using .format("XXX")

def get_sites_for_dataset_as_json(dataset: str):
    filename = sites_url.format(dataset)
    sites_response_json = requests.get(filename).json()
    if not os.path.exists(sites_dir):
        os.mkdir(sites_dir)
    with open(sites_json_file_base.format(dataset), 'w', encoding='utf-8') as f:
        json.dump(sites_response_json, f, ensure_ascii=False, indent=4)

def get_sites_for_dataset_as_pandas(dataset: str, display = False):
    """
     #   Column                               Non-Null Count  Dtype
    ---  ------                               --------------  -----
     0   type                                 130 non-null    object
     1   geometry.type                        130 non-null    object
     2   geometry.coordinates                 130 non-null    object
     3   properties.id                        130 non-null    int64
     4   properties.name                      130 non-null    object
     5   properties.river                     130 non-null    object
     6   properties.masid                     120 non-null    object
     7   properties.catchment_boundaries_url  130 non-null    object
    """
    filename = sites_json_file_base.format(dataset)
    if not os.path.exists(filename):
        get_sites_for_dataset_as_json(dataset)
    with open(filename) as f:
        sites_response_json = json.load(f)
    df = pd.json_normalize(sites_response_json["features"])
    # new_column_names = [col.replace("metadata.", "") for col in df.columns]
    # df.columns = new_column_names
    if display:
        print(df.info())
        print(df)
    return df

##### TIMESERIES EXTRACTION, NO DETERMINAND #####
timeseries_site_dataset_url = "https://oxfordrivers.ceh.ac.uk/getTimeseries?siteID={0}&datasetID={1}" # requires using .format(site, dataset)
timeseries_dir = "timeseries_data"
timeseries_site_dataset_json_file_base = os.path.join(timeseries_dir, "timeseries_{0}_{1}.json") # requires using .format(site, dataset)

def get_timeseries_for_dataset_and_site_as_json(site: str, dataset: str):
    timeseries_response_json = requests.get(timeseries_site_dataset_url.format(site, dataset)).json()
    if not os.path.exists(timeseries_dir):
        os.mkdir(timeseries_dir)
    with open(timeseries_site_dataset_json_file_base.format(site, dataset),'w', encoding='utf-8') as f:
        json.dump(timeseries_response_json, f, ensure_ascii=False, indent=4)

def get_timeseries_for_dataset_and_site_as_pandas(site: str, dataset: str, display=False):
    filename = timeseries_site_dataset_json_file_base.format(site, dataset)
    if not os.path.exists(filename):
        get_timeseries_for_dataset_and_site_as_json(site, dataset)
    with open(filename) as f:
        timeseries_response_json = json.load(f)
    df = pd.json_normalize(timeseries_response_json["data"])
    if display:
        print(df.info())
        print(df)
    return df

##### TIMESERIES EXTRACTION WITH DETERMINAND #####
timeseries_site_dataset_determinand_url = "https://oxfordrivers.ceh.ac.uk/getTimeseries?siteID={0}&datasetID={1}&determinand={2}" # requires using .format(site, dataset, determinand)
timeseries_site_dataset_determinand_json_file_base = os.path.join(timeseries_dir, "timeseries_{0}_{1}_{2}.json") # requires using .format(site, dataset, determinand)

def get_timeseries_for_dataset_site_determinand_as_json(site: str, dataset: str, determinand: str):
    timeseries_response_json = requests.get(timeseries_site_dataset_determinand_url.format(site, dataset, determinand)).json()
    if not os.path.exists(timeseries_dir):
        os.mkdir(timeseries_dir)
    filename = timeseries_site_dataset_determinand_json_file_base.format(site, dataset, determinand)
    with open(filename,'w', encoding='utf-8') as f:
        json.dump(timeseries_response_json, f, ensure_ascii=False, indent=4)

def get_timeseries_for_dataset_site_determinand_as_pandas(site: str, dataset: str, determinand: str, display=False):
    filename = timeseries_site_dataset_determinand_json_file_base.format(site, dataset, determinand)
    if not os.path.exists(filename):
        get_timeseries_for_dataset_site_determinand_as_json(site, dataset, determinand)
    with open(filename) as f:
        timeseries_response_json = json.load(f)
    df = pd.json_normalize(timeseries_response_json["data"])
    if display:
        print(df.info())
        print(df)
    return df

##### TIMESERIES EXTRACTION WITH DATE #####
timeseries_site_dataset_date_url = "https://oxfordrivers.ceh.ac.uk/getTimeseries?siteID={0}&date={1}&datasetID={2}" # requires using .format(site, date (yyyy-mm-dd), dataset)
timeseries_site_dataset_date_json_file_base = os.path.join(timeseries_dir, "timeseries_{0}_{1}_{2}.json") # requires using .format(site, date, dataset)

def get_timeseries_for_date_dataset_as_json(site: str, dataset: str, date: datetime.date):
    date_str = date.strftime('%Y-%m-%d')
    timeseries_response_json = requests.get(timeseries_site_dataset_date_url.format(site, date_str, dataset)).json()
    if not os.path.exists(timeseries_dir):
        os.mkdir(timeseries_dir)
    with open(timeseries_site_dataset_date_json_file_base.format(site, date_str, dataset),'w', encoding='utf-8') as f:
        json.dump(timeseries_response_json, f, ensure_ascii=False, indent=4)

def get_timeseries_for_date_dataset_as_pandas(site: str, dataset: str, date: datetime.date, display=False):
    date_str = date.strftime('%Y-%m-%d')
    filename = timeseries_site_dataset_date_json_file_base.format(site, date_str, dataset)
    if not os.path.exists(filename):
        get_timeseries_for_date_dataset_as_json(site, dataset, date)
    with open(filename) as f:
        date_response_json = json.load(f)
    df = pd.json_normalize(date_response_json["data"])
    if display:
        print(df.info())
        print(df)
    return df

##### DATA FOR DATE EXTRACTION #####
date_dataset_url = "https://oxfordrivers.ceh.ac.uk/getDataForDate?datasetID={0}&date={1}" # requires using .format(dataset, date (yyyy-mm-dd)
date_dataset_dir = "date_data"
date_dataset_json_file_base = os.path.join(date_dataset_dir, "date_{0}_{1}.json") # requires using .format(site, dataset)

def get_data_for_date_dataset_as_json(dataset: str, date: datetime.date):
    date_str = date.strftime('%Y-%m-%d')
    date_response_json = requests.get(date_dataset_url.format(dataset, date_str)).json()
    if not os.path.exists(date_dataset_dir):
        os.mkdir(date_dataset_dir)
    with open(date_dataset_json_file_base.format(dataset, date_str),'w', encoding='utf-8') as f:
        json.dump(date_response_json, f, ensure_ascii=False, indent=4)

def get_data_for_date_dataset_as_pandas(dataset: str, date: datetime.date, display=False):
    date_str = date.strftime('%Y-%m-%d')
    filename = date_dataset_json_file_base.format(dataset, date_str)
    if not os.path.exists(filename):
        get_data_for_date_dataset_as_json(dataset, date)
    with open(filename) as f:
        date_response_json = json.load(f)
    df = pd.json_normalize(date_response_json["data"])
    if display:
        print(df.info())
        print(df)
    return df

def split_col(s):
    #split into value and qualifier like the ea_bathing_water dataset

    s = s.astype(str).str.strip()

    # Extract qualifier
    qualifier = s.str.extract(r'([<>])')[0].map({
        '<': 'lessThan',
        '>': 'greaterThan'
    }).fillna('actual')

    # Extract numeric part (digits only)
    numeric = pd.to_numeric(s.str.extract(r'(\d+)')[0], errors='coerce')

    return numeric, qualifier

def split_interval_across_days(start, end):
    #splits edm spills into chunks (i.e. if spill goes over multiple days, it splits into multiple entries for each day with hours for that day)
    results = []
    current = start

    while current.date() < end.date():
        # end of current day
        day_end = pd.Timestamp.combine(current.date(), datetime.time(23, 59, 59))
        hours = (day_end - current).total_seconds() / 3600
        results.append((current.date(), hours))
        current = day_end + pd.Timedelta(seconds=1)

    # final partial day
    final_hours = (end - current).total_seconds() / 3600
    results.append((current.date(), final_hours))

    return results

def process_edm(df):
    #split into each spill event
    events = df[df['value'].isin(['Start', 'Stop'])].copy()
    events = events.sort_values('datetime').reset_index(drop=True)
    events['next_time'] = events['datetime'].shift(-1)
    events['next_value'] = events['value'].shift(-1)
    pairs = events[(events['value'] == 'Start') & (events['next_value'] == 'Stop')].copy()

    #calculate spill durations per day
    rows = []
    for _, row in pairs.iterrows():
        start = row['datetime']
        end = row['next_time']
        chunks = split_interval_across_days(start, end)
        for d, h in chunks:
            rows.append((d, h))

    #final aggregation into dataframe, filling gaps between first and last spill with 0 spill hours
    daily_spill = pd.DataFrame(rows, columns=['date', 'duration_hours'])
    daily_spill['date'] = pd.to_datetime(daily_spill['date'])
    daily_spill = daily_spill.groupby('date')['duration_hours'].sum().to_frame()
    full_time = pd.date_range(start=daily_spill.index.min(),end=daily_spill.index.max(),freq='D')
    daily_spill = daily_spill.reindex(full_time, fill_value=0)
    daily_spill = daily_spill.round(2).reset_index().rename(columns={'index': 'datetime'})

    return daily_spill

##### EXAMPLE USAGE #####
# get dataset info as pandas
df_datasets = get_datasets_as_pandas(display=False)
# get determinands info as pandas
df_determinands = get_determinands_as_pandas(display=False)
# get sites info for a single example dataset
df_sites_rainfall = get_sites_for_dataset_as_pandas("rainfall", display=False)
# get timeseries without determinand example
df_timeseries_Oxford_fft = get_timeseries_for_dataset_and_site_as_pandas("Oxford", "fft", display=False)
# get timeseries with determinand example
df_timeseries_Wolvercote_sonde_turbidity = get_timeseries_for_dataset_site_determinand_as_pandas("E01612A", "ea_wq_sonde", "turbidity", display=False)
# get data for date example
df_date_rainfall_2024_07_31 = get_data_for_date_dataset_as_pandas("rainfall", datetime.date(2024, 7, 31), display=False)
# get timeseries for date example
df_timeseries_Cassington_edm_2021_01_01 = get_timeseries_for_date_dataset_as_pandas('Cassington', 'edm', datetime.date(2021, 1, 1), display=False)

##### GET DATA FOR ECOLI #####
def get_ecoli_datasets() -> dict:
    """
    Returns a dictionary with keys as tuple of (site_id, dataset_id) and values
    of time series data
    """
    # get time series that contain ecoli info
    # yields -> [[{'code': 'ea_bathing_water', 'id': 'EC', 'column': 'escherichia coli count'}, {'code': 'wtrt', 'id': 'EC', 'column': 'escherichia coli count'}]]
    ecoli_datasets_ids = df_determinands[df_determinands["name"].str.contains("coli", case=False, na=False)]["datasets"].values[0]
    ecoli_timeseries_dfs = {}
    for dataset in ecoli_datasets_ids:
        dataset_id = dataset["code"]
        determinand_id = dataset["id"]
        for site in get_sites_for_dataset_as_pandas(dataset_id)["properties.id"]:
            df = get_timeseries_for_dataset_site_determinand_as_pandas(site, dataset_id, determinand_id)
            #get both datasets into consistent format
            if dataset_id == 'ea_bathing_water':
                # reshape dataframe to have datetime and ecoli/enterococci columns
                columns = ['sample date time', 'escherichia coli count', 'escherichia coli qualifier', 'intestinal enterococci count', 'intestinal enterococci qualifier'] #unique columns, excluding record date which is included in sample date time
                df_new = pd.DataFrame()
                for col in columns:
                    mask = df.columns.str.contains(f'{col}.*')
                    df_new[col] = pd.Series(df.loc[:, mask].T.values.ravel())
                #format datetime to match
                df_new['datetime'] = pd.to_datetime(df_new['sample date time'])
                df_new = df_new.drop(columns=['sample date time'])
                df_new = df_new.sort_values(by='datetime')
                ecoli_timeseries_dfs[(site, dataset_id)] = df_new
            else:
                try:
                    df['datetime'] = pd.to_datetime(df['datetime'])
                    df['escherichia coli count'], df['escherichia coli qualifier'] = split_col(df['value']) #split value into count and qualifier e.g. < 10 (value) -> 10 (count) and lessThan (qualifier)
                    df = df.drop(columns=['value'])
                    df = df.sort_values(by='datetime')
                    ecoli_timeseries_dfs[(site, dataset_id)] = df
                except Exception as e:
                    pass
                    #print(f"Error for site {site} dataset {dataset_id}: {e}") #site 1743499042454x452904883018006500 dataset wtrt is empty
    return ecoli_timeseries_dfs


