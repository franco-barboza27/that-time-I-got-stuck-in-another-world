def floatandround(values):
    newlist = []
    for item in values:
        try:
            newitem = int(round(float(item)))
            newlist.append(newitem)
        except:
            pass
    
    return newlist