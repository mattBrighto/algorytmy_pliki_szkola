def hundreds_to_words(n, i=0):
    #init vars
    anwser = ""
    digits = ["", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć"]
    teens = ["dziesięć", "jedenaście", "dwanaście", "trzynaście", "czternaście", "piętnaście", "szesnaście", "siedemnaście", "osiemnaście", "dziewiętnaście"]
    tens = ["", "dziesięć", "dwadzieścia", "trzydzieści", "czterdzieści", "pięćdziesiąt", "sześćdziesiąt", "siedemdziesiąt", "osiemdziesiąt", "dziewięćdziesiąt"]
    hundreds = ["", "sto", "dwieście", "trzysta", "czterysta", "pięćset", "sześćset", "siedemset", "osiemset", "dziewięćset"]

    if n >= 100: #hundreds
        anwser += hundreds[n//100] + " " 
        n -= ((n//100)*100)
    if n >= 20: #tens
        anwser += tens[n//10] + " "
        n -= (n//10)*10
    if n >= 10 and n < 20: #teens
        anwser += teens[n-10] + " "

    if n == 1 and i > 0: #the problem of 1
        pass
    elif n == 0: #the problem of 0
        pass
    elif n < 10: #digits
        anwser += digits[n] + " "
    
    return anwser

def enumerate(xs, start=0, step=1):
    for x in xs:
        yield (start, x)
        start += step

def num_to_words(n):
    modifiers = [["","",""], ["tysiąc", "tysiące", "tysięcy"], "milion", "miliard", "bilion", "biliard", "trylion", "tryliard", "kwadrylion", "kwadryliard", "kwintylion", "kwintyliard", "sekstylion", "sekstyliard", "septylion", "septyliard", "oktylion", "oktyliard", "nonilion", "noniliard", "decylion", "decyliard", "undecylion", "undecyliard", "duodecylion", "duodecyliard"]
    anwser = ""
    n = str(n)

    #sign check
    if str(n)[0] == "-":
        anwser += "minus "
        n = n[1::]

    #check if it is zero
    if n == "0":
        return "zero"

    #split into groups of integers of three digits (right aligned)
    lista = [int(n[::-1][i:i+3][::-1]) for i in range(0, len(n), 3)][::-1]
    
    #for every group do hundreds_to_words(n) and assign a modifier
    for i, n in enumerate(lista, len(lista)-1, -1):

        #i = len(lista) - i - 1 #invert i (how many element left inclusive) for the purpose of how the modifiers are picked
        anwser += hundreds_to_words(n, i)
        
        #add the modifier
        if n == 0: #if group is 0 then don't add any modifier
            continue
        if n == 1:
            if i < 2:
                anwser += modifiers[i][0] + " " #if group is 1
            else:
                anwser += modifiers[i] + " "
        elif n%10 < 5 and n%10 > 1 and (n-((n//100)*100))//10 != 1: #if the last digit of group belongs to <2;4> and the two last digits don't belong to <10;19>
            if i < 2:
                anwser += modifiers[i][1] + " " 
            else:
                anwser += modifiers[i] + "y "
        else: #else so for any other cases
            if i < 2:
                anwser += modifiers[i][2] + " "
            else:
                anwser += modifiers[i] + "ów "
    return anwser

#testing

#print(6, "=", num_to_words(6))
#print(-2, "=", num_to_words(-2))
#print(1, "=", num_to_words(1))
#print(14, "=", num_to_words(14))
#print(36, "=", num_to_words(36))
#print(-96, "=", num_to_words(-96))
#print(-264, "=", num_to_words(-264))
#print(315, "=", num_to_words(315))
#print(708, "=", num_to_words(708))
#print(1111000000000000000000000123, "=", num_to_words(1111000000000000000000000123))
print(123214043210057407034623062570324007507040040567060504360000004536, "=", num_to_words(123214043210057407034623062570324007507040040567060504360000004536))


#number = input("Podaj liczbę: ")
#print(number, "=", num_to_words(number))

'''
for i in range(1000000, 100000000, 11100):
    print(i, "=", num_to_words(i))
'''
