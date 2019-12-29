# OpenStreetMap Imports preparations

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->


This is a proof of concept and a pet project for learning python while preparing data for importing it to [OpenStreetMap](https://openstreetmap.org). Although I will start small (importing trees from Barcelona city council), I aim to set the foundations for adding other types of imports that may (or may not) be added in the future, hopefully with other people's contributions.

## Documentation

Project's documentation can be found in `docs` folder and a live version, generated using [mkdocs](https://www.mkdocs.org/), can be found [here](https://osmimports.mapcolabora.org)



## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://carloscamara.es"><img src="https://avatars1.githubusercontent.com/u/706549?v=4" width="100px;" alt=""/><br /><sub><b>Carlos Cámara</b></sub></a><br /><a href="https://github.com/mapcolabora/osm_imports_preparations/commits?author=ccamara" title="Code">💻</a> <a href="https://github.com/mapcolabora/osm_imports_preparations/commits?author=ccamara" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/msevilla00"><img src="https://avatars2.githubusercontent.com/u/1491985?v=4" width="100px;" alt=""/><br /><sub><b>Miguel Sevilla-Callejo</b></sub></a><br /><a href="https://github.com/mapcolabora/osm_imports_preparations/commits?author=msevilla00" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/gabrieldemarmiesse"><img src="https://avatars1.githubusercontent.com/u/12891691?v=4" width="100px;" alt=""/><br /><sub><b>Gabriel de Marmiesse</b></sub></a><br /><a href="#question-gabrieldemarmiesse" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://github.com/alejandroscf"><img src="https://avatars3.githubusercontent.com/u/3200102?v=4" width="100px;" alt=""/><br /><sub><b>Alejandro Suarez</b></sub></a><br /><a href="#maintenance-alejandroscf" title="Maintenance">🚧</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!


Project Organization
------------

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
    ├── environment.yml    <- The environment file for reproducing the analysis environment, e.g.
    │                         `conda activate osm_imports_preparations`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions
        │   ├── predict_model.py
        │   └── train_model.py
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
            └── visualize.py



--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
