class Document:
    def __init__(self, name, tags):
        self.name = name
        self.tags = tags


class Tag:

    def __init__(self, value):
        self.value = value
        self.documents = []

    def add_document(self, doc):
        self.documents.append(doc)
