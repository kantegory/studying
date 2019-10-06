import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class CLUSTER:

    def __init__(self, centroid):
        self.patterns = []
        self.centroid = centroid

    def add_pattern(self, pattern):
        self.patterns.append(pattern)

    def set_centroid(self, centroid):
        self.centroid = centroid

    def update_centroid(self):
        if len(self.patterns) != 0:
            pattern_matrix = np.asanyarray(self.patterns)
            mean_matrix = pattern_matrix.mean(0)
            self.centroid = list(mean_matrix)

    def set_intervals(self, pattern):
        return np.linalg.norm(np.asarray(self.centroid) - np.asarray(pattern))

    def clean_patterns(self):
        self.patterns = []

    def get_partial_distortion(self):
        partial_distortion = 0

        for index in range(len(self.patterns)):
            partial_distortion += np.linalg.norm(np.asarray(self.centroid) - np.asarray(self.patterns[index]))

        return partial_distortion

    def print_cluster(self):
        print("Centroids:")
        print(self.centroid)


class LBG:

    def __init__(self, dataset, quants, error, iters):
        self.dataset = dataset
        self.quants = quants
        self.error = error
        self.iters = iters
        self.clusters = []
        self.old_distortion = 0
        self.new_distortion = 0
        self.codebook = []

    def set_codebook(self):
        for index in range(len(self.clusters)):
            self.codebook.append(self.clusters[index].centroid)

    def get_codebook(self):
        return np.asarray(self.codebook)

    def clean_clusters(self):
        for index in range(len(self.clusters)):
            self.clusters[index].clean_patterns()

    def add_cluster(self, centroid):
        cluster = CLUSTER(centroid)
        self.clusters.append(cluster)

    def generate_clusters(self):
        indexes = np.random.choice(range(len(self.dataset)), self.quants, replace=False)
        for index in indexes:
            self.add_cluster(list(self.dataset[index]))

    def allocate_closest_cluster(self):

        for pattern in self.dataset:
            lowest_interval = float("inf")
            lowest_index = -1

            for index in range(len(self.clusters)):
                interval = self.clusters[index].set_intervals(list(pattern))

                if interval < lowest_interval:
                    lowest_interval = interval
                    lowest_index = index

            self.clusters[lowest_index].add_pattern(list(pattern))

    def update_centroids(self):
        for index in range(len(self.clusters)):
            self.clusters[index].update_centroid()

    def set_distortion(self):
        distortion = 0

        for index in range(len(self.clusters)):
            distortion += self.clusters[index].get_partial_distortion()

        self.old_distortion = self.new_distortion
        self.new_distortion = distortion

    def get_distortion_flag(self):
        return (self.old_distortion - self.new_distortion) / self.new_distortion

    def print_clusters(self):
        for cluster in self.clusters:
            cluster.print_cluster()

    def run(self):
        self.generate_clusters()
        iters_partial = 1

        self.print_clusters()

        # Make twice to initiate distortions
        for i in range(2):
            self.clean_clusters()
            self.allocate_closest_cluster()
            self.update_centroids()
            self.set_distortion()
            iters_partial += 1

        # While iters_partial is different of max iterations and distortion flag > error
        while (iters_partial < self.iters) and (self.get_distortion_flag() > self.error):
            self.clean_clusters()
            self.allocate_closest_cluster()
            self.update_centroids()
            self.set_distortion()
            iters_partial += 1
        self.set_codebook()


def create_data(mu, sigma, rows, cols):
    return np.random.normal(mu, sigma, (rows, cols))


def paint_plot(df, centroids):
    plt.scatter('x', 'y', color='g', data=df)
    plt.scatter('x', 'y', color='b', data=centroids)
    plt.show()


def main():
    mu = 0
    sigma = 1
    rows = 100
    cols = 2
    quants = 8
    error = 0.5 * 10**(-4)
    max_iter = 3000
    dataset = create_data(mu, sigma, rows, cols)
    vq_lg = LBG(dataset, quants, error, max_iter)
    vq_lg.run()
    codebook = vq_lg.get_codebook()
    df = pd.DataFrame(data=dataset, columns=['x', 'y'], index=range(rows))
    centroids = pd.DataFrame(data=codebook, columns=['x', 'y'], index=range(quants))
    print(codebook)
    paint_plot(df, centroids)


if __name__ == "__main__":
    main()
