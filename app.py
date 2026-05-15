import streamlit as st

# App styling and title
st.set_page_config(page_title="Love Physics Engine", page_icon="⚛️", layout="centered")

st.title("⚛️ The Love Physics Engine v1.0")
st.write("---")
st.subheader("Phase 1: The Quantum Crush Evaluator")
st.write("Calculate the state of the *Relational Superposition* before you risk a collapse (confession).")

# Section 1: Mechanical Physics (Inputs)
st.header("1. Mechanical Forces (Action Data)")

initiation = st.slider(
    "Initiation Vector: Out of the last 10 interactions, how many did THEY start?",
    min_value=0, max_value=10, value=5
)

latency = st.selectbox(
    "Response Latency (Δt): What is their typical text reply time?",
    options=["Instantly to < 15 mins", "15 mins to 2 hours", "2 to 6 hours", "6+ hours / Next day"]
)

# Section 2: Theoretical Physics (Inputs)
st.header("2. Theoretical Constants")

object_permanence = st.radio(
    "Object Permanence: Do they remember 'low-mass' details you mentioned days ago?",
    options=["Yes, perfectly", "Sometimes", "Rarely/Never"]
)

# Conversion logic for calculations
latency_scores = {
    "Instantly to < 15 mins": 10,
    "15 mins to 2 hours": 7,
    "2 to 6 hours": 4,
    "6+ hours / Next day": 1
}

op_scores = {
    "Yes, perfectly": 10,
    "Sometimes": 5,
    "Rarely/Never": 0
}

# The Physics Calculations
if st.button("RUN ENGINE ANALYSIS"):
    # Calculate total energy score out of 30
    score = (initiation * 1.0) + latency_scores[latency] + op_scores[object_permanence]
    probability = (score / 30.0) * 100
    
    st.write("---")
    st.header("📊 System Analysis Results")
    st.metric(label="Probability of Love State (Ψ)", value=f"{probability:.1f}%")
    
    # Logic boundaries (The Safety Gates)
    if probability >= 75:
        st.success("🟢 STABLE ORBIT: The data shows strong mutual gravity. The wavefunction is stable enough for observation (confession).")
    elif 40 <= probability < 75:
        st.warning("🟡 UNCERTAINTY PRINCIPLE ACTIVE: High superposition/mixed signals. Keep gathering data outside the Event Horizon. Do NOT collapse the wavefunction yet.")
    else:
        st.error("🔴 BLACK HOLE DETECTED: Massively asymmetrical energy output. If you cross this Event Horizon, you risk a total energy drain. Abort system integration.")

st.write("---")
st.caption("Numbers never lie. Protect your system parameters.")
