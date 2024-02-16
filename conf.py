# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
#sys.path.insert(0, 'C:\\Users\\Etscheidt\\Documents\\pyth\\check_web\\src')

# my_dir=os.path.abspath(os.path.join('.','..','..','src'))
# print (my_dir)
# sys.path.append(my_dir)


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'knoffhoff'
copyright = '2024, Klaus Etscheidt'
author = 'Klaus Etscheidt'
release = '1.0'
# root_doc = 'Readme'  macht Probleme root muss immer index heißen
htmlhelp_basename = project

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage', 'sphinx.ext.napoleon',
              'sphinx.ext.todo', 'myst_parser']

# templates_path = ['_templates']
# exclude_patterns = []

language = 'de'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
# html_static_path = ['_static']

# autoclass_content = 'both'

# autodoc_member_order = 'bysource'
# autodoc_inherit_docstrings = False

napoleon_use_param = True

myst_heading_anchors = 7
myst_enable_extensions = ["deflist"]

# def change(app, what, name, obj, options, lines):
#     print(lines)
#     #name += '#######'

# def setup(app):
#     app.connect("autodoc-process-docstring", change)