def nyolcadik():
    #beolvasás
    beFajl = open("fajlok/dal.txt","r", encoding="utf-8")
    fajlTartalma=beFajl.read()
    #print(type(fajlTartalma))
    #print(fajlTartalma)
    dbk = 0
    dbK = 0
    fajlTartalmaUj = ""
    for index in range(0, len(fajlTartalma),1):
        if fajlTartalma[index] == "k":
            dbk += 1
            fajlTartalmaUj += "*"
        elif fajlTartalma[index] == "k":
            dbK += 1
            fajlTartalmaUj += "*"
        else:
            fajlTartalmaUj += fajlTartalma[index]
        print(f"Cenzúrázott fájl tartalma:{fajlTartalmaUj}")

