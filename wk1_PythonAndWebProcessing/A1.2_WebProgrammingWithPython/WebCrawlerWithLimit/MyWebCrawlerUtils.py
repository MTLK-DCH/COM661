import urllib.request

def get_all_new_links_on_page(page, prev_links):
    depth = page[1] + 1
    page = page[0]
    response = urllib.request.urlopen(page)

    html = str(response.read())

    links, pos = [], 0
    all_found = False

    while not all_found:
        tag_start = html.find("<a href=", pos)
        if tag_start > -1:
            # find url
            href = html.find('"', tag_start + 1)
            end_href = html.find('"', href + 1)
            url = html[href + 1: end_href]
            if url[:5] == "http:" or url[:6] == "https:":           
                if url[-1] == "/":
                    url = url[:-1]
                isInside = False
                for prev_link in prev_links:
                    if url == prev_link[0]:
                        isInside = True
                        break
                if not isInside and url not in links:
                    links.append([url, depth])
            # search the end of attribute
            close_tag = html.find("</a>", tag_start)
            pos = close_tag + 1
        else:
            all_found = True

    return links