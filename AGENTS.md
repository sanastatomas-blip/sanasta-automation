# SANASTA Codex darbo instrukcija

## Paskirtis
Šis repo yra SANASTA operacinės sistemos pradžia. Codex turi padėti ne kurti dar vieną žaislą, o paversti Tomo chaosą į veiksmų sistemą.

Tomo archetipas: **Starteris–Valdovas**.

- Stiprybė: greitai pradėti, pramušti, parduoti, spausti rezultatą.
- Rizika: pradėti per daug frontų, neužbaigti, laikyti rutiną galvoje.
- Pagrindinė taisyklė: naujas frontas leidžiamas tik tada, kai senas turi aiškų kitą veiksmą.

## Kiekviena užduotis privalo turėti

- `object_or_client` – objektas, klientas arba tema
- `value_eur` – piniginė vertė, suma arba galima rizika
- `deadline` – terminas
- `responsible_person` – atsakingas žmogus
- `next_action` – vienas konkretus kitas veiksmas
- `recorded_in` – kur įrašyta: Gmail, Calendar, CRM, Trello, Sheets ar kita
- `status` – būsena
- `priority` – A, B arba C
- `source` – iš kur atėjo: Gmail, rankinis įvedimas, klientas, kalendorius
- `notes` – trumpa pastaba

## Prioritetų logika

### A prioritetas
Skiriamas tik tada, kai yra pinigai, klientas laukia, skola, teisinė / garantinė rizika arba terminas šiandien / rytoj.

A negali būti skiriamas, jeigu nėra bent:

- `value_eur` arba aiškios rizikos,
- `deadline`,
- `next_action`.

### B prioritetas
Sistemos kūrimas: šablonai, CRM, kalendorius, procesas, standartas, automatizacija.

### C prioritetas
Idėjos be aiškios vertės, termino arba atsakingo žmogaus. C nėra šiukšlė visam laikui, bet ji negali užgožti A ir B darbų.

## Dienos režimas
Sistema turi padėti išrinkti tik 3 pagrindinius uždarymus:

1. Pinigų veiksmas
2. Sistemos veiksmas
3. Uždarymo veiksmas

Nedaryti ekranų su 47 užduotimis. Tomas nėra serverių ferma, nors kartais taip elgiasi.

## Codex darbo taisyklės

1. Pirmiausia paprastumas, tada grožis.
2. Telefonu naudojamas vaizdas yra svarbesnis už teorinį tobulumą.
3. Kiekviena funkcija turi mažinti chaosą arba artinti pinigus.
4. Nepridėti sudėtingų priklausomybių be reikalo.
5. Kiekvienas pakeitimas turi būti paaiškintas README.
6. Jeigu reikia pasirinkti tarp naujos funkcijos ir užbaigimo disciplinos, rinktis užbaigimo discipliną.

## Draudžiama

- Kurti funkcijas be aiškaus ryšio su pinigais, rizika, terminais arba sistema.
- Leisti A prioritetą be būtinos informacijos.
- Kurti ekranus, kurie skatina dar daugiau chaoso.
- Slėpti neaiškią logiką kode be komentarų.
