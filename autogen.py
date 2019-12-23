# content of docs/autogen.py

from keras_autodoc import DocumentationGenerator

from src.features import bcn_trees


pages = {
    'api_bcn_trees.md': [
        'src.features.bcn_trees.data_download',
        'src.features.bcn_trees.data_munging'
    ]
}

doc_generator = DocumentationGenerator(pages)
doc_generator.generate('./sources')
