#!usr/bin/python3.8

def get_descripion():
    """ return random weather, just like the Dros"""
    from random import choice
    possiblilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possiblilities)
