import streamlit as st
import math

st.set_page_config(page_title="Love Physics Engine", page_icon="⚛️", layout="centered")

st.title("⚛️ The Love Physics Engine v5.0")
st.write("---")

phase = st.sidebar.radio(
    "Select Engine Module:",
    [
        "Phase 1: Mechanical Force Calculator", 
        "Phase 2: Entropy & Red Flag Filter", 
        "Phase 3: Trajectory Simulator",
        "Phase 4: Quantum Wavefunction Collapse"
    ]
)

# ==========================================
# PHASE 1: MECHANICAL PHYSICS
# ==========================================
if phase == "Phase 1: Mechanical Force Calculator":
    st.subheader("Phase 1: Classical Mechanics & Kinematics")
    st.write("Calculate the actual **Mechanical Force (F)** someone is exerting toward you using Newton's Second Law.")
    
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
    
    delta_t = st.number_input(
        "Response Latency (Δt) - How many HOURS did it take them to execute this action/reply?",
        min_value=0.1, max_value=48.0, value=1.0, step=0.1
    )
    
    mass_map = {
        "Low Mass (1 kg): Sent a lazy, dry text response ('lol', 'cool', 'ok')": 1.0,
        "Medium Mass (5 kg): Initiated a genuine conversation or shared a meme/link": 5.0,
        "High Mass (10 kg): Called you out of the blue or set up a concrete plan to hang out": 10.0,
        "Super Massive (25 kg): Showed up for you when you needed help, or brought a thoughtful gift": 25.0
    }
    m = mass_map[mass_choice]
    
    if st.button("EXECUTE KINEMATIC CALCULATION"):
        st.write("---")
        st.header("⚙️ Mathematical Computation")
        a = 1.0 / delta_t
        F = m * a
        st.latex(r"a = \frac{1}{\Delta t} = \frac{1}{" + f"{delta_t}" + r"} = " + f"{a:.3f}" + r" \text{ m/s}^2")
        st.latex(r"F = m \cdot a = " + f"{m}" + r" \cdot " + f"{a:.3f}" + r" = " + f"{F:.3f}" + r" \text{ Newtons}")
        
        st.subheader("📊 Engine Output Verdict")
        st.metric(label="Calculated Attraction Force (F)", value=f"{F:.3f} N")
        
        if F >= 5.0: st.success("🟢 STRONG MOMENTUM: Safe to maintain orbit.")
        elif 1.0 <= F < 5.0: st.warning("🟡 WEAK KINETIC ENERGY: Minimal force. Do not advance.")
        else: st.error("🔴 INERTIA LOCK: Force approaches 0 Newtons. Abort.")

# ==========================================
# PHASE 2 & 3 CODE
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
        if energy_delta < 0: st.error(f"📉 THERMAL DECAY: Drop of {abs(energy_delta)} units.")
        else: st.success("⚖️ System stable or gaining heat.")
        if red_flags_tripped >= 3: st.error("🚨🚨 CRITICAL FAILURE: Melt down imminent.")
        else: st.success("🛡️ Structural integrity within margin.")

elif phase == "Phase 3: Trajectory Simulator":
    st.subheader("Phase 3: Trajectory & Velocity Simulator")
    your_v = st.slider("Your Vulnerability Speed", 1, 10, 5)
    their_v = st.slider("Their Vulnerability Speed", 1, 10, 5)
    alignment = st.slider("Alignment Score", 0, 100, 50)
    if st.button("RUN SIMULATION MODELLING"):
        if alignment < 40: st.error("💥 TRUNCATED TRAJECTORY: Collision predicted.")
        elif abs(your_v - their_v) >= 4: st.warning("🧗 VELOCITY MISMATCH: Burnout risk.")
        else: st.success("🚀 DEEP SPACE HORIZON: Target locked.")

# ==========================================
# NEW!! PHASE 4: QUANTUM WAVEFUNCTION COLLAPSE
# ==========================================
elif phase == "Phase 4: Quantum Wavefunction Collapse":
    st.subheader("Phase 4: Schrödinger's Crush Equation")
    st.write("Before you observe the system (confess), the crush exists in a superposition of states.")
    st.latex(r"|\Psi\rangle = c_1|\text{Love}\rangle + c_2|\text{No Love}\rangle")
    st.write("Let's calculate the probability amplitude ($|c_1|^2$) to predict the final state post-collapse.")
    
    st.header("1. Quantum Parameters")
    
    entanglement = st.slider(
        "Quantum Entanglement (χ): How strongly do their moods/actions sync with yours natively?",
        min_value=1, max_value=10, value=5,
        help="1 = Completely independent particles, 10 = Perfect synchronous reactions"
    )
    
    interference = st.radio(
        "Wave Interference Pattern:",
        options=[
            "Constructive (Being around them multiplies your energy and makes things easy)",
            "Destructive (Interactions feel draining, heavy, or filled with friction/anxiety)"
        ]
    )
    
    barrier = st.slider(
        "Potential Barrier (V₀): How many obstacles exist? (e.g., they work together, distance, exes around)",
        min_value=1, max_value=10, value=3
    )
    
    if st.button("COLLAPSE THE WAVEFUNCTION (SIMULATION)"):
        st.write("---")
        st.header("🔬 Quantum Probability Mechanics")
        
        # Base calculation for c1 amplitude
        interference_factor = 25 if "Constructive" in interference else -20
        
        # Quantum formula representation
        # Higher entanglement increases probability; higher barrier decreases probability via quantum tunneling simulation
        raw_probability = (entanglement * 7.5) + interference_factor - (barrier * 2.5)
        
        # Bound probability between 1% and 99% (Quantum uncertainty dictates it can never be 100% or 0% before observation)
        prob_c1 = max(1.0, min(99.0, raw_probability))
        prob_c2 = 100.0 - prob_c1
        
        # Display probability amplitudes using LaTeX
        st.latex(r"|c_1|^2 \text{ (Probability of Love)} = " + f"{prob_c1:.1f}\\%")
        st.latex(r"|c_2|^2 \text{ (Probability of No Love)} = " + f"{prob_c2:.1f}\\%")
        
        st.subheader("🔮 Post-Observation Forecast")
        if prob_c1 >= 70:
            st.success(f"🐈 THE CAT IS ALIVE: High probability amplitude ($|c_1|^2 = {prob_c1:.1f}\\%$). The system behavior suggests quantum alignment. Observation/Confession has a statistically high green-light success rate.")
        elif 40 <= prob_c1 < 70:
            st.warning(f"🌀 COHERENCE HAZARD: Probability is split evenly. The cat is strictly in superposition. If you observe right now, the wavefunction collapse is completely unpredictable. Maintain isolation and gather more data.")
        else:
            st.error(f"💀 THE CAT IS DEAD: Probability amplitude favors a ground state ($|c_2|^2 = {prob_c2:.1f}\\%$). Attempting to force a collapse (confessing) right now will highly likely resolve into a firm 'No Love' state. Protect your system parameters and abort.")

st.write("---")
st.caption("Numbers never lie. Protect your system parameters.")
