#!/usr/bin/env python3

import yaml
import os

gua64_file = os.path.expanduser("~/data/gua64.yaml")

with open(gua64_file) as fh:
    gua64_data = yaml.load(fh, Loader=yaml.FullLoader)
