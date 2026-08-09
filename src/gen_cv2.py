# -*- coding: utf-8 -*-
"""CV allineato al sito: palette del sito, conteggi a destra dei titoli di sezione,
didattica e supervisioni rigenerate da data.py.

I numeri non si scrivono a mano da nessuna parte: o vengono da data.py o vengono contati
dai file .tex delle pubblicazioni. Se un dato cambia li, cambia qui.
"""
import os, re, shutil, subprocess, glob, html as _html
import data as D
from traduzioni import apply_tr

import os as _os
# Percorsi ricavati dalla posizione di questo file: il generatore funziona
# ovunque sia il repository, senza percorsi assoluti da aggiornare a mano.
_HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.dirname(_HERE)                     # la radice del sito

SRC = _os.path.join(ROOT, "curriculum_vitae")
OUT = _os.path.join(_os.path.dirname(ROOT), "_build_cv")

# esattamente i colori del sito in modalita chiara
PAL = {"accent": "98461F", "dark": "17150F", "gray": "4E463B",
       "light": "8C8272", "page": "FFFDF8"}

# ---------------------------------------------------------------- utilita

def tex(s):
    """Da stringa del sito a stringa LaTeX: via i tag, via le entita, via i caratteri attivi."""
    if isinstance(s, dict):
        raise TypeError("passa prima la lingua")
    s = re.sub(r"<[^>]+>", "", s)
    # decodifica di tutte le entita, non di una lista scelta a mano: &rsquo; e &ldquo;
    # erano sfuggiti alla lista e finivano stampati alla lettera nel PDF
    s = _html.unescape(s)
    s = s.replace("\\", r"\textbackslash{}")
    for ch in "&%$#_{}":
        s = s.replace(ch, "\\" + ch)
    s = s.replace("~", r"\textasciitilde{}").replace("^", r"\textasciicircum{}")
    for a, b in (("—", "---"), ("–", "--"), ("−", "--"), ("·", r"\textperiodcentered{}"),
                 ("×", r"\texttimes{}"), ("’", "'"), ("‘", "`"),
                 ("“", "``"), ("”", "''"), ("…", r"\ldots{}")):
        s = s.replace(a, b)
    return s


def L(d, lang):
    return d[lang] if isinstance(d, dict) else d


# ---------------------------------------------------------------- conteggi

def count_pubs(path):
    """Divide il file per voci e legge lo Status di ciascuna: i grep sulle righe
    contano le occorrenze, non le voci, e le due cose non coincidono."""
    src = open(path, encoding="utf-8").read()
    blocks = src.split(r"\cventry")[1:]
    tot = len(blocks)
    review = sum(1 for b in blocks if re.search(r"Status:\s*Under\s+review", b, re.I))
    return tot, review


def counts():
    j_tot, j_rev = count_pubs(os.path.join(SRC, "resume", "journalpublications.tex"))
    c_tot, c_rev = count_pubs(os.path.join(SRC, "resume", "conferencepublications.tex"))
    comp = len(open(os.path.join(SRC, "resume", "competitions.tex"),
                    encoding="utf-8").read().split(r"\cventry")) - 1
    return {"j_tot": j_tot, "j_rev": j_rev, "c_tot": c_tot, "c_rev": c_rev, "comp": comp}


# ---------------------------------------------------------------- struttura

# Ordine e titoli delle sezioni, allineati a quelli del sito. Le voci che il sito non
# ha (Tesi proprie, Competizioni, e la separazione rivista/conferenza al posto di una
# sola "Selected Publications") restano: sul CV le informazioni aggiuntive vanno tenute.
SECTIONS = [
    # About, Sintesi, Formazione ed Esperienza sono la prima pagina, a colonne:
    # non sono piu sezioni del flusso. Le tesi proprie stanno sotto il titolo di studio
    # cui appartengono, quindi la sezione Theses non serve piu.
    ("journalpublications",       {"en": "Journal Publications", "it": "Pubblicazioni su rivista"}),
    ("conferencepublications",    {"en": "Conference and Workshop Publications",
                                   "it": "Pubblicazioni a conferenze e workshop"}),
    ("awards_and_prizes",         {"en": "Awards and Achievements", "it": "Riconoscimenti"}),
    ("projects",                  {"en": "Projects", "it": "Progetti"}),
    ("tutoring",                  {"en": "Teaching Activities", "it": "Attività didattiche"}),
    ("supervision",               {"en": "Supervisions", "it": "Supervisioni"}),
    ("competitions",              {"en": "Competitions", "it": "Competizioni"}),            # solo CV
]

EDU_TITLE = {"en": "Experience and Education", "it": "Esperienza e formazione"}
SECT = {k: v for k, v in SECTIONS if v}


def notes(k):
    """Nessuna annotazione a destra dei titoli: i conteggi erano ridondanti rispetto
    agli elenchi che introducono. La funzione resta perche i numeri sono derivati e
    rimetterli e una riga."""
    return {}


def _notes_unused(k):
    """Annotazione a destra di ogni titolo di sezione, per file, nelle due lingue."""
    uni = sum(1 for t in D.TEACHING if t["kind"] in ("bsc", "msc", "phd", "techcamp"))
    corp = sum(1 for t in D.TEACHING if t["kind"] == "corporate")
    return {
        "about": {"en": "", "it": ""},
        "research": {"en": "%d areas" % len(D.INTERESTS),
                     "it": "%d aree" % len(D.INTERESTS)},
        "education": {"en": "", "it": ""},
        "thesis": {"en": "PhD cum laude", "it": "dottorato con lode"},
        "journalpublications": {
            "en": "%d entries \\textperiodcentered{} %d under review" % (k["j_tot"], k["j_rev"]),
            "it": "%d voci \\textperiodcentered{} %d in revisione" % (k["j_tot"], k["j_rev"])},
        "conferencepublications": {
            "en": "%d entries \\textperiodcentered{} %d under review" % (k["c_tot"], k["c_rev"]),
            "it": "%d voci \\textperiodcentered{} %d in revisione" % (k["c_tot"], k["c_rev"])},
        "awards_and_prizes": {"en": "", "it": ""},
        "projects": {
            "en": "%d projects \\textperiodcentered{} AI lead in all" % len(D.PROJECTS),
            "it": "%d progetti \\textperiodcentered{} responsabile IA in tutti" % len(D.PROJECTS)},
        "tutoring": {
            "en": "%d courses \\textperiodcentered{} %d university / %d corporate "
                  "\\textperiodcentered{} %d hours" % (len(D.TEACHING), uni, corp, D.TEACHING_HOURS),
            "it": "%d corsi \\textperiodcentered{} %d universitari / %d aziendali "
                  "\\textperiodcentered{} %d ore" % (len(D.TEACHING), uni, corp, D.TEACHING_HOURS)},
        "supervision": {
            "en": "%d MSc \\textperiodcentered{} %d PhD \\textperiodcentered{} co-advisor in all"
                  % (len(D.SUPERVISION), len(D.PHD_SUPERVISION)),
            "it": "%d magistrali \\textperiodcentered{} %d dottorati \\textperiodcentered{} "
                  "co-relatore in tutte" % (len(D.SUPERVISION), len(D.PHD_SUPERVISION))},
        "competitions": {"en": "%d entries" % k["comp"], "it": "%d voci" % k["comp"]},
    }


