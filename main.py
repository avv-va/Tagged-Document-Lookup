import argparse

from algorithm.config import DOCUMENTS_ADDRESS, QUERY_ADDRESS
from algorithm.naive import query as naive_query
from algorithm.smart import query as smart_query, preprocess
from algorithm.reader import get_all_documents_and_tags, get_query_input


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--algorithm', type=str, required=True, help='Algorithm Type. Enter either naive or smart')
    return parser.parse_args()


if __name__ == "__main__":
    all_documents, all_tags = get_all_documents_and_tags(DOCUMENTS_ADDRESS)
    query_tags = get_query_input(all_tags, QUERY_ADDRESS)

    if get_args().algorithm == "naive":
        result = naive_query(all_documents, query_tags)
    else:
        preprocess(all_documents)
        result = smart_query(all_documents, query_tags)

    for doc in result:
        print(doc.name)
