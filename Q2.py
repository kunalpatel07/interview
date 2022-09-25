'''2. Provide a program to read the CSV file.
• CSV file has three columns, the first column names, the second column is birthdate(YYYYMM-DD) the third column is salary.
• Read the file and display the data and age in the terminal.
• The file path, delimiter, and quote char are the input by the user.
• The program has to work from the terminal. The input and output have been taken/displayed
on the terminal.'''

def csv(path,delimiter):
    from csv import reader
    from datetime import date
    temp = ""
    with open(path, mode ='r') as file:  
        csvReader = reader(file)
        header = next(csvReader)
        print(delimiter,end="")
        for i in header:
            print(" ",i,"       ",delimiter,end="")
        print("AGE     ",delimiter)
        for i in csvReader:
            for j in range(10):
                try:
                    temp += i[0][j]
                except:
                    temp+=" "
            d = date.today()
            age = ((int(d.year) - int(i[1][0:4])))
            print(delimiter,temp,"  ",delimiter,i[1],"       ",delimiter,i[2],"         ",delimiter,age,"    ",delimiter)  
            temp="" 
p = input("enter path of file :")
d = input("enter delimiter :")
csv(p,d)
