from Node import Node

class Topology(object):
	def __init__(self, n):
		self.nodes = []
		for i in range(0, n):
			self.nodes.append(Node(i));

	def __str__(self):
		s = 'Topology with ' + str(len(self.nodes)) + ' nodes'
		return s

	def __repr__(self):
		s = 'Topology with ' + str(len(self.nodes)) + ' nodes'
		return s