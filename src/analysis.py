# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Data Loading
def load_data():
    return pd.read_csv("../data/processed/inpe_data_processed.csv", sep = ";")


# Data Filtering
def  filter_without_degradation(df):
    return df[df["category"]=="without_degradation"]


# Data Aggregation Deforestation
def aggregation_deforestation(df_without_degradation):
    return df_without_degradation.groupby(["category", "Year"])["D_Area"].sum().reset_index()


# Data Aggregation Carbon Emission
def aggregation_carbon_emission(df_without_degradation):
    return df_without_degradation.groupby(["category", "Year"])["VR_CO2_1stOrder"].sum().reset_index()


# Find Max and Min Deforestation
def extremes_deforestation(df_grouped_deforestation):
    max_row = df_grouped_deforestation.loc[df_grouped_deforestation["D_Area"].idxmax()]
    min_row = df_grouped_deforestation.loc[df_grouped_deforestation["D_Area"].idxmin()]

    max_year_deforestation, max_value_deforestation = max_row["Year"], max_row["D_Area"]/1_000_000
    min_year_deforestation, min_value_deforestation = min_row["Year"], min_row["D_Area"]/1_000_000

    return max_year_deforestation, max_value_deforestation, min_year_deforestation, min_value_deforestation


# Find Max and Min Carbon Emission
def extremes_carbon_emission(df_grouped_carbon_emission):
    max_row = df_grouped_carbon_emission.loc[df_grouped_carbon_emission["VR_CO2_1stOrder"].idxmax()]
    min_row = df_grouped_carbon_emission.loc[df_grouped_carbon_emission["VR_CO2_1stOrder"].idxmin()]

    max_year_carbon_emission, max_value_carbon_emission = max_row["Year"], max_row["VR_CO2_1stOrder"]
    min_year_carbon_emission, min_value_carbon_emission = min_row["Year"], min_row["VR_CO2_1stOrder"]

    return max_year_carbon_emission, max_value_carbon_emission, min_year_carbon_emission, min_value_carbon_emission


# Plot Graphic Deforestation Per Year
def plot_graphic_deforestation(df_grouped_deforestation, max_year, max_value, min_year, min_value):
    
    # Create Figure
    plt.figure(figsize=(10,6))

    # Main Line
    plt.plot(df_grouped_deforestation["Year"], df_grouped_deforestation["D_Area"]/ 1_000_000, marker = "o", markersize = 3)

    # Highlight Max and Min
    plt.scatter(max_year, max_value, color = "red", zorder = 3)
    plt.scatter(min_year, min_value, color = "red", zorder = 3)

    # Annotations
    plt.annotate("Peak (1995)", color = "red",xy = (1995, 2.9), xytext = (1999, 2.87), fontsize= 11, arrowprops=dict(color="red",arrowstyle="->", mutation_scale = 20))
    plt.annotate("Minimum (2012)", color = "red",xy = (2012, 0.46), xytext = (1995, 0.45), fontsize= 11, arrowprops=dict(color="red",arrowstyle="->", mutation_scale = 20))

    # Reference Line
    plt.axvline(x=1979, linestyle="--", color="red", alpha=0.5, label = "Data quality improves")

    # Configure axes
    plt.xticks(np.arange(df_grouped_deforestation["Year"].min(), df_grouped_deforestation["Year"].max()+5, 5))
    plt.ticklabel_format(style='plain', axis='y')

    # Titles and Labels
    plt.title("Deforestation in the Brazilian Amazon (1960–2020)", fontsize = 13, fontweight="bold")
    plt.ylabel("Total Deforested Area (Million Ha)" ,fontweight = "bold")

    # Style
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Show plot
    plt.show()


# Plot Graphic Carbon Emission
def plot_graphic_carbon_emission(df_grouped_carbon_emission, max_year_carbon_emission, max_value_carbon_emission, min_year_carbon_emission, min_value_carbon_emission):
    
    # Create Figure
    plt.figure(figsize=(10,6))

    # Main Line
    plt.plot(df_grouped_carbon_emission["Year"], df_grouped_carbon_emission["VR_CO2_1stOrder"], marker = "o", markersize = 3)

    # Highlight Max and Min
    plt.scatter(max_year_carbon_emission, max_value_carbon_emission, color = "red", zorder = 3)
    plt.scatter(min_year_carbon_emission, min_value_carbon_emission, color = "red", zorder = 3)

    # Annotations
    plt.annotate("Peak (1995)", color = "red",xy = (1995, 1600), xytext = (1999, 1589), fontsize= 11, arrowprops=dict(color="red",arrowstyle="->", mutation_scale = 20))
    plt.annotate("Minimum (2012)", color = "red",xy = (2012, 260), xytext = (1995, 240), fontsize= 11, arrowprops=dict(color="red",arrowstyle="->", mutation_scale = 20))

    # Reference Line
    plt.axvline(x=1979, linestyle="--", color="red", alpha=0.5, label = "Data quality improves")

    # Configure axes
    plt.xticks(np.arange(df_grouped_carbon_emission["Year"].min(), df_grouped_carbon_emission["Year"].max()+5, 5))
    plt.ticklabel_format(style='plain', axis='y')

    # Titles and Labels
    plt.title("First Order CO² Emissions in the Brazilian Amazon (1960–2020)", fontsize = 13, fontweight="bold")
    plt.ylabel("Total CO² Emitted(MtCO²/Year)" ,fontweight = "bold")

    # Style
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Show plot
    plt.show()


# Main
def main():
    # load
    df = load_data()

    # filter
    df_without_degradation = filter_without_degradation(df)

    # aggregation
    df_grouped_deforestation = aggregation_deforestation(df_without_degradation)

    df_grouped_carbon_emission = aggregation_carbon_emission(df_without_degradation)

    # extremes 
    max_year_deforestation, max_value_deforestation, min_year_deforestation, min_value_deforestation = extremes_deforestation(df_grouped_deforestation)
    
    max_year_carbon_emission, max_value_carbon_emission, min_year_carbon_emission, min_value_carbon_emission = extremes_carbon_emission(df_grouped_carbon_emission)

    # plot 
    plot_graphic_deforestation(df_grouped_deforestation, max_year_deforestation, max_value_deforestation, min_year_deforestation, min_value_deforestation)

    plot_graphic_carbon_emission(df_grouped_carbon_emission, max_year_carbon_emission, max_value_carbon_emission, min_year_carbon_emission, min_value_carbon_emission)

if __name__ == "__main__":
    main()
    