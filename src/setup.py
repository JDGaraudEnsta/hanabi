"""
setup.py for tha Hanabi game.
Use it with e.g.:
    python3 setup.py install --user
"""


from setuptools import setup, find_packages

setup(
    name = "hanabi",
    version = "0.1.0",
    packages = find_packages("."),
    author = "JD. Garaud",
    author_email = "jdgaraud@onera.fr",
    description = "Hanabi game: CLI, GUI and AI",
    license="LGPL",
    keywords = "Hanabi, game, GUI, AI",
    url = "https://gitlab.ensta.fr/garaud/Hanabi",
    # could also include long_description, download_url, classifiers, etc.
)


