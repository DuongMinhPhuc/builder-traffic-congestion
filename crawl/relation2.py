import csv


def savetoCSV(newsitems, filename):
    # specifying the fields for csv file
    fields = ['node','relation_nodes']
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

with open('relationfix.csv') as f:
    relations = [{k: str(v) for k, v in row.items()}
for row in csv.DictReader(f, skipinitialspace=True)]

# print(relations)
with open('ways.csv') as p:
    ways = [{g: str(f) for g, f in row.items()}
for row in csv.DictReader(p, skipinitialspace=True)]

# print(ways)

for way in ways:
    nodes_of_way = way['nodes'].split(',')
    # nodes_of_way = list(map(int, nodes_of_way))
    first_node = nodes_of_way[0]
    last_node = nodes_of_way[-1]
    new_relations = []
    for relation in relations:
        relation_nodes = relation['relation_nodes'].split(',')
        # for i in range(len(relation_nodes)):
        #     relation_nodes[i] = int(relation_nodes[i])
        # print('check type: ', type(relation_nodes[0]))
        # print(relation_nodes)
        # relation_nodes = list(map(int, relation_nodes))
        if (last_node in relation_nodes) and (first_node in relation_nodes):
            new_relations.append(relation['node'])
    if len(new_relations)>1:
        for new_node in new_relations:
            for relation in relations:
                if relation['node'] == new_node:
                    relation['relation_nodes'] += ','+','.join(str(x) for x in new_relations)
                    # relation['relation_nodes'].remove(relation['node'])
                    print('new relation',relation['relation_nodes'])


savetoCSV(relations, 'relation2.csv')





