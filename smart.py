from collections import Counter


def preprocess_tags(): pass


def query(all_documents, all_tags, target_tags):
    all_tags = preprocess_tags(all_documents, all_tags)

    all_documents_in_target_tags = []
    for doc in target_tags.docs:
        all_documents_in_target_tags.append(doc)

    should_be_repeated = len(target_tags)

    result_docs = []
    documents_with_numbers_of_repetence = Counter(all_documents_in_target_tags)  # complexitiy is O(N)

    for doc, repetence_num in documents_with_numbers_of_repetence.items():
        if repetence_num == should_be_repeated and len(doc.tags) == should_be_repeated:
            result_docs.append(doc)

    return result_docs
