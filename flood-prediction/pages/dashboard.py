import streamlit as st

# CSS for styling
def add_custom_css():
    st.markdown("""
    <style>
        .dashboard-header {
            text-align: center;
            margin-bottom: 40px;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin: 20px;
        }
        .stat-card {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
    </style>
    """, unsafe_allow_html=True)

# Main content
def display_page():
    add_custom_css()
    st.markdown("<h1 class='dashboard-header'>Flood Prediction Dashboard</h1>", unsafe_allow_html=True)

    st.markdown("<h2>Flood Levels Across Regions</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="stats-grid">
        <div class="stat-card"><h3>Region A</h3><p>High</p></div>
        <div class="stat-card"><h3>Region B</h3><p>Moderate</p></div>
        <div class="stat-card"><h3>Region C</h3><p>Low</p></div>
        <div class="stat-card"><h3>Region D</h3><p>Critical</p></div>
    </div>
    """, unsafe_allow_html=True)
