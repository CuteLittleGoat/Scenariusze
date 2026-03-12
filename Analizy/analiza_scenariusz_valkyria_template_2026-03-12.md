# Analiza: przygotowanie scenariusza na bazie `template.html`, `Gilead.html` i `Na_Skrzydalach_Valkyrii.pdf`

## Prompt użytkownika
> Przeprowadź analizę.
> Mając do dyspozycji pliki:
> template.html
> Warhammer40k/Gilead/Gilead.html
> Warhammer40k/TA_02/Na_Skrzydalach_Valkyrii.pdf
>
> Jesteś w stanie przygotować scenariusz do przygody? Czy jakieś dodatkowe instrukcje/wytyczne można zawrzeć w pliku template.html w sekcji "Instrukcja dla AI"? Masz jakieś sugestie i propozycje co zrobić, żeby cały proces przebiegał optymalnie?

---

## Krótka odpowiedź
Tak — na podstawie tych trzech plików **da się przygotować pełny, grywalny scenariusz**.

- `template.html` daje bardzo dobry szkielet techniczny i redakcyjny scenariusza (sceny, linkowanie materiałów, handouty, ilustracje, NPC, zakończenie).
- `Warhammer40k/Gilead/Gilead.html` dostarcza szerokie tło lore systemu Gilead (frakcje, planety, klimat imperium nihilus, napięcia między organizacjami).
- `Na_Skrzydalach_Valkyrii.pdf` dostarcza gotowy wzorzec „wojennego” scenariusza W&G: segmenty, tempo, briefing, cele operacyjne, walki, wsparcie, eskalacja, finał.

To zestaw wystarczający do przygotowania przygody zarówno „od zera”, jak i do adaptacji istniejącego formatu operacyjnego na nową fabułę.

---

## Co działa już teraz bardzo dobrze
1. **Praktyczny układ dla MG** (template): sekcje są nastawione na użycie przy stole, nie tylko na „ładny opis”.
2. **Nacisk na spójność odnośników** (`H1/IL1` + linki zwrotne): bardzo pomaga w prowadzeniu sesji online lub hybrydowo.
3. **Silna baza settingowa** (Gilead): pozwala osadzić scenariusz bez łamania klimatu.
4. **Sprawdzony model militarnego przebiegu przygody** (Valkyria): segmentacja misji + jasne cele + rosnąca presja.

---

## Najważniejsze braki / ryzyka przy automatycznym tworzeniu scenariuszy
1. **Brak wymuszonego „briefu wejściowego”** przed generowaniem treści.
   - AI bez danych wejściowych będzie zgadywać poziom drużyny, typ kampanii i ton przygody.
2. **Brak checklisty lore consistency**.
   - Model może tworzyć elementy fajne fabularnie, ale słabo osadzone w Gileadzie lub sprzeczne z poprzednimi notatkami grupy.
3. **Brak jawnych kryteriów „grywalności” sceny**.
   - Opis może być klimatyczny, ale bez decyzji, stawek i konsekwencji.
4. **Brak standardu dla testów/mechaniki W&G**.
   - AI może podać niejednolite ST/konsekwencje lub pominąć mechaniczne wsparcie dla MG.
5. **Brak standardu „skalowania trudności”**.
   - Scenariusz może być zbyt ciężki lub zbyt łatwy dla konkretnego Tieru/Archetypów.

---

## Co dopisać do sekcji „Instrukcja dla AI” w `template.html`

Poniższe punkty warto dodać jako twarde reguły (najlepiej numerowane), żeby poprawić powtarzalność i jakość:

### 1) Obowiązkowy brief wejściowy (przed generacją)
Dodaj wymóg, że AI najpierw ma zebrać/uzupełnić zestaw danych:
- system i edycja (tu: Wrath & Glory),
- Tier drużyny,
- liczba graczy i dominujące archetypy,
- długość sesji (one-shot vs mini-kampania),
- procent walka/śledztwo/socjal,
- ton (grimdark, militarny, horror, polityka),
- ograniczenia treści (safety),
- dotychczasowy stan kampanii (co już zaszło).

### 2) Twarde zasady lore
- AI ma używać wyłącznie bytów/fakcji/lokacji zgodnych z Gilead.
- Każdy nowy element autorski ma być oznaczony jako „rozszerzenie lokalne” i nie może przeczyć znanym faktom.
- Jeśli brak pewności lore: AI ma oznaczyć punkt jako „do weryfikacji MG”.

### 3) Minimalny standard sceny (Definition of Done)
Każda scena musi zawierać:
- cel sceny,
- stawkę,
- co najmniej 2 decyzje graczy,
- min. 1 komplikację,
- konsekwencję sukcesu i porażki,
- wyraźne przejście do kolejnej sceny.

