# first line: 232
@memory.cache
def get_california_housing() -> Tuple[np.ndarray, np.ndarray]:
    """Fetch the California housing dataset from sklearn."""
    datasets = pytest.importorskip("sklearn.datasets")
    data = datasets.fetch_california_housing()
    return data.data, data.target
