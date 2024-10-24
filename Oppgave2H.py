import pandas as pd
import altair as alt

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

# Oppgave H Plotting med Altair
valgt_kommune = "Deatnu"

# Filtrer dataene for den valgte kommunen
kommune_data = renset_kb[renset_kb['kom'] == valgt_kommune]

# Sjekk om data finnes for den valgte kommunen
if kommune_data.empty:
    print(f"Ingen data funnet for kommunen {valgt_kommune}.")
else:
    # Transformere datastrukturen for plotting
    kommune_data_melted = kommune_data.melt(
        id_vars='kom', 
        value_vars=['y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23'],
        var_name='År',
        value_name='Prosent'
    )

    # Endre 'År'-kolonnen til riktige årstall
    kommune_data_melted['År'] = kommune_data_melted['År'].str[1:].astype(int)

    # Lag diagrammet
    chart = alt.Chart(kommune_data_melted).mark_line(point=True).encode(
        x=alt.X('År:O', title='År'),
        y=alt.Y('Prosent:Q', title='Prosentandel barn i barnehage'),
        tooltip=['År', 'Prosent']
    ).properties(
        title=f'Prosentandel barn i ett- og to-årsalderen i barnehage i {valgt_kommune} (2015-2023)',
        width=600,
        height=400
    )

    # Lagrer diagrammet som en HTML-fil
    chart.save('kommunebarnehage_diagram.html')

    print("Diagrammet er lagret som 'kommunebarnehage_diagram.html'. Åpne denne filen i en nettleser for å se diagrammet.")
    
    
