"""Doubly-linked list impliment of FIFO
	copyright @ c.c.<exiledkingcc@gmail.com>
"""

class DlistFIFO(object):

	class _Node(object):

		def __init__(self, v):
			self.value=v
			self.prev=None
			self.next=None
			

	def __init__(self):
		self.head=None
		self.tail=None

	def empty(self):
		return self.head==None

	def push(self, v):
		node=DlistFIFO._Node(v)
		if self.empty():
			self.head=self.tail=node
		else:
			self.tail.next=node
			node.prev=self.tail
			self.tail=node

	def pop(self):
		if self.empty():
			return None
		else:
			v=self.head.value
			self.head=self.head.next
			if self.head is None:
				self.tail=None
			else:
				self.head.prev=None
			return v


def main(script,n='10',*args):
	n=int(n)
	d=DlistFIFO()
	for i in range(n):
		d.push(i)
	while not d.empty():
		print(d.pop())

if __name__ == '__main__':
	import sys
	main(*sys.argv)