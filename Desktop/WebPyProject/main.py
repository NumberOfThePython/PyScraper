import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from threading import Thread
from dead_linker import get_all_links, check_link_statuses

def analyze_links():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Niepoprawny link", "Podaj poprawny URL!")
        return

    status_label.config(text="Weryfikacja w toku...")
    check_button.config(state="disabled")
    progress_bar.start()
    progress_bar.pack(pady=12)

    def progressbar():
        try:
            links = get_all_links(url)
            if not links:
                root.after(0, lambda: messagebox.showinfo("Linków nie znaleziono", "Pod podanym URL nie ma linków do analizy"))
                root.after(0, lambda: status_label.config(text="Linków nie znaleziono"))
                return

            results = check_link_statuses(links)

            # Logujemy wyniki do konsoli
            print(f"Wyniki analizy: {results}")

            if not results:
                root.after(0, lambda: messagebox.showinfo("Brak błędnych linków", "Wszystkie linki mają status 200."))
                root.after(0, lambda: status_label.config(text="Wszystkie linki poprawne."))
                return

            # Przekazanie wyników do UI
            root.after(0, show_results, results)
        except Exception as e:
            root.after(0, lambda: messagebox.showerror("Error", str(e)))
        finally:
            root.after(0, lambda: progress_bar.stop())
            root.after(0, lambda: progress_bar.pack_forget())
            root.after(0, lambda: status_label.config(text="Proces zakończony."))
            root.after(0, lambda: check_button.config(state="normal"))

    analysis_thread = Thread(target=progressbar)
    analysis_thread.start()

def show_results(results):
    # Wyświetlenie wyników
    result_window = tk.Toplevel(root)
    result_window.title("Wyniki")
    result_text = tk.Text(result_window, wrap="word")
    result_text.pack(expand=1, fill="both")

    for link, status in results.items():
        result_text.insert("end", f"{link}: {status}\n")

# Zmiany w GUI
root = tk.Tk()
root.title("Dead Link Checker")

url_label = tk.Label(root, text="Podaj URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

check_button = tk.Button(root, text="Sprawdź linki na stronie!", command=analyze_links)
check_button.pack(pady=10)

status_label = tk.Label(root, text="", fg="red")
status_label.pack(pady=10)

# Dodanie Progressbar
progress_bar = ttk.Progressbar(root, mode="indeterminate")
progress_bar.pack(pady=10)
progress_bar.grid_remove()  # Ukrycie Progressbar na początku

root.mainloop()