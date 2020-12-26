
from algorithm.naive import query
import random

def generate_tags(num_of_tags):
    tags = []
    for i in range(0, num_of_tags):
        tags.append(f'tag{i}')
    return tags


def generate_documents(tags, num_of_documents, num_of_doc_per_tag):
    documents = []
    for i in range(0, num_of_documents):

        number_of_tags = random.randint(num_of_doc_per_tag[0], min(num_of_doc_per_tag[1], len(tags)))
        random_tags = random.sample(tags, k=number_of_tags)

        doc_line = f'D{i}: '
        for t in range(0, len(random_tags)):
            if t != len(random_tags) - 1:
                doc_line += f'{random_tags[t]}, '
            else:
                doc_line += f'{random_tags[t]}'
        documents.append(doc_line)
    return documents


def generete_query_tags(tags, num_of_queries):
    query_tags_to_write = []
    query_tags = random.sample(tags, k=min(num_of_queries, len(tags)))
    for i in range(0, len(query_tags)):
        if i != len(query_tags) - 1:
            query_tags_to_write.append(f'{query_tags[i]}, ')
        else:
            query_tags_to_write.append(f'{query_tags[i]}')
    return query_tags_to_write


def write_tescases(documents, queries, testcase_number):
    with open(f'testcases/documents/{testcase_number}.txt', "w") as writer:
        writer.write("\n".join(documents))

    with open(f'testcases/queries/{testcase_number}.txt', "w") as writer:
        writer.writelines(queries)


if __name__ == "__main__":
    documents_interval = (10**4, 10**5 + 1, 3000)
    queries_interval = (10, 40 + 1, 5)
    testcase_number = 0
    for doc in range(documents_interval[0], documents_interval[1], documents_interval[2]):
        for query in range(queries_interval[0], queries_interval[1], queries_interval[2]):
            tags = generate_tags(num_of_tags=100)
            documents = generate_documents(tags=tags, num_of_documents=doc, num_of_doc_per_tag=(2, 7))
            queries = generete_query_tags(tags=tags, num_of_queries=query)
            write_tescases(documents, queries, testcase_number)
            testcase_number += 1
