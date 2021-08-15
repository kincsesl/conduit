def beolvas():
    lista = []
    with open("veletlen_adatok.csv", "r") as file:  # Beolvassa az első sort
        for sor in file:
            sor = sor[0:len(sor)-1]
            allista = sor.split(";")
            lista.append(allista)
    return lista

print(beolvas())
