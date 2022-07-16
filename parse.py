import json
# load text file
with open('data.txt') as tf:
    _index =0
    _keys=[]
    datas=[]
    for line in tf:
        _index +=1
        # for keys
        if _index < 6:
            continue   
        # for values
        tmpLineList = line.split('   ')
        for i in range(0, len(tmpLineList), 3):
            st={}
            st['State'] =tmpLineList[i].strip()
            st['Postal Abbr.']=tmpLineList[i+1].strip()
            st['FIPS Code'] =int(tmpLineList[i+2].strip())
            datas.append(st)
print(sorted(datas, key=lambda i: i['FIPS Code']))
data ={'data':datas}
with open('data.json', 'w') as jf:
    json.dump(data, jf)
