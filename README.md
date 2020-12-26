### Tagged Document Look Up

# Run algorithm
To run the algorithm on the already 216 generated testcases in the ```testcases/``` directory, set the corresponding testcase number in ```TESTCASE_NUM``` variable in ```algorith/config.py``` file. To run on a specified input, set its address in ``DOCUMENTS_ADDRESS`` and ```QUERY_ADDRESS``` variables.

Then, enter the followig command:

```python main.py --algorithm [algorithm_type]```

Note: algorithm_type can be either ```naive``` or ```smart```.

# Benchmark
To simulate the algorithm with the generated testcases as the input, enter the following:

```python benchmark.py```

You can set the number of testcases and accuracy in the ```benchmark/config.py```.
The current benchmark, generates six 2d plots which either considers the number of documents to be constant and number of queries to be changeable or vice versa. It also generates a 3d plot. 

The generated plots, run with the current config is saved in the folder ```plot```.

Note: the name ```query_constant_30```, implies that the number of queries was 30 and the number of docs were changeable.

# Generate Testcase
The data is generated randomly by the intervals specified in ```generate.py```.
To generate your own testcases, change the intervals and enter:

```python generate.py```
