import io
import numpy as np


def task_3():
    h = open('run_of_60_mark.txt', 'w')
    f = open('run_of_60_m.txt', encoding='utf-8')
    a = []
    for line in f:
        a.append(line.split(","))

    win = []

    for i in range(len(a)):
        # условия для девочек 6 класс
        if a[i][1] == " ж" and a[i][2] == " 6" and int(a[i][3]) < 10.3:
            h.write(a[i][0] + " 5" + '\n')
            #print(a[i][0], " 5")
        if a[i][1] == " ж" and a[i][2] == " 6" and 11.2 > int(a[i][3]) > 10.6:
            h.write(a[i][0] + " 4" + '\n')
            #print(a[i][0], " 4")
        if a[i][1] == " ж" and a[i][2] == " 6" and int(a[i][3]) > 11.2:
            h.write(a[i][0] + " 3" + '\n')
            #print(a[i][0], " 3")

        # условия для мальчиков 6 класс
        if a[i][1] == " м" and a[i][2] == " 6" and int(a[i][3]) < 9.9:
            h.write(a[i][0] + " 5" + '\n')
            #print(a[i][0], " 5")
        if a[i][1] == " м" and a[i][2] == " 6" and 10.4 > int(a[i][3]) > 9.9:
            h.write(a[i][0] + " 4" + '\n')
            #print(a[i][0], " 4")
        if a[i][1] == " м" and a[i][2] == " 6" and 11.4 > int(a[i][3]) > 10.6:
            h.write(a[i][0] + " 3" + '\n')
            #print(a[i][0], " 3")


        # условия для девочек 7 класс
        if a[i][1] == " ж" and a[i][2] == " 7" and int(a[i][3]) < 9.8:
            h.write(a[i][0] + " 5" + '\n')
            #print(a[i][0], " 5")
        if a[i][1] == " ж" and a[i][2] == " 7" and 10.6 > int(a[i][3]) > 9.8:
            h.write(a[i][0] + " 4" + '\n')
            #print(a[i][0], " 4")
        if a[i][1] == " ж" and a[i][2] == " 7" and int(a[i][3]) > 10.6:
            h.write(a[i][0] + " 3" + '\n')
            #print(a[i][0], " 3")

        # условия для мальчиков 7 класс
        if a[i][1] == " м" and a[i][2] == " 7" and int(a[i][3]) < 9.4:
            h.write(a[i][0] + " 5" + '\n')
            #print(a[i][0], " 5")
        if a[i][1] == " м" and a[i][2] == " 7" and  10.2 > int(a[i][3]) > 9.4:
            h.write(a[i][0] + " 4" + '\n')
            #print(a[i][0], " 4")
        if a[i][1] == " м" and a[i][2] == " 7" and 10.4 < int(a[i][3]):
            h.write(a[i][0] + " 3" + '\n')
            #print(a[i][0], " 3")

        if a[i-1][3] < a[i][3]:
            win.append(a[i][0] + a[i][2] + " класс " + a[i][3] + " секунд")

    print(win[-2:])







task_3()
