import tkinter as tk
from tkinter import ttk, messagebox
import requests

def oblicz_elastycznosc(typ, cena_poczatkowa, cena_koncowa, ilosc_poczatkowa, ilosc_koncowa):
    try:
        zmiana_procentowa_ceny = ((cena_koncowa - cena_poczatkowa) / cena_poczatkowa) * 100
        zmiana_procentowa_ilosci = ((ilosc_koncowa - ilosc_poczatkowa) / ilosc_poczatkowa) * 100
        elastycznosc = zmiana_procentowa_ilosci / zmiana_procentowa_ceny

        if typ == "cenowa":
            if elastycznosc > 1:
                opis_elastycznosci = "Elastyczny"
            elif elastycznosc < 1:
                opis_elastycznosci = "Nieelastyczny"
            else:
                opis_elastycznosci = "Jednostkowa elastyczność"
        elif typ == "dochodowa":
            if elastycznosc > 1:
                opis_elastycznosci = "Dobro luksusowe"
            elif elastycznosc > 0:
                opis_elastycznosci = "Dobro normalne"
            else:
                opis_elastycznosci = "Dobro podrzędne"
        elif typ == "krzyzowa":
            if elastycznosc > 0:
                opis_elastycznosci = "Substytuty"
            elif elastycznosc < 0:
                opis_elastycznosci = "Komplementy"
            else:
                opis_elastycznosci = "Niezależne"

        return elastycznosc, opis_elastycznosci

    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź prawidłowe liczby.")
        return None, None

def oblicz_elastycznosc_cenowa():
    cena_poczatkowa = float(entry_cena_poczatkowa.get())
    cena_koncowa = float(entry_cena_koncowa.get())
    ilosc_poczatkowa = float(entry_ilosc_poczatkowa.get())
    ilosc_koncowa = float(entry_ilosc_koncowa.get())
    elastycznosc, opis_elastycznosci = oblicz_elastycznosc("cenowa", cena_poczatkowa, cena_koncowa, ilosc_poczatkowa, ilosc_koncowa)
    if elastycznosc is not None:
        result_label.config(text=f"Elastyczność cenowa popytu: {elastycznosc:.2f} ({opis_elastycznosci})")
        history_listbox.insert(tk.END, f"Elastyczność cenowa: {elastycznosc:.2f} ({opis_elastycznosci})")

def oblicz_elastycznosc_dochodowa():
    dochod_poczatkowy = float(entry_dochod_poczatkowy.get())
    dochod_koncowy = float(entry_dochod_koncowy.get())
    ilosc_poczatkowa = float(entry_ilosc_poczatkowa.get())
    ilosc_koncowa = float(entry_ilosc_koncowa.get())
    elastycznosc, opis_elastycznosci = oblicz_elastycznosc("dochodowa", dochod_poczatkowy, dochod_koncowy, ilosc_poczatkowa, ilosc_koncowa)
    if elastycznosc is not None:
        result_label.config(text=f"Elastyczność dochodowa popytu: {elastycznosc:.2f} ({opis_elastycznosci})")
        history_listbox.insert(tk.END, f"Elastyczność dochodowa: {elastycznosc:.2f} ({opis_elastycznosci})")

def oblicz_elastycznosc_cenowa_krzyzowa():
    cena_poczatkowa_a = float(entry_cena_poczatkowa_a.get())
    cena_koncowa_a = float(entry_cena_koncowa_a.get())
    ilosc_poczatkowa_b = float(entry_ilosc_poczatkowa_b.get())
    ilosc_koncowa_b = float(entry_ilosc_koncowa_b.get())
    elastycznosc, opis_elastycznosci = oblicz_elastycznosc("krzyzowa", cena_poczatkowa_a, cena_koncowa_a, ilosc_poczatkowa_b, ilosc_koncowa_b)
    if elastycznosc is not None:
        result_label.config(text=f"Elastyczność cenowa krzyżowa popytu: {elastycznosc:.2f} ({opis_elastycznosci})")
        history_listbox.insert(tk.END, f"Elastyczność cenowa krzyżowa: {elastycznosc:.2f} ({opis_elastycznosci})")

def pobierz_kurs_wymiany():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        kurs = data["rates"]["PLN"]
        exchange_rate_label.config(text=f"Kurs USD/PLN: {kurs:.2f}")
    except requests.RequestException as e:
        messagebox.showerror("Błąd", f"Nie udało się pobrać kursu wymiany: {e}")

