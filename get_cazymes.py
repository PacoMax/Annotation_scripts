# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 13:50:20 2023

@author: pacomax
"""
import re
import sys

#The script uses the output file "overview" of dbcan and an output file.
#It just enlists the results of dbcan keeping with a cazyme at least founded
#with two algorithms.

#In case of more than one algorith found the cazyme, the output name of eCAMI is kept
#If it found the cazyme with DIAMOND and HMMER, DIAMOND name is kept.
#If the gene is componned of more than one cazyme, all the cazymes are kept and enlisted.

Cazy_in = sys.argv[1]
Cazy_ou = sys.argv[2]


Cazy=[]
with open(Cazy_in, "r") as file:
    for line in file:
        # Procesa la línea
        line = line.strip()
        variables = line.split("\t")  
        if variables[5]=="3":
            Cazy.append(variables[3])
        if variables[5]=="2":
            if variables[3]!="-":
                Cazy.append(variables[3])
            else:
                Cazy.append(variables[4])
      #  if variables[5]=="1":
       #     if variables[2]!="-":
        #        Cazy.append(variables[2])
         #   if variables[3]!="-":
          #      Cazy.append(variables[3])
           # if variables[4]!="-":
            #    Cazy.append(variables[4])
    for variable in Cazy:
        variable=variable.split("+")
        new_variable= [re.sub(r'\(\w+-\w+\)', '', item)  for item in  variable]
        new_variable_2= [re.sub(r'_\w+', '', item_2)  for item_2 in  new_variable]
        with open(Cazy_ou, "a") as file:
            file.write("\n".join(new_variable_2)+"\n")
