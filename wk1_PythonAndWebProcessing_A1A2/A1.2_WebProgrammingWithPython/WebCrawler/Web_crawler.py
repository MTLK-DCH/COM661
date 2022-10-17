import MyWebCrawlerUtils

seedUrl = "http://adrianmoore.net/com661/test_index.html"

to_crawl = [seedUrl]
crawled = []

while to_crawl:
    url = to_crawl.pop()
    crawled.append(url)
    new_links = MyWebCrawlerUtils.get_all_new_links_on_page(url, crawled)
    to_crawl = list(set(to_crawl) | set(new_links))

print(crawled)