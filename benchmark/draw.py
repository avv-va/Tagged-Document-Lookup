import timeit
import matplotlib.pyplot as plt

def draw_2d_plot_for_specified_query_size(smart_benchmark, naive_benchmark, query_size):
    target_smart_doc_size, target_smart_time = [], []
    target_naive_doc_size, target_naive_time = [], []

    for i in range(0, len(smart_benchmark)):
        if smart_benchmark[i][2] == query_size:
            target_smart_time.append(smart_benchmark[i][0])
            target_smart_doc_size.append(smart_benchmark[i][1])

            target_naive_time.append(naive_benchmark[i][0])
            target_naive_doc_size.append(naive_benchmark[i][1])

    draw_plot_2d(target_smart_doc_size, target_smart_time, 'smart', target_naive_doc_size,
                 target_naive_time, 'naive', 'doc size', 'time', f'plot/query_constant_{query_size}.png')

def draw_2d_plot_for_specified_document_size(smart_benchmark, naive_benchmark, doc_size):
    target_smart_query_size, target_smart_time = [], []
    target_naive_query_size, target_naive_time = [], []

    for i in range(0, len(smart_benchmark)):
        if smart_benchmark[i][1] == doc_size:
            target_smart_time.append(smart_benchmark[i][0])
            target_smart_query_size.append(smart_benchmark[i][2])

            target_naive_time.append(naive_benchmark[i][0])
            target_naive_query_size.append(naive_benchmark[i][2])
    
    draw_plot_2d(target_smart_query_size, target_smart_time, "smart", target_naive_query_size, 
                 target_naive_time, "naive", "query size", "time", f"plot/doc_constant_{doc_size}.png")

def draw_3d_plot(smart_benchmark, naive_benchmark):
    doc_size, query_size, smart_time, naive_time = [], [], [], []
    for i in range(0, len(smart_benchmark)):
        smart_time.append(smart_benchmark[i][0])
        naive_time.append(naive_benchmark[i][0])
        doc_size.append(smart_benchmark[i][1])
        query_size.append(smart_benchmark[i][2])

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.plot3D(doc_size, query_size, smart_time, 'gray')
    ax.plot3D(doc_size, query_size, naive_time, 'green')

    ax.scatter3D(doc_size, query_size, naive_time, 'yellow')
    ax.scatter3D(doc_size, query_size, smart_time, 'red')

    ax.set_xlabel('doc size')
    ax.set_ylabel('query size')
    ax.set_zlabel('time')
    plt.savefig("plot/3d.png")
    plt.show()


def draw_plot_2d(x1, y1, label1, x2, y2, label2, x_axis_label, y_axis_label, address):
    plt.plot(x1, y1, label=label1)
    plt.plot(x2, y2, label=label2) 
    plt.xlabel(x_axis_label) 
    plt.ylabel(y_axis_label) 
    plt.legend()
    plt.savefig(address)
    plt.show()
