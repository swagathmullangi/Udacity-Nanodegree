#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
The output should be a dictionary with the tag name as the key
and number of times this tag can be encountered in the map as value.
Note that your code will be tested with a different data file than the 'example.osm'
"""
import xml.etree.ElementTree as ET
import pprint

def count_tags(filename):
    with open(filename, 'r+') as f:
        tree = ET.parse(f)

    tags = dict()
    for node in tree.iter():
        if node.tag in tags:
            tag_count = tags[node.tag]
            tag_count+=1
            tags[node.tag] = tag_count
        else:
            tags[node.tag] = 1

    return tags

def test():

    tags = count_tags('/Users/Baid/Desktop/denver.osm')
    pprint.pprint(tags)



if __name__ == "__main__":
    test()