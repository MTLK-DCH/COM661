from get_page_text_enhance import get_page_text
def add_word_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            print(1)
            entry[1].append(url)
            return
    index.append([keyword, [url]])

def add_page_to_index(index, url):
    page_words = get_page_text(url)
    print(page_words)
    for word in page_words:
        print(word)
        add_word_to_index(index, word, url)

index, page_words = [], []
url = "http://www.ulster.ac.uk/campuses/belfast"
add_page_to_index(index, url)
print(index)
