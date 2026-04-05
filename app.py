import streamlit as st

KB = {
    "time series": "A time series is a sequence of data points indexed in time order (e.g. monthly sales). It captures how a variable evolves over time.",
    "components": "A time series has 4 components:\n1. Trend (T) — long-run direction\n2. Seasonality (S) — repeating periodic patterns\n3. Cyclical (C) — irregular multi-year fluctuations\n4. Irregular/Residual (I) — random noise",
    "stationarity": "A time series is stationary if its mean, variance, and autocovariance remain constant over time. Required for ARIMA modeling.",
    "arima": "ARIMA(p,d,q) = AutoRegressive Integrated Moving Average.\n• p = AR order (past values)\n• d = differencing (for stationarity)\n• q = MA order (past errors)\nFormula: φ(B)·Δᵈ·Yₜ = θ(B)·εₜ",
    "ar": "AR(p): Yₜ = c + φ₁Yₜ₋₁ + ... + φₚYₜ₋ₚ + εₜ\nCurrent value depends on its own past p values.",
    "ma": "MA(q): Yₜ = μ + εₜ + θ₁εₜ₋₁ + ... + θqεₜ₋q\nCurrent value depends on past q error terms.",
    "acf": "ACF measures correlation between Yₜ and Yₜ₋ₖ at lag k.\n• ACF cuts off after lag q → MA(q)\n• ACF tails off → AR process",
    "pacf": "PACF measures direct correlation at lag k.\n• PACF cuts off after lag p → AR(p)\n• PACF tails off → MA process",
    "differencing": "Differencing removes trend to achieve stationarity.\n• 1st difference: ΔYₜ = Yₜ − Yₜ₋₁\nd in ARIMA = number of differences needed.",
    "adf": "ADF test: checks for unit root.\n• H₀: non-stationary\n• p-value < 0.05 → stationary",
    "kpss": "KPSS test: checks stationarity directly.\n• H₀: stationary\n• p-value < 0.05 → non-stationary",
    "white noise": "White noise: E(εₜ)=0, Var(εₜ)=σ², Cov(εₜ,εₛ)=0.\nResiduals of a good model should be white noise.",
    "random walk": "Random walk: Yₜ = Yₜ₋₁ + εₜ\nNon-stationary; 1st difference gives white noise.",
    "trend": "Trend: long-term upward/downward movement. Can be deterministic or stochastic.",
    "seasonality": "Seasonality: regular patterns tied to calendar periods (e.g., quarterly peaks).",
    "sarima": "SARIMA(p,d,q)(P,D,Q)S: seasonal ARIMA.\nS = seasonal period (12 for monthly data).",
    "aic": "AIC/BIC: model selection criteria. Lower = better. BIC penalises complexity more.",
    "bic": "BIC penalises model complexity more than AIC. Use both to select optimal ARIMA orders.",
    "exponential smoothing": "Ŷₜ = αYₜ + (1−α)Ŷₜ₋₁, α ∈ (0,1)\nMore weight to recent obs. Holt-Winters extends to trend & seasonality.",
    "ljung": "Ljung-Box test: checks if residuals are white noise.\n• H₀: residuals uncorrelated\n• p-value > 0.05 → model is adequate",
    "unit root": "Unit root: AR polynomial root = 1 → non-stationary. Use ADF to detect. Fix by differencing.",
    "forecast": "h-step forecast: Ŷₜ₊ₕ|ₜ. Intervals widen with h.\nMeasures: MAE, RMSE, MAPE.",
    "hi": "Hello! Ask me about time series concepts, formulas, and models.",
    "hello": "Hi! I'm your Applied Time Series assistant. What would you like to know?",
    "help": "I can answer about: stationarity, ARIMA, ACF, PACF, ADF, KPSS, white noise, differencing, exponential smoothing, forecasting, AIC/BIC, Ljung-Box."
}

def get_response(user_input):
    q = user_input.lower().strip()
    for key in KB:
        if key in q:
            return KB[key]
    if "test" in q:
        return "Common tests: ADF (unit root), KPSS (stationarity), Ljung-Box (residuals)."
    if "model" in q or "select" in q:
        return "Model selection: check ACF/PACF plots → identify p,q → use AIC/BIC to compare → validate with Ljung-Box."
    return "I don't have that yet. Try: stationarity, ARIMA, ACF, PACF, ADF, forecasting, white noise."

st.set_page_config(page_title="Time Series Bot", page_icon="📈")
st.title("📈 Applied Time Series Chatbot")
st.caption("Rule-based NLP chatbot using keyword matching for domain-specific knowledge retrieval.")

if "history" not in st.session_state:
    st.session_state.history = [("bot", "Hi! Ask me about ARIMA, stationarity, ACF, PACF, forecasting and more.")]

for role, msg in st.session_state.history:
    with st.chat_message("assistant" if role == "bot" else "user"):
        st.markdown(msg)

user_input = st.chat_input("Type your question here...")
if user_input:
    st.session_state.history.append(("user", user_input))
    reply = get_response(user_input)
    st.session_state.history.append(("bot", reply))
    st.rerun()
