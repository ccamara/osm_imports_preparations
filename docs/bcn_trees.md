# Barcelona's Trees Import documentation

## Goals

The goal is to manually merge and import all the trees' information provided by Barcelona City Council, while testing the scripts for data preparation.

## Data Sources

Two datasets provided by Barcelona City Council will be used:

* [Arbrat viari](https://opendata-ajuntament.barcelona.cat/data/ca/dataset/arbrat-viari): Name of the species and geolocation of the trees of the city of Barcelona located on public roads. The information contains, among other data, the scientific name, the common name, the height, the direction and the width of the sidewalk... The trees of the parks are not included. The coordinates are expressed in the ETRS89 reference system. This dataset complemens of Zone trees of the city of Barcelona.
Historical resources which contain data available until the last week of the term are published. The resources are ordered by year and term, information that can be found in the name of the resource.
* [Arbrat zona](https://opendata-ajuntament.barcelona.cat/data/ca/dataset/arbrat-zona): Name of the species and geolocation of the trees of the city of Barcelona located on public roads. The information contains, among other data, the scientific name, the common name, the height, the direction and the width of the sidewalk... The trees of the parks are not included. The coordinates are expressed in the ETRS89 reference system. This dataset complemens of Street trees of the city of Barcelona.
Historical resources which contain data available until the last week of the term are published. The resources are ordered by year and term, information that can be found in the name of the resource.

### Licence

We have an express authorization from the Barcelona city council for the reuse of open data published on theirs open Government website

![](https://wiki.openstreetmap.org/w/images/thumb/9/9a/201801107_AcordOSM_AjuntamentBarcelona_Def.pdf/page1-1240px-201801107_AcordOSM_AjuntamentBarcelona_Def.pdf.jpg)


## Import type

This import will be done manually, using JOSM to edit the data. Consider using Task Manager.

## Data preparations

All data preparations will be made automatically by the scripts within this repository. More specifically from `import_bcn_trees.py`, which in turn imports the functions defined in `src/features/bcn_trees.py` aimed to convert original tagging into OSM tagging (for a complete documentation of those functions, please refer to the [API Documentation]()).

Tagging Conversion table:

Original field  | Description  | OSM tagging  |  Comments
----------------|--------------|--------------|------------
`CODI` | Internal ID  | Not currently imported  | Consider importing it, as it may be useful for future data updates.
`X_ETRS89`  | X coordinates, ETRS89 format  | | Not imported
`Y_ETRS89`  | Y coordinates, ETRS89 format  | | Not imported
`LATITUD_WGS84`  | Latitude coordinates, WGS84 format  |   | Geometry information. No tagging used.
`LONGITUD_WGS84`  | Longitude coordinates, WGS84 format  |   | Geometry information. No tagging used.  |   |   |    |   |   |   |   |   |
`TIPUS_ELEMENT`  | Object's type (viari/zona)  |  | Not imported
`ESPAI VERD`  | Name of Green space where the tree is located   |   | Not imported
`ADRECA`  | Address  |   | Not imported
`ALCADA`  | Tree's height. It does not use meters, but categories  | `height`  | height is calculated according to tree's category, following [this documentation](https://ajuntament.barcelona.cat/ecologiaurbana/sites/default/files/Plagestioarbratviaribcn_cat.pdf) (p. 22).
`CAT_ESPECIE_ID`  | Species' ID  |   | Not imported
`NOM_CIENTIFIC`  | scientific name of the species (popularly known as the Latin name)  | `species`  |
`NOM_CASTELLA`  | Name in Spanish  | `species:es`   |
`NOM_CATALA`  | Name in Catalan  | `species:ca`  |
`CATEGORIA_ARBRAT`  | Tree's category. Internal classification according to height and diameter.  | `diameter`  | Not directly imported, but used to calculate `height` and `diameter`, following [this documentation](https://ajuntament.barcelona.cat/ecologiaurbana/sites/default/files/Plagestioarbratviaribcn_cat.pdf) (p. 19 and 22).
`AMPLADA_VORERA`  | Sidewalk's width  |   | Not imported.
`DATA_PLANTACIO`  | Date in which the tree was planted  | `planted_date`  |
`TIPUS_AIGUA`  | Water type  |   | Not imported.
`TIPUS_REG`  | Watering mechanism  |   | Not imported.
`TIPUS_SUPERFICIE`  | Surface type  |   | Not imported.
`TIPUS_SUPORT`  | Support type  |   | Not imported.
`COBERTURA_ESCOCELL`  | Whether the Tree pit is covered or not  |   | Not currently imported due to lack of specific tagging, but it would be a nice have to feature.
`MIDA_ESCOCELL`  | Tree pit Size  |   | Not currently imported due to lack of specific tagging, but it would be a nice have to feature.

Also, a `source=Opendata Ajuntament de Barcelona` will be added automatically to all the trees.

## Import workflow

1. Run `import_bcn_trees.py` to prepare a single CSV file with all the converted tagging, as specified before. This step only needs to be run once.
2. Use the CSV file generated in the previous step as datasource.
3. Create a project in task manager (TODO)


### Changesets' tagging

We will use the following changeset tags:

* comment=#Ajuntament de Barcelona Trees' import
* import=yes
* source=Ajuntament de Barcelona
* source:date=* the same that in the dataset
* url= (this page)


## References

* [Import Guidelines](https://wiki.openstreetmap.org/wiki/Import/Guidelines)
* [Procedimiento para preparar importaciones](https://wiki.openstreetmap.org/wiki/ES:Importaci%C3%B3n/Directrices) (in Spanish)
* [Sample import documentation project](https://wiki.openstreetmap.org/wiki/Import_information_and_care_points_for_women_and_LGTBI_collectives_in_Catalunya) (thanks Lanxana!)