### 4) Standard mechaniczny W&G
W każdej scenie AI powinno podać:
- proponowane testy (Atrybut + Umiejętność),
- sugerowane ST,
- konsekwencje porażki (fail-forward),
- co daje wydanie Wrath/Glory,
- gdzie MG może użyć Ruin do eskalacji.

### 5) Skalowanie i warianty
Wymuś sekcję „Skalowanie”:
- wariant łatwiejszy,
- wariant standard,
- wariant trudniejszy,
- alternatywy dla drużyn bez silnego combatanta / bez tech-postaci / bez sociala.

### 6) Kontrola spójności linków i numeracji
Na końcu generacji AI ma wykonać mini-audyt:
- czy każde `H#` i `IL#` istnieje,
- czy każdy ma link zwrotny,
- czy nie ma duplikatów numeracji,
- czy sceny nie odwołują się do nieistniejących materiałów.

### 7) Odróżnienie „dla MG” vs „dla graczy”
Wymuś tagowanie treści:
- **[MG]** – informacje tajne,
- **[GRACZE]** – tekst do odczytu,
- **[MECHANIKA]** – testy, ST, konsekwencje.

To bardzo ogranicza chaos podczas prowadzenia.

### 8) Safety i komfort gry
Dodać regułę: AI ma proponować 3–5 potencjalnych trigger warningów i krótką sugestię użycia narzędzi bezpieczeństwa (np. Lines & Veils, X-card).

---

## Gotowy blok do wklejenia do „Instrukcja dla AI” (wersja skrócona)

1. Zanim uzupełnisz scenariusz, przygotuj „Brief wejściowy” i jeśli brakuje danych, wypisz brakujące pola.
2. Pilnuj spójności z lore Gilead; elementy autorskie oznaczaj jako „rozszerzenie lokalne”.
3. Każda scena musi mieć: cel, stawkę, decyzje graczy, komplikację, konsekwencje sukcesu/porażki i przejście dalej.
4. Do każdej sceny podawaj mechanikę W&G: testy, ST, fail-forward oraz punkty użycia Wrath/Glory/Ruin.
5. Dodawaj sekcję „Skalowanie” (łatwiej / standard / trudniej).
6. Po wygenerowaniu wykonaj audyt numeracji i linków H#/IL# oraz linków zwrotnych.
7. Oznaczaj treści jako [MG], [GRACZE], [MECHANIKA].
8. Uwzględniaj safety: potencjalne trigger warningi i rekomendowane narzędzia bezpieczeństwa.

---

## Propozycja procesu optymalnego (krok po kroku)

1. **Krok 0 — Brief kampanii (2–5 min):**
   MG wypełnia krótki formularz wejściowy (Tier, skład drużyny, ton, czas sesji).

2. **Krok 1 — Szkic szkieletu (AI):**
   AI tworzy tylko: tytuł, logline, sceny i zakończenia (bez detali).

3. **Krok 2 — Walidacja MG:**
   MG akceptuje strukturę i kierunek fabularny.

4. **Krok 3 — Wypełnienie scen (AI):**
   AI rozpisuje sceny + mechanikę + komplikacje + przejścia.

5. **Krok 4 — Materiały pomocnicze (AI):**
   NPC, handouty, ilustracje, powiązane linki.

6. **Krok 5 — Audyt automatyczny (AI):**
   checklista: lore, numeracja, linki, spójność nazw, skala trudności.

7. **Krok 6 — Finalny pass MG:**
   tylko poprawki autorskie i dostrojenie tempa.

Taki pipeline zwykle skraca liczbę poprawek i ogranicza „rozjazdy” między klimatem, mechaniką i linkowaniem.

---

## Sugestie dodatkowe (praktyczne)
- Trzymaj obok `template.html` mały plik `brief_scenariusza.md` z formularzem wejściowym.
- Dodaj „tag czasu sceny” (np. 20–30 min), żeby lepiej kontrolować sesję.
- Dodaj „Plan B”, gdy gracze ominą kluczową scenę.
- Dla przygód militarnych (jak Valkyria) dodaj licznik presji (np. „Alarm 0–6”), który rośnie po porażkach i wpływa na kolejne sceny.

---

## Wniosek końcowy
**Tak, ten zestaw plików jest wystarczający do przygotowania bardzo dobrego scenariusza.**
Największą poprawę jakości da dopisanie do „Instrukcji dla AI” reguł: brief wejściowy, walidacja lore, standard sceny, standard mechaniczny W&G oraz audyt końcowy spójności numeracji/linków. Dzięki temu proces będzie bardziej przewidywalny, szybszy i mniej podatny na błędy redakcyjne.