# ---------------------------------------------------------------- preambolo

BASE, RATIO = 9.0, 4 / 3


def step(k):
    """Corpo del passo k sulla quarta giusta gia usata dal documento (9 - 12 - 16)."""
    return "%.1fpt" % (BASE * RATIO ** k)


_ICON = {"scholar": r"\aiGoogleScholar", "scopus": r"\aiScopus",
         "github": r"\faGithub", "linkedin": r"\faLinkedin", "instagram": r"\faInstagram"}


def header(lang):
    """Nome su una riga sopra il filetto; email e marchi sotto.

    L'email sta a sinistra e i cinque marchi a destra, sulla stessa linea. Busta e
    indirizzo sono piu piccoli dei marchi, e il testo e rialzato: appoggiandolo alla
    stessa linea di base della busta sembrava piu basso, perche il suo occhio medio e
    meta di quello del simbolo.
    """
    first, last = D.PROFILE["name"].split(" ", 1)
    mail = D.PROFILE["email"]
    marks = "".join(
        r"\ic{%s}{2.0em}{%s}{%s}" % (step(2), _ICON[ic], url.replace("&", r"\&"))
        for _lab, url, ic in D.PROFILE["links"])
    return r"""
\vspace*{9mm}   %% il titolo scende un poco dal margine
\begingroup\raggedright
  {\fontsize{%(ls)s}{1em}\headerfont\mdseries\color{graytext}%(first)s\;}%%
  {\fontsize{%(ls)s}{1em}\headerfont\bfseries\color{awesome}%(last)s}%%
  {\fontsize{%(ls)s}{1em}\headerfont\mdseries\color{graytext}, PhD}
\endgroup
\par\vspace{3.0mm}{\color{awesome}\hrule height 1.1pt}\vspace{3.2mm}

\noindent\begin{minipage}[c]{0.70\textwidth}\raggedright
  \href{mailto:%(mail)s}{{\fontsize{%(is)s}{1em}\selectfont\textcolor{awesome}{\faEnvelopeO}}%%
    \hspace{0.40em}\raisebox{0.10em}{\fontsize{%(ms)s}{1em}\bodyfont\color{darktext}%(mail)s}}%%
  \hspace{1.0em}%%
  \href{https://%(site)s}{{\fontsize{%(is)s}{1em}\selectfont\textcolor{awesome}{\faGlobe}}%%
    \hspace{0.40em}\raisebox{0.10em}{\fontsize{%(ms)s}{1em}\bodyfont\color{darktext}%(site)s}}
\end{minipage}\hfill
\begin{minipage}[c]{0.28\textwidth}\raggedleft
  %(marks)s
\end{minipage}

%%%% numero di pagina in basso a destra: corrente su totale.
%%%% \pageref* invece di \pageref: la versione non stellata crea un collegamento e
%%%% hyperref colora il totale d'accento, lasciando i due numeri di colore diverso.
\makecvfooter{}{}{\thepage\;/\;\pageref*{LastPage}}
""" % {"ls": step(3), "is": "14pt", "ms": "10.5pt", "first": first, "last": last,
       "mail": mail, "site": D.PROFILE["site"], "marks": marks}


PREAMBLE = r"""
\usepackage{needspace}

%% Metadati del PDF: senza, un motore di ricerca mostra il nome del file al posto
%% del titolo, e il documento non risulta attribuito a nessuno.
\hypersetup{
  pdftitle={PDFTITLE},
  pdfauthor={Eugenio Lomurno},
  pdfsubject={PDFSUBJECT},
  pdfkeywords={generative deep learning, synthetic data, privacy-preserving machine
    learning, multimodal learning, neural architecture search, healthcare AI,
    Politecnico di Milano, AIRLab},
  pdflang={PDFLANG}
}
\usepackage{lastpage}   % per il totale delle pagine nel piede

% --- stessa tipografia della prima pagina su tutte le altre ---
% La classe usa \bodyfontlight in undici stili diversi e corpi fra 7 e 10 punti: la
% prima pagina era uniforme e le altre no. Qui si riscrivono tutti gli stili con due
% soli corpi, 9 per il testo e 7.5 per il maiuscoletto, e nessun peso chiaro.
\renewcommand*{\paragraphstyle}{\fontsize{9pt}{1.4em}\bodyfont\upshape\color{text}}
\renewcommand*{\entrytitlestyle}[1]{{\fontsize{9pt}{1.2em}\bodyfont\bfseries\color{darktext} #1}}
\renewcommand*{\entrypositionstyle}[1]{{\fontsize{7.5pt}{1em}\bodyfont\scshape\color{graytext} #1}}
\renewcommand*{\entrydatestyle}[1]{{\fontsize{9pt}{1em}\bodyfont\slshape\color{graytext} #1}}
\renewcommand*{\entrylocationstyle}[1]{{\fontsize{9pt}{1em}\bodyfont\slshape\color{awesome} #1}}
\renewcommand*{\descriptionstyle}[1]{{\fontsize{9pt}{1.22em}\bodyfont\upshape\color{text} #1}}
\renewcommand*{\subentrytitlestyle}[1]{{\fontsize{9pt}{1em}\bodyfont\mdseries\color{graytext} #1}}
\renewcommand*{\subentrypositionstyle}[1]{{\fontsize{7.5pt}{1em}\bodyfont\scshape\color{graytext} #1}}
\renewcommand*{\subentrydatestyle}[1]{{\fontsize{7.5pt}{1em}\bodyfont\slshape\color{graytext} #1}}
\renewcommand*{\subentrylocationstyle}[1]{{\fontsize{7.5pt}{1em}\bodyfont\slshape\color{awesome} #1}}
\renewcommand*{\subdescriptionstyle}[1]{{\fontsize{9pt}{1.22em}\bodyfont\upshape\color{text} #1}}
\renewcommand*{\honortitlestyle}[1]{{\fontsize{9pt}{1em}\bodyfont\color{graytext} #1}}
\renewcommand*{\honorpositionstyle}[1]{{\fontsize{9pt}{1em}\bodyfont\bfseries\color{darktext} #1}}
\renewcommand*{\honordatestyle}[1]{{\fontsize{9pt}{1em}\bodyfont\color{graytext} #1}}
\renewcommand*{\honorlocationstyle}[1]{{\fontsize{9pt}{1em}\bodyfont\slshape\color{awesome} #1}}
\renewcommand*{\skilltypestyle}[1]{{\fontsize{9pt}{1em}\bodyfont\bfseries\color{darktext} #1}}
\renewcommand*{\skillsetstyle}[1]{{\fontsize{9pt}{1em}\bodyfont\color{text} #1}}
% gli indirizzi nel carattere del testo: in monospazio sono un terzo carattere estraneo
\urlstyle{same}

% --- marchi accademici come grafica locale, non dal pacchetto academicons ---
% Misurando l'inchiostro a 400 dpi, i glifi academicons uscivano il 16% piu piccoli
% dei FontAwesome accanto. La correzione (1.0em di altezza, -0.13em di appoggio) vale
% solo per questi due PDF: se si usasse il pacchetto, la taratura andrebbe rifatta e
% dipenderebbe dalla versione installata. Cosi il risultato e lo stesso ovunque.
\RequirePackage{graphicx}
\newcommand*{\aiGoogleScholar}{\raisebox{-0.13em}{\includegraphics[height=1.0em]{ai-scholar.pdf}}}
\newcommand*{\aiScopus}{\raisebox{-0.13em}{\includegraphics[height=1.0em]{ai-scopus.pdf}}}
\newcommand*{\aiOrcid}{\textbullet}

% --- marchi dell'intestazione ---
% Ogni marchio in una scatola di larghezza fissa e centrata: i glifi hanno larghezze
% diverse e senza scatola il passo fra un'icona e l'altra sarebbe irregolare.
% #1 corpo, #2 larghezza, #3 glifo, #4 indirizzo
\newcommand{\ic}[4]{{\fontsize{#1}{1em}\selectfont
  \href{#4}{\makebox[#2][c]{\textcolor{awesome}{#3}}}}}

% --- titolo di sezione con annotazione a destra, sopra il filetto ---
% Il filetto passa sotto entrambi, a tutta larghezza: cosi il numero appartiene
% visibilmente alla sezione che introduce e non alla riga di testo che segue.
% \needspace impedisce che un titolo resti da solo in fondo alla pagina.
\newcommand*{\sectionnotestyle}[1]{{\fontsize{7.5pt}{1em}\bodyfont\color{graytext} #1}}
\renewcommand{\cvsection}[2][]{%
  \needspace{5\baselineskip}%
  \vspace{\acvSectionTopSkip}%
  \begingroup
  \sectionstyle{#2}\hfill\sectionnotestyle{#1}%
  \par\vspace{1.1mm}%
  {\color{gray}\hrule height 0.9pt}%
  \endgroup
  \phantomsection
}

% --- righe della sintesi ---
% Prima erano \cventry{\empty}{...} con un \vspace{-7mm} di compensazione: la prima riga
% ereditava lo spazio d'apertura di cventries e restava piu staccata delle altre.
% Come paragrafi normali la spaziatura e una sola, dichiarata qui.
\newcommand{\overviewline}[2]{%
  \par\noindent{\fontsize{9.2pt}{1.4em}\bodyfont\color{graytext}#1}\enskip
  {\fontsize{9.2pt}{1.4em}\bodyfont\bfseries\color{darktext}#2}\par\vspace{1.3mm}}
\let\overviewlast\overviewline
"""


