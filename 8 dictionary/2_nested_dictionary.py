# sub-dictionary/ies within a dictionary


d={
    'd1':{
        'name': 'nameless',
        'age': '00'
    },
    'd2':{
        'language':"Espanol"
    },
    'd3':{
        'gender':'female',
        'experties':'killing',
        'd4':{
            'dummyKey': 'dummyValue'
        }
    }
}

# print(d)
# print(d['d3'])
# print(d['d3']['d4'])

for key,value in d.items():
    print(key, value)