import pandas as pd

#Importerer av data
kgdata = pd.read_excel("ssb-barnehager-2015-2023-alder-1-2-aar.xlsm", sheet_name="KOSandel120000",
                       header=3,
                       names=['kom','y15','y16','y17','y18','y19','y20','y21','y22','y23'],
                       na_values=['.', '..'])





# Dette er selve vaskingen av data
for coln in ['y15','y16','y17','y18','y19','y20','y21','y22','y23']:
    mask_over_100 = (kgdata[coln] > 100) # 
    kgdata.loc[mask_over_100, coln] = float("nan")
    
    # Vasking rydder, det og fjerner unødvendiger kolonenr og gjør det om tik "NaN", kan ikke skrive "0" fordi tallet 0 i seg selv er en verdi 
    
    
kgdata.loc[724:779, 'kom'] = "NaN"
    
    
    
# Her filtrer vi bare navnet på komumunen fra "kom" og deretter ligger "kom" lik denne verdier. D
kgdata["kom"] = kgdata['kom'].str.split(" ").apply(lambda x: x[1] if len(x) > 1 else "")



# Dette må gjøres for å unngå ikke relevante felt i vid tabell
kgdata_no_meta = kgdata.drop(kgdata.index[724:])

# Dette er repsenterte dataen som er vasket

renset_kb = kgdata_no_meta
print(renset_kb)



#Oppgave 2A

#


#Input : tabell
#output : tabell
#For å finne hvilken kommne som har høyest andel barn til 1-2 år alderen i år 2023
høyest = renset_kb['y23'].max()

# Her lager jeg en tabell med alle kommunene om har høyest prosen andel på barnehage
kommune_høyest = renset_kb[renset_kb['y23'] == høyest]

# Printer ut kommunene med høyest andel på barnahager
print("Kommuner med høyest andel barn til 1-2 års alderen i år 2023") #Dette skiver jeg for å kunne skille tabllene og se hva som er hva.
print(kommune_høyest[['kom', 'y23']]) # Her printes resultat og det blir vist full oversikt av kommunene



#Oppgave 2B
# Finne kommune med lavest andel barn 1-2 år alderen 2023, bruker "min" som referer til laveste
lavest = renset_kb['y23'].min()

# Lager en tabell med alle kommunene med lavest andel på barnehage
kommune_lavest = renset_kb[renset_kb['y23'] == lavest]

#Printer ut kommunene med lavest andel på barnehager
print("Kommuner med lavest andel barn til 1-2 års alderen i år 2023") # Dette blir som overskrift som skiller tabellene fra hverandre
print(kommune_lavest[['kom', 'y23']]) # her prinstes resultat av en oversikt over kommuner med lavest andel



#Oppgave 2C
renset_kb['gjennomsnitt_høy'] = renset_kb[['y23', 'y22', 'y21', 'y20','y19', 'y18', 'y17', 'y16', 'y15']].mean(axis=1, skipna=True)

#Finner høyeste vedi og jeg bruker max som skal ta maximum verdi i kolonnen 
høy_gjennomsnitt = renset_kb['gjennomsnitt_høy'].max()

# Spesfiere med navn, slik at det lettere å bruke den videre og ii
kommune_høy_gjennomsnitt = renset_kb[renset_kb['gjennomsnitt_høy'] == høy_gjennomsnitt]

#printer
print("Kommunen med den høyeste gjennomsnittet andel barn fra 2015-2023")
print(kommune_høy_gjennomsnitt[['kom', 'gjennomsnitt_høy']])
#Oppgave 2D

renset_kb['gjennomsnitt_lav'] = renset_kb[['y23', 'y22', 'y21', 'y20', 'y19', 'y18', 'y17', 'y16', 'y15']].mean(axis=1, skipna=True)

# Lavest gjennomsnitt, min bli brukt for å vise at vi leter minimum verdi
lav_gjennomsnitt = renset_kb['gjennomsnitt_lav'].min()

# spesifisere med navn
kommune_lav_gjennomsnitt = renset_kb[renset_kb['gjennomsnitt_lav'] == lav_gjennomsnitt]

#printer ut 
print("Komunen med den laveste gjennomsnittet andel barn fra år 2015 til år 2023")
print(kommune_lav_gjennomsnitt[['kom', 'gjennomsnitt_lav']])



#Oppgave 2F
# Beregner gjennomsnittlig prosentandel for 2016
gjennomsnitt_2016 = renset_kb['y16'].mean(skipna=True)

print(f"Gjennomsnittlig prosentandel for alle kommuner i 2016: {gjennomsnitt_2016:.2f}%")




