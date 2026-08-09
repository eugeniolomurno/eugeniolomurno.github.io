# -*- coding: utf-8 -*-
"""Sorgente unica bilingue. I dati neutri (nomi, titoli, date, DOI) non si traducono;
le etichette derivano da vocabolari per lingua, cosi una voce nuova non richiede due scritture."""

LANGS = ("en", "it")

# ---------------------------------------------------------------- vocabolari
VOC = {
    # tipo di corso
    "bsc":       {"en": "BSc Course",      "it": "Corso triennale"},
    "msc":       {"en": "MSc Course",      "it": "Corso magistrale"},
    "phd":       {"en": "PhD Course",      "it": "Corso di dottorato"},
    "techcamp":  {"en": "Summer School",   "it": "Summer School"},
    "corporate": {"en": "Corporate Course", "it": "Corso aziendale"},
    # ruolo didattico
    "ta":        {"en": "Teaching Assistant", "it": "Assistente alla didattica"},
    "teacher":   {"en": "Teacher",            "it": "Docente"},
    # varie
    "editions":  {"en": "Editions",   "it": "edizioni"},
    "edition":   {"en": "Edition",    "it": "edizione"},
    "with":      {"en": "with",       "it": "con"},
    "hours":     {"en": "h",          "it": "h"},
}

UI = {
    # la nav raggruppa le sezioni in cinque macro-aree
    "nav_about":       {"en": "About",        "it": "Chi sono"},
    "nav_research":    {"en": "Research",     "it": "Ricerca"},
    "nav_publications": {"en": "Publications", "it": "Pubblicazioni"},
    "nav_projects":    {"en": "Projects",     "it": "Progetti"},
    "nav_teaching":    {"en": "Teaching",   "it": "Didattica"},
    "nav_supervision": {"en": "Supervisions", "it": "Supervisioni"},
    "nav_awards":      {"en": "Awards",       "it": "Riconoscimenti"},
    "nav_education":   {"en": "Experience",   "it": "Esperienza"},

    "t_about":       {"en": "About",                    "it": "Chi sono"},
    "t_research":    {"en": "Research Interests",       "it": "Aree di ricerca"},
    "t_publications": {"en": "Selected Publications",   "it": "Pubblicazioni selezionate"},
    "t_projects":    {"en": "Research Projects",        "it": "Progetti di ricerca"},
    "t_teaching":    {"en": "Teaching Activities",      "it": "Attività didattica"},
    "t_supervision": {"en": "Supervisions",             "it": "Supervisioni"},
    "t_awards":      {"en": "Awards and Achievements",  "it": "Riconoscimenti e risultati"},
    "t_education":   {"en": "Education and Experience", "it": "Formazione ed esperienza"},
    "t_contact":     {"en": "Contact",                  "it": "Contatti"},
    # intestazioni delle due colonne di Esperienza e formazione
    "col_education":  {"en": "Education",  "it": "Formazione"},
    "col_experience": {"en": "Experience", "it": "Esperienza"},

    "contact_p":  {"en": "If these topics resonate with you &mdash; for a discussion or a collaboration, in academia as well as in the entrepreneurial world &mdash; I&rsquo;d be glad to hear from you.",
                   "it": "Se questi temi ti interessano &mdash; per un confronto o una collaborazione, nel mondo della ricerca cos&igrave; come in quello imprenditoriale &mdash; sar&ograve; lieto di sentirti."},
    "email_btn":  {"en": "\u2709 Email me",          "it": "\u2709 Scrivimi"},
    "cv_btn":     {"en": "Download CV",          "it": "Scarica il CV"},
    "contact_btn": {"en": "Get in touch",        "it": "Scrivimi"},
    "tag_j":      {"en": "Journal",              "it": "Rivista"},
    "tag_c":      {"en": "Conference",           "it": "Conferenza"},
    "all_pubs":   {"en": "Full list on Google Scholar",
                   "it": "Elenco completo su Google Scholar"},
    "full_cv":    {"en": "Download the full CV (PDF)",
                   "it": "Scarica il CV completo (PDF)"},
    "competitions": {"en": "Competitions",       "it": "Competizioni"},
    "thesis_link": {"en": "thesis",              "it": "tesi"},
    "keywords":   {"en": "Keywords",            "it": "Parole chiave"},
    "thesis_lab": {"en": "Thesis",              "it": "Tesi"},
    "show_all_courses": {"en": "Show all %d courses", "it": "Mostra tutti i %d corsi"},
    "show_all_theses":  {"en": "Show all %d MSc theses",
                         "it": "Mostra tutte le %d tesi magistrali"},
    "div_phd":    {"en": "PhD &mdash; Co-Advisor",  "it": "Dottorato &mdash; Co-tutore"},
    "div_msc":    {"en": "MSc &mdash; Co-Advisor",  "it": "Magistrali &mdash; Co-relatore"},
    "tag_phd":    {"en": "PhD",                  "it": "Dottorato"},
    "tag_msc":    {"en": "MSc",                  "it": "Magistrale"},
    "coadvisor":  {"en": "Co-Advisor",           "it": "Co-tutore"},
    "advisor":    {"en": "Co-Supervisor",        "it": "Co-relatore"},
    "show_fewer": {"en": "Show fewer",           "it": "Mostra meno"},
    "loc":        {"en": "Milano, Italy",        "it": "Milano, Italia"},
    # in grassetto ovunque compaia: e l'unica informazione temporale che cambia da sola
    "present":    {"en": "<span class='pres'>present</span>", "it": "<span class='pres'>in corso</span>"},
    "lang_switch": {"en": "IT",                  "it": "EN"},
}

