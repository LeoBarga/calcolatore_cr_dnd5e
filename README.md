#  Calcolatore Classe di Sfida (CR) per D&D 5e

Benvenuto nel **Calcolatore CR per Dungeons & Dragons 5a Edizione**, un'applicazione grafica scritta in Python con `tkinter`, pensata per supportare i Dungeon Master nel bilanciamento degli incontri in base al numero e al livello dei personaggi giocanti.

##  Funzionalità

- Calcola la **Classe di Sfida consigliata** per un nemico in base:
  - al numero di giocatori,
  - al loro livello,
  - al tipo di incontro (boss singolo, boss con scagnozzi, nemici multipli).
- Fornisce suggerimenti per la CR degli scagnozzi quando presenti.
- Interfaccia grafica semplice e chiara, facilmente utilizzabile durante la preparazione di una sessione.

##  Come usarlo

###  Requisiti

- Python 3.7 o superiore
- Libreria `tkinter` (inclusa di default in Python)

###  Avvio

Clona questo repository e avvia lo script Python:

```bash
git clone https://github.com/tuo-username/calcolatore_cr_dnd5e.git
cd calcolatore_cr_dnd5e
python calcolatore_cr.py
```

###  File principali

- calcolatore_cr.py – contiene tutta la logica del calcolo CR e l'interfaccia grafica.

###  Dettagli del calcolo

La CR viene adattata automaticamente in base:

- al numero di giocatori (con modificatori proporzionati),

- al livello dei PG,

- alla struttura dell’incontro:

    - Boss singolo

    - Boss con scagnozzi

    - Nemici multipli

Sono previsti output per 4 livelli di difficoltà:

- Facile

- Medio

- Difficile

- Letale

Nel caso di "Boss + scagnozzi", il calcolatore include una CR specifica per gli scagnozzi e una nota descrittiva sul loro uso bilanciato.

## Perchè usarlo

Bilanciare gli incontri in D&D 5e può diventare complicato e soggettivo. Questo strumento ti offre una guida chiara, coerente e flessibile per creare sfide adeguate alle capacità del gruppo.

## Contribuire

Pull request, issue e suggerimenti sono benvenuti! Se hai idee per nuove funzionalità (es. generatore di mostri, export PDF, gestione campagne) apri una issue o proponi una PR.