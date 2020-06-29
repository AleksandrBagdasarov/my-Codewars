def is_valid_walk(walk):
    if ''.join(walk).count('e') == ''.join(walk).count('w') and ''.join(walk).count('n') == ''.join(walk).count('s') and len(''.join(walk)) == 10:
        return True
    else:
        return False



is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])# 'should return True');
is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])# 'should return False');
is_valid_walk(['w'])# 'should return False');
is_valid_walk(['n','n','n','s','n','s','n','s','n','s'])# 'should return False');