def overview(lang):
    uni = sum(1 for t in D.TEACHING if t["kind"] in ("bsc", "msc", "phd", "techcamp"))
    corp = sum(1 for t in D.TEACHING if t["kind"] == "corporate")
    g = {"en": dict(sec="Overview", when="August 2026", h="h-index (Scholar/Scopus):",
                    cit="Citations (Scholar):", pub="Publications:", pro="Projects:",
                    aw="Awards:", co="Courses:", th="(Co-)supervised theses:",
                    u="university", c="corporate", lead="AI lead role in all five",
                    a1="Leonardo Fibonacci Best Paper Award; PhD thesis \\emph{cum laude}",
                    hh="teaching hours", msc="MSc", phd="PhD"),
         "it": dict(sec="Sintesi", when="agosto 2026", h="h-index (Scholar/Scopus):",
                    cit="Citazioni (Scholar):", pub="Pubblicazioni:", pro="Progetti:",
                    aw="Riconoscimenti:", co="Corsi:", th="Tesi (co-)seguite:",
                    u="universitari", c="aziendali", lead="ruolo di lead IA in tutti e cinque",
                    a1="Leonardo Fibonacci Best Paper Award; tesi di dottorato \\emph{con lode}",
                    hh="ore di didattica", msc="magistrali", phd="dottorati")}[lang]
    acr = ", ".join(p["acro"] for p in D.PROJECTS)
    return (r"""\vspace{5mm}
\cvsection{%(sec)s}
\vspace{2mm}
\begingroup\setlength{\parskip}{0pt}\setlength{\parindent}{0pt}
  \overviewline{%(h)s}{12/9}
  \overviewline{%(cit)s}{330}
  \overviewline{%(pub)s}{30 (13 A+ / Q1)}
  \overviewline{%(pro)s}{%(np)d (%(acr)s) --- %(lead)s}
  \overviewline{%(aw)s}{%(a1)s}
  \overviewline{%(co)s}{%(nt)d --- %(uni)d %(u)s, %(corp)d %(c)s, %(hrs)d %(hh)s}
  \overviewlast{%(th)s}{%(nm)d %(msc)s, %(nd)d %(phd)s}
\endgroup
""" % dict(g, np=len(D.PROJECTS), acr=acr, nt=len(D.TEACHING), uni=uni, corp=corp,
           hrs=D.TEACHING_HOURS, nm=len(D.SUPERVISION), nd=len(D.PHD_SUPERVISION)))


# ---------------------------------------------------------------- sezioni rigenerate

CITY = {"en": "Milan, Italy", "it": "Milano, Italia"}


def tutoring_tex(lang):
    """Didattica generata da data.py: 14 voci, ciascuna con le proprie ore.

    Tre righe per voce: ente, ruolo con edizioni e docente, ore. Le ore erano in coda
    alla riga del ruolo, dove sparivano fra due punti medi; su una riga propria con la
    loro etichetta si leggono, e sono il dato che il conteggio complessivo somma."""
    hours_lab = {"en": "Total teaching hours", "it": "Totale ore di didattica"}[lang]
    o = [r"\cvsection{%s}" % tex(L(SECT["tutoring"], lang)), r"\begin{cventries}", ""]
    for t in D.TEACHING:
        kind = tex(L(D.VOC[t["kind"]], lang))
        # la barra separava due nomi di ente: fra due nomi ci va una virgola
        org = tex(t["org"].replace("&amp;", "&")).replace(" | ", ", ")
        role = tex(L(D.VOC[t["role"]], lang))
        ed = t["editions"]
        edw = tex(L(D.VOC["editions" if ed > 1 else "edition"], lang))
        det = "%s, %d %s" % (role, ed, edw)
        if t.get("prof"):
            prof = {"en": "Professor", "it": "Docente"}[lang]
            det += r" \enskip\textbar\enskip %s: %s" % (prof, tex(t["prof"]))
        per = tex(D.period_of_teaching(t, lang) if hasattr(D, "period_of_teaching")
                  else _period(t, lang))
        o += [r"    \vspace{2mm}", r"    \cventry",
              "        {%s}" % kind,
              "        {%s}" % tex(t["course"]),
              "        {%s}" % CITY[lang],
              "        {%s}" % per,
              "        {",
              r"        \begin{cvitems}",
              "            \\item {%s}" % org,
              "            \\item {%s}" % det,
              "            \\item {%s: %dh}" % (hours_lab, t["hours"]),
              r"        \end{cvitems}",
              "        }", ""]
    o += [r"\end{cventries}", ""]
    return "\n".join(o)


