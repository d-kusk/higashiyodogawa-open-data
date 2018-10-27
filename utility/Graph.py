from external.Geocoding import Geocoding


class Graph():
    def __init__(self):
        self.graph = {}

    def appendBasicInfo(self, data):
        self.graph['@type'] = "schema:Place"
        if "name" in data:
            self.graph['name'] = data['name']
        if "address" in data:
            self.graph['address'] = data['address']

    def appendLocation(self, data):
        if "address" in data:
            local_dict = Geocoding().location(data['address'])
            # print(local_dict)

            self.graph['geo'] = {}
            self.graph['geo']['@type'] = "schema:GeoCoordinates"
            self.graph['geo']['latitude'] = local_dict['latitude']
            self.graph['geo']['longitude'] = local_dict['longitude']

    def appendCateogry(self, category_name):
        self.graph['category'] = category_name

    def getGraph(self):
        return self.graph
