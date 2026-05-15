import streamlit as st
import math

st.set_page_config(page_title="Love Physics Engine", page_icon="⚛️", layout="centered")

st.title("⚛️ The Love Physics Engine v6.0")
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
# PHASE 4: QUANTUM MECHANICS
# ==========================================
elif phase == "Phase 4: Quantum Wavefunction Collapse":
    st.subheader("Phase 4: Schrödinger's Crush Equation")
    st.write("Before you observe the system (confess), the crush exists in a superposition of states.")
    st.latex(r"|\Psi\rangle = c_1|\text{Love}\rangle + c_2|\text{No Love}\rangle")
    
    st.header("1. Quantum Parameters")
    entanglement = st.slider("Quantum Entanglement (χ): Native mood/action sync?", 1, 10, 5)
    interference = st.radio("Wave Interference Pattern:", ["Constructive (Multiplies your energy)", "Destructive (Drains your energy/causes friction)"])
    barrier = st.slider("Potential Barrier (V₀): System obstacles?", 1, 10, 3)
    
    if st.button("COLLAPSE THE WAVEFUNCTION (SIMULATION)"):
        st.write("---")
        st.header("🔬 Quantum Probability Mechanics")
        interference_factor = 25 if "Constructive" in interference else -20
        raw_probability = (entanglement * 7.5) + interference_factor - (barrier * 2.5)
        prob_c1 = max(1.0, min(99.0, raw_probability))
        prob_c2 = 100.0 - prob_c1
        
        st.latex(r"|c_1|^2 \text{ (Probability of Love)} = " + f"{prob_c1:.1f}\\%")
        st.latex(r"|c_2|^2 \text{ (Probability of No Love)} = " + f"{prob_c2:.1f}\\%")
        
        if prob_c1 >= 70: st.success("🐈 THE CAT IS ALIVE: Statistical green light for observation.")
        elif 40 <= prob_c1 < 70: st.warning("🌀 COHERENCE HAZARD: Unpredictable superposition. Maintain isolation.")
        else: st.error("💀 THE CAT IS DEAD: High probability of a 'No Love' ground state. Abort.")

# ==========================================
# NEW!! PHASE 5: ASTROPHYSICS & ESCAPE VELOCITY
# ==========================================
elif phase == "Phase 5: Relativistic Escape Velocity":
    st.subheader("Phase 5: Gravitational Breakaway Simulation")
    st.write("If a relationship turns toxic or draining, how much emotional 'velocity' do you need to break free before crossing the Event Horizon?")
    st.latex(r"v_e = \sqrt{\frac{2GM}{r}}")
    
    st.header("1. Gravitational Parameters")
    
    attachment_g = st.slider(
        "Your Attachment Constant (G): How quickly/deeply do you normally catch feelings?",
        min_value=1, max_value=10, value=5,
        help="1 = Cold space debris, 10 = High-density gravity well"
    )
    
    mental_mass = st.slider(
        "Target's Mental Mass (M): How much headspace do they occupy? (Thinking about them, checking phone)",
        min_value=1, max_value=10, value=5,
        help="1 = Micro-asteroid, 10 = Supermassive Black Hole"
    )
    
    proximity_r = st.slider(
        "Current Proximity Radius (r): How close are you physically/socially right now?",
        min_value=1, max_value=10, value=5,
        help="1 = Deeply integrated (texting daily, seeing each other), 10 = High orbit (rarely talk)"
    )
    
    if st.button("CALCULATE ESCAPE TRAJECTORY"):
        st.write("---")
        st.header("🚀 Orbital Mechanics Diagnostics")
        
        # Avoid division by zero by ensuring r is never absolute zero
        r_calc = proximity_r * 1.0
        
        # Custom simulation formula for escape velocity mapping
        v_e_squared = (2.0 * attachment_g * mental_mass) / r_calc
        v_e = math.sqrt(v_e_squared)
        
        st.latex(r"v_e = \sqrt{\frac{2 \cdot " + f"{attachment_g}" + r" \cdot " + f"{mental_mass}" + r"}{" + f"{proximity_r}" + r"}} = " + f"{v_e:.2f} \text{ Mach}")
        
        st.subheader("📋 Flight Plan Verdict")
        if v_e > 5.0:
            st.error(f"🚨 EXTREME GRAVITATIONAL PULL: Escape velocity is exceptionally high ({v_e:.2f} Mach). You are danger-close to the Event Horizon. To break free, you must cut all communication entirely (Radio Silence Thrusters) immediately. Incremental pulling back will fail.")
        elif 2.5 <= v_e <= 5.0:
            st.warning(f"⚠️ STRONG ORBITAL TETHER: Escape velocity is moderate ({v_e:.2f} Mach). Breaking free will require conscious, sustained effort. Mute notifications and re-allocate your energy to external systems.")
        else:
            st.success(f"🌌 LOW GRAVITY WELL: Escape velocity is negligible ({v_e:.2f} Mach). This object has very little hold over your system parameters. You can detach cleanly with minimal energy expenditure.")

st.write("---")
st.caption("Numbers never lie. Protect your system parameters.")
