from DOInterface import DOInterface

DOI = None

#Initialize all nodes in the network
def getNodes(n, i):
	DOKey = '31c9796a2ba7c4968da001958fd85fd9bea056a88a6ad434e082351a4f80ccdf'
	SSHKey = 'Main Key'

	global DOI
	DOI = DOInterface(DOKey, SSHKey, n)

	nodes = DOI.importDroplets('droplets.json') if i else DOI.createDroplets()
	DOI.exportDroplets()
	return nodes

def destroyNodes(nodes):
	DOI.destroyDroplets(nodes)