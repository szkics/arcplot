#!/bin/bash

set -e

source arcenv/bin/activate
black arcplot/arcplot.py
black main.py
python main.py