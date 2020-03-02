# %% Dependencies and variables' definitions.

import pandas as pd
import geopandas as gpd
from osmi_helpers import data_gathering as osmi_dg

# Define Data Sources

ARBRAT_VIARI_URL = "https://opendata-ajuntament.barcelona.cat/data/dataset/27b3f8a7-e536-4eea-b025-ce094817b2bd/resource/28034af4-b636-48e7-b3df-fa1c422e6287/download"
ARBRAT_ZONA_URL = "https://opendata-ajuntament.barcelona.cat/data/dataset/9b525e1d-13b8-48f1-abf6-f5cd03baa1dd/resource/8f2402dd-72dc-4b07-8145-e3f75004b0de/download"

CSV_PARSER = 'fields_mapping.csv'

# %% [markdown]
# # Barcelona Trees' import.
#
# ## Goals¶
#
# The goal is to manually merge and import all the trees' information provided by Barcelona City Council, while testing the scripts for data preparation.
#
# ## Data Sources¶
#
# Two datasets provided by Barcelona City Council will be used:
#
# * [Arbrat viari](https://opendata-ajuntament.barcelona.cat/data/ca/dataset/arbrat-viari): Name of the species and geolocation of the trees of the city of Barcelona located on public roads. The information contains, among other data, the scientific name, the common name, the height, the direction and the width of the sidewalk... The trees of the parks are not included. The coordinates are expressed in the ETRS89 reference system. This dataset complemens of Zone trees of the city of Barcelona. Historical resources which contain data available until the last week of the term are published. The resources are ordered by year and term, information that can be found in the name of the resource.
# * [Arbrat zona](https://opendata-ajuntament.barcelona.cat/data/ca/dataset/arbrat-zona): Name of the species and geolocation of the trees of the city of Barcelona located on public roads. The information contains, among other data, the scientific name, the common name, the height, the direction and the width of the sidewalk... The trees of the parks are not included. The coordinates are expressed in the ETRS89 reference system. This dataset complemens of Street trees of the city of Barcelona. Historical resources which contain data available until the last week of the term are published. The resources are ordered by year and term, information that can be found in the name of the resource.
#
# ## License
#
# We have an express authorization from the Barcelona city council for the reuse of open data published on theirs open Government website
#
# ![](https://wiki.openstreetmap.org/w/images/thumb/9/9a/201801107_AcordOSM_AjuntamentBarcelona_Def.pdf/page1-1240px-201801107_AcordOSM_AjuntamentBarcelona_Def.pdf.jpg)
#
# ## Import type¶
#
# This import will be done manually, using JOSM to edit the data. Consider using Task Manager.
#
# ## Data preparations¶
#
# All data preparations will be made automatically in this notebook.
#
# ### Fields' mapping.


# %% Read CSV file with fields' mapping and description.

fields_mapping = pd.read_csv(CSV_PARSER)

# Display table.
fields_mapping

# %% [markdown]

# ## Import script.

# ### Data Gathering

# %% Data Gathering

# Download a file and convert it into a dataframe.
df_aviari = pd.read_csv(ARBRAT_VIARI_URL)
df_azona = pd.read_csv(ARBRAT_ZONA_URL)

# Combine both data sources into a single one.
df_raw = pd.concat([df_aviari, df_azona])

df_raw


# %% Conversion process

# Selects and renames fields according to CSV parser.
df = osmi_dg.csv_parser(df_raw, CSV_PARSER)

# Calculate some fields.

# Create genus column
df['genus'] = df['species'].str.split().str[0]

# Convert columns into categories (R's factors)
# https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html
# When converted to categories, export to Geojson does not work.
# df["species"] = df["species"].astype("category")
# df["species:ca"] = df["species:ca"].astype("category")

# TODO: Populate leaf_cycle column according to species
# https://wiki.openstreetmap.org/wiki/Key:leaf_cycle

# Calculate height, according to city council's guide:
# https://ajuntament.barcelona.cat/ecologiaurbana/sites/default/files/Plagestioarbratviaribcn_cat.pdf (p. 22)
df.loc[df.height == "PETITA", 'height'] = 5
df.loc[df.height == "MITJANA", 'height'] = 10
df.loc[df.height == "GRAN", 'height'] = 15
df.loc[df.height == "EXEMPLAR", 'height'] = 20


# Convert 'CATEGORIA' into circumference, according to city council's
# guide: https://ajuntament.barcelona.cat/ecologiaurbana/sites/default/files/Plagestioarbratviaribcn_cat.pdf (p. 19)
df.loc[df.circumference == "PRIMERA", 'circumference'] = 0.4
df.loc[df.circumference == "SEGONA", 'circumference'] = 0.8
df.loc[df.circumference == "TERCERA", 'circumference'] = 1.1
df.loc[df.circumference == "EXEMPLAR", 'circumference'] = 1.5

# TODO: Tag tree pits for accessibility purposes.

# Create a source column with "Opendata Ajuntament Barcelona"
df['source'] = "Opendata Ajuntament de Barcelona"

df.head(10)

# %% 

# Convert dataframe into a GeoDataframe.
gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df.lon, df.lat))


# Export to geojson.
gdf.to_file("data/processed/bcn_trees.geojson", driver='GeoJSON')

# TODO: do not export null values.
# TODO: drop latitude and longitude fields.


# %%
