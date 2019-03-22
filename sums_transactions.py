#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 18:31:17 2019

@author: francescobenfenati
"""
from transactions import sum_transactions
for filename in snakemake.input:
    sum_transactions(str(filename),str(snakemake.output))