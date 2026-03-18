# Analiza promptu do Codex i przyczyn rozjazdu względem `template.html`

## Prompt użytkownika

> Przeprowadź analizę i zapisz jej wyniki w Analizy/
>
> Przygotowałem taki prompt dla ChatGPT do modułu codex:
>
> ===
> Przeczytaj plik template.html a następnie:
>
> 1. Przeczytaj plik Warhammer40k/Scenariusz_Oko/old/Oko_09.html i utwórz nowy plik o nazwie Warhammer40k/Scenariusz_Oko/Oko_10.html
> Plik Warhammer40k/Scenariusz_Oko/Oko_10.html ma zawierać te same dane co Warhammer40k/Scenariusz_Oko/old/Oko_09.html, ale układ strony (jej wygląd itd.) ma być jak w template.html
> Chodzi mi głównie o numerację rzymską, tytuły scen na przyciskach nawigacji na panelu bocznym i wygląd przycisków do zmiany fontu  oraz tym, żeby wszystkie sekcje domyślnie były zwinięte.
>
> 2. Przeczytaj plik Warhammer40k/Scenariusz_Rico/old/Rico_09.html i utwórz nowy plik o nazwie Warhammer40k/Scenariusz_Rico/Rico_10.html
> Plik Warhammer40k/Scenariusz_Rico/Rico_10.html ma zawierać te same dane co Warhammer40k/Scenariusz_Rico/old/Rico_09.html, ale układ strony (jej wygląd itd.) ma być jak w template.html
> Chodzi mi głównie o numerację rzymską, tytuły scen na przyciskach nawigacji na panelu bocznym i wygląd przycisków do zmiany fontu  oraz tym, żeby wszystkie sekcje domyślnie były zwinięte.
>
> 3.  Przeczytaj plik Warhammer40k/Scenariusz_Epilog/old/Epilog_04.html i utwórz nowy plik o nazwie Warhammer40k/Scenariusz_Epilog/Epilog_05.html
> Plik Warhammer40k/Scenariusz_Epilog/Epilog_05.html ma zawierać te same dane co Warhammer40k/Scenariusz_Epilog/old/Epilog_04.html, ale układ strony (jej wygląd itd.) ma być jak w template.html
> Chodzi mi głównie o numerację rzymską, tytuły scen na przyciskach nawigacji na panelu bocznym i wygląd przycisków do zmiany fontu  oraz tym, żeby wszystkie sekcje domyślnie były zwinięte.
> ===
>
> Przeczytaj jeszcze raz pliki template.html oraz wszystkie wskazane i nowoutworzone pliki.
> Odpowiedz mi na pytanie, czemu te pliki nie trzymają się ściśle szablonu z template?
> Np. w pliki Oko nie ma kolorowych nagłówków w sekcji Handouty czy Ilustracje. Przyciski nawigacyjne w pliku Rico są w innym rozmiarze niż w template.html
>
> Sprawdź czemu. Czy coś jest źle zapisane w instrukcji dla AI? Czy coś źle w prompcie napisałem?

---

## Krótka odpowiedź

Tak — problem wynika **częściowo z promptu**, a **częściowo z błędnego wykonania przez AI**.

Najważniejsze przyczyny:

1. W punkcie 2 wskazany jest **nieistniejący plik źródłowy** `Warhammer40k/Scenariusz_Rico/old/Rico_09.html`.
2. Prompt mówi o tym, że układ ma być „jak w `template.html`”, ale **nie wymaga wiernego skopiowania struktury i stylów 1:1**.
3. Prompt wskazuje kilka elementów „głównie” (rzymska numeracja, tytuły scen, font buttons, sekcje zwinięte), więc AI mogło uznać, że **to są priorytety, a reszta szablonu może być tylko przybliżona**.
4. Co najmniej w `Rico_10.html` widać też zwykły błąd generacji / mieszanie kontekstu: plik Rico dostał tytuł z Epilogu.

---

## Co konkretnie nie trzyma się szablonu

### 1. `Oko_10.html` nie odwzorowuje sekcji `Ilustracje` i `Handouty` tak jak `template.html`

