import random, json


def generate_dummy_data(num):
    towns = [
        'Coleraine', 'Banbridge', 'Belfast',
        'Lisburn', 'Ballymena', 'Derry',
        'newry', 'Enniskillen', 'Omagh'
    ]
    business_list = []

    for i in range(num):
        name = "buz" + str(i)
        town = towns[random.randint(0, len(towns)-1)]
        rating = random.randint(1, 5)
        business_list.append({
            "name": name,
            'town': town,
            'rating': rating,
            'reviews': []
        })
    
    return business_list

businesses = generate_dummy_data(100)
fout = open('data.json', 'w')
fout.write(json.dumps(businesses))
fout.close

