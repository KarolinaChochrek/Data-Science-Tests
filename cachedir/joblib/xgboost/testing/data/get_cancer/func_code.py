# first line: 248
@memory.cache
def get_cancer() -> Tuple[np.ndarray, np.ndarray]:
    """Fetch the breast cancer dataset from sklearn."""
    datasets = pytest.importorskip("sklearn.datasets")
    return datasets.load_breast_cancer(return_X_y=True)
