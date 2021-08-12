import randomstring

with open("veletlen_adatok.csv", "w") as file:  # 10 véletlen regisztrációs adatot hoz létre és ment csv-be.
    for i in range(10):
        a = randomstring.name()
        b = randomstring.emil()
        c = randomstring.passw()
        s = a + ";" + b + ";" + c + "\n"
        file.write(s)
