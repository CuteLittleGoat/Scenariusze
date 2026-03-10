# Analiza błędu przycisku „Odśwież” – HTTP 405

## Prompt użytkownika
"Nie wprowadzaj zmian w kodzie. Przeprowadź analizę.
Teraz pojawia się błąd: Status: nie udało się odświeżyć listy plików (backend refresh nie działa (405))."

## Kontekst
Po ostatniej zmianie kliknięcie przycisku „Odśwież” wykonuje najpierw żądanie `POST /refresh-manifest`, a dopiero później pobiera `files-manifest.json`.

## Co oznacza błąd 405
HTTP 405 = "Method Not Allowed" (metoda niedozwolona). W praktyce dla tego przypadku oznacza to, że serwer, z którego faktycznie korzysta UI, **nie przyjmuje metody POST** na endpoint odświeżania.

## Najbardziej prawdopodobna przyczyna
1. Frontend został przygotowany pod lokalny serwer `Main/local_server.py`, który obsługuje `POST /refresh-manifest`.
2. U Ciebie UI działa najpewniej na innym hostingu / innym serwerze statycznym (np. prosty static server, Pages, reverse proxy), który:
   - albo w ogóle nie ma endpointu `/refresh-manifest`,
   - albo nie zezwala na metodę POST,
   - albo ma reguły routingu blokujące to żądanie.
3. Skutek: kliknięcie „Odśwież” kończy się 405 zanim dojdzie do odczytu świeżego manifestu.

## Dlaczego wcześniej wyglądało, że „działa”
Wcześniej przycisk odświeżał tylko odczyt istniejącego JSON (bez przebudowy). Teraz próbuje uruchomić backendowy refresh, ale środowisko runtime nie dostarcza takiego backendu (lub nie dopuszcza POST), więc problem ujawnia się natychmiast.

## Potwierdzenie techniczne (na podstawie kodu repo)
- Frontend wysyła `POST` do `/refresh-manifest`.
- Lokalny serwer w repo (`Main/local_server.py`) przewiduje ten endpoint i metodę POST/GET.
- Jeżeli aplikacja nie działa pod tym serwerem, endpoint może nie istnieć lub metoda POST może być zablokowana.

## Rekomendowane rozwiązanie docelowe (1 klik = pełne odświeżenie)
### Wariant A (najprostszy operacyjnie)
Uruchamiać UI zawsze przez backend, który obsługuje `/refresh-manifest` (np. `Main/local_server.py` lub jego produkcyjny odpowiednik).

**Przebieg po kliknięciu:**
1. UI: `POST /refresh-manifest`.
2. Backend: uruchamia generator manifestu.
3. Backend: zapisuje nowy `files-manifest.json`.
4. UI: pobiera JSON i renderuje nową listę plików.

### Wariant B (jeśli hosting jest statyczny)
Dodać cienką warstwę backendową (serverless/API) do obsługi odświeżania:
- endpoint `POST /refresh-manifest` wywołuje skan repo / skrypt,
- zapisuje wynik do miejsca dostępnego dla UI,
- UI pozostaje „jedno kliknięcie”.

### Wariant C (gdy nie można mieć backendu synchronicznego)
Automatyzacja asynchroniczna:
- nowy plik -> webhook/CI -> automatyczna regeneracja manifestu,
- przycisk „Odśwież” tylko pobiera najnowszy gotowy JSON.

## Dodatkowe zalecenia jakościowe
1. Dodać diagnostykę statusu środowiska (np. "tryb statyczny / brak backend refresh").
2. Dla 405 zwracać użytkownikowi komunikat wskazujący brak obsługi POST na serwerze.
3. Spiąć monitoring: logowanie kodów odpowiedzi dla `/refresh-manifest`.

## Wniosek
Błąd 405 nie wynika z samego mechanizmu listowania plików, tylko z niedopasowania między frontendem oczekującym backendowego endpointu POST a środowiskiem uruchomieniowym, które tej metody/ścieżki nie obsługuje. Aby zachować wymaganie „jedno kliknięcie = pełne odświeżenie”, trzeba zapewnić realnie działający endpoint backendowy w docelowym środowisku (lub równoważną automatyzację po stronie CI/API).
