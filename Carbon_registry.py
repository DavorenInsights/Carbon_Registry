import streamlit as st

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
        "page": "pages/3_📘_Methodologies.py",
        "badge": "Beta",
    },
]

# MUST be first Streamlit call
st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON, layout="wide")


def inject_css() -> None:
    css = r"""
:root{
  --bg:#020c08;
  --panel: rgba(10,25,15,.45);
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
html, body, .stApp{ background: var(--bg) !important; color: var(--text) !important; font-family: "Segoe UI", Roboto, sans-serif !important; }
section[data-testid="stSidebar"]{ background: rgba(5,20,10,.90) !important; backdrop-filter: blur(12px); border-right: 1px solid rgba(57,255,159,.12); box-shadow: 4px 0 20px rgba(0,255,138,.08); }
section[data-testid="stSidebar"] *{ color: var(--dim) !important; }
section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3{ color: var(--soft) !important; }
.stButton>button, button[kind="primary"], .stDownloadButton button{
  background: var(--mid) !important; color:#00120a !important; border:none !important; font-weight:700 !important;
  border-radius: var(--r) !important; box-shadow: var(--glow) !important; transition:.18s ease-in-out !important;
}
.stButton>button:hover, button[kind="primary"]:hover, .stDownloadButton button:hover{
  background: var(--neon) !important; transform: translateY(-2px); box-shadow: 0 0 18px rgba(57,255,159,.65) !important;
}
.di-card{
  border-radius: var(--r);
  background: var(--panel);
  border: 1px solid var(--stroke);
  box-shadow: var(--shadow);
  backdrop-filter: blur(16px);
  padding: 22px;
}
hr{ border:none; height:1px; background: linear-gradient(90deg, rgba(57,255,159,0) 0%, rgba(57,255,159,.55) 50%, rgba(57,255,159,0) 100%); margin: 22px 0; }
footer{ visibility:hidden !important; }
"""
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def render_hero(title: str, subtitle_html: str) -> None:
    st.markdown(
        f"""
<div class="di-card" style="padding: 26px 26px 14px 26px; margin-bottom: 14px;">
<h1 style="margin:0; color:#86ffcf; text-shadow:0 0 10px #39ff9f;">{title}</h1>
<p style="font-size:18px; margin-top:10px; color:#b3ffdd;">{subtitle_html}</p>
<p style="font-size:14px; margin-top:10px; color:#b3ffdd; opacity:0.85;">
Suggested flow: <b>{APP_TAGLINE}</b>
</p>
</div>
""",
        unsafe_allow_html=True,
    )


def safe_switch_page(page_path: str) -> None:
    try:
        st.switch_page(page_path)
    except Exception as e:
        st.error("Navigation failed: page not found or renamed.")
        st.caption(f"Expected file: {page_path}")
        st.caption(f"Details: {e}")


inject_css()

with st.sidebar:
    st.markdown(f"## {APP_ICON} {APP_TITLE}")
    st.caption(APP_VERSION)
    st.divider()
    st.markdown("### Navigation")
    for i, item in enumerate(NAV_ITEMS):
        if st.button(item["card_title"], key=f"side_nav_{i}", use_container_width=True):
            safe_switch_page(item["page"])

render_hero(
    "🌍 Carbon Registry & Methods Explorer",
    "A transparent workspace for <b>boundaries</b>, <b>assumptions</b>, activity logs, and calculator demos."
    f"<br/><span style='opacity:0.85;'>Version: {APP_VERSION}</span>",
)

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
