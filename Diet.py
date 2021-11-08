import pyinputplus as pyip

dict_meat = {
    "Agnello": 35,
    "Anatra": 35,
    "Bresaola": 20,
    "Carne bovina in gelatina": 55,
    "Carne bovina pressata": 45,
    "Capretto": 35,
    "Cavallo": 35,
    "Cervo": 35,
    "Coniglio": 35,
    "Gallina": 35,
    "Maiale (lonza o braciola)": 35,
    "Manzo (tagli magri)": 35,
    "Pollo (coscia)": 35,
    "Pollo (petto)": 30,
    "Prosciutto crudo (sgrassato)": 25,
    "Prosciutto cotto (sgrassato)": 30,
    "Quaglia": 30,
    "Speck (sgrassato)": 25,
    "Tacchino (coscia)": 20,
    "Tacchino (petto)": 30,
    "Trippa": 45,
    "Vitello": 35,
}

dict_fish = {
    "Alici": 30,
    "Aragosta": 45,
    "Baccalà ammollato": 30,
    "Baccalà secco": 25,
    "Boga": 40,
    "Branzino (di allevamento)": 35,
    "Branzino (di mare)": 40,
    "Calamari": 55,
    "Capesante": 70,
    "Carpa": 40,
    "Caviale": 25,
    "Cefalo muggine": 45,
    "Cernia": 40,
    "Coregone": 35,
    "Corvina": 35,
    "Cozze": 60,
    "Dentice": 40,
    "Gamberetti": 45,
    "Gamberi (freschi)": 50,
    "Gamberi (surgelati)": 40,
    "Granchio": 40,
    "Halibut": 35,
    "Merluzzo": 40,
    "Mormora": 40,
    "Nasello": 40,
    "Occhiata": 35,
    "Orata": 35,
    "Palombo": 45,
    "Pesce gatto": 45,
    "Pesce persico": 45,
    "Pesce spada": 45,
    "Polpo": 65,
    "Rana pescatrice": 55,
    "Razza": 50,
    "Rombo": 45,
    "Salmone (fresco)": 40,
    "Salmone (affumicato)": 30,
    "Salmone (in salamoia)": 35,
    "Salpa": 40,
    "Sarda": 35,
    "Sardine": 35,
    "Scorfano": 35,
    "Seppia": 50,
    "Sgombro (fresco)": 40,
    "Sgombro (in salamoia)": 35,
    "Sogliola": 40,
    "Spigola (di allevamento)": 35,
    "Spigola (di mare)": 40,
    "Stoccafisso (ammollato)": 35,
    "Stoccafisso (secco)": 10,
    "Storione": 35,
    "Sugarello": 40,
    "Tinca": 40,
    "Tonno (sott'olio, sgocciolato)": 30,
    "Tonno (trancio)": 35,
    "Triglia": 45,
    "Trota (di allevamento)": 35,
    "Trota (di mare)": 50,
    "Trota (surgelata)": 40,
    "Vongole": 70,
}

dict_eggs = {
    "Albume": 2,
    "Uova di quaglia": 4,
    "Uova intere": 1,
}

dict_dairy = {
    "Cacioricotta di capra": 60,
    "Caciottina fresca": 40,
    "Caprino light": 50,
    "Crescenza": 45,
    "Feta": 45,
    "Fiocchi di latte magro": 70,
    "Fior di latte": 35,
    "Formaggio cremoso": 75,
    "Formaggio fresco di capra": 35,
    "Formaggio light": 45,
    "Formaggino light": 50,
    "Grana": 20,
    "Mozzarella (bufala)": 40,
    "Mozzarella light": 35,
    "Mozzarella (mucca)": 35,
    "Parmigiano": 20,
    "Ricotta (bufala)": 65,
    "Ricotta (mucca)": 80,
    "Ricotta (pecora)": 75,
    "Sottiletta light": 30,
    "Spalmabile light": 75,
}

dict_veg = {
    "Asparagi": 300,
    "Asparagi (bosco)": 250,
    "Asparagi (campo)": 270,
    "Asparagi (serra)": 300,
    "Biete": 320,
    "Barbabietola": 225,
    "Broccoletti di rapa (cime)": 450,
    "Broccoli": 190,
    "Carciofi": 360,
    "Cardi": 530,
    "Carote": 120,
    "Cavolfiori": 330,
    "Cavolini di Bruxelles": 215,
    "Cavolo cappuccio": 360,
    "Cavolo cappuccio (rosso)": 335,
    "Cetrioli": 500,
    "Cicoria": 530,
    "Cicoria (campo)": 1285,
    "Cipolle": 160,
    "Cipolline": 105,
    "Coste": 250,
    "Crauti": 140,
    "Cuore di palma": 160,
    "Finocchi": 900,
    "Funghi": 900,
    "Invidia belga": 280,
    "Lattuga": 400,
    "Lattuga cappuccio": 300,
    "Mais": 30,
    "Melanzane": 350,
    "Minestra di verdure": 240,
    "Passato di verdure": 240,
    "Patate": 50,
    "Pomodori (conserva)": 45,
    "Pomodori (insalata)": 320,
    "Pomodori (maturi)": 260,
    "Pomodori (passata)": 300,
    "Porri": 170,
    "Radicchio rosso": 560,
    "Rape": 240,
    "Ravanelli": 500,
    "Rucola": 230,
    "Sedano": 380,
    "Sedano rapa": 235,
    "Spinaci": 300,
    "Tarassaco": 245,
    "Topinambur": 45,
    "Verza cappuccio": 400,
    "Zucca": 250,
    "Zucchine": 640,
}

