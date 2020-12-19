def query(documents, tags, target_tags):
    result_docs = []
    for doc in documents:
        if is_subset(doc.tags, target_tags):
            result_docs.append(doc)
    return result_docs


def is_subset(list1, list2):
    hashset = set()
    for item in list2:
        hashset.add(item)
    for item in list1:
        if item not in hashset:
            return False
    return True
