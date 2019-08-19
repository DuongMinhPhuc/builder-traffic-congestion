import csv
import xml.etree.ElementTree as ET
tree = ET.parse('datastreets.xml')
root = tree.getroot()



def savetoCSV(newsitems, filename):
    # specifying the fields for csv file
    fields = ['wayid','nodes']
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


ways = []

for child in root:
    check_bound = 0
    if child.tag == 'way':
        way = {}
        # print(child.tag, child.attrib)
        way['wayid'] = child.attrib['id']
        num_node = 1
        way['nodes'] = ''
        for node in child:
            # print(node.tag, node.attrib)
            if node.tag == 'nd':
                way['nodes'] += node.attrib['ref']+','
                num_node += 1
            #check boundway
            if node.tag == 'tag':
                if node.attrib['v'] == 'roundabout':
                    check_bound = 1

            # if node.tag == 'tag':
            #     if node.attrib['k'] == 'name':
            #         way['streetname'] = (node.attrib['v'])
        way['nodes'] = way['nodes'].rstrip(',')
        print(way)
        if check_bound == 1:
            ways.append(way)

        # way = {}
        # way['id'] = child.attrib['id']
        # way['lat'] = child.attrib['lat']
        # way['lon'] = child.attrib['lon']
        # ways.append(way)

# print(ways)
savetoCSV(ways, 'boundways.csv')

