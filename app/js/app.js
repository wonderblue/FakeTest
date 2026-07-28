const STORAGE_KEY = "ledger-reset-progress-v1";

const state = {
  db: null,
  route: "/",
  progress: loadProgress(),
};

function loadProgress() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY)) || defaultProgress();
  } catch {
    return defaultProgress();
  }
}

function defaultProgress() {
  return {
    completedDays: [],
    quizScores: {},
    earnedVisas: [],
    flashSeen: {},
    trainerBest: 0,
    practiceDone: [],
  };
}

function saveProgress() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state.progress));
}

async function loadDb() {
  const res = await fetch("./db.json", { cache: "no-store" });
  if (!res.ok) throw new Error("Could not load db.json. Serve the folder over HTTP.");
  state.db = await res.json();
}

function $(sel, root = document) {
  return root.querySelector(sel);
}

function el(html) {
  const t = document.createElement("template");
  t.innerHTML = html.trim();
  return t.content.firstElementChild;
}

function escapeHtml(str) {
  return String(str)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function toast(msg) {
  document.querySelectorAll(".toast").forEach((n) => n.remove());
  const n = el(`<div class="toast" role="status">${escapeHtml(msg)}</div>`);
  document.body.appendChild(n);
  setTimeout(() => n.remove(), 2400);
}

function parseRoute() {
  const hash = location.hash.replace(/^#/, "") || "/";
  const [path, query = ""] = hash.split("?");
  const params = Object.fromEntries(new URLSearchParams(query));
  return { path: path || "/", params };
}

function navigate(to) {
  location.hash = to.startsWith("#") ? to : `#${to}`;
}

function setActiveNav(path) {
  document.querySelectorAll(".nav a").forEach((a) => {
    const href = a.getAttribute("href").replace("#", "");
    a.classList.toggle("active", path === href || (href !== "/" && path.startsWith(href)));
  });
}

function progressSummary() {
  const p = state.progress;
  const visas = p.earnedVisas.length;
  const days = p.completedDays.length;
  const quizzes = Object.keys(p.quizScores).length;
  return { visas, days, quizzes };
}

function maybeEarnVisa(visaId, reason) {
  if (!visaId) return;
  if (state.progress.earnedVisas.includes(visaId)) return;
  state.progress.earnedVisas.push(visaId);
  saveProgress();
  const visa = state.db.masteryVisas.find((v) => v.id === visaId);
  toast(`Visa stamped: ${visa ? visa.title : visaId}${reason ? " — " + reason : ""}`);
}

function renderHome() {
  const plan = state.db.workPlan[0];
  const counts = {
    flashcards: state.db.flashcards.length,
    questions: state.db.questions.length,
    practice: state.db.practiceProblems.length,
    glossary: state.db.glossary.length,
  };
  const { visas, days, quizzes } = progressSummary();

  return `
    <section class="hero">
      <h1 class="hero__brand">Ledger Reset</h1>
      <p class="hero__headline">${escapeHtml(plan.tagline)}</p>
      <p class="hero__support">${escapeHtml(plan.audience)}. About ${escapeHtml(plan.weeklyHours)}.</p>
      <div class="hero__cta">
        <a class="btn" href="#/plan" data-link>Open 14-day plan</a>
        <a class="btn btn--ghost" href="#/trainer" data-link>Drill debits & credits</a>
      </div>
      <div class="stat-strip">
        <div><strong>${counts.flashcards}</strong> flashcards</div>
        <div><strong>${counts.questions}</strong> quiz questions</div>
        <div><strong>${counts.practice}</strong> practice items</div>
        <div><strong>${days}/14</strong> days touched · <strong>${visas}</strong> visas · <strong>${quizzes}</strong> quizzes logged</div>
      </div>
    </section>

    <section class="panel panel--solid">
      <h2 style="font-family:var(--font-display);margin-top:0">How this reboot works</h2>
      <div class="grid grid--2">
        <div>
          <p class="tag">Method</p>
          <ul class="checklist">${plan.method.map((m) => `<li>${escapeHtml(m)}</li>`).join("")}</ul>
        </div>
        <div>
          <p class="tag">Rules of engagement</p>
          <ul class="checklist">${plan.rulesOfEngagement.map((m) => `<li>${escapeHtml(m)}</li>`).join("")}</ul>
        </div>
      </div>
    </section>

    <section class="panel">
      <p class="tag">Start with the hard parts</p>
      <div class="grid grid--3">
        <div>
          <h3 style="font-family:var(--font-display);margin:.2rem 0">Account types</h3>
          <p>Classify until it is boring. Debits make sense only after types are automatic.</p>
          <a class="btn btn--small" href="#/accounts" data-link>Explore types</a>
        </div>
        <div>
          <h3 style="font-family:var(--font-display);margin:.2rem 0">Debits & credits</h3>
          <p>DEA-LER on loop. Left and right — not good and bad. Then build full entries.</p>
          <a class="btn btn--small" href="#/flashcards?deck=debit-credit" data-link>Open deck</a>
          <a class="btn btn--small btn--ghost" href="#/builder" data-link style="color:var(--ink);border-color:var(--line)">Journal Builder</a>
        </div>
        <div>
          <h3 style="font-family:var(--font-display);margin:.2rem 0">Mastery visas</h3>
          <p>Stamp competence as you clear quizzes and drills — a passport for the basics.</p>
          <a class="btn btn--small" href="#/visas" data-link>View passport</a>
        </div>
      </div>
    </section>
  `;
}

function renderPlan() {
  const days = state.db.studyPlan;
  const done = new Set(state.progress.completedDays);

  return `
    <p class="tag">Work plan</p>
    <h1 class="page-title">14 days to confident basics</h1>
    <p class="lede">Week 1 rebuilds the foundation. Week 2 connects statements, adjustments, finance ratios, and a capstone. Mark a day complete after its checkpoint.</p>
    <div class="panel panel--solid">
      ${days
        .map((d) => {
          const checked = done.has(d.day);
          return `
          <div class="day-row">
            <div class="day-num">${String(d.day).padStart(2, "0")}</div>
            <div>
              <p class="tag">Week ${d.week} · ${escapeHtml(d.theme)} · ~${d.durationMinutes} min</p>
              <strong>${escapeHtml(d.title)}</strong>
              <div style="margin-top:.35rem;color:rgba(12,26,20,.75)">${escapeHtml(d.checkpoint)}</div>
            </div>
            <button class="btn btn--small" data-day-toggle="${d.day}">${checked ? "Completed" : "Mark done"}</button>
          </div>`;
        })
        .join("")}
    </div>
    <div class="grid grid--2">
      ${days
        .map(
          (d) => `
        <article class="panel" id="day-${d.day}">
          <p class="tag">Day ${d.day}</p>
          <h2 style="font-family:var(--font-display);margin:.2rem 0 0.6rem">${escapeHtml(d.title)}</h2>
          <p><strong>Goals</strong></p>
          <ul class="checklist">${d.goals.map((g) => `<li>${escapeHtml(g)}</li>`).join("")}</ul>
          <p><strong>Tasks</strong></p>
          <ul class="checklist">
            ${d.tasks
              .map((t) => {
                let href = "#/lessons";
                if (t.type === "flashcards") href = `#/flashcards?deck=${encodeURIComponent(t.deck)}`;
                if (t.type === "quiz") href = `#/quiz/${encodeURIComponent(t.ref)}`;
                if (t.type === "trainer") href = "#/trainer";
                if (t.type === "practice") href = `#/practice?set=${encodeURIComponent(t.ref)}`;
                if (t.type === "read") href = `#/lesson/${encodeURIComponent(t.ref)}`;
                if (t.type === "visa") href = "#/visas";
                return `<li><a href="${href}" data-link>${escapeHtml(t.label)}</a></li>`;
              })
              .join("")}
          </ul>
          ${d.visaUnlock ? `<p class="muted">Visa target: <a href="#/visas" data-link>${escapeHtml(d.visaUnlock)}</a></p>` : ""}
        </article>`
        )
        .join("")}
    </div>
  `;
}

function renderLessons() {
  return `
    <p class="tag">Lessons</p>
    <h1 class="page-title">Deep dives</h1>
    <p class="lede">Twelve modules from the equation through cash flow and a keep-sharp plan. Read one per study day; revisit when a quiz exposes a gap.</p>
    <div class="panel panel--solid">
      ${state.db.modules
        .map(
          (m) => `
        <div class="list-row">
          <div class="day-num">${String(m.id).padStart(2, "0")}</div>
          <div>
            <p class="tag">${escapeHtml(m.level)} · ${m.readMinutes} min read</p>
            <strong>${escapeHtml(m.title)}</strong>
            <div style="color:rgba(12,26,20,.7)">${escapeHtml(m.subtitle)}</div>
          </div>
          <a class="btn btn--small" href="#/lesson/${m.slug}" data-link>Read</a>
        </div>`
        )
        .join("")}
    </div>
  `;
}

function renderLesson(slug) {
  const m = state.db.modules.find((x) => x.slug === slug);
  if (!m) return `<p class="lede">Lesson not found.</p>`;
  return `
    <p class="tag"><a href="#/lessons" data-link>Lessons</a> · ${escapeHtml(m.level)}</p>
    <h1 class="page-title">${escapeHtml(m.title)}</h1>
    <p class="lede">${escapeHtml(m.subtitle)} · ${m.readMinutes} min</p>
    <article class="panel panel--solid module-body">
      ${m.sections
        .map(
          (s) => `
        <h3>${escapeHtml(s.heading)}</h3>
        <p>${escapeHtml(s.body)}</p>`
        )
        .join("")}
      <h3>Key takeaways</h3>
      <ul class="checklist">${m.keyTakeaways.map((k) => `<li>${escapeHtml(k)}</li>`).join("")}</ul>
      <h3>Self-check</h3>
      <ul class="checklist">${m.selfCheck.map((k) => `<li>${escapeHtml(k)}</li>`).join("")}</ul>
    </article>
  `;
}

function renderAccounts() {
  return `
    <p class="tag">Account mastery</p>
    <h1 class="page-title">The five account types</h1>
    <p class="lede">Type first. Side second. If classification is shaky, debits and credits will feel random.</p>
    <div class="grid grid--2">
      ${state.db.accountTypes
        .map(
          (a) => `
        <article class="panel panel--solid account-type">
          <h3>${escapeHtml(a.name)}</h3>
          <p>${escapeHtml(a.definition)}</p>
          <div class="pill-meta">
            <span>Normal: ${escapeHtml(a.normalBalance)}</span>
            <span>Increase: ${escapeHtml(a.increaseWith)}</span>
            <span>${escapeHtml(a.statement)}</span>
            <span>${a.temporary ? "Temporary" : "Permanent"}</span>
          </div>
          <ul class="example-list">
            ${a.examples.map((ex) => `<li><strong>${escapeHtml(ex.name)}</strong> — ${escapeHtml(ex.note)}</li>`).join("")}
          </ul>
        </article>`
        )
        .join("")}
    </div>
    <section class="panel">
      <h2 style="font-family:var(--font-display);margin-top:0">Mnemonics</h2>
      <div class="grid grid--2">
        ${state.db.mnemonics
          .map(
            (m) => `<div><p class="tag">${escapeHtml(m.title)}</p><p>${escapeHtml(m.body)}</p></div>`
          )
          .join("")}
      </div>
    </section>
  `;
}

function renderFlashcards(params) {
  const decks = state.db.decks;
  const deckId = params.deck || decks[0].id;
  const cards = state.db.flashcards.filter((c) => c.deck === deckId);
  const deck = decks.find((d) => d.id === deckId) || { title: deckId };

  return `
    <p class="tag">Flashcards</p>
    <h1 class="page-title">${escapeHtml(deck.title)}</h1>
    <p class="lede">${cards.length} cards. Click the card to flip. Be honest — mark Known only when you could teach it.</p>
    <div class="panel" style="margin-bottom:1rem">
      <label for="deckSelect"><strong>Deck</strong></label>
      <select id="deckSelect" class="search" style="margin-top:.4rem">
        ${decks
          .map(
            (d) =>
              `<option value="${d.id}" ${d.id === deckId ? "selected" : ""}>${escapeHtml(d.title)}</option>`
          )
          .join("")}
      </select>
    </div>
    <div class="panel panel--solid" id="flashRoot" data-deck="${escapeHtml(deckId)}" data-count="${cards.length}">
      <div class="flash-stage" id="flashStage" tabindex="0" role="button" aria-label="Flip flashcard"></div>
      <div class="flash-actions">
        <button class="btn btn--ghost btn--small" id="flashPrev">Previous</button>
        <button class="btn btn--small" id="flashFlip">Flip</button>
        <button class="btn btn--ghost btn--small" id="flashNext">Next</button>
        <button class="btn btn--small" id="flashKnow" style="background:var(--moss);color:#fff">Known</button>
        <button class="btn btn--small" id="flashMiss" style="background:var(--danger);color:#fff">Missed</button>
      </div>
      <p class="muted" id="flashMeta" style="text-align:center;margin-top:1rem"></p>
    </div>
  `;
}

function initFlashcards(params) {
  const deckId = params.deck || state.db.decks[0].id;
  let cards = state.db.flashcards.filter((c) => c.deck === deckId);
  if (!cards.length) return;

  // Prefer unseen / missed ordering lightly
  cards = [...cards].sort((a, b) => {
    const as = state.progress.flashSeen[a.id] || 0;
    const bs = state.progress.flashSeen[b.id] || 0;
    return as - bs;
  });

  let idx = 0;
  let showBack = false;
  const stage = $("#flashStage");
  const meta = $("#flashMeta");

  function paint() {
    const c = cards[idx];
    const text = showBack ? c.back : c.front;
    const label = showBack ? "Answer" : "Prompt";
    stage.innerHTML = `
      <div class="flash-card-face">
        <p class="tag">${label} · ${idx + 1}/${cards.length}</p>
        <h3>${escapeHtml(text)}</h3>
        ${c.hint && !showBack ? `<p class="muted">Hint: ${escapeHtml(c.hint)}</p>` : ""}
        <p class="muted">${showBack ? "Click for prompt" : "Click to reveal"}</p>
      </div>`;
    meta.textContent = `Deck progress remembered locally. Known marks reduce how often a card resurfaces.`;
  }

  function flip() {
    showBack = !showBack;
    paint();
  }

  function step(delta) {
    idx = (idx + delta + cards.length) % cards.length;
    showBack = false;
    paint();
  }

  function mark(delta) {
    const c = cards[idx];
    const cur = state.progress.flashSeen[c.id] || 0;
    state.progress.flashSeen[c.id] = Math.max(0, cur + delta);
    saveProgress();
    step(1);
  }

  stage.addEventListener("click", flip);
  $("#flashFlip").addEventListener("click", flip);
  $("#flashPrev").addEventListener("click", () => step(-1));
  $("#flashNext").addEventListener("click", () => step(1));
  $("#flashKnow").addEventListener("click", () => mark(2));
  $("#flashMiss").addEventListener("click", () => mark(-1));
  $("#deckSelect").addEventListener("change", (e) => {
    navigate(`/flashcards?deck=${encodeURIComponent(e.target.value)}`);
  });
  stage.addEventListener("keydown", (e) => {
    if (e.key === " " || e.key === "Enter") {
      e.preventDefault();
      flip();
    }
    if (e.key === "ArrowRight") step(1);
    if (e.key === "ArrowLeft") step(-1);
  });
  paint();
}

function renderQuizzes() {
  return `
    <p class="tag">Quizzes</p>
    <h1 class="page-title">Prove it</h1>
    <p class="lede">Pass score is usually 80% (85% for Mixed Mastery). Passing stamps the matching Mastery Visa.</p>
    <div class="panel panel--solid">
      ${state.db.quizzes
        .map((q) => {
          const score = state.progress.quizScores[q.id];
          const scoreLabel = score == null ? "Not attempted" : `${score}%`;
          return `
          <div class="list-row">
            <div class="day-num">${String(q.day).padStart(2, "0")}</div>
            <div>
              <p class="tag">Pass ≥ ${q.passScore}% ${q.visa ? "· visa: " + q.visa : ""}</p>
              <strong>${escapeHtml(q.title)}</strong>
              <div style="color:rgba(12,26,20,.7)">Best: ${scoreLabel}</div>
            </div>
            <a class="btn btn--small" href="#/quiz/${q.id}" data-link>Start</a>
          </div>`;
        })
        .join("")}
    </div>
  `;
}

function renderQuiz(id) {
  const quiz = state.db.quizzes.find((q) => q.id === id);
  if (!quiz) return `<p class="lede">Quiz not found.</p>`;
  const questions = state.db.questions.filter((q) => q.quizId === id);
  return `
    <p class="tag"><a href="#/quizzes" data-link>Quizzes</a> · Day ${quiz.day}</p>
    <h1 class="page-title">${escapeHtml(quiz.title)}</h1>
    <p class="lede">${questions.length} questions · pass ≥ ${quiz.passScore}%</p>
    <div class="panel panel--solid" id="quizRoot" data-quiz="${quiz.id}" data-pass="${quiz.passScore}" data-visa="${quiz.visa || ""}">
      <div id="quizBody"></div>
    </div>
  `;
}

function initQuiz(id) {
  const quiz = state.db.quizzes.find((q) => q.id === id);
  const questions = state.db.questions.filter((q) => q.quizId === id);
  if (!quiz || !questions.length) return;

  let idx = 0;
  let correct = 0;
  let locked = false;
  const body = $("#quizBody");

  function finish() {
    const pct = Math.round((correct / questions.length) * 100);
    state.progress.quizScores[quiz.id] = Math.max(state.progress.quizScores[quiz.id] || 0, pct);
    saveProgress();
    const passed = pct >= quiz.passScore;
    if (passed) maybeEarnVisa(quiz.visa, `${pct}%`);
    body.innerHTML = `
      <h2 style="font-family:var(--font-display)">${passed ? "Passed" : "Keep drilling"} — ${pct}%</h2>
      <p>You got ${correct} of ${questions.length}. Pass line: ${quiz.passScore}%.</p>
      <div class="progress-rail"><span style="width:${pct}%"></span></div>
      <div style="margin-top:1rem;display:flex;gap:.6rem;flex-wrap:wrap">
        <button class="btn" id="quizRetry">Retry</button>
        <a class="btn btn--ghost" href="#/flashcards" data-link>Flashcards</a>
        <a class="btn btn--ghost" href="#/visas" data-link>Visas</a>
      </div>`;
    $("#quizRetry").addEventListener("click", () => {
      idx = 0;
      correct = 0;
      locked = false;
      paint();
    });
  }

  function paint() {
    if (idx >= questions.length) {
      finish();
      return;
    }
    const q = questions[idx];
    locked = false;
    body.innerHTML = `
      <p class="tag">Question ${idx + 1} / ${questions.length}</p>
      <h2 style="font-family:var(--font-display);font-size:1.45rem">${escapeHtml(q.prompt)}</h2>
      <div id="options">
        ${q.options
          .map(
            (opt, i) =>
              `<button class="quiz-option" data-i="${i}">${escapeHtml(opt)}</button>`
          )
          .join("")}
      </div>
      <p id="explain" class="muted" style="min-height:1.4em"></p>
      <button class="btn btn--small" id="quizNext" hidden>Next</button>`;

    body.querySelectorAll(".quiz-option").forEach((btn) => {
      btn.addEventListener("click", () => {
        if (locked) return;
        locked = true;
        const choice = Number(btn.dataset.i);
        const ok = choice === q.answer;
        if (ok) correct += 1;
        body.querySelectorAll(".quiz-option").forEach((b, i) => {
          if (i === q.answer) b.classList.add("correct");
          if (i === choice && !ok) b.classList.add("wrong");
        });
        $("#explain").textContent = q.explain;
        $("#quizNext").hidden = false;
      });
    });
    $("#quizNext").addEventListener("click", () => {
      idx += 1;
      paint();
    });
  }

  paint();
}

function renderTrainer() {
  return `
    <p class="tag">Debit / Credit trainer</p>
    <h1 class="page-title">Which side?</h1>
    <p class="lede">Given an account movement, choose Debit or Credit. Best streak saved: ${state.progress.trainerBest}. Hit 25 correct in a session for the Debits & Credits visa track.</p>
    <div class="panel panel--solid" id="trainerRoot">
      <p class="tag" id="trainerStats">Score 0 · Streak 0</p>
      <p class="trainer-prompt" id="trainerPrompt">Loading…</p>
      <div class="choice-row">
        <button class="btn" data-side="debit">Debit</button>
        <button class="btn" data-side="credit" style="background:var(--forest);color:#f3f8f4">Credit</button>
      </div>
      <p id="trainerFeedback" class="muted" style="margin-top:1rem;min-height:1.5em"></p>
    </div>
  `;
}

function initTrainer() {
  const prompts = [...state.db.trainerPrompts];
  let i = 0;
  let score = 0;
  let streak = 0;
  let answered = 0;

  function shuffle() {
    for (let a = prompts.length - 1; a > 0; a--) {
      const b = Math.floor(Math.random() * (a + 1));
      [prompts[a], prompts[b]] = [prompts[b], prompts[a]];
    }
  }
  shuffle();

  function show() {
    const p = prompts[i % prompts.length];
    $("#trainerPrompt").textContent = p.prompt;
    $("#trainerStats").textContent = `Score ${score}/${answered || 0} · Streak ${streak} · Best ${state.progress.trainerBest}`;
    $("#trainerFeedback").textContent = " ";
  }

  document.querySelectorAll("#trainerRoot [data-side]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const p = prompts[i % prompts.length];
      const choice = btn.dataset.side;
      answered += 1;
      const ok = choice === p.answer;
      if (ok) {
        score += 1;
        streak += 1;
        state.progress.trainerBest = Math.max(state.progress.trainerBest, streak);
        saveProgress();
        $("#trainerFeedback").textContent = `Correct — ${p.explain}`;
        if (streak >= 25 || score >= 25) maybeEarnVisa("debits-credits", "trainer milestone");
      } else {
        streak = 0;
        $("#trainerFeedback").textContent = `Not quite. Answer: ${p.answer}. ${p.explain}`;
      }
      i += 1;
      if (i % prompts.length === 0) shuffle();
      setTimeout(show, 650);
      $("#trainerStats").textContent = `Score ${score}/${answered} · Streak ${streak} · Best ${state.progress.trainerBest}`;
    });
  });
  show();
}

