# Analiza działania przycisku „Odśwież” i błąd File System Access API

## Prompt użytkownika
> Przeprowadź analizę działania przycisku "Odśwież". Aplikacja zwraca błąd "Status: przeglądarka nie obsługuje File System Access API."
> Zaproponuj alternatywne rozwiązania.
> Efektem oczekiwanym jest, żeby użytkownik mógł nacisnąć przycisk a aplikacja wyświetliła listę plików w danych folderach.
> Nie chcę żadnego łączenia z Firebase itp. Wszystko ma się odbywać tylko przy użyciu plików i skryptów jakie możesz utworzyć w Main/

## Co obecnie robi przycisk „Odśwież”
W `Main/index.html` przycisk wywołuje `refreshFileList()`, które:
1. Sprawdza wsparcie `showDirectoryPicker`.
2. Jeśli API nie istnieje, kończy działanie komunikatem:
   `Status: przeglądarka nie obsługuje File System Access API.`
3. Jeśli API istnieje, prosi użytkownika o wybór katalogu głównego repo (`Scenariusze`), następnie próbuje czytać wskazane foldery i renderuje listy plików.

## Dlaczego pojawia się błąd
Błąd pojawia się, bo aplikacja jest oparta wyłącznie o File System Access API, które:
- działa tylko w części przeglądarek (głównie Chromium),
- często wymaga uruchomienia strony w **secure context** (np. `https://` albo `http://localhost`),
- nie działa w wielu scenariuszach uruchamiania lokalnego (np. część przypadków `file://` lub przeglądarki bez implementacji API).

W efekcie przycisk nie ma ścieżki awaryjnej i cała funkcja odświeżania jest zablokowana.

## Alternatywy bez Firebase i bez zewnętrznej bazy
Poniżej opcje zgodne z wymaganiem „tylko pliki i skrypty w `Main/`”.

### Opcja A (rekomendowana): manifest JSON generowany skryptem lokalnym
**Idea:**
- Tworzysz skrypt (np. `Main/generate-manifest.js` lub `.py`), który skanuje foldery i zapisuje `Main/files-manifest.json`.
- Przycisk „Odśwież” w UI robi `fetch('./files-manifest.json')` i renderuje dane.

**Plusy:**
- działa w praktycznie każdej przeglądarce,
- brak zależności od File System Access API,
- prosta diagnostyka (widać gotowy JSON).

**Minusy:**
- żeby mieć najnowsze dane, trzeba przed odświeżeniem uruchomić skrypt generujący manifest.

**Wariant ulepszony:**
- dodać `Main/refresh.ps1` / `Main/refresh.sh`, który jednym poleceniem generuje manifest i uruchamia prosty serwer lokalny.

---

### Opcja B: fallback przez `<input type="file" webkitdirectory>`
**Idea:**
- Gdy `showDirectoryPicker` nie jest dostępne, kliknięcie „Odśwież” otwiera ukryty input z wyborem folderu.
- Użytkownik wskazuje katalog, a aplikacja czyta listę plików z `FileList` i `webkitRelativePath`.

**Plusy:**
- bezpośrednio z poziomu przeglądarki, bez API `showDirectoryPicker`,
- bez dodatkowego backendu i bez chmury.

**Minusy:**
- API `webkitdirectory` też nie jest idealnie jednolite między przeglądarkami,
- zwykle mniej wygodne UX niż natywny directory picker,
- nadal zależne od wyraźnego wyboru folderu przez użytkownika.

---

### Opcja C: statyczny indeks plików utrzymywany ręcznie
**Idea:**
- Trzymasz plik `Main/files-manifest.json` aktualizowany ręcznie (lub półautomatycznie).
- Przycisk tylko odczytuje i renderuje ten plik.

**Plusy:**
- najprostsze technicznie i najbardziej przenośne.

**Minusy:**
- duże ryzyko rozjazdu indeksu i faktycznego stanu repo.

## Rekomendowana architektura końcowa
Najbardziej praktyczne jest połączenie:
1. **Priorytet:** `showDirectoryPicker` (jeśli dostępne).
2. **Fallback 1:** `webkitdirectory`.
3. **Fallback 2:** `files-manifest.json` (ostatnia znana lista).

Dzięki temu przycisk „Odśwież” prawie zawsze zwróci listę plików, a nie błąd o braku API.

## Minimalny plan wdrożenia (Main/)
1. Dodać skrypt generujący `Main/files-manifest.json` ze strukturą odpowiadającą `sectionConfig`.
2. W `refreshFileList()`:
   - jeśli jest `showDirectoryPicker` → obecna ścieżka,
   - w przeciwnym razie próbować fallback z input directory,
   - jeśli fallback nie zadziała lub użytkownik anuluje → odczytać manifest JSON.
3. Dodać czytelne statusy, np.:
   - „Odświeżono z lokalnego folderu”,
   - „Odświeżono z manifestu (tryb kompatybilny)”.

## Odpowiedź na wymaganie użytkownika
Tak, wymagany efekt („użytkownik naciska przycisk i widzi listę plików”) można osiągnąć **bez Firebase i bez zewnętrznej bazy**, wyłącznie przez pliki i skrypty w `Main/`, najlepiej przez manifest + fallback.
