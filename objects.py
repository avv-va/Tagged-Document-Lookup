class Document:
    def __init__(self, name, tags):
        self.name = name
        self.tags = tags


class Tag:
    # documents = []

    def __init__(self, value):
        self.value = value

    # def add_corresponding_document(self, doc):
    #     self.documents.append(doc)
