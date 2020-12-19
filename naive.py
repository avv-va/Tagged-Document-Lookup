def query(documents, tags, query_tags):
    result_docs = []
    for doc in documents:
        if doc.tags.is_subset(query_tags):
            result_docs.append(doc)
    return result_docs
