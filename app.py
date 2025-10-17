import streamlit as st
import random
import time

st.set_page_config(page_title="Universal AI Agent | Aadarsh Potadar", page_icon="🤖", layout="wide")

# ---------- CUSTOM CSS (Dropdown + Inputs) ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');
body, .stApp {
    background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%) !important;
    color: #e4e4e7 !important;
    font-family: 'Inter', sans-serif;
}
.header-card {
    background: linear-gradient(135deg, rgba(99,102,241,0.1), rgba(168,85,247,0.1));
    border-radius: 20px;
    border: 1px solid rgba(99,102,241,0.2);
    backdrop-filter: blur(10px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.3);
    padding: 30px 20px;
    margin-bottom: 40px;
    text-align:center;
}
.header-card h1 {
    font-size: 2.8rem;
    font-weight: 700;
    background: linear-gradient(135deg, #6366f1, #a855f7, #ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
    letter-spacing: -1px;
}
.header-card .subtitle {
    color: #94a3b8;
    font-size: 1.1rem;
    font-weight: 400;
}
.header-card .author {
    color: #64748b;
    font-size: 0.95rem;
    margin-top: 16px;
}
/* Panel styles */
.panel-row {
    display: flex;
    gap: 30px;
    width: 100%;
    justify-content: space-between;
}
.left-panel, .right-panel {
    flex: 1;
    background: rgba(30, 30, 46, 0.8);
    border: 1px solid rgba(99, 102, 241, 0.3);
    border-radius: 16px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
    padding: 32px 22px 28px 22px;
    transition: box-shadow 0.3s ease;
    min-width: 340px;
}
.left-panel:hover, .right-panel:hover {
    box-shadow: 0 28px 70px rgba(99,102,241,0.19);
}
/* Section title */
.section-title {
    font-size: 1.35rem;
    font-weight: 600;
    margin-bottom: 20px;
    color: #f1f5f9 !important;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-title::before {
    content: '';
    width: 4px;
    height: 24px;
    background: linear-gradient(135deg, #6366f1, #a855f7);
    border-radius: 2px;
}
.stSelectbox label {
    color: #a5b4fc !important;
    font-weight: 500 !important;
    font-size: 1rem !important;
}
.stTextInput label {
    color: #a5b4fc !important;
    font-weight: 500 !important;
    font-size: 1rem !important;
}
.stSlider label {
    color: #a5b4fc !important;
    font-weight: 500 !important;
    font-size: 1rem !important;
}

/* --- Custom Dropdown --- */
.stSelectbox [data-baseweb="select"] {
    background: #23225a !important;
    color: #86efac !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 700 !important;
    font-size: 1.09rem !important;
    border-radius: 9px !important;
    border: 1px solid #6366f1 !important;
    min-height: 46px !important;
}
.stSelectbox [data-baseweb="popover"] {
    background: #181730 !important;
    color: #38bdf8 !important;
    border-radius: 14px !important;
    box-shadow: 0 0 14px 4px rgba(99,102,241,0.12) !important;
}
.stSelectbox [data-baseweb="option"] {
    background: #181730 !important;
    color: #38bdf8 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 700 !important;
    font-size: 1.07rem !important;
    border-bottom: 1px solid #23225a !important;
    transition: all 0.19s;
}
.stSelectbox [data-baseweb="option"]:hover {
    background: linear-gradient(90deg,#6366f1bb,#8B5CF6bb) !important;
    color: #fff !important;
}
.stSelectbox [aria-selected="true"] {
    background: linear-gradient(90deg,#60a5fa,#818cf8,#c084fc,#f472b6) !important;
    color: #22223b !important;
}
/* TextInput styles */
.stTextInput>div>input {
    background: #161743 !important;
    color: #38bdf8 !important;
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.07rem !important;
    border-radius: 9px !important;
    border: 1px solid #6366f1 !important;
}
/* Slider value */
.stSlider .css-1vg6q84 {
    color: #a855f7 !important;
    font-family: 'JetBrains Mono', monospace;
    font-size: 1rem;
}
/* Button */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg,#6366f1,#8b5cf6);
    color: white;
    font-weight: 600;
    padding: 16px;
    border-radius: 12px;
    border: none;
    font-size: 1.1rem;
    box-shadow: 0 8px 20px rgba(99, 102, 241, 0.27);
    transition: all 0.3s ease;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 18px 40px rgba(99,102,241,0.21);
}
/* Pills */
.industry-pill {
    display: inline-block;
    padding: 8px 16px;
    background: rgba(99,102,241,0.1);
    border: 1px solid rgba(99,102,241,0.3);
    border-radius: 20px;
    font-size: 0.85rem;
    color: #a5b4fc;
    font-weight: 500;
    margin: 9px 7px 0 0;
}
/* Log panel */
.decision-log {
    background: rgba(30, 30, 46, 0.7);
    border-radius: 16px;
    border: 1px solid rgba(99,102,241,0.32);
    box-shadow: 0 8px 32px rgba(48,46,70,0.11);
    padding: 23px 15px 2px 15px;
    min-height: 310px;
    font-size: 1rem;
    max-height: 490px;
    overflow-y: auto;
    margin-top: 10px;
    transition: box-shadow 0.3s;
}
.log-entry {
    background: rgba(23,23,44,0.7);
    border-left: 4px solid #6366F1;
    border-radius: 6px;
    margin: 10px 0;
    padding: 13px 14px 8px 16px;
    box-shadow: 0 3px 10px rgba(99,102,241,0.09);
    font-family: 'JetBrains Mono', monospace;
}
.log-entry.success { border-left: 4px solid #22C55E; }
.log-entry.error { border-left: 4px solid #EF4444; }
.log-entry.warning { border-left: 4px solid #F59E0B; }
/* Result Panel */
.result-panel {
    background: rgba(32,35,55,0.9);
    border-radius: 14px;
    padding: 18px;
    border: 2px solid #22C55E;
    margin-top: 18px;
    box-shadow: 0 0 28px rgba(34,197,94,0.12);
    font-family: 'JetBrains Mono', monospace;
    color: #D1FAE5;
    font-size: 1.1rem;
}
.result-panel.error {
    border-color: #EF4444;
    box-shadow: 0 0 25px rgba(239,68,68,0.15);
    color: #FCA5A5;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class="header-card">
    <h1>🤖 Universal AI Agent Simulator</h1>
    <p class="subtitle">Autonomous Task Planning Across Multiple Industries</p>
    <p class="author">Created by <strong>Aadarsh Potadar</strong> | Portfolio Project</p>
</div>
""", unsafe_allow_html=True)

# ---------- MAIN PANELS ----------
st.markdown('<div class="panel-row">', unsafe_allow_html=True)
st.markdown('<div class="left-panel">', unsafe_allow_html=True)

st.markdown('<div class="section-title">Task Configuration</div>', unsafe_allow_html=True)
industry = st.selectbox("Select Industry", [
    "🚁 Autonomous Drones (FlytBase, DJI)",
    "📦 Logistics & Delivery (Amazon, FedEx)",
    "🏭 Manufacturing (Tesla, Robotics)",
    "🏥 Healthcare (Hospitals, Clinics)",
    "⚡ Energy Management (Grid, Utilities)"
])
location = st.text_input("Target Location", "Solar Farm Alpha")
distance = st.slider("Distance (km)", 5, 100, 25)
complexity = st.selectbox("Task Complexity", [
    "Low - Simple task", "Medium - Standard operation", "High - Complex mission"])
weather = st.selectbox("Weather / Conditions", [
    "Favorable (Clear, Low Wind)",
    "Moderate (Cloudy, Medium Wind)",
    "Unfavorable (Rain / High Wind)"])

execute = st.button("🚀 Execute AI Agent")

st.markdown("""
<div>
    <span class="industry-pill">Agentic AI</span>
    <span class="industry-pill">Autonomous Systems</span>
    <span class="industry-pill">Multi-Industry</span>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="right-panel">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Agent Decision Log</div>', unsafe_allow_html=True)
log = st.container()
result_box = st.empty()
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- AI SIMULATION ----------
if execute:
    with log:
        st.markdown('<div class="decision-log">', unsafe_allow_html=True)
        def log_entry(step, decision, reasoning, status="info"):
            status_cls = {"success":"success","error":"error","warning":"warning"}.get(status,"")
            st.markdown(f"""
            <div class="log-entry {status_cls}">
                <div><b>{step}</b> — {decision}</div>
                <div style="font-size:0.98rem;color:#cbd5e1;">{reasoning}</div>
            </div>
            """, unsafe_allow_html=True)
        log_entry("STEP 1: Environment Analysis","🌍 Checking Conditions...",f"Analyzing safety for {location}")
        time.sleep(0.6)
        weather_ok = "Favorable" in weather or ("Moderate" in weather and random.random()>0.3)
        if weather_ok:
            log_entry("STEP 1: Environment Analysis","✅ CONDITIONS APPROVED","Environment is safe for operation","success")
        else:
            log_entry("STEP 1: Environment Analysis","❌ CONDITIONS UNSAFE","Detected severe conditions","error")
            st.markdown('</div>', unsafe_allow_html=True)
            result_box.markdown("""<div class="result-panel error">❌ TASK REJECTED — Unsafe environmental conditions</div>""", unsafe_allow_html=True)
            st.stop()
        time.sleep(0.8)
        log_entry("STEP 2: Resource Calculation","📊 Estimating Resource Load...",f"Distance: {distance}km, Complexity: {complexity}")
        complexity_factor = {"Low":1.0,"Medium":1.3,"High":1.6}[[i for i in complexity.split() if i][0]]
        total = distance * 1.5 * complexity_factor
        log_entry("STEP 2: Resource Calculation",f"✅ {round(total)}% total load","Added safety margin 20%","success")
        resource_ok = total <= 95
        time.sleep(0.9)
        if resource_ok:
            log_entry("STEP 3: Resource Selection","✅ RESOURCE FOUND","Assigned RESOURCE-001, 95% capacity","success")
        else:
            log_entry("STEP 3: Resource Selection","❌ INSUFFICIENT RESOURCES","Capacity exceeds threshold","error")
            st.markdown('</div>', unsafe_allow_html=True)
            result_box.markdown("""<div class="result-panel error">❌ TASK REJECTED — Insufficient resources</div>""", unsafe_allow_html=True)
            st.stop()
        time.sleep(0.7)
        eta = round((distance/45)*60)
        log_entry("STEP 4: Path Planning","✅ OPTIMAL ROUTE READY",f"ETA: {eta} minutes, 5 checkpoints","success")
        time.sleep(0.6)
        log_entry("STEP 5: Final Decision","🎯 APPROVED","All systems ready for deployment","success")
        st.markdown('</div>', unsafe_allow_html=True)
        result_box.markdown(f"""
        <div class="result-panel">
        ✅ TASK APPROVED<br>Resource Assigned: <span style='color:#A7F3D0'>RESOURCE-001</span><br>
        Capacity Use: <span style='color:#FDE68A'>95% (required {round(total)}%)</span><br>
        ETA: <span style='color:#93C5FD'>{eta} minutes</span><br>
        Location: <span style='color:#E5E7EB'>{location}</span>
        </div>
        """, unsafe_allow_html=True)


