import streamlit as st
import math

st.set_page_config(page_title="Love Physics Engine", page_icon="⚛️", layout="centered")

st.title("⚛️ The Love Physics Engine v6.1")
st.write("---")

phase = st.sidebar.radio(
    "Select Engine Module:",
    [
        "Phase 1: Mechanical Force Calculator", 
        "Phase 2: Entropy & Red Flag Filter", 
        "Phase 3: Trajectory Simulator",
        "Phase 4: Quantum Wavefunction Collapse",
        "Phase 5: Relativistic Escape Velocity"
    ]
)

# ==========================================
# PHASE 1: MECHANICAL PHYSICS
# ==========================================
if phase == "Phase 1: Mechanical Force Calculator":
    st.subheader("Phase 1: Classical Mechanics & Kinematics")
    st.header("1. Input System Variables")
    mass_choice = st.selectbox(
        "Action Mass (m) - What was their latest major action?",
        options=[
            "Low Mass (1 kg): Sent a lazy, dry text response ('lol', 'cool', 'ok')",
            "Medium Mass (5 kg): Initiated a genuine conversation or shared a meme/link",
            "High Mass (10 kg): Called you out of the blue or set up a concrete plan to hang out",
            "Super Massive (25 kg): Showed up for you when you needed help, or brought a thoughtful gift"
        ]
    )
    delta_t = st.number_input("Response Latency (Δt) - Hours", min_value=0.1, max_value=48.0, value=1.0)
    mass_map = {"Low Mass (1 kg): Sent a lazy, dry text response ('lol', 'cool', 'ok')": 1.0, "Medium Mass (5 kg): Initiated a genuine conversation or shared a meme/link": 5.0, "High Mass (10 kg): Called you out of the blue or set up a concrete plan to hang out": 10.0, "Super Massive (25 kg): Showed up for you when you needed help, or brought a thoughtful gift": 25.0}
    m = mass_map[mass_choice]
    if st.button("EXECUTE KINEMATIC CALCULATION"):
        a = 1.0 / delta_t
        F = m * a
        st.latex(r"F = m \cdot a = " + f"{m}" + r" \cdot " + f"{a:.3f}" + r" = " + f"{F:.3f} N")
        if F >= 5.0: st.success("🟢 STRONG MOMENTUM")
        elif 1.0 <= F < 5.0: st.warning("🟡 WEAK KINETIC ENERGY")
        else: st.error("🔴 INERTIA LOCK")

# ==========================================
# PHASE 2 & 3
# ==========================================
elif phase == "Phase 2: Entropy & Red Flag Filter":
    st.subheader("Phase 2: Entropy & Red Flag Filter")
    past_energy = st.slider("Past Energy Output", 1, 10, 5)
    current_energy = st.slider("Current Energy Output", 1, 10, 5)
    rf_hot_cold = st.checkbox("Hot and Cold Cycles")
    rf_deflection = st.checkbox("Accountability Deflection")
    rf_hidden = st.checkbox("Hidden Parameters")
    rf_one_way = st.checkbox("One-Way Mirror")
    if st.button("RUN THERMODYNAMIC FILTER"):
        energy_delta = current_energy - past_energy
        red_flags_tripped = sum([rf_hot_cold, rf_deflection, rf_hidden, rf_one_way])
        if energy_delta < 0: st.error("📉 THERMAL DECAY")
        else: st.success("⚖️ System stable.")
        if red_flags_tripped >= 3: st.error("🚨🚨 CRITICAL FAILURE")

elif phase == "Phase 3: Trajectory Simulator":
    st.subheader("Phase 3: Trajectory & Velocity Simulator")
    your_v = st.slider("Your Vulnerability Speed", 1, 10, 5)
    their_v = st.slider("Their Vulnerability Speed", 1, 10, 5)
    alignment = st.slider("Alignment Score", 0, 100, 50)
    if st.button("RUN SIMULATION MODELLING"):
        if alignment < 40: st.error("💥 TRUNCATED TRAJECTORY")
        else: st.success("🚀 DEEP SPACE HORIZON")

# ==========================================
# PHASE 4: QUANTUM
# ==========================================
elif phase == "Phase 4: Quantum Wavefunction Collapse":
    st.subheader("Phase 4: Schrödinger's Crush Equation")
    entanglement = st.slider("Quantum Entanglement (χ)", 1, 10, 5)
    interference = st.radio("Wave Interference Pattern:", ["Constructive", "Destructive"])
    barrier = st.slider("Potential Barrier (V₀)", 1, 10, 3)
    if st.button("COLLAPSE THE WAVEFUNCTION"):
        int_f = 25 if interference == "Constructive" else -20
        prob_c1 = max(1.0, min(99.0, (entanglement * 7.5) + int_f - (barrier * 2.5)))
        st.latex(r"|c_1|^2 = " + f"{prob_c1:.1f}\\%")
        if prob_c1 >= 70: st.success("🐈 THE CAT IS ALIVE")
        else: st.error("💀 THE CAT IS DEAD")

# ==========================================
# FIXED PHASE 5: ESCAPE VELOCITY
# ==========================================
elif phase == "Phase 5: Relativistic Escape Velocity":
    st.subheader("Phase 5: Gravitational Breakaway Simulation")
    st.latex(r"v_e = \sqrt{\frac{2GM}{r}}")
    
    # Inputs
    att_g = st.slider("Your Attachment Constant (G)", 1, 10, 5)
    m_mass = st.slider("Target's Mental Mass (M)", 1, 10, 5)
    prox_r = st.slider("Current Proximity Radius (r)", 1, 10, 5)
    
    if st.button("CALCULATE ESCAPE TRAJECTORY"):
        st.write("---")
        # The Math
        ve_sq = (2.0 * att_g * m_mass) / prox_r
        ve_val = math.sqrt(ve_sq)
        
        # FIXED LATEX LINE (The source of your error)
        st.latex(r"v_e = \sqrt{\frac{2 \cdot " + str(att_g) + r" \cdot " + str(m_mass) + r"}{" + str(prox_r) + r"}}")
        st.metric(label="Required Escape Velocity", value=f"{ve_val:.2f} Mach")
        
        if ve_val > 5.0:
            st.error("🚨 EXTREME GRAVITATIONAL PULL: Escape Velocity high. Cut all comms immediately.")
        elif 2.5 <= ve_val <= 5.0:
            st.warning("⚠️ STRONG ORBITAL TETHER: High effort required to detach.")
        else:
            st.success("🌌 LOW GRAVITY WELL: Easy detachment possible.")

st.write("---")
st.caption("Numbers never lie. Structural integrity restored.")
