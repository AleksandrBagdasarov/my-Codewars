def get_middle(s):
    if ( not len(s) % 2 ):
        return(s[len(s) // 2 -1] + s[(len(s) // 2)])
    else:
        return(s[len(s[:-1]) // 2])



get_middle("test")#"es")
get_middle("testing")#"t")
get_middle("middle")#"dd")
get_middle("A")#"A")
get_middle("of")#"of")