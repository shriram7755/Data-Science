# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:20:45 2023

@author: SHRI
"""

def make_pizza(size,*toppings):
    #summarize the pizza we are about to make
    print(f"\n Making a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"-{topping}")