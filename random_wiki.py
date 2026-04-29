import requests
import webbrowser

blocked_words = ["politics", "city", "country", "geography", "town", "village"]

def exclude_articles():

    for i in range(1, 6):

        valid = False
        while not(valid):
            #Get info of random wikipedia article

            response = requests.get('https://en.wikipedia.org/api/rest_v1/page/random/summary')
            json = response.json()

            #get a summary of the random wikipaedia article

            summary = json['extract']

            #check for banned words in wikipedia article

            if not any(c in summary for c in blocked_words):
                valid = True
                print(summary)

                #get URL to open in a browser
                title = json['title']

                title = "".join(i for i in title if ord(i)<128)
                url = 'https://en.wikipedia.org/wiki/' + title.replace(" ","_")

                #open url
                webbrowser.open_new_tab(url)


#exclude_articles()



#function for searching articles based on certain keywords

wanted_words = ["Games", "games", "videos", "online", "esports", "social media", "media", "fortnite", "brawl stars", "minecraft"]

def include_articles():

    for i in range(1, 6):

        valid = False
        while not(valid):
            #Get info of random wikipedia article

            response = requests.get('https://en.wikipedia.org/api/rest_v1/page/random/summary')
            json = response.json()

            #get a summary of the random wikipaedia article

            summary = json['extract']

            #check for included words in wikipedia article

            if any(c in summary for c in wanted_words):

                valid = True

                matches = [w for w in wanted_words if w in summary]
                print(matches)

                print(summary + "\n\n")

                #get URL to open in a browser
                title = json['title']

                title = "".join(i for i in title if ord(i)<128)
                url = 'https://en.wikipedia.org/wiki/' + title.replace(" ","_")

                #open url
                webbrowser.open_new_tab(url)


#include_articles()

def scan_full_article():

    for i in range(1, 6):

        valid = False
        while not(valid):
            #Get info of random wikipedia article

            response = requests.get('https://en.wikipedia.org/api/rest_v1/page/random/html')
            html = response.text

            #check for included words in wikipedia article

            if any(c in html for c in wanted_words):

                valid = True

                matches = [w for w in wanted_words if w in html]
                print(matches)

                title = response.url
                title = title.replace("https://en.wikipedia.org/api/rest_v1/page/html/","")
                url = 'https://en.wikipedia.org/wiki/' + title

                webbrowser.open_new_tab(url)

#scan_full_article()