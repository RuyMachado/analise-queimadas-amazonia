# %%

import pandas as pd

df_without_degradation = pd.read_excel("../data/raw/inpe_EM_BRAmz_results.xlsx", sheet_name="Sem degracação", skiprows=10)

df_with_degradation = pd.read_excel("../data/raw/inpe_EM_BRAmz_results.xlsx", sheet_name="Com degradação", skiprows=10)


# %%

df_with_degradation = df_with_degradation.replace("-", pd.NA)
df_with_degradation = df_with_degradation.dropna(axis=1, how='all')
df_with_degradation["category"] = "with_degradation"

df_without_degradation = df_without_degradation.replace("-", pd.NA)
df_without_degradation = df_without_degradation.dropna(axis=1, how='all')
df_without_degradation["category"] = "without_degradation"

columns_with_degradation = set(df_with_degradation.columns)
columns_without_degradation = set(df_without_degradation.columns)

common_columns = ["Year", "D_Area", "D_AreaAcc", "VR_CO2_1stOrder", "VR_CO2_2ndOrder", "SV_CO2Emission", "SV_CO2Absorption", "NET_CO2_1stOrder", "NET_2nd_Order", "category"]
only_with_degradation = list(columns_with_degradation - columns_without_degradation)
only_without_degradation = list(columns_without_degradation - columns_with_degradation)

columns_final_order = common_columns + only_with_degradation + only_without_degradation

df_with_degradation = df_with_degradation.reindex(columns=columns_final_order)
df_without_degradation = df_without_degradation.reindex(columns=columns_final_order)


df = pd.concat([df_without_degradation, df_with_degradation], ignore_index=True)

df = df.convert_dtypes()

# Save processed Dataframe
df.to_csv("../data/processed/inpe_data_processed.csv", index = False, sep = ';')