# D1: bird, tori, parande
# D2: tiger, tora, babr
# D3: tora, tori
# D4: bird, tiger

import random


def generate_tags(num_of_tags):
    tags = []
    for i in range(0, num_of_tags):
        tags.append("tag{}".format(random.randint(0, num_of_tags)))
    return tags


def generate_documents(tags, num_of_documents):
    documents = []
    for i in range(0, num_of_documents):

        number_of_tags = random.randint(1, len(tags))
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


def write_tescases(documents, queries):
    with open("testcases/documents/2.txt", "w") as writer:
        writer.write("\n".join(documents))

    with open("testcases/queries/2.txt", "w") as writer:
        writer.writelines(queries)


if __name__ == "__main__":

    # documents: 10^4 ta 10^5
    # tags: 100
    # d_t: 2 ta 7
    # query: 10 ta 40

    tags = generate_tags(3)
    documents = generate_documents(tags, 10)
    queries = generete_query_tags(tags, 4)
    write_tescases(documents, queries)
