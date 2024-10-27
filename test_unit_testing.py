def test_load_data():
    path = "tests/unit_tests/test_data/sample.csv"
    di = DataIngestion()
    df = di.load_data(path)
    assert isinstance(df, pd.DataFrame)


@pytest.mark.parametrize("path,expected", [("path1", "The data file does not exist"),
("incorrect path", "The data file does not exist"), ("xyz.abc", "The data file does not exist")])
def test_load_data_error(path, expected):
    with pytest.raises(FileNotFoundError) as F:
        df = DataIngestion().load_data(path)
        assert F.message == expected