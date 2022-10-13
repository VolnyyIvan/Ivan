def task_2():
    word = input()

    dick = {
    1 : ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
    2 : ['D', 'G'],
    3 : ['B', 'C', 'E', 'M', 'P'],
    4 : ['F', 'H', 'V', 'W', 'Y'],
    5 : ['K'],
    8 : ['J', 'X'],
    10 : ['Q', 'Z'],
    }


    word_list = []

    for c in word:
        word_list.append(c)


    count = 0
    for k, v in dick.items():
        for i in v:
            for j in word_list:
                if j == i and k == 1:
                    count += 1

                if j == i and k == 2:
                    count += 2

                if j == i and k == 3:
                    count += 3

                if j == i and k == 4:
                    count += 4

                if j == i and k == 5:
                    count += 5

                if j == i and k == 8:
                    count += 8

                if j == i and k == 10:
                    count += 10
    print(count)





task_2()
