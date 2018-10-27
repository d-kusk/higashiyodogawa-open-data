from utility.CSV import CSV
from utility.JSONLD import JSONLD
from utility.Graph import Graph


def main():
    csv = CSV()
    csv.filePath('./assets/hinan2.csv')
    place_data = csv.extract(shape)
    print("place_data", place_data)

    jsonld = JSONLD()
    jsonld.setGraph(place_data)
    jsonld.create("hinan2.jsonld")


def shape(data):
    graph = Graph()
    graph.appendBasicInfo(data)
    graph.appendLocation(data)
    graph.appendCateogry("一時避難所")
    return graph.getGraph()


if __name__ == '__main__':
    main()
