import tkinter

main_window = tkinter.Tk()
# setiap kelas pasti huruf besar
# kalo huruf kecil itu fungsi

print(main_window.__dict__)

label1 = tkinter.Label(main_window, text="label 1")
label2 = tkinter.Label(main_window, text="label 2")
label3 = tkinter.Label(main_window, text="label 3")

tombol1 = tkinter.Button(main_window, text="tombol1")
tombol2 = tkinter.Button(main_window, text="tombol2")

# method positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()


# method menampilkan GUI
main_window.mainloop()
