"""Barcelona City Council's Trees imports.

This script is aimed to define all functions required to import data regarding
trees from Barcelona's OpenData portal.

  Typical usage example:

  df = bcn_trees.data_muning()
"""


import wget


def data_download(url, filename):
    """Downloads data and stores it into a file"""
    wget.download(url, 'data/raw/' + filename + '.csv')


def data_munging(df, file_name):
    """Cleans and prepares data from Barcelona City Council Opendata
    for importing trees' information into OSM, provided a dataframe.
    Stores the resulting dataframe into a csv file.

    Tagging conversion has been made following `Tag:natural=tree <https://wiki.openstreetmap.org/wiki/Tag:natural%3Dtree>`_ in OSM Wiki.

    Arguments:
    ---------

        ``df``: DataFrame
            The Raw Dataframe we want to use import into OSM.

        ``file_name``: String
            The name we want to give to the resulting csv export.

    Returns:
    --------

        ``df``: A clean dataframe, ready for importing to OSM.

        ``csv file``, stored in ``/data/processed`` folder and named after
        ``file_name``

    """

    print('Preparing dataframe...')

    # Select columns.
    df = df[['LATITUD_WGS84',
             'LONGITUD_WGS84',
             'NOM_CIENTIFIC',
             'NOM_CASTELLA',
             'NOM_CATALA',
             'DATA_PLANTACIO',
             'CATEGORIA_ARBRAT',
             'ALCADA',
             'CODI'
             ]]

    # Tagging conversion using natural=Tree OSM wiki as a reference:
    # https://wiki.openstreetmap.org/wiki/Tag:natural%3Dtree

    # Rename columns
    df = df.rename(columns={'LATITUD_WGS84': 'latitude',
                            'LONGITUD_WGS84': 'longitude',
                            'NOM_CIENTIFIC': 'species',
                            'NOM_CASTELLA': 'species:es',
                            'NOM_CATALA': 'species:ca',
                            'DATA_PLANTACIO': 'planted_date',
                            'CODI': 'source:pkey'
                            })

    # Create genus column
    df['genus'] = df['species'].str.split().str[0]

    # Convert columns into categories (R's factors)
    # https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html
    df["species"] = df["species"].astype("category")
    df["species:ca"] = df["species:ca"].astype("category")

    # TODO: Populate leaf_cycle column according to species
    # https://wiki.openstreetmap.org/wiki/Key:leaf_cycle

    # Convert 'ALCADA' into height, according to city council's guide:
    # https://ajuntament.barcelona.cat/ecologiaurbana/sites/default/files/Plagestioarbratviaribcn_cat.pdf (p. 22)
    df["ALCADA"] = df["ALCADA"].astype("category")

    df.loc[df.ALCADA == "PETITA", 'height'] = 5
    df.loc[df.ALCADA == "MITJANA", 'height'] = 10
    df.loc[df.ALCADA == "GRAN", 'height'] = 15
    df.loc[df.ALCADA == "EXEMPLAR", 'height'] = 20

    # Convert 'CATEGORIA' into circumference, according to city council's
    # guide: https://ajuntament.barcelona.cat/ecologiaurbana/sites/default/files/Plagestioarbratviaribcn_cat.pdf (p. 19)
    df["CATEGORIA_ARBRAT"] = df["CATEGORIA_ARBRAT"].astype("category")

    df.loc[df.CATEGORIA_ARBRAT == "PRIMERA", 'circumference'] = 0.4
    df.loc[df.CATEGORIA_ARBRAT == "SEGONA", 'circumference'] = 0.8
    df.loc[df.CATEGORIA_ARBRAT == "TERCERA", 'circumference'] = 1.1
    df.loc[df.CATEGORIA_ARBRAT == "EXEMPLAR", 'circumference'] = 1.5

    # TODO: Tag tree pits for accessibility purposes.

    # Drop unused intermediate columns.
    df = df.drop(columns=['CATEGORIA_ARBRAT', 'ALCADA'])

    # Create a source column with "Opendata Ajuntament Barcelona"
    df['source'] = "Opendata Ajuntament de Barcelona"

    print('Dataframe created. Saving it into a CSV file...')

    df.to_csv('data/processed/' + file_name + '.csv', sep='\t',
              encoding='utf-8')

    return(df)
