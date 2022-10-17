import urllib.request

def get_all_new_links_on_page(page, prev_links):
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
                if url not in links and url not in prev_links:
                    links.append(url)
                    print(url)
            # search the end of attribute
            close_tag = html.find("</a>", tag_start)
            pos = close_tag + 1
        else:
            all_found = True

    return links