# Configuration file for the Sphinx documentation builder.

# -- Project information
rst_prolog = """
.. |app| replace:: *AndBible*
.. |hamburger| replace:: ☰ 
"""

project = 'Bible Study App'
copyright = '2021, And Bible Open Source Project'
author = 'And Bible Open Source Project'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
]

# Make sure the target is unique
autosectionlabel_prefix_document = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

def setup(app):
    app.add_css_file('custom.css')


