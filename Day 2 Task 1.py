
# Solution I:
def openOrSenior(data):
    output = []
    for i in data:
        if i[0] > 54 and i[1] > 7:
            output.append('Senior')
        else:
            output.append('Open')
    return output

# Solution II:
def openOrSenior(data):
    return ["Senior" if m[0]>54 and m[1]>7 else "Open" for m in data]



