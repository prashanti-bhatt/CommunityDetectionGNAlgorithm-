
import sys

#lines = open('soc-wiki-Vote.txt').read().splitlines()
modularity_data = open(r'C:\Users\Sony\Desktop\ADB_gn\USAirlines\USop.txt').read().splitlines()
fo = open("Subgraph_density.txt", "w")
count = 1
total_edges = 0

for line in modularity_data:
	if count == 1:
		count += 1
		continue
	elif (count % 2) == 0:
		fo.write('{0}\n'.format(line))
	elif (count % 2) != 0:
		data = line.split(",")
		total_edges += len(data)/2
		fo.write('{0}\n'.format(len(data)/2))
	count += 1

fo.write("Total Edges in graph : {0}\n".format(total_edges))
fo.close()

#for line in lines:
	#line.lstrip()
#	data = line.split(",")
#	i = 0
#	fo.write('{0} {1} {2}\n'.format(int(data[0]), int(data[1]), 1))
# fo.close()

