__author__ = 'xray'

# coding: gbk
from wiki_baike import url_manager, html_downloader, html_parser, html_outputer

import logging


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()  #
        self.downloader = html_downloader.HtmlDownloader()  #
        self.parser = html_parser.HtmlParser()  #
        self.outputer = html_outputer.HtmlOutputer()  #

    def craw(self, root_url):
        count = 1  #
        self.urls.add_new_url(root_url)  #
        while self.urls.has_new_url():  #
            try:
                new_url = self.urls.get_new_url()  #
                print 'craw %d:%s' % (count, new_url)
                html_cont = self.downloader.download(new_url)  #
                new_urls, new_data = self.parser.parse(new_url, html_cont)  #
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)  #
                print new_data['title']
                if count == 10:
                    break
                count += 1

            except Exception as e:
                logging.exception(e)
                print 'error'
        self.outputer.output_html()  #
        print 'ok'
if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)  #
