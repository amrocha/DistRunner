from initializeNodes import *
from Topologies import *

rsaFile = '/Users/andreRocha/.ssh/id_rsa'
nodes = getNodes(3, True)

#Create topology
ipList = []
for n in nodes:
	ipList.append(n.networks['v4'][0]['ip_address'])

exportLinks(Ring(ipList))
print ipList
print Ring(ipList)