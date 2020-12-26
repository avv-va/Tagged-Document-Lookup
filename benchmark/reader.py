import timeit

from algorithm.reader import get_all_documents_and_tags, get_query_input
from algorithm.smart import query as smart_query, preprocess
from algorithm.naive import query as naive_query


def get_test_addresses(index):
    return f'testcases/documents/{index}.txt',  f'testcases/queries/{index}.txt'


def get_naive_setup():
    return "from algorithm.naive import query as naive_query"


def get_smart_setup():
    return "from algorithm.smart import query as smart_query"


def read_testcases(num_of_testcases, accuracy):
    naive_benchmark, smart_benchmark = [], []
    for i in range(0, num_of_testcases):
        document_address, query_address = get_test_addresses(i)
        all_documents, all_tags = get_all_documents_and_tags(document_address)
        preprocess(all_documents)
        query_tags = get_query_input(all_tags, query_address)

        time_taken_naive = timeit.timeit(stmt=lambda: naive_query(all_documents, query_tags), setup=get_naive_setup(), number=accuracy) / accuracy
        naive_benchmark.append((time_taken_naive, len(all_documents), len(query_tags)))

        time_taken_smart = timeit.timeit(stmt=lambda: smart_query(all_documents, query_tags), setup=get_smart_setup(), number=accuracy) / accuracy
        smart_benchmark.append((time_taken_smart, len(all_documents), len(query_tags)))

    return smart_benchmark, naive_benchmark
