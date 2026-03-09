# Analiza problemu: `template.html` — brak działania zmiany fontu na mobile

## Prompt użytkownika
> Przeprowadź analizę kodu pliku template.html
> W wersji mobilnej nie działa powiększanie i pomniejszanie fontu. W wersji PC działa prawidłowo. Co jest przyczyną? Jak to naprawić, żeby nie popsuć funkcjonalności na PC?

## Diagnoza przyczyny
Problem wynika z konfliktu reguł CSS, a nie z błędu JavaScript.

1. W bazowej regule `.content` rozmiar czcionki jest sterowany zmienną CSS:
   - `font-size: var(--content-font-size);`
2. Funkcja JS (`changeFontSize`) zmienia właśnie tę zmienną:
   - `--content-font-size`
3. Jednak w media query dla mobile (`@media (max-width: 720px)`) `.content` dostaje sztywną wartość:
   - `font-size: 17px;`

Efekt: na mobile reguła z media query nadpisuje mechanizm oparty o zmienną, więc przyciski `Font ▲/▼` zmieniają zmienną, ale nie wpływają już na realny `font-size` elementu `.content`.

## Dlaczego na PC działa
Na desktopie reguła mobile (`max-width: 720px`) nie jest aktywna, więc `.content` używa `font-size: var(--content-font-size)` i zmiana zmiennej przez JS działa poprawnie.

## Jak naprawić bez psucia PC
Najbezpieczniejsza poprawka:

1. **Nie nadpisywać `font-size` na sztywno w media query mobile.**
2. Jeśli potrzebujesz innego startowego rozmiaru na mobile (np. 17px), ustaw **zmienną**, a nie bezpośrednio `font-size`.

### Rekomendowany wariant CSS
```css
/* baza zostaje */
.content {
  font-size: var(--content-font-size);
}

@media (max-width: 720px) {
  :root {
    --content-font-size: 17px; /* mobilny punkt startowy */
  }

  .content {
    font-size: var(--content-font-size); /* zamiast 17px na sztywno */
  }
}
```

### Dodatkowa uwaga do JS
Obecnie JS ma twardy fallback `18`:
```js
const defaultSize = savedSize ? parseFloat(savedSize) : 18;
```
Jeśli chcesz, żeby domyślna wartość szanowała CSS (w tym mobile 17px), lepiej pobierać fallback z `getComputedStyle` dla `--content-font-size`.

Przykład idei:
```js
const cssDefault = parseFloat(getComputedStyle(document.documentElement)
  .getPropertyValue("--content-font-size")) || 18;
const defaultSize = savedSize ? parseFloat(savedSize) : cssDefault;
```

## Podsumowanie
- Przyczyna: mobile media query ustawia `.content { font-size: 17px; }`, co odcina mechanizm oparty o `--content-font-size`.
- Naprawa: na mobile operować dalej na `--content-font-size` (ew. ustawić tam wartość 17px), nie na sztywnej wartości `font-size`.
- Dzięki temu PC zachowa aktualne działanie, a mobile odzyska działające `Font ▲/▼`.
