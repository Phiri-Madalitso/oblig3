import pandas as pd


# Importerer data
kgdata = pd.read_excel("ssb-barnehager-2015-2023-alder-1-2-aar.xlsm", sheet_name="KOSandel120000",
                       header=3,
                       names=['kom','y15','y16','y17','y18','y19','y20','y21','y22','y23'],
                       na_values=['.', '..'])

# Dette er selve vaskingen av data
for coln in ['y15','y16','y17','y18','y19','y20','y21','y22','y23']:
    mask_over_100 = (kgdata[coln] > 100)
    kgdata.loc[mask_over_100, coln] = float("nan")

# Fjerner unødvendige rader
kgdata.loc[724:779, 'kom'] = "NaN"

# Filtrer ut navnet på kommunen
kgdata["kom"] = kgdata['kom'].str.split(" ").apply(lambda x: x[1] if len(x) > 1 else "")

# Fjerner ikke-relevante rader
kgdata_no_meta = kgdata.drop(kgdata.index[724:])

# Dette er de rensede dataene
renset_kb = kgdata_no_meta
print(renset_kb)

# Oppgave 2A
# For å finne hvilken kommune som har høyest andel barn til 1-2 år alderen i år 2023
høyest = renset_kb['y23'].max()

# Lager en tabell med alle kommunene som har høyest prosentandel på barnehage
kommune_høyest = renset_kb[renset_kb['y23'] == høyest]

# Printer ut kommunene med høyest andel på barnehager
print("Kommuner med høyest andel barn til 1-2 års alderen i år 2023")
print(kommune_høyest[['kom', 'y23']])

# Oppgave 2B
# Finne kommune med lavest andel barn 1-2 år alderen 2023
lavest = renset_kb['y23'].min()

# Lager en tabell med alle kommunene med lavest andel på barnehage
kommune_lavest = renset_kb[renset_kb['y23'] == lavest]

# Printer ut kommunene med lavest andel på barnehager
print("Kommuner med lavest andel barn til 1-2 års alderen i år 2023")
print(kommune_lavest[['kom', 'y23']])

# Oppgave 2C
renset_kb['gjennomsnitt_høy'] = renset_kb[['y23', 'y22', 'y21', 'y20','y19', 'y18', 'y17', 'y16', 'y15']].mean(axis=1, skipna=True)

# Finner høyeste verdi
høy_gjennomsnitt = renset_kb['gjennomsnitt_høy'].max()

# Spesifiserer med navn
kommune_høy_gjennomsnitt = renset_kb[renset_kb['gjennomsnitt_høy'] == høy_gjennomsnitt]

# Printer
print("Kommunen med den høyeste gjennomsnittet andel barn fra 2015-2023")
print(kommune_høy_gjennomsnitt[['kom', 'gjennomsnitt_høy']])

# Oppgave 2D
renset_kb['gjennomsnitt_lav'] = renset_kb[['y23', 'y22', 'y21', 'y20', 'y19', 'y18', 'y17', 'y16', 'y15']].mean(axis=1, skipna=True)

# Lavest gjennomsnitt
lav_gjennomsnitt = renset_kb['gjennomsnitt_lav'].min()

# Spesifiserer med navn
kommune_lav_gjennomsnitt = renset_kb[renset_kb['gjennomsnitt_lav'] == lav_gjennomsnitt]

# Printer ut
print("Kommunen med den laveste gjennomsnittet andel barn fra år 2015 til år 2023")
print(kommune_lav_gjennomsnitt[['kom', 'gjennomsnitt_lav']])

# Oppgave 2F
# Beregner gjennomsnittlig prosentandel for 2016
gjennomsnitt_2016 = renset_kb['y16'].mean(skipna=True)

print(f"Gjennomsnittlig prosentandel for alle kommuner i 2016: {gjennomsnitt_2016:.2f}%")




