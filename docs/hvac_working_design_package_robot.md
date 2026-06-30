# SANASTA darbinio ŠVOK projekto robotas

## Paskirtis

Šis dokumentas aprašo aukštesnio lygio SANASTA projektavimo pagalbinį robotą, kurio tikslas yra iš namo projekto arba patalpų duomenų paruošti darbinį ŠVOK projekto paketą.

Tai nėra tik preliminarus skaičiuotuvas. Tai turi būti darbo paketas, pagal kurį lengviau dirbti Tomui, rangovui, subrangovui, technikui, klientui ir, kai reikia, atsakingam projektuotojui.

## Kodėl to reikia SANASTAI

Dabar daug mažesnių objektų vertinami rankiniu būdu: iš plano, patirties, Excel, tiekėjų kainynų ir Tomo galvos. Tai veikia, bet nekelia įmonės lygio taip, kaip galėtų.

Darbinio ŠVOK projekto robotas turi padėti SANASTAI atrodyti ir veikti kaip įmonė, turinti aiškią projektavimo sistemą.

Tikslas:

```text
Ne „kažkaip paskaičiavome“.
O „paruoštas darbinis ŠVOK paketas: schemos logika, skaičiai, medžiagos, atsakomybės ribos, darbų apimtis“.
```

## Vertė

Šis robotas kelia SANASTA lygį, nes leidžia:

- greičiau paruošti pasiūlymą;
- sumažinti rankinį skaičiavimą;
- aiškiau perduoti darbą montuotojui;
- aiškiau komunikuoti klientui;
- aiškiau perduoti medžiagų sąrašą tiekimui;
- turėti patikrinamą pagrindą, iš kur atsirado kiekiai;
- sumažinti ginčus, kas ką turėjo suprasti;
- dirbti taip, lyg SANASTA turėtų vidinį projektavimo skyrių;
- prireikus perduoti paketą žmogui projektuotojui patikrai / tvirtinimui.

## Darbinio projekto paketo turinys

Robotui keliama užduotis sugeneruoti tokį paketą:

### 1. Įvesties santrauka

- objekto tipas;
- adresas / objektas, jei nurodyta;
- plotas;
- aukštai;
- patalpų sąrašas;
- konstrukcijos, jei žinomos;
- kliento pageidavimai;
- kas neaišku;
- kokie dokumentai naudoti.

### 2. Patalpų lentelė

Kiekvienai patalpai:

- pavadinimas;
- plotas;
- aukštis;
- tūris;
- paskirtis;
- šildymas taip / ne;
- vėdinimas taip / ne;
- kondicionavimas taip / ne;
- pastabos.

### 3. Šildymo dalis

Paruošti:

- preliminarų šilumos poreikį;
- zonų logiką;
- grindinio šildymo kontūrų pasiūlymą;
- kolektorių vietų pasiūlymą;
- vamzdžio ilgių juodraštį;
- termostatų / pavarų / zonų kiekį;
- pagrindinių mazgų aprašymą;
- hidraulinės logikos pastabas;
- rizikas ir neaiškumus.

### 4. Vėdinimo dalis

Paruošti:

- tiekiamo oro kiekius;
- šalinamo oro kiekius;
- oro balansą;
- difuzorių / grotelių kiekį;
- ortakių trasų logiką;
- rekuperatoriaus vietos pasiūlymą;
- lauko oro / išmetimo vietų pastabas;
- triukšmo, ilgių, kondensato ir montavimo rizikas.

### 5. Kondicionavimo / vėsinimo dalis, jei taikoma

Paruošti:

- preliminarią vėsos poreikio kryptį;
- vidinių blokų vietų pasiūlymą;
- lauko bloko vietos pastabas;
- trasų ilgių juodraštį;
- kondensato nuvedimo logiką;
- rizikas.

### 6. Medžiagų žiniaraštis

Paruošti medžiagų sąrašą:

- grindinio šildymo vamzdis;
- kolektoriai;
- spintelės;
- pavaros;
- termostatai;
- jungtys;
- izoliacija;
- tvirtinimai;
- ortakiai;
- alkūnės;
- trišakiai;
- perėjimai;
- difuzoriai;
- grotelės;
- sklendės;
- rekuperatorius;
- kondensato dalys;
- papildomi mazgai.

