import csv

def savetoCSV(newsitems, filename):
    fields = ['node','relation_nodes']
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(newsitems)


with open('relation2.csv') as f:
    relations = [{k: str(v) for k, v in row.items()}
for row in csv.DictReader(f, skipinitialspace=True)]

all_nodes = []

for relation in relations:
    node = relation['node']
    relation_nodes = relation['relation_nodes'].split(',')
    for relation_node in relation_nodes:
        #xet thang node relation dang check
        for relation2 in relations:
            if relation2['node'] == relation_node:
                #coi xem no co thang node o tren o trong relation chua, neu chua thi add vao
                relation_nodes2 = relation2['relation_nodes'].split(',')
                if node not in relation_nodes2:
                    relation_nodes2.append(node)
                    relation2['relation_nodes'] = ','.join(relation_nodes2)
                    print(relation2['node'])
                    print(relation2['relation_nodes'])


savetoCSV(relations, 'relation3.csv')








