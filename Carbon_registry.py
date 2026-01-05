import streamlit as st

# ---------------------------------------------------------
# CONFIG
# ---------------------------------------------------------
APP_TITLE = "Carbon Registry"
APP_ICON = "🌍"
APP_VERSION = "v1.0 (foundation beta)"
APP_TAGLINE = "Boundaries → Assumptions → Calculators → Evidence"

NAV_ITEMS = [
    {
        "card_title": "⚖️ Carbon Registry",
        "desc": "Create projects, log activities, and capture boundaries + assumptions.",
        "button": "Open Carbon Registry",
        "page": "pages/1_Registry.py",
        "badge": "Core",
    },
    {
        "card_title": "📊 Scope 1 / 2 / 3 Calculator",
        "desc": "Baseline estimates across scopes with transparent factors + assumptions.",
        "button": "Open Scope Calculator",
        "page": "pages/2_Scope_Calculator.py",
        "badge": "Core",
    },
    {
        "card_title": "📘 Methodology Tools",
        "desc": "Verra-aligned worked examples (demos, not audit outputs): VM0038, VMR0007, EV, hydrogen.",
        "button": "Open Methodology Examples",
        "page": "pages/3_📘_Methodologies.py",  # keep exactly as your file name
        "badge": "Beta",
    },
]

# ---------------------------------------------------------
# PAGE CONFIG (ONLY ONCE, FIRST STREAMLIT CALL)
# ---------------------------------------------------------
st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON, layout="wide")


def safe_switch_page(page_path: str) -> None:
    """Switch pages with a friendly error if the target can't be opened."""
    try:
        st.switch_page(page_path)
    except Exception as e:
        st.error("Navigation failed: page not found or renamed.")
        st.caption(f"Expected file: {page_path}")
        st.caption(f"Details: {e}")


def inject_css() -> None:
    """Embedded CSS injection (no external file dependency)."""
    css = r"""
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

html, body {
    margin: 0 !important;
    padding: 0 !important;
    background: var(--bg-dark) !important;
    font-family: "Segoe UI", Roboto, sans-serif !important;
    color: var(--text-light) !important;
}

.stApp {
    background: var(--bg-dark) !important;
}

h1, h2, h3, h4 {
    color: var(--green-soft) !important;
    letter-spacing: 0.6px;
    text-shadow: 0 0 8px rgba(57, 255, 159, 0.25);
}

p, label, span, div {
    color: var(--text-mid) !important;
}

section[data-testid="stSidebar"] {
    background: rgba(5, 20, 10, 0.9) !important;
    backdrop-filter: blur(12px);
    border-right: 1px solid rgba(57, 255, 159, 0.15);
    box-shadow: 4px 0 20px rgba(0, 255, 138, 0.08);
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] div {
    color: var(--green-soft) !important;
}

.stButton > button,
button[kind="primary"],
.stDownloadButton button {
    background: var(--green-mid) !important;
    color: black !important;
    font-weight: 700 !important;
    border-radius: var(--radius) !important;
    border: none !important;
    box-shadow: var(--border-glow) !important;
    transition: var(--transition) !important;
}

.stButton > button:hover,
button[kind="primary"]:hover,
.stDownloadButton button:hover {
    background: var(--green-neon) !important;
    transform: translateY(-2px);
    box-shadow: 0 0 20px rgba(57, 255, 159, 0.7) !important;
}

/* IMPORTANT: DO NOT STYLE .stMarkdown AS A CARD */

.card, .glass-box {
    border-radius: var(--radius);
    border: 1px solid rgba(57, 255, 159, 0.25);
    box-shadow: var(--shadow-card);
    backdrop-filter: blur(30px);
}

.card {
    background: var(--bg-card);
    padding: 20px;
}

.glass-box {
    background: rgba(10, 25, 15, 0.45);
    padding: 25px;
}

input, textarea, select {
    background: rgba(5, 20, 10, 0.5) !important;
    border: 1px solid rgba(57, 255, 159, 0.25) !important;
    border-radius: var(--radius) !important;
    color: var(--text-light) !important;
}

input:focus, textarea:focus, select:focus {
    border-color: var(--green-neon) !important;
    box-shadow: var(--border-glow) !important;
}

.stSuccess, .stWarning, .stInfo, .stError {
    padding: 12px 18px !important;
    border-radius: var(--radius) !important;
    border-left: 4px solid var(--green-neon) !important;
    background: rgba(0, 255, 138, 0.08) !important;
}

div[data-testid="stExpander"] summary {
    background: rgba(10, 30, 15, 0.6) !important;
    color: var(--green-soft) !important;
    border-radius: var(--radius) !important;
    border: 1px solid rgba(57, 255, 159, 0.18) !important;
}

div[data-testid="stExpander"] summary:hover {
    border-color: rgba(57, 255, 159, 0.35) !important;
}

div[data-testid="stDataFrame"] * {
    color: var(--text-light) !important;
}

table, thead, tbody, tr, th, td {
    background: rgba(10, 30, 15, 0.22) !important;
    border-color: rgba(57, 255, 159, 0.18) !important;
}

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

footer { visibility: hidden !important; }
"""
    st.markdown(f"<style id='di-theme'>{css}</style>", unsafe_allow_html=True)


