import time

def time_execution(code):
    start = time.perf_counter()
    eval(code)
    run_time = time.perf_counter() - start
    return run_time

def add_word_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])

def make_string(list_of_letters):
    str = ""
    for e in list_of_letters:
        str = str + e
    return str

def make_big_index(index, size):
    letters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
    while len(index) < size:
        word = make_string(letters)
        add_word_to_index(index, word, "dummyURL")
        for i in range(len(letters) - 1, 0, -1):
            if letters[i] < 'z':
                letters[i] = chr(ord(letters[i]) + 1)
                break
            else:
                letters[i] = 'a'
    return index

def lookup(keyword, index):
    for e in index:
        if e[0] == keyword:
            return e[1]

index = []

make_big_index(index, 1000)
print("Lookup for index 1000")
print(time_execution("lookup('xxx', index)"))

make_big_index(index, 10000)
print("Lookup for index 10000")
print(time_execution("lookup('xxx', index)"))
make_big_index(index, 100000)
print("Lookup for index 100000")
print(time_execution("lookup('xxx', index)"))
make_big_index(index, 1000000)
print("Lookup for index 1000000")
print(time_execution("lookup('xxx', index)"))