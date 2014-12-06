class Link(object):
	def __init__(self, node, label=None):
		self.node = node
		self.label = label

	def __str__(self):
		s = self.label + ': Node ' + str(self.node.id)
		return s 

	def __repr__(self):
		s = self.label + ': Node ' + str(self.node.id)
		return s 