
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# --------------------------------
# PAGE SETTINGS
# --------------------------------

st.set_page_config(
    page_title="Particle in a Box | Quantum Physics",
    page_icon="⚛️",
    layout="wide"
)

# --------------------------------
# CUSTOM COLOUR THEME
# --------------------------------

st.markdown("""
<style>
.stApp {
    background-color: #0b1324;
    color: #e8f1ff;
}

[data-testid="stSidebar"] {
    background-color: #111f36;
}

h1, h2, h3 {
    color: #70d6ff !important;
}

p, label {
    color: #d7e5f5;
}

div[data-testid="stMetric"] {
    background-color: #142640;
    border: 1px solid #254568;
    padding: 16px;
    border-radius: 12px;
}

.stNumberInput input {
    background-color: #142640;
}

hr {
    border-color: #294663;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------
# TITLE
# --------------------------------

st.title("⚛️ Particle in a Box")

st.markdown(
    "### An Interactive Quantum Mechanics Simulation"
)

st.markdown(
    "Explore the energy states, wavefunction and probability "
    "distribution of a particle confined in a one-dimensional "
    "infinite potential well."
)

st.divider()

# --------------------------------
# PHYSICAL CONSTANTS
# --------------------------------

h = 6.62607015e-34
m = 9.1093837e-31
e = 1.602176634e-19

# --------------------------------
# USER INPUTS
# --------------------------------

st.sidebar.title("Simulation Controls")
st.sidebar.markdown("Adjust the parameters below.")

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

st.sidebar.divider()
st.sidebar.caption(
    "Particle: Electron | Potential: Infinite square well"
)

# --------------------------------
# CALCULATIONS
# --------------------------------

L = L_nm * 1e-9
n = int(n)
N = int(N)

x = np.linspace(0, L, N)

# Wavefunction
psi = np.sqrt(2/L) * np.sin(n * np.pi * x / L)

# Energy
E = (h**2 / (8 * m * L**2)) * n**2
E_ev = E / e

# Dimensionless quantities for plotting
psi_scaled = psi * np.sqrt(L)

P = np.abs(psi)**2
P_scaled = P * L

# --------------------------------
# ENERGY RESULTS
# --------------------------------

st.header("Energy Results")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Energy (Joules)",
        value=f"{E:.3e} J"
    )

with col2:
    st.metric(
        label="Energy (electronvolts)",
        value=f"{E_ev:.4f} eV"
    )

energy_table = pd.DataFrame({
    "Quantum Number": [n],
    "Energy (Joules)": [E],
    "Energy (eV)": [E_ev]
})

st.dataframe(
    energy_table.style.format({
        "Energy (Joules)": "{:.3e}",
        "Energy (eV)": "{:.4f}"
    }),
    use_container_width=True,
    hide_index=True
)

st.divider()

# --------------------------------
# MATHEMATICAL EQUATIONS
# --------------------------------

st.header("Mathematical Model")

st.markdown("**1. Energy eigenvalues**")

st.latex(r"E_n = \frac{n^2 h^2}{8mL^2}")

st.markdown("**2. Wavefunction**")

st.latex(
    r"\psi_n(x)=\sqrt{\frac{2}{L}}"
    r"\sin\left(\frac{n\pi x}{L}\right)"
)

st.markdown("**3. Probability density**")

st.latex(
    r"P_n(x)=|\psi_n(x)|^2"
    r"=\frac{2}{L}\sin^2\left(\frac{n\pi x}{L}\right)"
)

st.caption(
    "Here, n is the quantum number, h is Planck's constant, "
    "m is the electron mass and L is the box length."
)

st.divider()

# --------------------------------
# WAVEFUNCTION GRAPH
# --------------------------------

st.header("Quantum State Visualisation")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Wavefunction")

    fig1, ax1 = plt.subplots(figsize=(7, 4))

    fig1.patch.set_facecolor("#142640")
    ax1.set_facecolor("#142640")

    ax1.plot(
        x * 1e9,
        psi_scaled,
        color="#70d6ff",
        linewidth=2.5
    )

    ax1.axhline(0, color="white", linewidth=0.8, alpha=0.6)

    ax1.set_xlabel("Position x (nm)", color="white")
    ax1.set_ylabel("Scaled wavefunction", color="white")
    ax1.set_title(f"Wavefunction for n = {n}", color="white")

    ax1.tick_params(colors="white")
    ax1.grid(alpha=0.2, color="white")

    for spine in ax1.spines.values():
        spine.set_color("#52708f")

    fig1.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)

with col2:
    st.subheader("Probability Density")

    fig2, ax2 = plt.subplots(figsize=(7, 4))

    fig2.patch.set_facecolor("#142640")
    ax2.set_facecolor("#142640")

    ax2.plot(
        x * 1e9,
        P_scaled,
        color="#55e6c1",
        linewidth=2.5
    )

    ax2.fill_between(
        x * 1e9,
        P_scaled,
        color="#55e6c1",
        alpha=0.18
    )

    ax2.set_xlabel("Position x (nm)", color="white")
    ax2.set_ylabel("Scaled probability density", color="white")
    ax2.set_title(f"Probability Density for n = {n}", color="white")

    ax2.tick_params(colors="white")
    ax2.grid(alpha=0.2, color="white")

    for spine in ax2.spines.values():
        spine.set_color("#52708f")

    fig2.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)

st.divider()

# --------------------------------
# PHYSICS EXPLANATION
# --------------------------------

st.header("Understanding the Physics")

with st.expander("What are bound states?"):
    st.write("""
    The state in which the particle moves back and fro is called a bound state.

    In such types of states the energy of the particle is quantized. 
    """)

with st.expander("What is a Particle in a Box?"):
    st.write("""
    The particle in a box is a basic model in quantum mechanics.

    It describes a particle confined inside a one-dimensional
    region with perfectly rigid walls.

    The potential energy is zero inside the box and infinite
    outside it. Therefore, the particle cannot exist outside
    the box.
    """)

with st.expander("What does the wavefunction graph show?"):
    st.write("""
    The wavefunction describes the quantum state of the particle.

    It can have positive and negative values. The number of
    half-wavelength sections inside the box depends on the
    quantum number n.

    The wavefunction is zero at both walls.
    """)

with st.expander("What does probability density show?"):
    st.write("""
    The probability density is the square of the absolute
    value of the wavefunction.

    It tells us the probablity of finding the particle inside the box.

    A larger probability density means a greater probablity
    of finding the particle in that region.
    """)

st.divider()

st.caption(
    "Particle in a Box | Computational Quantum Mechanics Project"
)
