# %%
import pandas as pd

# Load raw data

# Load data
def load_data():
    df_without_degradation = pd.read_excel("../data/raw/inpe_EM_BRAmz_results.xlsx", sheet_name="Sem degracação", skiprows=10)
    df_with_degradation = pd.read_excel("../data/raw/inpe_EM_BRAmz_results.xlsx", sheet_name="Com degradação", skiprows=10)

    return df_without_degradation, df_with_degradation

# Data Cleaning
def cleaning(df_without_degradation, df_with_degradation):
    
    df_with_degradation = df_with_degradation.replace("-", pd.NA)
    df_with_degradation = df_with_degradation.dropna(axis=1, how='all')
    df_with_degradation["category"] = "with_degradation"

    df_without_degradation = df_without_degradation.replace("-", pd.NA)
    df_without_degradation = df_without_degradation.dropna(axis=1, how='all')
    df_without_degradation["category"] = "without_degradation"


    # Set columns
    columns_with_degradation = set(df_with_degradation.columns)
    columns_without_degradation = set(df_without_degradation.columns)


    # Define common columns
    common_columns = ["Year", "D_Area", "D_AreaAcc", "VR_CO2_1stOrder", "VR_CO2_2ndOrder", "SV_CO2Emission", "SV_CO2Absorption", "NET_CO2_1stOrder", "NET_2nd_Order", "category"]


    # Unique columns in each dataset
    only_with_degradation = list(columns_with_degradation - columns_without_degradation)


    only_without_degradation = list(columns_without_degradation - columns_with_degradation)


    # Define final column order
    columns_final_order = common_columns + only_with_degradation + only_without_degradation


    # reindex Dataframes
    df_with_degradation = df_with_degradation.reindex(columns=columns_final_order)

    df_without_degradation = df_without_degradation.reindex(columns=columns_final_order)


    # Concatenation into a single Dataframe
    df = pd.concat([df_without_degradation, df_with_degradation], ignore_index=True)


    # Convert data types
    df = df.convert_dtypes()

    return df

# Save processed Dataframe
def save(df):
    df.to_csv("../data/processed/inpe_data_processed.csv", index = False, sep = ';')


def main():
    df_without_degradation, df_with_degradation = load_data()
    df = cleaning(df_without_degradation, df_with_degradation)
    save(df)

if __name__ == "__main__":
    main()