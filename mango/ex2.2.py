s = 'void'
val = {'b':'d','d':'b','i':'i','o':'o','p':'q','q':'p','v':'v','w':'w','x':'x'}
def valid(s):
    for letter in s:
        if letter not in val:
            return False
        return True
def mirror(s):
    ls = ''
    if valid(s):
        for a in s:
            ls += val[a]
        return ls[::-1]
    return 'NOT POSSIBLE'
print(mirror(s))


     


        


    






    




    




