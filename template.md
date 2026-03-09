<!--- https://raw.githubusercontent.com/cutelittlegoat/Scenariusze/main/template.md --->

<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Template scenariusza TTRPG</title>
  <style>
    :root {
      --bg: #0b0f14;
      --bg-2: #111821;
      --panel: #131b24;
      --panel-2: #18222d;
      --panel-3: #0f151d;
      --text: #dce6f1;
      --muted: #93a3b5;
      --accent: #7fc8ff;
      --accent-2: #89e0c2;
      --border: #243140;
      --border-strong: #324557;
      --shadow: rgba(0, 0, 0, 0.42);
      --sidebar-w: 290px;
      --content-font-size: 18px;
    }

    * {
      box-sizing: border-box;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      margin: 0;
      background:
        radial-gradient(circle at top left, rgba(127, 200, 255, 0.08), transparent 28%),
        radial-gradient(circle at bottom right, rgba(137, 224, 194, 0.05), transparent 22%),
        linear-gradient(180deg, var(--bg), #080b10 100%);
      color: var(--text);
      font-family: Inter, Segoe UI, Roboto, Arial, sans-serif;
      line-height: 1.7;
      font-size: 18px;
    }

    a {
      color: inherit;
    }

    .layout {
      display: flex;
      min-height: 100vh;
    }

    .sidebar {
      position: sticky;
      top: 0;
      align-self: flex-start;
      width: var(--sidebar-w);
      height: 100vh;
      padding: 18px;
      border-right: 1px solid var(--border);
      background:
        linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0)),
        rgba(9, 13, 18, 0.92);
      backdrop-filter: blur(10px);
      overflow-y: auto;
      flex: 0 0 var(--sidebar-w);
      font-size: 18px;
    }

    .sidebar-card {
      background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.015));
      border: 1px solid var(--border);
      border-radius: 20px;
      box-shadow: 0 18px 40px var(--shadow);
      padding: 18px;
    }

    .sidebar h2 {
      margin: 0 0 6px;
      font-size: 1.05rem;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: var(--muted);
    }

    .sidebar-intro {
      margin: 0 0 14px;
      color: var(--muted);
      font-size: 0.95rem;
      line-height: 1.45;
    }

    .toolbar {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 16px;
      padding: 10px 12px;
      background: rgba(255,255,255,0.03);
      border: 1px solid var(--border);
      border-radius: 14px;
    }

    .toolbar span {
      color: var(--muted);
      font-size: 0.92rem;
    }

    .toolbar button {
      width: 34px;
      height: 34px;
      border-radius: 10px;
      border: 1px solid var(--border);
      background: var(--panel-2);
      color: var(--text);
      cursor: pointer;
      transition: 0.2s ease;
      font-size: 1rem;
    }

    .toolbar button:hover {
      border-color: var(--accent);
      color: var(--accent);
      transform: translateY(-1px);
      box-shadow: 0 0 0 4px rgba(127, 200, 255, 0.08);
    }

    .nav-group {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .nav-link {
      display: block;
      text-decoration: none;
      padding: 11px 13px;
      border-radius: 12px;
      border: 1px solid transparent;
      color: var(--text);
      background: transparent;
      transition: 0.2s ease;
      font-size: 0.98rem;
    }

    .nav-link:hover {
      background: rgba(255,255,255,0.035);
      border-color: var(--border);
      color: var(--accent);
      transform: translateX(2px);
    }

    .nav-link.is-main {
      background: rgba(127, 200, 255, 0.06);
      border-color: rgba(127, 200, 255, 0.14);
    }

    .nav-divider {
      height: 1px;
      margin: 14px 0;
      background: linear-gradient(90deg, transparent, var(--border-strong), transparent);
    }

    .content {
      flex: 1;
      min-width: 0;
      padding: 26px 24px 70px 24px;
      font-size: var(--content-font-size);
    }

    .content-inner {
      width: 100%;
      max-width: none;
      margin: 0;
    }

    .hero,
    details,
    .ai-instruction-box {
      background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.015));
      border: 1px solid var(--border);
      border-radius: 18px;
      box-shadow: 0 18px 40px var(--shadow);
    }

    .hero {
      padding: 30px 28px;
      margin-bottom: 22px;
      position: relative;
      overflow: hidden;
    }

    .hero::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(circle at top right, rgba(127, 200, 255, 0.09), transparent 25%),
        radial-gradient(circle at bottom left, rgba(137, 224, 194, 0.06), transparent 20%);
      pointer-events: none;
    }

    .hero > * {
      position: relative;
      z-index: 1;
    }

    .hero h1 {
      margin: 0 0 12px;
      font-size: 2.15em;
      line-height: 1.1;
      letter-spacing: -0.02em;
    }

    .lead {
      color: var(--muted);
      margin: 0;
      max-width: none;
    }

    details {
      margin-bottom: 18px;
      overflow: hidden;
    }

    summary {
      list-style: none;
      cursor: pointer;
      padding: 20px 24px;
      user-select: none;
      background: linear-gradient(180deg, rgba(255,255,255,0.015), rgba(255,255,255,0));
      transition: 0.2s ease;
    }

    summary::-webkit-details-marker {
      display: none;
    }

    details[open] summary {
      border-bottom: 1px solid var(--border);
      background: linear-gradient(180deg, rgba(127, 200, 255, 0.05), rgba(255,255,255,0));
    }

    .summary-top {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 16px;
    }

    .summary-title {
      margin: 0;
      font-size: 1.35em;
      line-height: 1.2;
      letter-spacing: -0.01em;
    }

    .summary-desc {
      margin: 8px 0 0;
      color: var(--muted);
    }

    .chevron {
      color: var(--accent);
      font-size: 1.2em;
      transition: transform 0.2s ease;
      flex: 0 0 auto;
      padding-top: 2px;
    }

    details[open] .chevron {
      transform: rotate(180deg);
    }

    .section-body {
      padding: 22px;
      background: rgba(255,255,255,0.01);
    }

    .block {
      margin-bottom: 18px;
      padding: 18px;
      border: 1px solid var(--border);
      border-radius: 16px;
      background:
        linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)),
        var(--panel);
      box-shadow: inset 0 1px 0 rgba(255,255,255,0.02);
    }

    .block:last-child {
      margin-bottom: 0;
    }

    .block h3 {
      margin: 0 0 10px;
      font-size: 1.04em;
      color: var(--accent-2);
      letter-spacing: 0.01em;
    }

    .block p,
    .block li {
      margin-top: 0;
    }

    .block ul,
    .block ol {
      margin: 0;
      padding-left: 24px;
    }

    .muted {
      color: var(--muted);
    }

    .example {
      margin-top: 12px;
      padding: 14px 16px;
      border-radius: 14px;
      background: rgba(255,255,255,0.03);
      border: 1px dashed var(--border-strong);
    }

    .small-label {
      display: block;
      margin-bottom: 8px;
      color: var(--muted);
      font-size: 0.84em;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .link-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .tag {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 34px;
      padding: 6px 11px;
      border-radius: 999px;
      border: 1px solid var(--border);
      background: rgba(127, 200, 255, 0.08);
      color: var(--accent);
      text-decoration: none;
      font-size: 0.9em;
      transition: 0.2s ease;
    }

    .tag:hover {
      border-color: var(--accent);
      background: rgba(127, 200, 255, 0.14);
      transform: translateY(-1px);
    }

    .table-wrap {
      overflow-x: auto;
      border: 1px solid var(--border);
      border-radius: 14px;
      background: var(--panel-3);
    }

    table {
      width: 100%;
      min-width: 760px;
      border-collapse: collapse;
    }

    th,
    td {
      padding: 14px 16px;
      text-align: left;
      vertical-align: top;
      border-right: 1px solid var(--border);
      border-bottom: 1px solid var(--border);
    }

    th:last-child,
    td:last-child {
      border-right: none;
    }

    tbody tr:last-child td {
      border-bottom: none;
    }

    th {
      background: rgba(255,255,255,0.04);
      color: var(--accent-2);
      font-size: 0.98em;
    }

    .button-placeholder {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 38px;
      padding: 8px 14px;
      border-radius: 11px;
      border: 1px solid var(--border);
      background: linear-gradient(180deg, rgba(127, 200, 255, 0.12), rgba(127, 200, 255, 0.04));
      color: var(--text);
      cursor: pointer;
      transition: 0.2s ease;
      user-select: none;
    }

    .button-placeholder:hover {
      border-color: var(--accent);
      color: var(--accent);
      transform: translateY(-1px);
    }

    .entry-card {
      margin-bottom: 16px;
      padding: 16px;
      border: 1px solid var(--border);
      border-radius: 16px;
      background:
        linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)),
        var(--panel-3);
    }

    .entry-card:last-child {
      margin-bottom: 0;
    }

    .entry-title {
      margin: 0 0 8px;
      font-size: 1.05em;
      color: var(--accent);
    }

    .entry-meta {
      margin-bottom: 12px;
      color: var(--muted);
    }

    .mini-id {
      display: inline-block;
      margin-right: 8px;
      color: var(--accent);
      font-size: 0.86em;
      font-weight: 700;
      letter-spacing: 0.04em;
    }

    .readaloud {
      padding: 14px 16px;
      border-left: 4px solid var(--accent);
      border-radius: 12px;
      background: rgba(127, 200, 255, 0.08);
      box-shadow: inset 0 1px 0 rgba(255,255,255,0.03);
    }

    .ai-instruction-box {
      margin-top: 26px;
      padding: 14px;
      background: #0a0d12;
    }

    .ai-instruction-title {
      margin: 0 0 8px;
      font-size: 14px;
      color: #748190;
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }

    .ai-instruction-content {
      font-size: 1px !important;
      line-height: 1.2;
      color: #808b97;
      white-space: pre-wrap;
      word-break: break-word;
      user-select: text;
    }

    @media (max-width: 1100px) {
      .layout {
        display: block;
      }

      .sidebar {
        position: sticky;
        top: 0;
        width: 100%;
        height: auto;
        max-height: 55vh;
        border-right: none;
        border-bottom: 1px solid var(--border);
        z-index: 40;
      }

      .content {
        padding: 20px 16px 60px;
      }
    }

    @media (max-width: 720px) {
      .content {
        font-size: 17px;
      }

      .hero {
        padding: 24px 20px;
      }

      .hero h1 {
        font-size: 2em;
      }

      summary {
        padding: 18px 18px;
      }

      .section-body {
        padding: 16px;
      }

      .summary-title {
        font-size: 1.15em;
      }

      table {
        min-width: 620px;
      }
    }
  </style>
