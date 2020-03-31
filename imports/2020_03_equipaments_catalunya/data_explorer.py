# %%

import pandas as pd
import geopandas as gpd

# Define Data Sources
DATA_RAW = 'data/raw/Equipaments_de_Catalunya.csv'
CSV_PARSER = 'fields_mapping.csv'

# Download a file and convert it into a dataframe.
df_raw = pd.read_csv(DATA_RAW)

df_raw.head()




# %%

# Display unique values
df_raw.CATEGORIA.unique()

# %%
# Filter out entries without category
df_raw = df_raw.dropna(subset=['CATEGORIA'])

df_raw
# %% Museums

df_museums = df_raw[df_raw['CATEGORIA'].str.contains("Museus")]

df_museums

# %%

df_libraries = df_raw[df_raw['CATEGORIA'].str.contains("Biblioteques")]

df_libraries


# %%
df_civic = df_raw[df_raw['CATEGORIA'].str.contains("Equipaments cívics")]

df_civic

# %%  Geopandas

gdf = gpd.read_file("data/raw/Equipaments de Catalunya.geojson")

gdf.head(10)

# %%
gdf.head(10)

# %%
# Filter out entries without category
gdf = gdf.dropna(subset=['categoria'])

type(gdf)

gdf

# %%
