# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Data Loading
def load_data():
    return pd.read_csv("../data/processed/inpe_data_processed.csv", sep = ";")


# Data Filtering
def filter_without_degradation(df):
    return df[df["category"]=="without_degradation"]

def filter_with_degradation(df):
    return df[df["category"]=="with_degradation"]


# Data Aggregation Deforestation
def aggregation_deforestation(df_without_degradation):
    return df_without_degradation.groupby(["category", "Year"])["D_Area"].sum().reset_index()


# Data Aggregation Carbon Emission
def aggregation_carbon_emission_without_degradation(df_without_degradation):
    return df_without_degradation.groupby(["category", "Year"])["VR_CO2_1stOrder"].sum().reset_index()

def aggregation_carbon_emission_with_degradation(df_with_degradation):
    return df_with_degradation.groupby(["category", "Year"])["VR_CO2_2ndOrder"].sum().reset_index()


# Find Max and Min Deforestation
def extremes_deforestation_without_degradation(df_grouped_deforestation_whithout_degradation):
    max_row = df_grouped_deforestation_whithout_degradation.loc[df_grouped_deforestation_whithout_degradation["D_Area"].idxmax()]
    min_row = df_grouped_deforestation_whithout_degradation.loc[df_grouped_deforestation_whithout_degradation["D_Area"].idxmin()]

    max_year_deforestation_without_degradation, max_value_deforestation_without_degradation = max_row["Year"], max_row["D_Area"]/1_000_000
    min_year_deforestation_without_degradation, min_value_deforestation_without_degradation = min_row["Year"], min_row["D_Area"]/1_000_000

    return max_year_deforestation_without_degradation, max_value_deforestation_without_degradation, min_year_deforestation_without_degradation, min_value_deforestation_without_degradation


# Find Max and Min Carbon Emission Without Degradation
def extremes_carbon_emission_without_degradation(df_grouped_carbon_emission_without_degradation):
    max_row = df_grouped_carbon_emission_without_degradation.loc[df_grouped_carbon_emission_without_degradation["VR_CO2_1stOrder"].idxmax()]
    min_row = df_grouped_carbon_emission_without_degradation.loc[df_grouped_carbon_emission_without_degradation["VR_CO2_1stOrder"].idxmin()]

    max_year_carbon_emission_without_degradation, max_value_carbon_emission_without_degradation = max_row["Year"], max_row["VR_CO2_1stOrder"]
    min_year_carbon_emission_without_degradation, min_value_carbon_emission_without_degradation = min_row["Year"], min_row["VR_CO2_1stOrder"]

    return max_year_carbon_emission_without_degradation, max_value_carbon_emission_without_degradation, min_year_carbon_emission_without_degradation, min_value_carbon_emission_without_degradation


# Find Max and Min Carbon Emission With Degradation
def extremes_carbon_emission_with_degradation(df_grouped_carbon_emission_with_degradation):
    max_row = df_grouped_carbon_emission_with_degradation.loc[df_grouped_carbon_emission_with_degradation["VR_CO2_2ndOrder"].idxmax()]
    min_row = df_grouped_carbon_emission_with_degradation.loc[df_grouped_carbon_emission_with_degradation["VR_CO2_2ndOrder"].idxmin()]

    max_year_carbon_emission_with_degradation, max_value_carbon_emission_with_degradation = max_row["Year"], max_row["VR_CO2_2ndOrder"]
    min_year_carbon_emission_with_degradation, min_value_carbon_emission_with_degradation = min_row["Year"], min_row["VR_CO2_2ndOrder"]

    return max_year_carbon_emission_with_degradation, max_value_carbon_emission_with_degradation, min_year_carbon_emission_with_degradation, min_value_carbon_emission_with_degradation



