def query(all_documents, query_tags):
    result_docs = []
    for doc in all_documents:
        if set(doc.tags).issubset(set(query_tags)):
            result_docs.append(doc)
    return result_docs
