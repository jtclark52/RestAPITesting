from test.ddg import ddg
import requests

url_ddg = "https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json"

def test_ddg0():
    resp = requests.get(url_ddg)
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]
