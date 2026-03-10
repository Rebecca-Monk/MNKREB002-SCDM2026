#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 08:52:47 2026

@author: rebeccamonk
"""
filename = "ctd_profiles.dat"
file open(filename, mode ='r') 
import pandas as pd
df = pd.read_csv("ctd_profiles.dat", sep="\t")
print(df)