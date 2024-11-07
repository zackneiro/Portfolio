list = [1, 2, 3, 4, 5]
rotation = 2
while rotation != 0:
    for i in range(len(list) - 1):
        if i == 0:
            number_to_move = list[i]
        list[i] = list[i + 1]
    list[i+1] = number_to_move
    rotation -= 1
print(list) 