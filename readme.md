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

```
bank-etl2/
│
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
│
├── .github/workflows/
│   └── ci.yml
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Pipeline ETL

La pipeline elabora i dati grezzi seguendo queste fasi:

```
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
```

---

## 🧪 Data Quality e validazione

Il sistema garantisce l’affidabilità dei dati attraverso:

- Rilevamento valori nulli
- Conversione e validazione dei tipi
- Applicazione di regole di business
- Separazione dei record validi e non validi


## 🧪 Data Quality e validazione

Il sistema garantisce l’affidabilità dei dati attraverso:

- Rilevamento valori nulli
- Conversione e validazione dei tipi
- Applicazione di regole di business
- Separazione dei record validi e non validi

---

## 📊 Sistema di logging

Ogni esecuzione della pipeline viene tracciata tramite log strutturati:

```
2026-06-16 16:12:15 - ETL START
2026-06-16 16:12:17 - Record estratti: 2000000
2026-06-16 16:12:21 - Record validi: 1980087
2026-06-16 16:12:21 - Record non validi: 19913
2026-06-16 16:13:04 - Caricamento completato
2026-06-16 16:13:04 - ETL END
```


I log vengono salvati per mantenere uno storico delle esecuzioni e garantire tracciabilità.

---

## 🧪 Test automatici

Il progetto include test unitari per garantire la stabilità della pipeline.

### Esempi di test:

- Validazione valori non nulli per account
- Verifica unicità transaction_id
- Controlli sulle trasformazioni dei dati

### Esempio output:


collected 4 items

test_transform.py .... [100%]

4 test superati in 0.72s


---

## 🔒 CI/CD e protezione branch

Il repository utilizza regole di protezione su GitHub:

- Il branch `main` è protetto
- Non è consentito il push diretto su `main`
- Le modifiche devono passare tramite Pull Request
- La pipeline CI viene eseguita automaticamente ad ogni commit

### Workflow:


feature branch → pull request → review → merge → main


### Esempio errore su branch protetto:


GH006: aggiornamento non consentito sul branch protetto
Le modifiche devono essere effettuate tramite Pull Request


---

## 📈 Valore del progetto

Questo progetto migliora affidabilità e qualità dei dati attraverso:

- Riduzione delle regressioni
- Automazione dei controlli
- Maggiore fiducia nei dati analitici
- Migliore manutenibilità della pipeline ETL

---

## ✅ Risultati ottenuti

- Pipeline ETL completamente automatizzata
- Dataset puliti e standardizzati
- Framework di test integrato (pytest)
- CI/CD attivo con GitHub Actions
- Workflow di sviluppo in stile enterprise