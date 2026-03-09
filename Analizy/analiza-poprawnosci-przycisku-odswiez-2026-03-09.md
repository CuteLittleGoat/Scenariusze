# Analiza poprawności działania przycisku „Odśwież”

## Prompt użytkownika
> Przeprowadź analizę poprawności działania przycisku Odśwież.
> Obecnie kolejno wyświetlają się statusy:
> Status: gotowe do odświeżenia.
> Status: generowanie nowego manifestu.
> coś-tam z endpoint (nie zdążyłem przyczytać)
> Status: odświeżono z istniejącego manifestu (9.03.2026, 12:52:30).

## Wniosek skrócony
Sekwencja statusów, którą opisałeś, jest **zgodna z aktualną logiką aplikacji** i najpewniej oznacza, że:
1. aplikacja próbowała wywołać lokalny endpoint generujący nowy manifest,
2. endpoint był niedostępny (lub środowisko nie pozwalało na wywołanie),
3. zadziałał mechanizm fallback do istniejącego `files-manifest.json`,
4. lista została poprawnie odświeżona z ostatnio wygenerowanych danych.

Czyli: to wygląda bardziej na **działanie zapasowe (fallback)** niż na błąd krytyczny.

## Co dokładnie robi kod przy kliknięciu „Odśwież”
W `refreshFileList()` przebieg jest następujący:

1. Ustawienie statusu: „generowanie nowego manifestu...”
2. Próba `POST` na endpointach:
   - `/refresh-manifest`
   - `./refresh-manifest`
3. Jeżeli generacja się powiedzie:
   - odczyt świeżego `files-manifest.json`,
   - status końcowy: „wygenerowano i odświeżono manifest (...)”.
4. Jeżeli endpoint lokalny nie działa:
   - status pośredni: „brak lokalnego endpointu, próba odczytu aktualnej listy z GitHub API...”,
   - próba fallbacku do GitHub API.
5. Jeżeli GitHub API też nie zadziała lub nie jest możliwe:
   - status: „odczytywanie istniejącego manifestu...”,
   - odczyt lokalnego `files-manifest.json`,
   - status końcowy: „odświeżono z istniejącego manifestu (...)”.

## Interpretacja Twojej obserwacji
Twoja kolejność statusów bardzo dobrze pasuje do ścieżki:

- „gotowe do odświeżenia” (stan początkowy),
- „generowanie nowego manifestu” (start próby),
- „coś z endpoint” (najpewniej komunikat o braku lokalnego endpointu),
- „odświeżono z istniejącego manifestu (...)” (fallback zakończony powodzeniem).

To oznacza, że przycisk **działa poprawnie funkcjonalnie** (odświeżenie nastąpiło), ale najpewniej **nie nastąpiło wygenerowanie nowego manifestu na serwerze**.

## Co warto sprawdzić operacyjnie
Aby mieć „pełne” odświeżenie (z nową generacją manifestu), potrzebny jest backend obsługujący `POST /refresh-manifest`.

Do sprawdzenia:
1. Czy aplikacja działa w środowisku z serwerem, który wystawia endpoint `/refresh-manifest`.
2. Czy endpoint zwraca status 200 dla metody POST.
3. Czy po wywołaniu endpointu aktualizuje się fizycznie plik `files-manifest.json`.

## Sugestia UX
Warto skrócić i uprościć status pośredni, np.:
- „Brak lokalnego generatora manifestu — używam danych zapasowych.”

Dzięki temu użytkownik szybciej zrozumie, że to kontrolowany fallback, a nie awaria aplikacji.
