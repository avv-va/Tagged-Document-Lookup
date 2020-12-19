class Document:
    def __init__(self, doc_name):
        self.doc_name = doc_name

    def set_tags(self, tags):
        self.tags = tags


class Tag:
    documents = []

    def __init__(self, value):
        self.value = value

    def add_corresponding_document(self, doc):
        self.documents.append(doc)
