import json
import requests
data=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=5b00428da5f24a4dae3f2558212dd2d8")
extractedata=data.json()
#print(extractedata)
#print(extractedata["status"])
#print(extractedata["articles"])
articles=extractedata["articles"]
#print(len(articles))
vowel="aeiou"
for i in articles:
    title=i["title"]
    count={}.fromkeys(vowel,0)
    print(title.lower())

    for x in title.lower():
        if x in count:
            count[x]=count[x]+1
    print(count)
