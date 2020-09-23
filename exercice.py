#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
  
    return abs(float(input("Entrez un nombre : ")))


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOPQ', 'ack'
l = len(prefixes)
result = []
for i in range(l):
  name = prefixes[i] + suffixe
  result.append(name)
  
    return result


S = 0

for Number in range(1, 101):
    count = 0
    for i in range(2, (Number // 2 + 1)):
        if (Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        S=S+Number
print(S)
      


def factorial(number: int) -> int:
  number = input( 'Veuillez saisir un nombre n : ')
number = int(number)

Factoriel = 1
for i in range(1,number+1):
  Factoriel = i*Factoriel
print(Factoriel)

    return 0


def use_continue() -> None:
  for i in range(1,11):

  if i!=5:
    pass
    print(i)
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
