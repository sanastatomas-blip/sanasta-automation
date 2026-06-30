# SANASTA Codex operaciju automatizavimo backlogas

## Paskirtis

Sis dokumentas skirtas Codex darbo krypciai: automatizuoti SANASTA operacijas taip, kad Tomas kuo maziau sedetu prie kompiuterio.

Tikslas: Tomas turi valdyti versla per trumpas komandas, telefona, balso diktavima ir sprendimus, o ne per rankini laisku, lenteliu, kalendoriaus, saskaitu ir priminimu tampyma.

## Pagrindine taisykle

Kiekviena automatizacija turi mazinti viena is siu dalyku:

- Tomo laika prie kompiuterio;
- rankini informacijos kopijavima;
- pamestu klientu skaiciu;
- veluojancius follow-up;
- neisrasytas / neapmoketas saskaitas;
- neuzdarytus objektus;
- rizika, kad klientas sakys „negavau informacijos“.

Jeigu funkcija to nemazina, ji nera prioritetas.

## Automatikos kryptys pagal 7 stalcius

### 01_SANASTA_OS

Tikslas: visi procesai turi buti randami per viena navigacija.

Codex darbai:

- sukurti pagrindini OS indeksavima;
- uztikrinti, kad `AGENTS.md`, `SANASTA_START_HERE.md`, `README_START_HERE.md` ir `docs/README.md` butu nuoseklus;
- padaryti taisykle: naujas dokumentas negali atsirasti be paskirties ir stalciaus;
- sukurti paprasta komanda / checklista „kur sita deti?“;
- sukurti `ARCHYVAS_NELIESTI_2026` logika senoms idejoms ir failams.

### 02_GMAIL_RADARAS

Tikslas: Tomas neturi rankomis skaityti ir rusiuoti kiekvieno laisko.

Codex darbai:

- automatiskai klasifikuoti laiskus i AUTO / REVIEW / DECISION / NO_ACTION;
- istraukti klienta, objekta, suma, termina, rizika ir kita veiksma;
- ruosti atsakymu juodrascius;
- zymeti laiskus pagal busena;
- aptikti siustas saskaitas;
- po saskaitos tikrinti, ar klientui issiusta poirengimine instrukcija;
- daryti follow-up, jei klientas neatsake;
- daryti skolu priminimu juodrascius;
- isskirti instituciju / teisinius / rizikos laiskus i DECISION.

### 03_CRM_KLIENTAI

Tikslas: nei vienas klientas neturi dingti be statuso ir kito veiksmo.

Codex darbai:

- is laisku ir pokalbiu kurti klientu / objektu korteles;
- kiekvienam klientui priskirti next_action;
- zymeti statusa: naujas, laukiama atsakymo, pasiulymas issiustas, darbai suplanuoti, atlikta, saskaita issiusta, apmoketa, uzdaryta;
- automatiskai kurti follow-up datas;
- tikrinti, kurie klientai laukia per ilgai;
- daryti dienos 3 svarbiausiu klientu sarasa;
- atskirti aktyvius klientus nuo archyvo.

### 04_MONITORINGAS

Tikslas: monitoringas turi skaluotis be Tomo rankinio ziurejimo i visus klientus.

Codex darbai:

- ruosti monitoringo klientu statusu modeli;
- susieti klienta, irengini, plana, garantija ir serviso istorija;
- kurti rizikos zonas: zalia, geltona, oranzine, raudona;
- skaiciuoti, kurie klientai reikalauja zmogaus sprendimo;
- kaupti ivykiu statistika capacity modeliui;
- ruosti metinio aptarnavimo pasiulymus;
- ruosti PRO / PRO+ upsell sarasa;
- ruosti serviso komandos poreikio skaiciavima.

### 05_KOMERCINIAI_PASIULYMAI

Tikslas: pasiulymai turi buti paruosiami is sablono, o Tomas tik patvirtina kaina / sprendima.

Codex darbai:

