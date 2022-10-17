import urllib.request
response = urllib.request.urlopen("http://www.ulster.ac.uk/campuses/belfast")
html = str(response.read())

page_text, page_words = "", []
html = html[html.find("<body") + 5:html.find("</body>")]

finished = False
while not finished:
	next_close_tag = html.find(">")
	next_open_tag = html.find("<", next_close_tag + 1)
	if next_open_tag > -1:
		content = " ".join(html[next_close_tag + 1:next_open_tag].strip().split())
		page_text = page_text + " " + content
		html = html[next_open_tag + 1:]
	else:
		finished = True
		
for word in page_text.split():
	if word.isalnum() and word not in page_words:
		page_words.append(word)


print(page_words)
print("{} unique words found".format(len(page_words)))