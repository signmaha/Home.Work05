my_list = []
for elem in range(3, 21):
    text = f' наш элемент: {elem}'
    for x in range(1, elem):
        for y in range(1, elem):
            if elem % (x + y) == 0:
                text += f'{x} + {y} '
    print(text)
