#oneways
#relation3
#last file relation
import csv

def savetoCSV(newsitems, filename):
    fields = ['node','relation_nodes']
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(newsitems)

with open('relation_bound.csv') as f:
    relations = [{k: str(v) for k, v in row.items()}
for row in csv.DictReader(f, skipinitialspace=True)]

with open('oneways.csv') as f:
    oneways = [{k: str(v) for k, v in row.items()}
for row in csv.DictReader(f, skipinitialspace=True)]

for oneway in oneways:
    oneway_nodes = oneway['nodes'].split(',')
    # for oneway_node in oneway_nodes:
    for i in range(1,len(oneway_nodes)):
        for relation in relations:
            if oneway_nodes[i] == relation['node']:
                # print('node:')
                # print(oneway_nodes[i])
                relation_nodes = relation['relation_nodes'].split(',')
                # print('relation_node_start:')
                # print(relation_nodes)
                for j in range(0, i):
                    if oneway_nodes[j] in relation_nodes:
                        relation_nodes.remove(oneway_nodes[j])
                relation['relation_nodes'] = ','.join(relation_nodes)
                # print('relation_node_end:')
                # print(relation_nodes)


savetoCSV(relations, 'relation_oneway_last.csv')







