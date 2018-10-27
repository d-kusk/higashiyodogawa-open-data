import csv


class CSV():
    def __init__(self):
        pass

    def filePath(self, filepath):
        self.filePath = filepath

    def extract(self, shap):
        with open(self.filePath, 'r') as f:
            reader = csv.reader(f)
            # skip header and table header
            header = next(reader)
            table_header = next(reader)

            places = []
            for row in reader:
                data = {}
                data['name'] = row[0]
                data['address'] = row[1]
                places.append(shap(data))
        return places
