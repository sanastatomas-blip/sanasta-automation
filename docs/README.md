# SANASTA docs indeksas

Sis aplankas skirtas pagalbinems SANASTA OS taisyklems ir projektiniams dokumentams.

Jeigu `AGENTS.md` yra pagrindines taisykles, tai `docs/` yra issamesni paaiskinimai, projektiniai modeliai ir darbo rezimai.

## Dokumentu sarasas

### `dictation_mode_rules.md`

Paskirtis: taisykles, kaip agentas turi elgtis, kai Tomas diktuoja telefone, autobuse, objekte arba chaotiskai.

Naudoti, kai:

- tekstas ne iki galo aiskus;
- uzduotis aisku apie 80 procentu;
- reikia paruosti juodrasti;
- truksta kainos, termino ar kitos esmines informacijos;
- neaisku, ar siusti, ar tik ruosti.

Pagrindine taisykle:

> Neaisku = nesiusti. Daryti juodrasti ir pazymeti, kas neaisku.

---

### `monitoring_scale_capacity.md`

Paskirtis: SANASTA monitoringo mastelio ir pajegumo modelis.

Naudoti, kai:

- kalbama apie monitoringo augima;
- reikia atsakyti, kaip aptarnauti 1000 klientu;
- reikia skaiciuoti, kiek zmoniu / techniku / koordinatoriu reikes;
- reikia projektuoti Basic / PRO / PRO+ logika;
- reikia ruosti atsakyma partneriui, investuotojui ar rimtam verslininkui.

Pagrindine taisykle:

> Pajeguma skaiciuojam ne pagal bendra klientu skaiciu, o pagal realiu ivykiu skaiciu.

---

### `post_install_client_instruction.md`

Paskirtis: taisykle ir sablonas, ka klientui siusti po irangos irengimo kartu su saskaita arba atskiru laisku.

Naudoti, kai:

- objektas sumontuotas / paleistas;
- klientui siunciama saskaita;
- reikia uzdaryti objekta komunikaciskai;
- reikia apsaugoti SANASTA nuo situacijos, kai klientas veliau sako, kad negavo prieziuros informacijos;
- reikia paaiskinti techninio aptarnavimo, naudojimo ir garantijos ribas.

Pagrindine taisykle:

> Saskaita viena pati objekto komunikaciskai neuzdaro. Su saskaita turi buti siunciama poirengimine instrukcija.

---

## Kaip kurti nauja docs dokumenta

Naujas dokumentas kuriamas tik tada, kai informacija:

- per ilga `AGENTS.md` failui;
- turi atskira paskirti;
- bus naudojama daugiau nei viena karta;
- priklauso vienam is 7 SANASTA stalciu.

Naujo dokumento formatas:

```text
# SANASTA [tema]

## Paskirtis

## Kada naudoti

## Pagrindines taisykles

## Draudziama

## Statusas
```

## Draudziama

- Kurti dokumenta be paskirties.
- Kurti dokumenta tik tam, kad nebutu reikia uzbaigti seno.
- Dubliuoti tas pacias taisykles keliose vietose be nuorodos.
- Naudoti pavadinimus `final`, `naujas`, `geras`, `testas`.

## Tvarkymo taisykles

Kiekvienas docs dokumentas turi tureti:

- aisku pavadinima;
- paskirti;
- kada naudoti;
- pagrindine taisykle;
- rysi su SANASTA_START_HERE.md.
