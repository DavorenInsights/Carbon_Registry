from __future__ import annotations

import streamlit as st
from pathlib import Path
from typing import List, Dict, Optional

# ---------------------------------------------------------
# APP CONSTANTS
# ---------------------------------------------------------
APP_TITLE = "Carbon Registry"
APP_ICON = "🌍"
APP_VERSION = "v1.0 (foundation beta)"
APP_TAGLINE = "Boundaries → Assumptions → Calculators → Evidence"

NAV_ITEMS: List[Dict[str, str]] = [
    {
        "card_title": "🏠 Home",
        "desc": "Launch hub and navigation.",
        "button": "Open Home",
        "page": "Carbon_registry.py",
        "badge": "Hub",
    },
    {
        "card_title": "⚖️ Carbon Registry",
        "desc": "Create projects, log activity, capture boundaries + assumptions.",
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
        "desc": "Worked examples (demos): VM0038, AM0124, VMR0007.",
        "button": "Open Methodology Examples",
        "page": "pages/3_Methodologies.py",
        "badge": "Beta",
    },
]

# ---------------------------------------------------------
# THEME LOADING (robust across multipage)
# ---------------------------------------------------------
def _repo_root() -> Path:
    """
    utils/ui.py is in utils/.
    Repo root is one level above utils/ (parent of utils).
    This works from any page import.
    """
    return Path(__file__).resolve().parents[1]

def _read_css_from_assets() -> Optional[str]:
    css_path = _repo_root() / "assets" / "style.css"
    if css_path.exists():
        return css_path.read_text(encoding="utf-8")
    return None

def _embedded_fallback_css() -> str:
    # Fallback: safe minimal theme if assets/style.css missing.
    # Your full CSS can remain in assets/style.css; this is a safety net.
    return """
    :root {
        --bg-dark:#020c08; --green-neon:#39ff9f; --green-mid:#00b46f; --green-soft:#86ffcf;
        --text-light:#e8fff2; --text-mid:#b3ffdd; --radius:18px;
    }
    html, body, .stApp { background: var(--bg-dark) !important; color: var(--text-light) !important; }
    h1,h2,h3,h4 { color: var(--green-soft) !important; text-shadow:0 0 8px rgba(57,255,159,.25); }
    section[data-testid="stSidebar"] { background: rgba(5,20,10,.9) !important; border-right:1px solid rgba(57,255,159,.15); }
    .stButton>button { background: var(--green-mid) !important; color:black !important; border-radius: var(--radius) !important; }
    .stButton>button:hover { background: var(--green-neon) !important; }
    """

def inject_css() -> None:
    css = _read_css_from_assets()
    if not css:
        css = _embedded_fallback_css()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# ---------------------------------------------------------
# PAGE SETUP (single, consistent)
# ---------------------------------------------------------
def setup_page(*, page_title: str, page_icon: str, layout: str = "wide") -> None:
    """
    Must be called before any other Streamlit UI calls in the page.
    """
    st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
    inject_css()

# ---------------------------------------------------------
# NAVIGATION
# ---------------------------------------------------------
def safe_switch_page(page_path: str) -> None:
    try:
        st.switch_page(page_path)
    except Exception as e:
        st.error("Navigation failed: page not found or renamed.")
        st.caption(f"Expected file: {page_path}")
        st.caption(f"Details: {e}")

def sidebar_nav(*, show_how_to: bool = True, show_whats_new: bool = True) -> None:
    with st.sidebar:
        st.markdown(f"## {APP_ICON} {APP_TITLE}")
        st.caption(APP_VERSION)
        st.divider()

        st.markdown("### Navigation")
        for i, item in enumerate(NAV_ITEMS):
            if st.button(item["card_title"], key=f"side_nav_{i}", use_container_width=True):
                safe_switch_page(item["page"])

        if show_how_to:
            st.divider()
            with st.expander("How to use (fast)"):
                st.write("1) Define **boundaries** for a project.")
                st.write("2) Record **assumptions + data sources**.")
                st.write("3) Run **calculator demos** with transparent factors.")
                st.write("4) Export notes/results for review.")

        if show_whats_new:
            with st.expander("What’s new"):
                st.write("- UI utilities stabilized (no more signature crashes)")
                st.write("- CSS loading fixed for multipage paths")
                st.write("- Theme now consistent across pages")

# ---------------------------------------------------------
# HERO (stable signature!)
# ---------------------------------------------------------
def render_hero(*, title: str, subtitle: str, tagline: Optional[str] = None) -> None:
    """
    Stable signature: render_hero(title=..., subtitle=..., tagline=...)
    'subtitle' can contain HTML if you want (set unsafe=True below).
    """
    st.markdown(
    f"""
    <div style='padding: 28px 30px 14px 30px;'>
    <h1 style='color:#86ffcf; text-shadow:0 0 10px #39ff9f; margin-bottom:6px;'>
    {title}
    </h1>
    <p style='font-size:18px; color:#b3ffdd; margin-top:0;'>
    {subtitle}
    </p>
    {"<p style='font-size:14px; color:#b3ffdd; opacity:0.85; margin-top:12px;'>" +
    {"Suggested flow: <b>" + tagline + "</b></p>" if tagline else ""}
    </div>
        """,
        unsafe_allow_html=True,
    )
