from helper import YTHelper

def test_helper_saves_keys():
    y = YTHelper(api_key = "myKey123!")
    assert(y.getKey() == "myKey123!")
