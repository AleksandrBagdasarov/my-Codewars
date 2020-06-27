def is_isogram(string):
    f = ''
    string = string.lower()
    for x in string:
        if string.count(x) != 1:
            f += x
    return(len(f)==0)



is_isogram("Dermatoglyphics")# True )
is_isogram("Isogram")# True )
is_isogram("aba")# False# "same chars may not be adjacent" )
is_isogram("moOse")# False# "same chars may not be same case" )
is_isogram("isIsogram")# False )
is_isogram("")# True# "an empty string is a valid isogram" )