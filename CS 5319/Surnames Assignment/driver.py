#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 22:26:03 2020

@author: oscargalindo
"""

import predictor

src = './'
file = 'surnames-dev.csv'
countries = predictor.process_file(src+file)
names = predictor.process_file_names(src+file)
n = predictor.get_keys(names)
origins = predictor.get_origins(n)
predictor.calculate_accuracy(names, origins)
predictor.get_stats_origins(names,origins,['Japanese'])
# #############Musicians###################
# musicians = predictor.process_file_names(src+'composers.txt')
# n = predictor.get_keys(musicians)
# origins = predictor.get_origins(n)
# predictor.calculate_accuracy(musicians, origins)
# predictor.write_predictions(src, musicians, origins)