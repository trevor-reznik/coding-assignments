string = "NYNJPANYMANYNYMANYNYCTNJNJNYNHMANYNJPARINYNYNJNYNYNYRINYCTPAPANYNYNJASPAPANYMANYNJMEPAPANJCTNYPAPANYMAPAPAMAPARIPANJVTMAMAPANYNYPANYPAMANYNJNYNJNYMACTRINJNYCTPAMAMANJNYNYNJPANJCTNYPANYNYNYMENYPAMENJPAMAMANYMAPANJNYPANYPANJMANJNJNJCTNYPANYNYPAPAPAPANYNYNYPAMEPAMAMANJNYPAVTPANJNYMERINYNJPAPAPANYNYNYCTCTNJPANYMANYMAPANYNYNHPAPAPANYNJPANYPAPAPANYPAPAMACTMANYNJMAPANJNYPANY"

list1 = []
i = 0
while i < len(string):
    list1.append(string[i:i+2])
    i +=2

list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)

print(list2)