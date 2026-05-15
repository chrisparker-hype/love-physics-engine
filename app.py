import streamlit as st

# App styling and title
st.set_page_config(page_title="Love Physics Engine", page_icon="⚛️", layout="centered")

st.title("⚛️ The Love Physics Engine v2.0")
st.write("---")

# Navigation Sidebar
phase = st.sidebar.radio(
    "Select Engine Module:",
    ["Phase 1: Quantum Crush Evaluator", "Phase 2: Entropy & Red Flag Filter"]
)

# ==========================================
# PHASE 1 CODE
# ==========================================
if phase == "Phase 1: Quantum Crush Evaluator":
    st.subheader("Phase 1: The Quantum Crush Evaluator")
    st.write("Calculate the state of the *Relational Superposition* before you risk a collapse (confession).")
    
    st.header("1. Mechanical Forces (Action Data)")
    initiation = st.slider(
        "Initiation Vector: Out of the last 10 interactions, how many did THEY start?",
        min_value=0, max_value=10, value=5
    )
    
    latency = st.selectbox(
        "Response Latency (Δt): What is their typical text reply time?",
        options=["Instantly to < 15 mins", "15 mins to 2 hours", "2 to 6 hours", "6+ hours / Next day"]
    )
    
    st.header("2. Theoretical Constants")
    object_permanence = st.radio(
        "Object Permanence: Do they remember 'low-mass' details you mentioned days ago?",
        options=["Yes, perfectly", "Sometimes", "Rarely/Never"]
    )
    
    latency_scores = {"Instantly to < 15 mins": 10, "15 mins to 2 hours": 7, "2 to 6 hours": 4, "6+ hours / Next day": 1}
    op_scores = {"Yes, perfectly": 10, "Sometimes": 5, "Rarely/Never": 0}
    
    if st.button("RUN ENGINE ANALYSIS"):
        score = (initiation * 1.0) + latency_scores[latency] + op_scores[object_permanence]
        probability = (score / 30.0) * 100
        
        st.write("---")
        st.header("📊 System Analysis Results")
        st.metric(label="Probability of Love State (Ψ)", value=f"{probability:.1f}%")
        
        if probability >= 75:
            st.success("🟢 STABLE ORBIT: The data shows strong mutual gravity. The wavefunction is stable enough for observation (confession).")
        elif 40 <= probability < 75:
            st.warning("🟡 UNCERTAINTY PRINCIPLE ACTIVE: High superposition/mixed signals. Keep gathering data outside the Event Horizon. Do NOT collapse the wavefunction yet.")
        else:
            st.error("🔴 BLACK HOLE DETECTED: Massively asymmetrical energy output. If you cross this Event Horizon, you risk a total energy drain. Abort system integration.")

# ==========================================
# PHASE 2 CODE
# ==========================================
elif phase == "Phase 2: Entropy & Red Flag Filter":
    st.subheader("Phase 2: Entropy & Red Flag Filter")
    st.write("Detect if the system is losing thermal energy (cooling down) or leaking power through structural flaws (red flags).")
    
    st.header("1. The Entropy Coefficient (Trending Energy)")
    st.write("Compare their communication levels *last month* vs. *this week*.")
    
    past_energy = st.slider("Past Energy Output (1 = Ice cold, 10 = Supernova)", 1, 10, 5, key="past")
    current_energy = st.slider("Current Energy Output (1 = Ice cold, 10 = Supernova)", 1, 10, 5, key="current")
    
    st.header("2. Critical Thermal Leaks (Red Flags)")
    st.write("Check any anomalies detected in the system behavior:")
    
    rf_hot_cold = st.checkbox("Hot and Cold Cycles (They act obsessed one day, ghost the next)")
    rf_deflection = st.checkbox("Accountability Deflection (Never apologizes, warps reality when challenged)")
    rf_hidden = st.checkbox("Hidden Parameters (Keeps their phone heavily guarded / hides you from their life)")
    rf_one_way = st.checkbox("One-Way Mirror (Expects you to be an open book but stays completely mysterious)")

    if st.button("RUN THERMODYNAMIC FILTER"):
        st.write("---")
        st.header("📊 Thermodynamic Report")
        
        # Calculate Entropy
        energy_delta = current_energy - past_energy
        
        # Count total red flags
        red_flags_tripped = sum([rf_hot_cold, rf_deflection, rf_hidden, rf_one_way])
        
        # Output Entropy Status
        if energy_delta < 0:
            st.error(f"📉 THERMAL DECAY DETECTED: System energy has dropped by {abs(energy_delta)} units. The relationship is succumbing to negative entropy.")
        elif energy_delta > 0:
            st.success(f"📈 ENERGY INJECTION: System energy increased by {energy_delta} units. The orbit is warming up.")
        else:
            st.info("⚖️ THERMAL EQUILIBRIUM: Energy levels are perfectly stable.")
            
        # Output Red Flag Status
        st.write("---")
        st.subheader("⚠️ Structural Integrity Scan")
        if red_flags_tripped == 0:
            st.success("🛡️ No critical anomalies detected. System containment is secure.")
        elif 1 <= red_flags_tripped <= 2:
            st.warning(f"⚠️ Warning: {red_flags_tripped} critical thermal leaks detected. Monitor system stability closely.")
        else:
            st.error(f"🚨 CRITICAL SYSTEM FAILURE: {red_flags_tripped} red flags active. Total structural meltdown imminent. EJECT SYSTEM IMMEDIATELY.")

st.write("---")
st.caption("Numbers never lie. Protect your system parameters.")
