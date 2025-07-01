# Configuration file for the Sphinx documentation builder.
#
# -- Project information -----------------------------------------------------

project = 'SPHEREx Archive Documentation'
copyright = '2025 SPHEREx Archive -- IPAC/IRSA'
author = 'SPHEREx Archive -- IPAC/IRSA'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_nb',
    'sphinx_copybutton',
]

myst_enable_extensions = [
    'dollarmath',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'notes', '.tox', '.tmp', '.pytest_cache', ]

# Top level README file's sole purpose is for the repo.
exclude_patterns += ['README.md',]

# MyST-NB configuration
nb_execution_timeout = 1200
nb_execution_mode = 'off'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
html_title = 'SPHEREx Archive Documentation'
html_logo = '_static/irsa_logo.png'
html_favicon = '_static/irsa-favicon.ico'
html_theme_options = {
    "github_url": "https://github.com/Caltech-IPAC/SPHEREx-archive-documentation",
    "repository_url": "https://github.com/Caltech-IPAC/SPHEREx-archive-documentation",
    "repository_branch": "main",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "launch_buttons": {"binderhub_url": "https://mybinder.org",},
    "logo": {
        "link": "https://irsa.ipac.caltech.edu/",
        "alt_text": "NASA/IPAC Infrared Science Archive - Home",
    },
    "home_page_in_toc": True,
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# myst configurations
myst_heading_anchors = 4
