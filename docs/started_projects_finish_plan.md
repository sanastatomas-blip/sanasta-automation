# SANASTA pradetu projektu uzbaigimo planas

## Paskirtis

Sis dokumentas skirtas uzrakinti vakar sutarta principa: baigiame pradetus projektus, o ne atidarome dar daugiau frontu.

Tikslas: visi pradeti, bet nebaigti SANASTA / ChatGPT / Codex / automatizacijos projektai turi tureti aisku uzbaigimo plana, prioritetu eile ir kita veiksma.

## Pagrindine taisykle

Naujas projektas nepradedamas, kol seni projektai neturi:

- stalciaus;
- statuso;
- uzbaigimo kriterijaus;
- kito veiksmo;
- atsakingo vykdytojo;
- sprendimo, ar tai aktyvu, laukia, archyvas, sujungti ar istrinti.

Tomas turi likti tikrintojas, deleguotojas ir sprendimu priemejas.

## Projekto uzbaigimo kriterijus

Projektas laikomas uzbaigtu, kai:

- taisykles perkeltos i `AGENTS.md` arba `docs/`;
- praktinis veiksmas suformuotas kaip GitHub issue / taskas / checklistas;
- yra aiskus MVP arba sprendimas, kad projektas archyvuojamas;
- nebera „kazkur buvo pokalbis“;
- Tomas mato, ka daryti toliau.

## 0 etapas: inventorizacija

Naudojami dokumentai:

- `SANASTA_START_HERE.md`
- `README_START_HERE.md`
- `AGENTS.md`
- `docs/README.md`
- `docs/chatgpt_projects_inventory.md`
- `docs/chatgpt_projects_localization.md`
- `docs/codex_operations_automation_backlog.md`

Veiksmai:

1. Visi ChatGPT projektai ir pokalbiai priskiriami 7 stalciams.
2. Kiekvienam suteikiamas statusas: AKTYVU, LAUKIA, ARCHYVAS, SUJUNGTI, ISTRINTI.
3. Kiekvienam aktyviam projektui priskiriamas next_action.
4. Dubliuojantys projektai pazymimi SUJUNGTI.
5. Nevertingi projektai keliauja i ARCHYVAS arba ISTRINTI.

## Uzbaigimo eile

### 1 projektas: SANASTA OS / Codex taisykles

**Stalcius:** 01_SANASTA_OS  
**Statusas:** AKTYVU  
**Svarba:** A/B  
**Tikslas:** baigti pagrindine operacines sistemos struktura.

Kas jau padaryta:

- `AGENTS.md` turi pagrindines taisykles;
- `SANASTA_START_HERE.md` sukurtas;
- `README_START_HERE.md` sukurtas;
- `docs/README.md` sukurtas;
- 7 stalciu struktura uzrakinta;
- Tomo vaidmuo: tikrintojas / deleguotojas / sprendimu priemejas uzfiksuotas.

Kas liko:

- patikrinti, ar `docs/README.md` rodo visus naujus dokumentus;
- patikrinti, ar `README_START_HERE.md` turi visas svarbiausias nuorodas;
- sujungti dubliuojancias taisykles;
- sukurti viena „kur pradeti“ kelia Codexui.

Uzbaigimo kriterijus:

- Tomas atsidaro viena starto faila ir supranta, kur viskas gyvena.

Kitas veiksmas:

- atnaujinti `docs/README.md` ir `README_START_HERE.md` su naujais dokumentais.

---

### 2 projektas: Vieno lango dashboardas

**Stalcius:** 01_SANASTA_OS + 07_OPERACIJOS_DARBAI  
**Statusas:** AKTYVU  
**Svarba:** A/B  
**Tikslas:** Tomas neturi ieskoti tarp 13 ivykiu.

Kas jau padaryta:

- sukurtas `docs/sanasta_one_window_dashboard.md`;
- uzrakinti 5 blokai:
  - Siandien dega;
  - Reikia Tomo sprendimo;
  - Deleguota robotui;
  - Laukia kliento / apmokejimo;
  - Siandien uzdaryti.

Kas liko:

- padaryti praktini duomenu formata;
- susieti su SANASTA event objektu;
- sukurti GitHub issue Codexui del prototipo;
- nuspresti, ar pirmas vaizdas bus Markdown / Sheets / paprastas web / Trello vaizdas.

