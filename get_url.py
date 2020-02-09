# -*- coding: utf-8 -*-
"""get_url.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Us7gzE7b8EO1bg_7Pqwy7-Mxb6rXaa2m
"""

def get_url(user_input):
    
  import pyperclip
  import pyautogui
  import time
  url = user_input
  #click anywhere on the webpage to focus on the tab
  pyautogui.click(0,200)
  #in case the location clicked was a link object, wait until page refreshes
  time.sleep(4)
  pyautogui.press('f6')
  pyautogui.hotkey('ctrl', 'c')
  #get the copied url from the clipboard and pass it through to the
  #news_summarizer function
  url = pyperclip.paste()
  #news_summarizer(url)
  return url