def scanner(name, func):
    #[func(line) for line in open(name) if str(line).strip() != ""]
    map(func, [line for line in open(name) if str(line).strip() != ""])
    '''
    for line in open(name):
        if str(line).rstrip() != "":
            func(line)
    '''