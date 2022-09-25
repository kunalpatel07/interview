'''1. Provide a program for the calculator from terminal.
• Make sure it do not ask questions but when you press enter. it displays the result.
• Amount and formula has to be in one line.
e.g 456 - 12
 564/ 10
 456*1234+09-12'''


def calculation(no):
    try:
        no = no + "="
        arr = ["1","2","3","4","5","6","7","8","9","0"]
        temp = ""
        number1 = ""
        number2 = ""
        opp = ""
        res = 0
        for i in no:
            if i in arr:
                temp += i
            else:
                if(number1==""):
                    number1 = temp
                else:
                    number2 = temp
                    if(opp == "+"):
                        res = int(number1)+int(number2)
                    elif(opp == "-"):
                        res =int(number1)-int(number2)
                    elif(opp == "/"):
                        res = int(number1)/int(number2)
                    elif(opp == "*"):
                        res = int(number1)*int(number2)
                    elif(opp == "%"):
                        res = int(number1)%int(number2)
                    elif(opp == "//"):
                        res = int(number1)//int(number2)
                    number1=res           
                opp = i   
                temp = ""
        return(res)
    except:
        print("operator not available enter valid input")
    
print(calculation(str(input("Enter Value :"))))