- sukurti pasiulymo sablonu biblioteka;
- atskirti pasiulymus pagal tipa: kondicionierius, silumos siurblys, vedinimas, filtrai, servisas, monitoringas;
- automatiskai istraukti kliento poreiki is laisko / diktavimo;
- paruosti pasiulymo juodrasti be kainos, jei kaina neaiski;
- pazymeti, kur reikia Tomo sprendimo;
- prideti psichologine SANASTA verte: „kad po montavimo nereiketu ieskoti kaltu“;
- po pasiulymo issiuntimo sukurti follow-up.

### 06_MARKETINGAS_POSTAI

Tikslas: postai neturi gyventi pokalbiuose. Jie turi tureti tema, statusa ir data.

Codex darbai:

- is pokalbiu ir objektu generuoti postu idejas;
- sukurti postu lentele su statusais;
- zymeti kanalus: LinkedIn, Facebook, TikTok, BNI;
- daryti turinio kalendoriu;
- techninius atvejus paversti klientui suprantamais postais;
- paruosti postu juodrascius;
- nesiusti / neskelbti be Tomo patvirtinimo.

### 07_OPERACIJOS_DARBAI

Tikslas: objektai, servisai ir medziagos turi judeti be Tomo rankinio gaudymo.

Codex darbai:

- is diktavimo sukurti darbo kortele;
- kiekvienam darbui priskirti klienta, objekta, termina, atsakinga, medziagas, kita veiksma;
- paruosti medziagu sarasa;
- sukurti kalendoriaus iraso juodrasti;
- po darbo priminti apie nuotraukas, dokumentus, saskaita ir poirengimine instrukcija;
- tikrinti, ar objektas tikrai uzdarytas;
- atskirti apmoketa / neapmoketa / laukiama apmokejimo;
- daryti dienos 3 uzdarymu sarasa.

## Prioritetinis MVP

Pirmi 5 darbai, kuriuos Codex turetu automatizuoti:

1. Gmail -> uzduotis / klientas / next_action istraukimas.
2. Issiusta saskaita -> tikrinti, ar issiusta poirengimine instrukcija.
3. Diktavimas -> tvarkingas darbo / kliento / pasiulymo juodrastis.
4. Pasiulymas issiustas -> automatinis follow-up priminimas.
5. Darbas atliktas -> objekto uzdarymo checklistas.

## Tomo darbo mazininimo principas

Tomas neturi daryti:

- kopijuoti informacijos tarp Gmail, Trello, Sheets ir Calendar;
- ieskoti, kam reikia atsakyti;
- prisiminti, kam issiusta saskaita;
- rankomis gaudyti follow-up;
- rankomis rasyti kartotinius laiskus;
- ieskoti, ar klientui buvo paaiskinta prieziura;
- galvoti, kur padeti nauja ideja.

Tomas turi daryti:

- priimti sprendimus del kainos;
- patvirtinti nuolaidas;
- spresti konfliktus;
- tvirtinti garantijos / atsakomybes ribas;
- tvirtinti didelius objektus;
- duoti krypti.

## Komandu modelis

Tomas turi galeti rasyti trumpai:

- „deleguoti“;
- „paruoskti laiska“;
- „padaryk pasiulyma“;
- „itraukti i kalendoriu“;
- „sukurti taska“;
- „patikrinti skolas“;
- „kas laukia?“;
- „kas dega?“;
- „ka siandien uzdaryti?“

Agentas turi suprasti, i kuri stalciu tai keliauja ir kokio veiksmo reikia.

## Darbo režimai

- AUTO: paprasti mazos rizikos veiksmai.
- REVIEW: juodrastis Tomui.
- DECISION: reikia Tomo sprendimo.
- NO_ACTION: archyvuoti / nieko nedaryti.

## Statusas

Sis dokumentas yra B prioritetas. Jis skirtas Codex darbo planui ir SANASTA operaciju automatizavimo krypciai.
