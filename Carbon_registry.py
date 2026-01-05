# Carbon_registry.py
# ------------------------------------------------------------
# Carbon Registry • Landing Page (clean, single-file, embedded theme)
# - No external CSS dependency
# - No render_hero() dependency (fixes your TypeError)
# - Safe navigation via st.switch_page
# ------------------------------------------------------------


import streamlit as st

# ------------------------------------------------------------
# PAGE CONFIG (must be first Streamlit call)
# ------------------------------------------------------------
st.set_page_config(page_title="Carbon Registry • Methodologies", page_icon="📘", layout="wide")


# ------------------------------------------------------------
# EMBEDDED CSS (full)
# ------------------------------------------------------------
EMBEDDED_CSS = r"""
/* ============================================================
   GLOBAL VARIABLES
============================================================ */
:root {
    --bg-dark: #020c08;
    --bg-card: rgba(10, 25, 15, 0.55);
    --bg-card-strong: rgba(10, 25, 15, 0.85);

    --green-neon: #39ff9f;
    --green-mid: #00b46f;
    --green-soft: #86ffcf;

    --text-light: #e8fff2;
    --text-mid: #b3ffdd;

    --border-glow: 0 0 12px rgba(57, 255, 159, 0.45);
    --shadow-card: 0 0 20px rgba(0, 255, 138, 0.15);

    --radius: 18px;
    --transition: 0.25s ease-in-out;
}

/* ============================================================
   RESET / BASE
============================================================ */
html, body {
    margin: 0 !important;
    padding: 0 !important;
    background: var(--bg-dark) !important;
    font-family: "Segoe UI", Roboto, sans-serif;
    color: var(--text-light);
}

h1, h2, h3, h4 {
    color: var(--green-soft) !important;
    letter-spacing: 0.6px;
    text-shadow: 0 0 8px rgba(57, 255, 159, 0.25);
}

p, label, span, div {
    color: var(--text-mid) !important;
}

/* ============================================================
   STREAMLIT OVERRIDES
============================================================ */
.stApp {
    background: var(--bg-dark) !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(5, 20, 10, 0.9) !important;
    backdrop-filter: blur(12px);
    border-right: 1px solid rgba(57, 255, 159, 0.15);
    box-shadow: 4px 0 20px rgba(0, 255, 138, 0.08);
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: var(--green-soft) !important;
}

/* Sidebar buttons */
.stButton>button {
    background: var(--green-mid) !important;
    color: black !important;
    font-weight: 600;
    border-radius: var(--radius);
    border: none;
    box-shadow: var(--border-glow);
    transition: var(--transition);
}

.stButton>button:hover {
    background: var(--green-neon) !important;
    transform: translateY(-2px);
    box-shadow: 0 0 18px rgba(57, 255, 159, 0.8);
}

/* ============================================================
   CARDS / CONTAINERS
============================================================ */
.im-card, .stContainer, .stMarkdown {
    background: var(--bg-card) !important;
    padding: 18px 22px !important;
    border-radius: var(--radius);
    border: 1px solid rgba(57, 255, 159, 0.2);
    box-shadow: var(--shadow-card);
    backdrop-filter: blur(40px) saturate(120%);
}

/* General input styling */
input, textarea, select {
    background: rgba(5, 20, 10, 0.5) !important;
    border: 1px solid rgba(57, 255, 159, 0.25) !important;
    border-radius: var(--radius) !important;
    color: var(--text-light) !important;
}

input:focus, textarea:focus, select:focus {
    border-color: var(--green-neon) !important;
    box-shadow: var(--border-glow);
}

/* Metric outputs */
.stSuccess, .stAlert {
    border-left: 4px solid var(--green-neon) !important;
    background: rgba(0, 255, 138, 0.08) !important;
    color: var(--green-soft) !important;
}

/* ============================================================
   GLOW SEPARATORS
============================================================ */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(
        90deg,
        rgba(57, 255, 159, 0) 0%,
        rgba(57, 255, 159, 0.6) 50%,
        rgba(57, 255, 159, 0) 100%
    );
    margin: 25px 0;
}

/* ============================================================
   CUSTOM UTILITY CLASSES
============================================================ */
.green-glow {
    text-shadow: 0 0 12px var(--green-neon);
    color: var(--green-neon) !important;
    font-weight: 700;
}

.card {
    background: var(--bg-card);
    border-radius: var(--radius);
    padding: 20px;
    border: 1px solid rgba(57, 255, 159, 0.25);
    box-shadow: var(--shadow-card);
    backdrop-filter: blur(14px);
}

.glass-box {
    border-radius: var(--radius);
    background: rgba(10, 25, 15, 0.45);
    border: 1px solid rgba(57, 255, 159, 0.25);
    padding: 25px;
    box-shadow: var(--shadow-card);
    backdrop-filter: blur(30px);
}

/* ============================================================
   EXPANDERS
============================================================ */
.streamlit-expanderHeader {
    background: rgba(10, 30, 15, 0.6) !important;
    color: var(--green-soft) !important;
    border-radius: var(--radius) !important;
}

/* ============================================================
   TABLES
============================================================ */
tbody, thead, tr, th, td {
    color: var(--text-light) !important;
    background: rgba(10, 30, 15, 0.25) !important;
    border-color: rgba(57, 255, 159, 0.2) !important;
}

/* ============================================================
   SUCCESS, WARNING, INFO TEXT
============================================================ */
.stSuccess, .stWarning, .stInfo, .stError {
    padding: 12px 18px !important;
    border-radius: var(--radius) !important;
    border-left: 4px solid var(--green-neon) !important;
}

/* ============================================================
   BUTTONS (global)
============================================================ */
button[kind="primary"], .stDownloadButton button {
    background: var(--green-mid) !important;
    color: black !important;
    border-radius: var(--radius) !important;
    border: none !important;
    box-shadow: var(--border-glow) !important;
    transition: var(--transition);
    font-weight: 600 !important;
}

button[kind="primary"]:hover,
.stDownloadButton button:hover {
    background: var(--green-neon) !important;
    transform: translateY(-2px);
    box-shadow: 0 0 20px rgba(57, 255, 159, 0.7) !important;
}

/* ============================================================
   FOOTER HIDE
============================================================ */
footer { visibility: hidden !important; }

/* ============================================================
   ALTAIR / VEGA EMBED BACKGROUND (dark-friendly)
============================================================ */
.vega-embed, .vega-embed details, .vega-embed summary {
    background: rgba(10, 25, 15, 0.35) !important;
    border: 1px solid rgba(57, 255, 159, 0.20) !important;
    box-shadow: 0 0 20px rgba(0, 255, 138, 0.12) !important;
    border-radius: 18px !important;
    padding: 10px !important;
}

/* ============================================================
   END OF FILE
============================================================ */
"""
st.markdown(f"<style>{EMBEDDED_CSS}</style>", unsafe_allow_html=True)


