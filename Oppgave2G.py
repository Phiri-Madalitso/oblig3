import pandas as pd
import altair as alt
import os

# Sjekk om filen eksisterer
file_path = "ssb-barnehager-2015-2023-alder-1-2-aar.xlsm"
if not os.path.exists(file_path):
    print(f"Filen {file_path} ble ikke funnet. Sørg for at filen er plassert i riktig katalog.")
else:
    # Importerer data
    kgdata = pd.read_excel(file_path, sheet_name="KOSandel120000",
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

    # Beregn gjennomsnittlig prosentandel for årene 2015-2023 for hver kommune
    renset_kb['gjennomsnitt'] = renset_kb[['y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23']].mean(axis=1, skipna=True)

    # Filtrer kommuner som har data for alle årene
    renset_kb_filtered = renset_kb.dropna(subset=['y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23'])

    # Velg de 10 kommunene med høyest gjennomsnittlig prosentandel barn i barnehage
    top_10_kommuner = renset_kb_filtered.nlargest(10, 'gjennomsnitt')

    # Transformere datastrukturen for plotting
    top_10_kommuner_melted = top_10_kommuner.melt(
        id_vars='kom',
        value_vars=['y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23'],
        var_name='År',
        value_name='Prosent'
    )

    # Endre 'År'-kolonnen til riktige årstall
    top_10_kommuner_melted['År'] = top_10_kommuner_melted['År'].str[1:].astype(int)

    # Lag diagrammet
    chart = alt.Chart(top_10_kommuner_melted).mark_line(point=True).encode(
        x=alt.X('År:O', title='År'),
        y=alt.Y('Prosent:Q', title='Prosentandel barn i barnehage'),
        color='kom:N',
        tooltip=['kom', 'År', 'Prosent']
    ).properties(
        title='Gjennomsnittlig prosentandel barn i ett- og to-årsalderen i barnehage (2015-2023)',
        width=800,
        height=600
    )

    # Lagrer diagrammet som en HTML-fil
    chart.save('top_10_kommuner_diagram.html')

    print("Diagrammet er lagret som 'top_10_kommuner_diagram.html'. Åpne denne filen i en nettleser for å se diagrammet.")