W `template.html` obie sekcje są zbudowane z kart wpisów (`entry-card`), tytułów z identyfikatorami (`mini-id`), metadanych (`entry-meta`) i linków zwrotnych (`tag`). To właśnie daje „kolorowe” / bardziej zaakcentowane nagłówki i ujednolicony wygląd wpisów. Widać to np. w sekcji `Ilustracje` i `Handouty`.  

Natomiast w `Oko_10.html` ta sama zawartość została wpisana jako proste bloki `div` typu `illustration` i `handout`, z prostymi nagłówkami `h4` i akapitami. AI przeniosło treść, ale nie zachowało pełnego komponentowego układu z szablonu. Efekt: sekcje są „w stylu template” tylko ogólnie, ale nie 1:1.

### 2. `Rico_10.html` ma inny wygląd przycisków nawigacyjnych niż `template.html`

W `template.html` klasa `.nav-link` ma jawnie ustawione `font-family: var(--font-navigation);`.  
W `Rico_10.html` ta linia zniknęła. Przez to linki nawigacyjne renderują się domyślnym krojem pisma zamiast krojem nawigacyjnym z template. Nawet przy tej samej wartości `font-size`, inny font daje inny wizualny rozmiar, szerokość i gęstość tekstu. To bardzo prawdopodobnie tłumaczy, czemu przyciski w Rico wyglądają na „inny rozmiar”.

### 3. `Rico_10.html` zawiera ślad pomieszania z Epilogiem

Już w nagłówku pliku `Rico_10.html` tytuł brzmi `Jądro Popiołu — Epilog kampanii`, co nie odpowiada plikowi Rico. To bardzo mocny sygnał, że model mieszał kontekst między zadaniem 2 i 3 albo skopiował fragment z niewłaściwego wyniku.

### 4. `Epilog_05.html` też nie jest wierną kopią stylu `template.html`

W `Epilog_05.html` podmieniono zestaw fontów z template na `Inter / Segoe UI / Roboto`, usunięto część zmiennych fontowych (`--font-heading`, `--font-navigation`, `--font-table`), a przez to zniknęły również przypisania tych fontów w wybranych sekcjach. To znaczy, że nawet tam, gdzie układ wygląda podobnie, nie jest to ścisłe trzymanie się szablonu.

---

## Co w promptcie jest problematyczne

### A. Najważniejszy błąd: zła ścieżka do Rico

W promptcie wpisano:

- `Warhammer40k/Scenariusz_Rico/old/Rico_09.html`

Taki plik **nie istnieje**. W katalogu `old` znajduje się `Rico_08.html`, a nie `Rico_09.html`.

To jest bardzo istotne, bo jeśli model nie znajdzie wskazanego pliku, może:

- zgadnąć, że chodziło o `Rico_08.html`,
- użyć innego podobnego pliku,
- albo zacząć mieszać zawartość z kolejnych poleceń.

To samo w sobie mogło już obniżyć jakość wyniku dla Rico.

### B. „Jak w template.html” jest za mało precyzyjne

Sformułowanie:

- „układ strony (jej wygląd itd.) ma być jak w `template.html`”

jest dla człowieka czytelne, ale dla modelu nadal dość szerokie. AI może to zinterpretować jako:

- „ma być podobny styl”,
- „ma używać `details/summary`”,
- „ma mieć sidebar i zwijane sekcje”,
- ale **niekoniecznie** „ma zachować wszystkie klasy CSS, wszystkie fonty, wszystkie komponenty i wszystkie drobne zależności 1:1”.

### C. Słowo „głównie” zawęża priorytet

Dopisek:

- „Chodzi mi głównie o numerację rzymską, tytuły scen na przyciskach nawigacji na panelu bocznym i wygląd przycisków do zmiany fontu oraz tym, żeby wszystkie sekcje domyślnie były zwinięte.”

sugeruje modelowi, że właśnie te elementy są najważniejsze. W praktyce model może potraktować resztę jako mniej istotną i pozwolić sobie na uproszczenia w innych obszarach, np. w kartach `Handouty` / `Ilustracje`, fontach, klasach CSS czy semantyce HTML.

