# utils/ui.py
from __future__ import annotations

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from typing import List, Dict, Any

# -------------------------------
# App constants
# -------------------------------
APP_TITLE = "Carbon Registry"
APP_VERSION = "v1.0 (foundation beta)"

# -------------------------------
# Navigation model
# IMPORTANT: These must match your actual filenames in /pages
# -------------------------------
NAV_ITEMS: List[Dict[str, Any]] = [
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
        "desc": "Verra-aligned worked examples (demos, not audit outputs): VM0038, AM0124, VMR0007.",
        "button": "Open Methodology Examples",
        "page": "pages/3_Methodologies.py",
        "badge": "Beta",
    },
]

# -------------------------------
# CSS loader (robust for multipage + Streamlit Cloud)
# -------------------------------
def _read_css(css_path: Path) -> str:
    try:
        return css_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""

def inject_css(css: str) -> None:
    """Inject CSS twice for robustness (markdown + html component)."""
    if not css.strip():
        return
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    components.html(f"<style>{css}</style>", height=0, width=0)

def setup_page(*, page_title: str, page_icon: str = "🌍", layout: str = "wide") -> None:
    """
    Call this at the TOP of every page, before other Streamlit rendering.
    Sets page config and injects CSS from /assets/style.css (repo root).
    """
    st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

    # Resolve repo root robustly (utils/ is one level below root)
    root = Path(__file__).resolve().parents[1]
    css_path = root / "assets" / "style.css"

    css = _read_css(css_path)
    if not css:
        # Non-fatal warning (only shown if file missing)
        st.warning(f"⚠️ style.css not found at: {css_path.as_posix()}")
        return

    inject_css(css)

# -------------------------------
# UI components
# -------------------------------
def render_hero(*, title: str, subtitle: str) -> None:
    """Hero block used across pages. Accepts title/subtitle exactly as your landing page calls it."""
    st.markdown(
    f"""
    <div style='padding: 28px 30px 14px 30px;'>
    <h1 style='color:#86ffcf; text-shadow:0 0 10px #39ff9f; margin-bottom:6px;'>
    {title}
    </h1>
    <p style='font-size:18px; color:#b3ffdd; margin-top:0;'>
    {subtitle}
    </p>
    </div>
        """,
        unsafe_allow_html=True,
    )

def safe_switch_page(page_path: str) -> None:
    """Switch pages with a friendly error if the target can't be opened."""
    try:
        st.switch_page(page_path)
    except Exception as e:
        st.error("Navigation failed: page not found or renamed.")
        st.caption(f"Expected file: {page_path}")
        st.caption(f"Details: {e}")
