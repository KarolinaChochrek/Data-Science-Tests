# first line: 255
@memory.cache
def get_sparse() -> Tuple[np.ndarray, np.ndarray]:
    """Generate a sparse dataset."""
    datasets = pytest.importorskip("sklearn.datasets")
    rng = np.random.RandomState(199)
    n = 2000
    sparsity = 0.75
    X, y = datasets.make_regression(n, random_state=rng)
    flag = rng.binomial(1, sparsity, X.shape)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            if flag[i, j]:
                X[i, j] = np.nan
    return X, y
