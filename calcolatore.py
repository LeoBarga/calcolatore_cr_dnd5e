import tkinter as tk
from tkinter import ttk

# Funzione principale per calcolare la CR (Classe di Sfida)
def calcola_cr():
    # Recupera i valori inseriti dall'utente nell'interfaccia
    tipo = tipo_var.get()
    n_giocatori = int(giocatori_var.get())
    livello_pg = int(livello_var.get())
    n_nemici = int(nemici_var.get()) if tipo == "Nemici multipli" else 1

    # Calcola un modificatore in base al numero di giocatori e al livello
    if 1 <= livello_pg <= 7:
        modificatore = {2: 1, 3: 0.5, 4: 0, 5: -0.5, 6: -1}.get(n_giocatori, 0)
        modificatore_scagn = 1
    elif 8 <= livello_pg <= 15:
        modificatore = {2: 1.5, 3: 1, 4: 0, 5: -1, 6: -1.5}.get(n_giocatori, 0)
        modificatore_scagn = 2
    else:
        modificatore = {2: 2, 3: 1.5, 4: 0, 5: -1.5, 6: -2}.get(n_giocatori, 0)
        modificatore_scagn = 3.5

    # Definisce una CR base in funzione del livello dei personaggi
    if livello_pg in [1, 2]:
        base_cr = 1
    elif livello_pg in [3, 4]:
        base_cr = 2
    elif livello_pg in [5, 6]:
        base_cr = 4
    elif livello_pg in [7, 8]:
        base_cr = 6
    elif livello_pg in [9, 10]:
        base_cr = 9
    elif livello_pg in [11, 12]:
        base_cr = 11
    elif livello_pg in [13, 14]:
        base_cr = 13
    elif livello_pg in [15, 16]:
        base_cr = 15
    elif livello_pg in [17, 18]:
        base_cr = 17
    else:
        base_cr = 19

    # Modifica la CR base in base al tipo di incontro e al numero di nemici
    if tipo == "Boss + scagnozzi":
        base_cr -= 1 if livello_pg <= 10 else 2
    elif tipo == "Nemici multipli":
        if n_nemici == 1:
            pass
        elif n_nemici == 2:
            base_cr = base_cr / 1.5
        elif 3 <= n_nemici <= 6:
            base_cr = base_cr / 2
        elif 7 <= n_nemici <= 10:
            base_cr = base_cr / 3
        else:
            base_cr = base_cr / 3.5

    # Calcola la CR finale per ciascun livello di difficoltà
    facile = round(max(0.125, base_cr - modificatore), 2)
    medio = round(max(0.125, base_cr + 1 - modificatore), 2)
    difficile = round(max(0.125, base_cr + 2 - modificatore), 2)
    letale = round(max(0.125, base_cr + 4 - modificatore), 2)

    # Calcola la CR dei possibili scagnozzi
    facile_scagn = round(max(0.125, modificatore_scagn), 2)
    medio_scagn = round(max(0.125, modificatore_scagn + 0.5), 2)
    difficile_scagn = round(max(0.125, modificatore_scagn + 1), 2)
    letale_scagn = round(max(0.125, modificatore_scagn + 1.5), 2)

    # Crea la stringa di output da mostrare all’utente
    risultato = (
        f"CR consigliata per ciascun livello di difficoltà:\n"
        f"Facile: {facile}\n"
        f"Medio: {medio}\n"
        f"Difficile: {difficile}\n"
        f"Letale: {letale}"
    )

    # Se si tratta di un boss con scagnozzi, aggiungi info sulla loro CR
    if tipo == "Boss + scagnozzi":
        risultato += (
            f"\n\nCR consigliato scagnozzi per ogni livello di difficoltà:\n"
            f"Facile: {facile_scagn}\n"
            f"Medio: {medio_scagn}\n"
            f"Difficile: {difficile_scagn}\n"
            f"Letale: {letale_scagn}\n\n"
            "Nota: Questa CR è calcolata per un numero di scagnozzi uguale al numero di giocatori "
            "e può essere un pò imprecisa a livelli molto bassi (1, 2, 3)."
            "Gli scagnozzi possono avere vari scopi come danni, effetti di stato, copertura del boss ecc. "
            "sulla base dei quali si può variare leggermente la CR ma non devono mai dominare o si perde il senso del boss."
        )

    # Mostra il risultato nell'etichetta della GUI
    risultato_label.config(text=risultato)


# ---- SETUP DELL’INTERFACCIA GRAFICA ----

# Crea finestra principale
finestra = tk.Tk()
finestra.title("Calcolatore CR per DnD 5e")
finestra.geometry("500x600")

# Etichetta di benvenuto
tk.Label(finestra, text="Benvenuto nel calcolatore di Classe Sfida per DnD 5e!", font=("Helvetica", 12, "bold")).pack(pady=10)

# Selezione tipo incontro
tk.Label(finestra, text="Tipo di Encounter:").pack()
tipo_var = tk.StringVar(value="Boss singolo")
tipi = ["Boss singolo", "Boss + scagnozzi", "Nemici multipli"]
tk.OptionMenu(finestra, tipo_var, *tipi).pack()

# Selezione numero giocatori
tk.Label(finestra, text="Numero di giocatori:").pack()
giocatori_var = tk.StringVar(value="4")
tk.Spinbox(finestra, from_=2, to=6, textvariable=giocatori_var).pack()

# Selezione livello dei personaggi
tk.Label(finestra, text="Livello dei personaggi:").pack()
livello_var = tk.StringVar(value="5")
tk.Spinbox(finestra, from_=1, to=20, textvariable=livello_var).pack()

# Selezione numero di nemici (solo per "Nemici multipli")
tk.Label(finestra, text="Numero di nemici (se hai selezionato multipli):").pack()
nemici_var = tk.StringVar(value="3")
tk.Spinbox(finestra, from_=1, to=14, textvariable=nemici_var).pack()

# Bottone per calcolare la CR
tk.Button(finestra, text="Calcola CR", command=calcola_cr, bg="lightgreen").pack(pady=10)

# Etichetta per visualizzare il risultato
risultato_label = tk.Label(
    finestra,
    text="",
    justify="left",
    font=("Courier", 10),
    wraplength=480,  # Imposta larghezza massima prima di andare a capo
    anchor="w"       # Allineamento a sinistra
)
risultato_label.pack(pady=10, fill="both", expand=True)

# Avvia l'interfaccia grafica
finestra.mainloop()
