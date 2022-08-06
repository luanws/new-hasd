import json
import webbrowser

urls_list_1 = json.load(open('urls/1-100.json'))
urls_list_2 = json.load(open('urls/101-200.json'))
urls_list_3 = json.load(open('urls/201-300.json'))
urls_list_4 = json.load(open('urls/301-400.json'))
urls_list_5 = json.load(open('urls/401-500.json'))
urls_list_6 = json.load(open('urls/501-600.json'))

url_list = urls_list_1 + urls_list_2 + urls_list_3 + urls_list_4 + urls_list_5 + urls_list_6


def open_in_browser(url):
    webbrowser.open(url)


for url in url_list:
    open_in_browser(url)