def _period(t, lang):
    pres = {"en": "present", "it": "in corso"}[lang]
    if t.get("ongoing"):
        return "%s -- %s" % (t["from"], pres)
    return t["from"] if str(t.get("to", t["from"])) == str(t["from"]) else \
        "%s -- %s" % (t["from"], t["to"])


def about_tex(lang):
    """About giustificato a tutta larghezza, peso normale, interlinea ampia.

    Sillabazione attiva solo in inglese: i pattern italiani non sono installati e
    applicare quelli inglesi a un testo italiano produce a capo scorretti. Senza
    sillabazione la giustificazione allarga gli spazi fra le parole, che a questa
    misura resta accettabile; con i pattern sbagliati si spezzerebbero le parole male.
    """
    # Lo stesso testo del sito, da data.py, con i collegamenti conservati: un PDF si
    # legge quasi sempre a schermo, e i nomi dei progetti sono il punto naturale da cui
    # arrivare alle loro pagine. Gli <a href> diventano \href prima che tex() tolga i tag.
    def links(s):
        parts, out = re.split(r"<a\s+href='([^']+)'[^>]*>(.*?)</a>", s), []
        for i in range(0, len(parts), 3):
            out.append(tex(parts[i]))
            if i + 2 < len(parts):
                out.append(r"\href{%s}{%s}" % (parts[i + 1], tex(parts[i + 2])))
        return "".join(out)

    paras = [links(p) for p in D.PROFILE["bio"][lang]]

    o = [r"\vspace{2.5mm}",
         r"\begingroup\setlength{\parskip}{0pt}\setlength{\parindent}{0pt}"]
    if lang != "en":
        # \emergencystretch: senza, due righe sbordavano di 6.7 e 19.2 punti nel margine.
        # Concede stiramento supplementare solo alle righe che non si sistemano
        # altrimenti, invece di allentare tutto il paragrafo come farebbe \sloppy.
        o.append(r"\hyphenpenalty=10000 \exhyphenpenalty=10000 \emergencystretch=3em")
    for n, p in enumerate(paras):
        # \looseness=-1 sull'ultimo paragrafo: chiede a TeX di rispezzarlo in una riga
        # in meno. Senza, l'ultima riga italiana conteneva la sola parola "climatica.".
        # Togliere una parola dal testo non bastava: ne servivano una dozzina di
        # caratteri, e questo risolve senza toccare il contenuto.
        # \looseness da solo non basta: TeX lo onora solo se trova una spezzatura
        # ammissibile entro \tolerance, e senza sillabazione non la trova. Alzando la
        # tolleranza e lo stiramento d'emergenza solo per questo paragrafo, ci riesce.
        loose = (r"\tolerance=9999\emergencystretch=6em\looseness=-1"
                 if n == len(paras) - 1 else "")
        o.append(r"  {\fontsize{9pt}{1.5em}\bodyfont\color{darktext}%s%s\par}\vspace{2.1mm}"
                 % (p, loose))
    o += [r"\endgroup", ""]
    return "\n".join(o)


def airlab_tex(lang):
    """Le voci AIRLab in cima a Experience, prese da data.py come sul sito.

    education.tex non e generato da data.py - contiene dettagli che data.py non ha,
    come i mesi e le specializzazioni - quindi le due voci nuove vanno inserite qui,
    non riscrivendo il file: riscriverlo perderebbe quei dettagli.
    """
    out = []
    for e in D.EDUCATION:
        if "AIRLab" not in e["degree"]["en"]:
            continue
        out += [r"  \cventry",
                "    {\\textbf{%s}}" % tex(e["inst"]),
                "    {%s}" % tex(L(e["degree"], lang)),
                "    {%s}" % CITY[lang],
                "    {%s}" % tex(D.period_of(e["period"], lang)),
                "    {}",
                r"    \vspace{2mm}"]
    return "\n".join(out)


def research_tex(lang):
    """Interessi di ricerca: la sezione che il sito ha e il CV no. Stessi sei testi."""
    # Non \cventry: quella macro riserva lo spazio di luogo e date anche quando sono
    # vuoti, e sei voci con due campi vuoti ciascuna sprecavano mezza pagina.
    o = [r"\cvsection{%s}" % tex(L(SECT["research"], lang)),
         r"\vspace{2mm}",
         r"\begingroup\setlength{\parskip}{0pt}\setlength{\parindent}{0pt}"]
    for it in D.INTERESTS:
        o += [r"  \entrytitlestyle{%s}\par\vspace{0.6mm}" % tex(L(it["t"], lang)),
              r"  \descriptionstyle{%s}\par\vspace{2.4mm}" % tex(L(it["d"], lang))]
    o += [r"\endgroup", ""]
    return "\n".join(o)


def supervision_tex(lang):
    """Supervisioni generate da data.py: dottorati prima, poi magistrali."""
    o = [r"\cvsection{%s}" % tex(L(SECT["supervision"], lang)), r"\begin{cventries}", ""]
    lab = {"en": {"phd": "PhD thesis", "msc": "MSc thesis"},
           "it": {"phd": "Tesi di dottorato", "msc": "Tesi magistrale"}}[lang]
    co = {"en": "Co-advisor", "it": "Co-relatore"}[lang]
    rows = ([("phd", e) for e in D.PHD_SUPERVISION] + [("msc", e) for e in D.SUPERVISION])
    for level, e in rows:
        title, student, period, url, kw = e
        who = tex(student)
        if url:
            who += r" - [\href{%s}{link}]" % url
        o += [r"    \vspace{2mm}", r"    \cventry",
              "        {%s}" % who,
              "        {%s}" % tex(title),
              "        {%s}" % CITY[lang],
              "        {%s}" % tex(D.period_of(period, lang)),
              "        {",
              r"        \begin{cvitems}",
              "            \\item {%s \\enskip\\textbar\\enskip %s}" % (lab[level], co),
              "            \\item {Keywords: %s}" % tex(kw),
              r"        \end{cvitems}",
              "        }", ""]
    o += [r"\end{cventries}", ""]
    return "\n".join(o)



def about_body(lang):
    """Il testo di About. Il titolo lo mette page1_block, per colorarlo come gli altri."""
    return about_tex(lang)


# ================================================================ prima pagina
# Due coppie di colonne: About | Sintesi, poi Formazione | Esperienza.
# Quattro corpi soli: 16 titoli, 12 cifre, 9 testo, 7.5 maiuscoletto. Nessun peso chiaro.

UNI = sum(1 for t in D.TEACHING if t["kind"] in ("bsc", "msc", "phd", "techcamp"))
CORP = sum(1 for t in D.TEACHING if t["kind"] == "corporate")
NTH = len(D.SUPERVISION) + len(D.PHD_SUPERVISION)
FS_TITLE, FS_SMALL, FS_INST = "9pt", "9pt", "7.5pt"
EDU2_TITLE = {"en": "Education", "it": "Formazione"}
EXP_TITLE = {"en": "Experience", "it": "Esperienza"}
ABOUT_TITLE = {"en": "About", "it": "Chi sono"}
THESIS_LAB = {"en": "Thesis", "it": "Tesi"}
SUP_LAB = {"en": "Supervisor", "it": "Relatore"}
DEG_IT = {"phd": "Dottorato in Information Technology (con lode)",
          "msc": "Laurea magistrale in Ingegneria Informatica",
          "bsc": "Laurea triennale in Ingegneria dell'Informazione"}
