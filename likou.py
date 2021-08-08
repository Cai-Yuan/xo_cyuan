import pandas as pd
import numpy as np

class node(object):
    def __init__(self, val, hang,lie):
        self.val=val
        self.hang=hang
        self.lie=lie
        self.sun=[]
    def add_sun(self,asunnode):
        self.sun.append(asunnode)

class tree(object):
    def __init__(self):














