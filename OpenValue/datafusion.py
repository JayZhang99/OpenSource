import pandas as pd
import numpy as np

class data(object):
    def __init__(self,LOC,CC,HV,CO,AST,II,IP):
        self.LOC=LOC
        self.CC=CC
        self.HV=HV
        self.CO=CO
        self.AST=AST
        self.II=II
        self.IP=IP
    def fusion(self):
        self.C=self.LOC+self.CC+self.HV-self.CO
        self.Score=self.AST*self.II*self.C*(self.IP+1)
    