Uzbaigimo kriterijus:

- vienas langas rodo 3 degancius, 3 sprendimus, 3 laukimus ir 3 uzdarymus.

Kitas veiksmas:

- Codexui duoti MVP: sugeneruoti vieno lango dashboarda is eventu saraso.

---

### 3 projektas: WhatsApp / vairavimo rezimas / Voice -> klientui tekstas

**Stalcius:** 02_KOMUNIKACIJOS_RADARAS + 07_OPERACIJOS_DARBAI  
**Statusas:** AKTYVU  
**Svarba:** A  
**Tikslas:** Tomas vairuoja, robotas dirba.

Kas jau padaryta:

- sukurtas `docs/whatsapp_android_ai_tasker_setup.md`;
- sukurtas `docs/sanasta_driving_mode.md`;
- GitHub issue #1 sukurtas: `MVP: Voice fact -> WhatsApp client draft -> SANASTA event`;
- pavyzdinis kondensato zarnos atvejis paruostas kaip test case.

Kas liko:

- Codex turi sukurti maza prototipa;
- input: Tomo diktavimas;
- output: WhatsApp juodrastis + SANASTA event;
- jokio automatinio siuntimo be Tomo patvirtinimo;
- jautrius atvejus zymeti REVIEW / DECISION.

Uzbaigimo kriterijus:

- Tomas padiktuoja viena fakta ir gauna paruosta WhatsApp teksta + eventa.

Kitas veiksmas:

- vykdyti GitHub issue #1.

---

### 4 projektas: Gmail / komunikacijos radaras

**Stalcius:** 02_GMAIL_RADARAS / KOMUNIKACIJOS_RADARAS  
**Statusas:** AKTYVU  
**Svarba:** A  
**Tikslas:** laiskai turi buti ne tik atrenkami, bet ir atsakomi per juodrascius.

Kas jau padaryta:

- atsakymu rezimai AUTO / REVIEW / DECISION / NO_ACTION uzrakinti;
- Gmail turi veikti kartu su Calendar;
- neutralus laiskai gali buti ruosiami / siunciami pagal taisykles;
- jautrus laiskai eina i REVIEW / DECISION.

Kas liko:

- sukurti praktini laisku klasifikavimo MVP;
- istraukti klienta, objekta, suma, termina, rizika, next_action;
- ruosti atsakymo juodrasti;
- aptikti saskaitas;
- susieti su poirengimine instrukcija ir apmokejimo follow-up.

Uzbaigimo kriterijus:

- Gmail laiskas pavirsta eventu, juodrasciu ir next_action.

Kitas veiksmas:

- sukurti GitHub issue: Gmail -> SANASTA event -> draft -> follow-up.

---

### 5 projektas: Saskaita -> poirengimine instrukcija -> apmokejimo follow-up

**Stalcius:** 05_KOMERCINIAI_PASIULYMAI + 07_OPERACIJOS_DARBAI  
**Statusas:** AKTYVU  
**Svarba:** A  
**Tikslas:** saugoti pinigus, garantine rizika ir objekto uzdaryma.

Kas jau padaryta:

- sukurtas `docs/post_install_client_instruction.md`;
- uzrakinta, kad saskaita viena pati objekto komunikaciskai neuzdaro;
- kondensato zarnos realus atvejis itrauktas;
- metinio aptarnavimo ir garantines rizikos logika pradzioje sutvarkyta.

Kas liko:

- sukurti automatini tikrinima: issiusta saskaita -> ar issiusta instrukcija;
- jei ne, paruosiamas laiskas;
- sukuriamas apmokejimo follow-up;
- objektas tikrinamas pagal uzdarymo checklista.

Uzbaigimo kriterijus:

- kiekviena saskaita sukuria instrukcijos patikrinima ir apmokejimo follow-up.

Kitas veiksmas:

- sukurti GitHub issue: Invoice -> instruction -> payment follow-up.

---

### 6 projektas: Darbo pabaigos diktavimas -> ataskaita -> saskaitos eilutes -> uzdarymas

**Stalcius:** 07_OPERACIJOS_DARBAI  
**Statusas:** AKTYVU  
**Svarba:** A/B  
**Tikslas:** po darbo Tomas padiktuoja, sistema sutvarko dokumentacija.

