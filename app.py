import streamlit as st
import math

st.set_page_config(page_title="Love Physics Engine", page_icon="⚛️", layout="centered")

st.title("⚛️ The Love Physics Engine v7.1")
st.write("---")

phase = st.sidebar.radio(
    "Select Engine Module:",
    [
        "Phase 1: Mechanical Force Calculator", 
        "Phase 2: Entropy & Red Flag Filter", 
        "Phase 3: Trajectory Simulator",
        "Phase 4: Quantum Wavefunction Collapse",
        "Phase 5: Relativistic Escape Velocity",
        "Phase 6: The Black Box (Debrief)"
    ]
)

# --- Shared Logic for Phase 1 ---
mass_map = {"Low Mass (1 kg)": 1.0, "Medium Mass (5 kg)": 5.0, "High Mass (10 kg)": 10.0, "Super Massive (25 kg)": 25.0}

if phase == "Phase 1: Mechanical Force Calculator":
    st.subheader("Phase 1: Classical Mechanics")
    mass_choice = st.selectbox("Action Mass (m)", list(mass_map.keys()))
    delta_t = st.number_input("Response Latency (Δt) - Hours", min_value=0.1, value=1.0)
    if st.button("CALCULATE FORCE"):
        a = 1.0 / delta_t
        F = mass_map[mass_choice] * a
        st.latex(r"F = " + f"{F:.3f} N")
        if F >= 5.0: st.success("🟢 STRONG MOMENTUM")
        else: st.error("🔴 INERTIA LOCK")

elif phase == "Phase 2: Entropy & Red Flag Filter":
    st.subheader("Phase 2: Thermodynamics")
    past = st.slider("Past Energy", 1, 10, 5)
    curr = st.slider("Current Energy", 1, 10, 5)
    flags = st.checkbox("Hot/Cold Cycles") + st.checkbox("Gaslighting/Deflection") + st.checkbox("Hidden Phone/Secrets")
    if st.button("ANALYZE ENTROPY"):
        if curr < past: st.error(f"📉 ENERGY LOSS: {past-curr} units.")
        if flags > 0: st.warning(f"⚠️ {flags} Structural Leaks Found.")

elif phase == "Phase 3: Trajectory Simulator":
    st.subheader("Phase 3: Orbital Pathing")
    align = st.slider("Core Alignment %", 0, 100, 50)
    if st.button("SIMULATE"):
        if align < 50: st.error("💥 COLLISION LIKELY")
        else: st.success("🚀 STABLE TRAJECTORY")

elif phase == "Phase 4: Quantum Wavefunction Collapse":
    st.subheader("Phase 4: Schrödinger's Crush")
    entang = st.slider("Entanglement (Sync)", 1, 10, 5)
    interf = st.radio("Interference", ["Constructive", "Destructive"])
    if st.button("COLLAPSE WAVEFUNCTION"):
        prob = (entang * 10) + (20 if interf == "Constructive" else -20)
        prob = max(1, min(99, prob))
        st.latex(r"|c_1|^2 = " + f"{prob}%")
        if prob > 60: st.success("🐈 ALIVE")
        else: st.error("💀 DEAD")

# ==========================================
# FIXED PHASE 5: ESCAPE VELOCITY
# ==========================================
elif phase == "Phase 5: Relativistic Escape Velocity":
    st.subheader("Phase 5: Escape Velocity")
    g = st.slider("Your Attachment (G)", 1, 10, 5)
    m = st.slider("Their Mass (M)", 1, 10, 5)
    r = st.slider("Proximity (r)", 1, 10, 5)
    if st.button("CALCULATE VE"):
        ve_val = math.sqrt((2.0 * g * m) / r)
        # Cleaned up formatting string to prevent conflicting variables
        st.latex(r"v_e = " + f"{ve_val:.2f}" + r" \text{ Mach}")
        if ve_val > 5.0: 
            st.error("🚨 EXTREME GRAVITATIONAL PULL: Escape Velocity high. Cut all comms immediately.")
        elif 2.5 <= ve_val <= 5.0:
            st.warning("⚠️ STRONG ORBITAL TETHER: High effort required to detach.")
        else:
            st.success("🌌 LOW GRAVITY WELL: Easy detachment possible.")

elif phase == "Phase 6: The Black Box (Debrief)":
    st.subheader("Phase 6: Post-Mission Root Cause Analysis")
    st.write("Use this section to record the 'Black Box' data from past failed missions.")
    st.info("💡 RESEARCH NOTE: Ask her questions about Delta T (timing), Mass (effort type), and Gravity (clinginess).")
    
    lesson_1 = st.text_area("What was the primary cause of system failure?")
    lesson_2 = st.text_area("What variable did the engine miss?")
    
    adjustment = st.multiselect(
        "Select Adjustments:",
        ["Be stricter with Response Latency (Phase 1)", 
         "Don't ignore the First Law of Entropy (Phase 2)", 
         "Wait for higher Entanglement before collapsing (Phase 4)",
         "Maintain a larger Proximity Radius early on (Phase 5)"]
    )
    if st.button("LOG DEBRIEF DATA"):
        st.success("✅ MISSION DATA ARCHIVED. Your system parameters have been mentally updated.")
        st.balloons()

st.write("---")
st.caption("Numbers never lie. Structural integrity restored.")
