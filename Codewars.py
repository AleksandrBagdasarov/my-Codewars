def increment_string(strng):
    x = ''
    #index = -1
    if len(strng) == 0 or strng[-1].isalpha():
        print(strng+'1')
        return(strng+'1')
    else:
        print(qqq(strng, x))
        #while strng[index].isdigit():
        #    q = strng[-1]
        #    q = int(q)
        #    q += 1
        #    if len(str(q)) > 1:
        #        x += '0'
        #        index += -1
        #    else:
        #        s = strng[0:-1]
        #        s = s+str(q)
        #        s += str(x)
        #        print(s)
        #        return s
        #if strng[-1].isalpha():
        #    s +='1'
        #    s += str(x)
        #    print(s)
        #    return s

def qqq(s,x):
    if len(s) == 0 or s[-1].isalpha():
        s +='1'
        s += str(x)
        #print(type(s),s)
        return f'{s}'
    else:
        q = s[-1]
        q = int(q)
        q += 1
        if len(str(q)) > 1:
            x += '0'
            return qqq(s[0:-1], x)
        else:
            s = s[0:-1]
            s = s+str(q)
            s += str(x)
            #print(type(s),s)
            return f'{s}'

increment_string("foo")# "foo1")
increment_string("foobar001")# "foobar002" foobar002
increment_string("foobar1")# "foobar2")
increment_string("foobar00")# "foobar01")
increment_string("foobar99")
increment_string("foobar999")# "foobar100")
increment_string("foobar099")# "foobar100")
increment_string("")# "1")
increment_string("999")