import tkinter as tk
from tkinter import messagebox
from dead_linker import check_dead_link

# FUNKCJA do wpisania dla przycisku "sprawdź linki":
def on_check_link():
    url = url_entry.get() #pobranie URL z pola URL_ENTRY DO ZDEFINIOWANIA JAKO POLE
    if not url:
        messagebox.showwarning("Podaj URL.")
        return

    try:
        response = requests.get(url)
        if response.status_code == 404:
            status.label.config(text="Błąd 404")
        elif response.status_code == 403:
            status.label.config(text="Bład 403 [Forbidden]")
        elif response.status.code == 500:
            status.label.config(text="Błąd 500 [Internal Server Error]")
        else:
            status.label.config(text=f"Link jest OK (Status: {response.status_code})")
    except requests.exceptions.RequestException as e:
        status_label.config(text=f"Błąd: {e}")


# Tworzymy główne okno aplikacji
root = tk.Tk()
root.title("Dead Link Checker")

# Etykieta dla URL
url_label = tk.Label(root, text="Wprowadź Link:")
url_label.pack(pady=10)

# Pole tekstowe do wprowadzenia URL
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

#przycisk do sprawdzenia linku
check_button = tk.Button(root, text="Sprawdź linki", command=check_dead_link)
check_button.pack(pady=10)

#etykieta, która wyświetli status linku
status_label = tk.Label(root, text="", fg="red")
status_label.pack(pady=10)

#pętla
root.mainloop()


