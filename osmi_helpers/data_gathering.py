#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script is aimed to define all functions required to import and manipulate
generic data into osm.

@author: ccamara
"""

import pandas as pd


def csv_parser(df, mapping_csv):
    """Selects and renames columns according to a CSV file that defines the
    parsing rules.

    Arguments:
    ---------

        ``df``: DataFrame
            The Raw Dataframe we want to use import into OSM.

        ``mapping_csv``: String
            The path pointing to a CSV with the parsing rules. The CSV must
            have the following columns: `Original field`, `Description`,
            `OSM tagging`, `Comments`, otherwise the function will not work.
.

    Returns:
    --------

        ``df``: A clean dataframe, ready for importing to OSM.

    """

    # Let's extract information from the CSV with the fields' mapping.
    # This information will be used to manipulate the original data according
    # to the parsing rules described in the CSV file.
    df_mapping = pd.read_csv(mapping_csv)

    df_mapping = df_mapping.rename(columns={'Original field': 'original_field',
                                            'OSM tagging': 'osm_tagging'})

    # Select only fields that are going to be imported into OSM, this is only
    # those which have some kind of value in the `osm_tagging` column.
    df_mapping.dropna(subset=['osm_tagging'], inplace=True)

    # We will only use two columns: original_field and osm_tagging.
    df_mapping = df_mapping[['original_field', 'osm_tagging']]

    # Generate a series from all values within the original field.
    # This series will be used for selecting columns on de data dataframe.
    selected_columns = df_mapping.loc[:, 'original_field']

    # Generate a dictionary with the original fields' names and their
    # equivalents in OSM tagging.
    parsing_dict = df_mapping.to_dict(orient='dict')

    parsing_dict = pd.Series(df_mapping.osm_tagging.values,
                             index=df_mapping.original_field).to_dict()

    # Now we start with the dataframe manipulations.

    # Select columns that will be parsed, according to the CSV file.
    df = df[selected_columns]

    # Rename columns
    df = df.rename(columns=parsing_dict)

    return(df)


def test_function(parameter):
    """
    This is a sample test function for testing documentation purposes.

    Parameters
    ----------
    parameter : TYPE
        This is some text here describing the `parameter`.

    Returns
    -------
    parameter.

    """
    return(parameter)
