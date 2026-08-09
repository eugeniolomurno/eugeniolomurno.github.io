# -*- coding: utf-8 -*-
"""Palette Rame + CSS + JS condivisi."""

RAME = {
    "gfont": "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700"
             "&family=Inter:wght@300..700&display=swap",
    "display": "'Fraunces', Georgia, serif",
    "body": "'Inter', system-ui, sans-serif",
    # taratura "avorio": fondo quasi bianco, riquadro nettamente tinto, secondari scuriti
    "light": {"bg": "#FFFDF8", "fg": "#17150F", "muted": "#4E463B", "card": "#F2EADC",
              "line": "#DCCFBB", "accent": "#98461F", "accent2": "#6F6044",
              "soft": "#F7E5D6", "chip": "#EEE4D4"},
    "dark": {"bg": "#17150F", "fg": "#EDE7DD", "muted": "#9C9285", "card": "#211E18",
             "line": "#302B23", "accent": "#DA8B58", "accent2": "#B9A583",
             "soft": "#33261D", "chip": "#262119"},
}


def vars_block(sel, p):
    return (sel + "{--bg:%(bg)s;--fg:%(fg)s;--muted:%(muted)s;--card:%(card)s;--line:%(line)s;"
            "--accent:%(accent)s;--accent2:%(accent2)s;--soft:%(soft)s;--chip:%(chip)s}" % p)


HEAD_SCRIPT = """(function(){var d=document.documentElement;d.classList.add('js');
try{var t=localStorage.getItem('el-theme');if(!t)t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';
d.setAttribute('data-theme',t);}catch(e){}
try{var l=localStorage.getItem('el-lang');if(l==='it'||l==='en')d.setAttribute('lang',l);}catch(e){}})();"""