# ---------------------------------------------------------------- profilo
PROFILE = {
    "name": "Eugenio Lomurno",
    "email": "eugenio.lomurno@polimi.it",
    "site": "eugeniolomurno.github.io",
    "photo": "photo.jpg",
    "affiliation": {"en": "AIRLab | DEIB | Politecnico di Milano",
                    "it": "AIRLab | DEIB | Politecnico di Milano"},
    "role": {"en": "Postdoctoral Fellow", "it": "Assegnista di ricerca"},
    "tagline": None,   # ridondante rispetto alle aree di ricerca
    "bio": {
        "en": [
            "I am a postdoctoral fellow in the AIRLab group at the Department of Electronics, "
            "Information and Bioengineering (DEIB), Politecnico di Milano, where I completed my "
            "PhD in Information Technology <em>cum laude</em> in 2025.",
            "My research has grown within the H2020 <a href='https://doi.org/10.3030/101016112' "
            "target='_blank' rel='noopener'>ESSENCE</a> and <a href='https://cordis.europa.eu/project/id/101016577' "
            "target='_blank' rel='noopener'>AI-SPRINT</a> projects and the PNRR <a href='https://fondazione-fair.it/' "
            "target='_blank' rel='noopener'>FAIR</a> project, and continues today &mdash; in the "
            "Lombardy-funded <em>PREDICT</em> project &mdash; with cutting-edge generative techniques for "
            "synthesising and privately sharing medical images and data. I am also part of the "
            "<a href='https://www.essilorluxottica.com/it/careers/smart-eyewear-lab/' target='_blank' "
            "rel='noopener'>SEL</a> (Smart Eyewear Lab), a joint research platform of EssilorLuxottica "
            "and Politecnico di Milano, where I work on quantised neural architecture "
            "search for edge devices.",
            # Terzo paragrafo, dal CV. Portato alla prima persona come i due precedenti:
            # nel CV era in terza, e alternare le due voci nello stesso testo stona.
            "Within the scientific debate, I share the concerns of that part of the scientific "
            "community which questions the scenarios of artificial intelligence, "
            "advocating the necessity to develop strategies to address critical phenomena such as "
            "goal misalignment, self-replication, and uncontrolled self-improvement in advanced AI "
            "systems. I believe the purpose of artificial intelligence must be the prosperity and "
            "wellbeing of humanity, and that among its most urgent tasks is confronting the "
            "climate crisis.",
        ],
        "it": [
            "Sono un assegnista di ricerca nel gruppo AIRLab del Dipartimento di Elettronica, "
            "Informazione e Bioingegneria (DEIB) del Politecnico di Milano, dove nel 2025 ho "
            "conseguito il dottorato in Information Technology <em>con lode</em>.",
            "La mia ricerca &egrave; cresciuta all'interno dei progetti H2020 "
            "<a href='https://doi.org/10.3030/101016112' target='_blank' rel='noopener'>ESSENCE</a> e "
            "<a href='https://cordis.europa.eu/project/id/101016577' target='_blank' rel='noopener'>AI-SPRINT</a> "
            "e nel progetto PNRR <a href='https://fondazione-fair.it/' target='_blank' rel='noopener'>FAIR</a>, "
            "e prosegue oggi &mdash; nel progetto <em>PREDICT</em> finanziato da Regione Lombardia &mdash; "
            "con tecniche generative all'avanguardia per sintetizzare e condividere in maniera privata immagini e dati medici. "
            "Faccio inoltre parte dello <a href='https://www.essilorluxottica.com/it/careers/smart-eyewear-lab/' "
            "target='_blank' rel='noopener'>SEL</a> (Smart Eyewear Lab), piattaforma di ricerca congiunta di "
            "EssilorLuxottica e Politecnico di Milano, dove mi occupo di neural "
            "architecture search quantizzato per dispositivi edge.",
            "Nel dibattito scientifico condivido le preoccupazioni di quella parte della comunit&agrave; "
            "che si interroga sugli scenari dell'intelligenza artificiale, e sostengo la "
            "necessit&agrave; di sviluppare strategie per affrontare fenomeni critici come il "
            "disallineamento degli obiettivi, l'autoreplicazione e l'automiglioramento incontrollato "
            "nei sistemi avanzati. Ritengo che il fine dell'intelligenza artificiale debba essere la "
            "prosperit&agrave; e il benessere dell'umanit&agrave;, e che fra i suoi compiti pi&ugrave; "
            "urgenti ci sia affrontare la crisi climatica.",
        ],
    },
    # (etichetta, url, chiave icona)
    "links": [
        ("Google Scholar", "https://scholar.google.com/citations?user=7VpjbGoAAAAJ&hl=it", "scholar"),
        ("Scopus", "https://www.scopus.com/authid/detail.uri?authorId=57226274677", "scopus"),
        ("GitHub", "https://github.com/eugeniolomurno", "github"),
        ("LinkedIn", "https://www.linkedin.com/in/eugenio-lomurno-a28b12162/", "linkedin"),
        ("Instagram", "https://www.instagram.com/tacchinoleso/", "instagram"),
    ],
}

