---
title: AgriSensa Intelligence
emoji: 🛰️
colorFrom: green
colorTo: blue
sdk: streamlit
sdk_version: 1.32.0
app_file: agrisensa_streamlit/Home.py
pinned: false
---
# 🛰️ AgriSensa Intelligence Ecosystem v5.0 (Global Standard)

![Platform Status](https://img.shields.io/badge/Status-Production--Ready-10b981?style=for-the-badge)
![AI Engine](https://img.shields.io/badge/AI-LightGBM%20%7C%20RandomForest%20%7C%20SHAP-3b82f6?style=for-the-badge)
![UI Theme](https://img.shields.io/badge/Theme-Emerald--Dark-064e3b?style=for-the-badge)
![Ecosystem Size](https://img.shields.io/badge/Satellites-10%2B%20Modules-9333ea?style=for-the-badge)

**AgriSensa** is an advanced agricultural super-app ecosystem designed for data-driven precision farming. It integrates real-world agronomic datasets (FAO), real-time food price monitoring (BAPANAS), and high-fidelity weather intelligence into a unified command center. 

Evolving from a single monolithic dashboard, AgriSensa is now a **Multi-Satellite Ecosystem**, equipped with Enterprise-grade Multi-Tenant architecture and Explainable AI (XAI).

---

## 🌟 Key Engineering Features

### 🧠 Advanced ML Pipeline & Explainable AI (XAI)
*   **Yield Prediction Ultra**: Powered by highly optimized Random Forest and LightGBM models (compressed from 111MB to 1.35MB for serverless deployment) trained on 28,000+ real-world FAO observations.
*   **Interpretable AI (SHAP)**: Decisions are no longer "Black Box"—the AI explains *why* it recommends specific actions based on feature importance (Nitrogen, pH, Temp).
*   **Robust Fallback Architecture**: Zero-downtime AI. If the cloud ML `.pkl` model fails to load, the system intelligently cascades to heuristic fallback algorithms without crashing the UI.
*   **Smart Crop Advisor**: 99.55% accuracy in crop recommendation based on specific soil and climate parameters.

### 🏢 Enterprise-Grade Software Architecture
*   **Multi-Tenant Bank Sampah**: Data isolation for multiple organizations using the `Bank Sampah Terpadu` module, complete with robust access control and real-time `st.data_editor`.
*   **Type-Hinted Codebase**: Clean, maintainable, and statically-typed Python codebase ensuring reliability across the ML-service layer.
*   **Serverless API Ready**: Prepared for external integration via REST APIs hosted on Vercel.

### 📊 Real-Time Market Intelligence
*   **Bapanas Auto-Seek**: Smart integration with the National Food Agency (BAPANAS) with 7-day lookback logic, ensuring price data is always available even during API lag.
*   **Market Trend Analysis**: Predictive price modeling using Linear Regression and Random Forest to anticipate market fluctuations.

---

## 🚀 The Satellite Network

AgriSensa is structured as a unified multi-satellite ecosystem. Each satellite focuses on a specific agricultural domain:

| Satellite / Module | Focus Area | Key Technologies |
| :--- | :--- | :--- |
| **AgriSensa Tech** | IoT, Hydroponics, GIS, & Precision Ag | Sensor Simulation, Folium |
| **AgriSensa Biz** | RAB, Profit Analysis, & Supply Chain | Dynamic Dataframes |
| **Ekonometrika Pro** | Advanced Econometrics Education (9 Chapters) | Panel Data Regression, OLS |
| **AgriSensa Eco** | Bank Sampah Terpadu, Conservation | Multi-Tenant Database, Auth |
| **AgriSensa Commodities** | SOPs, Jamu Saintifik, Cabai, Padi | Dynamic Recipe & RAB Engine |
| **AgriSensa Livestock** | Animal Husbandry & Aquaculture | FCR Calculators |

---

## 🛠️ Tech Stack & Architecture

- **Core**: Python 3.10+
- **Frontend**: Streamlit (Emerald Dark Theme & Custom CSS)
- **Machine Learning**: Scikit-Learn, LightGBM, Joblib, SHAP
- **Data Engineering**: Pandas, NumPy, JSON-API Integration
- **Backend/API**: Flask, Vercel Serverless Functions
- **Visualization**: Plotly, Altair, Folium (GIS)

---

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yandri918/streamlit_terbaru.git
   cd agrisensa-api
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_key
   DATABASE_URL=your_db_url
   BAPANAS_API_KEY=your_bapanas_key (Optional)
   ```

4. **Run the Dashboard**:
   ```bash
   streamlit run agrisensa_streamlit/Home.py
   ```

---

## 💎 Premium UI Configuration

The ecosystem is pre-configured with a professional dark theme. Configuration can be found in `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#10b981"
backgroundColor = "#0f172a"
secondaryBackgroundColor = "#1e293b"
textColor = "#f8fafc"
```

---

## ⚖️ Accountability & Data Source
*   **Agronomic Data**: UN FAO (Food and Agriculture Organization) statistics.
*   **Market Data**: BAPANAS (Badan Pangan Nasional) API.
*   **Weather Data**: Open-Meteo Professional API.
*   **Medical / Botanics**: B2P2TOOT Saintifikasi Jamu Research.

© 2026 AgriSensa Intelligence Systems | *Advancing Food Security through Data Precision & Explainable AI.*