lower=900
upper=1000
print("The prime numbers in range are:")
for number in range(lower,upper+1):
    if number > 1:
        for i in range(2,number):
            #% mean take remainder
            if(number%i)==0:
                break
    else:
        print(number)



