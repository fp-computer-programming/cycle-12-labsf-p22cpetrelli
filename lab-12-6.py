#author CJP 2/17/22
grades = {'End S1 Labs':0,'Start S2 Labs':0,'cycle 10 labs':0,'Mid-year Project Proposal':50,'cycle 10 practice quiz':0,'cycle 10 quiz':0}

print(grades.values())

for (k, v) in grades.items():
    print(k,v)


for (k,v) in grades.items():
    if v > 70:
        print(k,v)

for (k,v) in grades.items():
    if v < 50:
        print(k,v)