dict_fat = {
    "Anacardi": 3,
    "Arachidi": 3,
    "Avocado": 6,
    "Mandorle": 3,
    "Nocciole": 2.5,
    "Noci": 2.5,
    "Noci di macadamia": 2.5,
    "Pecan": 2,
    "Pinoli": 3,
    "Pistacchi": 2.5,
}

dict_oil = {
    "Burro": 1.5,
    "Olio d'oliva": 1.5,
    "Olio di semi": 1.5,
    "Olive (sott'olio)": 5,
    "Olive (nere)": 5,
    "Olive (verdi)": 10,
}

dict_fruit = {
    "Albicocche": 130,
    "Amarene": 90,
    "Ananas": 90,
    "Anguria": 250,
    "Arancia": 115,
    "Banana": 60,
    "Castagne": 25,
    "Castagne (arrosto)": 20,
    "Castagne (secche)": 15,
    "Ciliegie": 100,
    "Clementine": 100,
    "Cocco": 100,
    "Fragole": 170,
    "Kiwi": 100,
    "Lamponi": 140,
    "Limoni": 390,
    "Macedonia": 115,
    "Mandaranci": 70,
    "Mandarini": 50,
    "Mango": 70,
    "Mela": 90,
    "Mela (cotogna)": 140,
    "Mela (gialla)": 85,
    "Mela (succo)": 60,
    "Melograno": 55,
    "Melone (estate)": 120,
    "Melone (inverno)": 185,
    "Mirtilli": 175,
    "More": 110,
    "Nespole": 150,
    "Pera": 100,
    "Pesca": 150,
    "Pompelmo": 145,
    "Prugne (gialle)": 125,
    "Prugne (rosse)": 85,
    "Ribes": 135,
    "Uva": 60,
}

list_dairy = [
    "Cacioricotta di capra",
    "Caciottina fresca",
    "Caprino light",
    "Crescenza",
    "Feta",
    "Fiocchi di latte magro",
    "Fior di latte",
    "Formaggio cremoso",
    "Formaggio fresco di capra",
    "Formaggio light",
    "Formaggino light",
    "Grana",
    "Mozzarella (bufala)",
    "Mozzarella light",
    "Mozzarella (mucca)",
    "Parmigiano",
    "Ricotta (bufala)",
    "Ricotta (mucca)",
    "Ricotta (pecora)",
    "Sottiletta light",
    "Spalmabile light",
]

list_meat = [
    "Agnello",
    "Anatra",
    "Bresaola",
    "Carne bovina in gelatina",
    "Carne bovina pressata",
    "Capretto",
    "Cavallo",
    "Cervo",
    "Coniglio",
    "Gallina",
    "Maiale (lonza o braciola)",
    "Manzo (tagli magri)",
    "Pollo (coscia)",
    "Pollo (petto)",
    "Prosciutto crudo (sgrassato)",
    "Prosciutto cotto (sgrassato)",
    "Quaglia",
    "Speck (sgrassato)",
    "Tacchino (coscia)",
    "Tacchino (petto)",
    "Trippa",
    "Vitello",
]

list_fish = [
    "Alici",
    "Aragosta",
    "Baccalà ammollato",
    "Baccalà secco",
    "Boga",
    "Branzino (di allevamento)",
    "Branzino (di mare)",
    "Calamari",
    "Capesante",
    "Carpa",
    "Caviale",
    "Cefalo muggine",
    "Cernia",
    "Coregone",
    "Corvina",
    "Cozze",
    "Dentice",
    "Gamberetti",
    "Gamberi (freschi)",
    "Gamberi (surgelati)",
    "Granchio",
    "Halibut",
    "Merluzzo",
    "Mormora",
    "Nasello",
    "Occhiata",
    "Orata",
    "Palombo",
    "Pesce gatto",
    "Pesce persico",
    "Pesce spada",
    "Polpo",
    "Rana pescatrice",
    "Razza",
    "Rombo",
    "Salmone (fresco)",
    "Salmone (affumicato)",
    "Salmone (in salamoia)",
    "Salpa",
    "Sarda",
    "Sardine",
    "Scorfano",
    "Seppia",
    "Sgombro (fresco)",
    "Sgombro (in salamoia)",
    "Sogliola",
    "Spigola (di allevamento)",
    "Spigola (di mare)",
    "Stoccafisso (ammollato)",
    "Stoccafisso (secco)",
    "Storione",
    "Sugarello",
    "Tinca",
    "Tonno (sott'olio, sgocciolato)",
    "Tonno (trancio)",
    "Triglia",
    "Trota (di allevamento)",
    "Trota (di mare)",
    "Trota (surgelata)",
    "Vongole",
]

