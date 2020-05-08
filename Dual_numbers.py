#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
class Dual:

    def __init__(self, r, g):

        self.r = r
        self.g = g
    
    def __str__(self):
        return str(self.r)+"+g("+str(self.g)+")"

    def __eq__(self, other):
        if not isinstance(other, Dual):
            other = Dual(other,0)
        er = (self.r == other.r)
        eg = (self.g == other.g)
        return er and eg    

    def __add__(self,other):
        if not isinstance(other, Dual):
            other = Dual(other,0)
        newr = self.r + other.r
        newg = self.g + other.g
        return Dual(newr, newg)
    
    def __radd__(self, other):
        if not isinstance(other, Dual):
            other = Dual(other,0)
        return self+other
    
    def _iadd__(self, other):
        return self+other
    
    def __sub__(self, other):
        if not isinstance(other, Dual):
            other = Dual(other,0)
        return Dual(self.r-other.r, self.g - other.g)

    def __rsub__(self, other):
        if not isinstance(other, Dual):
            other = Dual(other,0)
        return other-self        

    def _isub__(self, other):
        return self-other

    def __mul__(self, other):
        if not isinstance(other, Dual):
            other = Dual(other,0)
        newr = self.r * other.r
        newg = self.r * other.g + self.g * other.r
        return Dual(newr, newg)
    def __rmul__(self, other):
        if not isinstance(other, Dual):
            other = Dual(other,0)
        return other*self

    def _imul__(self, other):
        return self*other

    def __neg__(self):
        return Dual(-self.r, -self.g)

    
    def __truediv__(self, other):
        if not isinstance(other, Dual):
            other = Dual(other,0)
        return Dual(self.r/other.r , self.g/other.r - self.r*other.g/other.r/other.r)

    def __rtruediv__(self, other):
        if not isinstance(other, Dual):
            other = Dual(other,0)
        return other/self
    
    def __itruediv__(self, other):
        return self/other
    
    def __pow__(self, other):
        return Dual(self.r**other, self.g*other*self.r**(other-1)) #only for `usual` other, else look power

    def __abs__(self):
        return abs(self.r)
def exp(s):
    if not isinstance(s, Dual):
        s = Dual(s, 0)
    return Dual(np.exp(s.r), np.exp(s.r)*s.g)

def ln(s):
    if not isinstance(s, Dual):
        s = Dual(s, 0)
    return Dual(np.log(s.r), s.g / s.r)

def power(a, s):# a^x
    return exp(ln(a)*s)

def sin(s):
    if not isinstance(s, Dual):
        s = Dual(s, 0)
    return Dual(np.sin(s.r), s.g * np.cos(s.r))

def cos(s):
    if not isinstance(s, Dual):
        s = Dual(s, 0)
    return Dual(np.cos(s.r), -s.g*np.sin(s.r))


def dsin(x):
    i, lasts, s, fact, num, sign = 1, Dual(0,0), x, 1, x, 1
    while abs(s.r - lasts.r) > 1e-20:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num = num * x * x
        sign *= -1
        s = s + num / fact * sign
    return s

def dcos(x):
    i, lasts, s, fact, num, sign = 0, Dual(0,0), Dual(1,0), 1, 1, 1
    while abs((s.r - lasts.r)) > 1e-20:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num = num * x * x
        sign *= -1
        s = s + num / fact * sign
    return s
def ch(x):
    return (exp(x) + exp(-x))/2
def sh(x):
    return (exp(x) - exp(-x))/2



