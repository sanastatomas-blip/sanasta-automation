# SANASTA komandinė robotų sistema

## Paskirtis

Šis dokumentas užfiksuoja svarbų principą: SANASTA robotai turi dirbti ne tik Tomui, bet visai įmonei ir visai darbo grandinei.

Tikslas: Tomas neturi būti vienintelis žmogus, per kurį eina visa informacija, klientai, darbai, sąskaitos, marketingas, CRM ir sprendimai.

## Pagrindinė taisyklė

Robotai turi aptarnauti visą SANASTA sistemą:

- Tomą;
- technikus;
- subrangovus;
- klientus;
- buhalteriją;
- CRM;
- kalendorių;
- Gmail;
- WhatsApp;
- Facebook;
- LinkedIn;
- monitoringą;
- komercinius pasiūlymus;
- darbų uždarymą.

## Ne tik Tomo asistentas

Blogas modelis:

```text
Visi rašo Tomui -> Tomas aiškinasi -> Tomas perduoda -> Tomas primena -> Tomas uždaro
```

Teisingas modelis:

```text
Informacija patenka į sistemą
-> robotas sukuria eventą
-> priskiria atsakingą žmogų / robotą
-> paruošia veiksmą
-> Tomas gauna tik sprendimus ir patvirtinimus
```

## Kam robotai turi padėti

### Tomui

- ryto langas;
- sprendimai;
- klientų atsakymai;
- kainos / garantijos / atsakomybės klausimai;
- darbų uždarymas;
- marketingo kryptis.

### Technikui / subrangovui

- ką padaryti;
- kur važiuoti;
- ką pasiimti;
- ką nufotografuoti;
- ką pranešti po darbo;
- kada skambinti Tomui.

### Klientui

- aiškus atsakymas;
- statusas;
- instrukcija po darbo;
- priminimas dėl aptarnavimo;
- aiški komunikacija be chaoso.

### Buhalterijai / pinigams

- ar darbas atliktas;
- ar reikia sąskaitos;
- ar sąskaita išsiųsta;
- ar apmokėta;
- ar reikia priminimo;
- ar objektas gali būti uždarytas.

### Marketingui

- kasdienis Facebook turinys;
- LinkedIn ekspertinis turinys;
- realių atvejų pavertimas edukacija;
- Reels scenarijai;
- BNI temos;
- SANASTA inžinerinio pasitikėjimo stilius.

### CRM

- naujas klientas;
- statusas;
- pasiūlymo etapas;
- follow-up;
- metinis aptarnavimas;
- atsiliepimo prašymas.

## Sistemos centras

Visų robotų centras turi būti SANASTA event objektas.

Kiekvienas įvykis turi turėti:

- source;
- client_name;
- object_or_address;
- topic;
- message_summary;
- value_eur;
- risk_level;
- priority;
- mode;
- next_action;
- responsible_person;
- deadline;
- status.

## Atsakingo priskyrimas

Kiekvienas eventas turi atsakyti į klausimą:

```text
Kas turi daryti kitą veiksmą?
```

Galimi atsakingi:

- Tomas;
- robotas;
- technikas;
- subrangovas;
- buhalterija;
- klientas;
- tiekėjas;
- laukia atsakymo.

## Vieno lango tikslas

Tomas neturi matyti visų įvykių. Tomas turi matyti tik:

1. kas dega;
2. kur reikia Tomo sprendimo;
3. kas deleguota;
4. kur laukia pinigai;
5. ką šiandien uždaryti.

## Komandinis efektas

Robotų sistema turi padaryti taip, kad SANASTA veiktų net tada, kai Tomas:

- objekte;
- vairuoja;
- kalba su klientu;
- miega;
- neturi laiko rašyti;
- nenori kapstytis po 700 laiškų.

## Saugumo ribos

Robotai gali ruošti ir deleguoti, bet jautrūs sprendimai lieka Tomui.

Tomo sprendimo reikia, kai yra:

- kaina;
- nuolaida;
- garantija;
- atsakomybė;
- konfliktas;
- skola;
- institucija;
- nestandartinis terminas;
- reputacijos rizika.

## Statusas

Šis dokumentas priklauso 01_SANASTA_OS stalčiui ir jungia visus kitus stalčius.

Prioritetas: A. Robotai turi būti kuriami ne kaip asmeninis Tomo žaislas, o kaip visa SANASTA operacinė sistema.