CSS = """
/* ---------- scala tipografica: pochi gradini, fluidi dove serve ---------- */
:root{
  --fs-micro:12.5px;
  --fs-meta:13.5px;
  --fs-sec:14.5px;
  --fs-body:clamp(16px,.3vw + 15.1px,17px);
  --fs-lede:clamp(16.5px,.46vw + 15.1px,18.5px);
  --fs-role:clamp(18px,.75vw + 15.6px,21px);
  --fs-h1:clamp(29px,4.6vw + 8px,46px);
  --fs-h3:clamp(15.5px,.2vw + 15px,16.5px);
  --r-sm:5px;                 /* elementi bassi: tag, note */
  --gap-sec:clamp(44px,5.2vw,64px);   /* 64+64 = 128px fra sezioni, come misurato sul sito di Alberto */
  --pad-x:clamp(18px,4vw,26px);
}
*{box-sizing:border-box}
/* il fondo sta su html, non su body: cosi la grana puo stare dietro al contenuto
   ma davanti al fondo, con uno z-index negativo */
html{scroll-behavior:smooth;scroll-padding-top:72px;background:var(--bg);
     transition:background .25s}
/* 400, non 300: il peso sottile perde spessore apparente sui fondi chiari */
body{margin:0;background:transparent;color:var(--fg);font-family:var(--fb);font-weight:400;
     font-size:var(--fs-body);line-height:1.62;
     transition:color .25s}
/* grana di carta: solo in tema chiaro, fusa in soft-light per non spostare il colore del fondo.
   Fissa allo schermo: a questa frequenza non si distingue dallo scorrimento e non fa ridisegnare. */
html[data-theme="light"] body::before{content:"";position:fixed;inset:0;z-index:-1;
     pointer-events:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180' viewBox='0 0 180 180'%3E%3Cfilter id='n' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='180' height='180' filter='url(%23n)'/%3E%3C/svg%3E");background-size:180px 180px;
     opacity:.30;mix-blend-mode:soft-light}
@media(prefers-reduced-transparency:reduce){html[data-theme="light"] body::before{display:none}}
/* l'antialiasing assottiglia i glifi: utile solo dove il testo e chiaro su fondo scuro (macOS) */
html[data-theme="dark"] body{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
.wrap{max-width:900px;margin:0 auto;padding:0 var(--pad-x)}

/* ---------- topbar ---------- */
.topbar{position:sticky;top:0;z-index:40;background:color-mix(in srgb,var(--bg) 87%,transparent);
        backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.tb-in{max-width:900px;margin:0 auto;padding:0 var(--pad-x);height:56px;display:flex;align-items:center;gap:16px}
.brand{display:flex;align-items:center;color:var(--fg);font-family:var(--fd);
       font-weight:600;font-size:var(--fs-sec);white-space:nowrap;margin-left:-2px}
.brand:hover{text-decoration:none;color:var(--fg)}
.brand .in{color:var(--accent)}   /* iniziali in rame */
.nav{display:flex;gap:14px;margin-left:auto;overflow:visible}
.nav a{color:var(--muted);font-size:var(--fs-sec);font-weight:400;padding:3px 0;white-space:nowrap;
       border-bottom:1.5px solid transparent}
.nav a:hover,.nav a.on{color:var(--accent);border-bottom-color:var(--accent);text-decoration:none}
/* un solo margine automatico, sulla nav: nav e controlli restano un blocco unico a destra */
.ctrls{display:flex;gap:7px;flex:0 0 auto;margin-left:14px}
.tb-in.collapsed .ctrls{margin-left:auto}   /* nav nascosta: tocca ai controlli spingersi a destra */
.tbtn{display:grid;place-items:center;width:32px;height:32px;border-radius:var(--r);
      border:1px solid var(--line);background:var(--card);color:var(--fg);cursor:pointer;
      font-size:var(--fs-micro);font-weight:600;font-family:var(--fb);letter-spacing:.04em}
.tbtn:hover{border-color:var(--accent);color:var(--accent)}
/* rotazione al cambio lingua / tema, come sul sito attuale */
.spin{animation:spin .45s ease}
@keyframes spin{from{transform:rotate(0)}to{transform:rotate(360deg)}}
.ic-sun{display:none} html[data-theme="dark"] .ic-moon{display:none} html[data-theme="dark"] .ic-sun{display:block}

/* ---------- hero: niente wrap, la foto sparisce se non entra ---------- */
.hero{display:flex;gap:clamp(20px,3.5vw,36px);align-items:center;flex-wrap:nowrap;
      padding:clamp(34px,6vw,62px) 0 var(--gap-sec)}
.hero-txt{flex:1 1 auto;min-width:0}
.hero-img{flex:0 0 auto}
/* anello staccato: 3px di fondo, poi 2px di rame. Via box-shadow, non border,
   cosi l'orlatura non entra nel calcolo dell'ingombro */
.hero-img{padding:5px}
.hero-img img{width:clamp(132px,16.4vw,180px);height:clamp(132px,16.4vw,180px);
              border-radius:50%;object-fit:cover;display:block;border:none;
              box-shadow:0 0 0 3px var(--bg),0 0 0 5px var(--accent)}
@media(max-width:660px){.hero-img{display:none}}
.eyebrow{color:var(--accent);font-weight:600;font-size:var(--fs-micro);
         letter-spacing:.16em;text-transform:uppercase;margin-bottom:11px}
h1{font-family:var(--fd);font-size:var(--fs-h1);font-weight:700;margin:0 0 5px;
   letter-spacing:-.015em;line-height:1.04;overflow-wrap:break-word}
.role{margin:0 0 3px;font-size:var(--fs-role);font-weight:400}
.tag-line{margin:0 0 20px;font-size:var(--fs-sec);color:var(--muted)}
.cta{display:flex;gap:9px;flex-wrap:wrap;margin:20px 0 16px}
.btn{display:inline-flex;align-items:center;padding:9px 18px;border-radius:var(--r);
     background:var(--accent);color:#fff;font-size:var(--fs-sec);font-weight:500;border:1px solid var(--accent)}
.btn:hover{text-decoration:none;opacity:.9}
.btn.ghost{background:transparent;color:var(--accent)}
.btn.ghost:hover{background:var(--soft)}
/* collegamenti esterni: solo icone, nella barra in alto */
.social{display:flex;gap:2px;align-items:center;flex:0 0 auto;margin-right:8px;
        padding-right:9px;border-right:1px solid var(--line)}
.social a{display:grid;place-items:center;width:30px;height:30px;border-radius:var(--r);color:var(--muted)}
.social a svg{width:16px;height:16px}
.social a:hover{color:var(--accent);background:var(--soft);text-decoration:none}
.social-panel{display:flex;gap:2px;justify-content:space-between}
.social-panel a{display:grid;place-items:center;width:32px;height:32px;border-radius:var(--r);
                color:var(--muted);border:1px solid var(--line);flex:1 1 auto}
.social-panel a svg{width:16px;height:16px}
.social-panel a:hover{color:var(--accent);border-color:var(--accent);background:var(--soft);
                      text-decoration:none}

/* ---------- sezioni ---------- */
section{padding:var(--gap-sec) 0;border-top:1.5px solid var(--line)}
section.nb{border-top:none;padding-top:4px;padding-bottom:var(--gap-sec)}
h2{font-family:var(--fd);font-size:var(--fs-meta);font-weight:600;text-transform:uppercase;
   letter-spacing:.14em;color:var(--accent);margin:0 0 clamp(26px,3.3vw,41px)}
h3.sub{font-family:var(--fd);font-size:var(--fs-h3);font-weight:600;color:var(--fg);
       margin:clamp(22px,3vw,30px) 0 13px}
/* nessuna misura fissa: l'About segue gli stessi margini del resto della pagina */
/* stessa misura del resto del corpo: cambia solo l'interlinea, piu ampia per la prosa */
/* About e Contatti giustificati. La sillabazione automatica e necessaria, non un
   ornamento: senza, la giustificazione allarga gli spazi fra le parole e su una misura
   di 70 caratteri si aprono i buchi. Il browser sceglie il dizionario dall'attributo
   lang dell'html, che il selettore di lingua aggiorna a ogni cambio.
   Sotto i 640px si torna a bandiera: li la riga e troppo corta perche la
   giustificazione non si veda. */
.lede{margin:0 0 .85em;font-size:var(--fs-body);line-height:1.7;
      text-align:justify;text-justify:inter-word;
      -webkit-hyphens:auto;hyphens:auto}
@media(max-width:640px){.lede{text-align:left;hyphens:manual}}
.lede:last-child{margin-bottom:0}
.lede strong{font-weight:600} .lede em{font-style:italic}

/* ---------- schede aree di ricerca ---------- */
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,248px),1fr));gap:12px}
.icard{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:15px 16px}
.icard h3{font-family:var(--fd);font-size:var(--fs-h3);font-weight:600;margin:0 0 4px;color:var(--fg)}
.icard p{margin:0;font-size:var(--fs-sec);color:var(--muted);line-height:1.5}

/* ---------- righe ---------- */
.row{display:flex;gap:clamp(12px,2.4vw,22px);padding:13px 0;border-bottom:1px solid var(--line);
     align-items:baseline}
.row:last-of-type{border-bottom:none}
.row.compact{padding:10px 0}
.row-main{flex:1 1 auto;min-width:0}
.row-side{flex:0 0 auto;font-size:var(--fs-meta);color:var(--muted);text-align:right;
          white-space:nowrap;font-variant-numeric:tabular-nums}
/* "present": colore del testo pieno, peso normale */
.pres{color:var(--fg);font-weight:400}
/* riga del titolo: flex a baseline, cosi il pill non "galleggia" sopra il testo */
.titleline{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap}
.rt{font-family:var(--fd);font-weight:600;font-size:var(--fs-body);color:var(--fg);letter-spacing:-.01em}
a.rt:hover{color:var(--accent);text-decoration:none}
.star-ic{color:var(--accent)}   /* solo la stella prende l'accento, il titolo no */
.rm{font-size:var(--fs-sec);color:var(--muted);margin-top:3px}
.rm strong{color:var(--fg);font-weight:600}
.rx{font-size:var(--fs-meta);color:var(--muted);margin-top:3px;font-style:italic}
/* parole chiave della tesi: terza riga; solo l'etichetta prende il colore pieno */
.kw{font-size:var(--fs-micro);color:var(--muted);margin-top:4px;letter-spacing:.01em}
.kw-lab{color:var(--fg);font-weight:500}
.minilink{font-size:var(--fs-micro);white-space:nowrap}
.taglead{margin-bottom:6px}          /* il tipo di pubblicazione su una riga propria */
.tag{display:inline-block;flex:0 0 auto;font-size:10px;font-weight:600;letter-spacing:.09em;
     text-transform:uppercase;padding:3px 9px;border-radius:var(--r-sm);line-height:1.5}
.tag.j{background:var(--soft);color:var(--accent)}
.tag.c{background:var(--chip);color:var(--muted)}
/* --- progetti: acronimo, titolo esteso, info --- */
.proj-full{font-size:var(--fs-sec);color:var(--fg);margin-top:2px;font-weight:400}
.proj .rm{margin-top:3px}

/* --- trattamenti del ruolo (una sola variante attiva per pagina) --- */
.role-badge{flex:0 0 auto;font-size:10px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;
     padding:3px 9px;border-radius:var(--r);background:var(--accent);color:#fff;line-height:1.5}
.role-soft{flex:0 0 auto;font-size:10.5px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;
     padding:3px 9px;border-radius:var(--r-sm);background:var(--soft);color:var(--accent);line-height:1.5;
     border:1px solid color-mix(in srgb,var(--accent) 26%,transparent)}
.role-eyebrow{font-size:var(--fs-micro);font-weight:600;letter-spacing:.13em;text-transform:uppercase;
     color:var(--accent);margin-bottom:4px}
.role-line{margin-top:5px;font-size:var(--fs-meta);color:var(--muted)}
.role-key{font-weight:600;color:var(--fg)}
.role-key::after{content:" — "}
.role-line .role-val{color:var(--muted)}
.role-rule{margin-top:6px;padding-left:9px;border-left:2px solid var(--accent);
     font-size:var(--fs-meta);color:var(--fg);font-weight:500}
.role-side{margin-top:4px;font-size:var(--fs-micro);color:var(--accent);font-weight:500;
     white-space:normal;max-width:190px}
.more{margin:18px 0 0;font-size:var(--fs-sec)}

/* ---------- competizioni ---------- */
.comps{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,258px),1fr));gap:10px}
.comp{display:flex;gap:12px;align-items:center;background:var(--card);border:1px solid var(--line);
      border-radius:var(--r);padding:11px 13px}
.cm{flex:0 0 auto;font-family:var(--fd);font-weight:700;font-size:var(--fs-sec);padding:5px 9px;
    border-radius:var(--r);font-variant-numeric:tabular-nums}
.comp.gold .cm{background:#E8B923;color:#3A2E05}
.comp.bronze .cm{background:#C0885B;color:#33200E}
.cb{display:flex;flex-direction:column;min-width:0}
.cn{font-size:var(--fs-sec);font-weight:500;color:var(--fg)}
.co{font-size:var(--fs-micro);color:var(--muted)}

/* ---------- collassabili ---------- */
details.more-wrap summary{cursor:pointer;list-style:none;display:inline-flex;align-items:center;gap:7px;
  margin-top:13px;font-size:var(--fs-sec);font-weight:500;color:var(--accent);padding:6px 13px;
  border:1px solid var(--line);border-radius:var(--r);background:var(--card);user-select:none}
details.more-wrap summary::-webkit-details-marker{display:none}
details.more-wrap summary:hover{border-color:var(--accent);background:var(--soft)}
details[open].more-wrap summary{margin-bottom:12px}   /* aria fra il bottone e le voci che apre */
.chev{transition:transform .18s}
details[open].more-wrap summary .chev{transform:rotate(180deg)}
details.more-wrap summary .lbl-open{display:none}
details[open].more-wrap summary .lbl-shut{display:none}
details[open].more-wrap summary .lbl-open{display:inline}

/* ---------- filetto etichettato (separa dottorato e magistrali) ---------- */
/* Esperienza e formazione in due colonne, come sul CV. Il filetto verticale separa
   le due senza aggiungere un secondo titolo di sezione. */
.twocol{display:grid;grid-template-columns:1fr 1fr;gap:0 clamp(22px,3.2vw,38px)}
.twocol-c + .twocol-c{border-left:1.5px solid var(--line);padding-left:clamp(22px,3.2vw,38px)}
.twocol-c .row:last-of-type{border-bottom:none}
.colh{font-size:var(--fs-micro);font-weight:600;text-transform:uppercase;letter-spacing:.14em;
      color:var(--accent);margin:0 0 14px}
@media(max-width:860px){
  .twocol{grid-template-columns:1fr}
  .twocol-c + .twocol-c{border-left:none;padding-left:0;border-top:1.5px solid var(--line);
                        padding-top:20px;margin-top:6px}
}
.divlab{display:flex;align-items:center;gap:12px;margin:22px 0 6px;font-size:var(--fs-micro);
  font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
.divlab::after{content:"";flex:1 1 auto;height:1.5px;background:var(--line)}
.divlab:first-of-type{margin-top:0}

/* ---------- due colonne ---------- */
.twocol{display:grid;grid-template-columns:1fr 1fr;gap:0 28px}
.twocol .row{border-bottom:1px solid var(--line)}
@media(max-width:760px){.twocol{grid-template-columns:1fr}}

footer{padding:var(--gap-sec) 0 60px;border-top:1px solid var(--line);color:var(--muted);
       font-size:var(--fs-sec);display:flex;gap:9px;align-items:center;flex-wrap:wrap}
.dot{opacity:.5}
.badge-note{margin-left:auto;font-size:var(--fs-micro);padding:3px 10px;border-radius:var(--r-sm);
            background:var(--soft);color:var(--accent);font-weight:500}

/* ---------- menu a tendina (solo stretto) ---------- */
/* la tendina chiude la barra a destra, staccata da un filetto come le icone */
.navmenu{position:relative;display:none;flex:0 0 auto;
         margin-left:8px;padding-left:9px;border-left:1px solid var(--line)}
/* collassata: la barra non contiene tutte le voci, quindi passa alla tendina */
.tb-in.collapsed .nav{display:none}
.tb-in.collapsed .navmenu{display:block}
.navmenu > summary{list-style:none;display:grid;place-items:center;width:32px;height:32px;
  border-radius:var(--r);border:1px solid var(--line);background:var(--card);color:var(--fg);cursor:pointer}
.navmenu > summary::-webkit-details-marker{display:none}
.navmenu > summary:hover{border-color:var(--accent);color:var(--accent)}
.navmenu .panel{position:absolute;right:0;top:38px;min-width:190px;padding:6px;z-index:60;
  background:var(--card);border:1px solid var(--line);border-radius:var(--r);
  box-shadow:0 12px 34px rgba(0,0,0,.16);display:flex;flex-direction:column}
html[data-theme="dark"] .navmenu .panel{box-shadow:0 12px 34px rgba(0,0,0,.5)}
.navmenu .panel a{padding:9px 12px;font-size:var(--fs-sec);color:var(--fg);border-radius:6px}
.navmenu .panel a:hover{background:var(--soft);color:var(--accent);text-decoration:none}
/* duplicati utili solo quando la barra li nasconde */
.navmenu .tools{display:none;gap:6px;margin-top:6px;padding-top:8px;border-top:1px solid var(--line)}
.navmenu .tools .tbtn{flex:1 1 auto}

@media(max-width:720px){
  .nav{display:none}
  .navmenu{display:block}
  .ctrls > .tbtn,.ctrls > .social{display:none}   /* stretto: resta solo nome + tendina */
  /* sotto i 720px la nav e nascosta dal CSS, quindi fitNav non rileva debordamento:
     l'allineamento a destra deve venire dai controlli, non dalla classe collapsed */
  .ctrls{margin-left:auto}
  .navmenu{margin-left:0;padding-left:0;border-left:none}  /* niente filetto: non separa piu nulla */
  .navmenu .tools{display:flex}
  .row{flex-direction:column;gap:2px}
  .row-side{text-align:left}
}

/* ---------- apparizione ---------- */
/* i contatori partono nascosti SOLO se c'e JS, cosi senza JS restano i valori veri nell'HTML */
html.js [data-count]{opacity:0}
html.js [data-count].ready{opacity:1;transition:opacity .2s}
html.js .reveal{opacity:0;transform:translateY(16px)}
html.js .reveal.in{opacity:1;transform:none}
html.js .reveal{transition:opacity .62s cubic-bezier(.22,.61,.36,1),transform .62s cubic-bezier(.22,.61,.36,1);
                transition-delay:var(--d,0ms)}
@media(prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  html.js .reveal{opacity:1 !important;transform:none !important;transition:none !important}
  *{transition-duration:.01ms !important;animation-duration:.01ms !important}
}
"""

