
import string

from Graph import Vertex,Edge,Graph
from RandomGraph import RandomGraph
from GraphWorld import GraphWorld,CircleLayout

def main(script, n='10', k='3', *args):

    # create n Vertices
    n = int(n)
    k = int(k)
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]

    # create a graph and a layout
    g = Graph(vs)
    g.add_regular_edges(k)
    layout = CircleLayout(g)

    # draw the graph
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()

def main2(script, n='10', p='0.5', *args):

    # create n Vertices
    n = int(n)
    p = float(p)
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]

    # create a graph and a layout
    g = RandomGraph(vs)
    g.add_random_edges(p)
    layout = CircleLayout(g)

    # draw the graph
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()

    print(g.is_connected())

def test_n_p(n,p):
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]
    g = RandomGraph(vs)
    x=0;
    for i in range(100):
        g.add_random_edges(p)
        if g.is_connected() : x=x+1
        g.remove_all_edges()
    return x/100

def main3(script, *args):
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    xyz=[(x,y/20,test_n_p(x,y/20)) for x in range(1,20) for y in range(1,20)]
    x=np.array([x for x,y,z in xyz])
    y=np.array([y for x,y,z in xyz])
    z=np.array([z for x,y,z in xyz])
    ax.plot_trisurf(x,y,z)
    plt.show()


if __name__ == '__main__':
    import sys
    main3(*sys.argv)