</head>
<body>
  <div class="layout">
    <aside class="sidebar" aria-label="Panel nawigacyjny scenariusza">
      <div class="sidebar-card">
        <h2>Nawigacja scenariusza</h2>
        <p class="sidebar-intro">
          Szybkie przejścia między scenami i sekcjami pomocniczymi.
        </p>

        <div class="toolbar">
          <span>Rozmiar tekstu</span>
          <button type="button" onclick="changeFontSize(1)" aria-label="Powiększ tekst">▲</button>
          <button type="button" onclick="changeFontSize(-1)" aria-label="Pomniejsz tekst">▼</button>
        </div>

        <nav class="nav-group">
          <a class="nav-link is-main" href="#wprowadzenie">Wprowadzenie</a>
          <a class="nav-link is-main" href="#scena-1">Scena 1</a>
          <a class="nav-link is-main" href="#scena-2">Scena 2</a>
          <a class="nav-link is-main" href="#scena-3">Scena 3</a>
          <a class="nav-link is-main" href="#zakonczenie">Zakończenie</a>

          <div class="nav-divider"></div>

          <a class="nav-link" href="#przeciwnicy">Przeciwnicy</a>
          <a class="nav-link" href="#npc">NPC</a>
          <a class="nav-link" href="#ilustracje">Ilustracje</a>
          <a class="nav-link" href="#handouty">Handouty</a>
        </nav>
      </div>
    </aside>

    <main class="content" id="contentArea">
      <div class="content-inner">

        <section class="hero" id="wprowadzenie">
          <h1>Tytuł scenariusza</h1>
          <p class="lead">
            Tutaj wpisz krótki opis całego scenariusza: klimat, gatunek, główny konflikt, stawkę oraz to,
            dlaczego ta przygoda jest interesująca dla drużyny. Ten akapit powinien dawać MG szybki podgląd
            całości jeszcze przed czytaniem poszczególnych scen.
          </p>

          <div class="block" style="margin-top:20px;">
            <h3>Skrót scenariusza</h3>
            <p>
              W tej sekcji wpisz zwięzłe podsumowanie całej przygody w kilku akapitach. Opisz:
              jaki jest punkt wyjścia, co uruchamia akcję, jakie są najważniejsze zwroty fabularne,
              do czego prowadzą kolejne sceny oraz jaki typ finału przewiduje scenariusz.
              To ma być skrót dla MG, który pozwala szybko przypomnieć sobie przebieg całej sesji.
            </p>
          </div>
        </section>

        <details open id="scena-1">
          <summary>
            <div class="summary-top">
              <div>
                <h2 class="summary-title">Scena 1 — Tytuł sceny</h2>
                <p class="summary-desc">
                  Tutaj wpisz krótki opis roli tej sceny: otwarcie przygody, pierwsze spotkanie, śledztwo,
                  eksploracja, walka, negocjacje albo wprowadzenie konfliktu.
                </p>
              </div>
              <span class="chevron">▼</span>
            </div>
          </summary>

          <div class="section-body">
            <div class="block">
              <h3>Streszczenie sceny</h3>
              <p>
                Tutaj wpisz jedno konkretne streszczenie tej sceny. Opisz, po co scena istnieje,
                co mają z niej wynieść gracze, jaki jest jej główny konflikt oraz do jakiej kolejnej sceny
                lub decyzji ma prowadzić. To ma być szybki skrót dla MG.
              </p>
            </div>

            <div class="block" id="scena-1-dla-graczy">
              <h3>Sekcja dla Graczy</h3>
              <p>
                Tutaj wpisz treści przeznaczone bezpośrednio do przedstawienia graczom, na przykład opisy
                lokacji do odczytania przez MG, pierwsze wrażenia, narracyjne wejście do sceny, krótkie
                opisy wydarzeń albo informacje, które mają wybrzmieć w formie gotowego tekstu mówionego.
              </p>
              <div class="readaloud">
                <strong>Przykład formy:</strong><br />
                „Gdy wchodzicie do wnętrza budynku, czujecie zapach wilgoci i starego kurzu. Z głębi
                korytarza dobiega metaliczny stukot, a w świetle waszych latarek drżą długie cienie.”
              </div>
            </div>

            <div class="block">
              <h3>Scena Krok-po-kroku</h3>
              <p class="muted">
                W tym miejscu rozpisz scenę jako prostą sekwencję zdarzeń. Dzięki temu podczas prowadzenia sesji
                łatwo kontrolować tempo, kolejność ujawniania informacji i możliwe reakcje świata na działania graczy.
              </p>
              <div class="example">
                <ol>
                  <li>Graczy spotykają NPC1</li>
                  <li>NPC1 mówi graczom X</li>
                  <li>Gracze znajdują Y</li>
                </ol>
              </div>
            </div>

            <div class="block">
              <h3>Powiązane materiały</h3>
              <span class="small-label">Handouty używane w tej scenie</span>
              <div class="link-row">
                <a class="tag" href="#handout-h1">H1</a>
                <a class="tag" href="#handout-h2">H2</a>
              </div>

              <span class="small-label" style="margin-top:16px;">Ilustracje używane w tej scenie</span>
              <div class="link-row">
                <a class="tag" href="#ilustracja-il1">IL1</a>
                <a class="tag" href="#ilustracja-il2">IL2</a>
              </div>
            </div>

            <div class="block">
              <h3>Co ma się znaleźć w tej sekcji</h3>
              <ul>
                <li>opis miejsca akcji i jego atmosfery,</li>
                <li>co gracze widzą, słyszą i mogą od razu zrobić,</li>
                <li>jakie informacje można tutaj zdobyć,</li>
                <li>jakich NPC można tu spotkać,</li>
                <li>jakie testy, przeszkody, zagrożenia lub konflikty mogą się pojawić,</li>
                <li>jakie ilustracje są potrzebne do tej sceny, oznaczone numerami IL1, IL2, IL3 itd.,</li>
                <li>jakie handouty można tu zdobyć lub wykorzystać, oznaczone numerami H1, H2, H3 itd.,</li>
                <li>co się stanie, jeśli gracze odniosą sukces,</li>
                <li>co się stanie, jeśli gracze zawiodą, zignorują trop albo pójdą inną drogą,</li>
                <li>dokąd ta scena powinna prowadzić dalej.</li>
              </ul>
            </div>
          </div>
        </details>

        <details id="scena-2">
          <summary>
            <div class="summary-top">
              <div>
                <h2 class="summary-title">Scena 2 — Tytuł sceny</h2>
                <p class="summary-desc">
                  Tutaj wpisz krótki opis tego, jak ta scena rozwija sytuację: eskaluje zagrożenie,
                  ujawnia nowe informacje, zmienia kierunek śledztwa albo prowadzi do większego konfliktu.
                </p>
              </div>
              <span class="chevron">▼</span>
            </div>
          </summary>

          <div class="section-body">
            <div class="block">
              <h3>Streszczenie sceny</h3>
              <p>
                W tej sekcji wpisz krótki opis celu sceny, głównego napięcia oraz tego, z czym gracze powinni
                z niej wyjść: nową wiedzą, nowym zagrożeniem, nowym przeciwnikiem, ważnym wyborem albo dostępem
                do kolejnej części scenariusza.
              </p>
            </div>

            <div class="block" id="scena-2-dla-graczy">
              <h3>Sekcja dla Graczy</h3>
              <p>
                Tutaj wpisz teksty, które MG może odczytać graczom albo sparafrazować przy stole.
                To dobre miejsce na opisy pomieszczeń, nastroju, spotkań, odkryć, wizji, odgłosów
                i innych elementów, które mają wywołać określone wrażenie po stronie drużyny.
              </p>
              <div class="readaloud">
                <strong>Przykład formy:</strong><br />
                „Wąski korytarz kończy się ciężkimi drzwiami. Na metalu ktoś wyrył serię płytkich,
                nerwowych nacięć, jakby próbował zaznaczyć kolejne dni albo godziny.”
              </div>
            </div>

            <div class="block">
              <h3>Scena Krok-po-kroku</h3>
              <p class="muted">
                Rozpisz tutaj logiczną kolejność wydarzeń w scenie. Możesz potraktować tę listę jako plan bazowy,
                od którego łatwo odbić w improwizację.
              </p>
              <div class="example">
                <ol>
                  <li>Graczy spotykają NPC1</li>
                  <li>NPC1 mówi graczom X</li>
                  <li>Gracze znajdują Y</li>
                </ol>
              </div>
            </div>

            <div class="block">
              <h3>Powiązane materiały</h3>
              <span class="small-label">Handouty używane w tej scenie</span>
              <div class="link-row">
                <a class="tag" href="#handout-h2">H2</a>
                <a class="tag" href="#handout-h3">H3</a>
              </div>

              <span class="small-label" style="margin-top:16px;">Ilustracje używane w tej scenie</span>
              <div class="link-row">
                <a class="tag" href="#ilustracja-il2">IL2</a>
                <a class="tag" href="#ilustracja-il3">IL3</a>
              </div>
            </div>

            <div class="block">
              <h3>Co ma się znaleźć w tej sekcji</h3>
              <ul>
                <li>opis rozwoju sytuacji po poprzedniej scenie,</li>
                <li>jakie nowe tropy, informacje lub komplikacje pojawiają się tutaj,</li>
                <li>jakie decyzje mogą podjąć gracze,</li>
                <li>jak reagują NPC, przeciwnicy lub otoczenie,</li>
                <li>jakie ilustracje są potrzebne do tej sceny, oznaczone numerami IL1, IL2, IL3 itd.,</li>
                <li>jakie handouty można tu zdobyć lub wykorzystać, oznaczone numerami H1, H2, H3 itd.,</li>
                <li>jakie mogą być warianty przebiegu sceny,</li>
                <li>jak połączyć tę scenę z kolejnymi częściami scenariusza.</li>
              </ul>
            </div>
          </div>
        </details>

        <details id="scena-3">
          <summary>
            <div class="summary-top">
              <div>
                <h2 class="summary-title">Scena 3 — Tytuł sceny</h2>
                <p class="summary-desc">
                  Tutaj wpisz krótki opis kulminacji, punktu zwrotnego, wejścia do finału
                  albo sceny, w której gracze zdobywają kluczowe informacje i muszą podjąć ważną decyzję.
                </p>
              </div>
              <span class="chevron">▼</span>
            </div>
          </summary>

          <div class="section-body">
            <div class="block">
              <h3>Streszczenie sceny</h3>
              <p>
                Tutaj wpisz krótki opis tego, co musi wybrzmieć przed finałem lub przed przejściem do zakończenia.
                Możesz opisać konfrontację, odkrycie prawdy, zmianę sojuszy, zdradę, ujawnienie stawki albo moment,
                w którym gracze rozumieją pełny obraz sytuacji.
              </p>
            </div>

            <div class="block" id="scena-3-dla-graczy">
              <h3>Sekcja dla Graczy</h3>
              <p>
                Tutaj wpisz gotowe opisy do odczytania przez MG w kulminacyjnych momentach sceny:
                wejście do finału, odkrycie prawdy, ujawnienie przeciwnika, opis starcia, przemianę lokacji,
                wizję albo końcowe odsłonięcie stawki.
              </p>
              <div class="readaloud">
                <strong>Przykład formy:</strong><br />
                „Światła gasną jedno po drugim. W ciszy, która po nich zapada, słyszycie tylko własny oddech
                i pojedynczy dźwięk kroków, powoli zbliżających się z głębi hali.”
              </div>
            </div>

            <div class="block">
              <h3>Scena Krok-po-kroku</h3>
              <p class="muted">
                Rozpisz scenę jako listę najważniejszych uderzeń fabularnych. To szczególnie przydatne w scenach
                napięcia, walki, pościgu, rytuału, przesłuchania lub kulminacyjnego odkrycia.
              </p>
              <div class="example">
                <ol>
                  <li>Graczy spotykają NPC1</li>
                  <li>NPC1 mówi graczom X</li>
                  <li>Gracze znajdują Y</li>
                </ol>
              </div>
            </div>

            <div class="block">
              <h3>Powiązane materiały</h3>
              <span class="small-label">Handouty używane w tej scenie</span>
              <div class="link-row">
                <a class="tag" href="#handout-h3">H3</a>
                <a class="tag" href="#handout-h4">H4</a>
              </div>

              <span class="small-label" style="margin-top:16px;">Ilustracje używane w tej scenie</span>
              <div class="link-row">
                <a class="tag" href="#ilustracja-il3">IL3</a>
                <a class="tag" href="#ilustracja-il4">IL4</a>
              </div>
            </div>

            <div class="block">
              <h3>Co ma się znaleźć w tej sekcji</h3>
              <ul>
                <li>najważniejsze wydarzenie lub konflikt tej części przygody,</li>
                <li>ujawnienie kluczowej prawdy, przeciwnika albo zagrożenia,</li>
                <li>konsekwencje wcześniejszych decyzji graczy,</li>
                <li>jakie ilustracje są potrzebne do tej sceny, oznaczone numerami IL1, IL2, IL3 itd.,</li>
                <li>jakie handouty można tu zdobyć lub wykorzystać, oznaczone numerami H1, H2, H3 itd.,</li>
                <li>możliwe przejścia do finału lub alternatywne zakończenia,</li>
                <li>informacja, co musi zostać domknięte przed końcem scenariusza.</li>
              </ul>
            </div>
          </div>
        </details>

        <details id="zakonczenie">
          <summary>
            <div class="summary-top">
              <div>
                <h2 class="summary-title">Zakończenie — Tytuł finału</h2>
                <p class="summary-desc">
                  Tutaj wpisz krótki opis finału, epilogu oraz możliwych skutków działań graczy
                  dla świata, kampanii, frakcji, relacji i dalszych przygód.
                </p>
              </div>
              <span class="chevron">▼</span>
            </div>
          </summary>

          <div class="section-body">
            <div class="block">
              <h3>Streszczenie zakończenia</h3>
              <p>
                W tej sekcji opisz możliwe zakończenia scenariusza. Uwzględnij sukces, częściowy sukces,
                porażkę, nieoczekiwane decyzje graczy oraz to, jak można domknąć emocjonalnie całą opowieść.
                Możesz też wpisać pomysły na epilog i konsekwencje dla przyszłych sesji.
              </p>
            </div>

            <div class="block">
              <h3>Co ma się znaleźć w tej sekcji</h3>
              <ul>
                <li>warunki sukcesu i porażki,</li>
                <li>najważniejsze możliwe warianty finału,</li>
                <li>skutki decyzji graczy,</li>
                <li>los ważnych NPC,</li>
                <li>konsekwencje dla świata i ewentualne haczyki na dalszą kampanię,</li>
                <li>opcjonalny tekst epilogu do odczytania graczom.</li>
              </ul>
            </div>
          </div>
        </details>

        <details id="przeciwnicy">
          <summary>
            <div class="summary-top">
              <div>
                <h2 class="summary-title">Przeciwnicy</h2>
                <p class="summary-desc">
                  Sekcja na listę przeciwników występujących w scenariuszu oraz miejsce na przyszłe odnośniki
                  do zewnętrznych plików ze statystykami.
                </p>
              </div>
              <span class="chevron">▼</span>
            </div>
          </summary>

          <div class="section-body">
            <div class="block">
              <h3>Tabela przeciwników</h3>
              <p class="muted">
                Wpisz tutaj wyłącznie przeciwników, którzy faktycznie pojawiają się w scenariuszu.
                Przycisk w kolumnie „Statystyki” jest tylko placeholderem pod przyszłe linki do plików JPG.
              </p>

              <div class="table-wrap">
                <table>
                  <thead>
                    <tr>
                      <th style="width:45%;">Nazwa</th>
                      <th style="width:55%;">Statystyki</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <strong>Przeciwnik 1</strong>
                        <p class="muted">Tutaj wpisz nazwę przeciwnika, dokładnie tak, jak ma być widoczna dla MG.</p>
                      </td>
                      <td>
                        <span class="button-placeholder">Otwórz statystyki</span>
                        <p class="muted" style="margin-top:10px;">
                          Docelowo ten przycisk będzie prowadził do pliku JPG ze screenem statystyk.
                        </p>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <strong>Przeciwnik 2</strong>
                        <p class="muted">Dodaj kolejnych przeciwników tylko wtedy, gdy są potrzebni w danym scenariuszu.</p>
                      </td>
                      <td>
                        <span class="button-placeholder">Otwórz statystyki</span>
                        <p class="muted" style="margin-top:10px;">
                          Nie podpinaj tutaj jeszcze logiki. To ma być jedynie wizualny placeholder.
                        </p>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </details>

        <details id="npc">
          <summary>
            <div class="summary-top">
              <div>
                <h2 class="summary-title">NPC — Postacie niezależne</h2>
                <p class="summary-desc">
                  Sekcja na najważniejsze osoby występujące w scenariuszu: ich wygląd, rolę,
                  wiedzę, funkcję fabularną oraz sposób, w jaki wpływają na działania graczy.
                </p>
              </div>
              <span class="chevron">▼</span>
            </div>
          </summary>

          <div class="section-body">
            <div class="block">
              <h3>Tabela NPC</h3>
              <p class="muted">
                Dodawaj tutaj tylko tych NPC, którzy rzeczywiście są potrzebni w scenariuszu.
                Jeżeli przygoda nie wymaga żadnych ważnych postaci niezależnych, sekcja może zostać pusta.
              </p>

              <div class="table-wrap">
                <table>
                  <thead>
                    <tr>
                      <th style="width:18%;">Nazwa</th>
                      <th style="width:32%;">Wygląd</th>
                      <th style="width:50%;">Rola</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <strong>NPC1</strong>
                        <p class="muted">
                          Wpisz imię, nazwę albo określenie postaci. Ma to być krótka, czytelna etykieta,
                          po której MG od razu rozpozna danego NPC.
                        </p>
                      </td>
                      <td>
                        <p>
                          Opisz, jak wygląda ta postać: ubiór, sylwetka, wiek, znaki rozpoznawcze,
                          mimika, sposób poruszania się, głos, wyposażenie i wszystko, co gracze
                          mogą zauważyć przy pierwszym kontakcie.
                        </p>
                      </td>
                      <td>
                        <p>
                          Opisz, jaką funkcję pełni ten NPC w scenariuszu. Napisz, co wie, jak może pomóc graczom,
                          czego od nich chce, co może przed nimi ukrywać, jak może im przeszkodzić, czy jest
                          sojusznikiem, neutralną postacią, świadkiem, informatorem, celem albo antagonistą.
                        </p>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <strong>NPC2</strong>
                        <p class="muted">Dodaj kolejne wiersze według potrzeb scenariusza.</p>
                      </td>
                      <td>
                        <p>W tej kolumnie utrzymuj opis wizualny i behawioralny postaci.</p>
                      </td>
                      <td>
                        <p>W tej kolumnie utrzymuj opis funkcji fabularnej, wiedzy i wpływu na przebieg przygody.</p>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </details>

        <details id="ilustracje">
          <summary>
            <div class="summary-top">
              <div>
                <h2 class="summary-title">Ilustracje</h2>
                <p class="summary-desc">
                  miejsce na prompty do generowania ilustracji przez narzędzia AI. Prompty mają być długie,
                  rozbudowane oraz zawierać tagi pozytywne i tagi negatywne
                </p>
              </div>
              <span class="chevron">▼</span>
            </div>
          </summary>

          <div class="section-body">
            <div class="block">
              <h3>Co ma się znaleźć w tej sekcji</h3>
              <p>
                Tutaj wpisuj prompty do generowania ilustracji związanych ze scenariuszem. Każdy wpis powinien być
                oznaczony numerem, np. <strong>IL1</strong>, <strong>IL2</strong>, <strong>IL3</strong>, aby łatwo było
                odwoływać się do nich z poziomu poszczególnych scen.
              </p>
            </div>

            <div class="entry-card" id="ilustracja-il1">
              <h4 class="entry-title"><span class="mini-id">IL1</span>Nazwa ilustracji</h4>
              <div class="entry-meta">Powiązana scena: Scena 1</div>
              <p>
                Tutaj wpisz długi prompt do ilustracji. Opisz kompozycję, kadr, oświetlenie, nastrój,
                kluczowe obiekty, wygląd miejsca lub postaci, styl wizualny oraz szczegóły techniczne.
              </p>
              <p><strong>Tagi pozytywne:</strong> tutaj wpisz pożądane cechy obrazu.</p>
              <p><strong>Tagi negatywne:</strong> tutaj wpisz elementy, których generator ma unikać.</p>
              <div class="link-row">
                <a class="tag" href="#scena-1">Przejdź do Sceny 1</a>
              </div>
            </div>

            <div class="entry-card" id="ilustracja-il2">
              <h4 class="entry-title"><span class="mini-id">IL2</span>Nazwa ilustracji</h4>
              <div class="entry-meta">Powiązana scena: Scena 1 lub Scena 2</div>
              <p>
                Ten blok jest gotowym wzorem pod kolejną ilustrację. Zachowaj numerację IL1, IL2, IL3 itd.
              </p>
              <div class="link-row">
                <a class="tag" href="#scena-1">Przejdź do Sceny 1</a>
                <a class="tag" href="#scena-2">Przejdź do Sceny 2</a>
              </div>
            </div>

            <div class="entry-card" id="ilustracja-il3">
              <h4 class="entry-title"><span class="mini-id">IL3</span>Nazwa ilustracji</h4>
              <div class="entry-meta">Powiązana scena: Scena 2 lub Scena 3</div>
              <p>
                Kolejny wzór wpisu ilustracji. W razie potrzeby duplikuj cały blok i aktualizuj numer.
              </p>
              <div class="link-row">
                <a class="tag" href="#scena-2">Przejdź do Sceny 2</a>
                <a class="tag" href="#scena-3">Przejdź do Sceny 3</a>
              </div>
            </div>

            <div class="entry-card" id="ilustracja-il4">
              <h4 class="entry-title"><span class="mini-id">IL4</span>Nazwa ilustracji</h4>
              <div class="entry-meta">Powiązana scena: Scena 3</div>
              <p>
                Użyj tego układu dla ilustracji związanych z finałem lub zakończeniem przygody.
              </p>
              <div class="link-row">
                <a class="tag" href="#scena-3">Przejdź do Sceny 3</a>
              </div>
            </div>
          </div>
        </details>

        <details id="handouty">
          <summary>
            <div class="summary-top">
              <div>
                <h2 class="summary-title">Handouty</h2>
                <p class="summary-desc">
                  miejsce na treści listów, notatek itp. rzeczy, jakie mogą odnaleźć gracze w scenariuszu
                </p>
              </div>
              <span class="chevron">▼</span>
            </div>
          </summary>

          <div class="section-body">
            <div class="block">
              <h3>Co ma się znaleźć w tej sekcji</h3>
              <p>
                Tutaj wpisuj gotowe handouty do pokazania lub odczytania graczom. Każdy wpis powinien być
                oznaczony numerem, np. <strong>H1</strong>, <strong>H2</strong>, <strong>H3</strong>, aby łatwo było
                odwoływać się do nich w scenach.
              </p>
            </div>

            <div class="entry-card" id="handout-h1">
              <h4 class="entry-title"><span class="mini-id">H1</span>Nazwa handoutu</h4>
              <div class="entry-meta">Gdzie występuje: Scena 1</div>
              <p><strong>Miejsce odnalezienia:</strong> wpisz, gdzie gracze zdobywają ten materiał.</p>
              <p><strong>Treść handoutu:</strong></p>
              <div class="readaloud">
                Tutaj wpisz pełną treść listu, notatki, raportu, wiadomości, ogłoszenia albo innego materiału,
                który gracze mogą przeczytać lub otrzymać.
              </div>
              <div class="link-row">
                <a class="tag" href="#scena-1">Wróć do miejsca użycia w Scenie 1</a>
              </div>
            </div>

            <div class="entry-card" id="handout-h2">
              <h4 class="entry-title"><span class="mini-id">H2</span>Nazwa handoutu</h4>
              <div class="entry-meta">Gdzie występuje: Scena 1 lub Scena 2</div>
              <p><strong>Miejsce odnalezienia:</strong> wpisz, kiedy i gdzie handout trafia do graczy.</p>
              <p><strong>Treść handoutu:</strong> wpisz pełną treść materiału.</p>
              <div class="link-row">
                <a class="tag" href="#scena-1">Wróć do miejsca użycia w Scenie 1</a>
                <a class="tag" href="#scena-2">Wróć do miejsca użycia w Scenie 2</a>
              </div>
            </div>

            <div class="entry-card" id="handout-h3">
              <h4 class="entry-title"><span class="mini-id">H3</span>Nazwa handoutu</h4>
              <div class="entry-meta">Gdzie występuje: Scena 2 lub Scena 3</div>
              <p><strong>Miejsce odnalezienia:</strong> wpisz okoliczności znalezienia lub przekazania handoutu.</p>
              <p><strong>Treść handoutu:</strong> wpisz pełną treść materiału.</p>
              <div class="link-row">
                <a class="tag" href="#scena-2">Wróć do miejsca użycia w Scenie 2</a>
                <a class="tag" href="#scena-3">Wróć do miejsca użycia w Scenie 3</a>
              </div>
            </div>

            <div class="entry-card" id="handout-h4">
              <h4 class="entry-title"><span class="mini-id">H4</span>Nazwa handoutu</h4>
              <div class="entry-meta">Gdzie występuje: Scena 3</div>
              <p><strong>Miejsce odnalezienia:</strong> wpisz, gdzie ten handout pojawia się pod koniec przygody.</p>
              <p><strong>Treść handoutu:</strong> wpisz pełną treść materiału.</p>
              <div class="link-row">
                <a class="tag" href="#scena-3">Wróć do miejsca użycia w Scenie 3</a>
              </div>
            </div>
          </div>
        </details>

        <section class="ai-instruction-box" id="instrukcja-ai" aria-label="Instrukcja dla AI">
          <h2 class="ai-instruction-title">Instrukcja dla AI</h2>
          <div class="ai-instruction-content">To jest uniwersalny template do tworzenia scenariuszy TTRPG. Twoim zadaniem jest uzupełniać go logicznie, czytelnie i praktycznie z punktu widzenia Mistrza Gry. Każda sekcja ma określoną funkcję. Nie należy wpisywać treści przypadkowo ani na siłę. Jeżeli jakiś element nie występuje w danym scenariuszu, sekcja może pozostać pusta, bardzo krótka albo może zawierać tylko informację, że dana przygoda nie korzysta z tego typu elementów.