INTERESTS = [
    {"t": {"en": "Generative Deep Learning", "it": "Generative Deep Learning"},
     "d": {"en": "Diffusion, adversarial and variational models for the latent creation of new knowledge.",
           "it": "Modelli di diffusione, avversariali e variazionali per la creazione latente di nuova conoscenza."}},
    {"t": {"en": "Synthetic Dataset Generation", "it": "Synthetic Dataset Generation"},
     "d": {"en": "High-utility synthetic datasets, to train downstream machine learning models on synthetic data and test them on real data.",
           "it": "Realizzazione di dataset sintetici ad alta utilità, per addestrare sui sintetici e testare su reali i modelli di machine learning a valle."}},
    {"t": {"en": "Privacy-Preserving Deep Learning", "it": "Privacy-Preserving Deep Learning"},
     "d": {"en": "Synthetic-data techniques for building private models and exchanging knowledge across institutions.",
           "it": "Sviluppo di tecniche basate su dati sintetici per la realizzazione di modelli privati e lo scambio di conoscenza tra istituzioni."}},
    {"t": {"en": "Multimodal Deep Learning", "it": "Multimodal Deep Learning"},
     "d": {"en": "Techniques to build latent knowledge from heterogeneous sources and fuse it to optimise downstream tasks.",
           "it": "Tecniche per creare conoscenza latente da fonti eterogenee e fonderla per ottimizzare i task a valle."}},
    {"t": {"en": "Edge-Oriented Neural Architecture Search", "it": "Edge-Oriented Neural Architecture Search"},
     "d": {"en": "NAS techniques for architectures that are Pareto-optimal between accuracy and performance on edge devices.",
           "it": "Tecniche di NAS per lo sviluppo di architetture con ottimalità di Pareto tra accuratezza e performance per dispositivi edge."}},
    {"t": {"en": "Healthcare and Climate Applications", "it": "Healthcare and Climate Applications"},
     "d": {"en": "Applications serving human health and the safeguarding of the climate.",
           "it": "Applicazioni a beneficio della salute dell'essere umano e della salvaguardia del clima."}},
]

METRICS = [
    {"v": "12 / 9", "l": {"en": "h-index", "it": "h-index"},
     "s": {"en": "Google Scholar / Scopus", "it": "Google Scholar / Scopus"}},
    {"v": "340", "suf": "+", "l": {"en": "Citations", "it": "Citazioni"},
     "s": {"en": "Google Scholar", "it": "Google Scholar"}},
    {"v": "30 / 16", "l": {"en": "Publications", "it": "Pubblicazioni"},
     "s": {"en": "Overall / A+ Conferences or Q1 Journals",
           "it": "Totali / Conferenze A+ o riviste Q1"}},
    {"v": "5", "l": {"en": "Research Projects", "it": "Progetti di ricerca"},
     "s": {"en": "European, Regional, JRP", "it": "Europei, Regionali, JRP"}},
    {"v": "COURSES / HOURS", "suf": "+",
     "l": {"en": "Teaching Activities", "it": "Attività didattica"},
     "s": {"en": "University or Corporate Courses / Teaching Hours",
           "it": "Corsi universitari o aziendali / Ore di didattica"}},
    {"v": "THESES / PHD", "l": {"en": "Supervisions", "it": "Supervisioni"},
     "s": {"en": "MSc / PhD", "it": "Magistrali / Dottorato"}},
]

