import json
jfile=open('D:\cowin.json','r')
jsondata=jfile.read()
obj=json.loads(jsondata)
count = 0
count_45 = 0
count_18 = 0
hospitallist = []
li = obj['centers']
print(len(li))
for i in range(len(li)):
    jsonentry=obj['centers'][i]
    print(jsonentry)
    jsonsessionlen = len(jsonentry['sessions'])
    jsonxyz=(jsonentry['sessions'])
    for x in range(jsonsessionlen):
        sessioneach= (jsonxyz[x])
        min_age = sessioneach['min_age_limit']
        if(min_age >= 45):
            count_45 = count_45 + 1

        if(min_age >= 18):
            count_18 = count_18 + 1
            hospital_name=jsonentry['name']
            if hospital_name not in hospitallist:
                hospitallist.append(hospital_name)

print("Total no of hospitals providing vaccine to 45+ are ")
print(count_45)
print("Total no of hospitals providing vaccine to 18+ are ")
print(count_18)
print("Name of the hospitals providing vaccine to 18+ are")
print(hospitallist)