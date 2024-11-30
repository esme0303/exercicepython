def factorielle(n):
    """Calcule la factorielle d'un nombre entier positif."""
    if n < 0:
        return "La factorielle n'est pas définie pour les nombres négatifs."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def main():
    print("Calcul de la factorielle de deux nombres.")
    
    num1 = int(input("Entrez le premier nombre :
