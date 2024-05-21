data = "ini adalah string"
print(data)
print(type(data))


# 1. Cara membuat string
"""
1. dengan menggunakan single quote'...'
2. dengan menggunakan double quote"..."
"""

data = "menggunakan single quote"
print(data)

data = "menggunakan double quote"
print(data)

print('"Hallo, apa kabar?"')
print("'Hallo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda |

# membuat tanda ' menjadi string
print("mari shalat jum'at")
print("g'day, is'nt it?")  #'g\'day, is\'nt it?'

# backlash
print("C:\\user\\Ucup")

# tab
print("ucup \t\totong , jauhan")

# backspace
print("ucup \botong, deketan")

# newline
print("baris pertama.\n ini baris kedua.")  # lf-line feed
print("baris pertama.\r baris kedua.")  # cr carriage return
print(
    "baris pertama. \r\n baris kedua."
)  # cr lf - line feed carriage return -> dipakai oleh windows

# 3. String litteral atau raw
# hati-hati
print("C:\new folder")  # hati-hati akan salah path
print("C:\\new folder")

# menggunakan raw string
print(r"C:\new folder")

# multiline literal string
print(
    """
nama : ucup
kelas : 3 SD
"""
)

# multiline itteral string dan raw
print(
    r"""sumary_line
nama : ucup
kelas : 3 SD \newnormal 
Website : www.Ucup.com/NewID
"""
)
