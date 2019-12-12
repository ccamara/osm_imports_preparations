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

bcn_trees_df = bcn_trees.data_munging(bcn_arbrat_viari_raw)
