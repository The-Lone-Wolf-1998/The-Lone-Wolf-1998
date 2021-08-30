# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/Poulami/Documents/new_proj_dscience/chromedriver.exe"
df = gs.get_jobs("Data Science", 15, False, path, 15)