
candidates_age= []

while len(candidates_age) < 90 :
    user_input = int(input('give me an age: '))
    if user_input == -1:
        print(candidates_age[-2:])
        break
    candidates_age.append(user_input)
    candidates_age.sort()
    print(candidates_age)
    
    
        