function renderJournalBuilder() {
  const jb = state.db.journalBuilder[0];
  return `
    <p class="tag">Journal Entry Builder</p>
    <h1 class="page-title">Build the entry</h1>
    <p class="lede">Read the narrative, then pick the debit account and the credit account. ${jb.scenarios.length} scenarios covering the core patterns, prepaids, accruals, and adjustments. Best streak saved: ${state.progress.journalBest || 0}.</p>
    <div class="panel panel--solid" id="jbRoot">
      <p class="tag" id="jbStats">Score 0 · Streak 0</p>
      <p class="trainer-prompt" id="jbNarrative">Loading…</p>
      <div class="grid grid--2">
        <div>
          <label for="jbDebit"><strong>Debit</strong></label>
          <select id="jbDebit" class="search" style="margin-top:.4rem"></select>
        </div>
        <div>
          <label for="jbCredit"><strong>Credit</strong></label>
          <select id="jbCredit" class="search" style="margin-top:.4rem"></select>
        </div>
      </div>
      <div style="margin-top:1rem;display:flex;gap:.6rem;flex-wrap:wrap">
        <button class="btn" id="jbCheck">Check entry</button>
        <button class="btn btn--ghost" id="jbSkip">Skip</button>
      </div>
      <p id="jbFeedback" class="muted" style="margin-top:1rem;min-height:2.4em"></p>
    </div>
  `;
}

