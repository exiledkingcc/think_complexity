""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Edge(tuple):
    """An Edge is a list of two vertices."""

    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError('Edges must connect exactly two vertices.')
        return tuple.__new__(cls, vs)

    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.
    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    def __init__(self, vs=[], es=[]):
        """Creates a new graph.  
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)      
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}

    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.
        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self,v1,v2):
        return self.get(v1)

    def remove_edge(self,e):
        for v in self:
            for w in v:
                if self[v][w]==e:
                    self[v].pop(w)
                    self[w].pop(v)

    def vertices(self):
        return list(self.keys())

    def edges(self):
        es=[]
        for v in self:
            for w in v:
                if self[v][w] not in es:
                    es.append(self[v][w])
        return es

    def out_vertices(self,v):
        try:
            vs=self[v]
        except KeyError:
            return None
        return vs.keys()

    def out_edges(self,v):
        try:
            vs=self[v]
        except KeyError:
            return None
        return vs.values()

    def add_all_edges(self):
        vs=self.vertices()
        for i in range(len(vs)):
            for j in range(i+1,len(vs)):
                self.add_edge( Edge(vs[i],vs[j]) )

    def remove_all_edges(self):
        for v in self : self[v]={}

    def add_regular_edges(self,k):
        " k*v==2e "
        vs=self.vertices()
        v=len(vs)
        if k<=1 or k>=v or (k*v)%2!=0:
            raise ValueError("not possible for regular")
        kk=k//2
        for i in range(v):
            for j in range(1,kk+1):
                self.add_edge( Edge(vs[i],vs[(i+j)%v]) )
                self.add_edge( Edge(vs[i],vs[i-j]) )
        if k%2!=0:
            dis=v//2
            for i in range(v):
                self.add_edge( Edge(vs[i],vs[i-dis]) )

    def is_connected(self):
        vs=self.vertices()
        if len(vs)<=1 : return True
        op=[vs[0]]; cl=[vs[0]]
        while len(op)!=0:
            for i in self[op[0]]:
                if i not in cl:
                    cl.append(i)
                    op.append(i)
            op=op[1::]
        if len(vs)==len(cl):
            return True
        else:
            return False


def main(script, *args):
    v = Vertex('v')
    print(v)
    w = Vertex('w')
    print(w)
    e = Edge(v, w)
    print(e)
    g = Graph([v,w], [e])
    print(g)


if __name__ == '__main__':
    import sys
    main(*sys.argv)
