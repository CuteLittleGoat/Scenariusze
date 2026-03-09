# Analiza: automatyczne odświeżanie zawartości folderów w `Main/index.html`

## Prompt użytkownika
> Czy da się zrobić, żeby plik Main/index.html automatycznie odświeżał zawartość plików we wskazanych folderach? Przeprowadź analizę takiego rozwiązania.

## Krótka odpowiedź
Tak — **ale nie w 100% w samym statycznym HTML uruchamianym lokalnie z `file://`**. 
Aby lista plików odświeżała się automatycznie, potrzebujesz warstwy, która potrafi odczytać katalogi (backend/skrypt generujący indeks) i przekazać wynik do `Main/index.html`.

## Dlaczego obecny `Main/index.html` tego nie robi
Aktualny plik zawiera ręcznie wpisane wiersze tabel z konkretnymi plikami. To oznacza, że po dodaniu nowego pliku w folderze trzeba ręcznie dopisać kolejny `<tr>...</tr>`.

Dodatkowo przeglądarka (JavaScript po stronie klienta) z powodów bezpieczeństwa:
- nie ma swobodnego dostępu do systemu plików,
- nie może „przeskanować” dowolnych folderów repo i odczytać ich listy plików bezpośrednio.

## Realne warianty wdrożenia

### Wariant A (najprostszy i najpewniejszy): generator `index.html`
1. Tworzysz skrypt (np. Python/Node), który:
   - czyta wskazane foldery (`Analizy`, `Warhammer40k/...`),
   - buduje sekcje i wiersze tabel,
   - nadpisuje `Main/index.html`.
2. Uruchamiasz skrypt ręcznie lub automatycznie (np. Git hook, CI).

**Zalety:**
- brak potrzeby serwera aplikacyjnego,
- działa z obecnym stylem „statycznego archiwum”,
- prosta kontrola nad kolejnością i filtrowaniem plików.

**Wady:**
- odświeżenie nie jest „na żywo” bez uruchomienia skryptu,
- trzeba pilnować procesu aktualizacji.

### Wariant B: lekki backend API + dynamiczny frontend
1. Uruchamiasz mały serwer (np. Node/Express, Python/Flask/FastAPI).
2. Endpoint `/api/files` zwraca JSON z listą plików dla zdefiniowanych folderów.
3. `Main/index.html` pobiera dane przez `fetch()` i renderuje tabelę JS-em.
4. Auto-refresh:
   - polling co np. 30–60 s, albo
   - Server-Sent Events / WebSocket.

**Zalety:**
- prawdziwe automatyczne odświeżanie,
- brak ręcznej edycji listy plików.

**Wady:**
- trzeba utrzymywać proces backendu,
- większa złożoność niż statyczny HTML.

### Wariant C: skrypt + watcher katalogów (półautomatyczny live)
1. Jak w wariancie A, ale skrypt działa w trybie watch (nasłuch zmian).
2. Przy zmianie plików automatycznie regeneruje `Main/index.html`.
3. Opcjonalnie live-reload strony (narzędzie deweloperskie).

**Zalety:**
- bardzo wygodne w pracy lokalnej,
- nadal bez pełnego backendu aplikacyjnego.

**Wady:**
- to rozwiązanie głównie developerskie,
- produkcyjnie i tak finalnie publikujesz wygenerowany plik.

## Rekomendacja dla tego repozytorium
Dla charakteru repo („baza scenariuszy”) najlepszy kompromis to:
1. **Wariant A** jako baza (generator indeksu),
2. opcjonalnie **watch mode** z wariantu C dla wygody edycji.

Dzięki temu zachowujesz prostotę statycznych plików, a lista w `Main/index.html` jest zawsze spójna z zawartością katalogów po uruchomieniu generatora.

## Minimalny plan wdrożenia
1. Zdefiniować mapę sekcji i folderów źródłowych.
2. Napisać skrypt generujący sekcje `<details>` i wiersze `<tr>`.
3. Dodać komendę uruchomieniową (np. `python scripts/generate_index.py`).
4. (Opcjonalnie) dodać tryb watch.
5. Ustalić sortowanie i filtr (np. tylko `.md`, `.html`, `.txt`).

## Ryzyka i niuanse
- Spójność nazw plików i rozszerzeń (w obecnym indeksie widać ręczne rozjazdy typu `.md` vs `.html`).
- Kolejność wyświetlania (alfabetycznie, po dacie, niestandardowo).
- Linki względne muszą być liczone względem `Main/index.html`.

## Wniosek końcowy
Technicznie jest to jak najbardziej wykonalne, ale wymaga choć minimalnej automatyzacji poza samym statycznym HTML. Najpraktyczniej wdrożyć generator indeksu (ew. z watch mode), zamiast budować pełny backend.
