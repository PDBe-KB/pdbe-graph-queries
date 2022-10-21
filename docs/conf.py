# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
from pathlib import Path

import pdbequeries

# -- Project information -----------------------------------------------------

project = "PDBe graph queries"
copyright = "2022, Protein Data Bank in Europe"
author = "Protein Data Bank in Europe"

# The full version, including alpha/beta/rc tags
release = "1.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinxcontrib.napoleon",
    "sphinx.ext.todo",
    "sphinx_markdown_tables",
    "sphinx.ext.coverage",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "myst_parser",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_logo = "_static/imgs/logo.png"
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

pygments_style = "sphinx"
github_doc_root = "https://github.com/rtfd/recommonmark/tree/master/doc/"
add_module_names = False


def setup(app):
    # app.add_config_value(
    #     "recommonmark_config",
    #     {
    #         "url_resolver": lambda url: github_doc_root + url,
    #         "auto_toc_tree_section": "Contents",
    #     },
    #     True,
    # )
    # app.add_transform(AutoStructify)
    app.connect(
        "autodoc-process-docstring",
        no_namedtuple_attrib_docstring,
    )


def no_namedtuple_attrib_docstring(app, what, name, obj, options, lines):
    is_namedtuple_docstring = len(lines) == 1 and lines[0].startswith(
        "Alias for field number"
    )
    if is_namedtuple_docstring:
        # We don't return, so we need to purge in-place
        del lines[:]


# generate queries

for module in os.listdir(Path(pdbequeries.__file__).parent):
    if len(module) <= 3 or module[-3:] != ".py":
        continue

    module = module.split(".")[0]
    module = __import__(f"{pdbequeries.__name__}.{module}", fromlist="dummy")

    location = str(Path(pdbequeries.__file__).parent.parent)

    location = os.path.join(location, "docs", "api_doc", "rst_queries")
    os.makedirs(location, exist_ok=True)

    for attribute in module.__dict__:
        if attribute[0:2] == "Q_":  # get all the queries, they start with Q_
            value = getattr(module, attribute)
            path = os.path.join(location, f"{attribute}.rst")

            with open(path, "w") as f:
                f.write(".. code-block:: text\n\n")

                for line in value.splitlines():
                    f.write(f"   {line}\n")
                f.write("\n\n")
