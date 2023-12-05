#!/bin/bash

# Install Python packages
pip install opendatasets
pip install pandas
pip install pysqlite3
pip install kaggle


python3 data_pipeline.py
python3 test.py
