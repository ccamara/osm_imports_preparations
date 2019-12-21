# Project Setup

This project uses `virtual environments` (see below) to handle all dependencies and follows [cookiecutter datascience](https://drivendata.github.io/cookiecutter-data-science/) structure to keep the repo clean and tidy.

## Virtual environments

Virtual environments are managed by `conda`, which means that you should have [Anaconda distribution](https://www.anaconda.com) installed (Read [installing instructions on their website](https://www.anaconda.com/distribution/))

**Activate virtual environment**

```
conda activate osm_imports_preparations
```

**Deactivate virtual environment:**

```
conda deactivate
```

**Update virtual environment from  `environment.yml`:**

```
conda env update -f environment.yml
```

**Recreate virtual environment from `environment.yml`:**

```
conda env create -f environment.yml
```

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


## Updating Documentation

Documentation is generated using [MkDocs](https://www.mkdocs.org) with some plugins installed (they will all be installed after creating the virtual environment). The live documentation site retrieves two type of documentation:

* Static, manually created `*.md` files: these documents are manually created and stored in `/docs` folder.
* Automatically generated (API): these documents are generated using [`keras-audoc`](https://gabrieldemarmiesse.github.io/keras-autodoc/), which reads inline functions' comments and generates files according to `autogen.py`. (currently not working -visit: https://github.com/keras-team/keras-autodoc/issues/68)

In turn, menu (amongst other things) is defined in `mkdocs.yml` file.

In order to improve documentation you can do the following:

### Editing an existing `.md` file

1. Open the desired `.md` file within `/docs` folder and edit it normally.
2. Save your changes
3. Run `mkdocs serve` and watch your changes in `http://127.0.0.1:8000`
4. Once, you're done editing, press `CTRL-C` to stop the server
5. If you're happy with your changes, run `mkdocs gh-deploy`: a site will be generated and pushed to `gh-pages` branch within this repo. Soon after it will be visible in the live site.

### Creating a new `.md` file

1. Create a `.md` file within `/docs` folder and edit it normally.
2. Save your changes
3. Edit `mkdocs.yml` and add a menu entry pointing to the newly created file.
4.  Run `mkdocs serve` and watch your changes in `http://127.0.0.1:8000`
4. Once, you're done editing, press `CTRL-C` to stop the server
5. If you're happy with your changes, run `mkdocs gh-deploy`: a site will be generated and pushed to `gh-pages` branch within this repo. Soon after it will be visible in the live site.
