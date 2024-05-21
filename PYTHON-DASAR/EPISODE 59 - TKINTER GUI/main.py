# studi kasus
# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False, False)
window.title("Sapa, Dia!")

# variabel dan fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()


def tombol_click():
    """fungsi ini akan dipanggil oleh tombol"""
    pesan = f"Hallo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, ganteng"
    showinfo(title="whatsssupp!", message=pesan)


# frame input
input_frame = ttk.Frame(window)
# penempatan grid, pack, place
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# komponen-komponen
# 1. label untuk nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama depan : ")
nama_depan_label.pack(padx=10, fill="x", expand=True)
# 2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x", expand=True)
# 3. label untuk nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama belakang : ")
nama_belakang_label.pack(padx=10, fill="x", expand=True)
# 4. entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)


# 5. tombol
tombol_sapa = ttk.Button(input_frame, text="sapa!", command=tombol_click)
tombol_sapa.pack(fill="x", expand=True, pady=10, padx=10)

# main loop window
window.mainloop()