# acronimo -> titolo esteso -> riga di informazioni
PROJECTS = [
    {"acro": "SEL", "full": "Smart Eyewear Lab",
     "role": {"en": "Research Track Lead — Neural Architecture Search &times; Edge Devices",
              "it": "Responsabile di linea — Neural Architecture Search &times; dispositivi edge"},
     "info": {"en": "Joint Research Platform, Politecnico di Milano and EssilorLuxottica",
              "it": "Joint Research Platform, Politecnico di Milano ed EssilorLuxottica"},
     "period": {"en": "2026 — <span class='pres'>present</span>", "it": "2026 — <span class='pres'>in corso</span>"},
     "url": "https://www.essilorluxottica.com/it/careers/smart-eyewear-lab/"},
    {"acro": "PREDICT",
     "full": "Predictive Response and Disease Evaluation in Ovarian Cancer with Generative AI",
     "role": {"en": "AI Scientific Lead", "it": "Responsabile scientifico IA"},
     "info": {"en": "Fondazione Regionale per la Ricerca Biomedica, Regione Lombardia, ID 012024R0055",
              "it": "Fondazione Regionale per la Ricerca Biomedica, Regione Lombardia, ID 012024R0055"},
     "period": {"en": "2026 — <span class='pres'>present</span>", "it": "2026 — <span class='pres'>in corso</span>"},
     "url": "https://nearlab.polimi.it/neuroengineering-and-medical-robotics/medical/predict/"},
    {"acro": "FAIR", "full": "Future Artificial Intelligence Research",
     "role": {"en": "Research Track Lead — Generative AI", "it": "Responsabile di linea — IA generativa"},
     "info": {"en": "PNRR, MUR announcement no. 341, ID PE00000013",
              "it": "PNRR, Avviso MUR n. 341, ID PE00000013"},
     "period": {"en": "2024 — 2026", "it": "2024 — 2026"},
     "url": "https://fondazione-fair.it/"},
    {"acro": "AI-SPRINT",
     "full": "Artificial Intelligence in Secure Privacy-preserving Computing Continuum",
     "role": {"en": "AI Scientific Lead", "it": "Responsabile scientifico IA"},
     "info": {"en": "Horizon 2020, Grant Agreement 101016577",
              "it": "Horizon 2020, Grant Agreement 101016577"},
     "period": {"en": "2021 — 2023", "it": "2021 — 2023"},
     "url": "https://doi.org/10.3030/101016577"},
    {"acro": "ESSENCE",
     "full": "Empathic Platform to Monitor, Stimulate, Enrich and Assist Elders and Children",
     "role": {"en": "AI Scientific Lead", "it": "Responsabile scientifico IA"},
     "info": {"en": "Horizon 2020, Grant Agreement 101016112",
              "it": "Horizon 2020, Grant Agreement 101016112"},
     "period": {"en": "2020 — 2023", "it": "2020 — 2023"},
     "url": "https://doi.org/10.3030/101016112"},
]

# elenco e formato ripresi dal sito attuale: autori e sede su una riga sola
PUBLICATIONS = [
    ("j", "Your Image Generator Is Your New Private Dataset",
     "N. Resmini, <strong>E. Lomurno</strong>, C. Sbrolli, M. Matteucci | Image and Vision Computing, 2025",
     "https://doi.org/10.1016/j.imavis.2025.105727"),
    ("j", "Federated Knowledge Recycling: Privacy-Preserving Synthetic Data Sharing",
     "<strong>E. Lomurno</strong>, M. Matteucci | Pattern Recognition Letters, 2025",
     "https://doi.org/10.1016/j.patrec.2025.02.030"),
    ("j", "Synthetic Image Learning: Preserving Performance and Preventing Membership Inference Attacks",
     "<strong>E. Lomurno</strong>, M. Matteucci | Pattern Recognition Letters, 2025",
     "https://doi.org/10.1016/j.patrec.2025.02.003"),
    ("c", "Bridging the Gap: Enhancing the Utility of Synthetic Data via Post-Processing Techniques",
     "A. Lampis, <strong>E. Lomurno</strong>, M. Matteucci | BMVC, 2023",
     "https://papers.bmvc2023.org/0715.pdf"),
    ("j", "POPNASv3: A Pareto-Optimal Neural Architecture Search Solution for Image and Time Series Classification",
     "A. Falanti, <strong>E. Lomurno</strong>, D. Ardagna, M. Matteucci | Applied Soft Computing, 2023",
     "https://doi.org/10.1016/j.asoc.2023.110555"),
]

