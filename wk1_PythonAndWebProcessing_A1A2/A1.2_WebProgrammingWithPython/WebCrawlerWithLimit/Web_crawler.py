import MyWebCrawlerUtils

seedUrl = "http://adrianmoore.net/com661/test_index.html"
MAX_DEPTH = 1

to_crawl = [[seedUrl, 0]]
crawled = []

# while to_crawl:
#     url = to_crawl.pop()
#     crawled.append(url)
#     # url = [[seedUrl, 0]]
#     new_links = MyWebCrawlerUtils.get_all_new_links_on_page(url, crawled)
#     # to_crawl = list(set(to_crawl) | set(new_links))

while to_crawl:
    url = to_crawl.pop()
    if url[1] > MAX_DEPTH:
        url = to_crawl.pop()
    crawled.append(url)
    # url = [[seedUrl, 0]]
    new_links = MyWebCrawlerUtils.get_all_new_links_on_page(url, crawled)

    to_append = []
    for new_link in new_links:
        isInside = False
        for to_crawlurl in to_crawl:
            if to_crawlurl[0] == new_link[0]:
                isInside = True
                break
        if not isInside:
            to_append.append(new_link)
    print(to_crawl)
    to_crawl.extend(to_append)
    print(to_append)
    print("========================")




print(crawled)