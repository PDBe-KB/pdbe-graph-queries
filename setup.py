import os

from setuptools import find_namespace_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pdbequeries",
    version="1.0",
    description="Cypher graph queries used at the Protein Data Bank in Europe",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    project_urls={
        "Source code": "https://github.com/PDBe-KB/pdbe-graph-queries",
        "Documentation": "",
    },
    author="Protein Data Bank in Europe",
    author_email="pdbehelp@ebi.ac.uk",
    license="Apache License 2.0.",
    keywords="PDB CCD wwPDB Neo4j cypher graph",
    packages=find_namespace_packages(),
    zip_safe=False,
    include_package_data=True,
    python_requires=">=3.6",
    extras_require={
        "docs": [
            "sphinx",
            "sphinxcontrib-napoleon",
            "sphinx-copybutton",
            "sphinx_rtd_theme",
            "myst-parser",
            "sphinx-autodoc-typehints",
            "sphinx-markdown-tables",
        ],
    },
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Development Status :: 5 - Production/Stable",
    ],
)
