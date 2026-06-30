# SANASTA WhatsApp Android AI Tasker automatizacija

## Paskirtis

Sis dokumentas apraso WhatsApp automatizacijos darba Android telefone naudojant Tasker, AutoNotification ir AI logika.

Tikslas: Tomas padiktuoja fakta arba priezasti, sistema is karto paruosa WhatsApp atsakymo juodrasti klientui, o Tomas tik patvirtina.

## Pagrindine taisykle

WhatsApp automatika neturi pati siusti jautriu atsakymu be Tomo patvirtinimo.

Darbo modelis:

```text
Tomas padiktuoja fakta -> AI suformuoja klientui zinute -> Tomas patvirtina -> WhatsApp zinute siunciama
```

## Kada naudoti

Naudoti, kai Tomas objekte arba kelyje padiktuoja:

- gedimo priezasti;
- atlikta darba;
- radini objekte;
- ar bus skaiciuojamas mokestis;
- ar reikia kuro / atvykimo mokescio;
- ar klientas buvo apziuros metu;
- ar reikia trumpai informuoti klienta.

## Pavyzdys: kondensato zarna

Tomo diktavimas:

```text
Priezastis gali buti, kad kondensato zarna prasitryne i astrų kampa. Klientas buvo apziuros metu ir viska mate. Kuro neskaičiuojam, nes situacija susijusi su musu atliktu irengimu.
```

AI turi paruosti WhatsApp zinute:

```text
Sveiki, apziuros metu kartu mateme, kad kondensato zarna yra pazeista. Tiketina, kad ji galejo prasitrinti ties astresne vieta arba buvo mechaniskai spaudziama. Situacija sutvarkysime, o kuro / atvykimo mokescio siuo atveju neskaičiuosime.
```

## Jautrumo taisykle

Jeigu zinute susijusi su:

- kaina;
- nuolaida;
- garantija;
- atsakomybe;
- skola;
- konfliktu;
- institucija;
- terminu;
- pazadu klientui;

rezimas turi buti REVIEW arba DECISION.

Automatinis siuntimas draudziamas.

## Leidziami automatiniai juodrasciai

AI gali paruosti WhatsApp juodrasti, kai reikia:

- trumpai informuoti klienta apie rasta priezasti;
- patvirtinti, kad darbas atliktas;
- paprasyti nuotrauku / video;
- paprasyti adreso;
- informuoti, kad laikas bus patikslintas;
- paaiskinti, kad reikia techninio aptarnavimo;
- pranesti, kad paruosime pasiulyma;
- priminti del apmokejimo, jei tekstas neutralus ir patvirtintas pagal taisykles.

## WhatsApp zinutes formatas

Zinute turi buti:

- trumpa;
- rami;
- be perteklinio teisinio tono;
- be kaltės prisipazinimo, jeigu tai nepatvirtinta;
- su faktu;
- su sprendimu;
- su kitu veiksmu.

Formatas:

```text
Sveiki, [faktas]. [trumpas paaiskinimas]. [ka darome / padarysime]. [mokestis / terminas, jei patvirtinta].
```

## Kliento dalyvavimo taisykle

Jeigu klientas buvo apziuros metu ir mate radini, zinute turi buti trumpa.

Nereikia ilgai irodineti to, ka klientas pats mate.

Pavyzdys:

```text
Sveiki, kadangi apziuros metu situacija mateme kartu, papildomai nesiplesiu. Kondensato zarna buvo pazeista, ja sutvarkysime, o kuro / atvykimo mokescio siuo atveju neskaičiuosime.
```

## Kuro / atvykimo mokescio taisykle

Jeigu situacija susijusi su SANASTA atliktu irengimu ir vertinama kaip garantinis / atsakomybes veiksmas, kuro arba atvykimo mokestis klientui neskaiciuojamas.

Saugus tekstas:

```text
Siuo atveju kuro / atvykimo mokescio atskirai neskaiciuosime, nes situacija susijusi su musu atliktu irengimu.
```

Nerasyti:

```text
Tai musu klaida.
```

Rasyti:

```text
Situacija susijusi su musu atliktu irengimu.
```

## Agentas turi papildomai sukurti eventa

Kai ruosiamas WhatsApp atsakymas, sistema turi sukurti arba atnaujinti SANASTA eventa:

- source: WhatsApp / Voice;
- client_name;
- object_or_address;
- topic;
- message_summary;
- risk_level;
- mode;
- next_action;
- status;
- notes.

## Statusas

Sis dokumentas priklauso 02_GMAIL_RADARAS / KOMUNIKACIJOS_RADARAS ir 07_OPERACIJOS_DARBAI stalciams.

Pagrindinis tikslas: paversti Tomo trumpa diktavimo komanda i paruosta WhatsApp kliento zinute ir operacini eventa.
