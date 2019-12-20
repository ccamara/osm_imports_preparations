"""Barcelona City Council's Trees imports.

This script is aimed to define all functions required to import data regarding
trees from Barcelona's OpenData portal.
"""


import wget


def data_download(url, filename):
    """Downloads data and stores it into a file"""
    wget.download(url, 'data/raw/' + filename + '.csv')


def data_munging(df, file_name):
    """Cleans and prepares data from Barcelona City Council Opendata
    for importing trees' information into OSM, provided a dataframe.
    Stores the resulting dataframe into a csv file.

    Parameters
    ----------
    df : DataFrame
        The Raw Dataframe we want to use import into OSM.

    file_name : String
        The name we want to give to the resulting csv export.


    Returns
    -------
    df
        A clean dataframe, ready for importing to OSM.

    """

    print('Loading dataframe...')

    # Select columns.
    df = df[['LATITUD_WGS84',
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

    # Convert columns into categories (R's factors)
    # https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html
    df["species"] = df["species"].astype("category")
    df["species:ca"] = df["species:ca"].astype("category")

    # @TODO: Populate leaf_cycle column according to species
    # https://wiki.openstreetmap.org/wiki/Key:leaf_cycle

    # @TODO: convert 'CATEGORIA' into height or diameter, according to city
    # council's guide: https://ajuntament.barcelona.cat/ecologiaurbana/sites/default/files/Plagestioarbratviaribcn_cat.pdf

    # @TODO: Tag tree pits for accessibility purposes.

    # @TODO: Consider importing city council's IDs for updating purposes.

    # Create a source column with "Opendata Ajuntament Barcelona"
    df['source'] = "Opendata Ajuntament de Barcelona"

    df.to_csv('data/processed/' + file_name + '.csv', sep='\t',
              encoding='utf-8')

    return(df)
