import skiff
s = skiff.rig('31c9796a2ba7c4968da001958fd85fd9bea056a88a6ad434e082351a4f80ccdf')
droplets = s.Droplet.all()
print droplets
# nd = s.Droplet.create(name='test',
# 			  region='nyc3',
# 			  size='512mb',
# 			  image='ubuntu-14-04-x64')

# nd.wait_till_done()

# nd = nd.refresh()
# print nd