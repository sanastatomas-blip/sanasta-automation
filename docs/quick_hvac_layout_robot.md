# SANASTA greito ŠVOK užmetimo robotas

## Paskirtis

Šis dokumentas aprašo robotą, kuris padeda greitai paruošti žemesnės vertės šildymo ir vėdinimo sistemų techninį užmetimą pagal namo projektą.

Tikslas nėra paruošti galutinį pasirašomą projektą. Tikslas yra greitai iš plano gauti praktinius skaičius, medžiagų kiekius, įrangos kryptį, preliminarų sprendimą ir komercinio pasiūlymo pagrindą.

## Naudojimo situacija

Kai turime:

- namo planą PDF / DWG / nuotrauką;
- patalpų plotus;
- pastato aukštingumą;
- preliminarią konstrukciją;
- langų / durų informaciją, jei yra;
- kliento pageidavimą dėl šildymo, vėdinimo ar kondicionavimo;

robotas turi greitai paruošti techninį juodraštį.

## Ką robotas turi išvesti

### 1. Patalpų lentelė

- patalpos pavadinimas;
- plotas;
- aukštis, jei žinomas;
- tūris;
- paskirtis;
- ar reikalingas šildymas;
- ar reikalingas vėdinimas;
- ar reikalingas kondicionavimas.

### 2. Šildymo užmetimas

- preliminarus šilumos poreikis;
- rekomenduojama šildymo kryptis;
- grindinio šildymo kontūrų logika;
- kolektorių vietos pasiūlymas;
- vamzdžio ilgio preliminarus kiekis;
- termostatų / zonų logika;
- rizikos ir neaiškumai.

### 3. Vėdinimo užmetimas

- tiekiamo oro kiekiai;
- šalinamo oro kiekiai;
- patalpų balansas;
- difuzorių / grotelių kiekiai;
- ortakių kryptys;
- rekuperatoriaus vietos pasiūlymas;
- ortakių preliminarūs kiekiai;
- triukšmo / ilgių / montavimo rizikos.

### 4. Medžiagų kiekiai

Preliminariai:

- grindinio šildymo vamzdis;
- kolektoriai;
- spintelės;
- pavara / termostatai;
- izoliacija / tvirtinimai;
- ortakiai;
- alkūnės;
- trišakiai;
- difuzoriai;
- grotelės;
- sklendės;
- rekuperatorius;
- kondensato nubėgimas;
- papildomi mazgai.

### 5. Komercinio pasiūlymo pagrindas

Robotas turi paruošti ne tik techniką, bet ir pasiūlymo pagrindą:

- darbų apimtis;
- įrangos kryptis;
- medžiagų sąrašas;
- ko trūksta tikslinimui;
- ko neįtraukta;
- rizikos;
- kliento klausimai;
- ar reikia projektuotojo / atsakingo specialisto patikros.

## Svarbi atsakomybės riba

Visuose išėjimuose turi būti aiški žyma:

```text
Tai preliminarus techninis užmetimas ir komercinio pasiūlymo pagrindas. Galutinis projektas, jei jis reikalingas pagal statybos procesą ar teisės aktus, turi būti patikrintas ir patvirtintas atsakingo projektuotojo / specialisto.
```

## Darbo srautas

```text
Namo planas / PDF / DWG / nuotrauka
-> patalpų atpažinimas
-> plotų ir tūrių lentelė
-> šildymo užmetimas
-> vėdinimo užmetimas
-> medžiagų kiekiai
-> trūkstami duomenys
-> pasiūlymo pagrindas
-> REVIEW Tomui
```

## Režimas

Šis robotas beveik visada turi dirbti REVIEW režimu.

AUTO leidžiamas tik bendram skaičiavimo juodraščiui be kliento siuntimo.

DECISION reikalingas, kai:

- nurodoma galutinė kaina;
- pasirenkama brangi įranga;
- prisiimama atsakomybė;
- dokumentas siunčiamas klientui kaip galutinis;
- reikia projektuotojo parašo;
- yra normų ar teisinių įsipareigojimų klausimas.

## Pirmas MVP

Pirmas MVP turi būti labai paprastas:

Input:

- patalpų sąrašas su plotais;
- pastato tipas;
- ar reikia šildymo;
- ar reikia vėdinimo;
- ar reikia kondicionavimo.

Output:

- patalpų lentelė;
- preliminarus šildymo poreikis;
- grindinio šildymo vamzdžio kiekio juodraštis;
- vėdinimo oro kiekių juodraštis;
- difuzorių / šalinimo taškų kiekiai;
- trūkstami duomenys;
- pasiūlymo struktūra.

## Vėlesnis etapas

Vėliau galima jungti:

- PDF plano analizę;
- DWG / DXF importą;
- Excel medžiagų žiniaraštį;
- Revit / CAD užduoties generavimą;
- tiekėjų kainynus;
- pasiūlymo PDF generavimą;
- darbo užduotį montuotojui.

## Statusas

Šis dokumentas priklauso 07_OPERACIJOS_DARBAI, 05_KOMERCINIAI_PASIULYMAI ir 01_SANASTA_OS stalčiams.

Prioritetas: B/A pagal objektą. Tai labai praktiškas robotas mažesnės vertės objektams, kur reikia greitai įvertinti sprendimą ir paruošti pasiūlymo pagrindą.
