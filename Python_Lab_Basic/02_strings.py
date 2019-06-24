#LAB 02_strings
#1-3 just print with separator
print("#1-3")
print("This is the first line of text!")
print("This is the second line of text!\nThis is third line of text!")
print("This is some \" text")
#4 variable as print
print("#4")
phrase = "string in a Variable"
print(phrase)
print("\n" + phrase + " and concatenated string")
#5 change upper and lower cases to oposite
print("#5")
print(phrase.capitalize())
#6 change all letters to upper case
print("#6")
print(phrase.upper())
#7 check if string have ALL lower/upper cases
print("#7")
print(phrase.isupper())
print(phrase.islower())
#8 print with upper then check
print("#8")
print(phrase.upper() .isupper())
#9 len counts letters and print only third case (it is counted from 0
print("#9")
print(len(phrase))
print(phrase[2])
#10 prints "place" of specyfic latter
print("#10")
print(phrase.index("V"))
print(phrase.index("i"))
#11 replace string in a variable
print("#11")
print(phrase)
print(phrase.replace("Variable", 'variable_replaced'))

