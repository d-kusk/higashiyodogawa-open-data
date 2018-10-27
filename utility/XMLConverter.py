import xmltodict


class XMLConverter():
    def __init__(self):
        pass

    def convertToDict(self, law):
        return xmltodict.parse(law)
