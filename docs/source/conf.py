# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

# Adicione o caminho ao diretório que contém seus módulos
sys.path.insert(0, os.path.abspath('..\..'))

project = 'A1-Linguagem de Programação'
copyright = '2023, Guilherme Buss, João Gabriel, Gustavo Bianchi e Vinicius Nascimento'
author = 'Guilherme Buss, João Gabriel, Gustavo Bianchi e Vinicius Nascimento'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'pt'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
