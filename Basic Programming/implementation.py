S=str(raw_input())

zero=0
one=0
two=0
three=0
four=0
five=0
six=0
seven=0
eight=0
nine=0

for i in range(0,len(S)):
    if(S[i]=='0'):
        zero=zero+1
    elif (S[i] == '1'):
        one = one + 1
    elif (S[i] == '2'):
        two = two + 1
    elif (S[i] == '3'):
        three = three + 1
    elif (S[i] == '4'):
        four = four + 1
    elif (S[i] == '5'):
        five = five + 1
    elif (S[i] == '6'):
        six = six + 1
    elif (S[i] == '7'):
        seven = seven + 1
    elif (S[i] == '8'):
        eight = eight + 1
    elif (S[i] == '9'):
        nine = nine + 1


print "0",zero
print "1",one
print "2",two
print "3",three
print "4",four
print "5",five
print "6",six
print "7",seven
print "8",eight
print "9",nine