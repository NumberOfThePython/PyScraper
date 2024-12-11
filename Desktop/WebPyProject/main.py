import tkinter as tk
from tkinter import messagebox
from dead_linker import get_all_links, check_link_statuses

def analyze_links():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return

    # Pobranie linku i weryfikacja statusu
    try:
        links = get_all_links(url)
        if not links:
            messagebox.showinfo("Nie znaleziono linków", "Brak linków pod podanym URL!")
            return

       #Sprawdzenie statusów pod podanym linkaczem
        results = check_link_statuses(links)
        result_window = tk.Toplevel(root)
        result_window.title("Dead Link Checker")
        result_text = tk.Text(result_window, wrap="word")
        result_text.pack(expand=1, fill="both")

        # Wyświetlanie wyników na stronie - PAMIETAJ ZEBY USPRAWNIC I WYSWIETLAC TYLKO TE Z BLEDAMI
        for link, status in results.items():
            result_text.insert("end", f"{link}: {status}\n")
    except Exception as e:
        messagebox.showerror("Nieznany błąd", str(e))

# Zmiany w GUI
root = tk.Tk()
root.title("Dead Link Checker")

url_label = tk.Label(root, text="Podaj URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

check_button = tk.Button(root, text="Sprawdź linki na stronie!", command=analyze_links)
check_button.pack(pady=10)

root.mainloop()