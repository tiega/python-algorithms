import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance

def euclidean_distance(x, Y):
    return np.sqrt(np.sum(np.square(x - Y)))

def kmeans(pts, centroids, plot=True):
    data = np.array(pts, dtype=np.float64)
    centroids = np.array(centroids, dtype=np.float64)
    centroidIdxOld = 1
    centroidIdxNew = np.zeros([len(centroids), len(data)], dtype=np.uint8)
    idx = np.zeros(len(data))
    epoch = 0

    while True:
        centroidIdxOld = centroidIdxNew
        centroidIdxNew = np.zeros([len(centroids), len(data)], dtype=np.uint8)

        for i in np.arange(data.shape[0]):
            tempDis = [euclidean_distance(c, data[i]) for c in centroids]
            centroidIdxNew[tempDis.index(min(tempDis)), i] = 1

        if np.sum(centroidIdxOld - centroidIdxNew) == 0:
            break

        for i in np.arange(len(centroids)):
            if data[centroidIdxNew[i]==1].size>0:
                centroids[i] = np.mean(data[centroidIdxNew[i]==1], axis=0)

        idx = np.argmax(centroidIdxNew,axis=0)
        epoch += 1

        if plot:
            plt.scatter(data[:, 0], data[:, 1], c=idx)
            plt.plot(*zip(*centroids), 'rx', linewidth=3)
            plt.title("Epoch: {}".format(epoch))
            plt.show()


    if plot:
        plt.scatter(data[:,0], data[:,1], c=idx)

        plt.plot(*zip(*centroids), 'rx', linewidth=3)
        plt.title("Final Epoch: {}".format(epoch))
        plt.show()

    print("\n  K-means clustering results: \n")
    for i in range(len(centroids)):
        print("    {:d}. Centroid: ( {:5.4} , {:5.4} )"
                .format(i+1, *centroids[i]))
    print("  Total number of points: {:d}".format(len(data)))

    return centroids, idx



if __name__ == "__main__":
    from sklearn.datasets.samples_generator import make_blobs

    X, y_true = make_blobs(n_samples=4000, n_features=2, centers=4, cluster_std=0.6, random_state=0)

    cent = [[-1,7], [2,1], [3,5], [2,0]]
    centroids, idx = kmeans(X, cent, plot=True)

    from sklearn.cluster import KMeans
    km = KMeans(n_clusters=4)
    km = KMeans(n_clusters=4)
    km.fit(X)
    y_kmeans = km.predict(X)