# Plot Graphic Deforestation Without Degradation Per Year
def plot_graphic_deforestation_without_degradation(df_grouped_deforestation_whithout_degradation, max_year, max_value, min_year, min_value):
    
    # Create Figure
    plt.figure(figsize=(10,6))

    # Main Line
    plt.plot(df_grouped_deforestation_whithout_degradation["Year"], df_grouped_deforestation_whithout_degradation["D_Area"]/ 1_000_000, marker = "o", markersize = 2)

    # Highlight Max and Min
    plt.scatter(max_year, max_value, color = "red", zorder = 3, s=10)
    plt.scatter(min_year, min_value, color = "red", zorder = 3, s=10)

    # Annotations
    plt.annotate("Peak (1995)", color = "red",xy = (1995, 2.9), xytext = (1999, 2.87), fontsize= 11, arrowprops=dict(color="red",arrowstyle="->", mutation_scale = 20))
    plt.annotate("Minimum (2012)", color = "red",xy = (2012, 0.46), xytext = (1995, 0.45), fontsize= 11, arrowprops=dict(color="red",arrowstyle="->", mutation_scale = 20))

    # Reference Line
    plt.axvline(x=1979, linestyle="--", color="red", alpha=0.5, label = "Data quality improves")

    # Configure axes
    plt.xticks(np.arange(df_grouped_deforestation_whithout_degradation["Year"].min(), df_grouped_deforestation_whithout_degradation["Year"].max()+5, 5))
    plt.ticklabel_format(style='plain', axis='y')

    # Titles and Labels
    plt.title("Deforestation in the Brazilian Amazon (1960–2020)", fontsize = 13, fontweight="bold")
    plt.ylabel("Total Deforested Area (Million Ha)" ,fontweight = "bold")

    # Style
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Show plot
    plt.show()



# Plot Graphic Carbon Emission With Degradation
def plot_graphic_carbon_emission_with_degradation(df_grouped_carbon_emission_with_degradation, max_year_carbon_emission_with_degradation, max_value_carbon_emission_with_degradation, min_year_carbon_emission_with_degradation, min_value_carbon_emission_with_degradation):
    
    # Create Figure
    plt.figure(figsize=(10,6))

    # Main Line
    plt.plot(df_grouped_carbon_emission_with_degradation["Year"], df_grouped_carbon_emission_with_degradation["VR_CO2_2ndOrder"], marker = "o", markersize = 2)

    # Highlight Max and Min
    plt.scatter(max_year_carbon_emission_with_degradation, max_value_carbon_emission_with_degradation, color = "red", zorder = 3, s=10)

    plt.scatter(min_year_carbon_emission_with_degradation, min_value_carbon_emission_with_degradation, color = "red", zorder = 3, s=10)

    # Annotations
    plt.annotate("Peak (2004)", color = "red",xy = (2004, 1109), xytext = (1992, 1099), fontsize= 11, arrowprops=dict(color="red",arrowstyle="->", mutation_scale = 20))

    plt.annotate("Minimum (1960)", color = "red",xy = (1960, 129), xytext = (1963, 125), fontsize= 11, arrowprops=dict(color="red",arrowstyle="->", mutation_scale = 20))

    # Configure axes
    plt.xticks(np.arange(df_grouped_carbon_emission_with_degradation["Year"].min(), df_grouped_carbon_emission_with_degradation["Year"].max()+5, 5))
    plt.ticklabel_format(style='plain', axis='y')

    # Titles and Labels
    plt.title("Second Order CO₂ Emissions in the Brazilian Amazon (1960–2020)", fontsize = 13, fontweight="bold")
    plt.ylabel("Total CO₂ Emitted(MtCO₂/Year)" ,fontweight = "bold")

    # Style
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Show plot
    plt.show()

