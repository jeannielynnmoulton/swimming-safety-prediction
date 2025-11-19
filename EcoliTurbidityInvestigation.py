# Let's look at stats for ecoli at Wolvercote bathing site
import pandas as pd
from matplotlib import pyplot as plt

import app

ecoli_timeseries_dfs = app.get_ecoli_datasets()
df_timeseries_Wolvercote_sonde_turbidity = app.get_timeseries_for_dataset_site_determinand_as_pandas("E01612A", "ea_wq_sonde", "turbidity", display=False)

wolvercote_ecoli_timeseries = ecoli_timeseries_dfs[("11946", "ea_bathing_water")]
print(wolvercote_ecoli_timeseries)

# merge ecoli and turbidity
# first make datetimes just into dates
wolvercote_ecoli_timeseries["datetime"] = pd.to_datetime(wolvercote_ecoli_timeseries["datetime"].transform(lambda datetime: datetime.date()))
df_timeseries_Wolvercote_sonde_turbidity['datetime'] = pd.to_datetime(df_timeseries_Wolvercote_sonde_turbidity['datetime'])
df_timeseries_Wolvercote_sonde_turbidity = df_timeseries_Wolvercote_sonde_turbidity.set_index('datetime')
df_timeseries_Wolvercote_sonde_turbidity_resampled = df_timeseries_Wolvercote_sonde_turbidity.resample('D').mean().dropna()
wolvercote_ecoli_and_turbidity = wolvercote_ecoli_timeseries.merge(df_timeseries_Wolvercote_sonde_turbidity_resampled, on='datetime', how='left').dropna()

fig, ax1 = plt.subplots(figsize=(10,5))
ax1.plot(wolvercote_ecoli_and_turbidity['datetime'], wolvercote_ecoli_and_turbidity['escherichia coli count'], label='E. coli count')
ax1.set_ylabel('E. coli count')
ax2 = ax1.twinx()
ax2.plot(wolvercote_ecoli_and_turbidity['datetime'], wolvercote_ecoli_and_turbidity['value'], color='orange', label='Turbidity value')
ax2.set_ylabel('Turbidity value')
plt.title("E. coli count and Turbidity")
ax1.set_xlabel("Date")
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
plt.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

plt.show()