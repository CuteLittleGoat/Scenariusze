# Analiza: nowe rozwiązanie dla przycisku „Odśwież” (jeden przycisk, pewne odświeżenie UI)

## Prompt użytkownika
> Przeczytaj pliki w Analizy. Potem przeprowadź nową analizę.
> Przycisk Odśwież cały czas nie działa.
> Zaproponuj nowe rozwiązanie, które będzie skutkowało odświeżeniem danych w UI po naciśnięciu jednego przycisku.

## Kontekst po przeglądzie wcześniejszych analiz
W dotychczasowych analizach przewija się ten sam problem: logika „Odśwież” jest zależna od mechanizmów, które nie zawsze są dostępne w przeglądarce lub środowisku uruchomienia (np. File System Access API albo lokalny endpoint generujący manifest).

To powoduje sytuację, w której użytkownik klika jeden przycisk, ale efekt bywa losowy (działa tylko fallback do starego manifestu albo pojawia się błąd o braku API).

## Główny cel nowego podejścia
Zapewnić, że **jedno kliknięcie przycisku zawsze odświeża UI** w przewidywalny sposób, bez uzależnienia od niedostępnych funkcji przeglądarki.

## Proponowane rozwiązanie (rekomendowane)

### „Single-button refresh” oparty na jednym źródle prawdy: `files-manifest.json`

Zamiast próbować przy każdym kliknięciu skanować dysk z poziomu przeglądarki:

1. Źródłem danych dla UI jest wyłącznie `Main/files-manifest.json`.
2. Przycisk „Odśwież” w UI robi tylko:
   - cache-busting fetch (np. `files-manifest.json?ts=...`),
   - re-render listy plików,
   - komunikat statusu z timestampem z manifestu.
3. Aktualizacja manifestu odbywa się niezależnie od UI:
   - skrypt `Main/generate-manifest.*` (node/python),
   - opcjonalny watcher (`--watch`) do pracy lokalnej.

W efekcie przycisk zawsze robi to samo i nie zależy od File System Access API.

---

## Dlaczego to będzie działać stabilniej

- `fetch` JSON działa przewidywalnie w normalnym uruchomieniu przez lokalny serwer HTTP.
- Brak krytycznej zależności od `showDirectoryPicker` i uprawnień do systemu plików.
- Jeden kontrakt danych: UI renderuje strukturę manifestu; nie obchodzi go mechanizm skanowania folderów.
- Proste debugowanie: jeśli UI nie odświeża, porównujesz tylko odpowiedź HTTP i zawartość JSON.

## Projekt przepływu „jednego przycisku”

### Po stronie UI (`Main/index.html`)
Przycisk „Odśwież” uruchamia:
1. `setStatus("Odświeżanie...")`
2. `GET ./files-manifest.json?ts=<Date.now()>`
3. Walidacja minimalna (`sections`, `generatedAt`)
4. Render tabel
5. `setStatus("Odświeżono: <generatedAt>")`

### Po stronie danych (`Main/generate-manifest.*`)
Skrypt:
1. skanuje zdefiniowane foldery,
2. filtruje rozszerzenia,
3. zapisuje `Main/files-manifest.json` z polem `generatedAt`.

Przykładowy kształt:
```json
{
  "generatedAt": "2026-03-09T13:10:00Z",
  "sections": [
    {
      "id": "analizy",
      "title": "Analizy",
      "files": [
        { "name": "analiza-x.md", "path": "../Analizy/analiza-x.md" }
      ]
    }
  ]
}
```

## Co z wymaganiem „po naciśnięciu jednego przycisku”
Jeśli wymaganie dotyczy wyłącznie UX („jeden klik w UI ma odświeżyć listę”), to powyższy model je spełnia:
- użytkownik klika „Odśwież”,
- UI pobiera najnowszy dostępny manifest,
- lista natychmiast się aktualizuje.

Dla pełnej „świeżości” danych (także nowych plików dodanych sekundę temu) warto uruchamiać generator manifestu automatycznie w tle (watcher lokalny), ale nie musi to być część samego kliknięcia w przeglądarce.

## Alternatywa, jeśli koniecznie „klik” ma też wymuszać nowy skan folderów
Można dodać lokalny mini-serwer (np. Node/Python) z endpointem:
- `POST /refresh-manifest` → generuje nowy JSON,
- następnie UI robi `GET /files-manifest.json?ts=...`.

Wciąż jeden przycisk, ale już z wymaganiem uruchomionego procesu lokalnego. To podejście jest bardziej „live”, ale bardziej złożone operacyjnie.

## Rekomendacja końcowa
Najbezpieczniejszy i najmniej awaryjny wariant:
1. Ujednolicić odświeżanie UI do samego `fetch(files-manifest.json)`.
2. Usunąć krytyczną zależność od File System Access API z głównej ścieżki.
3. Utrzymywać aktualność manifestu skryptem (manualnie lub watcherem).

To da przewidywalne działanie przycisku „Odśwież” i realne odświeżanie widoku po jednym kliknięciu.
