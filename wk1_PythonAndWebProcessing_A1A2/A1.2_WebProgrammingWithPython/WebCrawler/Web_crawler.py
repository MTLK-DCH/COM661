import MyWebCrawlerUtils

seedUrl = "http://adrianmoore.net/com661/test_index.html"

to_crawl = [seedUrl]
crawled = []

step = 0
while to_crawl:
    print()
    print('step:' + str(step))
    print('---------------------')
    print('to_crawl=', to_crawl)
    url = to_crawl.pop()
    print('url=' + url)
    crawled.append(url)
    print('crawled=', crawled)
    new_links = MyWebCrawlerUtils.get_all_new_links_on_page(url, crawled)
    print('new_links=', new_links)
    to_crawl = list(set(to_crawl) | set(new_links))
    print('to_crawl', to_crawl)
    step += 1

print(crawled)