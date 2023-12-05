def osztalybeir():
    kiFajl = open("fajlok/proba.txt", "a", encoding="utf-8")
    kiFajl.write("\ndiak")
    kiFajl.close()


def kiir():
    beFajl = open("fajlok/proba.txt", "r", encoding="utf-8")
    adatok = beFajl.read()
    print(adatok)
    beFajl.close()

    beFajl = open("fajlok/proba.txt", "r", encoding="utf-8")
    beFajl.readline()
    print(beFajl.readline())
    beFajl.close()


    beFajl = open("fajlok/proba.txt", "r", encoding="utf-8")
    