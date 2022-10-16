import urllib.request
response = urllib.request.urlopen("https://www.ulster.ac.uk/campuses/belfast")
html = str(response.read())

pos = 0
all_found, links_found = False, 0
while not all_found:
	tag_start = html.find("<a href=", pos)
	if tag_start > -1:
		href = html.find('"', tag_start + 1)
		end_href = html.find('"', href + 1)
		url = html[href + 1:end_href]
		print(url)
		links_found = links_found + 1
		close_tag = html.find("</a>", tag_start)
		pos = close_tag + 1
	else:
		all_found = True   

print("{} hyperlinks found".format(links_found))

