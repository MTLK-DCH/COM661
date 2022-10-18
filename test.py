dics = {
    '111': {
        'id': 111, 
        'name': 'name'
    },
    '222': {
        'id': 222, 
        'name': 'name'
    }
}

dict = dics['111']
dict['id'] = '333'
print('111' in dics)