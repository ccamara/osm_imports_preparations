# content of docs/autogen.py

from keras_autodoc import DocumentationGenerator

from osmi_helpers import data_gathering

pages = {
    'osmi_helpers.md': [
        'osmi_helpers.data_gathering.csv_parser'
    ]
}

doc_generator = DocumentationGenerator(pages)
doc_generator.generate('./docs/sources')