ZASADY OGÓLNE:
1. Nie dodawaj treści na siłę tylko dlatego, że sekcja istnieje.
2. Nie każdy scenariusz wymaga NPC.
3. Nie każdy scenariusz wymaga Handoutów.
4. Nie każdy scenariusz wymaga Ilustracji.
5. Nie każdy scenariusz wymaga sekcji Przeciwnicy.
6. Nie każdy scenariusz będzie się składał z dokładnie trzech scen. Scen może być mniej albo więcej. W razie potrzeby należy powielać lub usuwać całe sekcje „Scena”.
7. Zachowuj spójność nazw, numeracji i odwołań pomiędzy sekcjami.
8. Jeżeli w scenie pojawia się odwołanie do ilustracji, używaj oznaczeń IL1, IL2, IL3 itd.
9. Jeżeli w scenie pojawia się odwołanie do handoutu, używaj oznaczeń H1, H2, H3 itd.
10. Nie wpisuj pustych ozdobników, lorem ipsum ani ogólników bez wartości praktycznej.
11. Pisz treści z myślą o późniejszym użyciu przy stole przez MG.
12. Zachowuj przejrzystość i funkcjonalność. Priorytetem jest użyteczność scenariusza, nie literackość dla samej literackości.
13. Jeżeli użytkownik poda własne nazwy sekcji, scen, NPC, handoutów lub ilustracji, należy ich używać konsekwentnie i nie podmieniać ich bez powodu.
14. W każdej scenie należy utrzymywać mały blok „Powiązane materiały”, zawierający szybkie linki do używanych tam handoutów i ilustracji.
15. Po kliknięciu oznaczenia H1, H2, H3 itd. użytkownik ma być przenoszony do odpowiedniego wpisu w sekcji „Handouty”.
16. Każdy wpis handoutu powinien zawierać link zwrotny do sceny, w której jest używany.
17. Po kliknięciu oznaczenia IL1, IL2, IL3 itd. użytkownik ma być przenoszony do odpowiedniego wpisu w sekcji „Ilustracje”.
18. Każdy wpis ilustracji powinien zawierać link zwrotny do sceny, w której jest używany.
19. Linki w blokach „Powiązane materiały” mają być utrzymywane ręcznie i aktualizowane przy dodawaniu lub usuwaniu scen, handoutów i ilustracji.
20. Sekcja „Instrukcja dla AI” ma pozostać bardzo mała wizualnie i nie może reagować na przyciski zmiany rozmiaru fontu.

