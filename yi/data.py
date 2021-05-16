#!/usr/bin/env python3

import yaml
import os

# gua64_file = os.path.expanduser("~/data/gua64.yaml")
gua64_file = './data/gua64.yaml'

with open(gua64_file, encoding='utf-8') as fh:
    gua64_data = yaml.load(fh, Loader=yaml.FullLoader)
