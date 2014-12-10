from initializeNodes import *
from Topologies import *
import paramiko
import logging
import sys
import time
import select
import threading

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def InstallProtocol(host, rsaFile, j):
	i = 1
	while True:
		print 'Connecting through SSH'

		try:
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(host, username='root', key_filename=rsaFile)
			logging.debug('Connected to %s' % host)
			break
		except paramiko.AuthenticationException:
			logging.debug('Authentication failed when connecting to %s' % host)
			sys.exit(1)
		except:
			logging.debug('Could not SSH to %s, waiting for it to start' % host)
			i+=1
			time.sleep(2)

		if(i == 5):
			logging.debug("Could not connect to %s. Giving up" % host)
			sys.exit(1)

	algorithmFile = '/Users/andreRocha/Documents/Projects/Code/DistRunner/algorithm.py'
	dataFile = '/Users/andreRocha/Documents/Projects/Code/DistRunner/data/node'+str(j)+'.json'

	sftp = ssh.open_sftp()
	sftp.put(algorithmFile, '/root/algorithm.py')
	sftp.put(dataFile, '/root/node.json')
	stdin, stdout, stderr = ssh.exec_command('python algorithm.py')

	# Setup for non-blocking execution
	while not stdout.channel.exit_status_ready():
		if stdout.channel.recv_ready():
			r1, w1, x1 = select.select([stdout.channel], [], [], 0.0)
			if len(r1) > 0:
				logging.debug(stdout.channel.recv(1024))

def startInstall(nodes, rsaFile):
	threads = []
	for i in range(0, len(nodes)):
		host = nodes[i].networks['v4'][0]['ip_address']
		t = threading.Thread(target=InstallProtocol, args=(host, rsaFile, i))
		threads.append(t)
		t.start()

	main_thread = threading.currentThread()
	for t in threading.enumerate():
	    if t is main_thread:
	        continue
	    logging.debug('joining %s', t.getName())
	    t.join()