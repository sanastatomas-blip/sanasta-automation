# SANASTA sistemu tarpusavio komunikacijos architektura

## Paskirtis

Sis dokumentas apraso, kaip SANASTA sistemos turi kalbeti tarpusavyje, kad Tomas nebutu rankinis tarpininkas tarp Gmail, WhatsApp, Calendar, CRM, Trello, saskaitu, pasiulymu ir monitoringo.

Tikslas: kiekviena zinute, laiskas, skambutis, saskaita, pasiulymas ar monitoringo signalas turi virsti aiskiu ivykiu su statusu, kita veiksmu ir vieta sistemoje.

## Pagrindine taisykle

Visos sistemos turi keistis ne padriku tekstu, o vienodu ivykiu formatu.

Jeigu informacija ateina is Gmail, WhatsApp, telefono diktavimo, kalendoriaus ar monitoringo, ji turi buti paversta i bendra SANASTA event objekta.

## SANASTA event objektas

Kiekvienas ivykis turi tureti siuos laukus:

- event_id;
- source: Gmail, WhatsApp, Calendar, Trello, CRM, Monitoring, Invoice, Voice;
- received_at;
- client_name;
- client_contact;
- object_or_address;
- topic;
- message_summary;
- value_eur;
- risk_level: green, yellow, orange, red;
- priority: A, B, C;
- mode: AUTO, REVIEW, DECISION, NO_ACTION;
- next_action;
- responsible_person;
- deadline;
- linked_files;
- status;
- notes.

Jeigu dalies lauku truksta, agentas turi juos pazymeti kaip neaiskius, o ne fantazuoti.

## Pagrindinis informacijos kelias

1. Informacija ateina is kanalo.
2. Agentas ja perskaito / istraukia esme.
3. Informacija paverciama SANASTA event objektu.
4. Event gauna prioritetus ir rezima.
5. Event keliauja i tinkama stalciu.
6. Sukuriamas kitas veiksmas.
7. Jei reikia, sukuriamas laiskas, taskas, kalendoriaus irasas, CRM irasas arba follow-up.

## Kanalai

### Gmail

Gmail yra oficialus dokumentu, saskaitu, instituciju ir rimtesniu klientu komunikacijos kanalas.

Gmail eventai gali virsti:

- atsakymo juodrasciu;
- CRM klientu;
- Trello uzduotimi;
- kalendoriaus irasu;
- skolos priminimu;
- poirengimines instrukcijos tikrinimu;
- DECISION, jei yra kaina, terminas, atsakomybe, institucija ar konfliktas.

### WhatsApp

WhatsApp yra greitas klientu ir objektu komunikacijos kanalas.

WhatsApp eventai gali virsti:

- kliento klausimu;
- foto / video prie objekto;
- serviso uzduotimi;
- pasiulymo juodrasciu;
- kalendoriaus juodrasciu;
- follow-up;
- REVIEW atsakymo juodrasciu.

WhatsApp automatika negali pati siusti jautriu atsakymu apie kaina, garantija, atsakomybe, skolas ar terminus be Tomo patvirtinimo.

### Google Calendar

Calendar yra laiko sistema, ne objekto busenos sistema.

Calendar eventai turi rodyti:

- vizitus;
- montavimus;
- serviso laikus;
- follow-up priminimus;
- terminus;
- pasirengimo darbus.

Objekto busena turi gyventi CRM / Trello / Sheets, ne vien kalendoriuje.

### CRM / Sheets / HubSpot

CRM yra kliento ir objekto istorijos vieta.

CRM turi gauti:

- kliento duomenis;
- objekto adresa;
- statusa;
- next_action;
- paskutini kontakta;
- pasiulymo / saskaitos / darbo busena;
- follow-up data.

### Trello / uzduotys

Trello yra darbo vykdymo lenta.

Trello kortele kuriama, kai event turi realu veiksma:

- nuvaziuoti;
- paruosti pasiulyma;
- israsyti saskaita;
- surinkti medziagas;
- paskambinti;
- patikrinti garantija;
- uzdaryti objekta.

### Saskaitos

Saskaitos eventas turi tikrinti:

- kam issiusta;
- uz ka issiusta;
- ar apmoketa;
- ar reikia priminimo;
- ar kartu issiusta poirengimine instrukcija;
- ar objektas gali buti uzdaromas.

### Monitoringas

Monitoringas generuoja techninius ivykius:

