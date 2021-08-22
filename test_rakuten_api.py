import rakuten_api

def test_search_items():
    res = rakuten_api.search_items("チーズケーキ")
    assert len(res) > 0

def test_get_maxmin_price():
    res = rakuten_api.get_maxmin_price("チーズケーキ")
    assert len(res) > 0

def test_get_ranking():
    res = rakuten_api.get_ranking(100283)
    assert len(res) > 0