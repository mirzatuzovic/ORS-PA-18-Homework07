"""
===================   TASK 4  ====================
* Name: Number of Appearances
*
* Write a function that will return which element
* of integer list has the greatest number of
* appearances in that list.
* In case that multiple elements have the same
* number of appearances return any.
*
* Note: You are not allowed to use built-in
* functions.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here


def broj_pojavljivanja_u_listi(lista):

    d= {}
    duzina = len(lista)
    broj_javljanja = 0

    for i in range(duzina):

        if lista[i] not in d:

            for broj in range(i,duzina):


                if lista[broj] == lista[i]:

                    broj_javljanja += 1

                dati_broj = lista[i]

                d[dati_broj] = broj_javljanja
        broj_javljanja=0

    niz = []

    for key in d:

        niz.append(d[key])
    maksimum = niz[0]

    for i in range(len(niz)):
        if niz[i]  >maksimum:
            maksimum=niz[i]


    for key in d:
        if maksimum==d[key]:
            return key



def main():

    lista = [3,8,2,3,6,4,3,8,6,0,9,1,2,4,3]
    x = broj_pojavljivanja_u_listi(lista)

    print("U datoj listi se najvise pojavljuje broj: " + str (x))
    pass

if __name__ == "__main__":
    main()