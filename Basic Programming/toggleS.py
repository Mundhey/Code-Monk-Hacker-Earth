
name=list(raw_input())


for i in range(0,len(name)):
    if(name[i].isupper()):
        name[i]=name[i].lower()
    else:
        name[i]=name[i].upper()


abc="".join(name)
print abc