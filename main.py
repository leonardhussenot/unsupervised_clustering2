from clustering import *
from tools import *


def test_spectral_clustering(n_individuals=2):
    data, labels = load_Yale_data()
    if n_individuals<38:
        n_max = np.where(labels==n_individuals)[0][0]
    else:
        n_max = data.shape[1]
    # n_max is the first index of individual of id n_individual+1
    for sigma in [10, 100, 500, 1000, 5000, 10000, 50000]:
        affinity = compute_affinity_matrix(data, K=3, sigma=sigma, n_pictures=n_max)
        labels = labels[:n_max]
        # print("Starting spectral clustering")
        pred_labels = SpectralClustering(affinity, n=n_individuals)
        error = clustering_error(pred_labels, labels[:n_max])
        print("prediction error for %i individuals, sigma=%i : %.2f%%" %(n_individuals, sigma, 100*error))


if __name__ == "__main__":
    test_spectral_clustering(n_individuals=15)