# ------------------------------------------------------------------ contatori
CSS_METRICS = """
/* nota accanto al numero: stessa resa del numero, ma esclusa dall'animazione */
.mv-note{white-space:nowrap}

/* griglia fissa: sempre 3 colonne x 2 righe, a ogni larghezza */
.m-card,.m-rule{display:grid;grid-template-columns:repeat(3,minmax(0,1fr))}
.m-band{display:grid;grid-template-columns:repeat(3,minmax(0,1fr))}

/* == 1. schede == */
.m-card{gap:clamp(7px,1.1vw,10px)}
.m-card .mi{background:var(--card);border:1px solid var(--line);border-radius:var(--r);
            padding:clamp(10px,1.6vw,15px) clamp(10px,1.6vw,15px) clamp(9px,1.4vw,13px);min-width:0}
.m-card .mv{display:block;font-family:var(--fd);font-size:clamp(19px,2.5vw,28px);font-weight:700;
            color:var(--accent);line-height:1.05;font-variant-numeric:tabular-nums}
/* color esplicito: senza, l'etichetta eredita il colore calcolato di body e non
   rilegge --fg quando le variabili vengono ridefinite piu in basso nell'albero */
.m-card .ml{display:block;font-size:var(--fs-sec);font-weight:500;margin-top:4px;color:var(--fg)}
.m-card .ms{display:block;font-size:var(--fs-meta);color:var(--muted);margin-top:2px;line-height:1.4}

/* == 2. fascia continua == */
.m-band{background:var(--card);border:1px solid var(--line);border-radius:var(--r);overflow:hidden}
.m-band .mi{padding:clamp(11px,1.7vw,16px) clamp(11px,1.8vw,18px);min-width:0;
            border-right:1px solid var(--line);border-bottom:1px solid var(--line)}
.m-band .mi:nth-child(3n){border-right:none}
.m-band .mi:nth-last-child(-n+3){border-bottom:none}
.m-band .mv{display:block;font-family:var(--fd);font-size:clamp(19px,2.3vw,26px);font-weight:700;
            color:var(--accent);line-height:1.05;font-variant-numeric:tabular-nums}
.m-band .ml{display:block;font-size:var(--fs-meta);font-weight:500;margin-top:3px;color:var(--fg)}
.m-band .ms{display:block;font-size:var(--fs-micro);color:var(--muted);line-height:1.35}

/* == 3. filetto d'accento == */
.m-rule{gap:clamp(12px,2.4vw,26px)}
.m-rule .mi{border-left:2px solid var(--accent);padding:2px 0 2px clamp(10px,1.5vw,14px);min-width:0}
.m-rule .mv{display:block;font-family:var(--fd);font-size:clamp(20px,2.7vw,30px);font-weight:700;
            line-height:1.02;font-variant-numeric:tabular-nums}
.m-rule .ml{display:block;font-size:var(--fs-meta);font-weight:500;margin-top:3px;color:var(--fg)}
.m-rule .ms{display:block;font-size:var(--fs-micro);color:var(--muted);line-height:1.35}

/* == 4. tre grandi + coda == */
.m-hero3 .top{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));
              gap:clamp(12px,3vw,34px);padding-bottom:18px;border-bottom:1px solid var(--line)}
.m-hero3 .top .mv{display:block;font-family:var(--fd);font-size:clamp(34px,5.2vw,52px);font-weight:700;
                  color:var(--accent);line-height:1;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.m-hero3 .top .ml{display:block;font-size:var(--fs-sec);font-weight:500;margin-top:5px}
.m-hero3 .top .ms{display:block;font-size:var(--fs-micro);color:var(--muted)}
.m-hero3 .rest{display:flex;flex-wrap:wrap;gap:8px 26px;padding-top:14px}
.m-hero3 .rest .mi{display:flex;align-items:baseline;gap:7px}
.m-hero3 .rest .mv{font-family:var(--fd);font-weight:700;font-size:var(--fs-lede);color:var(--accent);
                   font-variant-numeric:tabular-nums}
.m-hero3 .rest .ml{font-size:var(--fs-meta);color:var(--fg)}
.m-hero3 .rest .ms{font-size:var(--fs-micro);color:var(--muted)}

/* == 5. nastro editoriale == */
.m-inline{font-size:var(--fs-lede);line-height:2.05;max-width:66ch}
.m-inline .mi{display:inline;white-space:nowrap;margin-right:4px}
.m-inline .mv{font-family:var(--fd);font-weight:700;font-size:1.42em;color:var(--accent);
              font-variant-numeric:tabular-nums;vertical-align:-.04em}
.m-inline .ml{color:var(--fg)}
.m-inline .ms{display:none}
.m-inline .sep{color:var(--line);margin:0 9px}
"""

