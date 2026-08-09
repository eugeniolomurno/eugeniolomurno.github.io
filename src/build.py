# -*- coding: utf-8 -*-
"""Costruisce le tre varianti di struttura (bilingui, palette Rame) e la pagina di confronto contatori."""
import io, os, re
import data as D
from styles import RAME, vars_block, CSS, CSS_METRICS, JS, JS_UI, HEAD_SCRIPT

import os as _os
# Percorsi ricavati dalla posizione di questo file: il generatore funziona
# ovunque sia il repository, senza percorsi assoluti da aggiornare a mano.
_HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.dirname(_HERE)                     # la radice del sito

OUT = _os.path.join(ROOT, "prove")
T = RAME


def a(s):
    """Valore sicuro per attributo HTML."""
    return str(s).replace('"', "&quot;")


def bi(tag, d, cls="", extra=""):
    """Elemento bilingue: testo EN nel documento, IT nell'attributo."""
    c = ' class="%s"' % cls if cls else ""
    e = " " + extra if extra else ""
    return '<%s%s%s data-en="%s" data-it="%s">%s</%s>' % (
        tag, c, e, a(d["en"]), a(d["it"]), d["en"], tag)


LAYOUTS = {
    "1-completo": {
        "name": {"en": "Full", "it": "Completo"},
        "note": {"en": "everything open, one entry per line",
                 "it": "tutto aperto, una voce per riga"},
        "order": ["about", "metrics", "education", "research", "publications", "awards",
                  "projects", "teaching", "supervision", "contact"],
        "collapse": {"supervision": None}, "cols": {}, "metrics": "m-card", "roles": "rule",
    },
    "2-compatto": {
        "name": {"en": "Compact", "it": "Compatto"},
        "note": {"en": "long lists collapsed, projects up front",
                 "it": "elenchi lunghi collassati, progetti in alto"},
        "order": ["about", "metrics", "education", "research", "publications", "awards",
                  "projects", "teaching", "supervision", "contact"],
        "collapse": {"teaching": 4, "supervision": None}, "cols": {}, "metrics": "m-card", "roles": "rule",
    },
    "3-denso": {
        "name": {"en": "Dense", "it": "Denso"},
        "note": {"en": "long lists in two columns, awards up front",
                 "it": "elenchi su due colonne, premi in alto"},
        "order": ["about", "metrics", "education", "research", "publications", "awards",
                  "projects", "teaching", "supervision", "contact"],
        "collapse": {"supervision": None}, "cols": {"teaching": 2}, "metrics": "m-card", "roles": "rule",
    },
}

# la barra mostra cinque macro-aree, non le nove sezioni
NAV_GROUPS = [
    ("about",       "nav_about",       ["about", "metrics", "education"]),
    ("research",    "nav_research",    ["research", "publications", "awards"]),
    ("projects",    "nav_projects",    ["projects"]),
    ("teaching",    "nav_teaching",    ["teaching"]),
    ("supervision", "nav_supervision", ["supervision"]),
]

CHEV = ('<svg class="chev" width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="3" stroke-linecap="round"><path d="M6 9l6 6 6-6"/></svg>')

from icons_academic import ACADEMICONS

# Scholar e Scopus vengono da academicons, lo stesso pacchetto del CV LaTeX:
# sono i marchi reali, non ridisegnati a mano.
ICONS = {
    "scholar": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="%s"/></svg>'
               % ACADEMICONS["scholar"],
    "scopus": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="%s"/></svg>'
              % ACADEMICONS["scopus"],
    "linkedin": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
                '<path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67'
                'H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43'
                'a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zm1.78 13.02H3.56V9h3.56v11.45zM22.22 0H1.77'
                'C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73'
                'C24 .77 23.2 0 22.22 0z"/></svg>',
    "github": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 0'
              'c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577'
              'v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756'
              '-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 '
              '3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 '
              '1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 '
              '3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 '
              '2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 '
              '1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 '
              '0-6.627-5.373-12-12-12z"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" '
                 'aria-hidden="true"><rect x="2.6" y="2.6" width="18.8" height="18.8" rx="5.3"/>'
                 '<circle cx="12" cy="12" r="4.2"/>'
                 '<circle cx="17.6" cy="6.5" r="1.15" fill="currentColor" stroke="none"/></svg>',
}