list_eggs = ["Albume", "Uova di quaglia", "Uova intere"]

list_veg = [
    "Asparagi",
    "Asparagi (bosco)",
    "Asparagi (campo)",
    "Asparagi (serra)",
    "Biete",
    "Barbabietola",
    "Broccoletti di rapa (cime)",
    "Broccoli",
    "Carciofi",
    "Cardi",
    "Carote",
    "Cavolfiori",
    "Cavolini di Bruxelles",
    "Cavolo cappuccio",
    "Cavolo cappuccio (rosso)",
    "Cetrioli",
    "Cicoria",
    "Cicoria (campo)",
    "Cipolle",
    "Cipolline",
    "Coste",
    "Crauti",
    "Cuore di palma",
    "Finocchi",
    "Funghi",
    "Invidia belga",
    "Lattuga",
    "Lattuga cappuccio",
    "Mais",
    "Melanzane",
    "Minestra di verdure",
    "Passato di verdure",
    "Patate",
    "Pomodori (conserva)",
    "Pomodori (insalata)",
    "Pomodori (maturi)",
    "Pomodori (passata)",
    "Porri",
    "Radicchio rosso",
    "Rape",
    "Ravanelli",
    "Rucola",
    "Sedano",
    "Sedano rapa",
    "Spinaci",
    "Tarassaco",
    "Topinambur",
    "Verza cappuccio",
    "Zucca",
    "Zucchine",
]

list_fat = [
    "Anacardi",
    "Arachidi",
    "Avocado",
    "Mandorle",
    "Nocciole",
    "Noci",
    "Noci di macadamia",
    "Pecan",
    "Pinoli",
    "Pistacchi",
]

list_oil = [
    "Burro",
    "Olio d'oliva",
    "Olio di semi",
    "Olive (sott'olio)",
    "Olive (nere)",
    "Olive (verdi)",
]

list_fruit = [
    "Albicocche",
    "Amarene",
    "Ananas",
    "Anguria",
    "Arancia",
    "Banana",
    "Castagne",
    "Castagne (arrosto)",
    "Castagne (secche)",
    "Ciliegie",
    "Clementine",
    "Cocco",
    "Fragole",
    "Kiwi",
    "Lamponi",
    "Limoni",
    "Macedonia",
    "Mandaranci",
    "Mandarini",
    "Mango",
    "Mela",
    "Mela (cotogna)",
    "Mela (gialla)",
    "Mela (succo)",
    "Melograno",
    "Melone (estate)",
    "Melone (inverno)",
    "Mirtilli",
    "More",
    "Nespole",
    "Pera",
    "Pesca",
    "Pompelmo",
    "Prugne (gialle)",
    "Prugne (rosse)",
    "Ribes",
    "Uva",
]

def protein_choice(r, i, n):
    choice_type = pyip.inputMenu(
                ["Carne", "Pesce", "Uova", "Latticini"],
                lettered=False,
                numbered=True,
                prompt=f"Scegli il tipo di proteina numero {i}: \n",
    )
    match choice_type:
        case "Carne":
            choice = pyip.inputMenu(
                list_meat,
                lettered=False,
                numbered=True,
                prompt="Scegli la carne che preferisci: \n",
            )
            calc = r * int(dict_meat[choice]) / n
        case "Pesce":
            choice = pyip.inputMenu(
                list_fish,
                lettered=False,
                numbered=True,
                prompt="Scegli il pesce che preferisci: \n",
            )
        case "Uova":
            choice = pyip.inputMenu(
                list_eggs,
                lettered=False,
                numbered=True,
                prompt="Scegli il tipo di uovo che preferisci: \n",
            )
            calc = r * int(dict_eggs[choice]) / n
        case "Latticini":
            choice = pyip.inputMenu(
                list_dairy,
                lettered=False,
                numbered=True,
                prompt="Scegli il tipo di latticino che preferisci: \n",
            )
            calc = r * int(dict_dairy[choice]) / n
    return f"Ti spettano {calc}g di {choice}"

