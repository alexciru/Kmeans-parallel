# Kmeans-parallel
Project realize in Python where the K-means algorithm is implemented with parallel programming libraries with the objective of increasing the performance of the algorithm with big datasets.


# Introduction
The objective of this project it’s to implement the clustering algorithm: K-means. This algorithm 
is used in data mining for finding patterns in the dataset. The objective of this project is to 
present a design and implementation of the algorithm with parallel implementation in python.
The K-means algorithm is a simple algorithm that works as follows:
1. We generate one centroid random point for each cluster we want to classify.
2. We assign each point to the nearest centroid. For this project we will use the Euclidean 
distance.
3. Calculate the new position of the Centroid with the average position of the points assig 
to that centroid
4. With the new position of the centroid we assign the nearest point and repeat the 
process until the position of the centroid not vary


# Input and output
This project will receive the input for a .txt file. In this file we will read the x and y position. After 
the execution of the program we will write the output in another file writing the x and y position 
and the cluster where it belongs. We will write a file for every iteration in the algorithm in order to 
see the progression of each iteration
Once we have the output in the file, we will use Gnuplot, an open plotting tool, in order to plot 
the results in a graphic and realise a further analysis in order to take conclusions if possible.

# Structure of program

The program is structure as follows:
- Point.py: File where the point Class is storage. We will create an instance of a point for 
every entry in the input. The Point class will also storage the cluster where is assign
- cluster.py: File where the algorithm is executed. The Thread library is also imported for 
the parallel execution. In this file we also create an output file for each iteration of the 
algorithm.
- Main.py: In this file we read the input from file and we call the algorithm function. In this 
file we calculate the execution time in order to study the performance of the algorithm if 
we vary the number of entries in the input or the number of threads.
We will use the parallelism in the execution of the k-means algorithm, for the 2 most consumingtime operation:
1. The calculation of the Euclidian distance between point and centroid
2. The calculation of the new centroids
Both operations are performed in the cluster.py file. After the reading of the input file and the 
creation of the points we divide the list of points into n chunks and create n threads assigning 
each one of them a different chuck. After the operations the main process wait for the 
calculation of the threads and continue with the execution of the algorithm.
EDAMI PROJECT 3
Experiments
In order test the efficiency of the algorithm we have 3 different experiments with different 
datasets:
1. Iris Data (around 130 entries)
2. Artificial database (8000 entries)
3. Household power consumption database (2 million entries)
1. Iris dataset:
The objective of this experiment is to test if the k-means algorithm work properly with small 
numbers of entries. With this database there is have been a lot of experiments for classification 
and we can check if we obtain good results. The iris database is formed with 150 instances of 
flower belonging to 3 different classes. 
This was one of the first experiments and was mainly used to check the algorith while was 
writing.
As we can see in the result, we don’t see an improvement in the performance with the parallel 
execution due to the small dimension of the dataset.


![iris data](/output/iris_result/iris.png "iris data")
![iris data](\output\iris_result\iris.png "iris data kmeans")


### Threads average
1 0.107 ms 0.098 ms 0.122 ms 0.109 ms
2 0.125 ms 0.132 ms 0.130 ms 0.134 ms
3 0.137 ms 0.142 ms 0.148 ms 0.142 ms
4 0.140 ms 0.154 ms 0.151 ms 0.148 ms


2. Artificial dataset:
This dataset is formed of 8000 instances and was created by a tool called: MlDemos, a tool 
used for education and learning of IA techniques
The main objective is to see how the algorithm behave with some notorious number of 
instances with some clear cluster in order to check both the assignment of the clusters and the 
execution time.
As we can see in the result table there is a slightly improvement in the performance, but once 
we are used to many threads the performance decreases again.

### Threads average
1 0.654 ms 0.670 ms 0.633 ms 0.635 ms
2 0.577 ms 0.633 ms 0.672 ms 0.627 ms
3 0.606 ms 0.579 ms 0.588 ms 0.591 ms
4 0.554 ms 0.524 ms 0.541 ms 0.541 ms


3. Power Consummation:
This dataset has 2075259 instances and the point of the experiment is to take the 
implementation to the limit and, specially, to study how the algorithm performs with such high 
numbers.
The household power consumption has information about the electric measurements in a house 
between 2007 and 2010. In order to use this dataset, it needed to be cleaned, removing the 
empty instances. This dataset is not mean to be used for clustering, therefore we will not be 
able to take conclusion about the dataset.
For the huge number of instances, it can only be done 1 execution per number of threads.
### Threads average
1 0.654 ms 0.670 ms 0.633 ms 0.635 ms
2 0.577 ms 0.633 ms 0.672 ms 0.627 ms
3 0.606 ms 0.579 ms 0.588 ms 0.591 ms
4 0.554 ms 0.524 ms 0.541 ms 0.541 ms


As we can see for this huge database, we can see a huge increase in the performance
once we reach around 220 threads the performance decreases again.

###Issues with project:
One issue that is worth mentioning is the problem with the selection of the random centroids, for 
this test we used a seed in order to prevent any problems. The issue comes when one random 
centroid is situated in a position where no points are assigning to it. In order to fix we select 
another random point and hope it selected a better position. This case is very rare but, in this 
case, select another random position worked.
Another problem was the stop criteria, in the first version the stop criteria was once the 
centroids didn’t change between iterations but with higher databases could never stop because 
it enters a loop of position where a centroid oscillated between to values. It was once tried to be 
fixed it, adding a marginal error for the position of centroids. But at the end the best option was 
to add a limited number of the algorithm just in case the execution of the algorithm prolongates
too much.

# CONCLUSION
As we can see in the previous experiments, the execution time decrease when we execute the 
algorithm with parallelism, specially, when we work with big databases. Although the 
performance can vary depending on different factors such as the first position of the centroids, 
the number of iterations of the algorithm or other processes that can run in the same machine.
Another important conclusion that the output of the program depends of the first position of the 
centroids. If the initial centroids are selected properly, the final centroids will be calculated with 
less iterations of the algorithm and with less computational power.