DEG_EN = {"phd": "PhD in Information Technology (cum laude)",
          "msc": "MSc in Computer Science and Engineering",
          "bsc": "BSc in Information Engineering"}
_ICO = {"scholar": r"\aiGoogleScholar", "scopus": r"\aiScopus"}


def _m(i, lang):
    """Cella i delle metriche del sito: cifra, etichetta, sottotitolo."""
    m = D.METRICS[i]
    return (tex(str(m["v"]) + m.get("suf", "")), tex(m["l"][lang]), tex(m["s"][lang]))


def rows(lang):
    """(cifra, etichetta, dettaglio). Tre righe vengono dal sito senza ritocchi
    - Pubblicazioni, Citazioni, Didattica - le altre restano quelle del CV."""
    sup = {"en": ("Supervised Theses",
                  "%d MSc, %d PhD" % (len(D.SUPERVISION), len(D.PHD_SUPERVISION))),
           "it": ("Tesi seguite",
                  "%d magistrali, %d dottorati"
                  % (len(D.SUPERVISION), len(D.PHD_SUPERVISION)))}[lang]
    proj = {"en": "Research Projects", "it": "Progetti di ricerca"}[lang]
    return [
        _m(0, lang),                                   # h-index 12 / 9
        _m(1, lang),                                   # Citazioni 330+
        _m(2, lang),                                   # Pubblicazioni 30 / 13
        ("%d" % len(D.PROJECTS), proj, ""),            # senza elenco degli acronimi
        _m(4, lang),                                   # Didattica 14 / 420+
        ("%d" % NTH, sup[0], sup[1]),
    ]


def awards_list(lang):
    """I riconoscimenti come elenco con la stella in accento, come sul sito.

    Il sito usa il carattere U+2605, che pero non esiste ne in Roboto ne in Source
    Sans: verificato sul cmap dei font. Si usa la stella di FontAwesome, che e nel
    repo e quindi disegna lo stesso glifo su qualunque macchina.
    """
    o = []
    for aw in D.AWARDS:
        o.append(r"{\fontsize{" + FS_SMALL + r"}{1.3em}\bodyfont\color{darktext}"
                 r"\textcolor{awesome}{\faStar}\hspace{0.45em}%s}\par\vspace{1.5mm}"
                 % tex(aw["title"][lang]))
    return "\n".join(o)


AW_TITLE = {"en": "Achievements and Awards", "it": "Riconoscimenti"}

# ---------------------------------------------------------------- Formazione ed Esperienza

EDU_TITLE = {"en": "Education", "it": "Formazione"}
EXP_TITLE = {"en": "Experience", "it": "Esperienza"}
THESIS_LAB = {"en": "Thesis", "it": "Tesi"}
SUP_LAB = {"en": "Supervisor", "it": "Relatore"}


def _fields(blk, n=4):
    """I primi n gruppi di graffe di un \\cventry, contando le annidate.

    Con una regex tipo \\{([^{}]*)\\} il primo campo, {\\textbf{Politecnico di Milano}},
    non viene riconosciuto affatto: gli indici slittano e si finisce per leggere il
    campo sbagliato. Qui si conta l'annidamento."""
    out, i = [], 0
    while len(out) < n and i < len(blk):
        if blk[i] == "{":
            depth, j = 1, i + 1
            while j < len(blk) and depth:
                depth += (blk[j] == "{") - (blk[j] == "}")
                j += 1
            out.append(blk[i + 1:j - 1].strip())
            i = j
        else:
            i += 1
    return out


def _theses():
    """Titolo, relatore e link delle due tesi proprie, da thesis.tex."""
    src = open(os.path.join(SRC, "resume", "thesis.tex"), encoding="utf-8").read()
    out = {}
    for blk in src.split(r"\cventry")[1:]:
        f = _fields(blk, 2)
        kind = "phd" if "PhD" in f[0] else "msc"
        sup = re.search(r"Supervisor:\s*([^}]*)\}", blk)
        url = re.search(r"\\url\{([^}]*)\}", blk)
        out[kind] = (f[1], sup.group(1).strip() if sup else "", url.group(1) if url else "")
    return out


def _entry(title, inst, date, extra=""):
    o = [r"{\fontsize{%s}{1.2em}\bodyfont\bfseries\color{darktext}%s}\par\vspace{0.5mm}"
         % (FS_TITLE, title),
         r"{\fontsize{%s}{1.2em}\bodyfont\color{graytext}"
         r"\addfontfeature{LetterSpace=8}\MakeUppercase{%s}}\par\vspace{0.4mm}" % (FS_INST, inst),
         r"{\fontsize{%s}{1.2em}\bodyfont\slshape\color{graytext}%s}\par" % (FS_SMALL, date)]
    if extra:
        o.append(r"\vspace{0.7mm}" + extra)
    o.append(r"\vspace{2.6mm}")
    return "\n".join(o)


AIRLAB_INST = "AIRLab, DEIB, Politecnico di Milano"

DEG_IT = {"phd": "Dottorato in Information Technology (con lode)",
          "msc": "Laurea magistrale in Ingegneria Informatica",
          "bsc": "Laurea triennale in Ingegneria dell'Informazione"}
DEG_EN = {"phd": "PhD in Information Technology (cum laude)",
          "msc": "MSc in Computer Science and Engineering",
          "bsc": "BSc in Information Engineering"}


def education_col(lang):
    """Titoli di studio, dal dottorato alla triennale.

    Date e tesi vengono da data.py: anni soltanto, come sul sito. Il relatore resta
    l'unico dato che sta solo nel .tex del CV."""
    th = _theses()
    edu = {"phd": None, "msc": None, "bsc": None}
    for e in D.EDUCATION:
        k = e["degree"]["en"][:3].lower()
        if k in edu and edu[k] is None:
            edu[k] = e
    o = []
    for key in ("phd", "msc", "bsc"):
        e = edu[key]
        extra = ""
        if e.get("thesis"):
            body = tex(e["thesis"])
            if e.get("thesis_url"):
                body = r"\href{%s}{%s}" % (e["thesis_url"], body)
            extra = (r"{\fontsize{%s}{1.3em}\bodyfont\color{darktext}" % FS_SMALL +
                     r"\textbf{%s:} %s}\par\vspace{0.3mm}" % (THESIS_LAB[lang], body))
            sup = th.get(key, ("", "", ""))[1]
            if sup:
                extra += ("\n" + r"{\fontsize{" + FS_SMALL +
                          r"}{1.2em}\bodyfont\color{graytext}"
                          r"%s: %s}\par" % (SUP_LAB[lang], tex(sup)))
        deg = (DEG_EN if lang == "en" else DEG_IT)[key]
        # l'affiliazione viene da data.py: sul sito e sul CV deve essere la stessa
        o.append(_entry(tex(deg), tex(e["inst"]), tex(D.period_of(e["period"], lang)), extra))
    return "\n".join(o)


