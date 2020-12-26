from benchmark.reader import read_testcases
from benchmark.draw import draw_2d_plot_for_specified_query_size, draw_2d_plot_for_specified_document_size, draw_3d_plot
from benchmark.config import NUMBER_OF_TESTCASES, ACCURACY

if __name__ == '__main__':
    smart_benchmark, naive_benchmark = read_testcases(num_of_testcases=NUMBER_OF_TESTCASES, accuracy=ACCURACY)
    draw_2d_plot_for_specified_query_size(smart_benchmark=smart_benchmark, naive_benchmark=naive_benchmark, query_size=10)
    draw_2d_plot_for_specified_query_size(smart_benchmark=smart_benchmark, naive_benchmark=naive_benchmark, query_size=30)
    draw_2d_plot_for_specified_query_size(smart_benchmark=smart_benchmark, naive_benchmark=naive_benchmark, query_size=40)
    draw_2d_plot_for_specified_document_size(smart_benchmark=smart_benchmark, naive_benchmark=naive_benchmark, doc_size=10**4)
    draw_2d_plot_for_specified_document_size(smart_benchmark=smart_benchmark, naive_benchmark=naive_benchmark, doc_size=4 * 10**4)
    draw_2d_plot_for_specified_document_size(smart_benchmark=smart_benchmark, naive_benchmark=naive_benchmark, doc_size=10**5)
    draw_3d_plot(smart_benchmark, naive_benchmark)