# hours = totale sul corso (somma delle edizioni). None = da confermare.
TEACHING = [
    {"course": "Intelligenza Artificiale", "kind": "bsc", "org": "Politecnico di Milano",
     "role": "ta", "editions": 1, "prof": "A. Bonarini", "from": "2026", "ongoing": True, "hours": 6},
    {"course": "Advanced Deep Learning", "kind": "msc", "org": "Politecnico di Milano",
     "role": "ta", "editions": 1, "prof": "M. Matteucci", "from": "2026", "ongoing": True, "hours": 10},
    {"course": "Artificial Neural Networks and Deep Learning", "kind": "msc",
     "org": "Politecnico di Milano", "role": "ta", "editions": 5,
     "prof": "M. Matteucci, G. Boracchi", "from": "2021", "ongoing": True, "hours": 107},
    {"course": "AI Bootcamp \u2014 TechCamp", "kind": "techcamp", "org": "Politecnico di Milano",
     "role": "ta", "editions": 3, "prof": "M. Matteucci", "from": "2024", "ongoing": True, "hours": 45},
    {"course": "Artificial Intelligence", "kind": "corporate", "org": "Guber Banca S.p.A.",
     "role": "teacher", "editions": 2, "prof": "", "from": "2025", "to": "2026", "hours": 80},
    {"course": "AI Product Management Bootcamp", "kind": "corporate", "org": "CEFRIEL",
     "role": "ta", "editions": 1, "prof": "", "from": "2025", "to": "2025", "hours": 6},
    {"course": "Generative AI: Methods and Practice", "kind": "corporate",
     "org": "MADE | M.I.A. Lombardia EDIH", "role": "teacher", "editions": 1,
     "prof": "", "from": "2025", "to": "2025", "hours": 4},
    {"course": "Computer Vision and Image Processing", "kind": "msc", "org": "Università Bocconi",
     "role": "ta", "editions": 2, "prof": "G. Boracchi", "from": "2024", "to": "2025", "hours": 52},
    {"course": "Deep Learning for Computer Vision", "kind": "msc", "org": "Università Bocconi",
     "role": "ta", "editions": 2, "prof": "G. Boracchi", "from": "2023", "to": "2024", "hours": 50},
    {"course": "Deep Learning", "kind": "corporate", "org": "CEFRIEL | Master in Data Science &amp; AI",
     "role": "teacher", "editions": 1, "prof": "", "from": "2023", "to": "2023", "hours": 24},
    {"course": "Advanced Topics in Deep Learning: The Rise of Transformers", "kind": "phd",
     "org": "Politecnico di Milano", "role": "ta", "editions": 1, "prof": "M. Matteucci",
     "from": "2023", "to": "2023", "hours": 12},
    {"course": "Generative Adversarial Networks", "kind": "corporate",
     "org": "CEFRIEL | NOKIA Master AI&amp;ML", "role": "teacher", "editions": 1, "prof": "",
     "from": "2022", "to": "2022", "hours": 16},
    {"course": "Deep Learning and Neural Networks", "kind": "corporate",
     "org": "CEFRIEL | SIAE Master AI&amp;ML", "role": "ta", "editions": 1, "prof": "M. Matteucci",
     "from": "2022", "to": "2022", "hours": 12},
    {"course": "Advanced Deep Learning Models and Methods", "kind": "phd",
     "org": "Politecnico di Milano", "role": "ta", "editions": 1, "prof": "M. Matteucci",
     "from": "2022", "to": "2022", "hours": 2},
]

