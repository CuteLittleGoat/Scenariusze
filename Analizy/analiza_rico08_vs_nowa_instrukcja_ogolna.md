# Analiza: czy da się przygotować scenariusze na poziomie `Rico_08.html` przy nowej instrukcji ogólnej

## Prompt użytkownika

> Przeprowadź analizę czy byłbyś w stanie przygotować scenariusze jak Rico_08.html gdyby w instrukcje do AI w template był poniższy tekst (w instrukcjach do scenariusza jest to co obecnie w Rico_08.html):
> 
> [tu użytkownik wkleił pełną, 18-punktową „Instrukcję ogólną” obejmującą m.in. hierarchię instrukcji, nienaruszalność layoutu HTML, neutralność systemową, zgodność settingową, reguły scen, NPC, przeciwników, ilustracji/handoutów, notatek MG i oczekiwany efekt końcowy]

## Krótka odpowiedź

Tak — **byłbym w stanie przygotować scenariusze jak `Rico_08.html`** przy takiej instrukcji ogólnej, pod warunkiem, że zachowana zostanie deklarowana w niej hierarchia (polecenie użytkownika > instrukcja scenariusza > instrukcja ogólna).

## Dlaczego odpowiedź brzmi „tak”

1. Nowa instrukcja ogólna jest bardzo precyzyjna i operacyjna.
2. Wprost wymusza użyteczność dla MG, spójność, kontrolę odnośników i trzymanie funkcji sekcji.
3. Zawiera regułę hierarchii, która pozwala utrzymać specyficzne założenia scenariusza (`Rico_08.html`) nawet wtedy, gdy globalne zasady są bardziej ogólne lub nieco inne.
4. Ogranicza „samowolę” AI (layout/design, sekcje instrukcyjne, mechanika systemowa), co zwykle poprawia przewidywalność i jakość materiału.

## Co może się zmienić względem obecnego stylu pracy

### 1) Większa rygorystyczność techniczna
Nowa instrukcja mocniej blokuje modyfikacje warstwy technicznej HTML. To jest korzystne dla stabilności template’u, ale wymaga pilnowania, by wszystkie rozbudowy treści mieściły się w istniejącej strukturze.

### 2) Silniejsza neutralność mechaniczna
Bez wyraźnej prośby użytkownika nie powinny pojawiać się konkretne mechaniki (ST/DC/statystyki/HP itd.). To jest spójne z profesjonalnym template’em wielosystemowym i nie blokuje tworzenia scenariuszy klasy `Rico_08`.

### 3) Twardsze zasady sekcji „Przeciwnicy”
Nowa instrukcja ogólna narzuca konkretny format tej sekcji (nazwa + opis + przycisk „Otwórz statystyki”, domyślnie bez linku). To da się pogodzić z praktyką, ale może lokalnie kolidować ze starszymi instrukcjami scenariuszowymi.

## Potencjalne punkty konfliktu i jak je rozwiązać

1. **Konflikt „Przeciwnicy”**
   - Nowa ogólna instrukcja: sekcja ma działać wg wzoru „Oko Płomiennej Pomsty” i zawierać przeciwników ze scenariusza.
   - W `Rico_08` (obecna instrukcja scenariuszowa): AI nie powinno samodzielnie uzupełniać tej sekcji bez danych od użytkownika.
   - Rozwiązanie: stosować hierarchię — instrukcja scenariusza (wyższa) wygrywa z ogólną.

2. **Konflikt „co wolno dodać”**
   - Ogólna instrukcja pozwala dodawać elementy tylko gdy potrzebne dla spójności/użyteczności.
   - Jeśli instrukcja scenariusza precyzuje bardziej szczegółowe wymogi (np. konkretne bloki, styl, lokalne reguły linkowania), należy trzymać się tej lokalnej specyfikacji.

3. **Nienaruszalność sekcji instrukcyjnych**
   - To dobra zasada, ale trzeba pilnować, by model nie „poprawiał” instrukcji przy okazji edycji treści scenariusza.

## Ocena końcowa (praktyczna)

**Ocena: wykonalne i sensowne.**

Przy takim zestawie zasad da się tworzyć materiały jakości `Rico_08.html`, a nawet bardziej przewidywalne redakcyjnie. Kluczowe są:

- konsekwentne trzymanie hierarchii instrukcji,
- kontrola spójności odnośników i numeracji,
- rozdzielenie warstwy treści od warstwy technicznej,
- pilnowanie, by sekcje służyły MG operacyjnie, a nie tylko literacko.

## Rekomendacja wdrożeniowa

Aby zminimalizować błędy przy wielu scenariuszach, warto dodać krótką checklistę końcową (do użytku AI lub redakcji), np.:

1. Czy wszystkie linki scena ↔ handout/ilustracja są dwustronne i aktualne?
2. Czy żadna sekcja nie zawiera treści niezgodnej z jej funkcją?
3. Czy nie dodano mechaniki systemowej bez wyraźnej prośby?
4. Czy nie zmieniono layoutu/klas/ID/skryptów poza dozwolonym wyjątkiem?
5. Czy „Instrukcja ogólna dla AI” i „Instrukcja scenariusza” pozostały nienaruszone?

Taka checklista ułatwi utrzymanie jakości przy kolejnych plikach w stylu `Rico_08`.
