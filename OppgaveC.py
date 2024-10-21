
# Oppgave 9.1.1


# Her blir funksjonen hvor mye objekt eller mennesker på jorden veier på månden
def moon_weight(e_weight):
    return e_weight * (1/6) #Ganger 1/6 av det hadde veid på måned
print(moon_weight(60)) # svaret er den beregende vekten månden -> Jord
 
 
# Oppgave 9.1.6.1

numbers = [-1, 0, 5, -7, 9] #Her definer jeg tallene som numbers for listen

# bruker en liste som sjekker gjennom alle tallene
result = ["pos" if num > 0 else "neg" if num < 0 else "zero" for num in numbers]

print(result) #Resultat kommer av string, med tanke på hvor mye verdi tallet har

#9.1.8.2

# Laget en funksjon som skal soretere alle ord som har z i en liste og utelate annet
def all_z_words(wordlist: list) -> list:
    """Produce list of words from the input that contain 'z'."""
    return [wd for wd in wordlist if 'z' in wd]
#returner ordene som har z
# Output
Ord = ["pizza", "zebra", "house", "buzz", "apple", "crazy"]
z_words = all_z_words(Ord)
print(z_words)  # Output: ['pizza', 'zebra', 'buzz', 'crazy']

# Testblokk for teste ord med z
assert all_z_words(["pizza", "zebra", "house", "buzz", "apple", "crazy"]) == ['pizza', 'zebra', 'buzz', 'crazy']

# Filter Z bort med filter istedenfor for_loop
def z_words(listen: list) -> list:
    """Denne funksjonen filtrerer bort ord som ikke inneholder Z."""
    return list(filter(lambda word: 'Z' in word, listen))

Z_Liste = ["Zer", "Zyntanell", "Dantallian", "Jabir", "Zan"]
print(z_words(Z_Liste))  # Output: ['Zer', 'Zyntanell', 'Zan']

assert z_words(["Zer", "Zyntanell", "Dantallian", "Jabir", "Zan"]) == ['Zer', 'Zyntanell', 'Zan']

#9.2.2.2

1.  #Dectionary her setter opp definers alle rommene og antall seter de
rooms = {
    "Room 1": 10,
    "Room 2": 20,
    "Room 3": 30,
    "Room 4": 40,
    "Room 5": 50
}

# Funkjson som  sier at rom som ikke har navnet som de over blir ikke funnet 
def get_seats(room_name):
    return rooms.get(room_name, "Room not found")




# legg til 10+  seter Legger til 10 seter på et spesifikt rom

rooms ["Room 3"] += 10
print(f"Room 3 har nå {rooms['Room 3']} plasser.") 



# Minimum 50 Bruker en funksjon for å finne et rom med minst 50 seter
def find_large_rooms(min_seats=50):
    return [room for room, seats in rooms.items() if seats >= min_seats]

# Eksempel
large_rooms = find_large_rooms()
print(large_rooms)  # Output: ['Room 5']



