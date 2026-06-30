# SANASTA monitoringas - mastelio ir pajegumo modelis

## Kodel sitas dokumentas atsirado

Verslininko klausimas po SANASTA monitoringo idejos pristatymo:

> Kas bus, kai turesi 1000 klientu? Kaip juos aptarnausi? Kiek zmoniu reikes?

Sis klausimas turi buti laikomas esminiu SANASTA monitoringo projekto klausimu. Monitoringas negali buti kuriamas taip, kad Tomas arba vienas zmogus rankomis ziuretu i visus klientus.

## Pagrindine taisykle

Sistema turi aptarnauti mase klientu per filtravima, rizikos vertinima, automatini delegavima ir pajegumo planavima.

Ne zmogus aptarnauja 1000 klientu. Sistema atrenka, kuriems klientams siandien reikia zmogaus.

## Mastelio formule

1000 klientu -> 1000 duomenu srautu -> automatiniai filtrai -> realus ivykiai -> prioritetai -> Tomo sprendimai -> visa kita robotui.

Darbine formule:

1000 klientu -> 20 ivykiu per diena -> 5 prioritetai -> 3 Tomo sprendimai.

Skaiciai yra pradinis modelis, ne galutine tiesa. Jie turi buti tikrinami pagal realius duomenis.

## Reikalingas capacity modelis

Monitoringas privalo tureti pajegumo skaiciavima:

- kiek klientu gali aptarnauti 1 administravimo / monitoringo zmogus;
- kiek klientu gali aptarnauti 1 serviso zmogus;
- kiek raudonu / oranziniu ivykiu per diena tiketina is 100 klientu;
- kiek ivykiu robotas gali uzdaryti be zmogaus;
- kiek ivykiu reikalauja skambucio;
- kiek ivykiu reikalauja nuotolinio sprendimo;
- kiek ivykiu reikalauja vaziuoti i objekta;
- kiek klientu gali buti valdoma Basic, PRO ir PRO+ planuose;
- kada reikia samdyti / prijungti nauja zmogu arba partneri.

## Darbiniai vaidmenys augant monitoringui

### 1. Robotinis monitoringo agentas
Atsakingas uz:

- duomenu tikrinima;
- nukrypimu aptikima;
- rizikos zonu priskyrima;
- laisku / zinuciu juodrascius;
- Trello / CRM / Sheets irasus;
- follow-up priminimus;
- klientu grupavima pagal statusa.

### 2. Monitoringo koordinatorius
Reikalingas, kai Tomas nebegali pats perziureti visu oranziniu ir raudonu ivykiu.

Atsakingas uz:

- ryto radaro perziura;
- klientu kontaktavima;
- nuotolines rekomendacijas;
- serviso uzduociu paruosima;
- informacijos rinkima is kliento;
- prioritetu eskalavima Tomui.

### 3. Serviso zmogus / technikas
Atsakingas uz:

- fizinius vizitus;
- diagnostika objekte;
- garantinius veiksmus;
- mokamus serviso darbus;
- metines prieziuros darbus;
- techninius patvirtinimus po monitoringo signalu.

### 4. Tomas
Tomas neturi buti pirmo lygio operatorius.

Tomas sprendzia:

- kaina;
- nuolaida;
- garantijos / atsakomybes riba;
- prioritetu konfliktus;
- didelius objektus;
- partnerystes;
- produkto krypti;
- kada reikia naujo zmogaus.

## Reikalingi skaiciai, kuriuos sistema turi pradeti rinkti

Kad butu galima atsakyti i klausima "kiek zmoniu reikes", reikia rinkti:

- klientu skaiciu pagal plana: Basic / PRO / PRO+;
- kiek per diena atsiranda geltonu, oranziniu ir raudonu ivykiu;
- kiek ivykiu uzdaro robotas;
- kiek ivykiu reikalauja zmogaus perziuros;
- kiek ivykiu virsta realiu serviso vizitu;
- kiek laiko uztrunka vienas nuotolinis ivykis;
- kiek laiko uztrunka vienas fizinis vizitas;
- kiek procentu klientu per metus reikia metinio aptarnavimo;
- kiek klientu turi garantine rizika;
- kiek klientu tampa komercine galimybe.

## Pradinis pajegumo skaiciavimo principas

Kol nera realiu duomenu, naudoti atsargu modeli:

- 1 monitoringo koordinatorius gali valdyti tik tuos klientus, kuriuos sistema jau filtruoja;
- kuo daugiau automatizacijos, tuo maziau rankinio darbo;
- Basic klientai turi gauti daugiausia automatika;
- PRO klientai gauna aktyvesne zmogaus perziura;
- PRO+ klientai gauna prioritetini zmogaus demesi ir greitesni servisa.

Svarbu: zmogaus pajegumas turi buti skaiciuojamas ne pagal klientu skaiciu, o pagal ivykiu skaiciu.

1000 ramiu klientu nera problema. 100 klientu be filtro ir su nuolatiniais skambuciais yra problema.

## Sprendimo kryptis

SANASTA monitoringas turi buti projektuojamas taip:

1. Visi duomenys ateina i viena sistema.
2. Sistema skirsto klientus i zonas: zalia, geltona, oranzine, raudona.
3. Zali ir geltoni atvejai maksimaliai automatizuojami.
4. Oranziniai atvejai virsta uzduotimis, laiskais arba skambuciais.
5. Raudoni atvejai eskaluojami zmogui.
6. Tomas mato tik sprendimus, ne visa triuksma.
7. Sistema kaupia statistika, kad butu galima prognozuoti darbuotoju poreiki.

## Verslininko klausimo atsakymo forma

Kai reikia atsakyti partneriui / investuotojui / rimtam verslininkui:

> Mes neplanuojame 1000 klientu aptarnauti rankiniu budu. Monitoringas projektuojamas kaip filtravimo ir rizikos valdymo sistema. Dauguma klientu bus automatiskai stebimi, o zmogui bus keliami tik tie atvejai, kuriems reikia sprendimo. Pajeguma skaiciuosime ne pagal bendra klientu skaiciu, o pagal realiu ivykiu skaiciu: kiek is ju automatizuojama, kiek reikalauja kontakto ir kiek virsta fiziniu servisu.

## Statusas

Sis dokumentas yra SANASTA monitoringo projekto B prioritetas. Jis turi buti naudojamas kuriant produkto architektura, kainodara, komandos augimo plana ir serviso pajegumo skaiciavima.
