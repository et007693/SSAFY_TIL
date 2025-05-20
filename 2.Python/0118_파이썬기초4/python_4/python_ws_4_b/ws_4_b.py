food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]


# sol1
# for food in food_list:
#     name = food['이름']
#     kind = food['종류']

#     if name == '토마토':
#         kind = '과일'
#     elif name == '자장면':
#         print(f'{name}엔 고춧가루지')
        
#     print(f'{name} 은/는 {kind} (이)다.')

# print(food_list)

# sol2
cnt = 0
while cnt < len(food_list):
    food = food_list[cnt]
    name = food['이름']
    kind = food['종류']

    if name == '토마토':
        kind = '과일'
    elif name == '자장면':
        print(f'{name}엔 고춧가루지')
    
    print(f'{name} 은/는 {kind} (이)다.')
    cnt += 1

print(food_list)
