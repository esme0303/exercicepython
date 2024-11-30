def main():
    print("Déterminons la dérivée et la primitive d'une fonction polynôme du second degré.")
    a = float(input("Entrez le coefficient a (devant x^2) : "))
    b = float(input("Entrez le coefficient b (devant x) : "))
    c = float(input("Entrez le coefficient c (constante) : "))
    print(f"\nLa fonction polynôme est : f(x) = {a}x^2 + {b}x + {c}")
    derivative_a = 2 * a
    derivative_b = b
    print(f"La dérivée de f(x) est : f'(x) = {derivative_a}x + {derivative_b}")
    primitive_a = a / 3
    primitive_b = b / 2
    primitive_c = c
    print(f"La primitive de f(x) est : F(x) = {primitive_a}x^3 + {primitive_b}x^2 + {primitive_c}x + C")
    print("(C est une constante d'intégration)")
if __name__ == "__main__":
    main()
   
