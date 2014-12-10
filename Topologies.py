import json

def Ring(nodes):
	links = []

	n = len(nodes)
	for i in range(0, n):
		links.insert(i,{'id': i, 'left':nodes[(i-1)%n], 'right':nodes[(i+1)%n], 'ip':nodes[i]})
	return links

def exportLinks(links):
	for i, node in enumerate(links):
		filename = 'data/node' + str(i) + '.json'
		f = open(filename, 'w')
		f.write(json.dumps(node))
		f.close()