JS = """
(function(){
  var reduce=false;
  try{reduce=matchMedia('(prefers-reduced-motion: reduce)').matches}catch(e){}

  /* ---- apparizione delle sezioni ---- */
  var revs=[].slice.call(document.querySelectorAll('.reveal'));
  if(!('IntersectionObserver' in window)||reduce){
    revs.forEach(function(el){el.classList.add('in')});
  }else{
    var ro=new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(!e.isIntersecting)return;
        var el=e.target, sibs=[].slice.call(el.parentNode.children).filter(function(n){
          return n.classList&&n.classList.contains('reveal')});
        var i=sibs.indexOf(el);
        el.style.setProperty('--d',Math.min(i,6)*55+'ms');
        el.classList.add('in'); ro.unobserve(el);
      });
    },{rootMargin:'0px 0px -8% 0px',threshold:.06});
    revs.forEach(function(el){ro.observe(el)});
  }

  /* ---- contatori ---- */
  function ease(t){return 1-Math.pow(1-t,3)}
  function run(el){
    var raw=el.getAttribute('data-count')||'', suf=el.getAttribute('data-suffix')||'';
    var parts=raw.split('/').map(function(s){return parseFloat(s.trim())});
    if(parts.some(isNaN)){el.textContent=raw+suf;return}
    var t0=null, D=1100;
    function frame(ts){
      if(t0===null)t0=ts;
      var p=Math.min((ts-t0)/D,1), k=ease(p);
      el.textContent=parts.map(function(v){return Math.round(v*k)}).join(' / ')+(p===1?suf:'');
      if(p<1)requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }
  var counters=[].slice.call(document.querySelectorAll('[data-count]'));
  if(!('IntersectionObserver' in window)||reduce){
    counters.forEach(function(el){
      el.textContent=el.getAttribute('data-count')+(el.getAttribute('data-suffix')||'');
      el.classList.add('ready');
    });
  }else{
    var co=new IntersectionObserver(function(es){
      es.forEach(function(e){if(e.isIntersecting){run(e.target);co.unobserve(e.target)}});
    },{threshold:.5});
    counters.forEach(function(el){
      /* azzera prima di mostrare: evita il salto valore-reale -> 0 */
      var n=(el.getAttribute('data-count')||'').split('/').length;
      el.textContent=n>1?'0 / 0':'0';
      el.classList.add('ready');
      co.observe(el);
    });
  }

  /* ---- sezione attiva nella nav ---- */
  /* una voce di nav copre piu sezioni: costruisco la mappa sezione -> voce */
  var links={};
  [].forEach.call(document.querySelectorAll('.nav a'),function(a){
    var m=(a.getAttribute('data-sections')||a.getAttribute('href').slice(1)).split(' ');
    m.forEach(function(id){links[id]=a});
  });
  if('IntersectionObserver' in window){
    var no=new IntersectionObserver(function(es){
      es.forEach(function(e){
        var a=links[e.target.id]; if(!a||!e.isIntersecting)return;
        for(var k in links)links[k].classList.remove('on');
        a.classList.add('on');
      });
    },{rootMargin:'-58px 0px -70% 0px'});
    [].forEach.call(document.querySelectorAll('section[id]'),function(s){no.observe(s)});
  }
})();
"""