def experience_col(lang):
    """Incarichi, dal piu recente. Le due voci AIRLab vengono da data.py, la terza
    dal CV perche solo li c'e la data al mese."""
    air = [e for e in D.EDUCATION if "AIRLab" in e["degree"]["en"]]
    post = next(e for e in D.EDUCATION if e["degree"]["en"] == "Postdoctoral Fellow")
    out = [_entry(tex(post["degree"][lang]), tex(post["inst"]),
                  tex(D.period_of(post["period"], lang)))]
    for e in reversed(air):                      # Social Media Manager, poi Member
        # i canali vengono da data.py, come sul sito: una fonte sola
        extra = ""
        if e.get("channels"):
            extra = (r"{\fontsize{" + FS_SMALL + r"}{1.25em}\bodyfont\color{darktext}" +
                     r"\hspace{0.9em}".join(
                         r"\href{%s}{\textcolor{awesome}{%s}\hspace{0.32em}%s}"
                         % (u, {"linkedin": r"\faLinkedin",
                                "instagram": r"\faInstagram"}[ic], tex(h))
                         for ic, h, u in e["channels"]) + r"}\par")
        out.append(_entry(tex(e["degree"][lang]), tex(e["inst"]),
                          tex(D.period_of(e["period"], lang)), extra))
    return "\n".join(out)


OVER_TITLE = {"en": "Overview", "it": "Sintesi"}
ABOUT_TITLE = {"en": "About", "it": "Chi sono"}


def _plain_title(t, colour="darktext"):
    """Titolo di sezione, colore scelto.

    Lo \\strut serve: una minipage [t] si aggancia all'altezza della prima riga, e
    quell'altezza dipende dalle lettere. "Education" ha d e t che salgono, "Experience"
    no, quindi i due filetti cadevano sfalsati di 3 punti. Lo strut impone a entrambe
    la stessa altezza di riga, indipendente da cosa c'e scritto.
    """
    return (r"{\fontsize{16pt}{1em}\bodyfont\bfseries\color{%s}\strut %s}"
            r"\par\vspace{1.1mm}{\color{gray}\hrule height 0.9pt}" % (colour, tex(t)))

# --- tre trattamenti ---------------------------------------------------------

def _awards_block(lang, gap="3.4mm"):
    return "\n".join([
        r"\vspace{%s}" % gap,
        r"{\fontsize{9pt}{1.15em}\bodyfont\color{darktext}%s}\par\vspace{1.4mm}"
        % tex(AW_TITLE[lang]),
        awards_list(lang)])


def col_v3(lang):
    """V3: cifra e etichetta sulla stessa riga di base, dettaglio sotto, filetto
    sottile fra una voce e l'altra. La riga di separazione fa il lavoro che nelle
    altre due fa lo spazio bianco, e permette di stringere."""
    o = [r"\begingroup\setlength{\parskip}{0pt}\setlength{\parindent}{0pt}"]
    for n, (v, lab, det) in enumerate(rows(lang)):
        if n:
            o.append(r"{\color{lighttext}\hrule height 0.4pt}\vspace{2.2mm}")
        head = r"{\fontsize{" + FS_TITLE + r"}{1em}\bodyfont\bfseries\color{darktext}%s}" % lab
        if v:
            head += (r"\hfill{\fontsize{%s}{1em}\headerfont\bfseries\color{awesome}%s}"
                     % (step(1), v))
        o.append(head + r"\par\vspace{0.6mm}")
        if det:
            o.append(r"{\fontsize{" + FS_SMALL + r"}{1.3em}\bodyfont\color{graytext}%s}\par" % det)
        o.append(r"\vspace{2.4mm}")
    o.append(r"{\color{lighttext}\hrule height 0.4pt}\vspace{2.2mm}")
    o.append(r"{\fontsize{" + FS_TITLE + r"}{1em}\bodyfont\bfseries\color{darktext}%s}\par\vspace{1.4mm}"
             % tex(AW_TITLE[lang]))
    o.append(awards_list(lang))
    o.append(r"\endgroup")
    return "\n".join(o)

def page1_block(lang):
    """Titolo, poi About | Sintesi, poi Formazione | Esperienza."""
    W = 0.600
    return "\n".join([
        r"\begingroup\renewcommand{\needspace}[1]{}",
        r"\vspace{\acvSectionTopSkip}",
        r"\noindent\begin{minipage}[t]{%.3f\textwidth}" % W,
        _plain_title(ABOUT_TITLE[lang], "awesome"),
        r"\vspace{2mm}\par",
        about_body(lang),
        r"\end{minipage}\hfill",
        r"\begin{minipage}[t]{%.3f\textwidth}" % (0.955 - W),
        _plain_title(OVER_TITLE[lang]),
        r"\vspace{2mm}\par",
        col_v3(lang),
        r"\end{minipage}",
        r"\par\vspace{2.5mm}",
        r"\vspace{\acvSectionTopSkip}",
        r"\noindent\begin{minipage}[t]{%.3f\textwidth}" % W,
        _plain_title(EDU2_TITLE[lang], "awesome"),
        r"\vspace{2mm}\par",
        education_col(lang),
        r"\end{minipage}\hfill",
        r"\begin{minipage}[t]{%.3f\textwidth}" % (0.955 - W),
        _plain_title(EXP_TITLE[lang]),
        r"\vspace{2mm}\par",
        experience_col(lang),
        r"\end{minipage}",
        r"\endgroup",
        r"\par\vspace{2mm}",
    ])



# ---------------------------------------------------------------- ritocchi ai .tex

def patch_projects(txt, lang):
    """I ruoli dei progetti presi da data.py, cosi CV e sito dicono la stessa cosa.
    Nel .tex erano scritti a mano e due su cinque divergevano dal sito."""
    for pr in D.PROJECTS:
        role = tex(L(pr["role"], lang))
        lab = {"en": "Role", "it": "Ruolo"}[lang]
        txt = re.sub(r"(\\item \{)(?:Role|Ruolo): [^}]*(\}[^%]*?" + re.escape(pr["acro"]) + ")",
                     lambda m: m.group(1) + lab + ": " + role + m.group(2), txt)
    # sostituzione per posizione: le voci sono nell'ordine di data.py
    out, i = [], 0
    for chunk in re.split(r"(\\item \{(?:Role|Ruolo): [^}]*\})", txt):
        if re.match(r"\\item \{(?:Role|Ruolo): ", chunk) and i < len(D.PROJECTS):
            lab = {"en": "Role", "it": "Ruolo"}[lang]
            out.append(r"\item {%s: %s}" % (lab, tex(L(D.PROJECTS[i]["role"], lang))))
            i += 1
        else:
            out.append(chunk)
    return "".join(out)