SEKCJA „Tytuł scenariusza”:
Tutaj należy wpisać nazwę przygody. Tytuł powinien jasno identyfikować scenariusz i dobrze nadawać się do późniejszego wyszukiwania w archiwum użytkownika.

SEKCJA „krótki opis całego scenariusza”:
Tu należy wpisać zwięzły opis całej przygody: klimat, gatunek, motyw przewodni, stawkę, typ opowieści oraz ogólny charakter sesji. Ten fragment ma pomóc MG szybko zrozumieć, czym jest scenariusz.

SEKCJA „Skrót scenariusza”:
Tu należy wpisać pełniejsze podsumowanie całej historii dla MG. Należy opisać punkt wyjścia, główne wydarzenia, strukturę przygody, przewidywany przebieg oraz ogólny rodzaj finału. Ten skrót nie jest tekstem dla graczy, tylko szybkim kompendium dla prowadzącego.

SEKCJE „Scena”:
Każda scena jest osobnym modułem fabularnym. Nie zakładaj z góry, że scen muszą być trzy. To tylko szablon. Można dodać ich więcej, można usunąć zbędne.
Każda scena powinna mieć:
- numer i tytuł,
- krótki opis w nagłówku sekcji,
- streszczenie sceny,
- sekcję dla graczy,
- blok „Scena Krok-po-kroku”,
- blok „Powiązane materiały”,
- blok „Co ma się znaleźć w tej sekcji”.