function initJournalBuilder() {
  const jb = state.db.journalBuilder[0];
  const scenarios = [...jb.scenarios];
  for (let a = scenarios.length - 1; a > 0; a--) {
    const b = Math.floor(Math.random() * (a + 1));
    [scenarios[a], scenarios[b]] = [scenarios[b], scenarios[a]];
  }

  let i = 0;
  let score = 0;
  let streak = 0;
  let answered = 0;

  const optionHtml = ['<option value="">— choose account —</option>']
    .concat(jb.accounts.map((a) => `<option value="${escapeHtml(a)}">${escapeHtml(a)}</option>`))
    .join("");
  $("#jbDebit").innerHTML = optionHtml;
  $("#jbCredit").innerHTML = optionHtml;

  function show() {
    const s = scenarios[i % scenarios.length];
    $("#jbNarrative").textContent = `${s.narrative} ($${s.amount.toLocaleString()})`;
    $("#jbDebit").value = "";
    $("#jbCredit").value = "";
    $("#jbFeedback").textContent = " ";
    $("#jbStats").textContent = `Score ${score}/${answered} · Streak ${streak} · Best ${state.progress.journalBest || 0}`;
  }

  $("#jbCheck").addEventListener("click", () => {
    const s = scenarios[i % scenarios.length];
    const dr = $("#jbDebit").value;
    const cr = $("#jbCredit").value;
    if (!dr || !cr) {
      $("#jbFeedback").textContent = "Pick both a debit and a credit account first.";
      return;
    }
    answered += 1;
    const ok = dr === s.debit && cr === s.credit;
    if (ok) {
      score += 1;
      streak += 1;
      state.progress.journalBest = Math.max(state.progress.journalBest || 0, streak);
      saveProgress();
      $("#jbFeedback").textContent = `Correct — Dr ${s.debit} / Cr ${s.credit}. ${s.explain}`;
      if (streak >= 15) maybeEarnVisa("journal-entries", "builder milestone");
    } else {
      streak = 0;
      $("#jbFeedback").textContent = `Not quite. Correct: Dr ${s.debit} ${s.amount.toLocaleString()} / Cr ${s.credit} ${s.amount.toLocaleString()}. ${s.explain}`;
    }
    i += 1;
    setTimeout(show, 2600);
    $("#jbStats").textContent = `Score ${score}/${answered} · Streak ${streak} · Best ${state.progress.journalBest || 0}`;
  });

  $("#jbSkip").addEventListener("click", () => {
    i += 1;
    show();
  });

  show();
}

