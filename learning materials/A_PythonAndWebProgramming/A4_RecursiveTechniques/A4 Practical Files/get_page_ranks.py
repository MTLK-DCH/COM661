def compute_ranks(graph):
	d = 0.85
	num_loops = 10
	ranks = {}
	npages = len(graph)
	
	for page in graph:
		ranks[page] = 1 / npages
	
	for i in range(0, num_loops):
		new_ranks = {}
		for page in graph:
			new_rank = (1 - d) / npages
			for node in graph:
				if page in graph[node]:
					new_rank = new_rank + d * (ranks[node] / len(graph[node]))
			new_ranks[page] = new_rank
		ranks = new_ranks
	return ranks					

graph = { 'page1.html' : ['page2.html', 'page3.html'],
          'page2.html' : ['page3.html'],
          'page3.html' : [] 
        } 
ranks = compute_ranks(graph)
print(ranks)
