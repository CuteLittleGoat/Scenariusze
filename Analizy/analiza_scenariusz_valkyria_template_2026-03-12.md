# Analiza: przygotowanie scenariusza na bazie `template.html`, `Gilead.html` i `Na_Skrzydalach_Valkyrii.pdf`

## Prompt użytkownika (pierwotny)
> Przeprowadź analizę.
> Mając do dyspozycji pliki:
> template.html
> Warhammer40k/Gilead/Gilead.html
> Warhammer40k/TA_02/Na_Skrzydalach_Valkyrii.pdf
>
> Jesteś w stanie przygotować scenariusz do przygody? Czy jakieś dodatkowe instrukcje/wytyczne można zawrzeć w pliku template.html w sekcji "Instrukcja dla AI"? Masz jakieś sugestie i propozycje co zrobić, żeby cały proces przebiegał optymalnie?

## Prompt użytkownika (aktualizacja 2026-03-12)
> Zaktualizuj analizę Analizy/analiza_scenariusz_valkyria_template_2026-03-12.md o poniższe dane:
> 
> A. Najważniejsze braki / ryzyka przy automatycznym tworzeniu scenariuszy
> 1. Mam plik z notatkami Warhammer40k/Notatki/Notatki.md
> 2. plik z notatkami chyba rozwiązuje ten problem?
> 3. Rozwiń ten punkt, żebym dobrze go zrozumiał
> 4 i 5 - to celowy zabieg. Ten template i mechanizm ma być uniwersalny a nie tylko do jednego systemu. Rzeczy stricte mechaniczne (statystyki, rzuty) MG dopisuje samodzielnie - takie jest założenie. Napisz czy należy to dopisać do instrukcji.
> 
> B. Co dopisać do sekcji „Instrukcja dla AI” w template.html
> 1. Część już chyba wyjaśniłem w punkcie A.
> 2. To raczej powinna być część promptu, np. "Piszę scenariusz w settingu Warhammer 40k. Sprawdź spójność z lore". Template ma być uniwersalny dla wielu settingów to nie powinno się tego dopisywać do instrukcji dla ai.
> 3. Tu mam inną koncepcję. Niektóre sceny mogą być czysto narracyjne - np. przejście przez ciemny korytarz i opis migających świateł i odgłosu łopatek wentylatora dla zbudowania napięcia grozy
> 4. Jak już pisałem to nie wchodzi w grę. Template ma być uniwersalny a rzeczy mechaniczne ma dopisać MG.
> 
> C. 7) Odróżnienie „dla MG” vs „dla graczy”
> Z opisanych powodów odrzucamy [MECHANIKA]. Jak proponujesz zmienić template? Obecnie jest już "sekcja dla graczy".
> 
> D. 8) Safety i komfort gry
> To już MG musi dopasować do własnej drużyny. AI nie może nigdy decydować o treściach.
> 
> Podsumowania:
> template ma służyć do wielu sesji w różnych settingach. Niektóre przygody będą miały gotowy scenariusz (jak przykładowy PDF) i będą wymagały tylko przeredagowania. Inne będą od zera budowane w trakcie rozmowy z asystentem AI, jeszcze inne będą się opierać o chaotyczne zapiski MG i asystent AI będzie musiał je dopasować do template.
> 
> Mając to na uwadze zaktualizuj analizę.

---

## Krótka odpowiedź po aktualizacji
Tak — po uwzględnieniu Twoich założeń nadal da się bardzo skutecznie generować scenariusze, ale **template powinien jasno wymuszać rozdział**:
1) co ma robić AI (struktura, redakcja, spójność),
2) co zostaje po stronie MG (mechanika systemowa, safety, ostateczny dobór treści).

Najważniejsza zmiana względem poprzedniej wersji: template ma być **system-agnostyczny**, więc instrukcje nie mogą być „zaszyte” pod W&G.

---

## A. Najważniejsze braki / ryzyka — aktualizacja

### 1) „Mam plik z notatkami `Warhammer40k/Notatki/Notatki.md`”
To bardzo mocno poprawia jakość generowania, bo daje AI kontekst kampanii: co już zaszło, kogo gracze znają, jakie były konsekwencje wcześniejszych działań.

### 2) „Czy plik z notatkami rozwiązuje problem?”
**Rozwiązuje dużą część problemu spójności kampanii, ale nie 100%.**
- Rozwiązuje: ciągłość wydarzeń drużyny, powracające postacie, unikanie jawnych sprzeczności z historią stołu.
- Nie rozwiązuje automatycznie: jakości notatek (mogą być skrótowe), pełnej spójności z szerokim lore settingu, ani decyzji projektowych MG (tempo, ton, ciężar scen).

