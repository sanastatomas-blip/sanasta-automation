# SANASTA vairavimo režimas

## Paskirtis

Šis dokumentas aprašo SANASTA darbo režimą, kai Tomas vairuoja arba negali saugiai dirbti telefonu / kompiuteriu.

Tikslas: robotas turi dirbti tada, kai Tomas vairuoja. Tomas kalba, sistema paruošia veiksmus, o patvirtinimas vyksta tik tada, kai saugu.

## Pagrindinė taisyklė

Vairavimo metu Tomas neturi maigyti ekrano, rašyti klientams, kopijuoti informacijos ar ieškoti pokalbiuose.

Sistema turi priimti balsu padiktuotą informaciją ir ją paversti į:

- WhatsApp / Gmail atsakymo juodraštį;
- SANASTA event objektą;
- Trello / CRM / Calendar užduoties juodraštį;
- next_action;
- REVIEW arba DECISION kortelę viename lange.

## Darbo srautas

```text
Tomas vairuoja
-> padiktuoja faktą
-> sistema ištraukia esmę
-> sukuria eventą
-> paruošia tekstą / užduotį
-> padeda į REVIEW / DECISION
-> Tomas patvirtina tik kai saugu
```

## Vairavimo režimo ribos

Vairavimo režime sistema gali:

- klausyti diktavimo;
- paruošti tekstą;
- sukurti juodraštį;
- sukurti eventą;
- sukurti next_action;
- pažymėti riziką;
- padėti į vieno lango dashboardą.

Vairavimo režime sistema negali:

- reikalauti, kad Tomas ilgai skaitytų;
- siųsti jautrios žinutės be patvirtinimo;
- prašyti Tomo maigyti ekraną vairuojant;
- priimti sprendimo dėl kainos, nuolaidos, garantijos, atsakomybės ar termino;
- versti Tomo ieškoti tarp kelių pokalbių.

## Balso komandų pavyzdžiai

Tomas gali sakyti:

```text
Paruošk klientui WhatsApp.
Sukurk taską.
Įrašyk į objektą.
Padaryk follow-up.
Reikia Tomo sprendimo.
Kuro neskaičiuojam.
Klientas matė apžiūros metu.
Uždaryti po sąskaitos.
```

## Saugumo principas

Jeigu Tomas vairuoja, sistema turi duoti trumpą atsakymą, pvz.:

```text
Juodraštis paruoštas. Patvirtinti, kai sustosi.
```

Ne ilgą analizę, ne dvylikos punktų romaną. Vairavimas nėra seminaras apie CRM, nors žmonija turbūt ir tai bandytų parduoti.

## Režimai

### AUTO

Galima tik mažos rizikos informacijos apdorojimui:

- sukurti eventą;
- sukurti juodraštį;
- pažymėti follow-up;
- įrašyti pastabą.

### REVIEW

Naudoti, kai paruošta žinutė klientui, bet reikia Tomo patvirtinimo.

### DECISION

Naudoti, kai yra:

- kaina;
- nuolaida;
- garantija;
- atsakomybė;
- skola;
- konfliktas;
- institucija;
- nestandartinis terminas.

## Pavyzdys

Tomas padiktuoja:

```text
Klientas buvo apžiūros metu, matė pažeistą kondensato žarną. Tikėtina, kad prasitrinė ties kampu. Kuro neskaičiuojam.
```

Sistema paruošia:

```text
Sveiki, apžiūros metu kartu matėme, kad kondensato žarna yra pažeista. Tikėtina, kad ji galėjo prasitrinti ties aštresne vieta arba būti mechaniškai spaudžiama. Situaciją sutvarkysime, o kuro / atvykimo mokesčio šiuo atveju neskaičiuosime.
```

Ir eventą:

```json
{
  "source": "Voice/Driving",
  "topic": "Kondensato žarnos pažeidimas",
  "risk_level": "yellow",
  "mode": "REVIEW",
  "next_action": "Tomas patvirtina WhatsApp tekstą, kai saugu."
}
```

## Statusas

Šis dokumentas priklauso 01_SANASTA_OS, 02_GMAIL_RADARAS / KOMUNIKACIJOS_RADARAS ir 07_OPERACIJOS_DARBAI stalčiams.

Pagrindinis tikslas: robotas turi dirbti tada, kai Tomas vairuoja, o Tomas turi likti saugus, ne telefoną maigantis žmogus-API.
