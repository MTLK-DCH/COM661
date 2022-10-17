LOOP_COUNT = 10

def popularity(friends, person, timestamp):
	if timestamp == 0:
		return 1
	else:
		pop = 0 
		for f in friends[person]:
			pop = pop + popularity(friends, f, timestamp - 1)
		return pop		

def get_popularity_values(friends):
	popularities = {}
	for friend in friends:
		pop_value = popularity(friends, friend, LOOP_COUNT)
		popularities[friend] = pop_value
	return popularities	

friends={ 'Alice'  : ['Chloe','Frank','Gemma'],
          'Bob'    : ['Chloe','Gemma'],
          'Chloe'  : ['Derek'],
          'Derek'  : ['Chloe','Eileen'],
          'Eileen' : ['Derek','Frank'],
          'Frank'  : ['Chloe','Derek','Gemma'],
		  'Gemma'  : ['Alice','Derek']
		}
         
pop_values = get_popularity_values(friends)
print(pop_values)