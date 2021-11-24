def direktors():
    print("Andrejs Gluhovs, ir direktors no 2009. gada" )
    pass



def izglitibas_programmas():
    #saruna par izglītības programmu
    print("Šajā skolā ir daudz programmu, piemēram šogad bija Medicīna Programmēšana, un Sports un veselība")
    return 0

def pir_direktors():
    print("E. Kalniņš ir pirmais direktors, un kurš dibināja v2v")
    pass


def direktori():
    print(vards + " ,Jūs gribat uzzināt par bijušajiem direktoru vai tagadējo??")
    y = input ("1 - Pirmais direktors\n2- Tagadējo direktoru")
    lietotaju_izvele = int(y)
    if lietotaju_izvele == 1:
        pir_direktors()
    if lietotaju_izvele == 2:
        direktors()

    return 0



def tradicijas():
    print("Zinību diena\nSkolotāju diena\Skolas jubileja\nJaunā gada balle")

def skolas_eka():
    #saruna par skolas ēku
    print("Skola atrodas Raiņa iela 11")
    pass1



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
    if lietotaja_izvele == 4:
        skolas_eka()



def sasveicinaties(vards):
    print("Sveiks, " + vards)
    izvelne(vards)
    return 0

if __name__=="__main__" :
    print("Sveiki es esmu V2V čatbots, Pēteris. Es tev pastāstīšu vairāk par šo skolu")
    vards = input("Sveiki, kā jūs sauc??")
    sasveicinaties(vards)
    sasveicinaties(vards)
    exit(0)
