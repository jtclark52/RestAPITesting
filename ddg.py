import requests

url = 'https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json'

response = requests.get(url)

my_json = response.json()

# print(response.json())


for key in my_json.keys():
    print(key)

headings = my_json['Heading']
print('These are the Headings: \n', headings)

r_topics = my_json['RelatedTopics']
# print('These are the RelatedTopics: \n', r_topics)

for key in r_topics:
    print(key)