def plot_graphic_comparision_carbon_emission(df_grouped_carbon_emission_without_degradation, max_year_carbon_emission_without_degradation, max_value_carbon_emission_without_degradation, min_year_carbon_emission_without_degradation, min_value_carbon_emission_without_degradation,
df_grouped_carbon_emission_with_degradation, max_year_carbon_emission_with_degradation, max_value_carbon_emission_with_degradation, min_year_carbon_emission_with_degradation, min_value_carbon_emission_with_degradation):

    # Create Figure
    plt.figure(figsize=(10,6))


    # Main Lines
    plt.plot(df_grouped_carbon_emission_without_degradation["Year"], df_grouped_carbon_emission_without_degradation["VR_CO2_1stOrder"], marker = "o", markersize = 2, label= "Without Degradation")

    plt.plot(df_grouped_carbon_emission_with_degradation["Year"], df_grouped_carbon_emission_with_degradation["VR_CO2_2ndOrder"], marker = "o", markersize = 2, label= "With Degradation")


    # Highlight Max and Min Without Degradation
    plt.scatter(max_year_carbon_emission_without_degradation, max_value_carbon_emission_without_degradation, color = "blue", zorder = 3, s=10)
    plt.scatter(min_year_carbon_emission_without_degradation, min_value_carbon_emission_without_degradation, color = "blue", zorder = 3, s=10)


    # Highlight Max and Min With Degradation
    plt.scatter(max_year_carbon_emission_with_degradation, max_value_carbon_emission_with_degradation, color = "red", zorder = 3, s=10)
    plt.scatter(min_year_carbon_emission_with_degradation, min_value_carbon_emission_with_degradation, color = "red", zorder = 3, s=10)

    # Fill Area Between Curves
    plt.fill_between(
    df_grouped_carbon_emission_with_degradation["Year"],
    df_grouped_carbon_emission_with_degradation["VR_CO2_2ndOrder"],
    df_grouped_carbon_emission_without_degradation["VR_CO2_1stOrder"],
    where=(
        df_grouped_carbon_emission_without_degradation["VR_CO2_1stOrder"] >
        df_grouped_carbon_emission_with_degradation["VR_CO2_2ndOrder"]
    ),
    alpha=0.2,
    label="Extra emissions from degradation"
    )

    # Annotations
    plt.annotate("Peak (1995)", color = "red",xy = (1995, 1595), xytext = (1999, 1592), fontsize= 11, arrowprops=dict(color="red",arrowstyle="->", mutation_scale = 20))

    plt.annotate("Minimum (1960)", color = "red",xy = (1960, 133), xytext = (1963, 125), fontsize= 11, arrowprops=dict(color="red",arrowstyle="->", mutation_scale = 20))

    # Titles and Labels
    plt.title("CO₂ Emissions: With vs. Without Degradation (1960–2020)", fontsize = 13, fontweight="bold")
    plt.ylabel("Total CO₂ Emitted(MtCO₂/Year)" ,fontweight = "bold")


    #  Style
    plt.grid(True, alpha=0.3)
    plt.legend()


    # Show plot
    plt.show()
    

def plot_graphic_deforestation_carbon_emission(df_grouped_deforestation_whithout_degradation, max_year, max_value, min_year, min_value,df_grouped_carbon_emission_with_degradation, max_year_carbon_emission_with_degradation, max_value_carbon_emission_with_degradation, min_year_carbon_emission_with_degradation, min_value_carbon_emission_with_degradation):

    # Create Figure
    fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)


    # Main Lines
    axs[0].plot(
        df_grouped_deforestation_whithout_degradation["Year"],
        df_grouped_deforestation_whithout_degradation["D_Area"] / 1_000_000,
        marker="o", markersize=2
    )

    axs[1].plot(
        df_grouped_carbon_emission_with_degradation["Year"],
        df_grouped_carbon_emission_with_degradation["VR_CO2_2ndOrder"],
        marker="o", markersize=2, color="orange"
    )


    # Reference Lines
    for ax in axs:
        ax.axvline(x=1979, linestyle="--", color="red", alpha=0.5)


    # Highlight Max and Min
    axs[0].scatter(max_year, max_value, color = "red", zorder = 3, s=10)
    axs[0].scatter(min_year, min_value, color = "red", zorder = 3, s=10)

    axs[1].scatter(max_year_carbon_emission_with_degradation, max_value_carbon_emission_with_degradation, color = "red", zorder = 3, s=10)
    axs[1].scatter(min_year_carbon_emission_with_degradation, min_value_carbon_emission_with_degradation, color = "red", zorder = 3, s=10)


    # Titles and Labes
 

    axs[0].set_title("Deforestation in the Brazilian Amazon (1960–2020)", fontsize = 13, fontweight = 'bold')
    axs[0].set_ylabel("Total Deforested Area (Million Ha)" ,fontweight = "bold")
    
    axs[1].set_title("Second Order CO₂ Emissions in the Brazilian Amazon (1960–2020)", fontsize = 13, fontweight = 'bold')
    axs[1].set_ylabel("Total CO₂ Emitted(MtCO₂/Year)" ,fontweight = "bold")


    # Style
    axs[0].grid(True, alpha=0.3)
    axs[1].grid(True, alpha=0.3)


    # Show plot
    plt.show()


