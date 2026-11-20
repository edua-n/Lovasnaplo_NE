import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import lovas_NE

aktualis_lo = None

def rogzites():
    global aktualis_lo
    nev = lo_nev_be.get()

    try:
        perc = int(perc_be.get())

    except:
        messagebox.showinfo("Hiba!" ,"Nem számot adott meg!")
        return

    if aktualis_lo is None or aktualis_lo.lonev != nev:
        aktualis_lo = lovas_NE.Lo_NE(nev)

    aktualis_lo.edzeshozzaadas(perc)
    allapot = lovas_NE.terheles_ellenorzes_NE(aktualis_lo.hetialkalom)

    ma = datetime.date.today()
    pihenonap = datetime.timedelta(days=1)
    kovetkezo_edzes = ma + pihenonap
    datum_szoveg = kovetkezo_edzes.strftime("%d/%m/%Y")

    szoveg =(f"Ló neve: {aktualis_lo.lonev}\n"
             f"Heti edzések száma: {aktualis_lo.hetialkalom} alkalom\n"
             f"Összesített idő: {aktualis_lo.osszesperc}perc\n"
             f"Értékelés: {allapot}\n"
             f"Következő edzés (1 pihenőnap után): {datum_szoveg}"
            )
    eredmeny_cimke.configure(text=szoveg)

root = tk.Tk()
root.geometry('600x400')
root.title('app')
root.resizable(False, False)

cim_cimke = ttk.Label(text="Lovasnapló", font=('Arial', 12, 'bold'))
cim_cimke.grid(column=0, row=0, padx=20, pady=20)

lo_nev_szoveg = tk.StringVar(value="Hope")
lo_nev_be = ttk.Entry(textvariable=lo_nev_szoveg, width=15)
lo_nev_be.grid(column=0, row=1, padx=20, pady=10)

perc_szoveg = tk.StringVar(value="40")
perc_be = ttk.Entry(textvariable=perc_szoveg, width=10)
perc_be.grid(column=1, row=1, padx=10, pady=20)

rogzites_gomb = ttk.Button(text = "Edzés rögzítése", command=rogzites)
rogzites_gomb.grid(column=2, row=1, padx=10, pady=10)

kilepes_gomb =ttk.Button(text = "Kilépés", width= 10, command=root.destroy)
kilepes_gomb.grid(column=3, row=1, padx=10, pady=10)

eredmeny_cimke = ttk.Label(root, text ="Eredmény", font=('Arial', 12))
eredmeny_cimke.grid(column=0, row=2,columnspan= 4, padx=20, pady=20)

root.mainloop()

