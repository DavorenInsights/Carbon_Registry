import streamlit as st
from utils.ui import (
    setup_page, render_hero, sidebar_nav, NAV_ITEMS,
    safe_switch_page, APP_TITLE, APP_ICON, APP_VERSION, APP_TAGLINE
)

setup_page(page_title=APP_TITLE, page_icon=APP_ICON, layout="wide")
sidebar_nav()

render_hero(
    title="🌍 Carbon Registry & Methods Explorer",
    subtitle=(
        "A transparent workspace for <b>boundaries</b>, <b>assumptions</b>, activity logs, and calculator demos."
        f"<br/><span style='opacity:0.85;'>Version: {APP_VERSION}</span>"
    ),
    tagline=APP_TAGLINE,
)

# QUICK ACTIONS
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
            "- UI utilities stabilized\n"
            "- CSS path fixed for multipage\n"
            "- Theme consistent across pages"
        )

st.write("")

# NAV CARDS
cols = st.columns(3)
for idx, item in enumerate(NAV_ITEMS[1:4]):  # show the 3 core cards
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