W „Streszczeniu sceny” należy wpisać:
- po co scena istnieje,
- jaka jest jej funkcja w przygodzie,
- co powinni z niej wynieść gracze,
- jaki konflikt, problem albo odkrycie znajduje się w centrum tej sceny,
- do czego scena prowadzi dalej.

W „Sekcji dla Graczy” należy wpisać treści przeznaczone bezpośrednio do odczytania lub przedstawienia przez MG. Mogą to być:
- opisy wejścia do sceny,
- opisy lokacji,
- opisy pierwszego wrażenia,
- opisy dźwięków, zapachów i atmosfery,
- opisy ważnych odkryć,
- krótkie narracyjne komunikaty przygotowane do przeczytania na głos.
To jest sekcja użytkowa dla MG, ale jej treść jest skierowana do graczy.

W „Scena Krok-po-kroku” należy opisać możliwy przebieg sceny w kolejnych punktach. To nie musi być sztywny scenariusz działań graczy. Ma to być pomoc dla MG: uporządkowana sekwencja zdarzeń, informacji, reakcji NPC, możliwych odkryć i konsekwencji. Lista ma wspierać improwizację, a nie ją ograniczać.

W bloku „Powiązane materiały” należy umieszczać szybkie linki do handoutów i ilustracji używanych w danej scenie.
- Handouty należy oznaczać jako H1, H2, H3 itd.
- Ilustracje należy oznaczać jako IL1, IL2, IL3 itd.
- Każdy link powinien prowadzić do konkretnego wpisu niżej na stronie.
- Każdy wpis handoutu i ilustracji powinien mieć link zwrotny do sceny, gdzie jest używany.
- Przy zmianie numeracji należy poprawić wszystkie linki w obie strony.

