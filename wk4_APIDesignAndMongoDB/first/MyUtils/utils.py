import random
import uuid


def generate_dummy_daty(num):
    towns = [
        'Coleraine', 'Banbridge', 'Belfast',
        'Lisburn', 'Ballymena', 'Derry',
        'newry', 'Enniskillen', 'Omagh'
    ]
    business_dict = {}

    for i in range(num):
        id = str(uuid.uuid1())
        name = "buz" + str(i)
        town = towns[random.randint(0, len(towns)-1)]
        rating = random.randint(1, 5)
        business_dict[id] = {
            "name": name,
            'town': town,
            'rating': rating,
            'reviews': []
        }
    
    return business_dict