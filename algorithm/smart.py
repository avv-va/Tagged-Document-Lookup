from collections import Counter


def preprocess(all_documents):
    for doc in all_documents:
        for tag in doc.tags:
            tag.add_document(doc)


def query(all_documents, query_tags):
    documents_of_query_tags = []
    for tag in query_tags:
        documents_of_query_tags += tag.documents
    documents_with_numbers_of_repetition = Counter(documents_of_query_tags)

    result_docs = []
    for doc, repetition_num in documents_with_numbers_of_repetition.items():
        if len(doc.tags) == repetition_num:
            result_docs.append(doc)

    return result_docs