Wniosek: notatki są kluczowym źródłem wejściowym, ale i tak warto dodać prostą regułę „w razie niepewności oznacz do decyzji MG”.

### 3) Rozwinięcie punktu o „grywalności sceny”
To nie musi oznaczać „mechaniki”. Chodzi o to, żeby scena była używalna przy stole, a nie tylko ładna literacko.

Dobra scena (nawet czysto narracyjna) powinna mieć:
- **cel sceny** (po co istnieje w przygodzie),
- **funkcję dramaturgiczną** (np. budowanie napięcia, zwolnienie tempa po walce, sygnał zagrożenia),
- **punkt decyzyjny lub kierunkowy** (co najmniej jedna decyzja graczy albo świadome przejście do kolejnego etapu),
- **efekt po scenie** (co się zmienia: wiedza, nastrój, relacje, pozycja bohaterów).

Czyli Twój przykład „ciemny korytarz + dźwięki wentylatora” jak najbardziej ma sens, o ile ma rolę w strukturze przygody, a nie jest wyłącznie ozdobnikiem.

### 4–5) Brak mechaniki i skalowania jako zabieg celowy
Przyjmuję i potwierdzam: przy Twoim celu (uniwersalność template) to jest sensowne.

**Czy dopisać to do instrukcji? — Tak, zdecydowanie.**
Wprost, jedną krótką zasadą, np.:
> „Template jest niezależny od systemu. AI nie generuje statystyk, testów i rzutów, chyba że MG wyraźnie o to poprosi.”

To utnie nieporozumienia i utrzyma jednolity styl pracy.

---

## B. Co dopisać do „Instrukcja dla AI” — wersja zgodna z Twoją koncepcją

1. **Brief wejściowy** — zostaje (bo to uniwersalne i poprawia jakość).
2. **Lore konkretnego settingu** — przenosimy do promptu sesyjnego MG (nie do stałej instrukcji template).
3. **Sceny narracyjne** — dopisujemy jawnie, że są dozwolone i pożądane tam, gdzie służą tempu/nastrojowi.
4. **Mechanika** — zostaje po stronie MG (domyślnie AI jej nie dopisuje).

---

## C. Odróżnienie „dla MG” vs „dla graczy” (bez `[MECHANIKA]`)
Skoro odrzucamy tag `[MECHANIKA]`, proponuję prosty, czytelny standard dwublokowy:

- **[DLA MG]** — informacje ukryte, intencje sceny, prawdziwe motywacje NPC, możliwe konsekwencje.
- **[DLA GRACZY]** — opis do odczytania / parafrazy przy stole.

Dodatkowo (opcjonalnie) można dodać lekki znacznik techniczny:
- **[NOTATKA ROBOCZA MG]** — krótkie checklisty prowadzenia sceny (bez statystyk i rzutów).

To zachowuje Twoją zasadę „zero mechaniki w template”, a jednocześnie porządkuje użycie materiału podczas sesji.

---

## D. Safety i komfort gry
Pełna zgoda z Twoją decyzją: AI nie powinno decydować o granicach treści za drużynę.

Najlepsza wersja do template (minimalna i bez narzucania):
> „Asystent AI nie ustala samodzielnie granic treści. Kwestie komfortu i bezpieczeństwa gry każdorazowo określa MG w porozumieniu z graczami.”

To wystarczy jako reguła odpowiedzialności.

---

## Rekomendowany zestaw zapisów do `template.html` (krótka, uniwersalna wersja)
1. Najpierw przygotuj krótki brief wejściowy; jeśli brakuje danych, wypisz pytania do MG.
2. Template jest system-agnostyczny: nie dodawaj mechaniki (statystyk, testów, rzutów), chyba że MG wyraźnie o to poprosi.
3. Twórz zarówno sceny decyzyjne, jak i narracyjne — każda scena ma mieć cel i efekt dla dalszego przebiegu przygody.
4. Rozdzielaj treści na `[DLA MG]` i `[DLA GRACZY]`.
5. Gdy materiał wejściowy jest niejednoznaczny lub sprzeczny, oznacz punkt jako „do decyzji MG”.
6. Nie ustalaj samodzielnie zasad safety/komfortu — to decyzja MG i grupy.

---

## Jak to wspiera trzy tryby pracy, które opisałeś
1. **Przeredagowanie gotowego scenariusza (np. PDF):** AI mapuje istniejący materiał do struktury template.
2. **Tworzenie od zera w rozmowie:** AI prowadzi przez brief → szkic → pełną wersję.
3. **Praca na chaotycznych notatkach MG:** AI porządkuje i uzupełnia luki, ale oznacza miejsca wymagające decyzji MG.

Dzięki temu jeden template działa w wielu settingach i wielu stylach przygotowania sesji, bez „wpychania” mechaniki systemowej tam, gdzie nie jest pożądana.
