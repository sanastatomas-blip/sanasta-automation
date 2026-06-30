# SANASTA ChatGPT projektu inventorizacija

## Paskirtis

Sis failas skirtas realiai lokalizuoti ChatGPT projektus ir pokalbius i 7 SANASTA stalcius.

Kai Tomas atidaro projekta arba parodo ekrana, projektas turi buti ivertintas pagal sia lentele, pervadintas ir priskirtas stalciui.

## Inventorizacijos lentele

| Dabartinis pavadinimas | Naujas pavadinimas | Stalcius | Statusas | Ka issaugoti | Kitas veiksmas |
|---|---|---|---|---|---|
| Prisijungti prie WhatsApp | SANASTA_KOMUNIKACIJOS_WhatsApp_Tasker_AI_AKTYVU | 02_GMAIL_RADARAS / KOMUNIKACIJOS_RADARAS + 07_OPERACIJOS_DARBAI | AKTYVU | `whatsapp-android-ai-tasker-setup.md`, Tasker + AutoNotification + OpenAI API logika | Perkelti / dubliuoti esme i `docs/whatsapp_android_ai_tasker_setup.md`; uztikrinti REVIEW rezima, ne automatini siuntima |
| Codex / SANASTA automatizacija | SANASTA_OS_Codex_taisykles_AKTYVU | 01_SANASTA_OS | AKTYVU | AGENTS.md, START_HERE, docs indeksai, taisykles | Laikyti kaip pagrindini operacines sistemos projekta |
| Gmail radaras / laisku tvarkymas | SANASTA_KOMUNIKACIJOS_Gmail_Radaras_AKTYVU | 02_GMAIL_RADARAS / KOMUNIKACIJOS_RADARAS | AKTYVU | AUTO / REVIEW / DECISION, laisku rusiavimas, skolos, follow-up | Sujungti su komunikacijos radaru; nepalikti atskiro padriko projekto |
| Monitoringas / PRO / 1000 klientu | SANASTA_MONITORINGAS_1000_klientu_modelis_AKTYVU | 04_MONITORINGAS | AKTYVU | mastelio formule, capacity modelis, rizikos zonos | Naudoti `docs/monitoring_scale_capacity.md` kaip pagrinda |
| Komerciniai pasiulymai | SANASTA_KOMERCINIAI_PASIULYMAI_sablonai_AKTYVU | 05_KOMERCINIAI_PASIULYMAI | AKTYVU | pasiulymu psichologija, sablonai, kainodara | Visi pasiulymai turi eiti per sita stalciu |
| Marketingo postai / socialiniai | SANASTA_MARKETINGAS_postai_AKTYVU | 06_MARKETINGAS_POSTAI | LAUKIA | postu idejos, LinkedIn, FB, TikTok, BNI | Sukurti atskira postu lentele / kalendoriu |
| Darbu planavimas / operacijos | SANASTA_OPERACIJOS_darbai_kalendorius_AKTYVU | 07_OPERACIJOS_DARBAI | AKTYVU | montavimai, servisai, medziagos, kalendorius, Trello | Susieti su vieno lango dashboardu |

## Kaip pildyti toliau

Kai randamas naujas ChatGPT projektas:

1. Irasomas dabartinis pavadinimas.
2. Suteikiamas naujas SANASTA formato pavadinimas.
3. Priskiriamas stalcius.
4. Pazymimas statusas: AKTYVU, LAUKIA, ARCHYVAS, SUJUNGTI arba ISTRINTI.
5. Irasoma, ka reikia issaugoti.
6. Irasomas kitas veiksmas.

## Statusu reiksmes

- AKTYVU - naudojamas dabar.
- LAUKIA - vertingas, bet ne siandien.
- ARCHYVAS - saugoti, bet nenaudoti kasdien.
- SUJUNGTI - dubliuoja kita projekta.
- ISTRINTI - neturi vertes.

## Pirma praktine tvarkymo eile

1. Prisijungti prie WhatsApp -> pervadinti i `SANASTA_KOMUNIKACIJOS_WhatsApp_Tasker_AI_AKTYVU`.
2. Visi Gmail radarai -> sujungti i `SANASTA_KOMUNIKACIJOS_Gmail_Radaras_AKTYVU`.
3. Codex / agento taisykles -> laikyti `SANASTA_OS_Codex_taisykles_AKTYVU`.
4. Monitoringas -> laikyti `SANASTA_MONITORINGAS_1000_klientu_modelis_AKTYVU`.
5. Postai -> lokalizuoti, bet kol kas statusas LAUKIA.

## Svarbi taisykle

ChatGPT projektas nera uzdarytas, kol is jo naudinga informacija neperkelta i:

- `AGENTS.md`, jeigu tai taisykle;
- `docs/`, jeigu tai issamesnis procesas;
- CRM / Trello / Calendar, jeigu tai realus darbas;
- archyva, jeigu tai istorija.