import streamlit as st


# -----------------------------
# NAVIGATION
# -----------------------------
def safe_switch_page(page_path: str) -> None:
    try:
        st.switch_page(page_path)
    except Exception as e:
        st.error("Navigation failed: page not found or renamed.")
        st.caption(f"Expected file: {page_path}")
        st.caption(f"Details: {e}")


# -----------------------------
# RENDER
# -----------------------------
inject_css()

with st.sidebar:
    st.markdown(f"## {APP_ICON} {APP_TITLE}")
    st.caption(APP_VERSION)
    st.divider()

    st.markdown("### Navigation")
    for i, item in enumerate(NAV_ITEMS):
        if st.button(item["card_title"], key=f"side_nav_{i}", use_container_width=True):
            safe_switch_page(item["page"])

    st.divider()

    with st.expander("How to use (fast)"):
        st.write("1) Define **boundaries** for a project.")
        st.write("2) Record **assumptions + data sources**.")
        st.write("3) Run **calculator demos** with transparent factors.")
        st.write("4) Export notes/results for review.")


render_hero(
    title="🌍 Carbon Registry & Methods Explorer",
    subtitle_html=(
        "A transparent workspace for <b>boundaries</b>, <b>assumptions</b>, activity logs, and calculator demos."
        f"<br/><span style='opacity:0.85;'>Version: {APP_VERSION}</span>"
    ),
)

# Quick actions
qa1, qa2, qa3, qa4 = st.columns(4)

with qa1:
    if st.button("📌 Roadmap", use_container_width=True):
        st.info(
            "Roadmap (near-term)\n"
            "- Stabilize Registry data model (projects, activities, assumptions)\n"
            "- Finalize Scope calculator assumptions panel (sources + uncertainty)\n"
            "- Convert Methodology tools into worked examples (demo-ready)\n"
            "- Add Dialogue layer (guided boundary + assumption prompts)\n"
            "- Futures funnel stays separate (blog/sandbox)"
        )

with qa2:
    if st.button("📄 Docs", use_container_width=True):
        st.info(
            "Docs (how to use)\n"
            "1) Create a project and define boundaries\n"
            "2) Log activities and attach data sources\n"
            "3) Run a calculator demo with assumptions visible\n"
            "4) Export/record results for review"
        )

with qa3:
    if st.button("🐞 Report Bug", use_container_width=True):
        st.warning("Bug reporting (temporary): copy/paste this into your notes or issue tracker.")
        st.code(
            f"App: {APP_TITLE}\nVersion: {APP_VERSION}\nPage: Home\nStreamlit: {st.__version__}",
            language="text",
        )

with qa4:
    if st.button("✨ What’s New", use_container_width=True):
        st.success(
            "What’s new\n"
            "- Home hub repositioned as foundation tool\n"
            "- Quick actions enabled\n"
            "- Clearer module descriptions + disclaimers"
        )

st.write("")

# Nav cards
cols = st.columns(3)
for idx, item in enumerate(NAV_ITEMS):
    with cols[idx]:
        st.markdown(
            f"""
<div class="di-card">
<div style="display:flex; justify-content:space-between; align-items:center; gap:12px;">
<h3 style="margin:0; color:#86ffcf;">{item["card_title"]}</h3>
<span style="font-size:12px; opacity:0.85; color:#b3ffdd;">{item["badge"]}</span>
</div>
<p style="margin-top:10px; color:#b3ffdd;">{item["desc"]}</p>
</div>
""",
            unsafe_allow_html=True,
        )
        if st.button(item["button"], key=f"nav_btn_{idx}", use_container_width=True):
            safe_switch_page(item["page"])

st.divider()
st.caption(
    "Disclaimer: Beta tool for learning and analysis — not audit-ready. "
    "Validate inputs/results against the applicable standard/methodology and verified datasets."
)
st.caption(f"{APP_TITLE} • {APP_VERSION}")

