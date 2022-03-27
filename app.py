import tkinter as tk
import dao

def hirdetesekShow():
    result = dao.hirdetesekQuerry()
    for r in result:
        root.text = tk.Label()
        root.text["text"] = r
        root.text.grid(row=1+i, column=0)


root = tk.Tk()
root.title("Állásbörze")
root.geometry("400x300")

root.hirdetesek = tk.Button(text="Hirdetések lekérdezése", command=hirdetesekShow)
root.hirdetesek.grid(row=0,column=0)




root.mainloop()