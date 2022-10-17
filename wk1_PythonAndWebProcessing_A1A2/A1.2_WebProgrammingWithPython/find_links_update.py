import urllib.request

url = 'http://www.ulster.ac.uk/campuses/belfast'
response = urllib.request.urlopen(url)

html = str(response.read())

pos = 0
all_found, links_found = False, 0

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
            print(url)
            links_found = links_found + 1
        # search the end of attribute
        close_tag = html.find("</a>", tag_start)
        pos = close_tag + 1
    else:
        all_found = True

print("{} hyperlinks found".format(links_found))