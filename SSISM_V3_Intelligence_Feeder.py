import streamlit as st
import pandas as pd
from typing import List, Dict, Any # Added Any for the return type of process_submission

# --- CONFIGURATION ---
PROJECT_NAME = "SSISM V3 Intelligence Feeder"
APP_VERSION = "1.0"
MANDATE = "Secure input for the Ghost Node Repository."

# NOTE: In a real environment, this data would be securely sent to 
# a protected database/API endpoint for vector generation and analysis.

# --- FUNCTIONAL LOGIC ---

def process_submission(entity_name: str, primary_aliases: str, known_allies: str, theme: str, sample_posts: List[str]) -> Dict[str, Any]:
    """
    Simulates the processing of intelligence data into the Ghost Node format.
    
    This function extracts the core data needed to generate the F_L and F_I vectors.
    """
    
    # 1. Alias & Ally Processing (for F_I Vector generation)
    alias_list = [a.strip() for a in primary_aliases.split(',') if a.strip()]
    ally_list = [a.strip() for a in known_allies.split(',') if a.strip()]
    
    # 2. Linguistic Feature Sample (for F_L Vector generation)
    # NOTE: The actual vector calculation (TF-IDF, NLP) occurs in the protected backend.
    
    submission_data = {
        "Entity_ID_Concept": f"GN-{entity_name.replace(' ', '_').upper()}-{len(alias_list)}",
        "Primary_Known_Aliases": alias_list,
        "Known_Allied_Accounts": ally_list,
        "PsyWar_Theme": theme,
        "Sample_Post_Count": len([p for p in sample_posts if p]), # Count non-empty posts
        "Submitted_Timestamp": pd.Timestamp.now().isoformat(),
        "Status": "PENDING VECTOR GENERATION"
    }
    
    # Optionally include the raw posts for visibility (for debugging/review)
    submission_data["Raw_Sample_Posts"] = [p for p in sample_posts if p] 
    
    return submission_data

# --- STREAMLIT UI ---

st.set_page_config(page_title=PROJECT_NAME, layout="centered")

st.title(f"🛡️ {PROJECT_NAME}")
st.header("Ghost Node Repository Input (V3 TCE)")

st.markdown("""
This interface is for authorized partners (NGOs, Journalists) to securely input parameters
for a new **Ghost Node**—an adaptive entity suspected of coordinating **Psy War** campaigns.
The system will use this data to generate the entity's unique network ($\mathbf{F_I}$) and linguistic ($\mathbf{F_L}$) vectors.
""")

st.markdown("---")

# 1. Entity Naming & Identification
with st.form(key='ghost_node_form'):
    st.subheader("1. Target Entity Identification")
    
    entity_name = st.text_input(
        "Conceptual Entity Name (e.g., Kyaw Swar Persona)", 
        placeholder="The name used to track this entity internally"
    )
    
    primary_aliases = st.text_area(
        "Known Aliases/Pseudonyms (Comma-separated)",
        placeholder="e.g., Kyaw Swar, တပ်ကြပ်ကြီးဖိုးစီ, Alias_X_2025"
    )
    
    # 2. Interaction Vector Input (Crucial for F_I)
    st.subheader("2. Network & Context Clues")
    st.markdown("_The Interaction Vector ($\mathbf{F_I}$) is generated from these allied accounts to map the Ghost Node's local network cluster._")
    
    known_allies = st.text_area(
        "Known Allied Accounts/Cluster Members (Comma-separated)",
        placeholder="Enter 5-10 accounts the target consistently interacts with. (Crucial for F_I Vector)"
    )
    
    # 3. Linguistic Vector Input (Crucial for F_L)
    st.subheader("3. Content Sample")
    st.markdown("_The Linguistic Vector ($\mathbf{F_L}$) is generated from the content and theme._")
    
    theme = st.text_input(
        "Primary Psy War Theme/Topic",
        placeholder="e.g., Ethnic Divisiveness, Anti-Civil Society Narrative"
    )
    
    sample_post1 = st.text_area("Sample Post 1 (Burmese or English)", height=70)
    sample_post2 = st.text_area("Sample Post 2 (Burmese or English)", height=70)
    
    # Submission
    submit_button = st.form_submit_button(label='Submit Ghost Node Intelligence')

if submit_button:
    # Collect all sample posts, filtering out empty strings
    sample_posts = [sample_post1, sample_post2]
    
    if not entity_name or not primary_aliases or not known_allies:
        st.error("⚠️ Please fill out the **Entity Name**, **Aliases**, and **Allied Accounts** fields. These are essential for vector generation.")
    else:
        result = process_submission(entity_name, primary_aliases, known_allies, theme, sample_posts)
        
        st.success(f"✅ Intelligence successfully packaged for **{entity_name}**!")
        
        with st.expander("Review Submitted Data (Backend Package)"):
            st.markdown("**Data Submitted for Vector Generation (Backend):**")
            st.json(result)
        
        st.info("💡 The SSISM V3 TCE is now generating the Interaction ($\mathbf{F_I}$) and Linguistic ($\mathbf{F_L}$) vectors for this new Ghost Node. Thank you for fortifying the commons.")

st.markdown(f"--- \n *{MANDATE} | V{APP_VERSION}*")