### D. Brakuje wymogu „1:1” i listy zakazów

W promptcie nie ma wyraźnego warunku typu:

- „skopiuj strukturę CSS i HTML z `template.html` możliwie 1:1”,
- „nie wymyślaj nowych klas, jeśli istnieją odpowiedniki w template”,
- „sekcje `Ilustracje` i `Handouty` mają używać dokładnie tych samych komponentów co template: `entry-card`, `mini-id`, `entry-meta`, `tag`, `readaloud`, itd.”,
- „jeżeli jakiś styl z template nie pasuje do treści, zachowaj go mimo to i tylko podstaw dane”.

Bez takich warunków model często robi „transformację twórczą”, a nie „mechaniczne podstawienie treści do szablonu”.

### E. Brakuje kroku walidacyjnego

Prompt nie każe AI zrobić końcowego sprawdzenia w stylu:

- porównaj wygenerowany plik z `template.html`,
- wypisz wszystkie odstępstwa,
- popraw je tak, aby pozostały tylko treściowe różnice,
- upewnij się, że nie zmieniły się nazwy klas i definicje fontów.

Bez takiej walidacji model łatwo przepuszcza drobne rozjazdy.

---

## Co jest ewidentnie błędem AI, a nie Twojego promptu

Nie wszystko da się zrzucić na prompt. Kilka rzeczy wygląda po prostu na błąd wykonania:

1. `Rico_10.html` ma zły tytuł strony (`Jądro Popiołu — Epilog kampanii`).
2. `Rico_10.html` ma śmieciowy samotny znacznik `</p>` w sidebarze.
3. `Rico_10.html` i `Epilog_05.html` gubią część przypisań fontów z template mimo że prompt nie kazał ich usuwać.
4. `Epilog_05.html` zmienia rodzinę fontów na inną niż w template.

To są raczej objawy tego, że model nie wykonał zadania dostatecznie rygorystycznie.

---

## Dlaczego dokładnie w `Oko_10.html` nie ma tych „kolorowych nagłówków”

Najpewniej dlatego, że AI potraktowało sekcje `Handouty` i `Ilustracje` jako zwykłe listy zawartości do przepisania, a nie jako sekcje, które mają zachować **dokładnie te same komponenty wizualne co template**.

W template:

- wpisy są opakowane w `entry-card`,
- nagłówki mają `entry-title` + `mini-id`,
- są metadane `entry-meta`,
- są akcentowane linki `.tag`,
- jest ujednolicona kompozycja wpisu.

W `Oko_10.html`:

- wpisy są opakowane w własne klasy `illustration` i `handout`,
- nagłówki są prostymi `h4`,
- brak `mini-id`, `entry-meta`, `tag` i podobnych elementów w większości wpisów.

Czyli problem nie polega na tym, że CSS template „nie działa”, tylko że **HTML nie używa tych samych komponentów, które template zakłada**.

---

## Dlaczego dokładnie w `Rico_10.html` nawigacja wygląda inaczej

Najbardziej prawdopodobne przyczyny są dwie:

1. Usunięto `font-family: var(--font-navigation);` z `.nav-link`.
2. Usunięto `font-family: var(--font-heading);` z części nagłówków, co też zmienia odbiór całego sidebaru i hierarchii wizualnej.

Czyli rozmiar „wydaje się inny”, bo:

- użyty jest inny font,
- inny font ma inne proporcje znaków,
- tekst zajmuje inną szerokość i ma inny ciężar optyczny.

To jest bardziej problem wiernego odwzorowania stylu niż stricte wartości `font-size`.

---

## Jak poprawić prompt, żeby wynik był dużo bardziej przewidywalny

Poniżej wersja zasad, które warto dopisać.

### Wersja krótsza

