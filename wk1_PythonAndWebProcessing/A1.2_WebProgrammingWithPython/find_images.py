import urllib.request

url = input("Please input the Web link:\n")
url = 'https://www.w3schools.com/tags/att_a_href.asp'
response = urllib.request.urlopen(url)

html = str(response.read())

pos = 0
all_found, images_found = False, 0

while not all_found:
    tag_start = html.find("<img src=", pos)
    if tag_start > -1:
        # find url or the directory path
        src = html.find('"', tag_start + 1)
        end_src = html.find('"', src + 1)
        url = html[src + 1: end_src]
        print(url)
        isName = False
        uPos = 0
        while not isName:
            n = url.find('/', uPos)
            if url.find('/', n + 1) == -1:
                isName = True
                print(url[n + 1:])
            else:
                uPos = n + 1
        images_found = images_found + 1
        # search the end of attribute
        close_tag = html.find(">", tag_start)
        pos = close_tag + 1
    else:
        all_found = True

print("{} images found".format(images_found))