Kiekvienai eilutei turi būti:

- pavadinimas;
- kiekis;
- matavimo vienetas;
- pastaba;
- ar kiekis preliminarus, ar tikslintas.

### 7. Darbų apimties aprašymas

Robotui reikia paruošti aiškų darbų paketą:

- kas įtraukta;
- kas neįtraukta;
- ko reikia iš kliento;
- ko reikia iš rangovo;
- ko reikia iš projektuotojo, jei taikoma;
- kokie sprendimai turi būti patvirtinti prieš montavimą.

### 8. Atsakomybių ribos

Paketui būtina turėti atsakomybių lentelę:

| Sritis | Atsakingas |
|---|---|
| Pradiniai duomenys | klientas / architektas / Tomas |
| Preliminarus techninis užmetimas | SANASTA robotas + Tomas |
| Skaičių peržiūra | Tomas / atsakingas specialistas |
| Galutinis projektas, jei reikalingas | projektuotojas / atsakingas specialistas |
| Montavimo sprendimų laikymasis | rangovas / SANASTA / subrangovas pagal sutartį |
| Pakeitimai objekte | fiksuojami atskirai |

## Labai svarbi formuluotė

Kiekviename pakete turi būti aiški riba:

```text
Šis dokumentas yra darbinis ŠVOK projekto paketas ir komercinio pasiūlymo / montavimo pasiruošimo pagrindas. Jei pagal objekto statusą, teisės aktus ar sutartį reikalingas oficialus projektas, jis turi būti patikrintas ir patvirtintas atsakingo projektuotojo / specialisto.
```

## Kodėl tai geriau nei dabar

Dabar dažnai visi klausinėja:

- kiek vamzdžio?
- kiek difuzorių?
- kur kolektorius?
- kas skaičiavo?
- kodėl tokia įranga?
- kas atsakingas?
- ką montuotojas turi padaryti?

Su robotu turi būti taip:

```text
Yra paketas.
Yra skaičiai.
Yra medžiagos.
Yra darbų apimtis.
Yra atsakomybės ribos.
Yra ką tikrinti.
Yra ką pasirašyti / patvirtinti, jei reikia.
```

## Režimas

Darbinio projekto robotas dirba REVIEW režimu.

AUTO leidžiamas tik skaičių juodraščio ruošimui viduje.

DECISION reikalingas, kai:

- dokumentas siunčiamas klientui;
- dokumentas tampa sutarties / kainos pagrindu;
- nurodoma galutinė kaina;
- pasirenkama įranga;
- atsiranda atsakomybės klausimas;
- reikalingas projektuotojo parašas;
- daroma išvada, kas kaltas dėl neveikiančio sprendimo.

## Pirmas MVP

Pirmas MVP neturi skaityti sudėtingų PDF automatiškai.

Pirmas MVP turi priimti:

- patalpų sąrašą;
- plotus;
- aukštį;
- ar reikia šildymo;
- ar reikia vėdinimo;
- ar reikia kondicionavimo;
- pastato tipą;
- pastabas.

Ir sugeneruoti:

- patalpų lentelę;
- šildymo juodraštį;
- vėdinimo juodraštį;
- medžiagų žiniaraštį;
- trūkstamų duomenų sąrašą;
- darbų apimtį;
- atsakomybių ribas;
- pasiūlymo pagrindą.

## Vėlesnis etapas

Vėliau prijungti:

- PDF plano analizę;
- DWG / DXF importą;
- medžiagų kainynus;
- tiekėjų kodus;
- Excel žiniaraštį;
- PDF pasiūlymą;
- montuotojo darbo užduotį;
- projektuotojo patikros paketą;
- architektui / klientui skirtą aiškinamąją dalį.

## Statusas

Šis dokumentas priklauso 01_SANASTA_OS, 05_KOMERCINIAI_PASIULYMAI ir 07_OPERACIJOS_DARBAI stalčiams.

Prioritetas: A/B. Tai strateginis robotas, kuris gali kelti SANASTA reitingą, profesionalumą ir sumažinti Tomo rankinį projektavimo / skaičiavimo darbą.
