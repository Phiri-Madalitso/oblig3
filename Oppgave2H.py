import pandas as pd
import matplotlib.pyplot as plt
# Bruker av matplotlib, jeg og samarbeidspartner fikk ikke altair til å funke på noen av våre systmet

# Her laste selve data inn, slik som de andre oppgavene
kgdata = pd.read_excel("ssb-barnehager-2015-2023-alder-1-2-aar.xlsm", sheet_name="KOSandel120000",
                       header=3,
                       names=['kom','y15','y16','y17','y18','y19','y20','y21','y22','y23'],
                       na_values=['.', '..'])


# Dette er selve vaskingen av data
for coln in ['y15','y16','y17','y18','y19','y20','y21','y22','y23']:
    mask_over_100 = (kgdata[coln] > 100) # Kan bli et typeproblem?
    kgdata.loc[mask_over_100, coln] = float("nan")
    
    
kgdata.loc[724:779, 'kom'] = "NaN"
    
    
    
# Her filtrer vi bare navnet på komumunen fra "kom" og deretter ligger "kom" lik denne verdier. D
kgdata["kom"] = kgdata['kom'].str.split(" ").apply(lambda x: x[1] if len(x) > 1 else "")



# Dette må gjøres for å unngå ikke relevante felt i vid tabell
kgdata_no_meta = kgdata.drop(kgdata.index[724:])

# Dette er repsenterte dataen som er vasket

renset_kb = kgdata_no_meta
print(renset_kb)



"""Oppgave G, Lag et diagram, som viser prosent av barn i ett- og to-årsalderen i barnehagen
for alle årene 2015 - 2023 for en valgt kommune."""


#Oppagave 2G
#Kontrakt
#Innput: Kommune navn :: String
#Output:: Diagram av selve kommunen :: Diagram

def plot_kommune(kommune):
    """Diagram av den valgte kommunen blir laget"""
    kommune_Data = renset_kb[renset_kb['kom'] == 'Moss']
    if kommune_Data-empty:
        print(f"kommuen '{kommune}' finnes ikke i datasettet.")
        return
    
    
    # Her gir eg dataene navn
   """
   år = ['y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23']
    prosent = kommune_Data[år].values.flatten()
    """
    
   år = kommune_Data.groupby("kom").first()

     
    
    # Her så blir diagrammet laget og formet
    
    # Lager diagrammet
   """
   plt.figure(figsize=(10, 6))
    plt.plot(år, prosent, marker='o', linestyle='-', color='b')
    plt.title(f'Prosent av barn i ett- og to-årsalderen i barnehagen for {kommune}')
    plt.xlabel('År')
    plt.ylabel('Prosent')
    plt.grid(True)
    plt.xticks(ticks=range(len(år)), labels=[f'20{årstall[1:]}' for årstall in år])
    plt.show()
    """


# Bruke funksjonen for å kalle frem en spesfikk kommune

    plot_kommune("Moss")  #  Velg hvilket kommune du ønsket inni parantesen
  