AWARD_EXTRA = {
    "en": r"""
    \vspace{2mm}
    \cventry
        {Politecnico di Milano}
        {PhD Awarded \emph{Cum Laude}}
        {Milan, Italy}
        {May 2025}
        {
        \begin{cvitems}
            \item {Thesis: Adversarial and Generative Deep Learning for Data Privacy in Human-Centered Artificial Intelligence}
            \item {Link: \url{https://www.politesi.polimi.it/handle/10589/238117}}
        \end{cvitems}
        }
""",
    "it": r"""
    \vspace{2mm}
    \cventry
        {Politecnico di Milano}
        {Dottorato conseguito \emph{con lode}}
        {Milano, Italia}
        {maggio 2025}
        {
        \begin{cvitems}
            \item {Tesi: Adversarial and Generative Deep Learning for Data Privacy in Human-Centered Artificial Intelligence}
            \item {Link: \url{https://www.politesi.polimi.it/handle/10589/238117}}
        \end{cvitems}
        }
""",
}


def patch_awards(txt, lang):
    """La lode manca fra i riconoscimenti: c'e solo il premio Fibonacci."""
    return txt.replace(r"\end{cventries}", AWARD_EXTRA[lang] + r"\end{cventries}", 1)


# ---------------------------------------------------------------- costruzione

# ---------------------------------------------------------------- surrogati di anteprima
# Il sandbox non ha sourcesanspro, fontawesome e academicons e non puo installarli
# (niente root, e il mirror TeX Live e a una release diversa). Questi file esistono solo
# nella cartella di compilazione, mai nel repo: servono a vedere l'impaginato, non a
# sostituire i pacchetti veri, che sulla macchina dell'utente ci sono.
ROBOTO = ("Path=fonts/,Extension=.ttf,UprightFont=*-%s,ItalicFont=*-%sItalic,"
          "BoldFont=*-%s,BoldItalicFont=*-%sItalic")

SHIMS = {
    "sourcesanspro.sty": r"""\ProvidesPackage{sourcesanspro}[surrogato di anteprima]
\DeclareOption*{}\ProcessOptions\relax
\RequirePackage{fontspec}
\newfontfamily\sourcesanspro[""" + ROBOTO % ("Regular", "", "Bold", "Bold") + r"""]{Roboto}
\newfontfamily\sourcesansprolight[""" + ROBOTO % ("Light", "Light", "Medium", "Medium") + r"""]{Roboto}
\setmainfont[""" + ROBOTO % ("Regular", "", "Bold", "Bold") + r"""]{Roboto}
""",
    "fontawesome.sty": r"""\ProvidesPackage{fontawesome}[surrogato di anteprima]
\RequirePackage{fontspec}
\newfontfamily\FAshim[Path=fonts/,Extension=.ttf]{FontAwesome}
\newcommand*{\faStar}{{\FAshim\symbol{"F005}}}
\newcommand*{\faGlobe}{{\FAshim\symbol{"F0AC}}}
\newcommand*{\faLinkedin}{{\FAshim\symbol{"F0E1}}}
\newcommand*{\faInstagram}{{\FAshim\symbol{"F16D}}}
\newcommand*{\faEnvelopeO}{{\FAshim\symbol{"F003}}}
\newcommand*{\faGithub}{{\FAshim\symbol{"F09B}}}
\newcommand*{\faGitlab}{{\FAshim\symbol{"F296}}}
\newcommand*{\faHome}{{\FAshim\symbol{"F015}}}
\newcommand*{\faPhone}{{\FAshim\symbol{"F095}}}
\newcommand*{\faReddit}{{\FAshim\symbol{"F1A1}}}
\newcommand*{\faSkype}{{\FAshim\symbol{"F17E}}}
\newcommand*{\faStackOverflow}{{\FAshim\symbol{"F16C}}}
\newcommand*{\faTwitter}{{\FAshim\symbol{"F099}}}
\newcommand*{\faXingSquare}{{\FAshim\symbol{"F169}}}
""",
    # i tre marchi accademici sono seguiti dalla loro etichetta testuale: senza glifo
    # la riga resta leggibile, e nell'anteprima si vede un punto al loro posto
    "academicons.sty": r"""\ProvidesPackage{academicons}[surrogato di anteprima]
\newcommand*{\aiGoogleScholar}{\textbullet}
\newcommand*{\aiScopus}{\textbullet}
\newcommand*{\aiOrcid}{\textbullet}
""",
}


def next_dir():
    os.makedirs(OUT, exist_ok=True)
    n = 1
    while os.path.exists(os.path.join(OUT, "b%02d" % n)):
        n += 1
    d = os.path.join(OUT, "b%02d" % n)
    return d


