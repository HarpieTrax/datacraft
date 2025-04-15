# autoDocstring taper 3 fois " pour avoir l'autoDoc

import typing as t 
from typing import List, Dict, Union


def square(x : int =3) -> int:
    """calcule le carré d'un nombre

    Parameters
    ----------
    x : int
        a number

    Returns
    -------
    int
        square of this number
    """
    return x ** 2 


def triple_letter(letter : str ) -> t.List[str] :
    """crée une liste avec 3 fois la lettre passé en argument

    Parameters
    ----------
    letter : str
        lettre passé en argument à copier

    Returns
    -------
    t.List[str]
        liste contenant 3 fois la lettre passé en argument sous forme de caractère
    """
    return [letter] * 3

def find_max(numbers : List[int] ) -> int :
    """fct qui retourne le plus grand nb d'une liste de nb

    Parameters
    ----------
    numbers : List
        une liste de nb (int)

    Returns
    -------
    int
        le plus grand nb de la liste 

    Raises
    ------
    ValueError
        informe si la liste est vide
    """
    if not numbers:
        raise ValueError("The list is empty.")
    return max(numbers)

def divide(a : Union[int, float], b : Union[int, float]) -> Union[int, float] :
    """permet d'éffectuer une division d'entiers ou de nb décimales

    Parameters
    ----------
    a : Union[int, float]
        numérateur
    b : Union[int, float]
        dénominateur

    Returns
    -------
    Union[int, float]
        résultat de la division de a/b

    Raises
    ------
    ZeroDivisionError
        informe qu'on essaye d'effectuer une division par 0
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b if isinstance(a, float) or isinstance(b, float) else a // b


def add_entry(d : Dict[str, int], key : str, value : int) -> Dict[str, int]:
    """permet de créer un dico en lui donnant un nom, une clé et une valeur associé à cette clé

    Parameters
    ----------
    d : Dict[str, int]
        le dico ou on va ajouter une clé-valeur
    key : str
        la clé à ajouter au dico 
    value : int
        la valeur de la clé à ajouter au dico

    Returns
    -------
    Dict[str, int]
            le dictionnaire avec la nouvle paire clé-valeur
    """
    d[key] = value
    return d


    
def main() -> None:
    """appel la fct square à exécuter avec le nb 3

        la fct affiche uniquement un résultat 
    """
    n = 3
    print(square(n))


if __name__ == "__main__":
    main()

#Dans le terminal, entrer dans le fichier qui contient ce code 
# Puis python mon_fichier.py
