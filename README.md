# Real Estate Site

This is a prototype of site of realty for sale. 


# Requirements

Python 3.3 or higher and packages from requirements.txt 

# How to launch

First you should get a json file with certain keys. Example of json file file with
necessary keys is [here](https://devman.org/media/filer_public/e5/62/e56287d2-9519-4e18-878a-6d4849b628e2/ads.json).
Then create a sqlite database from valid json file by typing:

`python3 db_updater.py file.json`

A database with name 'realty.db' will be created in the same folder, where json file is.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
