import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Peccioli x New Orleans 2026",
    page_icon="🎷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# Helper immagini
# ----------------------------
BASE_DIR = Path(__file__).parent

def find_image(possible_names):
    for name in possible_names:
        p = BASE_DIR / name
        if p.exists():
            return str(p)
    return None

logo_path = find_image([
    "logo_comune.png",
    "logo_comune.jpg",
    "logo_comune.jpeg",
])

hero_img_1 = find_image([
    "Neworleans_foto.png",
    "Neworleans_foto.jpg",
    "Neworleans_foto.jpeg",
])

hero_img_2 = find_image([
    "New-Orleans_foto2.png",
    "New-Orleans_foto2.jpg",
    "New-Orleans_foto2.jpeg",
    "New-Orleans-April25-issue-CNTUS-Maya-Visnyei-Global.png",
])

# ----------------------------
# Stili grafici
# ----------------------------
st.markdown("""
<style>
html, body, [class*="css"]  {
    font-family: "Segoe UI", sans-serif;
}

.block-container {
    max-width: 1200px;
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #10233f 0%, #19365f 100%);
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.hero-box {
    padding: 1.8rem 1.8rem 1.5rem 1.8rem;
    border-radius: 28px;
    background: linear-gradient(135deg, #14213d 0%, #5b3a29 55%, #d08c38 100%);
    color: white;
    box-shadow: 0 16px 38px rgba(0,0,0,0.18);
    margin-bottom: 1.1rem;
}

.hero-title {
    font-size: 2.4rem;
    font-weight: 800;
    margin-bottom: 0.2rem;
    line-height: 1.1;
}

.hero-subtitle {
    font-size: 1.1rem;
    opacity: 0.92;
    margin-bottom: 0.9rem;
}

.hero-text {
    font-size: 1rem;
    line-height: 1.65;
}

.section-title {
    margin-top: 0.3rem;
    margin-bottom: 0.2rem;
}

.card {
    background: white;
    border-radius: 22px;
    padding: 1.1rem 1rem 1rem 1rem;
    border: 1px solid rgba(20,33,61,0.08);
    box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    height: 100%;
}

.card-title {
    font-size: 1.06rem;
    font-weight: 700;
    color: #14213d;
    margin-bottom: 0.35rem;
}

.soft-box {
    padding: 1rem 1rem;
    background: #f8fafc;
    border: 1px solid rgba(0,0,0,0.06);
    border-radius: 18px;
}

.mini-label {
    display: inline-block;
    background: #eef4ff;
    color: #19365f;
    padding: 0.25rem 0.55rem;
    border-radius: 999px;
    font-size: 0.8rem;
    margin-right: 0.35rem;
    margin-bottom: 0.35rem;
}

.note {
    color: #5b6472;
    font-size: 0.93rem;
}

.footer-box {
    text-align: center;
    color: #6c757d;
    font-size: 0.9rem;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Dati demo
# ----------------------------
incontri = pd.DataFrame([
    {"Data": "15 maggio 2026", "Titolo": "Benvenuti a New Orleans", "Formato": "In presenza", "Focus": "Introduzione al progetto, identità della città, curiosità iniziali"},
    {"Data": "29 maggio 2026", "Titolo": "Musica, jazz e street art", "Formato": "Incontro con esperto", "Focus": "Come leggere la città attraverso arte, musica e comunità"},
    {"Data": "12 giugno 2026", "Titolo": "Memoria, schiavitù e diritti civili", "Formato": "In presenza", "Focus": "Una preparazione semplice ma seria ai temi storici del viaggio"},
    {"Data": "26 giugno 2026", "Titolo": "Collegamento con New Orleans", "Formato": "Online", "Focus": "Domande, curiosità e primo contatto con una realtà locale"},
    {"Data": "10 luglio 2026", "Titolo": "Raccontare l’esperienza", "Formato": "Laboratorio", "Focus": "Foto, note, diario e idee per condividere il viaggio"},
])

materiali = pd.DataFrame([
    {"Titolo": "Guida rapida a New Orleans", "Tipo": "Scheda PDF", "Tema": "Introduzione", "Link": "https://example.com/guida-new-orleans"},
    {"Titolo": "Playlist jazz per entrare nell’atmosfera", "Tipo": "Playlist", "Tema": "Musica", "Link": "https://example.com/playlist-jazz"},
    {"Titolo": "Breve storia della Louisiana", "Tipo": "Articolo", "Tema": "Storia", "Link": "https://example.com/storia-louisiana"},
    {"Titolo": "Katrina e la rinascita della città", "Tipo": "Video", "Tema": "Resilienza", "Link": "https://example.com/video-katrina"},
    {"Titolo": "Cultura creola e cajun in 10 minuti", "Tipo": "Video", "Tema": "Multiculturalità", "Link": "https://example.com/creola-cajun"},
    {"Titolo": "Street art e identità urbana", "Tipo": "Articolo", "Tema": "Arte", "Link": "https://example.com/street-art-nola"},
])

mappe_df = pd.DataFrame({
    "lat": [29.9584, 29.9596, 29.9489, 29.9214, 29.9623],
    "lon": [-90.0645, -90.0773, -90.0715, -90.0790, -90.0637],
    "luogo": [
        "French Quarter",
        "Congo Square",
        "Warehouse District",
        "Lower Ninth Ward",
        "Jackson Square"
    ]
})

temi = [
    {
        "titolo": "Tradizioni culturali e multiculturalità",
        "testo": "New Orleans è un intreccio vivo di culture africane, francesi, creole, caraibiche e americane. L’idea è aiutare i ragazzi a leggere la città come uno spazio in cui le differenze non si cancellano, ma convivono e si rafforzano."
    },
    {
        "titolo": "Storia della schiavitù e dei diritti civili",
        "testo": "Una chiave importante per comprendere la città è il suo rapporto con la memoria: schiavitù, segregazione, diritti civili e il loro riflesso nella società contemporanea."
    },
    {
        "titolo": "Cultura musicale e artistica",
        "testo": "Jazz, piccoli club, street art, jam session e murales: a New Orleans l’arte è parte della vita quotidiana e racconta la voce delle comunità."
    },
    {
        "titolo": "Rinascita dopo Katrina",
        "testo": "Capire Katrina significa capire la resilienza della città, la ricostruzione dei quartieri e il legame profondo tra crisi, comunità e futuro."
    },
]

quiz_domande = [
    {
        "domanda": "Quale elemento rappresenta meglio New Orleans?",
        "opzioni": ["Solo turismo e divertimento", "Un intreccio di musica, memoria, culture e resilienza", "Una città americana come tutte le altre"],
        "corretta": "Un intreccio di musica, memoria, culture e resilienza",
        "spiegazione": "È proprio questa la chiave del progetto."
    },
    {
        "domanda": "Perché il jazz è così importante a New Orleans?",
        "opzioni": ["Perché è nato lì", "Perché non esistono altri generi", "Perché viene ascoltato solo nei musei"],
        "corretta": "Perché è nato lì",
        "spiegazione": "New Orleans è considerata la culla del jazz."
    },
    {
        "domanda": "Perché si parla di Katrina nel progetto?",
        "opzioni": ["Per capire come una città affronta una grande crisi", "Perché è solo una curiosità climatica", "Perché non riguarda New Orleans"],
        "corretta": "Per capire come una città affronta una grande crisi",
        "spiegazione": "Katrina aiuta a leggere il tema della resilienza urbana e comunitaria."
    },
]

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    if logo_path:
        st.image(logo_path, width=120)
    st.markdown("## Portale ragazzi")
    st.write("Uno spazio demo per accompagnare il progetto prima, durante e dopo il viaggio.")
    pagina = st.radio(
        "Naviga",
        [
            "Home",
            "Calendario incontri",
            "Materiali consigliati",
            "Mappe",
            "Schede temi",
            "Video e articoli",
            "Quiz e curiosità"
        ]
    )
    st.markdown("---")
    st.markdown("**Periodo indicativo**")
    st.write("Settembre 2026 • 8/9 giorni")
    st.markdown("**Temi**")
    st.markdown("""
    <span class="mini-label">Multiculturalità</span>
    <span class="mini-label">Jazz</span>
    <span class="mini-label">Diritti civili</span>
    <span class="mini-label">Street art</span>
    <span class="mini-label">Katrina</span>
    """, unsafe_allow_html=True)

# ----------------------------
# Hero header con logo e foto
# ----------------------------
col_logo, col_title = st.columns([1.1, 5])

with col_logo:
    if logo_path:
        st.image(logo_path, width=135)

with col_title:
    st.markdown("""
    <div class="hero-box">
        <div class="hero-title">Peccioli x New Orleans 2026</div>
        <div class="hero-subtitle">Portale demo per accompagnare i ragazzi nel progetto di scambio culturale</div>
        <div class="hero-text">
            Una proposta digitale pensata per essere davvero utile: calendario degli incontri,
            materiali consigliati, mappe, schede sui temi del viaggio, link di approfondimento
            e piccoli quiz per incuriosire i partecipanti prima della partenza.
        </div>
    </div>
    """, unsafe_allow_html=True)

img_col1, img_col2 = st.columns(2)
with img_col1:
    if hero_img_1:
        st.image(hero_img_1, use_container_width=True)
with img_col2:
    if hero_img_2:
        st.image(hero_img_2, use_container_width=True)

st.markdown("")

# ----------------------------
# Pagine
# ----------------------------
if pagina == "Home":
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="card">
            <div class="card-title">Prima del viaggio</div>
            Incontri, materiali introduttivi, curiosità e strumenti per arrivare preparati e creare gruppo.
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="card">
            <div class="card-title">Durante</div>
            Un punto di riferimento per orientarsi tra temi, luoghi e spunti utili da vivere sul posto.
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="card">
            <div class="card-title">Dopo</div>
            Uno spazio che può restare come memoria dell’esperienza e base per iniziative future.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Cosa si può fare qui")
    st.write("""
    Questa demo mostra come un portale del progetto possa diventare qualcosa di concreto e utile per i ragazzi:
    non solo una vetrina, ma uno strumento da usare davvero per prepararsi, orientarsi e restare coinvolti.
    """)

    st.markdown("""
    <div class="soft-box">
        <strong>Idea del progetto digitale:</strong> accompagnare il gruppo prima della partenza,
        stimolare curiosità, semplificare l’accesso ai materiali e lasciare una traccia dell’esperienza nel tempo.
    </div>
    """, unsafe_allow_html=True)

elif pagina == "Calendario incontri":
    st.header("📅 Calendario incontri")
    st.write("Una proposta di percorso formativo pre-viaggio, pensata in modo semplice e coinvolgente.")
    for _, row in incontri.iterrows():
        st.markdown(f"""
        <div class="card" style="margin-bottom:0.8rem;">
            <div class="card-title">{row['Data']} — {row['Titolo']}</div>
            <div class="note"><strong>Formato:</strong> {row['Formato']}</div>
            <div style="margin-top:0.45rem;">{row['Focus']}</div>
        </div>
        """, unsafe_allow_html=True)

elif pagina == "Materiali consigliati":
    st.header("📚 Materiali consigliati")
    st.write("Una piccola raccolta demo di contenuti introduttivi per arrivare più curiosi e più consapevoli.")
    filtro = st.selectbox("Filtra per tema", ["Tutti"] + sorted(materiali["Tema"].unique().tolist()))
    data = materiali if filtro == "Tutti" else materiali[materiali["Tema"] == filtro]
    for _, row in data.iterrows():
        st.markdown(f"""
        <div class="card" style="margin-bottom:0.75rem;">
            <div class="card-title">{row['Titolo']}</div>
            <div class="note">{row['Tipo']} • {row['Tema']}</div>
            <div style="margin-top:0.45rem;"><a href="{row['Link']}" target="_blank">Apri contenuto</a></div>
        </div>
        """, unsafe_allow_html=True)

elif pagina == "Mappe":
    st.header("🗺️ Mappe")
    st.write("Una mappa demo con alcuni luoghi simbolici collegati ai temi del progetto.")
    st.map(mappe_df.rename(columns={"lat": "LAT", "lon": "LON"}), latitude="LAT", longitude="LON", size=12)
    st.markdown("### Luoghi evidenziati")
    st.write(", ".join(mappe_df["luogo"].tolist()))

elif pagina == "Schede temi":
    st.header("📝 Brevi schede sui temi del viaggio")
    st.write("Schede sintetiche per dare un primo orientamento e aiutare i ragazzi a entrare nel clima del progetto.")
    for tema in temi:
        with st.expander(tema["titolo"], expanded=False):
            st.write(tema["testo"])

elif pagina == "Video e articoli":
    st.header("🎥 Video e articoli")
    st.write("Una sezione demo pensata per raccogliere in modo ordinato contenuti utili da consultare.")
    col1, col2 = st.columns(2)
    items = list(materiali.to_dict("records"))
    left = items[::2]
    right = items[1::2]
    with col1:
        for row in left:
            st.markdown(f"""
            <div class="card" style="margin-bottom:0.75rem;">
                <div class="card-title">{row['Titolo']}</div>
                <div class="note">{row['Tipo']} • {row['Tema']}</div>
                <div style="margin-top:0.45rem;"><a href="{row['Link']}" target="_blank">Vai al contenuto</a></div>
            </div>
            """, unsafe_allow_html=True)
    with col2:
        for row in right:
            st.markdown(f"""
            <div class="card" style="margin-bottom:0.75rem;">
                <div class="card-title">{row['Titolo']}</div>
                <div class="note">{row['Tipo']} • {row['Tema']}</div>
                <div style="margin-top:0.45rem;"><a href="{row['Link']}" target="_blank">Vai al contenuto</a></div>
            </div>
            """, unsafe_allow_html=True)

elif pagina == "Quiz e curiosità":
    st.header("❓ Quiz e curiosità")
    st.write("Piccole domande per incuriosire i ragazzi e farli entrare nello spirito del viaggio.")
    score = 0
    answered = 0
    for i, q in enumerate(quiz_domande):
        risposta = st.radio(q["domanda"], q["opzioni"], key=f"quiz_{i}", index=None)
        if risposta:
            answered += 1
            if risposta == q["corretta"]:
                st.success(q["spiegazione"])
                score += 1
            else:
                st.warning(q["spiegazione"])
        st.markdown("---")
    if st.button("Mostra il mio risultato"):
        if answered == 0:
            st.info("Rispondi ad almeno una domanda.")
        else:
            st.info(f"Hai risposto correttamente a {score} domande su {len(quiz_domande)}.")

st.markdown("<div class='footer-box'>Demo grafica del portale ragazzi • Peccioli x New Orleans 2026</div>", unsafe_allow_html=True)
