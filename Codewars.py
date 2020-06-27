def to_jaden_case(string):
    a = []
    for x in string.split():
        a.append(x.capitalize())
    return(' '.join(a))



quote = "How can mirrors be real if our eyes aren't real"
to_jaden_case(quote) # "How Can Mirrors Be Real If Our Eyes Aren't Real"