Kas jau padaryta:

- darbo korteles / event logika apibrezta;
- Tomo vaidmuo uzrakintas;
- vairavimo rezimas ir WhatsApp juodrasciai susieti.

Kas liko:

- sukurti MVP:
  - input: darbo pabaigos diktavimas;
  - output: darbo ataskaita;
  - output: klientui zinute;
  - output: saskaitos eilutes;
  - output: objekto uzdarymo checklistas.

Uzbaigimo kriterijus:

- vienas diktavimas sukuria visus darbo pabaigos dokumentus.

Kitas veiksmas:

- sukurti GitHub issue: Work completion voice -> report/invoice lines/closeout.

---

### 7 projektas: ChatGPT projektu lokalizavimas

**Stalcius:** 01_SANASTA_OS  
**Statusas:** AKTYVU  
**Svarba:** B  
**Tikslas:** visi ChatGPT pokalbiai turi vieta, statusa ir next_action.

Kas jau padaryta:

- sukurtas `docs/chatgpt_projects_localization.md`;
- sukurtas `docs/chatgpt_projects_inventory.md`;
- pradeta inventorizacijos lentele.

Kas liko:

- Tomas turi parodyti / pateikti likusiu projektu pavadinimus;
- kiekvienam priskirti stalciu;
- dublius pazymeti SUJUNGTI;
- nereikalingus pazymeti ARCHYVAS / ISTRINTI.

Uzbaigimo kriterijus:

- visi ChatGPT projektai pervadinti arba bent suinventorizuoti.

Kitas veiksmas:

- kai Tomas rodo ekrana, pildyti `docs/chatgpt_projects_inventory.md`.

---

### 8 projektas: Monitoringas / PRO / 1000 klientu modelis

**Stalcius:** 04_MONITORINGAS  
**Statusas:** AKTYVU, bet ne siandieninis gesinimas  
**Svarba:** B strateginis  
**Tikslas:** monitoringas turi skaluotis be Tomo rankinio ziurejimo i visus klientus.

Kas jau padaryta:

- sukurtas `docs/monitoring_scale_capacity.md`;
- uzrakinta formule: `1000 klientu -> 20 ivykiu -> 5 prioritetai -> 3 Tomo sprendimai`;
- rizikos zonos apibreztos.

Kas liko:

- susieti monitoringo eventus su vieno lango dashboardu;
- sudaryti Basic / PRO / PRO+ kliento statuso modeli;
- rinkti capacity skaicius.

Uzbaigimo kriterijus:

- monitoringas generuoja ne triuksma, o eventus pagal rizika.

Kitas veiksmas:

- kol kas laikyti B strateginiu; nepertraukti A projektu.

---

### 9 projektas: Komerciniai pasiulymai

**Stalcius:** 05_KOMERCINIAI_PASIULYMAI  
**Statusas:** AKTYVU  
**Svarba:** B/A pagal klienta  
**Tikslas:** pasiulymai turi buti ruosiami is sablonu, o Tomas tvirtina kaina.

Kas jau padaryta:

- psichologine kryptis uzrakinta: klientas perka ne iranga, o ramybe, atsakomybe ir viena kontakta;
- SANASTA pasiulymu verte apibrezta;
- poirengimine instrukcija susieta su pasiulymais.

Kas liko:

- sukurti sablonus pagal tipu: kondicionierius, silumos siurblys, vedinimas, filtrai, servisas, monitoringas;
- susieti pasiulyma su follow-up;
- pasiulyma po issiuntimo paversti CRM statusu.

Uzbaigimo kriterijus:

- pasiulymo juodrastis is diktavimo / laisko + follow-up.

Kitas veiksmas:

- po A projektu grizti prie sablonu bibliotekos.

---

### 10 projektas: Marketingo postai / BNI / socialiniai

**Stalcius:** 06_MARKETINGAS_POSTAI  
**Statusas:** LAUKIA  
**Svarba:** B/C siuo momentu  
**Tikslas:** realius techninius atvejus paversti turiniu, bet nepertraukti operaciju.

Kas jau padaryta:

- turinio kryptys zinomos;
- techniniu atveju -> postas ideja uzfiksuota.

Kas liko:

