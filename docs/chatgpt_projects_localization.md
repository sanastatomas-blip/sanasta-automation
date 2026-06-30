# SANASTA ChatGPT projektu ir pokalbiu lokalizavimo taisykles

## Paskirtis

Sis dokumentas skirtas sutvarkyti ChatGPT atidarytus projektus ir pokalbius taip, kad jie nebutu padrika istorija, o turetu aiskia vieta SANASTA sistemoje.

Tikslas: kiekvienas ChatGPT projektas arba pokalbis turi buti lokalizuotas i viena is 7 SANASTA stalciu, tureti statusa ir kita veiksma.

## Pagrindine taisykle

ChatGPT pokalbis nera sistema, kol jis neturi:

- stalciaus;
- temos;
- statuso;
- kito veiksmo;
- sprendimo, ar jis aktyvus, ar archyvas.

## 7 lokalizavimo stalciai

Kiekvienas ChatGPT projektas / pokalbis turi buti priskirtas vienam pagrindiniam stalciui:

1. 01_SANASTA_OS
2. 02_GMAIL_RADARAS / KOMUNIKACIJOS_RADARAS
3. 03_CRM_KLIENTAI
4. 04_MONITORINGAS
5. 05_KOMERCINIAI_PASIULYMAI
6. 06_MARKETINGAS_POSTAI
7. 07_OPERACIJOS_DARBAI

Jeigu pokalbis tinka keliems stalciams, pasirinkti pagrindini ir pazymeti antrini.

## Naujas pavadinimu formatas

ChatGPT projektus ir pokalbius pervadinti pagal formata:

SANASTA_[STALCIUS]_[TEMA]_[STATUSAS]

Pavyzdziai:

- SANASTA_OS_Codex_taisykles_AKTYVU
- SANASTA_KOMUNIKACIJOS_WhatsApp_Tasker_AI_AKTYVU
- SANASTA_GMAIL_Radaras_laisku_tvarkymas_AKTYVU
- SANASTA_MONITORINGAS_1000_klientu_modelis_AKTYVU
- SANASTA_KOMERCINIAI_PASIULYMAI_sablonai_AKTYVU
- SANASTA_MARKETINGAS_postu_idejos_ARCHYVAS
- SANASTA_OPERACIJOS_darbu_planavimas_AKTYVU

## Statusai

Naudoti tik siuos statusus:

- AKTYVU - naudojama dabar;
- LAUKIA - reikes veliau, bet ne siandien;
- ARCHYVAS - saugoma, bet nenaudojama;
- SUJUNGTI - dubliuoja kita projekta / pokalbi;
- ISTRINTI - nera vertes, tik siuksle.

## Ka daryti su esamais ChatGPT projektais

Kiekvienam projektui atlikti mini inventorizacija:

```text
Dabartinis pavadinimas:
Apie ka:
Stalcius:
Statusas:
Ar dubliuoja kita projekta:
Ka is jo reikia issaugoti:
Kitas veiksmas:
```

## Lokalizavimo procesas

1. Atidaryti projekta / pokalbi.
2. Perziureti tema ir paskirti.
3. Priskirti viena is 7 stalciu.
4. Pervadinti pagal pavadinimu taisykle.
5. Jei yra naudingu taisykliu, perkelti i GitHub docs arba AGENTS.md.
6. Jei yra veiksmu, sukurti taska / next_action.
7. Jei dubliuoja kita pokalbi, pazymeti SUJUNGTI.
8. Jei nebereikalinga, pazymeti ARCHYVAS arba ISTRINTI.

## Pokalbiu tipai

### Taisykliu pokalbiai

Keliauja i 01_SANASTA_OS.

Pavyzdziai:

- prioritetai;
- delegavimas;
- diktavimo rezimas;
- atsakomybe / garantija;
- objekto uzdarymas;
- vieno lango logika.

Jeigu taisykle svarbi, ji turi buti perkelta i AGENTS.md arba docs/.

### Komunikacijos pokalbiai

Keliauja i 02_GMAIL_RADARAS / KOMUNIKACIJOS_RADARAS.

Pavyzdziai:

- Gmail radaras;
- WhatsApp automatizacija;
- Tasker;
- laisku atsakymai;
- klientu follow-up;
- siustinos instrukcijos.

### Klientu / CRM pokalbiai

Keliauja i 03_CRM_KLIENTAI.

Pavyzdziai:

- konkretus klientai;
- objektai;
- kontaktai;
- HubSpot;
- follow-up;
- atsiliepimai.

### Monitoringo pokalbiai

Keliauja i 04_MONITORINGAS.

Pavyzdziai:

- Panasonic;
- PRO / PRO+;
- 1000 klientu modelis;
- capacity;
- signalai;
- serviso radaras.

### Pasiulymu pokalbiai

Keliauja i 05_KOMERCINIAI_PASIULYMAI.

Pavyzdziai:

- kainodara;
- komerciniai pasiulymai;
- PDF;
- klientu pasiulymai;
- filtrai;
- kondicionieriai;
- silumos siurbliai.

### Marketingo pokalbiai

Keliauja i 06_MARKETINGAS_POSTAI.

Pavyzdziai:

- postai;
- LinkedIn;
- Facebook;
- TikTok;
- BNI;
- pristatymai;
- reklaminiai tekstai.

### Operaciju pokalbiai

Keliauja i 07_OPERACIJOS_DARBAI.

Pavyzdziai:

- montavimai;
- servisai;
- medziagos;
- kalendorius;
- Trello;
- kasdieniai darbai;
- technines situacijos.

## Ka draudziama daryti

- Palikti pokalbi be stalciaus.
- Kurti nauja projekta, jei tema telpa i esama stalciu.
- Naudoti pavadinimus „testas“, „naujas“, „sitas“, „geras“, „final“.
- Laikyti svarbia taisykle tik pokalbyje, jei ji reikalinga ateityje.
- Dubliuoti ta pacia tema 5 projektuose.

## Minimalus vieno pokalbio sutvarkymo rezultatas

Po sutvarkymo turi buti aisku:

- kur pokalbis priklauso;
- ar jis aktyvus;
- ka is jo issaugoti;
- ar reikia perkelti i GitHub;
- koks kitas veiksmas.

## Pirma tvarkymo eile

Pirma lokalizuoti siuos ChatGPT projektus / temas:

1. Codex / SANASTA OS.
2. Gmail radaras.
3. WhatsApp / Tasker / AI komunikacija.
4. Monitoringas.
5. Komerciniai pasiulymai.
6. Marketingo postai.
7. Operacijos / darbai.

## Statusas

Sis dokumentas priklauso 01_SANASTA_OS ir 02_GMAIL_RADARAS / KOMUNIKACIJOS_RADARAS stalciams.

Jo paskirtis: sutvarkyti ChatGPT viduje esancius projektus ir pokalbius, kad jie taptu SANASTA sistemos dalimi, o ne atskira netvarka.
