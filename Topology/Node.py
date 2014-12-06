class Node(object):
	def __init__(self, id):
		self.id = id

	def __str__(self):
		s = 'Node ' + str(self.id)
		return s 

	def __repr__(self):
		s = 'Node ' + str(self.id) + ' linked to nodes' + str(self.links)
		return s 

	def setLinks(self, links):
		self.links = links