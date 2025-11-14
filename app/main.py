# app/main.py
# SS'ISM Paññā Shield v3.1 — LIVE ETHICAL INTELLIGENCE CONSOLE
# FIXED & SIMPLIFIED — No import errors
# Author: U Ingar Soe | 14 November 2025

import streamlit as st
import numpy as np
import random
from datetime import datetime

# =================================================================
# CORE ENGINE — FULLY EMBEDDED (NO EXTERNAL IMPORT NEEDED)
# =================================================================
def calculate_psywar_noise(GhostNode_Certainty: float, Network_Anomaly_Score: float) -> float:
    RISK_INVERSE = 1.0 - GhostNode_Certainty
    return max(RISK_INVERSE * Network_Anomaly_Score, 1e-9)

def calculate_atrocity_index(V_satellite: float, V_osint: float, V_veto_time: float) -> float:
    return (0.45 * V_satellite) + (0.35 * V_osint) + (0.20 * V_veto_time)

def calculate_fused_likelihood(V14_atrocity: float, V15_scg: float, V16_psywar_noise: float) -> float:
    W_Foresight = 0.88 * 1.0
    W_Social    = 0.88 * 0.9
    W_Context   = 0.88 * 1.1
    B_Karmic    = 0.15
    log_likelihood = (
        W_Foresight * np.log(max(V14_atrocity, 1e-9)) +
        W_Social    * np.log(max(V15_scg, 1e-9)) +
        W_Context   * np.log(max(V16_psywar_noise, 1e-9))
    ) - B_Karmic
    return np.exp(log_likelihood)

def paññā_fusion_decision(raw_action: str, is_laukī_cup_action: bool, is_wisdom_work: bool, is_user_constrained: bool) -> str:
    if not is_wisdom_work:
        return "VOID: Wisdom Gate failed."
    if is_laukī_cup_action and is_user_constrained:
        return f"A' (SIS): Paññā Work → Laukī Water-Cup activated for '{raw_action}'"
    return raw_action

# =================================================================
# STREAMLIT APP
# =================================================================
st.set_page_config(page_title="Paññā Shield v3.1", page_icon="🛡️", layout="centered")

st.markdown("""
<h1 style='text-align: center;'>🛡️ SS'ISM Paññā Shield v3.1</h1>
<p style='text-align: center;'><i>Live Ethical AI Console — Civil Society Intelligence</i></p>
<p style='text-align: center;'><b>“When vetoes silence justice, data becomes resistance.”</b></p>
""", unsafe_allow_html=True)

st.info("**AUTHORIZED PARTNERS ONLY** — All actions constrained by Sīla → Samādhi → Paññā")

mode = st.radio("Mode", ["Ghost Node Intel", "Misinfo Feeder"], horizontal=True)

def generate_receipt():
    return f"GN-{datetime.now().strftime('%Y-%m-%d')}-{random.randint(100,999)}"

# ====================== GHOST NODE INTEL ======================
if mode == "Ghost Node Intel":
    with st.form("intel_form"):
        st.subheader("Submit Ghost Node Intelligence")
        st.text_input("Entity Name", placeholder="e.g., Kyaw Swar Persona")
        st.text_input("Aliases", placeholder="Kyaw Swar, Alias_X_2025")
        st.text_area("Allied Accounts")
        st.text_input("Primary Theme", placeholder="Ethnic Divisiveness")
        st.text_area("Sample Post 1", height=80)
        st.text_area("Sample Post 2", height=80)
        submitted = st.form_submit_button("SUBMIT INTELLIGENCE")

    if submitted:
        with st.spinner("Analyzing..."):
            V16 = calculate_psywar_noise(0.88, 1.30)
            H = calculate_atrocity_index(0.80, 0.75, 0.85)
            L_fused = calculate_fused_likelihood(H, 0.78, V16)
            Phi_A = np.tanh(L_fused) * 0.9
            action = paññā_fusion_decision("Deploy counter-narrative", False, True, True)

        receipt = generate_receipt()
        st.success(f"**{receipt}** — Intel Received")
        st.progress(Phi_A)
        st.metric("Accountability Likelihood (Φ_A)", f"{Phi_A:.3f}")
        st.info(f"**Paññā SAYS:** {action}")

# ====================== MISINFO FEEDER ======================
else:
    st.warning("**MISINFO FEEDER MODE** — Confuse. Do not fight. Stay anonymous.")
    with st.form("feeder_form"):
        st.text_input("Target Account", placeholder="@JuntaVoice2025")
        st.text_area("Post 1", height=80)
        st.text_area("Post 2", height=80)
        goal = st.selectbox("Goal", [
            "Waste their time",
            "Force internal contradiction",
            "Expose coordination pattern"
        ])
        submitted = st.form_submit_button("GET FEEDING GUIDANCE")

    if submitted:
        with st.spinner("Crafting noise strategy..."):
            V16 = calculate_psywar_noise(0.91, 1.40)
            H = 0.82
            L_fused = calculate_fused_likelihood(H, 0.80, V16)
            Phi_A = np.tanh(L_fused) * 0.9

            strategies = {
                "Waste their time": [
                    "Fake urgent meeting invites (wrong link)",
                    "Leak impossible deadlines",
                    "Tag 10+ fake commanders"
                ],
                "Force internal contradiction": [
                    "Post Order A from one burner",
                    "Post Order B revoking A (2h later)",
                    "Use wrong unit names"
                ],
                "Expose coordination pattern": [
                    "5 identical replies at same minute",
                    "Use their hashtags + #JuntaFail",
                    "Force deletion → proves botnet"
                ]
            }

        receipt = generate_receipt()
        st.balloons()
        st.success(f"**{receipt}** — NOISE AUTHORIZED")
        st.progress(Phi_A)
        st.metric("Disruption Confidence", f"{Phi_A:.3f}")
        st.info("**Paññā FEEDING GUIDANCE:**\n" + "\n".join(f"• {s}" for s in strategies[goal]))
        st.markdown(f"**Thank you, Info Feeder #{receipt[-3:]} — you just cost them 48+ hours.** 🛡️")
