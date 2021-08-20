import main

def test_search_items():
    res = main.search_items("チーズケーキ")
    assert len(res) > 0

def test_get_maxmin_price():
    res = main.get_maxmin_price("チーズケーキ")
    assert len(res) > 0

def test_get_ranking():
    res = main.get_ranking(100283)
    assert len(res) > 0