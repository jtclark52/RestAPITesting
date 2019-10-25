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

# test should fail because there should only be 45 'Text' entries since there are 45 presidents but there are 50 entries under 'Text'
def test_ddg3():
    response = requests.get(url)
    my_jason = response.json()
    r_topics = my_jason['RelatedTopics']
    assert (str(r_topics).count('Text')) == 45
