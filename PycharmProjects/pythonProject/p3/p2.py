DBase = \
    [
        {
            "Год": 2006,
            "Фамилия": "Эльмиров",
            "Почта": "elm@emali.by"
        },

        {
            "Год": 2005,
            "Фамилия": "Анитоска",
            "Почта": "аyan@emali.ber"
        },

        {
            "Год": 2007,
            "Фамилия": "Ramazrov",
            "Почта": "234rer@emali.jp"
        }
    ]
for k in DBase:
    if k["Год"] > 2005:
        print(k["Фамилия"])

