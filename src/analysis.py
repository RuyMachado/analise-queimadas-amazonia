# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Data Loading
def load_data():
    return pd.read_csv("../data/processed/inpe_data_processed.csv", sep = ";")


# Data Filtering
def filter(df):
    return df[df["category"]=="with_degradation"]


# Data Aggregation
def aggregation(df_with_degradation):
    return df_with_degradation.groupby(["category", "Year"])["D_Area"].sum().reset_index()


# Find Max and Min
def extremes(df_grouped):
    max_row = df_grouped.loc[df_grouped["D_Area"].idxmax()]
    min_row = df_grouped.loc[df_grouped["D_Area"].idxmin()]

    max_year, max_value = max_row["Year"], max_row["D_Area"]/1_000_000
    min_year, min_value = min_row["Year"], min_row["D_Area"]/1_000_000

    return max_year, max_value, min_year, min_value


# Plot Graphic
def plot_graphic(df_grouped, max_year, max_value, min_year, min_value):
    
    # Create Figure
    plt.figure(figsize=(10,6))

    # Main Line
    plt.plot(df_grouped["Year"], df_grouped["D_Area"]/ 1_000_000, marker = "o", markersize = 3)

    # Highlight Max and Min
    plt.scatter(max_year, max_value, color = "red", zorder = 3)
    plt.scatter(min_year, min_value, color = "red", zorder = 3)


    # Annotations
    plt.annotate("Peak (1995)", color = "red",xy = (1995, 2.9), xytext = (1999, 2.87), fontsize= 11, arrowprops=dict(color="red",arrowstyle="->", mutation_scale = 20))
    plt.annotate("Minimum (2012)", color = "red",xy = (2012, 0.46), xytext = (1995, 0.45), fontsize= 11, arrowprops=dict(color="red",arrowstyle="->", mutation_scale = 20))


    # Reference Line
    plt.axvline(x=1979, linestyle="--", color="red", alpha=0.5, label = "Data quality improves")


    # Configure axes
    plt.xticks(np.arange(df_grouped["Year"].min(), df_grouped["Year"].max()+5, 5))
    plt.ticklabel_format(style='plain', axis='y')


    # Titles and Labels
    plt.title("Deforestation in the Amazon (1960–2020)", fontsize = 13, fontweight="bold")
    plt.ylabel("Total Deforested Area (Million Ha)" ,fontweight = "bold")


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
    df_with_degradation = filter(df)

    # aggregation
    df_grouped = aggregation(df_with_degradation)

    # extremes
    max_year, max_value, min_year, min_value = extremes(df_grouped)

    # plot 
    plot_graphic(df_grouped, max_year, max_value, min_year, min_value)


if __name__ == "__main__":
    main()
    