from setuptools import setup, find_packages
from js9notebook import __version__

setup(
    name="js9notebook",
    version=__version__,
    packages=find_packages(),
    author="Gijs Molenaar",
    author_email="gijs@pythonic.nl",
    description="Embed JS9 into Jupyter",
    license="MIT",
    keywords="astronomy JS9 DS9 jupyter notebook FITS ipython",
    url="https://github.com/gijzelaerr/js9notebook",

    package_data={
        'js9notebook': ['*.js', '*.css'],
    },

    install_requires=['notebook']


)
