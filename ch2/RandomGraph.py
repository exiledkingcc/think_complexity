
from Graph import Edge,Vertex,Graph

class RandomGraph(Graph):
    
    def add_random_edges(self,p):
        """adds edges at random so that the
        probability is p that there is an
        edge between any two nodes"""
        import random
        if p<=0 or p>=1:
            raise ValueError("0<= p <1")
        vs=self.vertices()
        for i in range(len(vs)):
            for j in range(i+1,len(vs)):
                r=random.random()
                if r<=p:
                    self.add_edge(Edge(vs[i],vs[j]))


def main(script, n='5', p='0.5', *args):
    import string
    n=int(n)
    p=float(p)
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]
    g = Graph(vs)
    g.add_random_edges(p)
    print(g)

if __name__ == '__main__':
    import sys
    main(*sys.argv)
