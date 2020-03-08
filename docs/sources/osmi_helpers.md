### csv_parser function


```python
osmi_helpers.data_gathering.csv_parser(df, mapping_csv)
```


Selects and renames columns according to a CSV file that defines the
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

    


----

