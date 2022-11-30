import urllib.request

# url = "http://www.ulster.ac.uk/campuses/belfast"

def get_page_text(url):
    response = urllib.request.urlopen(url)
    html = str(response.read())

    page_text, page_words = "", []
    html = html[html.find("<body") + 5 : html.find("</body>")]

    ignorefile = open("./ignorelist.txt", "r")
    ignorelist = []
    for line in ignorefile:
        ignorelist.append(line.strip())
    print('ignore lists are:', ignorelist)

    finished = False

    while not finished:
        next_script_start = html.find("<script>")
        next_script_end = html.find("</script>") + 9
        if next_script_start > -1:
            html = html[:next_script_start] + html[next_script_end:]
        else:
            finished = True
    
    finished = False

    while not finished:
        next_close_tag = html.find(">")
        next_open_tag = html.find("<", next_close_tag + 1)
        if next_open_tag > -1:
            content = " ".join(
                html[next_close_tag + 1 : next_open_tag].split())
            page_text = page_text + " " + content
            html = html[next_open_tag + 1 :]
        else:
            finished = True

    for word in page_text.split():

        if word.isalnum() and word not in page_words and word not in ignorelist:
            page_words.append(word)

    return page_words

# page_words = get_page_text(url)
    
# print(page_words)
# print("{} unique words found".format(len(page_words)))