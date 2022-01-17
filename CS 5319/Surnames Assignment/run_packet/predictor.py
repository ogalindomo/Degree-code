#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 17:52:13 2020

@author: oscargalindo
"""

import random

def is_arabic(name):
    strings=['fa','eif','ha','al','ba','ou','uo','ui','sar','dd','ad','ha','ni','nem','ki''zz','az','azz','am','sha','ai','ouf']
    name = name.lower()
    for s in strings:
        if s in name:
            return True
    return False

def is_chinese(name):
    strings=['ao','oa','wa','jin','qi','dai','Tz','ai','ia','an','xi','oo','ang','ni','in','sh']
    name = name.lower()
    for s in strings:
        if s in name:
            return True
    return False
    
def is_czech(name):
    strings=['ka','ff','sek','wa','sch','deh','ss','jj','ik','pp','vl','ski','ze','rich','cova','tak','ovsky','warz','schm','ich','witz','pp']
    name = name.lower()
    for s in strings:
        if s in name:
            return True
    return False

def is_dutch(name):
    strings=['ee','jer','aye','oo','gg','ee','aa','ker','ss','nn','kk','ke']
    name = name.lower()
    for s in strings:
        if s in name:
            return True
    return False

def is_english(name):
    strings=['ll','oo','wood','ers','bb','ss','way','ee','dow','ach','gg','van','tt','pp','down','ross','ver','ker','ren','ran','owe','mc']
    name = name.lower()
    for s in strings:
        if s in name:
            return True
    return False

def is_french(name):
    strings=['le','ss','and','aux','oli','vage','eux','tit','ieu','nna','bon','boi','dú','neau','eau','oy','ias','quet','reau','hur','agne']
    name = name.lower()
    for s in strings:
        if s in name:
            return True
    return False

def is_german(name):
    strings=['tt','ber','oh','eier','ich','altz','ieck','enz','hol','uh','aun','del','ō','eis','mm','kl','aub']
    name = name.lower()
    for s in strings:
        if s in name:
            return True
    return False

def is_greek(name):
    strings=['ous','kos','nos','mos','los','is','as']
    name = name.lower()
    for s in strings:
        if s in name:
            return True
    return False

def is_irish(name):
    strings=["o'",'ach',"ley","lly",'all','an','mac','oi','inn','ald']
    name = name.lower()
    for s in strings:
        if s in name:
            return True
    return False

def is_italian(name):
    strings=["eri","ari","icci","one","chi","ggi","gio","à","tti","di","gari","fin","lli","to","oli","dia","zzi","Scor","ini","ecce","acco","ani"]
    name = name.lower()
    for s in strings:
        if s in name:
            return True
    return False

def is_japanese(name):
    strings=['shi','oku','ida','iko','aka','tsu','awa','aya','ishi','uno','ima','chi','uya','hara','zak','aki','ji','uch']
    name = name.lower()
    for s in strings:
        if s in name:
            return True
    return False

def is_korean(name):
    strings=["mo","ch","oo","se","ha","san"]
    name = name.lower()
    for s in strings:
        if s in name:
            return True
    return False

def is_polish(name):
    strings=["ń","ka","ski","ó","no","cz","ko","zga"]
    name = name.lower()
    for s in strings:
        if s in name:
            return True
    return False

def is_portuguese(name):
    strings=["inho","ō","lho","ã","ro","é"]
    name = name.lower()
    for s in strings:
        if s in name:
            return True
    return False

def is_russian(name):
    strings=["ov","nov","ev","ivch","sky","tov","iev","ich","cev","in","ff","hin",""]
    name = name.lower()
    for s in strings:
        if s in name:
            return True
    return False

def is_scottish(name):
    strings=["aw","son","las","ald","ht","hy","ant","at"]
    name = name.lower()
    for s in strings:
        if s in name:
            return True
    return False

def is_spanish(name):
    strings=["ó","lix","oj","é","rez","lla","cal","que","res","aya","ey","ez",'á','í']
    name = name.lower()
    for s in strings:
        if s in name:
            return True
    return False

def is_vietnamese(name):
    strings=["im","hao","han","ly","ach","ch"]
    name = name.lower()
    for s in strings:
        if s in name:
            return True
    return False

def get_origins(names):
    origin = []
    for name in names:
        options = []
        if is_arabic(name): options.append('Arabic')
        if is_chinese(name): options.append('Chinese')
        if is_czech(name): options.append('Czech')
        if is_dutch(name): options.append('Dutch')
        if is_english(name): options.append('English')
        if is_french(name): options.append('French')
        if is_german(name): options.append('German')
        if is_greek(name): options.append('Greek')
        if is_irish(name): options.append('Irish')
        if is_italian(name): options.append("Italian")
        if is_japanese(name): options.append("Japanese")
        if is_korean(name): options.append('Korean')
        if is_polish(name): options.append('Polish')
        if is_portuguese(name): options.append('Portuguese')
        if is_russian(name): options.append('Russian')
        if is_scottish(name): options.append('Scottish')
        if is_spanish(name): options.append("Spanish")
        if is_vietnamese(name): options.append("Vietnamese")
        if len(options) > 0:
            i = random.randint(0, len(options)-1)
            origin.append([name,options[i]])
        else:
            o = ['Arabic','Chinese','Czech','Dutch','English','French','German','Greek','Irish','Italian','Japanese','Korean','Polish','Portuguese','Russian','Scottish','Spanish','Vietnamese']
            i = random.randint(0,len(o)-1)
            origin.append([name,options[i]])
    return origin

def process_file(src):
    lines = open(src).readlines()
    languages = dict()
    for line in lines:
        if 'To The First' in line: continue
        line = line.strip("\n")
        line = line.strip('"')
        line = line.strip('"')
        s = line.split(",")
        if "Jevolojnov" in line:
            s.remove('"')
            print(s)
        if not s[1] in languages:
            languages[s[1]] = []
        languages[s[1]].append(s[0])
    return languages

def process_file_names(src):
    lines = open(src).readlines()
    names = dict()
    for line in lines:
        if 'To The First' in line: continue
        line = line.strip("\n")
        line = line.strip('"')
        line = line.strip('"')
        s = line.split(",")
        if "Jevolojnov" in line:
            s.remove('"')
            print(s)
        if not s[0] in names:
            names[s[0]] = []
        if s[1] in names[s[0]]:
            continue
        else:
            names[s[0]].append(s[1])
    return names

def calculate_precision(names,origins):
    correct = 0
    for e in origins:
        if e[1] in names[e[0]]:
            correct+=1    
    print("Accuracy:",correct/len(names)) 
    
def write_predictions(src,true,predictions):
    f = open(src+"prediction.txt","w")
    f.write("Name"+"\t"+"Actual"+"\t"+"Predicted\n")
    for e in predictions:
        # row = e[0]+"\t"+true[e[0]]"\t"+e[1]+"\n"
        f.write(e[0]+"\t"+true[e[0]][0]+"\t"+e[1]+"\n")
    f.close()
      
if __name__ == "__main__":
    src = './'
    countries = process_file(src+'surnames-dev.csv')
    names = process_file_names(src+'surnames-dev.csv')
    n = []
    for k in names.keys():
        n.append(k)
    origins = get_origins(n)
    calculate_precision(names, origins)
    #############Musicians###################
    musicians = process_file_names(src+'composers.txt')
    n = []
    for k in musicians.keys():
        n.append(k)
    origins = get_origins(n)
    calculate_precision(musicians, origins)
    write_predictions(src, musicians, origins)
    
    