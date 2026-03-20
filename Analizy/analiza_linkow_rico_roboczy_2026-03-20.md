# Analiza odwołań i hiperłączy — `Warhammer40k/Scenariusz_Rico/Rico_roboczy.html`

## Prompt użytkownika
> Przeanalizuj plik Warhammer40k/Scenariusz_Rico/Rico_roboczy.html
>
> Sprawdź mi plik pod kątem odwołań i hiperłączy. Czy nie ma jakiś błędów? Odwołania powinny przenosić tylko do Handout i Ilustracji użytych w danej scenie. Przy danym Handout i Ilustracji powinien być odnośnik prowadzący do sceny.Sprawdź mi plik pod kątem odwołań i hiperłączy. Czy nie ma jakiś błędów? Odwołania powinny przenosić tylko do Handout i Ilustracji użytych w danej scenie. Przy danym Handout i Ilustracji powinien być odnośnik prowadzący do sceny.

## Zakres sprawdzenia
Sprawdziłem:
1. czy wszystkie wewnętrzne linki `href="#..."` wskazują na istniejące `id`,
2. czy scena linkuje wyłącznie do handoutów i ilustracji przypisanych do tej sceny,
3. czy każdy handout i każda ilustracja mają link zwrotny do sceny/scen, w których występują,
4. czy istnieją niespójności pomiędzy sekcją scen a kartami w sekcjach `Ilustracje` i `Handouty`.

## Wynik ogólny
- Nie znalazłem linków prowadzących do nieistniejących anchorów (`id`).
- Większość powiązań scena ↔ materiał jest spójna i działa dwukierunkowo.
- Znalazłem **jedną merytoryczną niespójność**: `H11` jest przypisany do Sceny IX w sekcji handoutów, ale **Scena IX nie linkuje do `#handout-h11`**.

## Wykryty problem
### 1. Brak linku do `H11` w Scenie IX
W Scenie IX sekcja „Handouty używane w tej scenie” zawiera wpis `Brak`, mimo że niżej istnieje karta `H11`, która jest oznaczona jako materiał występujący właśnie w Scenie IX i zawiera link powrotny do tej sceny.

### Szczegóły
- W `Scenie IX` wpisano brak handoutów.
- Karta `H11` istnieje i prowadzi z powrotem do `#scena-9`.
- To łamie oczekiwaną zasadę dwustronnego powiązania scena ↔ handout.

## Miejsca w pliku wymagające uwagi
- `Scena IX`:
  - sekcja „Handouty używane w tej scenie” pokazuje `Brak`.
- `H11`:
  - karta wskazuje, że materiał występuje w `Scenie IX` i ma poprawny link zwrotny.

## Rekomendowana poprawka
W `Scenie IX` warto zamienić:
- `Brak`

na:
- link do `H11`, czyli `href="#handout-h11"`.

## Powiązania, które wyglądają poprawnie
Poniższe wielokrotne powiązania są spójne w obie strony:
- `H5` ↔ Sceny V, VIII, XIII,
- `H10` ↔ Sceny VIII, X, XIII,
- `IL8` ↔ Sceny VIII, XI, XII, XIII,
- `IL10` ↔ Sceny X, XI,
- `H12` ↔ Scena XII,
- `IL11` ↔ Scena XIII.

## Podsumowanie
Na poziomie technicznym anchory są poprawne, ale na poziomie logiki odwołań jest jedna niespójność:
- **brakuje linku ze Sceny IX do handoutu `H11`**, mimo że sam handout jest przypisany do tej sceny i odsyła do niej poprawnie.
