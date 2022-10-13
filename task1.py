foot_dict = {
    'Россия': 'A',
    'Португалия' : 'B',
    'Франция': 'C',
    'Дания': 'C',
    'Египет': 'A',
    }

foot_dict['Турция'] = 'B'
print(foot_dict)



group=input()
for i in foot_dict:
    if foot_dict[i]==group:
        print(i)


unig=list(set(foot_dict.values()))
ug=dict.fromkeys(unig,0)
for i in foot_dict:
    ug[foot_dict[i]]+=1
print(ug)
        

    




