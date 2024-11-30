def pgcd(a, b):
    min_val = min(a, b)

    for i in range(min_val, 0, -1):  
        if a % i == 0 and b % i == 0:
            return i  a = int(input("Entrez le premier nombre : "))
b = int(input("Entrez le deuxième nombre : "))
resultat = pgcd(a, b)
print(f"Le PGCD de {a} et {b} est : {resultat}")