W bloku „Co ma się znaleźć w tej sekcji” należy umieszczać praktyczne informacje, które MG może wykorzystać przy prowadzeniu. Mogą to być:
- opis miejsca,
- atmosfera,
- pierwsze wrażenia,
- obecne zagrożenia,
- możliwe testy,
- dostępne tropy,
- obecni NPC,
- możliwe komplikacje,
- odwołania do handoutów,
- odwołania do ilustracji,
- konsekwencje sukcesu i porażki,
- przejścia do następnych scen.

SEKCJA „Zakończenie”:
Tu należy opisać finał przygody i możliwe warianty domknięcia historii. Można uwzględnić sukces, porażkę, częściowy sukces, ucieczkę, kompromis, katastrofę, zmianę stron, zdradę, ujawnienie prawdy albo otwarte zakończenie. Należy opisać skutki decyzji graczy oraz ewentualne haczyki na dalszą kampanię.

SEKCJA „Przeciwnicy”:
Ta sekcja służy wyłącznie do wpisania listy przeciwników oraz późniejszych przycisków prowadzących do screenów statystyk.
BARDZO WAŻNE:
AI NIE MA SAMODZIELNIE UZUPEŁNIAĆ SEKCJI „Przeciwnicy”.
AI nie powinno samodzielnie wymyślać nazw przeciwników.
AI nie powinno samodzielnie dopisywać linków do statystyk.
AI nie powinno samodzielnie tworzyć odnośników do plików JPG.
Użytkownik musi sam podać wszystkie nazwy przeciwników i wszystkie linki lub dane dotyczące statystyk.
Jeżeli użytkownik nie poda danych do tej sekcji, pozostaw ją w stanie szablonowym albo pustym.

