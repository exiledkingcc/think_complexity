"""time test for Map and TreeMap"""

import os
import random
import matplotlib.pyplot as pyplot
from TreeMap import TreeMap
from Map import HashMap

def etime():
    """Measures user and system time this process has used.
    Returns the sum of user and system time."""
    user, sys, chuser, chsys, real = os.times()
    return user+sys

def test_func(m, n):
    """m -- Map or TreeMap, n -- numbers"""
    data=[ random.randint(0,n*2) for i in range(n)]
    data=set(data)
    time1 = etime()
    for i in data:
        m.add(i,i)
    time2 = etime()
    for i in data:
        m.get(i)
    time3 = etime()
    return (time2-time1,time3-time2)

def test(name):
    m=eval(name)()
    factor=2000
    ns = []
    tsa = []
    tsg = []
    for i in range(2, 50):
        n = factor * i
        t = test_func(m, n)
        print(n, t[0], t[1])
        ns.append(n)
        tsa.append(t[0])
        tsg.append(t[1])

    return (ns, tsa, tsg)


def plot(ns, ts, label, color='blue'):
    """Plots data and a fitted curve.
    ns: sequence of n (problem size)
    ts: sequence of t (run time)
    label: string label for the data curve
    color: string color for the data curve
    """
    tfit = fit(ns, ts)
    pyplot.plot(ns, tfit, label='log2', color='0.7', linewidth=2, linestyle='dashed')
    pyplot.plot(ns, ts, label=label, color=color, linewidth=3)


def fit(ns, ts, exp=1.0, index=-1):
    """Fits a curve with the given exponent.
    Use the given index as a reference point, and scale all other
    points accordingly.
    """
    nref = ns[index]
    tref = ts[index]
 
    tfit = []
    for n in ns:
        ratio = float(n) / nref
        t = ratio**exp * tref
        tfit.append(t)
    return tfit

def save(root, exts=['eps', 'pdf']):
    """Saves the current figure in the given formats.
    root: string filename root
    exts: list of string extensions (specifying output formats).
    """
    for ext in exts:
        filename = '%s.%s' % (root, ext)
        print('Writing', filename)
        pyplot.savefig(filename)


def make_fig(cls, scale='log', filename=''):
    pyplot.clf()
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title('')
    pyplot.xlabel('n')
    pyplot.ylabel('run time (s)')

    colors = ['blue', 'orange']
    funcs = ['add', 'get']
    data = test(cls)
    ns=data[0]
    tss=data[1::]
    for (ts,color,func) in zip(tss,colors,funcs):
        plot(ns, ts, label=func, color=color)
    
    if filename:
        save(filename)
    else:
        pyplot.show()
        

def main(script):
    make_fig('HashMap', filename='HashMap_fig')
    make_fig('TreeMap', filename='TreeMap_fig')


if __name__ == '__main__':
    import sys
    main(*sys.argv)

