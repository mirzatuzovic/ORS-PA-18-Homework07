
"""
===================   TASK 2  ====================
* Name: Recursive Sum
*
* Write a recursive function that will sum given
* list of integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here


def sum(lista):

    duzina = len(lista)

    if duzina == 1:

        return lista[0]

    else:

        return sum(lista[1:]) + lista[0]


def main():
    lista= [4,3,8,2,9,7]

    print("Suma brojeva date liste je: " + str(sum(lista)))
    pass

if __name__ == "__main__":
    main()
