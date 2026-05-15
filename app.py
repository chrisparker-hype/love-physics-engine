import streamlit as st

st.set_page_config(page_title="Love Physics Engine", page_icon="⚛️", layout="centered")

st.title("⚛️ The Love Physics Engine v4.0")
st.write("---")

phase = st.sidebar.radio(
    "Select Engine Module:",
    ["Phase 1: Mechanical Force Calculator", "Phase 2: Entropy & Red Flag Filter", "Phase 3: Trajectory Simulator"]
)

# ==========================================
# REVISED PHASE 1: MECHANICAL PHYSICS
# ==========================================
if phase == "Phase 1: Mechanical Force Calculator":
    st.subheader("Phase 1: Classical Mechanics & Kinematics")
    st.write("Calculate the actual **Mechanical Force (F)** someone is exerting toward you using Newton's Second Law.")
    
    st.header("1. Input System Variables")
    
    # Mass = Emotional Weight of Action
    mass_choice = st.selectbox(
        "Action Mass (m) - What was their latest major action?",
        options=[
            "Low Mass (1 kg): Sent a lazy, dry text response ('lol', 'cool', 'ok')",
            "Medium Mass (5 kg): Initiated a genuine conversation or shared a meme/link",
            "High Mass (10 kg): Called you out of the blue or set up a concrete plan to hang out",
            "Super Massive (25 kg): Showed up for you when you needed help, or brought a thoughtful gift"
        ]
    )
    
    # Delta T = Time Delay
    delta_t = st.number_input(
        "Response Latency (Δt) - How many HOURS did it take them to execute this action/reply?",
        min_value=0.1, max_value=48.0, value=1.0, step=0.1,
        help="Example: If they replied in 30 minutes, enter 0.5. If it took 2 hours, enter 2.0."
    )
    
    # Mapping selection to raw numbers for math
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
        
        # Physics Math: Acceleration = Change in Velocity (assumed 1 unit of movement) over Time
        # a = 1 / delta_t. If delta_t is high (takes forever to reply), acceleration drops significantly.
        a = 1.0 / delta_t
        
        # Force = Mass * Acceleration
        F = m * a
        
        # Display the variables using LaTeX for formal physics presentation
        st.latex(r"a = \frac{1}{\Delta t} = \frac{1}{" + f"{delta_t}" + r"} = " + f"{a:.3f}" + r" \text{ m/s}^2")
        st.latex(r"F = m \cdot a = " + f"{m}" + r" \cdot " + f"{a:.3f}" + r" = " + f"{F:.3f}" + r" \text{ Newtons}")
        
        st.subheader("📊 Engine Output Verdict")
        st.metric(label="Calculated Attraction Force (F)", value=f"{F:.3f} N")
        
        # Mechanical Force boundaries
        if F >= 5.0:
            st.success("🟢 STRONG MOMENTUM: High kinetic force detected. This person is actively accelerating into your system. Safe to maintain orbit.")
        elif 1.0 <= F < 5.0:
            st.warning("🟡 WEAK KINETIC ENERGY: The force is minimal. Either their actions lack 'mass' or their response time ($\Delta t$) is causing massive friction. Do not advance.")
        else:
            st.error("🔴 INERTIA LOCK: Force approaches 0 Newtons. This is a static object. No self-generated mechanical movement detected from their side. Abort.")

# Keep Phase 2 and 3 intact below
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

st.write("---")
st.caption("Numbers never lie. Protect your system parameters.")