def odswiez_kurs_wymiany():
    pobierz_kurs_wymiany()

root = tk.Tk()
root.title("Kalkulator Wartości Ekonomicznych")
root.geometry("800x600")

exchange_rate_label = ttk.Label(root, text="Kurs USD/PLN: Ładowanie...")
exchange_rate_label.place(x=600, y=10)
refresh_button = ttk.Button(root, text="Odśwież kurs", command=odswiez_kurs_wymiany)
refresh_button.place(x=610, y=35)

label_cena_poczatkowa = ttk.Label(root, text="Cena początkowa:")
label_cena_poczatkowa.place(x=50, y=50)
entry_cena_poczatkowa = ttk.Entry(root)
entry_cena_poczatkowa.place(x=150, y=50)

label_cena_koncowa = ttk.Label(root, text="Cena końcowa:")
label_cena_koncowa.place(x=50, y=80)
entry_cena_koncowa = ttk.Entry(root)
entry_cena_koncowa.place(x=150, y=80)

label_ilosc_poczatkowa = ttk.Label(root, text="Ilość początkowa:")
label_ilosc_poczatkowa.place(x=50, y=110)
entry_ilosc_poczatkowa = ttk.Entry(root)
entry_ilosc_poczatkowa.place(x=150, y=110)

label_ilosc_koncowa = ttk.Label(root, text="Ilość końcowa:")
label_ilosc_koncowa.place(x=50, y=140)
entry_ilosc_koncowa = ttk.Entry(root)
entry_ilosc_koncowa.place(x=150, y=140)

calculate_price_elasticity_button = ttk.Button(root, text="Oblicz elastyczność cenową", command=oblicz_elastycznosc_cenowa)
calculate_price_elasticity_button.place(x=50, y=170)

label_dochod_poczatkowy = ttk.Label(root, text="Dochód początkowy:")
label_dochod_poczatkowy.place(x=50, y=220)
entry_dochod_poczatkowy = ttk.Entry(root)
entry_dochod_poczatkowy.place(x=150, y=220)

label_dochod_koncowy = ttk.Label(root, text="Dochód końcowy:")
label_dochod_koncowy.place(x=50, y=250)
entry_dochod_koncowy = ttk.Entry(root)
entry_dochod_koncowy.place(x=150, y=250)

calculate_income_elasticity_button = ttk.Button(root, text="Oblicz elastyczność dochodową", command=oblicz_elastycznosc_dochodowa)
calculate_income_elasticity_button.place(x=50, y=280)

label_cena_poczatkowa_a = ttk.Label(root, text="Cena początkowa Produktu A:")
label_cena_poczatkowa_a.place(x=50, y=330)
entry_cena_poczatkowa_a = ttk.Entry(root)
entry_cena_poczatkowa_a.place(x=220, y=330)

label_cena_koncowa_a = ttk.Label(root, text="Cena końcowa Produktu A:")
label_cena_koncowa_a.place(x=50, y=360)
entry_cena_koncowa_a = ttk.Entry(root)
entry_cena_koncowa_a.place(x=220, y=360)

label_ilosc_poczatkowa_b = ttk.Label(root, text="Ilość początkowa Produktu B:")
label_ilosc_poczatkowa_b.place(x=50, y=390)
entry_ilosc_poczatkowa_b = ttk.Entry(root)
entry_ilosc_poczatkowa_b.place(x=220, y=390)

label_ilosc_koncowa_b = ttk.Label(root, text="Ilość końcowa Produktu B:")
label_ilosc_koncowa_b.place(x=50, y=420)
entry_ilosc_koncowa_b = ttk.Entry(root)
entry_ilosc_koncowa_b.place(x=220, y=420)

calculate_cross_price_elasticity_button = ttk.Button(root, text="Oblicz elastyczność cenową krzyżową", command=oblicz_elastycznosc_cenowa_krzyzowa)
calculate_cross_price_elasticity_button.place(x=50, y=450)

result_label = ttk.Label(root, text="Wynik: ")
result_label.place(x=400, y=60)

history_label = ttk.Label(root, text="Historia:")
history_label.place(x=400, y=100)
history_listbox = tk.Listbox(root, height=10, width=50)
history_listbox.place(x=400, y=130)

odswiez_kurs_wymiany()

root.mainloop()
