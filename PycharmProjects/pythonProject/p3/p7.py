def reverseLookup(dictionaty: dict, v: str):
    for k in dictionaty.keys():
        if dictionaty[k] == v:
            print(k)

dictrs = [{"age": "13",
           "day": '13',
           "mounth": "132"},

        {"Странная": "места",
         "day": '13',
         "mounth": "132"},

          {"agdfe":"13",
           "ddfay": '13',
           "Почему?": "места"}]

for i in dictrs:
    reverseLookup(i, "13")
    reverseLookup(i, "132")
    reverseLookup(i, "места")
