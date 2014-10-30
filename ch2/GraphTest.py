
import string

from Graph import Vertex
from Graph import Edge
from Graph import Graph
from RandomGraph import RandomGraph
from GraphWorld import GraphWorld
from GraphWorld import CircleLayout

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


if __name__ == '__main__':
    import sys
    main2(*sys.argv)


