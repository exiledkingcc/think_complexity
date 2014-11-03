"""A Red-Black Tree"""


class TreeMap(object):
	
	_BLK=object()
	_RED=object()
	
	class _Node(object):
		def __init__(self, k, v):
			self.key=k
			self.value=v
			self.left=None
			self.right=None
			self.parent=None
			self.color=TreeMap._BLK

		def __str__(self):
			return "{{{0}:{1}}}".format(self.key,self.value)


	def __init__(self):
		self.root=None

	def get(self, k):
		p=self.root
		while p is not None:
			if k==p.key : return p.value
			elif k<p.key : p=p.left
			else : p=p.right
		raise KeyError("key not found")

	def _left_rotate(self, x):
		y=x.right
		x.right=y.left
		if y.left is not None : y.left.parent=x
		y.parent=x.parent
		if x.parent is None:
			self.root=y
		elif x==x.parent.left:
			x.parent.left=y
		else : x.parent.right=y
		y.left=x
		x.parent=y

	def _right_rotate(self, x):
		y=x.left
		x.left=y.right
		if y.right is not None : y.right.parent=x
		y.parent=x.parent
		if x.parent is None:
			self.root=y
		elif x==x.parent.right:
			x.parent.right=y
		else : x.parent.left=y
		y.right=x
		x.parent=y

	def add(self, k, v):
		z=TreeMap._Node(k,v)
		y=None
		x=self.root
		while x is not None:
			y=x
			if z.key<x.key : x=x.left
			else : x=x.right
		z.parent=y
		if y is None:
			self.root=z
			return
		elif z.key==y.key:
			raise KeyError("key alreay exists")
		elif z.key<y.key:
			y.left=z
		else : y.right=z
		z.color=TreeMap._RED
		while z.parent.color==TreeMap._RED:
			if z.parent.parent is None : break
			elif z.parent.parent.left==z.parent:
				y=z.parent.parent.right
				if y is not None and y.color==TreeMap._RED:
					y.color=TreeMap._BLK
					z.parent.color=TreeMap._BLK
					z.parent.parent.color=TreeMap._RED
					z=z.parent.parent
					if z.parent is None : break
				else:
					if z==z.parent.right:
						z=z.parent
						self._left_rotate(z)
					z.parent.color=TreeMap._BLK
					z.parent.parent.color=TreeMap._RED
					self._right_rotate(z.parent.parent)
			else:
				y=z.parent.parent.left
				if y is not None and y.color==TreeMap._RED:
					y.color=TreeMap._BLK
					z.parent.color=TreeMap._BLK
					z.parent.parent.color=TreeMap._RED
					z=z.parent.parent
					if z.parent is None : break
				else:
					if z==z.parent.left:
						z=z.parent
						self._right_rotate(z)
					z.parent.color=TreeMap._BLK
					z.parent.parent.color=TreeMap._RED
					self._left_rotate(z.parent.parent)
		self.root.color=TreeMap._BLK


	def level_print(self):
		p=self.root
		if p is None:
			print("{}")
			return
		ps=[p,None]
		while len(ps)>1:
			i=0
			while ps[i] is not None:
				if ps[i].left is not None:
					ps.append(ps[i].left)
				if ps[i].right is not None:
					ps.append(ps[i].right)
				print(str(ps[i]),end=" ")
				i+=1
			print()
			ps=ps[i+1::]
			ps.append(None)



def main(script, n='100', *args):
	import random
	n=int(n)
	m=TreeMap()
	for i in range(n):
		try:
			m.add(random.randint(0,100),random.randint(0,100))
		except KeyError:
			pass
	m.level_print()

if __name__ == '__main__':
	import sys
	main(*sys.argv)
