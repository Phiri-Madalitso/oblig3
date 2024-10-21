import pandas as pd 

print(pd.__version__)


# GJør det for å lage to forkskjellige lister

tabell = {

    'name': ['Obim', 'Murad', 'Brian', 'Sebastian'],

    'gruppe': ['Gr1', 'Gr2', 'Gr3', 'Gr4']

    }

# Her legges listene sammen inn i en tabell

StudentTabell = pd.DataFrame(tabell)

# Funksjon som blir brukt for finne en student

# Input :: er selve navnet studenten og hva slags liste vi ønsker å bruke

# Output :: Returverdi kommer i form av studentens navn og gruppen student er i

def FinnGr(Stud_name, Liste):

    """Funksjonen leter etter gruppen til eleven"""

    return Liste[Liste["name"] == Stud_name]

print(FinnGr('Murad', StudentTabell)) 


