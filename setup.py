from setuptools import setup

APP = ['main.py']  # Ton fichier principal
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',  # chemin vers ton icône mac (format .icns)
    'packages': ['selenium', 'openpyxl', 'tkinter'],  # modules nécessaires
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
