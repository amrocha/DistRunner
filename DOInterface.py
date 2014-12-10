import skiff
import threading
import logging
import json

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class DOInterface(object):
	def __init__(self, doKey, SSHKeyName, n):
		self.DOApi = skiff.rig(doKey)
		self.SSHKey = self.DOApi.Key.get(SSHKeyName)
		self.n = n
		self.droplets = []


	def createDroplet(self, i):
		nd = self.DOApi.Droplet.create(name='test'+str(i),
					  region='nyc3',
					  size='512mb',
					  image='ubuntu-14-04-x64',
					  ssh_keys=[self.SSHKey])

		nd.wait_till_done()
		nd = nd.refresh()
		self.droplets.append(nd)

	def destroyDroplet(self, droplet):
		droplet.destroy()

	def createDroplets(self):
		threads = []
		for i in range(0, self.n):
			t = threading.Thread(target=self.createDroplet, args=([i]))
			threads.append(t)
			t.start()

		main_thread = threading.currentThread()
		for t in threading.enumerate():
		    if t is main_thread:
		        continue
		    logging.debug('joining %s', t.getName())
		    t.join()

		return self.droplets

	def destroyDroplets(self):
		for i in range(0, len(self.droplets)):
			self.destroyDroplet(self.droplets[i])

	def importDroplets(self, f):
		json_data = open(f)
		data = json.load(json_data)

		self.droplets = []

		for x in data:
			d = self.DOApi.Droplet.get(x)
			self.droplets.append(d)
		return self.droplets

	def exportDroplets(self):
		data = []
		for d in self.droplets:
			data.append(d.id)
		f = open('droplets.json', 'w')
		f.write(json.dumps(data))
		f.close()