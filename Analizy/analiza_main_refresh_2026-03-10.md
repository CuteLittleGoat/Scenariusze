# Analiza działania przycisku „Odśwież” (folder `Main`)

## Prompt użytkownika

> Przeprowadź analizę plików w folderze Main.
> Sprawdź działanie przycisku "Odśwież".
> Przycisk obecnie nie działa. Wyświetla komunikat: Status: pobrano aktualny manifest: 10.03.2026, 07:34:07.
> Nie odświeżają się dane.
> Zaproponuj inne rozwiązanie. Coś co by sprawiło, że jednym przyciśnięciem przycisku "Odśwież" w odpowiednich zwijanych sekcjach strony by się pojawiały nowe pliki wraz z przyciskiem do otworzenia.
> Obecny mechanizm w żaden sposób nie działa. Po wielu analizach i poprawkach cały czas nie działa.
> Zaproponuj jakieś inne rozwiązanie, które pozwoliłby uzyskać efekt aktualizacji listy plików.

---

## Co robi obecna implementacja

1. Przycisk `Odśwież` uruchamia `refreshFileList()` w `Main/index.html`.
2. Funkcja **próbuje** najpierw wywołać backend `POST /refresh-manifest` (`triggerManifestRefresh()`), ale tylko jeśli `canUseBackendRefresh()` zwróci `true`.
3. `canUseBackendRefresh()` przepuszcza tylko uruchomienie przez `http(s)` i host `localhost/127.0.0.1/::1`.
4. Następnie frontend zawsze czyta `./files-manifest.json` z parametrem `?ts=...`.
5. Pliki pokazywane są tylko z gotowego JSON-a (`files-manifest.json`), który musi być wcześniej wygenerowany przez `generate_manifest.py`.

## Dlaczego widzisz komunikat „pobrano aktualny manifest...” i brak nowych danych

To zachowanie oznacza, że:

- backendowy refresh **nie został uruchomiony** (najczęściej strona nie działa na `localhost`, albo nie działa skrypt serwera Python),
- frontend jedynie pobrał istniejący `files-manifest.json`, który nie zawiera nowych plików,
- sam parametr `?ts=...` omija cache, ale **nie tworzy nowej zawartości manifestu**.

Krótko: przycisk odświeża tylko odczyt, nie źródło danych (jeśli nie ma lokalnego backendu).

---

## Proponowane inne rozwiązanie (działające w hostingu statycznym)

Najbardziej niezawodne rozwiązanie bez lokalnego Pythona:

## Opcja A (rekomendowana): odczyt plików bezpośrednio z API GitHub

### Założenie
Repo jest na GitHubie. Frontend po kliknięciu „Odśwież” pobiera listę plików dla każdej sekcji bezpośrednio z API GitHub (`/repos/{owner}/{repo}/contents/{path}`), zamiast czytać lokalny manifest.

### Efekt
- Jedno kliknięcie odświeża listy w `details`.
- Nowe pliki pojawiają się od razu po pushu do repo (bez ręcznego generowania JSON).
- Nie potrzeba endpointu `/refresh-manifest` ani lokalnego serwera Python do aktualizacji list.

### Szkic działania
1. W `sectionConfig` zostają ścieżki katalogów (jak teraz).
2. `refreshFileList()` dla każdej sekcji wywołuje `fetch` do GitHub API.
3. Odfiltrowuje rozszerzenia (`.html`, `.md`, `.txt`, `.png`).
4. Renderuje w tabeli nazwę + przycisk `Otwórz` do `download_url` lub linku do pliku w repo.
5. Pokazuje status z godziną odświeżenia.

### Zalety
- Działa na GitHub Pages i innym hostingu statycznym.
- Nie wymaga backendu na serwerze docelowym.
- Eliminuje problem „manifest stary mimo kliknięcia”.

### Ryzyka / uwagi
- Limit API GitHub dla niezalogowanych (zwykle wystarczający dla ręcznego odświeżania).
- Trzeba znać `owner/repo/branch`.

---

## Opcja B: automatyczne generowanie manifestu w CI (GitHub Actions)

Jeżeli chcesz zachować manifest:

1. Każdy push uruchamia workflow, który odpala `Main/generate_manifest.py`.
2. Workflow commit/publishuje nowy `Main/files-manifest.json`.
3. Przycisk `Odśwież` dalej czyta manifest, ale ten jest zawsze aktualny po pushu.

To też działa w hostingu statycznym, ale dane odświeżą się dopiero po zakończeniu workflow (nie „na żywo” z dysku użytkownika).

---

## Rekomendacja końcowa

Jeżeli celem jest „jedno kliknięcie i widać nowe pliki” bez utrzymywania backendu: **Opcja A (GitHub API)**.

Jeżeli chcesz minimalnych zmian w frontendzie i możesz dodać CI: **Opcja B (manifest generowany automatycznie przez GitHub Actions)**.

W obu przypadkach obecny endpoint `/refresh-manifest` warto zostawić tylko jako tryb lokalny developerski, a nie mechanizm główny.
