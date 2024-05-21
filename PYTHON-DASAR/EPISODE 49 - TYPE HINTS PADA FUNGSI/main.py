"""Type hints untuk fungsi"""

"""
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)


fungsi(1)
fungsi("ucup")
fungsi(True)
"""
# penggunaan type hints
import string


def sepuluh_pangkat(argument: int) -> int:
    output = 10**argument
    return output


HASIL = sepuluh_pangkat(2)
print(HASIL)


def display(argument: string):
    return argument


display("ucup")
import os

hasil = os.system("cls")
print(hasil)