JS_UI = """
document.getElementById('y').textContent=new Date().getFullYear();
/* i controlli esistono due volte (barra + tendina): li piloto per classe, non per id */
function $$(s){return [].slice.call(document.querySelectorAll(s))}
/* la barra passa alla tendina appena una voce non ci sta piu: misurata, non a breakpoint fisso */
function fitNav(){
  var bar=document.querySelector('.tb-in'); if(!bar)return;
  bar.classList.remove('collapsed');
  if(bar.scrollWidth > bar.clientWidth + 1) bar.classList.add('collapsed');
}
fitNav();
addEventListener('resize', fitNav);
if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitNav);

/* menu a tendina: chiudi al click su una voce, fuori, o con Esc */
(function(){
  var m=document.getElementById('navMenu'); if(!m)return;
  m.addEventListener('click',function(e){if(e.target.tagName==='A')m.removeAttribute('open')});
  document.addEventListener('click',function(e){if(!m.contains(e.target))m.removeAttribute('open')});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')m.removeAttribute('open')});
})();
/* rotazione: togli la classe, forza un reflow, rimettila — cosi riparte a ogni click */
function spin(el){
  try{if(matchMedia('(prefers-reduced-motion: reduce)').matches)return}catch(e){}
  el.classList.remove('spin'); void el.offsetWidth; el.classList.add('spin');
}
$$('.tbtn').forEach(function(b){
  b.addEventListener('animationend',function(){b.classList.remove('spin')});
});
$$('.js-theme').forEach(function(b){b.addEventListener('click',function(){
  var c=document.documentElement.getAttribute('data-theme')==='dark'?'light':'dark';
  document.documentElement.setAttribute('data-theme',c);
  try{localStorage.setItem('el-theme',c)}catch(e){}
  spin(b);
})});
(function(){
  var btns=$$('.js-lang'); if(!btns.length)return;
  function cur(){return document.documentElement.getAttribute('lang')==='it'?'it':'en'}
  function apply(l){
    document.documentElement.setAttribute('lang',l);
    $$('[data-en]').forEach(function(el){
      var v=el.getAttribute('data-'+l); if(v!==null)el.innerHTML=v;
    });
    $$('[data-en-attr]').forEach(function(el){
      var spec=el.getAttribute('data-'+l+'-attr'); if(!spec)return;
      var i=spec.indexOf(':'); el.setAttribute(spec.slice(0,i),spec.slice(i+1));
    });
    btns.forEach(function(b){b.textContent=(l==='en'?'IT':'EN')});
    if(typeof fitNav==='function')fitNav();
    try{localStorage.setItem('el-lang',l)}catch(e){}
  }
  btns.forEach(function(b){b.addEventListener('click',function(){
    apply(cur()==='en'?'it':'en'); spin(b);
  })});
  apply(cur());
})();
"""