- sukurti postu lentele;
- sudeti temas;
- nustatyti datas;
- naudoti realius atvejus.

Uzbaigimo kriterijus:

- postai turi lentele, statusa ir data.

Kitas veiksmas:

- palikti LAUKIA, kol uzdaromi A projektai.

---

### 11 projektas: Facebook / Messenger automatika

**Stalcius:** 06_MARKETINGAS_POSTAI + 03_CRM_KLIENTAI  
**Statusas:** LAUKIA / SUJUNGTI  
**Svarba:** B/C  
**Tikslas:** postas -> komentaras -> DM -> forma -> follow-up.

Kas jau zinoma:

- ankstesnis projektas buvo pradetasis FB darbas;
- nebaigta: postas -> komentaras -> DM -> bot -> Google Sheet / HubSpot -> follow-up;
- reikia nuspresti, ar naudoti profili, ar puslapi;
- reikia ijungti Messenger flow.

Kas liko:

- sujungti su Komunikacijos radaru ir CRM;
- nekurti atskiro chaoso.

Uzbaigimo kriterijus:

- vienas testinis FB / Messenger srautas.

Kitas veiksmas:

- laikyti LAUKIA; nejudinti iki Gmail / WhatsApp MVP.

---

### 12 projektas: HubSpot / CRM

**Stalcius:** 03_CRM_KLIENTAI  
**Statusas:** AKTYVU, bet priklauso nuo eventu logikos  
**Svarba:** B strateginis  
**Tikslas:** klientas neturi dingti be statuso ir next_action.

Kas jau zinoma:

- HubSpot pasirinktas kaip tinkama kryptis;
- minimalus kontaktai: email, vardas, pavarde, telefonas, legal basis;
- reikia klientu pipeline ir follow-up.

Kas liko:

- susieti su SANASTA event objektu;
- sukurti statusus: naujas, laukia atsakymo, pasiulymas issiustas, darbai suplanuoti, atlikta, saskaita issiusta, apmoketa, uzdaryta.

Uzbaigimo kriterijus:

- kiekvienas klientas turi statusa ir next_action.

Kitas veiksmas:

- po Gmail / WhatsApp MVP susieti eventus su CRM.

## Pirmas 7 dienu uzbaigimo planas

### Diena 1: OS indeksai

- atnaujinti `README_START_HERE.md`;
- atnaujinti `docs/README.md`;
- itraukti visus naujus dokumentus;
- patikrinti, kad startas aiskus.

### Diena 2: WhatsApp / Voice MVP

- vykdyti issue #1;
- padaryti viena veikianti input -> WhatsApp draft -> event pavyzdi;
- testuoti su kondensato zarnos atveju.

### Diena 3: Saskaita -> instrukcija -> follow-up

- sukurti issue;
- apibrezti inputus ir outputus;
- padaryti pirmo srauto prototipa.

### Diena 4: Gmail event MVP

- sukurti issue;
- laiskas -> event -> draft -> next_action;
- mode AUTO / REVIEW / DECISION.

### Diena 5: Darbo pabaigos diktavimas

- sukurti issue;
- input -> ataskaita -> klientui zinute -> saskaitos eilutes -> uzdarymo checklistas.

### Diena 6: Vieno lango dashboardas

- sukurti issue;
- eventai -> 5 blokai;
- rodyti tik svarbiausia.

### Diena 7: Inventorizacijos uzdarymas

- perziureti ChatGPT projektus;
- atnaujinti `docs/chatgpt_projects_inventory.md`;
- pazymeti SUJUNGTI / ARCHYVAS / ISTRINTI.

## Stop taisykle

Kol nebaigti pirmi 6 projektai, nauji projektai tik registruojami i C arba LAUKIA.

Naujas frontas leidziamas tik jei:

- jis tiesiogiai duoda pinigus dabar;
- gesina rizika;
- susijes su klientu siandien / rytoj;
- arba uzbaigia viena is pradetu projektu.

## Dienos valdymas

Kiekviena diena sistema turi pateikti tik:

1. 3 svarbiausi uzdarymai;
2. 3 Tomo sprendimai;
3. 3 robotui deleguoti veiksmai;
4. kas laukia pinigu;
5. kas nejudinama siandien.

Maziau triuksmo. Daugiau uzdarymo.
