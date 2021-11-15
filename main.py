


def izglitibas_programmas():
    #saruna par izglītības programmu
    print("programmas coming soon")
    return 0


def direktori():
    #sarunas par V2V direktoriem
    print("direktors coming soon")
    pass

def tradicijas():
    #saruna par skolas tradīcijām
    print("tradicijas coming soon")
    pass

def skolas_eka():
    #saruna par skolas ēku
    print("skolas ekas coming soon")
    pass



#Čatbots par skolas vēsturi
def izvelne(vards):
    print(vards + ",Izvelies ko tu gribi uzzināt")
    x = input("1 - izglitibas programmas\n2 - direktori\n3 - tradicijas\n4- skolas eka")
    lietotaja_izvele = int(x)
    if (lietotaja_izvele) == 1:
        izglitibas_programmas()
        if  (lietotaja_izvele) == 2:
            direktori()
    if (lietotaja_izvele) == 3:
        tradicijas()
    if (lietotaja_izvele) == 4:
        skolas_eka()

def sasveicinaties(vards):
    print("Sveiks, " + vards)
    izvelne(vards)
    return 0

if __name__ == "__main__" :
    print("sveiki es esmu V2V čatbots, Pēteris. Es tev pastāstīšu vairāk par šo skolu")
    vards = input("Sveiki, kā jūs sauc??")
    sasveicinaties(vards)