from objects import Document, Tag


def get_or_create_tags(tag_values_list, all_tags):
    tags = []
    for tag_value in tag_values_list:
        exists = False
        for tag in all_tags:
            if tag_value == tag.value:
                tags.append(tag)
                exists = True
                break
        if not exists:
            tag_object = Tag(tag_value)
            tags.append(tag_object)
    return list(set(tags))


def process_documents_and_tags_input(line):
    document_with_tags = line.split(":")
    document_name = document_with_tags[0]
    tag_values_list = [tag.strip() for tag in document_with_tags[1].split(",")]
    return document_name, tag_values_list


def get_all_documents_and_tags(documents_address):
    all_documents, all_tags = [], []

    with open(documents_address, 'r') as reader:
        for line in reader.readlines():
            document_name, tag_values_list = process_documents_and_tags_input(line)

            tags = get_or_create_tags(tag_values_list, all_tags)
            document = Document(document_name, tags)

            all_tags += tags
            all_documents.append(document)

    return all_documents, all_tags


def get_query_input(all_tags, testcase_address):
    with open(testcase_address, 'r') as reader:
        query_tags_value = [tag.strip() for tag in reader.readline().split(",")]
        query_tags = get_or_create_tags(query_tags_value, all_tags)
    return query_tags
