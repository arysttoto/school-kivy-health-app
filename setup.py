from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'iconfile': 'forheartapp.png'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