THEME_ICONS = (
    '<svg class="ic-moon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">'
    '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>'
    '<svg class="ic-sun" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/>'
    '<path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2'
    'M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>')


# ---------------------------------------------------------------- contatori
def metrics_html(style):
    o = io.StringIO(); w = o.write
    ms = D.METRICS

    def val(m):
        # il numero animato e la nota tra parentesi restano separati: il contatore
        # deve poter parsare solo cifre
        num = '<span data-count="%s"%s>%s%s</span>' % (
            a(m["v"]), (' data-suffix="%s"' % a(m["suf"])) if m.get("suf") else "",
            m["v"], m.get("suf", ""))
        note = (" " + bi("span", m["note"], "mv-note")) if m.get("note") else ""
        return '<span class="mv">%s%s</span>' % (num, note)

    if style == "m-hero3":
        w('<div class="m-hero3"><div class="top">')
        for m in ms[:3]:
            w('<div class="mi">%s%s%s</div>' % (val(m), bi("span", m["l"], "ml"), bi("span", m["s"], "ms")))
        w('</div><div class="rest">')
        for m in ms[3:]:
            w('<div class="mi">%s%s</div>' % (val(m), bi("span", m["l"], "ml")))
        w('</div></div>')
        return o.getvalue()

    if style == "m-inline":
        w('<div class="m-inline">')
        for i, m in enumerate(ms):
            if i:
                w('<span class="sep">/</span>')
            w('<span class="mi">%s %s</span>' % (val(m), bi("span", m["l"], "ml")))
        w('</div>')
        return o.getvalue()

    w('<div class="%s">' % style)
    for m in ms:
        w('<div class="mi">%s%s%s</div>' % (val(m), bi("span", m["l"], "ml"), bi("span", m["s"], "ms")))
    w('</div>')
    return o.getvalue()


# ---------------------------------------------------------------- sezioni
def rows_teaching(w, items):
    for e in items:
        org_en, det_en, per_en = D.teaching_labels(e, "en")
        org_it, det_it, per_it = D.teaching_labels(e, "it")
        w('<div class="row compact reveal"><div class="row-main">')
        w('<div class="titleline"><span class="rt">%s</span></div>' % e["course"])
        w('<div class="rm" data-en="%s" data-it="%s">%s</div>' % (
            a("%s | %s" % (org_en, det_en)), a("%s | %s" % (org_it, det_it)),
            "%s | %s" % (org_en, det_en)))
        w('</div><div class="row-side" data-en="%s" data-it="%s">%s</div></div>' % (
            a(per_en), a(per_it), per_en))


def rows_supervision(w, items, style="plain"):
    """Titolo, poi studente, poi tre parole chiave."""
    for level, title, student, period, url, kw in items:
        w('<div class="row compact reveal"><div class="row-main"><div class="titleline">')
        if style == "tag":
            w(bi("span", D.UI["tag_" + level], "tag " + ("j" if level == "phd" else "c")))
        w('<span class="rt">%s</span>' % title)          # niente link: la tesi non e sempre accessibile
        w('</div><div class="rm">%s</div>' % student)
        w('<div class="kw">%s: %s</div>' % (bi("span", D.UI["keywords"], "kw-lab"), kw))
        w('</div><div class="row-side" data-en="%s" data-it="%s">%s</div></div>'
          % (a(D.period_of(period, "en")), a(D.period_of(period, "it")),
             D.period_of(period, "en")))


