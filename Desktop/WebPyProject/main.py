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
        else
            status.label.config(text=f"Link jest OK (Status: {response.status_code})")
    except requests.exceptions.RequestException as e:
        status_label.config(text=f"Błąd: {e}")

