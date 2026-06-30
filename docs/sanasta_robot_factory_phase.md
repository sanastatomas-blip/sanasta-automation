# SANASTA robotu gamybos faze

## Paskirtis

Sis dokumentas uzfiksuoja nauja SANASTA automatikos etapa: pereinama nuo taisykliu rinkimo ir sistemos strukturos prie robotu gamybos.

Tikslas: SANASTA turi tureti ne viena chaotiska robota, o viena koordinuojama robotu sistema, kuri mazina Tomo rankini darba ir dirba pagal aiskias saugumo ribas.

## Kodel dabar

Anksciau robotai buvo per anksti, nes nebuvo aiskios sistemos:

- nebuvo 7 stalciu;
- nebuvo SANASTA event objekto;
- nebuvo AUTO / REVIEW / DECISION / NO_ACTION rezimu;
- nebuvo Tomo roles kaip tikrintojo, deleguotojo ir sprendimu priemejo;
- nebuvo vieno lango dashboardo logikos;
- nebuvo saugumo ribu jautriems klientu, kainos, garantijos ir atsakomybes klausimams.

Dabar pagrindas yra, todel galima pradeti robotu gamyba.

## Pagrindine formule

```text
Tomas kalba / gauna informacija
-> koordinatorius priskiria stalciu ir rezima
-> specializuotas robotas paruosia veiksma
-> Tomas patvirtina arba priima sprendima
-> sistema uzdaro / seka / primena
```

## Rekomenduojama robotu sistema

### 1. Koordinatorius

Atsakingas uz:

- informacijos priemima;
- stalciaus parinkima;
- prioriteto nustatyma;
- AUTO / REVIEW / DECISION / NO_ACTION rezima;
- perdavima specializuotam robotui;
- vieno lango dashboarda.

### 2. Komunikacijos robotas

Atsakingas uz:

- Gmail;
- WhatsApp;
- Messenger;
- klientu atsakymu juodrascius;
- SANASTA event kurima is zinuciu.

### 3. Operaciju robotas

Atsakingas uz:

- darbus;
- objektus;
- darbo pabaigos diktavima;
- ataskaitas;
- objekto istorija;
- uzdarymo checklista.

### 4. Pinigu robotas

Atsakingas uz:

- saskaitas;
- apmokejimus;
- poirengimines instrukcijas;
- follow-up;
- skolu priminimus;
- ar objektas gali buti uzdarytas.

### 5. Marketingo robotas

Atsakingas uz:

- Facebook;
- LinkedIn;
- Reels scenarijus;
- BNI turini;
- SANASTA inzinerinio pasitikejimo stiliu;
- AUTO / REVIEW / DECISION turinio filtra.

### 6. CRM robotas

Atsakingas uz:

- klientu statusus;
- HubSpot / CRM laukus;
- follow-up;
- pasiulymu busena;
- metini aptarnavima;
- atsiliepimu prasymus.

### 7. Ryto / nakties radaras

Atsakingas uz:

- ryto vieno lango paruosima;
- naktini marketingo paruosima;
- uzstrigusiu darbu radima;
- prioritetu atranka;
- kasdienio valdymo santrauka.

## Paleidimo eile

### MVP etapas

Pradeti ne nuo visu 7 robotu, o nuo vieno koordinatoriaus ir 3 moduliu:

1. Komunikacija: Voice / WhatsApp / Gmail.
2. Operacijos: darbo pabaiga / ataskaita / uzdarymas.
3. Marketingas: Facebook naktinis turinio ruosimas.

### Stabilus etapas

Prijungti:

4. Pinigu robota.
5. Ryto / nakties radara.

### Pilna SANASTA OS

Prijungti:

6. CRM robota.
7. Monitoringa / PRO prieziuros logika.

## Saugumo taisykle

Jeigu veiksmas susijes su kaina, nuolaida, garantija, atsakomybe, konfliktu, skola, institucija arba terminu, robotas negali veikti be Tomo.

Rezimai:

```text
AUTO: galima atlikti be Tomo tik mazos rizikos veiksmus.
REVIEW: robotas paruosia, Tomas patvirtina.
DECISION: reikia Tomo sprendimo.
NO_ACTION: archyvuoti arba nieko nedaryti.
```

## Statusas

Sis dokumentas priklauso 01_SANASTA_OS stalciui.

Prioritetas: A. Tai naujas etapas: nuo sistemos taisykliu pereinama prie robotu gamybos ir MVP paleidimo.