def fat_choice(r, i, n, type):
    match type:
        case "Nut":
            choice = pyip.inputMenu(
                list_fat,
                lettered=False,
                numbered=True,
                prompt=f"Scegli il grasso numero {i}: \n",
            )
            calc = r * int(dict_fat[choice]) / n
        case "Oil":
            choice = pyip.inputMenu(
                list_oil,
                lettered=False,
                numbered=True,
                prompt=f"Scegli il grasso numero {i}: \n",
            )
            calc = r * int(dict_oil[choice]) / n
    return f"Ti spettano {calc}g di {choice}"

def carb_choice(r, i, n, forced=None):
    if forced==None:
        choice_type = pyip.inputMenu(
                    ["Frutta", "Verdura"],
                    lettered=False,
                    numbered=True,
                    prompt=f"Scegli il tipo di carboidrato numero {i}: \n",
        )
    else:
        choice_type=forced
    match choice_type:
        case "Frutta":
            choice = pyip.inputMenu(
                list_fruit,
                lettered=False,
                numbered=True,
                prompt="Scegli la frutta che preferisci: \n",
            )
            calc = r * int(dict_fruit[choice]) / n
        case "Verdura":
            choice = pyip.inputMenu(
                list_veg,
                lettered=False,
                numbered=True,
                prompt="Scegli la verdura che preferisci: \n",
            )
            calc = r * int(dict_veg[choice]) / n
    return f"Ti spettano {calc}g di {choice}"


answer = []

input_meal = pyip.inputMenu(
    ["Colazione", "Pranzo", "Snack", "Cena"],
    lettered=False,
    numbered=True,
    prompt="Ciao Stefania, cosa vuoi mangiare oggi? \n",
)

match input_meal:
    case "Colazione":
        print("Ti spettano una proteina e un grasso. \n")
        n_prot = pyip.inputInt(min=0, prompt="Quante proteine diverse vuoi mescolare? \n")
        for i in range (1, n_prot + 1):
            answer.append(protein_choice(2, i, n_prot))           
        n_fat = pyip.inputInt(min=0, prompt="Quanti grassi diversi vuoi mescolare? \n")
        for i in range (1, n_fat + 1):
            answer.append(fat_choice(4, i, n_fat, "Nut"))
    case "Pranzo":
        print("Ti spettano un carboidrato, una proteina e un grasso. \n")
        n_carb = pyip.inputInt(min=0, prompt="Quanti carboidrati diversi vuoi mescolare? \n")
        for i in range (1, n_carb + 1):
            answer.append(carb_choice(1.5, i, n_carb))
        n_prot = pyip.inputInt(min=0, prompt="Quante proteine diverse vuoi mescolare? \n")
        for i in range (1, n_prot + 1):
            answer.append(protein_choice(5, i, n_prot))           
        n_fat = pyip.inputInt(min=0, prompt="Quanti grassi diversi vuoi mescolare? \n")
        for i in range (1, n_fat + 1):
            answer.append(fat_choice(18, i, n_fat, "Oil"))
    case "Snack":
        print("Ti spettano un carboidrato e un grasso.")
        n_carb = pyip.inputInt(min=0, prompt="Quanti carboidrati diversi vuoi mescolare? \n")
        for i in range (1, n_carb + 1):
            answer.append(carb_choice(1, i, n_carb, "Frutta"))
        n_fat = pyip.inputInt(min=0, prompt="Quanti grassi diversi vuoi mescolare? \n")
        for i in range (1, n_fat + 1):
            answer.append(fat_choice(2, i, n_fat, "Nut"))
    case "Cena":
        print("Ti spettano un carboidrato, una proteina e un grasso.")
        n_carb = pyip.inputInt(min=0, prompt="Quanti carboidrati diversi vuoi mescolare? \n")
        for i in range (1, n_carb + 1):
            answer.append(carb_choice(1.5, i, n_carb, "Verdura"))
        n_prot = pyip.inputInt(min=0, prompt="Quante proteine diverse vuoi mescolare? \n")
        for i in range (1, n_prot + 1):
            answer.append(protein_choice(5, i, n_prot))           
        n_fat = pyip.inputInt(min=0, prompt="Quanti grassi diversi vuoi mescolare? \n")
        for i in range (1, n_fat + 1):
            answer.append(fat_choice(18, i, n_fat, "Oil")) 

print("Quindi: \n")

for message in answer:
    print(message)

print("\n Buon appetito!")

end = input("Premi un tasto qualsiasi per terminare")

# Breakfast = 2 * protein + 4 * fats (dried fruit)

# Lunch = 1.5 * carbs + 5 * protein + 18 * fats (oil/butter)

# Snack = 1 * carbs (fruit) + 2 * fats (dried fruit)

# Dinner = 1.5 * carbs (vegs) + 5 * protein + 18 * fats (oil/butter)
