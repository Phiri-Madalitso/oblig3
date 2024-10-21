#Dette er funksjon er for my str-len
    #My_str_len :: string -> number
    #Input er selve ordet 
    #Output er antall tegn

def my_str_len(ord):
    siffer = 0
    for char in ord:
        siffer += 1
    return siffer

print(my_str_len("test")) #output 4

# my_max :: List -> number
# Input Listen med de forskjellige tallene
# Output Det kommer i form av tall, som er det høyeste nummeret. 
def my_max(lst):
    if not lst:
        raise Valueerror ("The list cannot be empty")
    
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value
    
print(my_max([1, 2, 7, 4, 5])) #5. output


