# File: clustering.py
# Author: Alejandro Cirugeda
# Description:
#   The k-means function will take a list of Class points and will execute the K-means algorthm in order to assign
#   a cluster to each point.s. The execution of the algorith is in parallel
#   spliting the number of points between differents threads in order to calculate the eucladian distance and the assigment 
#   of the different clusters. The output of every iteration is witten in a file for further annalisys
import random
import math
import threading
from point import Point

def k_means(n_klustering, points, n_threads):

    write_results("../output/initial_points.txt", points)   # We wrote the values of the
    centroids = create_random_controids(n_klustering)
    # We split the list for each thread
    chunks = split_points(points, n_threads) 
  
    iteration = 0
    while True:
        
        assing_nearnest_centroid_concurrency(chunks, centroids)   

        new_centroids = calculate_new_centroids_concurrency(chunks, centroids)

        print("Old centroids: " + str(centroids))
        print("New centroids: " + str(new_centroids))

        if centroids == new_centroids or iteration > 50: #if centroids didn't change we stop the algorithm
            break
        
        # We write values into the file
        filename = "klustering_" + str(iteration) + ".txt"
        #write_results(filename, points, centroids)

        centroids = new_centroids
        iteration += 1

    print("K-means execute correctly")
     # We write values into the file
    filename = "final_points.txt"
    write_results(filename, points, centroids)
    return



def eucladian_distance(x, y):
    """
    Returns the distance between two different points
    """
    distance =  ((x.x - y.x)**2) + ((x.y - y.y)**2)
    return distance



def create_random_controids(n_klustering):
    """
    Create a new point that will work as centroid of a cluster. Will start with a 
    random position.
    """
    centroids = [None] * n_klustering
    random.seed(2345)
    
    for i in range(0, n_klustering):
        random_x = float("%.3f" % random.uniform(-10, 10 ))
        random_y = float("%.3f" % random.uniform(-10, 10))
        print("Random centroid: " + str(random_x) + " - " + str(random_y))
        
        centroids[i] = Point(random_x, random_y)

    centroids[0] = Point(0, 240)
    centroids[1] = Point(0.3, 232)
    centroids[2] = Point(0.56, 238)
    return centroids




def assign_nearnest_centroid(points, centroids):
    """
    Goes thought the list of points and assign each one to the centroid which in more near
    """
    for point in points:
        distances = []
        for centro in centroids:
            distances.append( eucladian_distance(point, centro))

        point.cluster = distances.index(min(distances)) + 1  #index start in 0 - cluster start in 1

    return points



def write_results(filename, points, centroids = []):
    """
    Write the state of the point into a file. Write x, y and kluster_id
    """
    path = "../output/" + str(filename)
    f = open(path, 'w')
    for point in points:
        f.write("%.3f , %.3f , %d \n" % (point.x , point.y , point.cluster))
        
    # Write the centroids
    for point in centroids:
         f.write("%.3f , %.3f , %d \n" % (point.x , point.y , point.cluster))

    f.close
    return


def split_points(points, n_chunks):
    """
    Split the list of points into similar size chunks. Return the list of chucka
    """
    
    out = []
    if n_chunks < 2:
        out.append(points)
        return out

    avg = len(points) / float(n_chunks)
    last = 0.0
    while last < len(points):
        out.append(points[int(last):int(last + avg)])
        last += avg
    return out


def assing_nearnest_centroid_concurrency(point_chunk, centroids):
    threads = []

    for chunk in point_chunk:
        x = threading.Thread(target = assign_nearnest_centroid, args=(chunk, centroids))
        threads.append(x)
        x.start()

    for i in range(len(threads)):
        x.join()
    
    return point_chunk


def calculate_new_centroids(n_clusters, points, value_x , value_y, counter, lock):
    """
    This method Will be execute by the threads. Each thread will calculate the avg. 
    position of his chunk of points and add the result to variables avgx and avgy 
    guarded by a lock share bettween threads
    """
    local_counter        = [0] * n_clusters
    local_x              = [0] * n_clusters
    local_y              = [0] * n_clusters

    # Sum of values in the chunk
    for point in points:
        index = point.cluster - 1 #compensate index with kluster id

        local_counter[index] += 1
        local_x[index] += float("%.3f" % point.x)
        local_y[index] += float("%.3f" % point.y)
    

    # update the value
    for i in range(n_clusters):

        lock.acquire()
        value_x[i] += float("%.3f" % (local_x[i]))
        value_y[i] += float("%.3f" % (local_y[i]))
        counter[i] += local_counter[i]
        lock.release()
    
    return



def calculate_new_centroids_concurrency(point_chunk, centroids):
    n_cluster = len(centroids)

    threads = []
    lock = threading.Lock()
    value_x          = [0] * n_cluster
    value_y          = [0] * n_cluster
    counter          = [0] * n_cluster

    for chunk in point_chunk: 
        x = threading.Thread(target = calculate_new_centroids, args=(n_cluster, chunk, value_x, value_y, counter, lock))
        threads.append(x)
        x.start()

    # Wait for all the threads to finish
    for i in range(len(threads)):
        x.join()
    
    # Calculate the avg beetween threads and add it to the new list
    new_centroids  = [] 
    avg_x          = [0] * n_cluster
    avg_y          = [0] * n_cluster

    for i in range(n_cluster):

        if counter[i] != 0:
            avg_x[i] = float("%.3f" %(value_x[i] / counter[i]))
            avg_y[i] = float("%.3f" %(value_y[i] / counter[i]))
            new_centroids.append(Point(avg_x[i], avg_y[i]))
        else:
            avg_x[i] = float("%.3f" % random.uniform(0, 5))
            avg_y[i] = float("%.3f" % random.uniform(0, 5))
            new_centroids.append(Point(avg_x[i], avg_y[i]))


    return new_centroids