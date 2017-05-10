# -*- coding: utf-8 -*-
import requests
import sys

"""Simple program that returns live news headlines from a range of sources."""
# Uses the News API found here: https://newsapi.org/

def greetings():
    print "Which category would you like your news from?"
    print ""
    print "1. Business\n2. Entertainment\n3. Gaming\n4. General\n5. Music \
    \n6. Politics\n7. Science And Nature\n8. Sport\n9. Technology\n10. Exit"
    print ""
    choice = int(raw_input("Press a number to choose: "))

    if choice == 10:
        sys.exit()

    choices = ['business', 'entertainment', 'gaming', 'general', 'music', 'politics', 'science-and-nature', 'sport', 'technology']
    category = choices[choice - 1]
    return category

def news():
    print ""
    print "Hello there! And welcome to your personal News bot.".title()
    print ""
    while True:
        categ = greetings()

        # if categ is None:
        #     return

        sources_url = 'https://newsapi.org/v1/sources?language=en&country=us&category=' + categ
        sources_response = requests.get(sources_url)
        sources_data = sources_response.json()

        print ""
        print "Here's a collection of the latest headlines in " + categ.title() + ":"
        print ""
        for source in sources_data['sources']:
            print source['name'] + ':'
            print ""
            news_url = 'https://newsapi.org/v1/articles?source=' + source['id'] + '&sortBy=latest&apiKey=c4b7401b12c240b5a92498f4a6f58bfd'
            news_response = requests.get(news_url)
            news_data = news_response.json()
            # print news_data
            if news_data['status'] != 'error':
                print news_data['articles'][0]['title']
                print news_data['articles'][0]['url']
                print ""
            else:
                print "Cannot retrieve the latest news from this source."
                print ""


if __name__ == '__main__':
    news()
