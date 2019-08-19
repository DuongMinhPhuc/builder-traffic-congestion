import csv

def savetoCSV(newsitems, filename):
    fields = ['node','relation_nodes']
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(newsitems)

with open('relation_last.csv') as f:
    relations = [{k: str(v) for k, v in row.items()}
for row in csv.DictReader(f, skipinitialspace=True)]

with open('nodes.csv') as f:
    nodes_lat_lon = [{k: str(v) for k, v in row.items()}
for row in csv.DictReader(f, skipinitialspace=True)]


for relation in relations:
    node1 = relation['node']
    relation_nodes = relation['relation_nodes']
    for relation_node in relation_nodes:
        #tinh khoang cach node1 and relation_node

