#!/bin/bash

rm -rf dist/*
source venv/bin/activate
python setup.py sdist bdist_wheel
twine upload --repository pypi dist/*