def render_hero_inline(title: str, subtitle_html: str) -> None:
    st.markdown(
        f"""
<div class="glass-box" style="padding: 26px 26px 14px 26px; margin-bottom: 14px;">
<h1 style="margin:0; color:#86ffcf; text-shadow:0 0 10px #39ff9f;">{title}</h1>
<p style="font-size:18px; margin-top:10px; color:#b3ffdd;">{subtitle_html}</p>
<p style="font-size:14px; margin-top:10px; color:#b3ffdd; opacity:0.85;">
Suggested flow: <b>{APP_TAGLINE}</b>
</p>
</div>
        """,
        unsafe_allow_html=True,
    )


# Inject theme
inject_css()

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
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

    with st.expander("What’s new"):
        st.write("- Home hub repositioned as foundation tool (not audit-grade MRV)")
        st.write("- Quick Actions enabled (roadmap/docs/bug/what’s new)")
        st.write("- Clearer module descriptions + disclaimers")

# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------
render_hero_inline(
    title="🌍 Carbon Registry & Methods Explorer",
    subtitle_html=(
        "A transparent workspace for <b>boundaries</b>, <b>assumptions</b>, activity logs, and calculator demos."
        f"<br/><span style='opacity:0.85;'>Version: {APP_VERSION}</span>"
    ),
)

# ---------------------------------------------------------
# QUICK ACTIONS
# ---------------------------------------------------------
qa1, qa2, qa3, qa4 = st.columns(4)

with qa1:
    if st.button("📌 Roadmap", key="qa_roadmap", use_container_width=True):
        st.info(
            "Roadmap (near-term)\n"
            "- Stabilize Registry data model (projects, activities, assumptions)\n"
            "- Finalize Scope calculator assumptions panel (sources + uncertainty)\n"
            "- Convert Methodology tools into worked examples (demo-ready)\n"
            "- Add Dialogue layer (guided boundary + assumption prompts)\n"
            "- Futures funnel stays separate (blog/sandbox)"
        )

with qa2:
    if st.button("📄 Docs", key="qa_docs", use_container_width=True):
        st.info(
            "Docs (how to use)\n"
            "1) Create a project and define boundaries\n"
            "2) Log activities and attach data sources\n"
            "3) Run a calculator demo with assumptions visible\n"
            "4) Export/record results for review"
        )

with qa3:
    if st.button("🐞 Report Bug", key="qa_bug", use_container_width=True):
        st.warning("Bug reporting (temporary): copy/paste this into your notes or issue tracker.")
        st.code(
            f"App: {APP_TITLE}\nVersion: {APP_VERSION}\nPage: Home\nStreamlit: {st.__version__}",
            language="text",
        )

with qa4:
    if st.button("✨ What’s New", key="qa_whatsnew", use_container_width=True):
        st.success(
            "What’s new\n"
            "- Home hub repositioned as foundation tool\n"
            "- Quick actions enabled\n"
            "- Clearer module descriptions + disclaimers"
        )

st.write("")

# ---------------------------------------------------------
# NAV CARDS
# ---------------------------------------------------------
cols = st.columns(3)

for idx, item in enumerate(NAV_ITEMS):
    with cols[idx]:
        st.markdown(
            f"""
<div class='glass-box'>
<div style='display:flex; justify-content:space-between; align-items:center; gap:12px;'>
<h3 style='margin:0;'>{item["card_title"]}</h3>
<span style='font-size:12px; opacity:0.8;'>{item["badge"]}</span>
</div>
<p style='margin-top:10px;'>{item["desc"]}</p>
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
