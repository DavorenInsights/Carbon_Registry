# Carbon_registry.py
# ------------------------------------------------------------
# Carbon Registry • Landing Page (clean, single-file, embedded theme)
# - No external CSS dependency
# - No render_hero() dependency (fixes your TypeError)
# - Safe navigation via st.switch_page
# ------------------------------------------------------------

import streamlit as st

# -----------------------------
# CONFIG
# -----------------------------
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
        "desc": "Verra-aligned worked examples (demo-style): VM0038, AM0124, VMR0007.",
        "button": "Open Methodology Examples",
        "page": "pages/3_📘_Methodologies.py",  # keep exactly as your filename
        "badge": "Beta",
    },
]

# -----------------------------
# PAGE CONFIG (must be first)
# -----------------------------
st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON, layout="wide")


# -----------------------------
# THEME (embedded CSS)
# -----------------------------
def inject_css() -> None:
    css = r"""
:root{
  --bg:#020c08;
  --panel: rgba(10,25,15,.45);
  --panel2: rgba(10,25,15,.60);
  --stroke: rgba(57,255,159,.20);

  --neon:#39ff9f;
  --mid:#00b46f;
  --soft:#86ffcf;

  --text:#e8fff2;
  --dim:#b3ffdd;

  --r:18px;
  --shadow: 0 0 20px rgba(0,255,138,.12);
  --glow: 0 0 12px rgba(57,255,159,.35);
}

html, body, .stApp{
  background: var(--bg) !important;
  color: var(--text) !important;
  font-family: "Segoe UI", Roboto, sans-serif !important;
}

/* Sidebar */
section[data-testid="stSidebar"]{
  background: rgba(5,20,10,.90) !important;
  backdrop-filter: blur(12px);
  border-right: 1px solid rgba(57,255,159,.12);
  box-shadow: 4px 0 20px rgba(0,255,138,.08);
}
section[data-testid="stSidebar"] *{ color: var(--dim) !important; }
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{ color: var(--soft) !important; }

/* Buttons */
.stButton>button,
button[kind="primary"],
.stDownloadButton button{
  background: var(--mid) !important;
  color: #00120a !important;
  border: none !important;
  font-weight: 700 !important;
  border-radius: var(--r) !important;
  box-shadow: var(--glow) !important;
  transition: .18s ease-in-out !important;
}
.stButton>button:hover,
button[kind="primary"]:hover,
.stDownloadButton button:hover{
  background: var(--neon) !important;
  transform: translateY(-2px);
  box-shadow: 0 0 18px rgba(57,255,159,.65) !important;
}

/* Inputs */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-testid="stTextArea"] textarea,
[data-testid="stSelectbox"] div[role="combobox"],
[data-testid="stMultiSelect"] div[role="combobox"]{
  background: rgba(5,20,10,.55) !important;
  color: var(--text) !important;
  border: 1px solid rgba(57,255,159,.22) !important;
  border-radius: var(--r) !important;
}

/* Widget labels */
[data-testid="stWidgetLabel"] p{
  color: var(--dim) !important;
  font-weight: 600 !important;
}

/* Expanders */
[data-testid="stExpander"]{
  border: 1px solid rgba(57,255,159,.14) !important;
  border-radius: var(--r) !important;
  background: rgba(10,25,15,.22) !important;
}
[data-testid="stExpander"] summary{
  background: rgba(10,30,15,.55) !important;
  border-radius: var(--r) !important;
  border: 1px solid rgba(57,255,159,.14) !important;
}
[data-testid="stExpander"] summary *{ color: var(--soft) !important; }

/* Dataframes */
[data-testid="stDataFrame"]{
  background: rgba(10,25,15,.25) !important;
  border: 1px solid rgba(57,255,159,.14) !important;
  border-radius: var(--r) !important;
  box-shadow: var(--shadow) !important;
  overflow: hidden;
}
[data-testid="stDataFrame"] *{ color: var(--text) !important; }

/* Alerts */
.stAlert{
  border-radius: var(--r) !important;
  border: 1px solid rgba(57,255,159,.14) !important;
  background: rgba(0,255,138,.07) !important;
}
.stSuccess, .stInfo, .stWarning, .stError{
  border-left: 4px solid var(--neon) !important;
}

/* HR */
hr{
  border: none;
  height: 1px;
  background: linear-gradient(90deg,
    rgba(57,255,159,0) 0%,
    rgba(57,255,159,.55) 50%,
    rgba(57,255,159,0) 100%);
  margin: 22px 0;
}

/* Custom cards */
.di-card{
  border-radius: var(--r);
  background: var(--panel);
  border: 1px solid var(--stroke);
  box-shadow: var(--shadow);
  backdrop-filter: blur(16px);
  padding: 22px;
}

/* Hide Streamlit footer */
footer{ visibility:hidden !important; }
"""
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


# -----------------------------
# HERO (embedded, inline-safe)
# -----------------------------
def render_hero(title: str, subtitle_html: str) -> None:
    st.markdown(
        f"""
<div style="
  border-radius:18px;
  background: rgba(10,25,15,.45);
  border: 1px solid rgba(57,255,159,.20);
  box-shadow: 0 0 20px rgba(0,255,138,.12);
  backdrop-filter: blur(16px);
  padding: 26px 26px 14px 26px;
  margin-bottom: 14px;
">
<div style="display:flex; align-items:flex-start; justify-content:space-between; gap:16px; flex-wrap:wrap;">
<div style="min-width:260px;">
<h1 style="margin:0; color:#86ffcf; text-shadow:0 0 10px #39ff9f;">{title}</h1>
<p style="font-size:18px; margin:10px 0 0 0; color:#b3ffdd;">{subtitle_html}</p>
<p style="font-size:14px; margin:10px 0 0 0; color:#b3ffdd; opacity:0.85;">
Suggested flow: <b>{APP_TAGLINE}</b>
</p>
</div>

<div style="
border-radius:14px;
border: 1px solid rgba(57,255,159,.18);
background: rgba(2,12,8,.35);
padding: 12px 14px;
min-width:220px;
    ">
<div style="color:#86ffcf; font-weight:700; margin-bottom:6px;">Build status</div>
<div style="color:#b3ffdd; font-size:13px;">Version: <b>{APP_VERSION}</b></div>
<div style="color:#b3ffdd; font-size:13px; margin-top:4px;">Mode: Foundation beta</div>
</div>
</div>
</div>
""",
        unsafe_allow_html=True,
    )


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