function renderVisas() {
  const earned = new Set(state.progress.earnedVisas);
  return `
    <p class="tag">Mastery passport</p>
    <h1 class="page-title">Visas</h1>
    <p class="lede">Each visa is a competence stamp — clear the linked quiz and practice. Collect them across the 14-day plan.</p>
    <div class="visa-wall">
      ${state.db.masteryVisas
        .map((v) => {
          const has = earned.has(v.id);
          return `
          <article class="visa ${has ? "earned" : "locked"}" style="background:${v.color}">
            <div class="visa__sub">${escapeHtml(v.subtitle)} · Day ${v.day}</div>
            <h3 class="visa__title">${escapeHtml(v.title)}</h3>
            <p style="font-size:.92rem;opacity:.9">${escapeHtml(v.requirement)}</p>
            <ul style="margin:.5rem 0 0;padding-left:1rem;opacity:.9">
              ${v.skills.map((s) => `<li>${escapeHtml(s)}</li>`).join("")}
            </ul>
            <p style="margin-top:.8rem;font-weight:600">${has ? "STAMPED" : "LOCKED"}</p>
          </article>`;
        })
        .join("")}
    </div>
  `;
}

function renderPractice(params) {
  const sets = [...new Set(state.db.practiceProblems.map((p) => p.setId))];
  const setId = params.set || sets[0];
  const items = state.db.practiceProblems.filter((p) => p.setId === setId);
  const done = new Set(state.progress.practiceDone);

  return `
    <p class="tag">Practice lab</p>
    <h1 class="page-title">Worked problems</h1>
    <p class="lede">Reveal solutions only after you attempt them on paper or aloud. ${items.length} items in this set.</p>
    <div class="panel">
      <label for="setSelect"><strong>Practice set</strong></label>
      <select id="setSelect" class="search" style="margin-top:.4rem">
        ${sets
          .map((s) => `<option value="${s}" ${s === setId ? "selected" : ""}>${s}</option>`)
          .join("")}
      </select>
    </div>
    <div class="grid">
      ${items
        .map((p) => {
          const isDone = done.has(p.id);
          return `
          <article class="panel panel--solid" data-practice="${p.id}">
            <p class="tag">${escapeHtml(p.kind)} · ${escapeHtml(p.difficulty)}${isDone ? " · done" : ""}</p>
            <h3 style="font-family:var(--font-display);margin:.2rem 0">${escapeHtml(p.title)}</h3>
            <p>${escapeHtml(p.prompt)}</p>
            <details>
              <summary>Show solution</summary>
              <p><strong>${escapeHtml(p.solution)}</strong></p>
            </details>
            <button class="btn btn--small" data-practice-done="${p.id}" style="margin-top:.75rem">${isDone ? "Completed" : "Mark attempted"}</button>
          </article>`;
        })
        .join("")}
    </div>
  `;
}

