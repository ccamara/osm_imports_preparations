# content of docs/autogen.py

from keras_autodoc import DocumentationGenerator


pages = {
    'bcn_trees.md': [
        'features.data_download',
        'features.data_munging']
    }

doc_generator = DocumentationGenerator(pages)
doc_generator.generate('./sources')
