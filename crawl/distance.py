import csv
import geopy.distance

def savetoCSV(newsitems, filename):
    # specifying the fields for csv file
    fields = ['node1', 'node2', 'distance']
    # for i in range(1,75):
    #     fields.append('node'+str(i))
    # print(fields)
    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        # [item.encode("utf-8") for item in newsitems]

        writer.writerows(newsitems)

with open('relation2.csv') as f:
    relations = [{k: str(v) for k, v in row.items()}
for row in csv.DictReader(f, skipinitialspace=True)]

with open('nodes.csv') as f:
    nodes = [{k: str(v) for k, v in row.items()}
for row in csv.DictReader(f, skipinitialspace=True)]

for relation in relations:
    node = relation['node']
    relation_nodes = relation['relation_nodes'].split(',')
    distance = {}
    distances = []
    node1 = (0,0)
    node2 = (0,0)
    for relation_node in relation_nodes:
        distance['node1'] = node
        distance['node2'] = relation_node
        for node in nodes:
            if node['id'] == node:
                node1 = (int(node['lat']),int(node['lon']))
                print(node1)
            if node['id'] == relation_node:
                node2 = (int(node['lat']),int(node['lon']))
        # coords_1 = (nodes[node]['lat'], nodes[int(node)]['lon'])
        # coords_2 = (nodes[node]['relation_node'], nodes[int(node)]['relation_node'])
        print(node1)
        distance['distance'] = geopy.distance.vincenty(node1, node2).km
        distances.append(distance)

savetoCSV(distances, 'distance.csv')