function initPractice() {
  $("#setSelect")?.addEventListener("change", (e) => {
    navigate(`/practice?set=${encodeURIComponent(e.target.value)}`);
  });
  document.querySelectorAll("[data-practice-done]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const id = Number(btn.dataset.practiceDone);
      if (!state.progress.practiceDone.includes(id)) {
        state.progress.practiceDone.push(id);
        saveProgress();
      }
      btn.textContent = "Completed";
      toast("Practice logged");
    });
  });
}

function renderReference() {
  return `
    <p class="tag">Reference</p>
    <h1 class="page-title">Cheat sheets & glossary</h1>
    <p class="lede">Keep these open while journaling. Search the glossary when a term feels fuzzy.</p>
    <div style="display:flex;gap:.6rem;flex-wrap:wrap;margin-bottom:1rem" class="no-print">
      <button class="btn btn--small" id="printSheets">Print cheat sheets</button>
      <button class="btn btn--ghost btn--small" id="exportProgress">Export progress</button>
      <button class="btn btn--ghost btn--small" id="resetProgress">Reset progress</button>
    </div>
    <div class="grid grid--2 print-area">
      ${state.db.cheatSheets
        .map(
          (c) => `
        <article class="panel panel--solid">
          <h3 style="font-family:var(--font-display);margin-top:0">${escapeHtml(c.title)}</h3>
          <pre style="white-space:pre-wrap;font-family:var(--font-body);margin:0">${escapeHtml(c.body)}</pre>
        </article>`
        )
        .join("")}
    </div>
    <section class="panel panel--solid" style="margin-top:1rem">
      <input class="search" id="glossarySearch" placeholder="Search glossary…" />
      <div id="glossaryList" style="margin-top:1rem"></div>
    </section>
  `;
}

