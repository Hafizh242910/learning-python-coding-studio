import tkinter as tk

window = tk.Tk()
window.title("My Application")
window.geometry("300x250")

def sapa():
    hasil_nama = entry.get()
    label_ouput.config(text= f"Halo {hasil_nama}")
    # print(f"Halo {hasil_nama}")

# label
label = tk.Label(window, text="Inputkan Namamu:", font=("Helvetica", 20))
label.pack(pady=5)

# entry
entry = tk.Entry(window, width=20)
entry.pack(pady=5)

# button
button = tk.Button(window, text="Sapa Aku!", command=sapa)
button.pack(pady=5)

label_ouput = tk.Label(window, text="")
label_ouput .pack(pady=5)

# jalankan GUI
window.mainloop()