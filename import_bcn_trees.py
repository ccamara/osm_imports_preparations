# -*- coding: utf-8 -*-

import pandas as pd
import wget

from src.features import bcn_trees


# %% Data download.

url = 'https://opendata-ajuntament.barcelona.cat/data/dataset/27b3f8a7-e536-4eea-b025-ce094817b2bd/resource/28034af4-b636-48e7-b3df-fa1c422e6287/download'
wget.download(url, 'data/raw/arbrat_viari.csv')


# %% Data preparations according to OSM Wiki on natural=tree
# https://wiki.openstreetmap.org/wiki/Tag:natural%3Dtree

bcn_arbrat_viari_raw = pd.read_csv('data/raw/arbrat_viari.csv')

bcn_arbrat_viari = bcn_trees.data_munging(bcn_arbrat_viari_raw, 'arbrat_viari')


print(bcn_arbrat_viari.dtypes)
print(bcn_arbrat_viari['species:ca'].unique())


# %% Arbrat zones

url = "https://opendata-ajuntament.barcelona.cat/data/dataset/9b525e1d-13b8-48f1-abf6-f5cd03baa1dd/resource/8f2402dd-72dc-4b07-8145-e3f75004b0de/download"
wget.download(url, 'data/raw/arbrat_zona.csv')

bcn_arbrat_zona_raw = pd.read_csv('data/raw/arbrat_zona.csv')

bcn_arbrat_zona = bcn_trees.data_munging(bcn_arbrat_zona_raw, 'arbrat_zona')

# Combine dataframes into a single one
bcn_trees_df = pd.concat([bcn_arbrat_viari, bcn_arbrat_zona])


print(bcn_trees_df.dtypes)
print(bcn_trees_df['species:ca'].unique())