# Main
def main():
    # load
    df = load_data()

    # filter
    df_with_degradation = filter_with_degradation(df)
    df_without_degradation = filter_without_degradation(df)

    # aggregation
    df_grouped_deforestation_whithout_degradation = aggregation_deforestation(df_without_degradation)

    df_grouped_carbon_emission_without_degradation = aggregation_carbon_emission_without_degradation(df_without_degradation)

    df_grouped_carbon_emission_with_degradation = aggregation_carbon_emission_with_degradation(df_with_degradation)

    # extremes
    max_year_deforestation_without_degradation, max_value_deforestation_without_degradation, min_year_deforestation_without_degradation, min_value_deforestation_without_degradation = extremes_deforestation_without_degradation(df_grouped_deforestation_whithout_degradation)
    
    max_year_carbon_emission_without_degradation, max_value_carbon_emission_without_degradation, min_year_carbon_emission_without_degradation, min_value_carbon_emission_without_degradation = extremes_carbon_emission_without_degradation(df_grouped_carbon_emission_without_degradation)

    
    max_year_carbon_emission_with_degradation, max_value_carbon_emission_with_degradation, min_year_carbon_emission_with_degradation, min_value_carbon_emission_with_degradation = extremes_carbon_emission_with_degradation(df_grouped_carbon_emission_with_degradation)

    # plot 
    plot_graphic_deforestation_without_degradation(df_grouped_deforestation_whithout_degradation, max_year_deforestation_without_degradation, max_value_deforestation_without_degradation, min_year_deforestation_without_degradation, min_value_deforestation_without_degradation)

    plot_graphic_carbon_emission_with_degradation(df_grouped_carbon_emission_with_degradation, max_year_carbon_emission_with_degradation, max_value_carbon_emission_with_degradation, min_year_carbon_emission_with_degradation, min_value_carbon_emission_with_degradation)

    plot_graphic_comparision_carbon_emission(df_grouped_carbon_emission_without_degradation, max_year_carbon_emission_without_degradation, max_value_carbon_emission_without_degradation, min_year_carbon_emission_without_degradation, min_value_carbon_emission_without_degradation,df_grouped_carbon_emission_with_degradation, max_year_carbon_emission_with_degradation, max_value_carbon_emission_with_degradation, min_year_carbon_emission_with_degradation, min_value_carbon_emission_with_degradation)

    plot_graphic_deforestation_carbon_emission(df_grouped_deforestation_whithout_degradation, max_year_deforestation_without_degradation, max_value_deforestation_without_degradation, min_year_deforestation_without_degradation, min_value_deforestation_without_degradation,df_grouped_carbon_emission_with_degradation, max_year_carbon_emission_with_degradation, max_value_carbon_emission_with_degradation, min_year_carbon_emission_with_degradation, min_value_carbon_emission_with_degradation)


if __name__ == "__main__":
    main()
    
# %%
