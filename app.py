
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# -------------------------------
# PAGE SETTINGS
# -------------------------------

st.set_page_config(
    page_title="Particle in a Box",
    page_icon="⚛️",
    layout="wide"
)

st.title("⚛️ Particle in a Box")
st.write("An interactive simulation of a particle in a 1D infinite potential well.")

st.divider()

# -------------------------------
# PHYSICAL CONSTANTS
# -------------------------------

h = 6.62607015e-34
m = 9.1093837e-31
e = 1.602176634e-19

# -------------------------------
# USER INPUTS
# -------------------------------

st.sidebar.header("Simulation Parameters")

L_nm = st.sidebar.number_input(
    "Box length L (nm)",
    min_value=0.1,
    value=2.0,
    step=0.1
)

n = st.sidebar.number_input(
    "Quantum number (n)",
    min_value=1,
    value=2,
    step=1
)

N = st.sidebar.number_input(
    "Number of position points",
    min_value=10,
    value=500,
    step=10
)

# -------------------------------
# CALCULATIONS
# -------------------------------

L = L_nm * 1e-9

x = np.linspace(0, L, int(N))

psi = np.sqrt(2/L) * np.sin(n * np.pi * x / L)

E = (h**2 / (8 * m * L**2)) * n**2
E_ev = E / e

P = np.abs(psi)**2
psi_scaled = psi * np.sqrt(L)
P_scaled = P * L

# -------------------------------
# ENERGY RESULT
# -------------------------------

st.subheader("Energy of the Particle")

energy_table = pd.DataFrame({
    "Energy (Joules)": [E],
    "Energy (eV)": [E_ev]
}, index=[f"n = {n}"])

st.dataframe(
    energy_table.style.format({
        "Energy (Joules)": "{:.3e}",
        "Energy (eV)": "{:.4f}"
    }),
    use_container_width=True
)

st.divider()

# -------------------------------
# GRAPHS
# -------------------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("Wavefunction")

    fig1, ax1 = plt.subplots(figsize=(6, 4))

    ax1.plot(x * 1e9, psi_scaled)
    ax1.set_xlabel("Position x (nm)")
    ax1.set_ylabel("Scaled wavefunction")
    ax1.set_title(f"Wavefunction for n = {n}")
    ax1.grid()

    st.pyplot(fig1)

with col2:
    st.subheader("Probability Density")

    fig2, ax2 = plt.subplots(figsize=(6, 4))

    ax2.plot(x * 1e9, P_scaled)
    ax2.set_xlabel("Position x (nm)")
    ax2.set_ylabel("Scaled probability density")
    ax2.set_title(f"Probability density for n = {n}")
    ax2.grid()

    st.pyplot(fig2)

st.divider()

st.caption("Particle in a Box | Quantum Mechanics Simulation")