def section(w, key, lay):
    if key == "metrics":
        w('<section class="nb reveal">%s</section>\n' % metrics_html(lay["metrics"]))
        return

    w('<section id="%s">' % key)
    w(bi("h2", D.UI["t_" + key], "reveal"))

    if key == "about":
        for i in range(len(D.PROFILE["bio"]["en"])):
            w(bi("p", {"en": D.PROFILE["bio"]["en"][i], "it": D.PROFILE["bio"]["it"][i]}, "lede reveal"))

    elif key == "research":
        w('<div class="grid">')
        for it in D.INTERESTS:
            w('<div class="icard reveal">%s%s</div>' % (bi("h3", it["t"]), bi("p", it["d"])))
        w('</div>')

    elif key == "publications":
        for kind, title, credit, url in D.PUBLICATIONS:
            w('<div class="row reveal"><div class="row-main">')
            # il tipo sta sempre su una riga propria, sopra il titolo
            w('<div class="taglead">%s</div>'
              % bi("span", D.UI["tag_j" if kind == "j" else "tag_c"], "tag " + kind))
            w('<div class="titleline">')
            w('<a class="rt" href="%s" target="_blank" rel="noopener">%s</a>' % (url, title))
            w('</div><div class="rm">%s</div>' % credit)
            w('</div></div>')
        w('<p class="more reveal"><a href="%s" target="_blank" rel="noopener" '
          'data-en="%s &rarr;" data-it="%s &rarr;">%s &rarr;</a></p>' % (
              D.PROFILE["links"][0][1], a(D.UI["all_pubs"]["en"]), a(D.UI["all_pubs"]["it"]),
              D.UI["all_pubs"]["en"]))

    elif key == "projects":
        for p in D.PROJECTS:
            w(project_row(p, lay.get("roles", "badge")))

    elif key == "supervision":
        # filetto etichettato per livello; le magistrali concluse restano collassate
        phd = [e for e in D.ALL_SUPERVISION if e[0] == "phd"]
        msc = [e for e in D.ALL_SUPERVISION if e[0] == "msc"]
        msc_on = [e for e in msc if isinstance(e[3], dict)]
        msc_off = [e for e in msc if not isinstance(e[3], dict)]
        w(bi("div", D.UI["div_phd"], "divlab reveal"))
        rows_supervision(w, phd)
        w(bi("div", D.UI["div_msc"], "divlab reveal"))
        rows_supervision(w, msc_on)
        if msc_off:
            n = len(msc)
            w('<details class="more-wrap reveal"><summary>')
            w('<span class="lbl-shut" data-en="%s" data-it="%s">%s</span>' % (
                a(D.UI["show_all_theses"]["en"] % n), a(D.UI["show_all_theses"]["it"] % n),
                D.UI["show_all_theses"]["en"] % n))
            w(bi("span", D.UI["show_fewer"], "lbl-open"))
            w(CHEV + '</summary>')
            rows_supervision(w, msc_off)
            w('</details>')

    elif key == "teaching":
        items = D.TEACHING
        fn = rows_teaching
        coll, cols = lay["collapse"].get(key), lay["cols"].get(key)
        k = "show_all_courses"
        if coll:
            fn(w, items[:coll])
            w('<details class="more-wrap reveal"><summary>')
            w('<span class="lbl-shut" data-en="%s" data-it="%s">%s</span>' % (
                a(D.UI[k]["en"] % len(items)), a(D.UI[k]["it"] % len(items)), D.UI[k]["en"] % len(items)))
            w(bi("span", D.UI["show_fewer"], "lbl-open"))
            w(CHEV + '</summary>')
            fn(w, items[coll:])
            w('</details>')
        elif cols:
            w('<div class="twocol">'); fn(w, items); w('</div>')
        else:
            fn(w, items)

    elif key == "education":
        # Due colonne come sul CV: Formazione a sinistra, Esperienza a destra.
        # Sotto gli 860px si impilano: a meta larghezza le righe sarebbero troppo corte.
        exp = [e for e in D.EDUCATION
               if "AIRLab" in e["degree"]["en"] or e["degree"]["en"] == "Postdoctoral Fellow"]
        edu = [e for e in D.EDUCATION if e not in exp]
        # dal piu recente, come sul CV: in data.py l'appartenenza al laboratorio sta in
        # cima perche e la piu antica, e senza riordinare la colonna partirebbe dal 2019
        exp.sort(key=lambda e: re.search(r"\d{4}", e["period"]["en"]).group(0), reverse=True)

        def col(title, items):
            w('<div class="twocol-c">')
            w(bi("div", title, "colh reveal"))
            for e in items:
                w('<div class="row compact reveal"><div class="row-main"><div class="titleline">')
                w(bi("span", e["degree"], "rt"))
                w('</div><div class="rm">%s</div>' % e["inst"])
                if e.get("thesis"):
                    w('<div class="kw">%s: <a href="%s" target="_blank" rel="noopener">%s</a></div>'
                      % (bi("span", D.UI["thesis_lab"], "kw-lab"), e["thesis_url"], e["thesis"]))
                w('</div>')
                w(bi("div", e["period"], "row-side"))
                w('</div>')
            w('</div>')

        w('<div class="twocol">')
        col(D.UI["col_education"], edu)
        col(D.UI["col_experience"], exp)
        w('</div>')

    elif key == "contact":
        w(bi("p", D.UI["contact_p"], "lede reveal"))
        w('<p class="reveal" style="margin:22px 0 0">'
          '<a class="btn" href="mailto:%s?subject=Contact%%20from%%20your%%20website" '
          'data-en="%s" data-it="%s">%s</a></p>'
          % (D.PROFILE["email"], a(D.UI["email_btn"]["en"]), a(D.UI["email_btn"]["it"]),
             D.UI["email_btn"]["en"]))

    elif key == "awards":
        for aw in D.AWARDS:
            w('<div class="row reveal"><div class="row-main"><div class="titleline">')
            w('<span class="rt"><span class="star-ic">&#9733;</span> '
              '<span data-en="%s" data-it="%s">%s</span></span>' % (
                  a(aw["title"]["en"]), a(aw["title"]["it"]), aw["title"]["en"]))
            w('</div>')
            w(bi("div", aw["where"], "rm"))
            w('<div class="rx"><a href="%s" target="_blank" rel="noopener">%s</a></div>' % (aw["url"], aw["paper"]))
            w('</div></div>')

    w('</section>\n')


