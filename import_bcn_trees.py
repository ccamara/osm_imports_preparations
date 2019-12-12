# -*- coding: utf-8 -*-

import pandas as pd
import wget

import build_features


# %% Data download.

url = 'https://opendata-ajuntament.barcelona.cat/data/dataset/27b3f8a7-e536-4eea-b025-ce094817b2bd/resource/28034af4-b636-48e7-b3df-fa1c422e6287/download'
wget.download(url, 'data/raw/arbrat_viari.csv')


# %% Data preparations according to OSM Wiki on natural=tree
# https://wiki.openstreetmap.org/wiki/Tag:natural%3Dtree

bcn_arbrat_viari_raw = pd.read_csv('data/raw/arbrat_viari.csv')

bcn_trees = build_features.trees_data_munging(bcn_arbrat_viari_raw)


# %%% Test

# Select columns.
df = bcn_arbrat_viari_raw[['LATITUD_WGS84',
                    'LONGITUD_WGS84',
                    'NOM_CIENTIFIC',
                    'NOM_CASTELLA',
                    'NOM_CATALA',
                    'DATA_PLANTACIO',
                    'CATEGORIA_ARBRAT',
                    ]]

# Rename
df = df.rename(columns={'NOM_CIENTIFIC': 'species',
                        'NOM_CASTELLA': 'species:es',
                        'NOM_CATALA': 'species:ca',
                        'DATA_PLANTACIO': 'planted_date'})


# @TODO: Populate leaf_cycle column according to species
# https://wiki.openstreetmap.org/wiki/Key:leaf_cycle

# @TODO: convert 'CATEGORIA' into height or diameter, according to city
# council's guide: https://ajuntament.barcelona.cat/ecologiaurbana/sites/default/files/Plagestioarbratviaribcn_cat.pdf

# @TODO: Tag tree pits for accessibility purposes.

# @TODO: Consider importing city council's IDs for updating purposes.

# Create a source column with "Opendata Ajuntament Barcelona"
df['source'] = "Opendata Ajuntament de Barcelona"
