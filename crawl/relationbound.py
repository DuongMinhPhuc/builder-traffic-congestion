import csv

def savetoCSV(newsitems, filename):
    fields = ['node','relation_nodes']
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(newsitems)

with open('relation3.csv') as f:
    relations = [{k: str(v) for k, v in row.items()}
for row in csv.DictReader(f, skipinitialspace=True)]

with open('ways.csv') as f:
    ways = [{k: str(v) for k, v in row.items()}
for row in csv.DictReader(f, skipinitialspace=True)]

with open('boundways.csv') as f:
    boundways = [{k: str(v) for k, v in row.items()}
for row in csv.DictReader(f, skipinitialspace=True)]

for boundway in boundways:
    nodes = boundway['nodes'].split(',')
    list_node_relation_bound = []
    i = 1
    for node in nodes:
       for way in ways:
           nodes_of_way = way['nodes'].split(',')
           # nodes_of_way = list(map(int, nodes_of_way))
           first_node = nodes_of_way[0]
           last_node = nodes_of_way[-1]
           if node == first_node or node == last_node:
               list_node_relation_bound.append(node)
    for node_relation_bound in list_node_relation_bound:
        for relation in relations:
            if node_relation_bound == relation['node'] and (i+1 <= len(list_node_relation_bound)):
                relation['relation_nodes'] += ',' + list_node_relation_bound[i]
                i += 1
            if node_relation_bound == relation['node'] and (i-1 > len(list_node_relation_bound)):
                relation['relation_nodes'] += ',' + list_node_relation_bound[0]
                #cong node tiep theo

savetoCSV(relations, 'relation_bound.csv')


