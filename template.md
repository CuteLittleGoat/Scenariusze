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
      --font-body: Calibri, Arial, Verdana, Tahoma, "Trebuchet MS";
      --font-heading: "Trebuchet MS", Verdana, Arial, Tahoma, Calibri;
      --font-navigation: Verdana, Tahoma, Arial, Calibri, "Trebuchet MS";
      --font-ui: Tahoma, Verdana, Arial, Calibri, "Trebuchet MS";
      --font-table: Arial, Calibri, Verdana, Tahoma, "Trebuchet MS";
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
      font-family: var(--font-body);
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
      font-family: var(--font-heading);
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
      flex-direction: column;
      gap: 8px;
      margin-bottom: 16px;
      padding: 10px 12px;
      background: rgba(255,255,255,0.03);
      border: 1px solid var(--border);
      border-radius: 14px;
    }

    .toolbar button {
      font-family: var(--font-ui);
      width: 100%;
      height: auto;
      border-radius: 10px;
      border: 1px solid var(--border-strong);
      background: var(--panel-2);
      color: var(--text);
      cursor: pointer;
      transition: 0.2s ease;
      font-size: 0.95rem;
      text-align: left;
      padding: 9px 12px;
    }

    .toolbar button:hover {
      border-color: var(--accent);
      color: white;
    }

    .nav-group {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .nav-link {
      font-family: var(--font-navigation);
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
      font-family: var(--font-heading);
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
      font-family: var(--font-heading);
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
      font-family: var(--font-heading);
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
      font-family: var(--font-table);
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
      font-family: var(--font-heading);
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

    .ai-instruction-row {
      margin-top: 26px;
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 16px;
    }

    .ai-instruction-row .ai-instruction-box {
      margin-top: 0;
    }

    .ai-instruction-title {
      font-family: var(--font-navigation);
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
        position: static;
        width: 100%;
        height: auto;
        max-height: none;
        border-right: none;
        border-bottom: 1px solid var(--border);
        overflow-y: visible;
      }

      .content {
        padding: 20px 16px 60px;
      }
    }

    @media (max-width: 720px) {
      :root {
        --content-font-size: 17px;
      }

      .content {
        font-size: var(--content-font-size);
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

      .ai-instruction-row {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <div class="layout">
    <aside class="sidebar" aria-label="Panel nawigacyjny scenariusza">
      <div class="sidebar-card">

        <div class="toolbar">
          <button type="button" data-font-step="1" aria-label="Font ▲">Font ▲</button>
          <button type="button" data-font-step="-1" aria-label="Font ▼">Font ▼</button>
        </div>

        <nav class="nav-group">
          <a class="nav-link is-main" href="#wprowadzenie">Wprowadzenie</a>
          <a class="nav-link is-main" href="#scena-1">Scena I - Tytuł Sceny I</a>
          <a class="nav-link is-main" href="#scena-2">Scena II - Tytuł Sceny II</a>
          <a class="nav-link is-main" href="#scena-3">Scena III - Tytuł Sceny III</a>
          <a class="nav-link is-main" href="#zakonczenie">Zakończenie</a>

          <div class="nav-divider"></div>

          <a class="nav-link" href="#przeciwnicy">Przeciwnicy</a>
          <a class="nav-link" href="#npc">NPC</a>
          <a class="nav-link" href="#ilustracje">Ilustracje</a>
          <a class="nav-link" href="#handouty">Handouty</a>
          <a class="nav-link" href="#inne-notatki">Inne Notatki</a>
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

        <details id="scena-1">
          <summary>
            <div class="summary-top">
              <div>
                <h2 class="summary-title">Scena I - Tytuł Sceny I</h2>
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
                <h2 class="summary-title">Scena II - Tytuł Sceny II</h2>
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
                <h2 class="summary-title">Scena III - Tytuł Sceny III</h2>
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
                <h2 class="summary-title">Zakończenie</h2>
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
              <div class="entry-meta">Powiązana scena: Scena I</div>
              <p>
                Tutaj wpisz długi prompt do ilustracji. Opisz kompozycję, kadr, oświetlenie, nastrój,
                kluczowe obiekty, wygląd miejsca lub postaci, styl wizualny oraz szczegóły techniczne.
              </p>
              <p><strong>Tagi pozytywne:</strong> tutaj wpisz pożądane cechy obrazu.</p>
              <p><strong>Tagi negatywne:</strong> tutaj wpisz elementy, których generator ma unikać.</p>
              <div class="link-row">
                <a class="tag" href="#scena-1">Przejdź do Sceny I</a>
              </div>
            </div>

            <div class="entry-card" id="ilustracja-il2">
              <h4 class="entry-title"><span class="mini-id">IL2</span>Nazwa ilustracji</h4>
              <div class="entry-meta">Powiązana scena: Scena I lub Scena II</div>
              <p>
                Ten blok jest gotowym wzorem pod kolejną ilustrację. Zachowaj numerację IL1, IL2, IL3 itd.
              </p>
              <div class="link-row">
                <a class="tag" href="#scena-1">Przejdź do Sceny I</a>
                <a class="tag" href="#scena-2">Przejdź do Sceny II</a>
              </div>
            </div>

            <div class="entry-card" id="ilustracja-il3">
              <h4 class="entry-title"><span class="mini-id">IL3</span>Nazwa ilustracji</h4>
              <div class="entry-meta">Powiązana scena: Scena II lub Scena III</div>
              <p>
                Kolejny wzór wpisu ilustracji. W razie potrzeby duplikuj cały blok i aktualizuj numer.
              </p>
              <div class="link-row">
                <a class="tag" href="#scena-2">Przejdź do Sceny II</a>
                <a class="tag" href="#scena-3">Przejdź do Sceny III</a>
              </div>
            </div>

            <div class="entry-card" id="ilustracja-il4">
              <h4 class="entry-title"><span class="mini-id">IL4</span>Nazwa ilustracji</h4>
              <div class="entry-meta">Powiązana scena: Scena III</div>
              <p>
                Użyj tego układu dla ilustracji związanych z finałem lub zakończeniem przygody.
              </p>
              <div class="link-row">
                <a class="tag" href="#scena-3">Przejdź do Sceny III</a>
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
              <div class="entry-meta">Gdzie występuje: Scena I</div>
              <p><strong>Miejsce odnalezienia:</strong> wpisz, gdzie gracze zdobywają ten materiał.</p>
              <p><strong>Treść handoutu:</strong></p>
              <div class="readaloud">
                Tutaj wpisz pełną treść listu, notatki, raportu, wiadomości, ogłoszenia albo innego materiału,
                który gracze mogą przeczytać lub otrzymać.
              </div>
              <div class="link-row">
                <a class="tag" href="#scena-1">Wróć do miejsca użycia w Scenie I</a>
              </div>
            </div>

            <div class="entry-card" id="handout-h2">
              <h4 class="entry-title"><span class="mini-id">H2</span>Nazwa handoutu</h4>
              <div class="entry-meta">Gdzie występuje: Scena I lub Scena II</div>
              <p><strong>Miejsce odnalezienia:</strong> wpisz, kiedy i gdzie handout trafia do graczy.</p>
              <p><strong>Treść handoutu:</strong> wpisz pełną treść materiału.</p>
              <div class="link-row">
                <a class="tag" href="#scena-1">Wróć do miejsca użycia w Scenie I</a>
                <a class="tag" href="#scena-2">Wróć do miejsca użycia w Scenie II</a>
              </div>
            </div>

            <div class="entry-card" id="handout-h3">
              <h4 class="entry-title"><span class="mini-id">H3</span>Nazwa handoutu</h4>
              <div class="entry-meta">Gdzie występuje: Scena II lub Scena III</div>
              <p><strong>Miejsce odnalezienia:</strong> wpisz okoliczności znalezienia lub przekazania handoutu.</p>
              <p><strong>Treść handoutu:</strong> wpisz pełną treść materiału.</p>
              <div class="link-row">
                <a class="tag" href="#scena-2">Wróć do miejsca użycia w Scenie II</a>
                <a class="tag" href="#scena-3">Wróć do miejsca użycia w Scenie III</a>
              </div>
            </div>

            <div class="entry-card" id="handout-h4">
              <h4 class="entry-title"><span class="mini-id">H4</span>Nazwa handoutu</h4>
              <div class="entry-meta">Gdzie występuje: Scena III</div>
              <p><strong>Miejsce odnalezienia:</strong> wpisz, gdzie ten handout pojawia się pod koniec przygody.</p>
              <p><strong>Treść handoutu:</strong> wpisz pełną treść materiału.</p>
              <div class="link-row">
                <a class="tag" href="#scena-3">Wróć do miejsca użycia w Scenie III</a>
              </div>
            </div>
          </div>
        </details>

        <details id="inne-notatki">
          <summary>
            <div class="summary-top">
              <div>
                <h2 class="summary-title">Inne Notatki</h2>
                <p class="summary-desc">
                  miejsce na dodatkowe notatki do scenariusza, które nie pasują do innych sekcji
                </p>
              </div>
              <span class="chevron">▼</span>
            </div>
          </summary>

          <div class="section-body">
            <div class="block">
              <h3>Co ma się znaleźć w tej sekcji</h3>
              <p>
                W tej sekcji wpisuj dodatkowe informacje pomocnicze dla MG, które nie pasują do wcześniej
                rozpisanych sekcji. Mogą to być np. luźne pomysły, krótkie doprecyzowania zasad domowych,
                alternatywne warianty scen, przypomnienia organizacyjne albo notatki o konsekwencjach decyzji
                graczy, których nie ma sensu rozpisywać w głównych blokach scenariusza.
              </p>
            </div>

            <div class="entry-card" id="notatka-n1">
              <h4 class="entry-title"><span class="mini-id">N1</span>Nazwa notatki</h4>
              <div class="entry-meta">Typ: Notatka dodatkowa</div>
              <p><strong>Kontekst:</strong> wpisz, kiedy i po co ta notatka może się przydać podczas prowadzenia sesji.</p>
              <p><strong>Treść notatki:</strong> wpisz konkretną informację, wskazówkę lub doprecyzowanie dla MG.</p>
            </div>

            <div class="entry-card" id="notatka-n2">
              <h4 class="entry-title"><span class="mini-id">N2</span>Nazwa notatki</h4>
              <div class="entry-meta">Typ: Notatka dodatkowa</div>
              <p><strong>Kontekst:</strong> wpisz obszar scenariusza, którego dotyczy notatka.</p>
              <p><strong>Treść notatki:</strong> wpisz treść pomocniczą, której nie umieszczono w innych sekcjach.</p>
            </div>
          </div>
        </details>

        <div class="ai-instruction-row">
          <section class="ai-instruction-box" id="instrukcja-ai" aria-label="Instrukcja ogólna dla AI">
            <h2 class="ai-instruction-title">Instrukcja ogólna dla AI</h2>
            <div class="ai-instruction-content">
Ta instrukcja określa zasady wypełniania tego szablonu scenariusza TTRPG w HTML.

AI ma pracować wyłącznie w ramach istniejącej struktury dokumentu i uzupełniać treści w sposób spójny, praktyczny oraz czytelny dla Mistrza Gry. Celem jest stworzenie użytecznego materiału do prowadzenia sesji, a nie tekstu literackiego oderwanego od zastosowania przy stole.

---

### 1. Zasady nadrzędne

#### 1.1. Zachowanie struktury
AI nie może usuwać, przebudowywać ani samowolnie zmieniać podstawowej struktury HTML, układu sekcji, nazw sekcji, klas CSS, istniejących identyfikatorów, kotwic, logiki przycisków, skryptów ani technicznych elementów szablonu.

AI może dodawać nowe elementy tego samego typu, które przewiduje szablon, na przykład:
- nowe sceny,
- nowych NPC,
- nowe ilustracje,
- nowe handouty,
- nowe notatki MG,
- nowe wpisy na listach,
- nowe pozycje w sekcjach pomocniczych.

Jeżeli dodanie nowego elementu wymaga nowego identyfikatora, kotwicy lub linku technicznego, AI może go utworzyć wyłącznie według istniejącego wzoru szablonu i bez naruszania pozostałej struktury dokumentu.

#### 1.2. Priorytet poleceń
W razie konfliktu obowiązuje następująca kolejność ważności:
1. polecenia użytkownika,
2. lokalne instrukcje wpisane w danym scenariuszu,
3. niniejsza instrukcja ogólna,
4. teksty przykładowe i placeholdery obecne w szablonie.

Jeżeli użytkownik wyda polecenie sprzeczne z tekstem przykładowym w szablonie, AI ma stosować się do polecenia użytkownika, a nie do placeholdera.

#### 1.3. Nie nadpisuj instrukcji
AI nie może usuwać ani przerabiać tej sekcji instrukcyjnej, chyba że użytkownik wyraźnie o to poprosi.

#### 1.4. Elastyczność wypełniania
Nie wszystkie sekcje muszą być wypełnione.
AI ma używać tylko tych sekcji, które są potrzebne dla danego scenariusza.

Scenariusz może mieć:
- mniej scen niż wzór,
- więcej scen niż wzór,
- mniej lub więcej NPC,
- mniej lub więcej ilustracji,
- mniej lub więcej handoutów,
- mniej lub więcej notatek MG.

Najważniejsze jest zachowanie porządku, numeracji i spójności.

---

### 2. Ogólny styl tworzenia treści

#### 2.1. Styl użytkowy, nie literacki
Treść ma być tworzona tak, by była wygodna dla MG podczas sesji.
Opis powinien być konkretny, przydatny, czytelny i szybki do wykorzystania.

AI nie powinno tworzyć przesadnie rozwlekłych opisów, jeśli nie zwiększają one użyteczności scenariusza.

#### 2.2. Spójność
AI ma pilnować spójności:
- nazw własnych,
- numeracji scen,
- numeracji ilustracji,
- numeracji handoutów,
- linków między sekcjami,
- informacji fabularnych,
- tonu i stylu tekstu.

Jeżeli jakaś postać, przedmiot, lokacja lub wydarzenie pojawia się w kilku miejscach, opis musi być zgodny we wszystkich sekcjach.

#### 2.3. Uzupełnianie braków
Jeżeli użytkownik poda niepełne informacje, AI może twórczo uzupełnić brakujące elementy fabularne, ale tylko wtedy, gdy:
- nie łamie to poleceń użytkownika,
- nie wprowadza mechaniki systemowej,
- nie tworzy nieuzasadnionych statystyk,
- nie miesza settingów,
- nie zmienia sensu scenariusza.

AI ma uzupełniać brakujące treści w sposób ostrożny i zgodny z kontekstem.

---

### 3. Zasady systemowej neutralności

#### 3.1. Szablon uniwersalny
Ten szablon ma być uniwersalny i możliwy do użycia w różnych systemach TTRPG.
Dlatego AI nie może zakładać konkretnego systemu mechanicznego, jeśli użytkownik wyraźnie go nie zdefiniował.

#### 3.2. Zakaz wprowadzania mechaniki systemowej
AI nie może samodzielnie wpisywać:
- testów umiejętności,
- nazw mechanik typowych dla konkretnego systemu,
- poziomów trudności,
- klas trudności,
- ST / DC,
- modyfikatorów,
- premii,
- kar,
- rzutów kością,
- obrażeń,
- punktów życia,
- pancerza,
- statystyk przeciwników,
- gotowych rozstrzygnięć mechanicznych.

Nie należy używać sformułowań typu:
- „Test Percepcji pozwala zauważyć X”,
- „Rzut na Stealth ukrywa bohatera”,
- „ST 14, aby otworzyć drzwi”,
- „Przeciwnik ma 12 HP”,
- „Wykonaj test Investigation”,
- „Rzut na wolę, aby oprzeć się efektowi”.

#### 3.3. Dopuszczalne opisy zamiast mechaniki
Zamiast języka mechanicznego AI ma używać języka opisowego i neutralnego systemowo, na przykład:
- „Gracze mogą zauważyć X”,
- „Uważni bohaterowie mogą dostrzec Y”,
- „Dokładne przeszukanie pomieszczenia może ujawnić Z”,
- „Rozmowa z NPC może naprowadzić drużynę na trop”,
- „Jeżeli bohaterowie zachowają ostrożność, mogą uniknąć zagrożenia”,
- „Przy odpowiednim podejściu drzwi da się otworzyć bez użycia siły”.

AI ma opisywać możliwości, wskazówki, konsekwencje i informacje fabularne, ale bez narzucania konkretnej mechaniki.

#### 3.4. Mechanika tylko na wyraźne polecenie
Jeżeli użytkownik wyraźnie każe dodać elementy mechaniczne dla konkretnego systemu, AI może to zrobić tylko w zakresie podanym przez użytkownika.
Bez takiego polecenia należy zachować pełną neutralność systemową.

---

### 4. Zasady settingu, lore i słownictwa

#### 4.1. Brak samodzielnego zakładania settingu
AI nie może samodzielnie zakładać konkretnego settingu, uniwersum, linii fabularnej ani lore, jeśli użytkownik lub lokalna instrukcja scenariusza tego wyraźnie nie wskazują.

Jeżeli setting nie został wskazany, AI ma używać określeń ogólnych i neutralnych, takich jak:
- strażnik,
- żołnierz,
- artefakt,
- świątynia,
- magiczna bariera,
- statek,
- potwór,
- przywódca kultu.

#### 4.2. Słownictwo specyficzne dla settingu tylko po wskazaniu settingu
Jeżeli użytkownik, MG albo lokalna instrukcja scenariusza wyraźnie wskaże setting, AI może używać żargonu, nazw własnych, terminów lore i stylistyki pasujących do tego settingu.

Przykłady:
- w scenariuszu osadzonym w Star Wars można używać określeń takich jak Jedi, Sith, miecz świetlny, szturmowiec;
- w scenariuszu osadzonym w D&D można używać określeń takich jak czarodziej, magiczna tarcza, beholder, kapłan;
- w scenariuszu osadzonym w Warhammer 40,000 można używać określeń takich jak Adeptus Mechanicus, Inkwizycja, boltgun, servo-czaszka.

#### 4.3. Zakaz mieszania settingów
AI nie może mieszać settingów, estetyk ani słownictwa charakterystycznego dla różnych uniwersów.

Nie wolno używać terminów właściwych dla jednego settingu w scenariuszu należącym do innego settingu, chyba że użytkownik wyraźnie nakaże crossover, mashup albo zabieg celowo mieszający konwencje.

Przykładowo:
- nie wolno używać określenia „Adeptus Astartes uzbrojony w boltgun” w scenariuszu osadzonym w realiach II wojny światowej;
- nie wolno wprowadzać Jedi do klasycznego fantasy bez wyraźnej zgody użytkownika;
- nie wolno mieszać potworów, frakcji i technologii z różnych uniwersów tylko dlatego, że „pasują klimatem”.

#### 4.4. Homebrew tylko na wyraźne polecenie
AI nie może samodzielnie dopisywać autorskiego lore, nowych frakcji, nowych ras, nowych zakonów, nowych planet, nowych szkół magii ani innych elementów homebrew, jeśli użytkownik tego wyraźnie nie poleci.

Homebrew jest dozwolone wyłącznie wtedy, gdy użytkownik wyraźnie nakaże:
- stworzyć autorski setting,
- rozbudować istniejący setting o własne elementy,
- dopisać nowe frakcje, organizacje, bóstwa, planety, miejsca lub zjawiska,
- potraktować scenariusz jako wariant niekanoniczny.

#### 4.5. Pierwszeństwo zgodności settingowej
Jeżeli scenariusz ma wskazany setting, AI ma pilnować zgodności:
- słownictwa,
- klimatu,
- realiów świata,
- roli frakcji i organizacji,
- technologii lub magii,
- nazw uzbrojenia, przedmiotów i zjawisk,
- ogólnej logiki świata.

W razie wątpliwości AI ma wybierać określenia bardziej ogólne zamiast ryzykować błędne lub mieszane nazewnictwo.

---

### 5. Zasady budowy scenariusza

#### 5.1. Sceny
Każda scena powinna mieć:
- jasny tytuł,
- czytelny cel lub funkcję w scenariuszu,
- opis pomocny MG,
- informacje istotne dla przebiegu sesji,
- ewentualne powiązania z NPC, ilustracjami, handoutami i notatkami MG.

AI może dodawać nowe sceny, jeśli wymaga tego scenariusz, ale musi zachować spójne nazewnictwo i numerację.

#### 5.2. Zawartość scen
Sceny powinny zawierać przede wszystkim:
- opis miejsca lub sytuacji,
- istotne fakty i wskazówki,
- możliwe działania bohaterów w sensie fabularnym,
- potencjalne komplikacje,
- konsekwencje działań,
- powiązania z innymi elementami scenariusza.

AI nie powinno zamieniać scen w instrukcję mechaniczną dla konkretnego systemu.

#### 5.3. Sekcja dla graczy
Jeżeli scena zawiera fragment przeznaczony do odczytania lub pokazania graczom, AI może go uzupełnić w sposób klimatyczny i zwięzły.

Tekst dla graczy powinien:
- budować nastrój,
- zawierać to, co postacie mogą postrzec bezpośrednio,
- nie zdradzać ukrytych informacji przeznaczonych wyłącznie dla MG.

#### 5.4. Sekcja dla MG
Informacje dla MG powinny być praktyczne, konkretne i zwięzłe.
To tutaj należy umieszczać:
- ukryty kontekst sceny,
- rzeczywisty sens wydarzeń,
- motywacje postaci,
- możliwe rozwidlenia,
- konsekwencje decyzji graczy,
- ważne informacje, których nie należy ujawniać graczom od razu.

---

### 6. NPC

#### 6.1. Dodawanie NPC
AI może tworzyć i uzupełniać sekcje NPC, jeśli są one potrzebne dla scenariusza.

Każdy NPC powinien mieć w miarę potrzeby:
- imię lub nazwę,
- rolę fabularną,
- krótki opis,
- motywację,
- użyteczne informacje dla MG,
- powiązania z innymi elementami scenariusza.

#### 6.2. Styl opisu NPC
Opis NPC powinien być praktyczny i przydatny na sesji.
Należy unikać zbyt długich biografii, jeśli nie są potrzebne.

#### 6.3. Brak statystyk postaci
AI nie tworzy statystyk NPC ani przeciwników, chyba że użytkownik wyraźnie tego zażąda i wskaże konkretny system.
Domyślnie należy ograniczać się do opisu fabularnego i funkcjonalnego.

---

### 7. Przeciwnicy

#### 7.1. Nazwy przeciwników są dozwolone
AI może wpisywać nazwy przeciwników, grup przeciwników lub rodzajów zagrożeń, jeśli wynikają one z treści scenariusza, na przykład:
- kultysta,
- strażnik świątyni,
- wilki,
- bandyci,
- zmutowany stwór,
- najemnicy.

Nazwy te mają charakter fabularny i organizacyjny.

Jeżeli scenariusz ma wyraźnie wskazany setting, AI może stosować także nazwy przeciwników zgodne z tym settingiem i jego lore.

#### 7.2. Zakaz tworzenia statystyk przeciwników
AI nie może samodzielnie tworzyć statystyk przeciwników.
Dotyczy to w szczególności:
- punktów życia,
- obrażeń,
- współczynników,
- cech,
- umiejętności,
- pancerza,
- inicjatywy,
- poziomu zagrożenia,
- akcji specjalnych opisanych mechanicznie,
- odporności i słabości zapisanych w sposób systemowy,
- gotowych bloków statystycznych.

Tworzenie statystyk przeciwników należy do MG.

#### 7.3. Dopuszczalne opisy przeciwników
AI może opisywać przeciwników i zagrożenia w sposób fabularny, organizacyjny i klimatyczny, bez wchodzenia w mechanikę systemową.

Dopuszczalne są opisy takie jak:
- „uzbrojeni w prymitywną broń”,
- „szybcy i agresywni”,
- „dobrze wyszkoleni”,
- „raczej słabo uzbrojeni, ale liczni”,
- „stanowią poważne zagrożenie w zwarciu”.

Jeżeli setting został wyraźnie wskazany przez użytkownika lub w lokalnej instrukcji scenariusza, AI może używać również określeń charakterystycznych dla tego settingu i zgodnych z jego lore.

AI nie może jednak:
- zamieniać opisów przeciwników w blok mechaniczny,
- używać nazewnictwa z innego settingu,
- wprowadzać żargonu lore niepasującego do wskazanych realiów scenariusza.

#### 7.4. Przeciwnicy tylko tam, gdzie są potrzebni
AI nie ma obowiązku dodawać przeciwników do każdej sceny.
Należy umieszczać ich tylko tam, gdzie mają sens fabularny.

---

### 8. Ilustracje

#### 8.1. Dodawanie ilustracji
AI może dodawać ilustracje, jeśli wspierają one prowadzenie scenariusza.

#### 8.2. Numeracja ilustracji
Każda ilustracja musi mieć spójną numerację według wzoru stosowanego w szablonie, na przykład:
- IL1,
- IL2,
- IL3.

Jeżeli ilustracja jest powiązana z konkretną sceną, należy to jasno zaznaczyć.

#### 8.3. Powiązania z innymi sekcjami
Jeżeli scena odwołuje się do ilustracji, scena powinna zawierać link do ilustracji.
Jeżeli ilustracja dotyczy konkretnej sceny, ilustracja powinna wskazywać scenę.
Powiązania powinny być możliwie dwukierunkowe i spójne.

#### 8.4. Opisy i prompty ilustracji
Jeżeli szablon przewiduje miejsce na prompt lub opis ilustracji, AI może go uzupełnić.
Opis powinien być:
- konkretny,
- wizualny,
- praktyczny,
- zgodny z klimatem scenariusza.

AI powinno unikać sprzeczności między opisem ilustracji a treścią scenariusza.

---

### 9. Handouty

#### 9.1. Dodawanie handoutów
AI może dodawać handouty, jeśli są użyteczne dla scenariusza, na przykład:
- listy,
- notatki,
- mapy,
- ogłoszenia,
- zapiski,
- fragmenty dzienników,
- dokumenty,
- symbole,
- krótkie teksty do wręczenia graczom.

#### 9.2. Numeracja handoutów
Każdy handout powinien mieć spójną numerację według wzoru szablonu, na przykład:
- H1,
- H2,
- H3.

#### 9.3. Powiązania
Jeżeli scena korzysta z handoutu, scena powinna zawierać odwołanie do odpowiedniego handoutu.
Jeżeli handout należy do konkretnej sceny, handout powinien wskazywać tę scenę.

#### 9.4. Styl handoutów
Handout powinien brzmieć jak obiekt istniejący w świecie gry, a nie jak notatka techniczna dla MG, chyba że sekcja wyraźnie przewiduje materiał pomocniczy tylko dla prowadzącego.

Przy tworzeniu handoutu AI ma zachować zgodność ze wskazanym settingiem, a jeśli setting nie został wskazany, ma używać języka ogólnego i neutralnego.

---

### 10. Notatki MG

#### 10.1. Rola notatek MG
Notatki MG służą do przekazywania informacji przydatnych podczas prowadzenia sesji.

#### 10.2. Co można tam umieszczać
W notatkach MG można umieszczać:
- skróty ważnych informacji,
- ukryte zależności,
- przypomnienia,
- możliwe konsekwencje,
- alternatywne ścieżki wydarzeń,
- sugestie interpretacyjne,
- krótkie wskazówki organizacyjne.

#### 10.3. Czego nie wpisywać
AI nie powinno używać notatek MG do wpisywania gotowej mechaniki systemowej, jeśli użytkownik o to nie poprosił.

---

### 11. Numeracja, nazewnictwo i linkowanie

#### 11.1. Numeracja
AI ma pilnować poprawnej i ciągłej numeracji wszystkich elementów:
- scen,
- NPC,
- ilustracji,
- handoutów,
- notatek i innych sekcji pomocniczych.

#### 11.2. Nazewnictwo
Nazwy powinny być spójne i konsekwentne w całym dokumencie.
Ta sama postać, lokacja lub frakcja nie może występować pod kilkoma różnymi nazwami, jeśli nie wynika to świadomie z fabuły.

#### 11.3. Linki i odwołania
AI ma pilnować, by odwołania między sekcjami były poprawne.
Jeżeli tekst mówi o konkretnej ilustracji, handoucie, NPC lub scenie, odpowiedni link lub podpis powinien być zgodny z numeracją i rzeczywistym elementem dokumentu.

#### 11.4. Ręczna kontrola linków
Jeżeli szablon przewiduje sekcję typu „Powiązane materiały”, AI ma ją uzupełniać świadomie i zgodnie z rzeczywistymi powiązaniami.
Nie należy wpisywać tam elementów przypadkowych ani niespójnych.

---

### 12. Jak AI ma podejmować decyzje przy brakach danych

#### 12.1. Gdy czegoś nie podano
Jeżeli użytkownik nie podał wszystkich danych, AI powinno:
- zachować sens scenariusza,
- dopisać tylko to, co potrzebne,
- unikać przesadnego rozbudowywania materiału,
- nie dodawać mechaniki systemowej,
- nie tworzyć statystyk bez wyraźnego polecenia,
- nie dopisywać settingu ani homebrew bez wyraźnej podstawy.

#### 12.2. Gdy czegoś nie trzeba dopisywać
Jeżeli jakaś sekcja nie jest potrzebna, AI powinno pozostawić ją pustą albo ograniczyć jej zawartość do minimum zgodnego z szablonem.

#### 12.3. Ostrożność przy dopowiadaniu
AI nie powinno tworzyć dużych, arbitralnych fragmentów lore, nowych frakcji, dodatkowych wątków, tajemnic ani rozbudowanych konfliktów, jeśli nie są potrzebne dla scenariusza lub nie wynikają z polecenia użytkownika.

---

### 13. Czego AI ma unikać

AI powinno unikać:
- wprowadzania mechaniki konkretnego systemu bez polecenia,
- tworzenia statystyk przeciwników lub NPC bez polecenia,
- używania testów, ST, DC, rzutów i modyfikatorów w uniwersalnym szablonie,
- samodzielnego zakładania settingu bez podstawy,
- mieszania settingów i słownictwa z różnych uniwersów,
- dopisywania homebrew bez wyraźnej komendy użytkownika,
- zmieniania technicznej struktury dokumentu,
- niszczenia numeracji i linków,
- powtarzania tych samych informacji w wielu miejscach bez potrzeby,
- nadmiernie literackiego stylu kosztem użyteczności,
- dopisywania treści, które zdradzają graczom informacje przeznaczone wyłącznie dla MG,
- wpisywania przeciwników lub scen tylko po to, żeby „zapełnić miejsce”.

---

### 14. Główna zasada końcowa

Najważniejszym celem AI jest stworzenie czytelnego, praktycznego, spójnego i neutralnego systemowo scenariusza TTRPG, który:
- dobrze działa przy stole,
- pomaga MG prowadzić sesję,
- nie narzuca konkretnej mechaniki,
- nie miesza settingów,
- używa słownictwa zgodnego z realiami scenariusza,
- pozwala MG samodzielnie dopasować statystyki, testy i zasady do wybranego systemu.

AI może pomagać w warstwie fabularnej, opisowej, organizacyjnej i strukturalnej, ale mechaniczne szczegóły systemu oraz statystyki przeciwników pozostają po stronie MG, chyba że użytkownik wyraźnie nakaże inaczej.
            </div>
          </section>

          <section class="ai-instruction-box" id="instrukcja-ai-scenariusza" aria-label="Instrukcja dla AI odnośnie tego scenariusza">
            <h2 class="ai-instruction-title">Instrukcja dla AI odnośnie tego scenariusza</h2>
            <div class="ai-instruction-content">To jest miejsce do uzupełnienia przez MG.
Tutaj mają się znaleźć instrukcje specyficzne dla tego konkretnego scenariusza oraz linki do dokumentów jakie AI ma przeczytać.
            
            </div>
          </section>
        </div>

      </div>
    </main>
  </div>

  <script>
    (function () {
      const savedSize = localStorage.getItem("scenarioContentFontSize");
      const cssDefaultSize = parseFloat(
        getComputedStyle(document.documentElement).getPropertyValue("--content-font-size")
      ) || 18;
      const defaultSize = savedSize ? parseFloat(savedSize) : cssDefaultSize;
      document.documentElement.style.setProperty("--content-font-size", defaultSize + "px");

      document.querySelectorAll("[data-font-step]").forEach((button) => {
        button.addEventListener("click", () => {
          const step = parseFloat(button.getAttribute("data-font-step"));
          if (!Number.isNaN(step)) {
            changeFontSize(step);
          }
        });
      });

      document.querySelectorAll(".ai-instruction-content").forEach((aiSection) => {
        aiSection.style.fontSize = "1px";
      });
    })();

    function changeFontSize(step) {
      const rootStyles = getComputedStyle(document.documentElement);
      const current = parseFloat(rootStyles.getPropertyValue("--content-font-size")) || 18;
      const next = Math.min(26, Math.max(12, current + step));
      document.documentElement.style.setProperty("--content-font-size", next + "px");

      document.querySelectorAll(".ai-instruction-content").forEach((aiSection) => {
        aiSection.style.fontSize = "1px";
      });

      localStorage.setItem("scenarioContentFontSize", next);
    }
  </script>
</body>
</html><!DOCTYPE html>
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
      --font-body: Calibri, Arial, Verdana, Tahoma, "Trebuchet MS";
      --font-heading: "Trebuchet MS", Verdana, Arial, Tahoma, Calibri;
      --font-navigation: Verdana, Tahoma, Arial, Calibri, "Trebuchet MS";
      --font-ui: Tahoma, Verdana, Arial, Calibri, "Trebuchet MS";
      --font-table: Arial, Calibri, Verdana, Tahoma, "Trebuchet MS";
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
      font-family: var(--font-body);
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
      font-family: var(--font-heading);
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
      flex-direction: column;
      gap: 8px;
      margin-bottom: 16px;
      padding: 10px 12px;
      background: rgba(255,255,255,0.03);
      border: 1px solid var(--border);
      border-radius: 14px;
    }

    .toolbar button {
      font-family: var(--font-ui);
      width: 100%;
      height: auto;
      border-radius: 10px;
      border: 1px solid var(--border-strong);
      background: var(--panel-2);
      color: var(--text);
      cursor: pointer;
      transition: 0.2s ease;
      font-size: 0.95rem;
      text-align: left;
      padding: 9px 12px;
    }

    .toolbar button:hover {
      border-color: var(--accent);
      color: white;
    }

    .nav-group {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .nav-link {
      font-family: var(--font-navigation);
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
      font-family: var(--font-heading);
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
      font-family: var(--font-heading);
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
      font-family: var(--font-heading);
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
      font-family: var(--font-table);
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
      font-family: var(--font-heading);
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

    .ai-instruction-row {
      margin-top: 26px;
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 16px;
    }

    .ai-instruction-row .ai-instruction-box {
      margin-top: 0;
    }

    .ai-instruction-title {
      font-family: var(--font-navigation);
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
        position: static;
        width: 100%;
        height: auto;
        max-height: none;
        border-right: none;
        border-bottom: 1px solid var(--border);
        overflow-y: visible;
      }

      .content {
        padding: 20px 16px 60px;
      }
    }

    @media (max-width: 720px) {
      :root {
        --content-font-size: 17px;
      }

      .content {
        font-size: var(--content-font-size);
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

      .ai-instruction-row {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <div class="layout">
    <aside class="sidebar" aria-label="Panel nawigacyjny scenariusza">
      <div class="sidebar-card">

        <div class="toolbar">
          <button type="button" data-font-step="1" aria-label="Font ▲">Font ▲</button>
          <button type="button" data-font-step="-1" aria-label="Font ▼">Font ▼</button>
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
          <a class="nav-link" href="#inne-notatki">Inne Notatki</a>
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

        <details id="scena-1">
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

        <details id="inne-notatki">
          <summary>
            <div class="summary-top">
              <div>
                <h2 class="summary-title">Inne Notatki</h2>
                <p class="summary-desc">
                  miejsce na dodatkowe notatki do scenariusza, które nie pasują do innych sekcji
                </p>
              </div>
              <span class="chevron">▼</span>
            </div>
          </summary>

          <div class="section-body">
            <div class="block">
              <h3>Co ma się znaleźć w tej sekcji</h3>
              <p>
                W tej sekcji wpisuj dodatkowe informacje pomocnicze dla MG, które nie pasują do wcześniej
                rozpisanych sekcji. Mogą to być np. luźne pomysły, krótkie doprecyzowania zasad domowych,
                alternatywne warianty scen, przypomnienia organizacyjne albo notatki o konsekwencjach decyzji
                graczy, których nie ma sensu rozpisywać w głównych blokach scenariusza.
              </p>
            </div>

            <div class="entry-card" id="notatka-n1">
              <h4 class="entry-title"><span class="mini-id">N1</span>Nazwa notatki</h4>
              <div class="entry-meta">Typ: Notatka dodatkowa</div>
              <p><strong>Kontekst:</strong> wpisz, kiedy i po co ta notatka może się przydać podczas prowadzenia sesji.</p>
              <p><strong>Treść notatki:</strong> wpisz konkretną informację, wskazówkę lub doprecyzowanie dla MG.</p>
            </div>

            <div class="entry-card" id="notatka-n2">
              <h4 class="entry-title"><span class="mini-id">N2</span>Nazwa notatki</h4>
              <div class="entry-meta">Typ: Notatka dodatkowa</div>
              <p><strong>Kontekst:</strong> wpisz obszar scenariusza, którego dotyczy notatka.</p>
              <p><strong>Treść notatki:</strong> wpisz treść pomocniczą, której nie umieszczono w innych sekcjach.</p>
            </div>
          </div>
        </details>

        <div class="ai-instruction-row">
          <section class="ai-instruction-box" id="instrukcja-ai" aria-label="Instrukcja ogólna dla AI">
            <h2 class="ai-instruction-title">Instrukcja ogólna dla AI</h2>
            <div class="ai-instruction-content">To jest uniwersalny template do tworzenia scenariuszy TTRPG. Twoim zadaniem jest uzupełniać go logicznie, czytelnie i praktycznie z punktu widzenia Mistrza Gry. Każda sekcja ma określoną funkcję. Nie należy wpisywać treści przypadkowo ani na siłę. Jeżeli jakiś element nie występuje w danym scenariuszu, sekcja może pozostać pusta, bardzo krótka albo może zawierać tylko informację, że dana przygoda nie korzysta z tego typu elementów.
Design strony HTML zawierającej treść scenariusza musi być zgodny z szablonem: https://cutelittlegoat.github.io/Scenariusze/template.html

ZASADY OGÓLNE:
1. Nie dodawaj treści na siłę tylko dlatego, że sekcja istnieje.
2. Nie każdy scenariusz wymaga NPC.
3. Nie każdy scenariusz wymaga Handoutów.
4. Nie każdy scenariusz wymaga Ilustracji.
5. Nie każdy scenariusz wymaga sekcji Inne Notatki.
6. Nie każdy scenariusz wymaga sekcji Przeciwnicy.
7. Nie każdy scenariusz będzie się składał z dokładnie trzech scen. Scen może być mniej albo więcej. W razie potrzeby należy powielać lub usuwać całe sekcje „Scena”.
8. Zachowuj spójność nazw, numeracji i odwołań pomiędzy sekcjami.
9. Jeżeli w scenie pojawia się odwołanie do ilustracji, używaj oznaczeń IL1, IL2, IL3 itd.
10. Jeżeli w scenie pojawia się odwołanie do handoutu, używaj oznaczeń H1, H2, H3 itd.
11. Nie wpisuj pustych ozdobników, lorem ipsum ani ogólników bez wartości praktycznej.
12. Pisz treści z myślą o późniejszym użyciu przy stole przez MG.
13. Zachowuj przejrzystość i funkcjonalność. Priorytetem jest użyteczność scenariusza, nie literackość dla samej literackości.
14. Jeżeli użytkownik poda własne nazwy sekcji, scen, NPC, handoutów lub ilustracji, należy ich używać konsekwentnie i nie podmieniać ich bez powodu.
15. W każdej scenie należy utrzymywać mały blok „Powiązane materiały”, zawierający szybkie linki do używanych tam handoutów i ilustracji.
16. Po kliknięciu oznaczenia H1, H2, H3 itd. użytkownik ma być przenoszony do odpowiedniego wpisu w sekcji „Handouty”.
17. Każdy wpis handoutu powinien zawierać link zwrotny do sceny, w której jest używany.
18. Po kliknięciu oznaczenia IL1, IL2, IL3 itd. użytkownik ma być przenoszony do odpowiedniego wpisu w sekcji „Ilustracje”.
19. Każdy wpis ilustracji powinien zawierać link zwrotny do sceny, w której jest używany.
20. Linki w blokach „Powiązane materiały” mają być utrzymywane ręcznie i aktualizowane przy dodawaniu lub usuwaniu scen, handoutów i ilustracji.
21. Sekcja „Instrukcja dla AI” ma pozostać bardzo mała wizualnie i nie może reagować na przyciski zmiany rozmiaru fontu.
22. Nie możesz nic samodzielnie zmieniać w treści sekcji "Instrukcja ogólna dla AI" oraz "Instrukcja dla AI odnośnie tego scenariusza"

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

SEKCJA „Inne Notatki”:
Ta sekcja służy do zapisywania różnych dodatkowych notatek do scenariusza, które nie pasują do wcześniej rozpisanych sekcji.
Można tu wpisywać np.:
- luźne doprecyzowania dla MG,
- alternatywne warianty rozwoju scen,
- przypomnienia organizacyjne,
- krótkie uwagi o tempie sesji,
- dodatkowe konsekwencje działań graczy, które nie mieszczą się naturalnie w innych sekcjach.
Jeżeli scenariusz nie wymaga takich notatek, sekcję można zostawić pustą.

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
- Nie zakładaj, że każda przygoda ma sekcję Inne Notatki.
- Nie uzupełniaj samodzielnie sekcji „Przeciwnicy”.
- Nie dodawaj nazw przeciwników ani linków do statystyk bez wyraźnych danych od użytkownika.</div>
          </section>

          <section class="ai-instruction-box" id="instrukcja-ai-scenariusza" aria-label="Instrukcja dla AI odnośnie tego scenariusza">
            <h2 class="ai-instruction-title">Instrukcja dla AI odnośnie tego scenariusza</h2>
            <div class="ai-instruction-content">To jest miejsce do uzupełnienia przez MG.
Tutaj mają się znaleźć instrukcje specyficzne dla tego konkretnego scenariusza oraz linki do dokumentów jakie AI ma przeczytać.
            
            </div>
          </section>
        </div>

      </div>
    </main>
  </div>

  <script>
    (function () {
      const savedSize = localStorage.getItem("scenarioContentFontSize");
      const cssDefaultSize = parseFloat(
        getComputedStyle(document.documentElement).getPropertyValue("--content-font-size")
      ) || 18;
      const defaultSize = savedSize ? parseFloat(savedSize) : cssDefaultSize;
      document.documentElement.style.setProperty("--content-font-size", defaultSize + "px");

      document.querySelectorAll("[data-font-step]").forEach((button) => {
        button.addEventListener("click", () => {
          const step = parseFloat(button.getAttribute("data-font-step"));
          if (!Number.isNaN(step)) {
            changeFontSize(step);
          }
        });
      });

      document.querySelectorAll(".ai-instruction-content").forEach((aiSection) => {
        aiSection.style.fontSize = "1px";
      });
    })();

    function changeFontSize(step) {
      const rootStyles = getComputedStyle(document.documentElement);
      const current = parseFloat(rootStyles.getPropertyValue("--content-font-size")) || 18;
      const next = Math.min(26, Math.max(12, current + step));
      document.documentElement.style.setProperty("--content-font-size", next + "px");

      document.querySelectorAll(".ai-instruction-content").forEach((aiSection) => {
        aiSection.style.fontSize = "1px";
      });

      localStorage.setItem("scenarioContentFontSize", next);
    }
  </script>
</body>
</html>
