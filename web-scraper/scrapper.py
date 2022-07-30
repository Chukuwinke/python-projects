#https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions


import pandas as pd
import mechanicalsoup
import sqlite3

browser = mechanicalsoup.StatefulBrowser()

browser.open("https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions")

th = browser.page.find_all("th", attrs={"class": "table-rh"})
distribution = [value.text for value in th]

print(distribution)