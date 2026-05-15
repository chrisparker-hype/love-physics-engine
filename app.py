import streamlit as st

# App styling and title
st.set_page_config(page_title="Love Physics Engine", page_icon="⚛️", layout="centered")

st.title("⚛️ The Love Physics Engine v3.0")
st.write("---")

# Navigation Sidebar
phase = st.sidebar.radio(
    "Select Engine Module:",
    ["Phase 1: Quantum Crush Evaluator", "Phase 2: Entropy & Red Flag Filter", "Phase 3: Trajectory Simulator"]
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
    past_energy = st.slider("Past Energy Output (1 = Ice cold, 10 = Supernova)", 1, 10, 5, key="past")
    current_energy = st.slider("Current Energy Output (1 = Ice cold, 10 = Supernova)", 1, 10, 5, key="current")
    
    st.header("2. Critical Thermal Leaks (Red Flags)")
    rf_hot_cold = st.checkbox("Hot and Cold Cycles (They act obsessed one day, ghost the next)")
    rf_deflection = st.checkbox("Accountability Deflection (Never apologizes, warps reality when challenged)")
    rf_hidden = st.checkbox("Hidden Parameters (Keeps their phone heavily guarded / hides you from their life)")
    rf_one_way = st.checkbox("One-Way Mirror (Expects you to be an open book but stays completely mysterious)")

    if st.button("RUN THERMODYNAMIC FILTER"):
        st.write("---")
        st.header("📊 Thermodynamic Report")
        energy_delta = current_energy - past_energy
        red_flags_tripped = sum([rf_hot_cold, rf_deflection, rf_hidden, rf_one_way])
        
        if energy_delta < 0:
            st.error(f"📉 THERMAL DECAY DETECTED: System energy has dropped by {abs(energy_delta)} units.")
        elif energy_delta > 0:
            st.success(f"📈 ENERGY INJECTION: System energy increased by {energy_delta} units.")
        else:
            st.info("⚖️ THERMAL EQUILIBRIUM: Energy levels are perfectly stable.")
            
        st.write("---")
        st.subheader("⚠️ Structural Integrity Scan")
        if red_flags_tripped == 0:
            st.success("🛡️ No critical anomalies detected. System containment is secure.")
        elif 1 <= red_flags_tripped <= 2:
            st.warning(f"⚠️ Warning: {red_flags_tripped} critical thermal leaks detected.")
        else:
            st.error(f"🚨 CRITICAL SYSTEM FAILURE: {red_flags_tripped} red flags active. Total structural meltdown imminent.")

# ==========================================
# PHASE 3 CODE (NEW!)
# ==========================================
elif phase == "Phase 3: Trajectory Simulator":
    st.subheader("Phase 3: Trajectory & Velocity Simulator")
    st.write("Project the flight path of this relationship over the next 6 months based on mathematical alignment.")
    
    st.header("1. Velocity of Vulnerability")
    st.write("How fast are personal details, deep thoughts, and past history being shared?")
    your_v = st.slider("Your Vulnerability Speed (1 = Vault Knox, 10 = Light Speed sharing)", 1, 10, 5)
    their_v = st.slider("Their Vulnerability Speed (1 = Vault Knox, 10 = Light Speed sharing)", 1, 10, 5)
    
    st.header("2. Core Values Alignment (Mass Agreement)")
    st.write("Do your core life trajectories match up? (Long term goals, morals, lifestyle choices)")
    alignment = st.slider("Alignment Score (0% = Total Opposites, 100% = Perfect Sync)", 0, 100, 50)
    
    if st.button("RUN SIMULATION MODELLING"):
        st.write("---")
        st.header("🔮 6-Month Projected Orbit")
        
        v_differential = your_v - their_v
        
        # Scenario Logic based on physics principles
        if alignment < 40:
            st.error("💥 TRUNCATED TRAJECTORY: Massive vector mismatch. Regardless of emotional speed, your core paths diverge. A structural collision or break is statistically probable within 90 days.")
        elif v_differential >= 4:
            st.warning("🧗 ESCAPE VELOCITY FAILURE: You are sharing data at a much higher velocity than them. You risk over-exerting your engine while they remain static. Result: Emotional burnout.")
        elif v_differential <= -4:
            st.warning("🛰️ FREEZING ORBIT: They are opening up, but your parameters are locked down tightly. They may conclude your system is unresponsive and alter their course away from you.")
        elif 40 <= alignment < 75:
            st.info("🔄 ALTERNATING ORBIT: Stable for now, but requires massive corrective thrusters. You have decent alignment, but check back frequently to monitor adjustments.")
        else:
            st.success("🚀 DEEP SPACE HORIZON: Smooth acceleration. Velocities match up perfectly ($v \\approx v$) and core alignment is optimal. High probability of long-term mission success.")

st.write("---")
st.caption("Numbers never lie. Protect your system parameters.")
