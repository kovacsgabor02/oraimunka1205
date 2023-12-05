def tk():
    adatokListaja = []
    beFile = open("fajlok/allas.txt", "r", encoding="utf-8")
    for sor in beFile:
        daraboltSor = sor.strip().split("  ")
        # print(daraboltSor)
        # egy listába fűzöm össze az adatokat
        adatokListaja.extend(daraboltSor)

    beFile.close()

    # feladat lényegi megoldása
    db = 0
    # bejárom a listát
    index = 0
    while index < len(adatokListaja):
        if adatokListaja[index] == "0":
            db += 1
        index += 1
    # adatkiírás
    print(f"A ledöntött bábuk száma: {db}")
