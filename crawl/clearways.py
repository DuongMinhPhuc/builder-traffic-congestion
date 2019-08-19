import csv

with open('relation2.csv') as f:
    relations = [{k: str(v) for k, v in row.items()}
for row in csv.DictReader(f, skipinitialspace=True)]

print(relations)

all_relation = []
for relation in relations:
    relation_dict = {}
    relation_nodes = relation['relation_nodes'].split(',')
    #loai bo neu trung voi node
    while (relation['node'] in relation_nodes):
        relation_nodes.remove(relation['node'])
        print('delete node')
    #loai bo neu trung nhau
    relation_nodes = [x for x in relation_nodes if relation_nodes.count(x) < 2]

    relation_nodes = ','.join(str(x) for x in relation_nodes)
    if len(relation_nodes) == 1:
        relation_nodes = str(relation_nodes[0])
    print(relation_nodes)
    relation_dict['node'] = relation['node']
    relation_dict['relation_nodes'] = relation_nodes
    all_relation.append(relation_dict)

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

savetoCSV(all_relation, 'relation2.csv')


