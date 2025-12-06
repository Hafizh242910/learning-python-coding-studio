import tkinter as tk

window = tk.Tk()
window.title("My Application")
window.geometry("300x250")

# buat label nama
nama = tk.Label(window, text="Nama: ")
nama.grid(row=0, column=0, padx=10, pady=10)

# buat entry nama
entry_nama = tk.Entry(window, width=20)
entry_nama.grid(row=0, column=1, padx=10, pady=10)

# buat entry email
email = tk.Entry(window, text="Email: ")
email.grid(row=1, column=0, padx=10, pady=10)

# buat entry email
entry_nama = tk.Entry(window, width=20)
entry_nama.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()