def head(title_suffix=""):
    o = io.StringIO(); w = o.write
    w('<!DOCTYPE html>\n<html lang="en" data-theme="light">\n<head>\n<meta charset="UTF-8">\n')
    w('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    w('<title>%s — %s%s</title>\n' % (D.PROFILE["name"], D.PROFILE["role"]["en"], title_suffix))
    w('<script>%s</script>\n' % HEAD_SCRIPT)
    w('<link rel="preconnect" href="https://fonts.googleapis.com">\n')
    w('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n')
    w('<link href="%s" rel="stylesheet">\n<style>\n' % T["gfont"])
    w(vars_block(":root", T["light"]) + "\n")
    w(vars_block('html[data-theme="dark"]', T["dark"]) + "\n")
    w(":root{--fd:%s;--fb:%s;--r:10px}\n" % (T["display"], T["body"]))
    w(CSS); w(CSS_METRICS)
    return o.getvalue()


def project_row(p, style="badge"):
    """Acronimo, titolo esteso, riga info. `style` cambia solo come compare il ruolo."""
    o = io.StringIO(); w = o.write
    w('<div class="row proj reveal"><div class="row-main">')

    if style == "eyebrow":
        w(bi("div", p["role"], "role-eyebrow"))

    w('<div class="titleline">')
    if style == "badge":
        w(bi("span", p["role"], "role-badge"))
    elif style == "soft":
        w(bi("span", p["role"], "role-soft"))
    w('<a class="rt" href="%s" target="_blank" rel="noopener">%s</a>' % (p["url"], p["acro"]))
    w('</div>')

    w('<div class="proj-full">%s</div>' % p["full"])
    w(bi("div", p["info"], "rm"))

    if style == "line":
        w('<div class="role-line"><span class="role-key" data-en="Role" data-it="Ruolo">Role</span>'
          '%s</div>' % bi("span", p["role"], "role-val"))
    elif style == "rule":
        w(bi("div", p["role"], "role-rule"))
    w('</div>')

    w('<div class="row-side">')
    w(bi("div", p["period"]))
    if style == "side":
        w(bi("div", p["role"], "role-side"))
    w('</div></div>')
    return o.getvalue()


def social_icons(cls="social-panel"):
    out = ['<div class="%s">' % cls]
    for lab, url, ic in D.PROFILE["links"]:
        out.append('<a href="%s" target="_blank" rel="noopener" aria-label="%s" title="%s">%s</a>'
                   % (url, lab, lab, ICONS[ic]))
    out.append('</div>')
    return "".join(out)


def topbar(w, navkeys):
    w('<div class="topbar"><div class="tb-in">')
    w('<a class="brand" href="#top">Eugenio Lomurno</a>')
    if navkeys:
        w('<nav class="nav">')
        for anchor, key, members in NAV_GROUPS:
            if anchor not in navkeys:
                continue
            w('<a href="#%s" data-sections="%s" data-en="%s" data-it="%s">%s</a>' % (
                anchor, " ".join(members), a(D.UI[key]["en"]), a(D.UI[key]["it"]), D.UI[key]["en"]))
        w('</nav>')
    w('<div class="ctrls">')
    w(social_icons("social"))
    w('<button class="tbtn js-lang" aria-label="Switch language">IT</button>')
    w('<button class="tbtn js-theme" aria-label="Toggle theme">%s</button>' % THEME_ICONS)
    if navkeys:
        # la tendina chiude la barra a destra, dopo il tema, staccata da un filetto
        w('<details class="navmenu" id="navMenu"><summary aria-label="Sections">'
          '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
          'stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
          '</summary><div class="panel">')
        for anchor, key, _m in NAV_GROUPS:
            if anchor not in navkeys:
                continue
            w('<a href="#%s" data-en="%s" data-it="%s">%s</a>' % (
                anchor, a(D.UI[key]["en"]), a(D.UI[key]["it"]), D.UI[key]["en"]))
        w('<div class="tools">%s</div>' % social_icons())
        w('<div class="tools">')
        w('<button class="tbtn js-lang" aria-label="Switch language">IT</button>')
        w('<button class="tbtn js-theme" aria-label="Toggle theme">%s</button>' % THEME_ICONS)
        w('</div></div></details>')
    w('</div>')
    w('</div></div>\n')


def render_layout(key, lay):
    o = io.StringIO(); w = o.write
    w(head(" (%s)" % lay["name"]["en"]))
    w("\n</style>\n</head>\n<body>\n")
    topbar(w, [k for k in lay["order"] if k != "metrics"])
    w('<div class="wrap" id="top">\n<header class="hero">')
    # foto a sinistra: prima nel DOM, cosi l'ordine di lettura coincide con quello visivo
    # ritratto incorporato: un <img src="photo.jpg"> dipende da un file accanto
    # all'HTML, e basta aprire la pagina altrove perche resti il testo alternativo.
    # A 400 px il file pesa 25 KB, che incorporati diventano 33: si puo permettere.
    _photo = open(_os.path.join(_HERE, "photo_data.txt"), encoding="ascii").read().strip()
    w('<div class="hero-img reveal"><img src="%s" alt="%s" width="172" height="172">'
      '</div>' % (_photo, D.PROFILE["name"]))
    w('<div class="hero-txt">')
    w(bi("div", D.PROFILE["affiliation"], "eyebrow reveal"))
    w('<h1 class="reveal">%s</h1>' % D.PROFILE["name"])
    w(bi("p", D.PROFILE["role"], "role reveal"))
    if D.PROFILE["tagline"]:
        w(bi("p", D.PROFILE["tagline"], "tag-line reveal"))
    w('<div class="cta reveal">')
    # il nome del file lo vede chi scarica: deve dire chi e cosa, non da quale prototipo viene
    w('<a class="btn" href="CV_Eugenio_Lomurno_EN.pdf" download data-en="%s" data-it="%s" '
      'data-en-attr="href:CV_Eugenio_Lomurno_EN.pdf" '
      'data-it-attr="href:CV_Eugenio_Lomurno_IT.pdf">%s</a>' % (
          a(D.UI["cv_btn"]["en"]), a(D.UI["cv_btn"]["it"]), D.UI["cv_btn"]["en"]))
    w('<a class="btn ghost" href="mailto:%s" data-en="%s" data-it="%s">%s</a>' % (
        D.PROFILE["email"], a(D.UI["contact_btn"]["en"]), a(D.UI["contact_btn"]["it"]),
        D.UI["contact_btn"]["en"]))
    w('</div></div>')   # i collegamenti vivono nella barra in alto, non nell'hero
    w('</header>\n')
    for k in lay["order"]:
        section(w, k, lay)
    w('<footer>')
    w(bi("span", D.UI["loc"]))
    w('<span class="dot">|</span><a href="mailto:%s">%s</a><span class="dot">|</span>'
      % (D.PROFILE["email"], D.PROFILE["email"]))
    w('<span>&copy; <span id="y"></span> %s</span>' % D.PROFILE["name"])
    w('<span class="badge-note" data-en="%s" data-it="%s">%s</span>' % (
        a("%s — %s" % (lay["name"]["en"], lay["note"]["en"])),
        a("%s — %s" % (lay["name"]["it"], lay["note"]["it"])),
        "%s — %s" % (lay["name"]["en"], lay["note"]["en"])))
    w('</footer>\n</div>\n<script>\n')
    w(JS_UI); w(JS)
    w('</script>\n</body>\n</html>\n')
    return o.getvalue()


COUNTER_VARIANTS = [
    ("m-card", {"en": "1 | Cards", "it": "1 | Schede"},
     {"en": "boxed, one card per metric — closest to what you have now",
      "it": "riquadri, una scheda per metrica — il piu vicino a quello che hai ora"}),
    ("m-band", {"en": "2 | Band", "it": "2 | Fascia"},
     {"en": "a single continuous strip divided by hairlines — quieter, more compact",
      "it": "un'unica striscia continua divisa da filetti — piu sobrio e compatto"}),
    ("m-rule", {"en": "3 | Accent rule", "it": "3 | Filetto"},
     {"en": "no background at all, just a copper rule to the left of each figure",
      "it": "nessuno sfondo, solo un filetto rame a sinistra di ogni numero"}),
    ("m-hero3", {"en": "4 | Three large", "it": "4 | Tre grandi"},
     {"en": "three figures given real weight, the rest demoted to a single line",
      "it": "tre numeri con peso vero, il resto declassato a una riga"}),
    ("m-inline", {"en": "5 | Editorial ribbon", "it": "5 | Nastro editoriale"},
     {"en": "figures set inline in running text — the least 'dashboard' of the five",
      "it": "numeri nel flusso del testo — il meno 'cruscotto' dei cinque"}),
]


def render_counters():
    o = io.StringIO(); w = o.write
    w(head(" — contatori"))
    w("\n.vlabel{font-family:var(--fd);font-size:var(--fs-h3);font-weight:600;margin:0 0 3px}\n"
      ".vnote{font-size:var(--fs-sec);color:var(--muted);margin:0 0 16px;max-width:60ch}\n"
      "section.vsec{padding:clamp(26px,3.4vw,38px) 0}\n")
    w("\n</style>\n</head>\n<body>\n")
    topbar(w, [])
    w('<div class="wrap" id="top">\n<header class="hero"><div class="hero-txt">')
    w('<div class="eyebrow">Palette Rame</div>')
    w('<h1 style="font-size:clamp(26px,3.6vw,36px)" data-en="Counter band — five options" '
      'data-it="Fascia contatori — cinque varianti">Counter band — five options</h1>')
    w('<p class="tag-line" data-en="Same figures, five treatments. Try the theme and language toggles: '
      'the band behaves differently in dark mode." data-it="Stessi numeri, cinque trattamenti. '
      'Prova gli interruttori di tema e lingua: la fascia si comporta diversamente in scuro.">'
      'Same figures, five treatments. Try the theme and language toggles: the band behaves '
      'differently in dark mode.</p>')
    w('</div></header>\n')
    for style, label, note in COUNTER_VARIANTS:
        w('<section class="vsec">')
        w(bi("p", label, "vlabel"))
        w(bi("p", note, "vnote"))
        w('<div class="reveal">%s</div>' % metrics_html(style))
        w('</section>\n')
    w('<footer><span data-en="Comparison page — not the site" '
      'data-it="Pagina di confronto — non e il sito">Comparison page — not the site</span>'
      '<span>&copy; <span id="y"></span> %s</span></footer>\n' % D.PROFILE["name"])
    w('</div>\n<script>\n'); w(JS_UI); w(JS)
    w('</script>\n</body>\n</html>\n')
    return o.getvalue()


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for key, lay in LAYOUTS.items():
        p = os.path.join(OUT, "rame-%s.html" % key)
        open(p, "w", encoding="utf-8").write(render_layout(key, lay))
        print("scritto", os.path.basename(p))
    p = os.path.join(OUT, "contatori.html")
    open(p, "w", encoding="utf-8").write(render_counters())
    print("scritto", os.path.basename(p))
