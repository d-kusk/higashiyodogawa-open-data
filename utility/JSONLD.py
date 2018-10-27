import os.path
import json
from pyld import jsonld


class JSONLD():
    __outputPath = './dist'

    def __init__(self):
        self.context = {
            "schema": "https://schema.org/",
            "name": "schema:name",
            "address": "schema:address",
            "category": "schema:category",
            "geo": "schema:geo",
            "latitude": "schema:latitude",
            "longitude": "schema:longitude"
        }
        self.graph = []

    def setGraph(self, graph):
        self.graph = graph

    def create(self, filename):
        compacted = jsonld.compact(self.graph, self.context)
        print("compacted", compacted)
        # print(json.dumps(compacted, indent=2))
        with open(os.path.join(self.__outputPath, filename), 'w') as outfile:
            json.dump(compacted, outfile)
