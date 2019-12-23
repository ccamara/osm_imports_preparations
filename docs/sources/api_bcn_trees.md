### data_download function


```python
src.features.bcn_trees.data_download(url, filename)
```


Downloads data and stores it into a file

----

### data_munging function


```python
src.features.bcn_trees.data_munging(df, file_name)
```


Cleans and prepares data from Barcelona City Council Opendata
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

----