function initReference() {
  const list = $("#glossaryList");
  const terms = state.db.glossary;

  function paint(filter = "") {
    const q = filter.trim().toLowerCase();
    const rows = terms.filter(
      (t) => !q || t.term.toLowerCase().includes(q) || t.definition.toLowerCase().includes(q)
    );
    list.innerHTML = rows
      .map(
        (t) => `
      <div class="list-row" style="grid-template-columns:1fr">
        <div>
          <strong>${escapeHtml(t.term)}</strong>
          <div style="color:rgba(12,26,20,.75)">${escapeHtml(t.definition)}</div>
        </div>
      </div>`
      )
      .join("");
  }

  $("#glossarySearch").addEventListener("input", (e) => paint(e.target.value));
  paint();

  $("#printSheets").addEventListener("click", () => window.print());

  $("#exportProgress").addEventListener("click", () => {
    const blob = new Blob([JSON.stringify(state.progress, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "ledger-reset-progress.json";
    a.click();
    URL.revokeObjectURL(url);
    toast("Progress exported");
  });

  $("#resetProgress").addEventListener("click", () => {
    if (!confirm("Reset all local progress (quiz scores, visas, flashcard marks)?")) return;
    state.progress = defaultProgress();
    saveProgress();
    toast("Progress reset");
    render();
  });
}

function bindPlanToggles() {
  document.querySelectorAll("[data-day-toggle]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const day = Number(btn.dataset.dayToggle);
      const set = new Set(state.progress.completedDays);
      if (set.has(day)) set.delete(day);
      else set.add(day);
      state.progress.completedDays = [...set].sort((a, b) => a - b);
      saveProgress();
      const dayPlan = state.db.studyPlan.find((d) => d.day === day);
      if (set.has(day) && dayPlan?.visaUnlock) {
        // Soft hint only — visas still require quizzes, except we don't auto-grant here
      }
      render();
      toast(set.has(day) ? `Day ${day} marked complete` : `Day ${day} reopened`);
    });
  });
}

