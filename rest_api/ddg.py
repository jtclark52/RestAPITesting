import requests

url = "https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json"

# url = 'https://duckduckgo.com/?q=presidents+of+the+united+states&t=h_&ia=list&iax=list&format=json'

def ddg():

    response = requests.get(url)

    # Status code
    status = response.status_code

    print('The status code is',status)

    # json response
    my_json = response.json()

    for key in my_json.keys():
        print(key)

    # heading
    headings = my_json['Heading']
    print('This is the Heading:', headings)
    print('This is the number of Headings:')
    print(len(headings))

    # Related Topics
    r_topics = my_json['RelatedTopics']
    # print('These are the RelatedTopics: \n', r_topics)


    for key in r_topics:
        print(key)
    print(len(r_topics))

    # Count of key pair for Text
    print(str(r_topics).count('Text'))

ddg()
