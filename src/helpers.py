def floatandround(values):
    newlist = []
    for item in values:
        try:
            newitem = int(round(float(item)))
            newlist.append(newitem)
        except:
            try:
                info=str(item)
                newlist.append(info)
            except:
                try:
                    newitem = bool(newitem)
                    newlist.append(newitem)
                except:
                    pass

    print(newlist)
    return newlist