def direktors():
    print("Andrejs Gluhovs, ir direktors no 2009. gada" )
    pass


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



def tradicijas():
    print("Zinību diena\nSkolotāju diena\Skolas jubileja\nJaunā gada balle")

def skolas_eka():
    print("Skola atrodas Raiņa iela 11")
    pass


def izvelne(vards):
    print(vards + ",Izvelies ko tu gribi uzzināt")
    x = input("1 - izglitibas programmas\n2 - direktori\n3 - tradicijas\n4- skolas eka")
    lietotaja_izvele = int(x)
    if lietotaja_izvele == 2:
        direktori()
    if lietotaja_izvele == 3:
        tradicijas()
    if lietotaja_izvele == 4:
        skolas_eka()



def sasveicinaties(vards):
    print("Sveiks, " + vards)
    izvelne(vards)


if __name__=="__main__" :
    print("Sveiki es esmu V2V čatbots, Pēteris. Es tev pastāstīšu vairāk par šo skolu")
    vards = input("Sveiki, kā jūs sauc??")
    sasveicinaties(vards)
    exit(0)
