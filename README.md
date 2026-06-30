# sanasta-automation

SANASTA operacines sistemos MVP: Gmail ir saskaitu agento pradzia, pritaikyta Tomo darbo rezimui Starteris-Valdovas.

## Tikslas

Sistema turi kiekviena ideja, laiska, klienta ar objekta paversti aiskia uzduotimi:

- kas?
- kiek EUR arba kokia rizika?
- iki kada?
- kas atsakingas?
- kitas veiksmas?
- kur irasyta?

## Struktura

```text
agent/
  main.py              # paleidzia agenta ir rodo dienos 3 uzdarymus
  gmail_reader.py      # busima Gmail integracija
  invoice_parser.py    # busimas saskaitu duomenu istraukimas
  task_model.py        # SANASTA uzduoties modelis
  task_prioritizer.py  # A/B/C prioritetu logika
  daily_board.py       # dienos 3 uzdarymu lenta
AGENTS.md             # Codex darbo instrukcija
requirements.txt      # priklausomybes
```

## Starteris-Valdovas taisykle

Tomas stiprus ten, kur reikia pradeti, pramusti, parduoti ir spausti rezultata. Rizika: per daug pradetu frontu ir per mazai uzdarymo.

Kiekviena uzduotis turi tureti:

```text
OBJEKTAS / KLIENTAS:
VERTE EUR / RIZIKA:
TERMINAS:
ATSAKINGAS:
KITAS VEIKSMAS:
KUR IRASYTA:
BUSENA:
PRIORITETAS:
```

## Prioritetai

### A
Pinigai, klientas laukia, skola, teisine arba garantine rizika, terminas siandien arba rytoj.

A negalimas be:

- vertes arba rizikos,
- termino,
- kito veiksmo.

### B
Sistema: CRM, kalendorius, Trello, sablonai, procesai, standartai, automatizacija.

### C
Idejos be aiskios vertes, termino arba atsakingo zmogaus. Jos nedingsta, bet negali valdyti dienos.

## Dienos lenta

Sistema turi rodyti tik 3 pagrindinius uzdarymus:

1. Pinigu veiksmas
2. Sistemos veiksmas
3. Uzdarymo veiksmas

## Paleidimas

```bash
pip install -r requirements.txt
python agent/main.py
```

Kol Gmail integracija grazina tuscia sarasa, main.py parodo pavyzdines SANASTA uzduotis.

## Artimiausi darbai Codex'ui

1. Prijungti realu Gmail skaityma.
2. Is laisko automatiskai formuoti SanastaTask.
3. Prideti CSV eksporta.
4. Prideti paprasta telefono-friendly vaizda.
5. Prideti Google Calendar adapteri.
6. Prideti CRM arba Sheets eksporta.