- OK;
- Stebeti;
- Reikia kontakto;
- Reikia serviso;
- Avarine rizika;
- Komercine galimybe.

Monitoringas neturi kurti triuksmo. Jis turi sukurti tik realius eventus pagal rizikos zona.

## Rizikos rezimai

### AUTO

Galima atlikti automatiskai, jei nera kainos, termino, atsakomybes, konflikto ar teisinio jautrumo.

Pavyzdziai:

- gavimo patvirtinimas;
- neutralus priminimas;
- dokumentu prasymas;
- informacijos susisteminimas;
- uzduoties juodrastis.

### REVIEW

Agentas paruosa, Tomas patvirtina.

Naudoti, kai:

- tekstas aisku 80 procentu;
- reikia atsakymo, bet yra smulkiu neaiskumu;
- reikia pasiulymo juodrascio;
- reikia kliento zinutes, bet ne viskas patvirtinta.

### DECISION

Reikia Tomo sprendimo.

Naudoti, kai yra:

- kaina;
- nuolaida;
- atsakomybe;
- garantija;
- konfliktas;
- skola;
- institucija;
- terminas;
- didesnis objektas;
- partneryste.

### NO_ACTION

Nereikia veiksmo.

Naudoti, kai:

- reklama;
- spam;
- dubliuota informacija;
- informacija jau apdorota;
- istorinis triuksmas.

## Kaip sistemos turi kalbetis

### Pavyzdys: klientas parase WhatsApp del gedimo

1. WhatsApp zinute paverciama eventu.
2. Agentas nustato: klientas, objektas, problema, rizika.
3. Jei tai gedimas / pretenzija, rezimas REVIEW arba DECISION.
4. Sukuriamas Trello taskas.
5. Jei reikia vizito, ruosiamas Calendar irasas.
6. CRM atnaujinama kliento istorija.
7. Tomas gauna trumpa santrauka ir sprendima.

### Pavyzdys: issiusta saskaita

1. Gmail / saskaitos eventas aptinka saskaita.
2. CRM pazymi: saskaita issiusta.
3. Sukuriamas apmokejimo follow-up.
4. Tikrinama, ar issiusta poirengimine instrukcija.
5. Jei ne, ruosiamas instrukcijos laiskas.
6. Objektas tikrinamas pagal uzdarymo checklista.

### Pavyzdys: monitoringas rodo raudona rizika

1. Monitoringas sukuria eventa.
2. Risk_level = red.
3. Priority = A, jei klientui salta / karsta / gresia nuostolis.
4. Sukuriamas Trello taskas.
5. Paruosiamas kliento kontaktavimo tekstas.
6. Jei reikia, Calendar vizito juodrastis.

## Vienas tiesos saltinis

- Laikas gyvena Google Calendar.
- Kliento istorija gyvena CRM / Sheets / HubSpot.
- Vykdymas gyvena Trello / uzduotyse.
- Taisykles gyvena AGENTS.md ir docs/.
- Dokumentai / pasiulymai gyvena Drive arba repo pagal paskirti.
- Tomas sprendzia tik DECISION.

## Draudziama

- Laikyti objekto busena tik kalendoriuje.
- Siusti jautru WhatsApp / Gmail atsakyma be patvirtinimo.
- Kurti uzduoti be next_action.
- Kurti klienta be kontakto, jei kontaktas yra zinomas.
- Kurti nauja dokumentu vieta, jei tema telpa i 7 stalcius.
- Leisti, kad ta pati informacija gyventu 5 vietose be rysio.

## MVP integracijos prioritetas

1. Gmail -> event -> CRM/Trello/Calendar.
2. WhatsApp -> event -> REVIEW atsakymas / taskas.
3. Invoice -> event -> apmokejimo follow-up + poirengimine instrukcija.
4. Diktavimas -> event -> uzduotis / pasiulymas / kalendorius.
5. Monitoringas -> event -> rizikos zona / serviso uzduotis.

## Statusas

Sis dokumentas priklauso 01_SANASTA_OS, 02_GMAIL_RADARAS, 03_CRM_KLIENTAI, 04_MONITORINGAS ir 07_OPERACIJOS_DARBAI stalciams.

Pagrindine jo paskirtis: padaryti, kad visos SANASTA sistemos kalbetu viena event kalba ir Tomas nebutu rankinis tarpininkas tarp programu.