SEKCJA „NPC”:
Ta sekcja służy do wypisania ważnych postaci niezależnych, o ile scenariusz ich potrzebuje.
Nie dodawaj NPC tylko po to, żeby zapełnić tabelę.
Jeżeli scenariusz nie wymaga żadnych istotnych NPC, można zostawić sekcję pustą albo wpisać, że brak kluczowych NPC.
Kolumny znaczą:
- „Nazwa” = imię, przydomek, funkcja lub krótka nazwa postaci.
- „Wygląd” = opis zewnętrzny i pierwsze wrażenie, które odbierają gracze. Można uwzględnić ubiór, sylwetkę, wiek, charakterystyczne cechy, sposób poruszania się, ton głosu i inne zauważalne elementy.
- „Rola” = funkcja fabularna postaci. Należy tu wpisać, co NPC wie, jak może pomóc graczom, czego chce, jakie ma cele, jak może przeszkadzać, czy jest źródłem informacji, przewodnikiem, ofiarą, antagonistą, fałszywym sojusznikiem, klientem, świadkiem albo kimś jeszcze innym. To jest najważniejsza kolumna pod kątem użyteczności dla MG.

SEKCJA „Ilustracje”:
Ta sekcja służy do przygotowania promptów do generatorów obrazów AI.
Każdy wpis powinien mieć oznaczenie IL1, IL2, IL3 itd.
Każdy wpis powinien być powiązany z konkretną sceną, lokacją, NPC, wydarzeniem albo przedmiotem.
Każdy wpis powinien mieć też link zwrotny do sceny lub scen, gdzie dana ilustracja jest używana.
Prompty mają być długie, rozbudowane i praktyczne. Powinny zawierać:
- nazwę ilustracji,
- numer ilustracji,
- informację, do czego ilustracja służy,
- dokładny opis kompozycji,
- dokładny opis otoczenia,
- dokładny opis nastroju i światła,
- dokładny opis ważnych obiektów i postaci,
- styl wizualny, jeżeli użytkownik go określił,
- tagi pozytywne,
- tagi negatywne,
- opcjonalnie proporcje obrazu i inne parametry techniczne.
Nie twórz krótkich, ogólnikowych promptów. Ta sekcja ma być użyteczna przy realnym generowaniu grafik.

