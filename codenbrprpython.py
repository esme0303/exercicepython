def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def nombres_premiers_1_a_100():
    premiers = []
    for num in range(1, 101):
        if est_premier(num):
            premiers.append(num)
    return premiers
print("Les nombres premiers de 1 à 100 sont :")
print(nombres_premiers_1_a_100())
