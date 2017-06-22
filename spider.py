#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Perlou(perloukevin@gmail.com)'

import url_manager, html_downloader, html_parser, html_outputer

class Spider(object):
    def __init__(self):
        self.urls = url_manager

    def craw(self, url):
        print(url)


if __name__ == '__main__':
    root_url = 'https://meimeifa.com/news.html#all'
    mmf_spider = Spider()
    mmf_spider.craw(root_url)
