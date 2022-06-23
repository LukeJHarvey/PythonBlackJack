def YNInput(msg):
    resp = input(msg)
    while resp.lower() not in ["y", "n", "yes", "no"]:
        print("Incorrect input, only accepting 'y'/'yes' or 'n'/'no'")
        resp = input(msg)
    ret = True if resp.lower() in ["y", "yes"] else False
    return ret

def typedInput(msg, inp_type = str, empty = 0):
    while True:
        try:
            inp = input(msg)
            if inp is "":
                return empty
            return inp_type(inp)
        except:
            if inp_type is int: print("Please input only Integers")
            elif inp_type is float: print("Please input only Floats")