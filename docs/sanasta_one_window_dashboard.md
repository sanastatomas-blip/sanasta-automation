# SANASTA vieno lango darbo vaizdas

## Paskirtis

Sis dokumentas apraso, kaip turi atrodyti pagrindinis SANASTA darbo langas, kad Tomui nereiketu ieskoti tarp 13 ivykiu, laisku, kalendoriaus ir pokalbiu.

Tikslas: vienas ekranas turi parodyti, kas siandien svarbiausia, kas dega, kas laukia, kas deleguota ir kur reikia Tomo sprendimo.

## Pagrindine taisykle

Tomas neturi ieskoti. Sistema turi atrinkti.

Viename lange turi buti ne visi ivykiai, o tik svarbiausi sprendimai ir veiksmai.

## Pagrindinis langas

Pagrindinis SANASTA langas turi tureti 5 blokus:

1. Siandien dega
2. Reikia Tomo sprendimo
3. Deleguota robotui
4. Laukia kliento / apmokejimo
5. Siandien uzdaryti

## 1. Siandien dega

Rodoma tik tai, kas yra A prioritetas:

- klientas laukia;
- pinigai;
- skola;
- rizika;
- terminas siandien arba rytoj;
- klientui salta / karsta;
- garantine / reputacine rizika;
- objektas stringa.

Maksimaliai rodyti 3 elementus.

Jeigu yra daugiau nei 3, sistema turi atrinkti pagal:

1. rizika;
2. pinigus;
3. termina;
4. kliento svarba;
5. reputacija.

## 2. Reikia Tomo sprendimo

Cia rodomi tik DECISION elementai:

- kaina;
- nuolaida;
- konfliktas;
- garantija;
- atsakomybe;
- skola;
- institucija;
- partneryste;
- didesnis objektas;
- terminas, kurio negalima zadeti be Tomo.

Kiekvienas elementas turi tureti:

- trumpa santrauka;
- rekomenduojama sprendima;
- rizika;
- ka Tomas turi patvirtinti.

## 3. Deleguota robotui

Cia rodoma, ka sistema jau daro pati:

- paruostas laisko juodrastis;
- sukurtas taskas;
- sukurtas follow-up;
- paruostas medziagu sarasas;
- paruostas kalendoriaus irasas;
- patikrinta, ar issiusta poirengimine instrukcija;
- paruostas skolos priminimas;
- suvestas CRM irasas.

Tikslas: Tomas mato, kad darbas juda, bet pats nekopijuoja informacijos tarp sistemu.

## 4. Laukia kliento / apmokejimo

Cia rodomi piniginiai ir komunikaciniai laukimai:

- pasiulymas issiustas, laukia atsakymo;
- saskaita issiusta, laukia apmokejimo;
- klientas neatsake;
- reikia follow-up;
- reikia priminti del dokumentu;
- objektas atliktas, bet neuzdarytas.

Kiekvienas elementas turi tureti follow-up data.

## 5. Siandien uzdaryti

Cia rodomi darbai, kuriuos galima uzdaryti siandien:

- issiusti saskaita;
- issiusti poirengimine instrukcija;
- gauti apmokejima;
- patvirtinti akta;
- uzdaryti Trello kortele;
- perkelti objekta i archyva;
- issiusti paskutini follow-up.

Maksimaliai rodyti 3 uzdarymus per diena.

## Korteles formatas

Kiekvienas elementas viename lange turi buti rodomas trumpai:

```text
[Kategorija] Klientas / objektas
Kas vyksta: 1 sakinys
Rizika / verte: trumpai
Kitas veiksmas: konkretus veiksmas
Reikia: Tomas / robotas / technikas
Terminas: data arba siandien / rytoj
```

## Pavyzdys

```text
[A PRIORITETAS] Jonava - kondicionierius be aptarnavimo
Kas vyksta: Antri metai naudotas kondicionierius, nedarytas aptarnavimas, bega kondensatas.
Rizika / verte: klientas bando priskirti atsakomybe SANASTA.
Kitas veiksmas: atlikti mokama technini aptarnavima ir fiksuoti radinius.
Reikia: Tomas / technikas
Terminas: siandien
```

## Ko nerodyti pagrindiniame lange

Nerodyti:

- visu kalendoriaus ivykiu;
- visu laisku;
- visu ideju;
- visu C prioriteto pasvarstymu;
- archyvo;
- dubliuotu uzduociu;
- techniniu smulkmenu, kurios nereikalauja sprendimo.

Pagrindinis langas nera sandelis. Jis yra valdymo pultas.

## Filtravimo taisykles

Eventas patenka i pagrindini langa tik jei turi:

- A prioriteta;
- DECISION rezima;
- siandien / rytoj termina;
- pinigu laukima;
- objekto uzdarymo galimybe;
- aktyvu follow-up;
- raudona / oranzine rizika.

Visi kiti eventai lieka CRM / Trello / archyve / sistemos fone.

## Vieno lango tikslas

Vienas langas turi atsakyti i 5 klausimus:

1. Kas siandien dega?
2. Kur reikia Tomo sprendimo?
3. Ka robotas jau daro?
4. Kur pinigai / klientai laukia?
5. Ka siandien galima uzdaryti?

## Statusas

Sis dokumentas priklauso 01_SANASTA_OS ir 07_OPERACIJOS_DARBAI stalciams.

Jis yra B prioritetas, nes mazina Tomo laika prie kompiuterio ir padeda valdyti darba per viena aisku langa.
