from config import TESTCASE_ADDRESS, ALGORITHM_TYPE
from objects import Document, Tag
from naive import query as naive_query
from smart import query as smart_query

all_tags = set()
all_documents = set()


def create_or_use_existing_tag(tags_values, document):
    document_tags = set()
    for tag_value in tags_values:
        for tag in all_tags:
            if tag_value == tag.value:
                document_tags.add(tag)
                tag.add_corresponding_documents(document)
                break
        tag = Tag(tag_value)
        tag.add_corresponding_documents(document)
        all_tags.add(tag)
        document_tags.add(tag)
    return document_tags


if __name__ == "__main__":
    with open(TESTCASE_ADDRESS, 'r') as reader:
        for line in reader.readlines():
            document_with_tags = line.split(":")
            document_name = document_with_tags[0]
            tags = [tag.strip() for tag in document_with_tags[1].split(",")]
            doc = Document(document_name)
            tag_objects = create_or_use_existing_tag(tags, doc)
            doc.add_tags(tag_objects)
            all_documents.add(doc)

    naive_query(all_documents, all_tags, ["tora", "tori"])
