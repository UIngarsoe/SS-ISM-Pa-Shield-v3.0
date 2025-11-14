# app/main.py
# SS'ISM Paññā Shield v3.1 — LIVE ETHICAL INTELLIGENCE CONSOLE
# Author: U Ingar Soe | Launch: 14 November 2025
# License: AGPL-3.0 + Ethical Use Clause

import streamlit as st
import numpy as np
import random
from datetime import datetime

# === IMPORT CORE ENGINE FROM REPO ROOT ===
import sys
sys.path.append("..")
from core_demo import (
    calculate_atrocity_index,
    calculate_psywar_noise,
    calculate_fused_likelihood,
    paññā_fusion_decision
)

# === PAGE CONFIG ===
st.set_page_config(
    page_title="Paññā Shield v3.1",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# === HEADER ===
st.markdown("""
<div style='text-align: center;'>
    <h1>🛡️ SS'ISM Paññā Shield v3.1</h1>
    <p><i>Civil Society Intelligence Engine — Live Ethical AI Console</i></p>
    <p><b>“When vetoes silence justice, data becomes resistance.”</b></p>
</div>
""", unsafe_allow_html=True)

st.info("**AUTHORIZED PARTNERS ONLY** — All inputs processed through Sīla → Samādhi → Paññā. No action without wisdom.")

# === MODE SELECTION ===
mode = st.radio(
    "Select Mode",
    ["Ghost Node Intel", "Misinfo Feeder"],
    horizontal=True,
    help="Ghost Node: Report. Misinfo Feeder: Confuse."
)

# === RECEIPT ID GENERATOR ===
def generate_receipt():
    return f"GN-{datetime.now().strftime('%Y-%m-%d')}-{random.randint(100, 999)}"

# ==================================================================
# MODE 1: GHOST NODE INTEL
# ==================================================================
if mode == "Ghost Node Intel":
    st.subheader("Submit Ghost Node Intelligence")
    with st.form("ghost_intel_form"):
        st.markdown("**1. Target Entity**")
        entity = st.text_input("Conceptual Name", placeholder="e.g., Kyaw Swar Persona")
        aliases = st.text_input("Aliases (comma-separated)", placeholder="Kyaw Swar, Alias_X_2025")

        st.markdown("**2. Network Clues**")
        allies = st.text_area("Allied Accounts (5–10)", placeholder="Enter handles this entity interacts with")

        st.markdown("**3. Content Sample**")
        theme = st.text_input("Primary PsyWar Theme", placeholder="Ethnic Divisiveness")
        post1 = st.text_area("Sample Post 1", height=80)
        post2 = st.text_area("Sample Post 2", height=80)

        submitted = st.form_submit_button("SUBMIT GHOST NODE INTELLIGENCE")

    if submitted:
        with st.spinner("Paññā Shield is analyzing..."):
            # Simulate TCE
            GhostNode_Certainty = 0.88
            Network_Anomaly_Score = 1.30
            V16 = calculate_psywar_noise(GhostNode_Certainty, Network_Anomaly_Score)
            H = calculate_atrocity_index(0.80, 0.75, 0.85)
            L_fused = calculate_fused_likelihood(H, 0.78, V16)
            Phi_A = np.tanh(L_fused) * 0.9

            raw_action = "Deploy verified counter-narrative + legal challenge package"
            final_action = paññā_fusion_decision(raw_action, False, True, True)

        receipt = generate_receipt()
        st.success(f"**{receipt}** | INTEL RECEIVED")

        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric("Accountability Likelihood (Φ_A)", f"{Phi_A:.3f}")
            st.progress(min(Phi_A, 1.0))
            if Phi_A > 0.7: st.markdown("**HIGH CONFIDENCE**")
            elif Phi_A > 0.4: st.markdown("**MODERATE**")
            else: st.markdown("**MONITORING**")

        with col2:
            st.info(f"**Paññā SAYS:**\n\n{final_action}")

        with st.expander("Ethical Reasoning Trace"):
            st.write(f"Sīla → H: `{H:.4f}`")
            st.write(f"TCE → V16: `{V16:.4f}`")
            st.write(f"Samādhi → L_fused: `{L_fused:.4f}`")
            st.write(f"Paññā → Φ_A: `{Phi_A:.4f}`")

# ==================================================================
# MODE 2: MISINFO FEEDER
# ==================================================================
else:
    st.subheader("Misinfo Feeder Mode")
    st.warning("**CONFUSE. DO NOT FIGHT.** Feed noise. Break their tempo. Stay anonymous.")

    with st.form("misinfo_form"):
        target_handle = st.text_input("Target Account", placeholder="@JuntaVoice2025")
        post1 = st.text_area("Post 1 (copy-paste)", height=80)
        post2 = st.text_area("Post 2 (copy-paste)", height=80)
        goal = st.selectbox("Goal", [
            "Waste their time",
            "Force internal contradiction",
            "Expose coordination pattern"
        ])
        submit = st.form_submit_button("ANALYZE & GET FEEDING GUIDANCE")

    if submit:
        with st.spinner("Paññā is crafting your noise strategy..."):
            # Simulate high-confidence detection
            GhostNode_Certainty = 0.91
            Network_Anomaly_Score = 1.40
            V16 = calculate_psywar_noise(GhostNode_Certainty, Network_Anomaly_Score)
            H = 0.82
            L_fused = calculate_fused_likelihood(H, 0.80, V16)
            Phi_A = np.tanh(L_fused) * 0.9

            # Noise strategies
            strategies = {
                "Waste their time": [
                    "Send fake 'urgent meeting' invites (wrong Zoom link)",
                    "Leak 'internal memo' with impossible deadlines",
                    "Tag 10+ fake 'commanders' in replies"
                ],
                "Force internal contradiction": [
                    "Post 'Order A' from one burner",
                    "Post 'Order B revokes A' from another (2h later)",
                    "Use same jargon but wrong unit names"
                ],
                "Expose coordination pattern": [
                    "Reply with identical message from 5 burners at same minute",
                    "Use their own hashtags + #JuntaFail",
                    "Force them to delete → proves control"
                ]
            }

        receipt = generate_receipt()
        st.balloons()
        st.success(f"**{receipt}** | NOISE AUTHORIZED")

        st.progress(min(Phi_A, 1.0))
        st.metric("Disruption Confidence (Φ_A)", f"{Phi_A:.3f}")

        st.info(f"**Paññā FEEDING GUIDANCE:**\n" + "\n".join(f"• {s}" for s in strategies[goal]))
        st.caption("You are not fighting. You are *confusing*. That is victory.")

        st.markdown(f"**Thank you, Info Feeder #{receipt.split('-')[-1]}.** You just cost them 48+ hours. 🛡️")
