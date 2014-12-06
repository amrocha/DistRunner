from Topology import Topology
from Link import Link

class Ring(Topology):
	def __init__(self, n):
		super(Ring, self).__init__(n)

		for i in range(0, n):
			self.nodes[i].setLinks([Link(self.nodes[(i+1)%n], 'left'), Link(self.nodes[(i-1)%n], 'right')])

ring = Ring(10)
print ring
print ring.nodes