def factors_of_n(number):
    for i in range( 1, number+1):
        if number % i== 0 :
            print(i , end= " ")
    

number = int(input())
factors_of_n(number)
