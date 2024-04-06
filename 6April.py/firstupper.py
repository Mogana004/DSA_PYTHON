def get_first_upper_letter(string):
    list = []
   
    for i in string :
        if i.isupper():
            list.append(i)
    return list[0]


string = input()
upper_case_character =get_first_upper_letter(string)
print(upper_case_character)
