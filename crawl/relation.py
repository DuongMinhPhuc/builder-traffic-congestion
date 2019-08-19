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


#open file way-nodes
with open('ways.csv') as f:
    ways = [{k: str(v) for k, v in row.items()}
for row in csv.DictReader(f, skipinitialspace=True)]

# print(ways[5])
all_nodes_in_way = []
for way in ways:
    nodes = way['nodes'].split(',')
    #cast string to int
    nodes = list(map(int, nodes))
    print(nodes)
    all_nodes_in_way.append(nodes)

# print(all_nodes_in_way)
#way_nodes la list all node trong 1 way
relations = []
for way_nodes in all_nodes_in_way:
    first_node = way_nodes[0]
    last_node = way_nodes[-1]

    relation_of_first_node = {}
    relation_of_first_node['node'] = first_node
    relation_of_first_node['relation_nodes'] = ''

    relation_of_last_node = {}
    relation_of_last_node['node'] = last_node
    relation_of_last_node['relation_nodes'] = ''

    for way_nodes_2 in all_nodes_in_way:
        if way_nodes == way_nodes_2:
            continue
        if first_node in way_nodes_2:
            relation_of_first_node['relation_nodes'] += str(way_nodes_2[0]) + ','
            relation_of_first_node['relation_nodes'] += str(way_nodes_2[-1]) + ','
        if last_node in way_nodes_2:
            relation_of_last_node['relation_nodes'] += str(way_nodes_2[0]) + ','
            relation_of_last_node['relation_nodes'] += str(way_nodes_2[-1]) + ','

    relation_of_last_node['relation_nodes'] = relation_of_last_node['relation_nodes'].rstrip(',')
    relation_of_first_node['relation_nodes'] = relation_of_first_node['relation_nodes'].rstrip(',')
    # print(relation_of_last_node)
    # print(relation_of_first_node)
    relations.append(relation_of_first_node)
    relations.append(relation_of_last_node)


# print('relation:')
# print(relations)

savetoCSV(relations, 'relation2.csv')

#chay them file reltion fix



