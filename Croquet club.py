

def decideGroup(age,cap):
    if age>=55 and cap>7:
        return "Senior"
    else:
        return "Open"

testcase = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = []

for person in testcase:

    output.append(decideGroup(person[0],person[1]))

print(output)

