#!/usr/bin/python3

''' 
Leggera Browser
Author: c64-dev (nikosl@protonmail.com) 

A bare-bones and extremely fast browser using Webkit rendering engine. 
This browser can launch websites as standalone applications, without
the need for a full-blown web browser.
'''

import PyQt5
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from PyQt5.QtNetwork import *
import sys
from lxml import html
import requests


try:
    url = sys.argv[1]
except Exception as e:
    print("Please specify url and window pixel dimensions.\n Usage: leggera <URL> x y")
    exit()

class Browser(QWebEngineView):
    
    def __init__(self):
        self.view = QWebEngineView.__init__(self)
        self.setWindowTitle('Loading... - Leggera Browser')
        self.width = int(sys.argv[2])
        self.height = int(sys.argv[3])
        self.left = 70
        self.top = 70
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.titleChanged.connect(self.adjustTitle)
        self.title = sys.argv[1]
        
    def adjustTitle(self):
        scraper = html.fromstring(requests.get(url).content)
        name = scraper.find('.//title').text
        self.setWindowTitle(name + ' - Leggera Browser')
    
    def disableJS(self):
        settings = QWebSettings.globalSettings()
        settings.setAttribute(QWebSettings.JavascriptEnabled, True)

if __name__ == '__main__':
        app = QApplication(sys.argv)
        view = Browser()
        view.show()
        view.load(QUrl(url))
        sys.exit(app.exec_())
