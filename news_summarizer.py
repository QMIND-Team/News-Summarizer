# -*- coding: utf-8 -*-
"""news_summarizer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19B4bLSecBxyP2vh71k_Q4-XH9qoQcnmO
"""

def news_summarizer(url):
    import requests

    import webbrowser
    from bs4 import BeautifulSoup
    from flask import request
    import selenium
    from user_agents import parse
    
    article = ""
    #calls a response type object from the URL given.
    page = requests.get(url)
    #parse the HTML from the response object with BeautifulSoup's html parser
    soup = BeautifulSoup(page.content, 'html.parser')
    #first try to find all tags with <p/> that have a "c-article body text" class, this will filter all text
    # not related to the article. If the page is not structured with such id, just parse all <p/> tags.
    #try:

    #If CNN article then:
    exception1 = "cnn.com"
    exception2 = "thestar.com"
    if exception1 in url:
      paragraphs = soup.find_all('div', "zn-body__paragraph")

    # If the Toronto Star:
    elif exception2 in url:
      paragraphs = soup.find_all('p', "text-block-container")


# Generic case
    else:
    # If just about any other news site:
     paragraphs = soup.find_all('p', "c-article-body__text")
  
    #concatenate all paragraphs together into one large string to pass through to the mode
    for paragraph in paragraphs:
        #drop all HTML tags and convert to string
        paragraph = paragraph.get_text()
        if ("." in paragraph):
            article += paragraph
    print((article))
    print(len(article))
    return article