async function render() {
  const app = $("#app");
  const { path, params } = parseRoute();
  state.route = path;
  setActiveNav(path);

  let html = "";
  let after = null;

  if (path === "/" || path === "") {
    html = renderHome();
  } else if (path === "/plan") {
    html = renderPlan();
    after = bindPlanToggles;
  } else if (path === "/lessons") {
    html = renderLessons();
  } else if (path.startsWith("/lesson/")) {
    html = renderLesson(path.replace("/lesson/", ""));
  } else if (path === "/accounts") {
    html = renderAccounts();
  } else if (path === "/flashcards") {
    html = renderFlashcards(params);
    after = () => initFlashcards(params);
  } else if (path === "/quizzes") {
    html = renderQuizzes();
  } else if (path.startsWith("/quiz/")) {
    const id = path.replace("/quiz/", "");
    html = renderQuiz(id);
    after = () => initQuiz(id);
  } else if (path === "/trainer") {
    html = renderTrainer();
    after = initTrainer;
  } else if (path === "/builder") {
    html = renderJournalBuilder();
    after = initJournalBuilder;
  } else if (path === "/visas") {
    html = renderVisas();
  } else if (path === "/practice") {
    html = renderPractice(params);
    after = initPractice;
  } else if (path === "/reference") {
    html = renderReference();
    after = initReference;
  } else {
    html = `<p class="lede">Page not found. <a href="#/" data-link>Go home</a></p>`;
  }

  app.innerHTML = html;
  after?.();
  window.scrollTo({ top: 0, behavior: "instant" in window ? "instant" : "auto" });
}

function setupChrome() {
  const toggle = $("#navToggle");
  const nav = $("#mainNav");
  toggle.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(open));
  });
  document.body.addEventListener("click", (e) => {
    const a = e.target.closest("[data-link]");
    if (a) nav.classList.remove("open");
  });
}

async function main() {
  setupChrome();
  try {
    await loadDb();
  } catch (err) {
    $("#app").innerHTML = `
      <section class="panel panel--solid">
        <h1 class="page-title" style="color:var(--ink)">Could not load data</h1>
        <p>${escapeHtml(err.message)}</p>
        <p>From the repo root run: <code>python3 -m http.server 8080</code> then open <code>http://localhost:8080</code>.</p>
      </section>`;
    return;
  }
  window.addEventListener("hashchange", render);
  render();
}

main();