TEACHING_HOURS = sum(t["hours"] for t in TEACHING if t["hours"])
TEACHING_HOURS_FLOOR = (TEACHING_HOURS // 10) * 10          # arrotondato per difetto
TEACHING_HOURS_PENDING = [t["course"] for t in TEACHING if not t["hours"]]

def _end(t):
    return 9999 if t.get("ongoing") else int(t.get("to", t["from"]))


# decrescente per data di fine, poi per data di inizio; gli ongoing restano in testa
TEACHING.sort(key=lambda t: (-_end(t), -int(t["from"])))

_ONGOING_26 = {"en": "2026 — <span class='pres'>present</span>", "it": "2026 — <span class='pres'>in corso</span>"}
_ONGOING_25 = {"en": "2025 — <span class='pres'>present</span>", "it": "2025 — <span class='pres'>in corso</span>"}

# (studente, titolo, periodo, url) — periodo: stringa neutra oppure dict bilingue
PHD_SUPERVISION = [
    ("Advanced Generative Deep Learning for Healthcare", "Francesca Pia Panaccione", _ONGOING_25, "",
     "Generative Deep Learning | Medical Imaging | Healthcare AI"),
    ("Advanced Generative Deep Learning for Synthetic Data Utility Enrichment", "Leonardo Brusini",
     _ONGOING_26, "", "Generative Deep Learning | Synthetic Data | Data Utility"),
]

# keyword: da POLITesi dove pubblicate, altrimenti dedotte dal titolo
SUPERVISION = [
    ("What Shapes a Synthetic CT? On Multimodal 3D CT Generation and Conditioning", "Silvia Mombelli",
     _ONGOING_26, "", "Medical Imaging | 3D CT Generation | Multimodal Conditioning"),
    ("Who&rsquo;s in the Noise? Counterfactual vs Predictive Approaches to Longitudinal CT Synthesis",
     "Jie Chen", _ONGOING_26, "",
     "Counterfactual Generation | Longitudinal Imaging | CT Synthesis"),
    ("Compressing Without Compromising? On Knowledge Distillation for Quantization-Aware Training",
     "Giacomo Bossi", _ONGOING_26, "",
     "Knowledge Distillation | Quantisation-Aware Training | Model Compression"),
    ("Less is More? On Network Pruning and Low-Rank Approximation for Edge AI", "Andrea Sanvito",
     _ONGOING_26, "", "Network Pruning | Low-Rank Approximation | Edge AI"),
    ("&ldquo;P. Sherman, 42 Wallaby Way, Sydney&rdquo;: Investigating When LLMs Forget What They "
     "Were Talking About", "Fabiola Ribolsi", _ONGOING_26, "",
     "Large Language Models | Long-Context Memory | Context Degradation"),
    ("A Multimodal Benchmark for Text-Guided Anomaly Detection", "Teodora Jovanovi\u0107", "2025 \u2014 2026",
     "https://www.politesi.polimi.it/handle/10589/252794",
     "Anomaly Detection | Vision-Language Models | Industrial Inspection"),
    ("TARDIS: Tabular Distillation and Inference-time Sampling framework",
     "Filippo Balzarini &amp; Francesco Benelle", "2025 \u2014 2026", "",
     "Tabular Data | Knowledge Distillation | Inference-Time Sampling"),
    ("CONVERSE: Discovering Patient Groups in Survival Data via Deep Latent Clustering", "Pinar Erbil",
     "2025 \u2014 2026", "", "Survival Analysis | Deep Latent Clustering | Patient Stratification"),
    ("Generating ovarian cancer CT volumes via multimodal conditioning", "Carlotta Pecchiari",
     "2024 \u2014 2026", "",
     "Medical Imaging | 3D Generation | Multimodal Conditioning"),
    ("Enhancing Contrastive Learning with Synthetic Data from Text-to-Image Models", "Leonardo Brusini",
     "2024 \u2014 2025", "https://www.politesi.polimi.it/handle/10589/246635",
     "Contrastive Learning | Synthetic Data | Text-to-Image Models"),
    ("A Generative Pipeline for High-Quality Synthetic Survival Datasets", "Niccol\u00f2 Maria Rizzi",
     "2024 \u2014 2025", "https://www.politesi.polimi.it/handle/10589/235504",
     "Synthetic Datasets | Survival Analysis | Generative Deep Learning"),
    ("Neuro-Symbolic Conditioning for Synthetic Dataset Generation via GANs and Stable Diffusion",
     "Giacomo Savazzi", "2024 \u2014 2025", "https://www.politesi.polimi.it/handle/10589/234573",
     "Neuro-Symbolic Models | Scene Graph Generation | Latent Diffusion"),
    ("Text-Conditioned Knowledge Recycling: A Synthetic Dataset Generation Pipeline",
     "Nicol\u00f2 Francesco Resmini", "2024 \u2014 2025",
     "https://www.politesi.polimi.it/handle/10589/234657",
     "Text-Conditioned Diffusion | Knowledge Distillation | Membership Inference"),
    ("POMONAG: Pareto Optimal Many-Objective Neural Architecture Generator",
     "Samuele Mariani &amp; Matteo Monti", "2023 \u2014 2024",
     "https://www.politesi.polimi.it/handle/10589/218505",
     "Neural Architecture Search | Pareto Optimality | Diffusion Models"),
    ("Stable Diffusion Adaptation for Generation and Total Replacement of Real Data", "Matteo D&rsquo;Oria",
     "2023 \u2014 2024", "https://www.politesi.polimi.it/handle/10589/218608",
     "Stable Diffusion | Dataset Synthesis | Classification Accuracy Score"),
    ("A Journey to Improve Neural Architecture Search: Neural Architecture Transfer and Once-For-All",
     "Simone Sarti", "2022 \u2014 2023", "https://www.politesi.polimi.it/handle/10589/203273",
     "Neural Architecture Transfer | Once-For-All | Image Classification"),
    ("Adversarial Privacy: Balancing Accuracy and Security in Deep Neural Networks", "Francesca Ausonio",
     "2022 \u2014 2023", "https://www.politesi.polimi.it/handle/10589/208948",
     "Differential Privacy | Regularisation | Membership Inference"),
    ("Bridging the Gap: Improving Classification Accuracy through Post-Processing Techniques",
     "Andrea Lampis", "2022 \u2014 2023", "https://www.politesi.polimi.it/handle/10589/209359",
     "Generative Models | Classification Accuracy Score | Synthetic Images"),
    ("Longitudinal Monitoring of Graphical Abilities, Towards the Early Diagnosis of Dysgraphia",
     "Madhurii Gatto &amp; Matteo Bollettino", "2021 \u2014 2022",
     "https://www.politesi.polimi.it/handle/10589/197825",
     "Dysgraphia | Longitudinal Monitoring | Time-Series Embeddings"),
    ("On Dysgraphia Diagnosis Support via the Automation of the BVSCO Test Scoring &mdash; KTH",
     "Riccardo Sommaruga", "2021 \u2014 2022",
     "https://www.diva-portal.org/smash/get/diva2:1711449/FULLTEXT01.pdf",
     "Dysgraphia Screening | Handwriting Analysis | Automated Scoring"),
    ("Machine Learning-Based Analysis of Spontaneous Speech to Monitor Cognitive Decline",
     "Chiara Giangregorio", "2021 \u2014 2022", "https://www.politesi.polimi.it/handle/10589/189053",
     "Acoustic Features | Cognitive Decline | Speech Analysis"),
    ("Deep Neural Networks for Time Series Forecasting Beyond Transformers", "Riccardo Ughi",
     "2021 \u2014 2022", "https://www.politesi.polimi.it/handle/10589/197272",
     "Time-Series Forecasting | Transformers | Deep Learning"),
    ("Unsupervised Activities and Age Monitoring via Smart Ink Pen", "Maria Paola D&rsquo;Ercole",
     "2021 \u2014 2022", "https://www.politesi.polimi.it/handle/10589/186950",
     "Handwriting Analysis | Ageing | Smart Ink Pen"),
    ("POPNASv2: Efficient Neural Architecture Search Through Time-Accuracy Optimization",
     "Andrea Falanti", "2021 \u2014 2022", "https://www.politesi.polimi.it/handle/10589/186258",
     "Neural Architecture Search | Pareto Optimality | Image Classification"),
    ("On the Resilience and Protection of Regularization Techniques in Differential Privacy",
     "Marco Giammarresi", "2021 \u2014 2022", "https://www.politesi.polimi.it/handle/10589/187045",
     "Differential Privacy | Regularisation | Privacy Attacks"),
]

COMPETITIONS = [
    {"medal": "gold", "rank": "1 / 11", "name": "ACE Datathon — Odometer Mileage",
     "org": "ETH Zurich &amp; Bosch", "place": {"en": "Zurich, Switzerland", "it": "Zurigo, Svizzera"}, "year": "2019"},
    {"medal": "gold", "rank": "1 / 18", "name": "Polimi–Vodafone Challenge",
     "org": "Politecnico di Milano &amp; Vodafone", "place": {"en": "Milan, Italy", "it": "Milano, Italia"}, "year": "2018"},
    {"medal": "bronze", "rank": "3 / 98", "name": "The Mostly AI Prize",
     "org": "Mostly AI", "place": {"en": "Milan, Italy", "it": "Milano, Italia"}, "year": "2025"},
    {"medal": "bronze", "rank": "3 / 36", "name": "Genhack 2 — Climate Change Risk Modelling",
     "org": "École Polytechnique &amp; BNP Paribas", "place": {"en": "Paris, France", "it": "Parigi, Francia"}, "year": "2023"},
]

AWARDS = [
    {"title": {"en": "Leonardo Fibonacci Best Paper Award", "it": "Leonardo Fibonacci Best Paper Award"},
     "where": {"en": "11th International Conference on Machine Learning, Optimization and Data Science, 2025",
               "it": "11ª International Conference on Machine Learning, Optimization and Data Science, 2025"},
     "paper": "Neuro-Symbolic Scene Graph Conditioning for Synthetic Image Dataset Generation",
     "url": "https://doi.org/10.1007/978-3-032-21480-5_27"},
    {"title": {"en": "PhD Awarded <em>Cum Laude</em>", "it": "Dottorato conseguito <em>con lode</em>"},
     "where": {"en": "Politecnico di Milano, 2025", "it": "Politecnico di Milano, 2025"},
     "paper": "Adversarial and Generative Deep Learning for Data Privacy in Human-Centered Artificial Intelligence",
     "url": "https://www.politesi.polimi.it/handle/10589/238117"},
]

EDUCATION = [
    # L'appartenenza al laboratorio dal 2019 attraversa tesi magistrale, dottorato e
    # assegno: non e un incarico che si affianca agli altri, e la continuita che li lega.
    # Sta in cima per questo, e non ha un istituto diverso da quello delle voci sotto.
    {"degree": {"en": "AIRLab Member", "it": "Membro dell'AIRLab"},
     "inst": "AIRLab, DEIB, Politecnico di Milano",
     "period": {"en": "2019 \u2014 <span class='pres'>present</span>",
                "it": "2019 \u2014 <span class='pres'>in corso</span>"}},
    {"degree": {"en": "AIRLab Social Media Manager",
                "it": "Social Media Manager dell'AIRLab"},
     # i canali che gestisce: nome del profilo, non l'indirizzo per esteso, che su
     # carta occuperebbe due righe e nessuno digiterebbe
     "channels": [("linkedin", "airlab-polimi",
                   "https://www.linkedin.com/company/airlab-polimi/"),
                  ("instagram", "airlab_polimi",
                   "https://www.instagram.com/airlab_polimi/")],
     "inst": "AIRLab, DEIB, Politecnico di Milano",
     "period": {"en": "2024 \u2014 <span class='pres'>present</span>",
                "it": "2024 \u2014 <span class='pres'>in corso</span>"}},
    {"degree": {"en": "Postdoctoral Fellow", "it": "Assegnista di ricerca"},
     "inst": "AIRLab, DEIB, Politecnico di Milano",
     "period": {"en": "2025 \u2014 <span class='pres'>present</span>",
                "it": "2025 \u2014 <span class='pres'>in corso</span>"}},
    {"degree": {"en": "PhD in Information Technology <em>cum laude</em>",
                "it": "Dottorato in Information Technology <em>con lode</em>"},
     "inst": "AIRLab, DEIB, Politecnico di Milano",
     "thesis": "Adversarial and Generative Deep Learning for Data Privacy in "
               "Human-Centered Artificial Intelligence",
     "thesis_url": "https://www.politesi.polimi.it/handle/10589/238117",
     "period": {"en": "2020 \u2014 2025", "it": "2020 \u2014 2025"}},
    {"degree": {"en": "MSc in Computer Science and Engineering",
                "it": "Laurea magistrale in Ingegneria Informatica"},
     "inst": "Politecnico di Milano",
     "thesis": "SR-MVS: Multi-View Stereo Enhancement Through Super-Resolution",
     "thesis_url": "https://www.politesi.polimi.it/handle/10589/153077",
     "period": {"en": "2017 \u2014 2020", "it": "2017 \u2014 2020"}},
    {"degree": {"en": "BSc in Information Engineering",
                "it": "Laurea triennale in Ingegneria dell'Informazione"},
     "inst": "Politecnico di Milano",
     "period": {"en": "2013 \u2014 2017", "it": "2013 \u2014 2017"}},
]


# --- i numeri della fascia derivano dagli elenchi: non possono divergere dal contenuto ---
_SUBS = {
    "HOURS": str(TEACHING_HOURS_FLOOR),
    "COURSES": str(len(TEACHING)),
    "THESES": str(len(SUPERVISION)),
    "PHD": str(len(PHD_SUPERVISION)),
}
for _m in METRICS:
    for _k, _v in _SUBS.items():
        _m["v"] = _m["v"].replace(_k, _v)
        for _f in ("s", "note"):
            if _f in _m:
                for _l in LANGS:
                    _m[_f][_l] = _m[_f][_l].replace(_k, _v)


# separatore delle keyword: virgola, non barra
SUPERVISION = [e[:4] + (e[4].replace(" | ", ", "),) for e in SUPERVISION]
PHD_SUPERVISION = [e[:4] + (e[4].replace(" | ", ", "),) for e in PHD_SUPERVISION]


def period_of(p, lang):
    """Il periodo puo essere una stringa neutra o un dict bilingue."""
    return p[lang] if isinstance(p, dict) else p


# elenco unico: dottorato e magistrali insieme, in corso in testa
# (il periodo e un dict solo quando la tesi e in corso)
ALL_SUPERVISION = (
    [("phd",) + e for e in PHD_SUPERVISION if isinstance(e[2], dict)]
    + [("msc",) + e for e in SUPERVISION if isinstance(e[2], dict)]
    + [("phd",) + e for e in PHD_SUPERVISION if not isinstance(e[2], dict)]
    + [("msc",) + e for e in SUPERVISION if not isinstance(e[2], dict)]
)
ONGOING_SUPERVISION = sum(1 for e in ALL_SUPERVISION if isinstance(e[3], dict))


def teaching_labels(t, lang):
    """Costruisce org, dettaglio e periodo a partire dagli atomi, nella lingua richiesta."""
    org_line = "%s, %s" % (VOC[t["kind"]][lang], t["org"].replace(" | ", ", "))
    bits = [VOC[t["role"]][lang]]
    if t["editions"] > 1:
        bits.append("%d %s" % (t["editions"], VOC["editions"][lang]))
    if t.get("ongoing"):
        period = "%s — %s" % (t["from"], UI["present"][lang])
    elif t.get("to") and t["to"] != t["from"]:
        period = "%s — %s" % (t["from"], t["to"])
    else:
        period = t["from"]
    # virgola fra ruolo ed edizioni: sono lo stesso dato. La barra resta dove
    # separa due blocchi diversi, ente e ruolo, ed e messa da chi compone la riga.
    return org_line, ", ".join(bits), period