- Użyj `template.html` jako bazy 1:1 dla struktury HTML i CSS.
- Zachowaj wszystkie klasy, style, fonty i komponenty z `template.html`, chyba że zmiana jest absolutnie konieczna do wstawienia danych.
- Do nowego pliku wstaw tylko treść z pliku źródłowego, ale nie zmieniaj architektury szablonu.
- Sekcje `Ilustracje` i `Handouty` muszą używać dokładnie tych samych komponentów co w template (`entry-card`, `entry-title`, `mini-id`, `entry-meta`, `tag`, `readaloud` itd.).
- Panel boczny ma zachować identyczne style jak w template, łącznie z rodzinami fontów dla `.nav-link`, nagłówków i przycisków.
- Wszystkie sekcje `details` mają być domyślnie zamknięte.
- Po wygenerowaniu wykonaj kontrolę końcową: porównaj nowy plik z `template.html` i popraw wszystkie różnice stylistyczne, które nie wynikają bezpośrednio z podmiany treści.

### Wersja jeszcze lepsza: rozbij zadanie

Zamiast jednego dużego promptu dla trzech plików, lepiej robić:

1. Jeden prompt = jeden plik.
2. Po wygenerowaniu każ AI wypisać listę różnic względem template.
3. Potem dopiero poproś o poprawki.

To zmniejsza ryzyko mieszania kontekstu między Oko / Rico / Epilogiem.

---

## Proponowana poprawiona wersja Twojego promptu

Przykład dla jednego pliku:

> Przeczytaj `template.html` oraz `Warhammer40k/Scenariusz_Oko/old/Oko_09.html`.  
> Utwórz nowy plik `Warhammer40k/Scenariusz_Oko/Oko_10.html`.  
> 
> Wymagania:
> 1. Nowy plik ma zawierać te same dane merytoryczne co plik źródłowy.  
> 2. Struktura HTML, klasy CSS, style, fonty, komponenty sekcji i układ strony mają być zachowane możliwie 1:1 z `template.html`.  
> 3. Nie twórz własnych zamienników klas, jeśli w `template.html` istnieje już odpowiedni komponent.  
> 4. Sekcje `Ilustracje` i `Handouty` mają zachować dokładnie ten sam typ wpisów i wizualnych komponentów co w `template.html` (np. `entry-card`, `entry-title`, `mini-id`, `entry-meta`, `tag`, `readaloud`).  
> 5. Panel boczny ma zachować dokładnie style z `template.html`, w tym fonty dla nawigacji i przycisków.  
> 6. Numeracja scen w sidebarze ma być rzymska.  
> 7. Tytuły scen w sidebarze mają odpowiadać tytułom sekcji.  
> 8. Wszystkie sekcje `details` mają być domyślnie zwinięte.  
> 9. Na końcu sprawdź wygenerowany plik i wypisz, czy są jakiekolwiek różnice stylistyczne względem `template.html` poza podmianą treści. Jeśli są, popraw je.

---

## Wniosek końcowy

Twoja intencja w promptcie jest zrozumiała, ale prompt nie wymusza wystarczająco mocno odwzorowania `template.html` **1:1**. Do tego w części Rico jest realny błąd w ścieżce do pliku źródłowego (`Rico_09.html` nie istnieje), a sam model dodatkowo popełnił kilka własnych błędów wykonawczych i pomieszał kontekst między plikami.

### Ostateczna odpowiedź na pytanie „czy coś źle napisałem?”

**Tak, ale tylko częściowo.**

Najważniejsze rzeczy do poprawy po Twojej stronie:

1. popraw ścieżkę do Rico,
2. zamień „jak w template” na „zachowaj strukturę, klasy i style 1:1 z template”,
3. usuń słowo „głównie”, jeśli zależy Ci na pełnej zgodności,
4. dodaj krok walidacji końcowej,
5. najlepiej generuj każdy plik osobnym promptem.

Najważniejsze rzeczy, które były błędem AI:

1. pomieszanie tytułów między Rico i Epilogiem,
2. gubienie części deklaracji fontów,
3. uproszczenie sekcji `Handouty` i `Ilustracje` w `Oko_10.html`,
4. pozostawienie artefaktów HTML jak samotne `</p>`.