SEKCJA „Handouty”:
Ta sekcja służy do wpisywania materiałów, które mogą trafić do rąk graczy.
Każdy wpis powinien mieć oznaczenie H1, H2, H3 itd.
Każdy wpis powinien mieć też link zwrotny do sceny lub scen, gdzie dany handout jest używany.
Każdy handout powinien mieć:
- numer,
- nazwę,
- informację, gdzie i kiedy można go znaleźć,
- pełną treść gotową do pokazania graczom lub odczytania.
Handoutami mogą być:
- listy,
- notatki,
- raporty,
- pamiętniki,
- nagrania,
- transkrypcje,
- ogłoszenia,
- dokumenty,
- hasła,
- kody,
- wpisy z terminala,
- fragmenty ksiąg,
- mapki opisowe.
Jeżeli scenariusz nie przewiduje żadnych handoutów, nie trzeba ich dodawać.

NUMERACJA I SPÓJNOŚĆ:
- Każda ilustracja powinna mieć unikalny numer IL.
- Każdy handout powinien mieć unikalny numer H.
- W scenach należy odwoływać się do tych samych numerów.
- Nie mieszaj numeracji i nie duplikuj identyfikatorów.
- Jeżeli dodasz nową scenę, zadbaj o zgodność numeracji w panelu nawigacyjnym.
- Jeżeli usuniesz scenę, popraw odpowiednio odnośniki.
- Jeżeli scenariusz ma więcej scen, dodaj nowe sekcje „Scena” w tym samym układzie.
- Każdy link do handoutu powinien prowadzić do istniejącego identyfikatora w sekcji „Handouty”.
- Każdy link do ilustracji powinien prowadzić do istniejącego identyfikatora w sekcji „Ilustracje”.
- Każdy wpis handoutu i ilustracji powinien zawierać aktualne linki zwrotne.

STYL TREŚCI:
- Pisz po polsku, chyba że użytkownik zażąda inaczej.
- Pisz konkretnie i użytkowo.
- Nie zapełniaj sekcji pustą treścią.
- Nie wymyślaj elementów, których użytkownik nie chce.
- Gdy użytkownik poda konkretny świat, system albo konwencję, dopasuj do nich język i szczegóły.
- Pamiętaj, że szablon ma służyć późniejszemu rozwijaniu scenariusza, nie tylko jednorazowemu odczytowi.

NAJWAŻNIEJSZE OGRANICZENIA:
- Nie zakładaj, że każda przygoda ma trzy sceny.
- Nie zakładaj, że każda przygoda ma NPC.
- Nie zakładaj, że każda przygoda ma Handouty.
- Nie zakładaj, że każda przygoda ma Ilustracje.
- Nie uzupełniaj samodzielnie sekcji „Przeciwnicy”.
- Nie dodawaj nazw przeciwników ani linków do statystyk bez wyraźnych danych od użytkownika.</div>
        </section>

      </div>
    </main>
  </div>

  <script>
    (function () {
      const savedSize = localStorage.getItem("scenarioContentFontSize");
      const defaultSize = savedSize ? parseFloat(savedSize) : 18;
      document.documentElement.style.setProperty("--content-font-size", defaultSize + "px");

      const aiSection = document.querySelector(".ai-instruction-content");
      if (aiSection) {
        aiSection.style.fontSize = "1px";
      }
    })();

    function changeFontSize(step) {
      const rootStyles = getComputedStyle(document.documentElement);
      const current = parseFloat(rootStyles.getPropertyValue("--content-font-size")) || 18;
      const next = Math.min(26, Math.max(12, current + step));
      document.documentElement.style.setProperty("--content-font-size", next + "px");

      const aiSection = document.querySelector(".ai-instruction-content");
      if (aiSection) {
        aiSection.style.fontSize = "1px";
      }

      localStorage.setItem("scenarioContentFontSize", next);
    }
  </script>
</body>
</html>
