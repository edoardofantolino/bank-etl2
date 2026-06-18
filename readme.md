# 📊 Progetto Bank ETL – Pipeline Dati con CI/CD

## 🚀 Panoramica

Questo progetto simula un ambiente di data engineering per la gestione di transazioni bancarie, con focus su:

- Estrazione, pulizia e trasformazione dei dati
- Controlli di qualità e validazione dei dati
- Monitoraggio e analisi dei processi
- Automazione CI/CD tramite GitHub Actions

L’obiettivo è dimostrare la costruzione di una pipeline dati in stile enterprise, con buone pratiche di software engineering.

---

## 🧱 Architettura del progetto

bank-etl2/\n
       │\n
       ├── data/
       │   ├── raw/
       │   └── processed/
       │
       ├── src/
       │   ├── generator/
       │   ├── extract.py
       │   ├── transform.py
       │   ├── load.py
       │   ├── main.py    
       │   └── logger.py
       │
       ├── tests/
       ├── logs/
       │   └── etl.log            
       ├── .github/workflows/
       │   └── ci.yml                
       ├── requirements.txt
       └── README.md

---

## ⚙️ Pipeline ETL

La pipeline elabora i dati grezzi seguendo queste fasi:

CSV INPUT
│
▼
CONTROLLI DI QUALITÀ,
PULIZIA E STANDARDIZZAZIONE
│
▼ 
RECORD VALIDI e RECORD NON VALIDI
│ 
▼
LOGGING E AUDIT TRAIL
│
▼
TEST PYTEST
│
▼
GITHUB ACTIONS (CI/CD)


---

## 🧪 Data Quality e validazione

Il sistema garantisce l’affidabilità dei dati attraverso:

- Rilevamento valori nulli
- Conversione e validazione dei tipi
- Applicazione di regole di business
- Separazione dei record validi e non validi


## 📊 Sistema di logging

Ogni esecuzione della pipeline viene tracciata tramite log strutturati:
