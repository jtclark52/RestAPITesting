import requests

url = "https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json"

def test_ddg0():
    response = requests.get(url)
    my_jason = response.json()
    headings = my_jason['Heading']
    assert "Presidents of the United States" in headings
    assert len(headings) == 31

def test_ddg1():
    response = requests.get(url)
    my_jason = response.json()
    r_topics = my_jason['RelatedTopics']
    assert len(r_topics) == 50

def test_ddg3():
    response = requests.get(url)
    my_jason = response.json()
    r_topics = my_jason['RelatedTopics']
    assert (str(r_topics).count('Text')) == 50