def build(lang, base, preview=True):
    d = os.path.join(base, lang)
    shutil.copytree(SRC, d)
    if preview:
        # Un surrogato si scrive solo se il pacchetto vero manca davvero. Scriverlo
        # sempre significherebbe coprire Source Sans Pro con Roboto anche su una
        # installazione TeX completa, e il CV uscirebbe con il carattere sbagliato
        # senza che nulla lo segnali.
        for name, body in SHIMS.items():
            if name == "academicons.sty":
                continue                      # non piu caricato: i glifi sono ai-*.pdf
            found = subprocess.run(["kpsewhich", name], capture_output=True, text=True)
            if found.stdout.strip():
                continue
            print("   %s non installato: uso il surrogato (Roboto al posto del font vero)"
                  % name)
            open(os.path.join(d, name), "w", encoding="utf-8").write(body)
    k = counts()
    NOTE = notes(k)

    # --- traduzione dei file che non rigenero io ---
    # Va fatta PRIMA di inserire le annotazioni: la tabella cerca \cvsection{Titolo} e
    # dopo l'inserimento il titolo non e piu adiacente alla graffa aperta.
    tr = (lambda s: s) if lang == "en" else apply_tr
    if lang != "en":
        for fp in [os.path.join(d, "resume.tex")] + glob.glob(os.path.join(d, "resume", "*.tex")):
            body = open(fp, encoding="utf-8").read()
            open(fp, "w", encoding="utf-8").write(apply_tr(body))

    # --- resume.tex: palette, preambolo, titolo dei file ---
    p = os.path.join(d, "resume.tex")
    t = open(p, encoding="utf-8").read()
    for name, key in (("awesome", "accent"), ("darktext", "dark"), ("text", "dark"),
                      ("graytext", "gray"), ("lighttext", "light"), ("pagebg", "page"),
                      ("myblue", "accent")):
        t = re.sub(r"\\definecolor\{%s\}\{HTML\}\{[0-9A-Fa-f]{6}\}" % name,
                   lambda m, v=PAL[key], n=name: r"\definecolor{%s}{HTML}{%s}" % (n, v), t)
    # il pacchetto academicons non serve piu: i due glifi sono file locali
    # il blocco di autorizzazione al trattamento dati non passa da nessuno stile della
    # classe: restava al corpo predefinito, 10.95pt, unico nel documento
    t = re.sub(r"\n(Autorizzo [^\n]+)",
               lambda m: "\n{\\fontsize{9pt}{1.35em}\\bodyfont\\color{graytext}" + m.group(1) + "\\par}",
               t)
    t = t.replace(r"\usepackage{academicons}", "% academicons: sostituito da ai-*.pdf")
    meta = {"en": dict(pdftitle="Eugenio Lomurno - Curriculum Vitae",
                       pdfsubject="Curriculum vitae of Eugenio Lomurno, "
                                  "postdoctoral fellow at AIRLab, Politecnico di Milano",
                       pdflang="en"),
            "it": dict(pdftitle="Eugenio Lomurno - Curriculum Vitae",
                       pdfsubject="Curriculum vitae di Eugenio Lomurno, "
                                  "assegnista di ricerca all'AIRLab, Politecnico di Milano",
                       pdflang="it")}[lang]
    # sostituzione letterale, non formattazione: PREAMBLE e pieno di % che in LaTeX
    # aprono un commento e in Python sarebbero segnaposto
    pre = PREAMBLE
    for k, v in meta.items():
        pre = pre.replace(k.upper(), v)
    t = t.replace(r"\begin{document}", pre + "\n" + r"\begin{document}", 1)
    # via la foto e via l'intestazione della classe, sostituita dalla nostra
    t = t.replace(r"\ifcvphoto\photo[circle,edge,left]{profile.jpg}\fi", "")
    t = t.replace(r"{\hypersetup{urlcolor=darktext}\makecvheader[C]}\hypersetup{urlcolor=myblue}",
                  header(lang) + "\n" + page1_block(lang))
    # --- ordine delle sezioni, uguale a quello del sito ---
    # Riscrivo l'elenco degli \input invece di riordinare le righe esistenti: cosi
    # l'ordine e dichiarato in un posto solo, SECTIONS, e vale per entrambe le lingue.
    # Prima pagina: solo titolo, About e Overview, distribuiti sull'altezza.
    # I due \vfill si dividono lo spazio libero, quindi About cade a circa un terzo e
    # l'Overview si appoggia al fondo; il \newpage e cio che rende misurabile lo spazio.
    # Spazi fissi fra i tre blocchi e tutto il residuo in fondo: i \vfill di prima
    # dividevano lo spazio in parti uguali e spingevano About e Sintesi a meta e in
    # fondo alla pagina. Ora stanno in alto e il vuoto resta sotto.
    inputs = "\n".join(r"\input{resume/%s}" % f for f, _ in SECTIONS)
    t = t.replace("% \\input{resume/about}\n", "")     # riga commentata, ora superflua
    i = t.index(r"\input{resume/education}")
    j = t.rindex(r"\input{resume/")
    j = t.index("\n", j)
    # tengo le righe commentate fuori: vengono sostituite in blocco
    t = t[:t.rindex("\n", 0, i) + 1] + inputs + t[j:]
    open(p, "w", encoding="utf-8").write(t)

    # --- sezioni rigenerate da data.py ---
    for name, body in (("tutoring", tutoring_tex(lang)), ("supervision", supervision_tex(lang))):
        open(os.path.join(d, "resume", name + ".tex"), "w", encoding="utf-8").write(body)


    # --- titolo del sito e annotazione a destra, sezione per sezione ---
    # La chiave e il nome del file, non il testo del titolo: dopo la traduzione il testo
    # cambia e cercarlo significava tenere due tabelle allineate a mano.
    for fname, patch in (("projects", patch_projects), ("awards_and_prizes", patch_awards)):
        fp = os.path.join(d, "resume", fname + ".tex")
        body = open(fp, encoding="utf-8").read()
        open(fp, "w", encoding="utf-8").write(patch(body, lang))

    if lang == "it":
        fp = os.path.join(d, "resume", "projects.tex")
        body = open(fp, encoding="utf-8").read()
        open(fp, "w", encoding="utf-8").write(body.replace(
            "Joint Research Platform (JRP) between Politecnico di Milano and EssilorLuxottica",
            "Joint Research Platform (JRP) tra Politecnico di Milano e EssilorLuxottica"))

    for fname, title in SECTIONS:
        fp = os.path.join(d, "resume", fname + ".tex")
        if not os.path.exists(fp):
            continue
        s = open(fp, encoding="utf-8").read()
        # [^{}]* e non [^}]*: con il secondo, un titolo che contiene una graffa annidata
        # come \cvsection{Overview \textcolor{darktext}{(agosto 2026)}} veniva troncato
        # alla prima chiusura e restava una graffa orfana. Cosi, semmai, non sostituisce.
        if title:
            s = re.sub(r"\\cvsection\{[^{}]*\}", r"\\cvsection{%s}" % tex(L(title, lang)),
                       s, count=1)
        n = NOTE.get(fname, {}).get(lang, "")
        if n:
            s = re.sub(r"\\cvsection\{([^{}]*)\}",
                       lambda m: r"\cvsection[%s]{%s}" % (n, m.group(1)), s, count=1)
        open(fp, "w", encoding="utf-8").write(s)

    return d


def compile_pdf(d):
    for _ in range(2):
        r = subprocess.run(["xelatex", "-interaction=nonstopmode", "resume.tex"],
                           cwd=d, capture_output=True, text=True)
    pdf = os.path.join(d, "resume.pdf")
    if not os.path.exists(pdf):
        return None, r
    # xelatex esce con codice 0 anche quando una macro non e stata definita: gli
    # errori stanno nel log, non nel codice d'uscita.
    log = open(os.path.join(d, "resume.log"), encoding="utf-8", errors="replace").read()
    for e in dict.fromkeys(l for l in log.splitlines() if l.startswith("! ")):
        print("   ERRORE:", e)
    return pdf, r


DEST = ROOT
NAMES = {"en": "CV_Eugenio_Lomurno_EN.pdf", "it": "CV_Eugenio_Lomurno_IT.pdf"}


def publish_to(pdf, name):
    """Copia il PDF nella radice, togliendo prima il vecchio.

    Sovrascrivere direttamente fallisce con PermissionError quando la cartella e
    sincronizzata (OneDrive, Dropbox) e il file e aperto o bloccato dal client di
    sincronizzazione: il vecchio PDF resta al suo posto e sembra che sia tutto a
    posto. Cancellare prima aggira il blocco; se non basta, meglio dirlo forte.
    """
    dst = os.path.join(DEST, name)
    try:
        if os.path.exists(dst):
            os.remove(dst)
        shutil.copy(pdf, dst)
        return True
    except (PermissionError, OSError) as e:
        print("   NON pubblicato: %s (%s)" % (name, e.__class__.__name__))
        print("   Il file e bloccato: chiudilo, oppure metti in pausa la sincronizzazione.")
        return False

if __name__ == "__main__":
    import sys
    base = next_dir()
    os.makedirs(base)
    publish = "--publish" in sys.argv
    for lang in ("en", "it"):
        d = build(lang, base)
        pdf, r = compile_pdf(d)
        print(lang, "->", pdf or "FALLITO")
        if not pdf:
            print("\n".join(r.stdout.splitlines()[-40:]))
        elif publish:
            ok = publish_to(pdf, NAMES[lang])
            if lang == "en":
                ok &= publish_to(pdf, "CV_Eugenio_Lomurno.pdf")
            if ok:
                print("   pubblicato in", NAMES[lang])
            else:
                sys.exit(1)
