import streamlit as st
import pandas as pd
import plotly.express as px
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="NextGen AI Visualizer",
    page_icon="🚀",
    layout="wide"
)

# ---------------- PREMIUM MODERN CSS ----------------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #f6f9ff, #eef2ff);
}

.main {
    background: rgba(255, 255, 255, 0.75);
    backdrop-filter: blur(15px);
    padding: 40px;
    border-radius: 25px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.08);
}

/* ---- HERO CARD ---- */
.hero-wrapper {
    position: relative;
    margin: 10px 0 36px 0;
    border-radius: 32px;
    padding: 3px;
    background: linear-gradient(135deg, #42e695, #7873f5, #ff6ec4, #f7971e);
    background-size: 300% 300%;
    animation: gradientShift 6s ease infinite;
    box-shadow: 0 25px 70px rgba(66,230,149,0.28);
}

.hero-inner {
    background: rgba(255,255,255,0.97);
    border-radius: 30px;
    padding: 48px 48px 40px 48px;
    backdrop-filter: blur(24px);
    position: relative;
    overflow: hidden;
    text-align: center;
}

/* Decorative glow orbs */
.hero-inner::before {
    content: "";
    position: absolute;
    width: 400px; height: 400px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(120,115,245,0.09) 0%, transparent 70%);
    top: -140px; right: -120px;
    pointer-events: none;
}
.hero-inner::after {
    content: "";
    position: absolute;
    width: 280px; height: 280px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(66,230,149,0.09) 0%, transparent 70%);
    bottom: -80px; left: -80px;
    pointer-events: none;
}

.hero-title {
    font-size: 68px;
    font-weight: 900;
    background: linear-gradient(90deg, #42e695, #7873f5, #ff6ec4);
    background-size: 200% 200%;
    animation: gradientShift 5s ease infinite;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 2px;
    line-height: 1.1;
    margin-bottom: 18px;
}

.hero-subtitle {
    font-size: 22px;
    font-weight: 600;
    color: #666;
    margin-bottom: 28px;
    line-height: 1.5;
}

.hero-divider {
    height: 3px;
    border-radius: 2px;
    background: linear-gradient(90deg, #42e695, #7873f5, #ff6ec4, #f7971e);
    background-size: 200% 200%;
    animation: gradientShift 4s ease infinite;
    margin: 0 auto 28px auto;
    width: 60%;
}

.hero-badge-strip {
    display: flex;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 8px 20px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    color: white;
    box-shadow: 0 4px 16px rgba(0,0,0,0.12);
}

.hero-badge-green  { background: linear-gradient(90deg, #42e695, #3bb78f); }
.hero-badge-purple { background: linear-gradient(90deg, #7873f5, #6a11cb); }
.hero-badge-pink   { background: linear-gradient(90deg, #ff6ec4, #ff758c); }

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #ff758c, #ff7eb3);
    color: white;
    border-radius: 15px;
    height: 3.5em;
    font-size: 18px;
    font-weight: 600;
    border: none;
    box-shadow: 0 8px 20px rgba(255,118,136,0.4);
    transition: 0.3s ease;
}

.stButton>button:hover {
    transform: scale(1.05);
}

/* AI ULTRA CARD */
/* ---- AI SUMMARY CARD ---- */
.ai-summary-wrapper {
    position: relative;
    margin: 40px 0 0 0;
    border-radius: 28px 28px 0 0;
    padding: 3px 3px 0 3px;
    background: linear-gradient(135deg, #ff6ec4, #7873f5, #42e695, #f7971e);
    background-size: 300% 300%;
    animation: gradientShift 6s ease infinite;
    box-shadow: 0 25px 70px rgba(255,110,196,0.25);
}

.ai-summary-inner {
    background: rgba(255,255,255,0.97);
    border-radius: 26px 26px 0 0;
    padding: 28px 32px 14px 32px;
    backdrop-filter: blur(20px);
}

.ai-summary-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 14px;
}

.ai-summary-title {
    font-size: 28px;
    font-weight: 900;
    background: linear-gradient(90deg, #ff6ec4, #7873f5, #42e695);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 0.5px;
}

.ai-summary-pill {
    display: inline-block;
    padding: 5px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    color: white;
    background: linear-gradient(90deg, #ff6ec4, #7873f5);
    box-shadow: 0 4px 14px rgba(255,110,196,0.4);
}

.ai-summary-divider {
    height: 3px;
    border-radius: 2px;
    background: linear-gradient(90deg, #ff6ec4, #7873f5, #42e695, #f7971e);
    margin-bottom: 0;
    background-size: 200% 200%;
    animation: gradientShift 4s ease infinite;
}

/* body continuation */
.ai-summary-body {
    background: rgba(255,255,255,0.97);
    border-radius: 0 0 26px 26px;
    padding: 24px 32px 32px 32px;
    position: relative;
    z-index: 1;
    /* continue gradient border on sides + bottom */
    border-left: 3px solid transparent;
    border-right: 3px solid transparent;
    border-bottom: 3px solid transparent;
    background-clip: padding-box;
}
.ai-summary-body::before {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: 0 0 26px 26px;
    padding: 0 3px 3px 3px;
    background: linear-gradient(135deg, #ff6ec4, #7873f5, #42e695, #f7971e);
    background-size: 300% 300%;
    animation: gradientShift 6s ease infinite;
    -webkit-mask: linear-gradient(#fff 0 0) content-box,
                  linear-gradient(#fff 0 0);
    -webkit-mask-composite: destination-out;
    mask-composite: exclude;
    z-index: -1;
}

/* Stats grid */
.ai-stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin-bottom: 20px;
}

.ai-stat-chip {
    background: linear-gradient(135deg, rgba(120,115,245,0.07), rgba(255,110,196,0.07));
    border: 1.5px solid rgba(120,115,245,0.18);
    border-radius: 16px;
    padding: 14px 16px;
    text-align: center;
}

.ai-stat-chip-label {
    font-size: 11px;
    font-weight: 700;
    color: #7873f5;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    margin-bottom: 5px;
}

.ai-stat-chip-value {
    font-size: 22px;
    font-weight: 900;
    background: linear-gradient(90deg, #7873f5, #ff6ec4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.ai-stat-chip-sub {
    font-size: 11px;
    color: #999;
    margin-top: 2px;
}

/* Badge */
.ai-badge-new {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 8px 20px;
    border-radius: 999px;
    font-weight: 700;
    font-size: 14px;
    margin-bottom: 18px;
    background: linear-gradient(90deg, #ff6ec4, #7873f5);
    color: white;
    box-shadow: 0 4px 16px rgba(120,115,245,0.3);
}

/* Insight section */
.ai-insight-block {
    background: linear-gradient(135deg, rgba(120,115,245,0.04), rgba(66,230,149,0.04));
    border-left: 4px solid;
    border-image: linear-gradient(180deg, #7873f5, #42e695) 1;
    border-radius: 0 12px 12px 0;
    padding: 14px 18px;
    margin-bottom: 12px;
    font-size: 15px;
    line-height: 1.75;
    color: #1a1a1a;
}

/* ---- CHART CONTROLS CARD ---- */
.chart-controls-wrapper {
    position: relative;
    margin: 36px 0 0 0;
    border-radius: 28px !important;
    padding: 3px;
    background: linear-gradient(135deg, #42e695, #7873f5, #ff6ec4, #f7971e);
    background-size: 300% 300%;
    animation: gradientShift 6s ease infinite;
    box-shadow: 0 20px 60px rgba(66,230,149,0.25);
    overflow: hidden;
}

.chart-controls-inner {
    background: rgba(255,255,255,0.97);
    border-radius: 26px !important;
    padding: 28px 32px 28px 32px;
    backdrop-filter: blur(20px);
    overflow: hidden;
}

.chart-controls-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 14px;
}

.chart-controls-title {
    font-size: 28px;
    font-weight: 900;
    background: linear-gradient(90deg, #42e695, #7873f5, #ff6ec4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 0.5px;
}

.chart-controls-pill {
    display: inline-block;
    padding: 5px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    color: white;
    background: linear-gradient(90deg, #42e695, #7873f5);
    box-shadow: 0 4px 14px rgba(66,230,149,0.4);
}

.chart-controls-divider {
    height: 3px;
    border-radius: 2px;
    background: linear-gradient(90deg, #42e695, #7873f5, #ff6ec4, #f7971e);
    margin-bottom: 24px;
    background-size: 200% 200%;
    animation: gradientShift 4s ease infinite;
}

.widget-row-label {
    font-size: 13px;
    font-weight: 700;
    color: #7873f5;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    margin-bottom: 6px;
}

/* Polish widgets sitting inside the controls card */
.chart-controls-inner [data-testid="stMultiSelect"] > div,
.chart-controls-inner [data-baseweb="select"] > div {
    border-radius: 14px !important;
    border: 1.5px solid rgba(120,115,245,0.3) !important;
    background: rgba(120,115,245,0.04) !important;
    transition: border-color 0.25s, box-shadow 0.25s !important;
}

.chart-controls-inner [data-testid="stMultiSelect"] > div:focus-within,
.chart-controls-inner [data-baseweb="select"] > div:focus-within {
    border-color: #7873f5 !important;
    box-shadow: 0 0 0 3px rgba(120,115,245,0.15) !important;
}

/* Widget section separator inside card */
.widget-separator {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(120,115,245,0.2), transparent);
    margin: 20px 0;
}

/* ---- CHART DISPLAY CARD ---- */
.chart-display-wrapper {
    position: relative;
    margin: 28px 0 0 0;
    border-radius: 28px;
    padding: 3px;
    background: linear-gradient(135deg, #12c2e9, #7873f5, #ff6ec4, #42e695);
    background-size: 300% 300%;
    animation: gradientShift 8s ease infinite;
    box-shadow: 0 25px 70px rgba(18,194,233,0.28);
}

.chart-display-inner {
    background: rgba(255,255,255,0.98);
    border-radius: 26px;
    padding: 28px 32px 24px 32px;
    backdrop-filter: blur(20px);
    position: relative;
    overflow: hidden;
}

/* Decorative glow orbs behind the chart */
.chart-display-inner::before {
    content: "";
    position: absolute;
    width: 300px;
    height: 300px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(120,115,245,0.08) 0%, transparent 70%);
    top: -80px;
    right: -80px;
    pointer-events: none;
}

.chart-display-inner::after {
    content: "";
    position: absolute;
    width: 220px;
    height: 220px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(66,230,149,0.08) 0%, transparent 70%);
    bottom: -60px;
    left: -60px;
    pointer-events: none;
}

.chart-display-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 14px;
}

.chart-display-title {
    font-size: 28px;
    font-weight: 900;
    background: linear-gradient(90deg, #12c2e9, #7873f5, #ff6ec4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 0.5px;
}

.chart-type-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 7px 18px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    color: white;
    background: linear-gradient(90deg, #12c2e9, #7873f5);
    box-shadow: 0 4px 18px rgba(18,194,233,0.4);
    white-space: nowrap;
}

.chart-display-divider {
    height: 3px;
    border-radius: 2px;
    background: linear-gradient(90deg, #12c2e9, #7873f5, #ff6ec4, #42e695);
    margin-bottom: 18px;
    background-size: 200% 200%;
    animation: gradientShift 4s ease infinite;
}

.chart-meta-strip {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 18px;
}

.chart-meta-chip {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 5px 14px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
    border: 1.5px solid rgba(120,115,245,0.25);
    color: #7873f5;
    background: rgba(120,115,245,0.06);
}

/* Plotly chart container polish */
[data-testid="stPlotlyChart"] {
    border-radius: 18px !important;
    overflow: hidden !important;
    box-shadow: 0 6px 24px rgba(120,115,245,0.10) !important;
}

/* ---- FILE UPLOAD CARD ---- */
.upload-wrapper {
    position: relative;
    margin: 30px 0 10px 0;
    border-radius: 28px;
    padding: 3px;
    background: linear-gradient(135deg, #ff6ec4, #7873f5, #42e695, #f7971e);
    background-size: 300% 300%;
    animation: gradientShift 6s ease infinite;
    box-shadow: 0 20px 60px rgba(120,115,245,0.3);
}

.upload-inner {
    background: rgba(255,255,255,0.97);
    border-radius: 26px;
    padding: 28px 32px 20px 32px;
    backdrop-filter: blur(20px);
}

.upload-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 14px;
}

.upload-title {
    font-size: 28px;
    font-weight: 900;
    background: linear-gradient(90deg, #ff6ec4, #7873f5, #42e695);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 0.5px;
}

.upload-pill {
    display: inline-block;
    padding: 5px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    color: white;
    background: linear-gradient(90deg, #ff6ec4, #7873f5);
    box-shadow: 0 4px 14px rgba(255,110,196,0.35);
}

.upload-divider {
    height: 3px;
    border-radius: 2px;
    background: linear-gradient(90deg, #ff6ec4, #7873f5, #42e695, #f7971e);
    margin-bottom: 20px;
    background-size: 200% 200%;
    animation: gradientShift 4s ease infinite;
}

/* Style the Streamlit file uploader inside our card */
[data-testid="stFileUploader"] {
    background: linear-gradient(135deg, rgba(120,115,245,0.05), rgba(255,110,196,0.05)) !important;
    border-radius: 18px !important;
    border: 2px dashed rgba(120,115,245,0.35) !important;
    padding: 10px !important;
    transition: border-color 0.3s ease, box-shadow 0.3s ease !important;
}

[data-testid="stFileUploader"]:hover {
    border-color: rgba(120,115,245,0.7) !important;
    box-shadow: 0 6px 24px rgba(120,115,245,0.15) !important;
}

[data-testid="stFileUploaderDropzone"] {
    background: transparent !important;
}

/* ---- DATA PREVIEW SECTION ---- */
.preview-wrapper {
    position: relative;
    margin-top: 30px;
    margin-bottom: 10px;
    border-radius: 28px;
    padding: 3px;
    background: linear-gradient(135deg, #ff6ec4, #7873f5, #42e695, #f7971e);
    background-size: 300% 300%;
    animation: gradientShift 6s ease infinite;
    box-shadow: 0 20px 60px rgba(120,115,245,0.3);
}

@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.preview-inner {
    background: rgba(255,255,255,0.97);
    border-radius: 26px;
    padding: 30px 32px;
    backdrop-filter: blur(20px);
}

.preview-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 20px;
}

.preview-title {
    font-size: 28px;
    font-weight: 900;
    background: linear-gradient(90deg, #ff6ec4, #7873f5, #42e695);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 0.5px;
}

.preview-pill {,98
    display: inline-block;
    padding: 5px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    color: white;
    background: linear-gradient(90deg, #7873f5, #42e695);
    box-shadow: 0 4px 14px rgba(120,115,245,0.35);
}

.preview-divider {
    height: 3px;
    border-radius: 2px;
    background: linear-gradient(90deg, #ff6ec4, #7873f5, #42e695, #f7971e);
    margin-bottom: 22px;
    background-size: 200% 200%;
    animation: gradientShift 4s ease infinite;
}

/* Style the dataframe container that Streamlit renders inside our wrapper */
.preview-inner [data-testid="stDataFrame"] {
    border-radius: 16px !important;
    overflow: hidden;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
st.markdown("""
<div class="hero-wrapper">
  <div class="hero-inner">
    <div class="hero-title">🚀 NextGen AI Data Visualizer</div>
    <div class="hero-subtitle">✨ Transform Simple Numbers Into Colourful Interactive Stories ✨</div>
    <div class="hero-divider"></div>
    <div class="hero-badge-strip">
      <span class="hero-badge hero-badge-green">⚡ Instant Insights</span>
      <span class="hero-badge hero-badge-purple">📊 Interactive Charts</span>
      <span class="hero-badge hero-badge-pink">🤖 AI Analysis</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------------- FILE UPLOAD ----------------
st.markdown("""
<div class="upload-wrapper">
  <div class="upload-inner">
    <div class="upload-header">
      <div class="upload-title">📂 Upload Your CSV File</div>
      <span class="upload-pill">CSV only</span>
    </div>
    <div class="upload-divider"></div>
  </div>
</div>
""", unsafe_allow_html=True)

file = st.file_uploader("", type=["csv"], label_visibility="collapsed")

if file:
    df = pd.read_csv(file)

    # ---- Gradient-wrapped Data Preview ----
    row_count = len(df)
    col_count = len(df.columns)

    st.markdown(f"""
    <div class="preview-wrapper">
      <div class="preview-inner">
        <div class="preview-header">
          <div class="preview-title">📊 Live Data Preview</div>
          <span class="preview-pill">{row_count} rows &middot; {col_count} cols</span>
        </div>
        <div class="preview-divider"></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Styled dataframe
    st.markdown("""
    <style>
    [data-testid="stDataFrame"] {
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 30px rgba(120,115,245,0.15);
        border: 1.5px solid rgba(120,115,245,0.18);
    }
    [data-testid="stDataFrame"] thead tr th {
        background: linear-gradient(90deg, #7873f5, #ff6ec4) !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 14px !important;
    }
    [data-testid="stDataFrame"] tbody tr:nth-child(even) {
        background: rgba(120,115,245,0.05) !important;
    }
    [data-testid="stDataFrame"] tbody tr:hover {
        background: rgba(120,115,245,0.12) !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True)

    numeric_cols = df.select_dtypes(include=['int64','float64']).columns
    string_cols  = df.select_dtypes(include=['object']).columns

    # Auto-detect the best label column (first string column, e.g. Name)
    label_col = string_cols[0] if len(string_cols) > 0 else None
    x_axis    = label_col if label_col else df.index

    if len(numeric_cols) > 0:

        # ---- Chart Controls Card: all widgets truly inside ----
        st.markdown("""
        <style>
        /* Identify and style the container that holds our card marker + widgets */
        div[data-testid="stVerticalBlock"]:has(> div > div > .cc-marker) {
            background: rgba(255,255,255,0.97) !important;
            border-radius: 0 0 25px 25px !important;
            padding: 0 26px 26px 26px !important;
            margin-top: -4px !important;
            position: relative !important;
            z-index: 2 !important;
            border-left:  3px solid #7873f5 !important;
            border-right: 3px solid #42e695 !important;
            border-bottom: 3px solid #ff6ec4 !important;
        }
        /* Widget labels */
        .cc-label {
            font-size: 12px;
            font-weight: 800;
            color: #7873f5;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-bottom: 4px;
            padding-top: 4px;
        }
        /* Styled dropdowns */
        [data-testid="stMultiSelect"] [data-baseweb="select"] > div,
        [data-testid="stSelectbox"] [data-baseweb="select"] > div {
            border-radius: 14px !important;
            border: 1.5px solid rgba(120,115,245,0.3) !important;
            background: rgba(120,115,245,0.04) !important;
            transition: border-color 0.2s, box-shadow 0.2s !important;
        }
        [data-testid="stMultiSelect"] [data-baseweb="select"] > div:focus-within,
        [data-testid="stSelectbox"] [data-baseweb="select"] > div:focus-within {
            border-color: #7873f5 !important;
            box-shadow: 0 0 0 3px rgba(120,115,245,0.14) !important;
        }
        </style>
        <div class="chart-controls-wrapper" style="border-radius:28px 28px 0 0; padding-bottom:0; margin-bottom:0;">
          <div class="chart-controls-inner" style="border-radius:26px 26px 0 0; padding-bottom:18px;">
            <div class="chart-controls-header">
              <div class="chart-controls-title">🎛️ Chart Configuration</div>
              <span class="chart-controls-pill">Customize Your View</span>
            </div>
            <div class="chart-controls-divider" style="margin-bottom:0;"></div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        with st.container():
            # Invisible marker so CSS :has() can target this container
            st.markdown('<div class="cc-marker" style="display:none;"></div>', unsafe_allow_html=True)

            col1, col2 = st.columns([1.2, 1], gap="large")
            with col1:
                st.markdown('<div class="cc-label">🎯 Data Columns</div>', unsafe_allow_html=True)
                selected_cols = st.multiselect(
                    "",
                    options=list(numeric_cols),
                    default=[numeric_cols[0]],
                    help="Select one or more columns to visualise side by side!",
                    label_visibility="collapsed"
                )
            with col2:
                st.markdown('<div class="cc-label">📈 Chart Style</div>', unsafe_allow_html=True)
                chart_type = st.selectbox(
                    "",
                    ["Bar Blast 💥", "Smooth Line 🌊", "Column Chart 📊"],
                    label_visibility="collapsed"
                )

        if not selected_cols:
            st.warning("⚠️ Please select at least one column to visualise.")
            st.stop()

        # For AI summary, use the first selected column
        selected_col = selected_cols[0]

        # Melt dataframe for multi-column plotting
        plot_df = df.copy()
        if label_col:
            id_col = label_col
        else:
            plot_df["_index"] = plot_df.index.astype(str)
            id_col = "_index"

        melted = plot_df[[id_col] + list(selected_cols)].melt(
            id_vars=id_col, var_name="Metric", value_name="Value"
        )

        # Gradient pairs matching card/widget theme colors exactly
        GRADIENT_PAIRS = [
            ("#42e695", "#7873f5"),   # green → purple  (hero card)
            ("#ff6ec4", "#f7971e"),   # pink  → orange  (upload card)
            ("#12c2e9", "#42e695"),   # cyan  → green   (chart display card)
            ("#7873f5", "#ff6ec4"),   # purple → pink   (ai summary card)
            ("#f7971e", "#12c2e9"),   # orange → cyan
            ("#42e695", "#ff6ec4"),   # green → pink
        ]
        # Primary colors matching widget theme for line charts & legend
        BRIGHT_COLORS = ["#42e695", "#ff6ec4", "#12c2e9", "#7873f5", "#f7971e", "#42e695"]

        unique_metrics = melted["Metric"].unique().tolist()

        # ---------------- CHARTS ----------------
        if chart_type == "Bar Blast 💥":
            fig = px.bar(
                melted,
                x=id_col,
                y="Value",
                color="Metric",
                barmode="group",
                color_discrete_sequence=BRIGHT_COLORS,
                title="🔥 Power Bar Chart"
            )
            # Apply gradient fills to each bar trace
            for i, trace in enumerate(fig.data):
                pair = GRADIENT_PAIRS[i % len(GRADIENT_PAIRS)]
                fig.data[i].marker.color = pair[0]
                fig.data[i].marker.pattern.fillmode = "replace"
                # Use fillgradient for bright gradient bars
                fig.data[i].marker.update(
                    color=pair[0],
                    line=dict(width=0),
                )
                fig.data[i].update(
                    marker=dict(
                        color=pair[0],
                        line=dict(width=0),
                        opacity=1.0,
                    )
                )
                # Plotly supports fillgradient via marker colorscale trick
                # Use a list of colors mapped per bar for a gradient feel
                n_bars = len(fig.data[i].x) if fig.data[i].x is not None else 1
                import numpy as np
                import plotly.colors as pc
                grad_colors = pc.sample_colorscale(
                    [[0, pair[0]], [1, pair[1]]],
                    [k / max(n_bars - 1, 1) for k in range(n_bars)]
                )
                fig.data[i].marker.color = grad_colors
                fig.data[i].marker.line.width = 0

        elif chart_type == "Smooth Line 🌊":
            fig = px.line(
                melted,
                x=id_col,
                y="Value",
                color="Metric",
                markers=True,
                line_shape="spline",
                color_discrete_sequence=BRIGHT_COLORS,
                title="📈 Smooth Trend Line"
            )
            # Make lines thicker and add fill-to-zero gradient effect
            for i, trace in enumerate(fig.data):
                pair = GRADIENT_PAIRS[i % len(GRADIENT_PAIRS)]
                fig.data[i].update(
                    line=dict(color=BRIGHT_COLORS[i % len(BRIGHT_COLORS)], width=4),
                    marker=dict(size=9, color=pair[1], line=dict(color="white", width=2)),
                    fill="tozeroy",
                    fillcolor=f"rgba({int(pair[0][1:3],16)},{int(pair[0][3:5],16)},{int(pair[0][5:7],16)},0.18)"
                )

        else:
            fig = px.bar(
                melted,
                x="Value",
                y=id_col,
                color="Metric",
                barmode="group",
                orientation='h',
                color_discrete_sequence=BRIGHT_COLORS,
                title="📊 Column Chart"
            )
            import numpy as np
            import plotly.colors as pc
            for i, trace in enumerate(fig.data):
                pair = GRADIENT_PAIRS[i % len(GRADIENT_PAIRS)]
                n_bars = len(fig.data[i].y) if fig.data[i].y is not None else 1
                grad_colors = pc.sample_colorscale(
                    [[0, pair[0]], [1, pair[1]]],
                    [k / max(n_bars - 1, 1) for k in range(n_bars)]
                )
                fig.data[i].marker.color = grad_colors
                fig.data[i].marker.line.width = 0

        fig.update_layout(
            template="plotly_white",
            title="",                     # hide default title — shown in card header
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=10, r=10, t=10, b=10),
            legend=dict(
                orientation="h",
                yanchor="bottom", y=1.02,
                xanchor="right", x=1,
                font=dict(size=13, color="#7873f5", family="sans-serif"),
                bgcolor="rgba(255,255,255,0.85)",
                bordercolor="rgba(120,115,245,0.35)",
                borderwidth=1.5
            ),
            xaxis=dict(
                showgrid=True,
                gridcolor="rgba(120,115,245,0.15)",
                zeroline=False,
                tickfont=dict(size=13, color="#7873f5", family="sans-serif"),
                title_font=dict(size=14, color="#42e695", family="sans-serif"),
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor="rgba(120,115,245,0.15)",
                zeroline=False,
                tickfont=dict(size=13, color="#7873f5", family="sans-serif"),
                title_font=dict(size=14, color="#ff6ec4", family="sans-serif"),
            ),
            hoverlabel=dict(
                bgcolor="white",
                bordercolor="rgba(120,115,245,0.4)",
                font_size=13,
                font_family="sans-serif"
            )
        )

        fig.update_traces(
            marker_line_width=0,
            opacity=1.0
        )

        # Chart type label for display card
        chart_icon_map = {
            "Bar Blast 💥": "💥 Bar Blast",
            "Smooth Line 🌊": "🌊 Smooth Line",
            "Column Chart 📊": "📊 Column Chart"
        }
        chart_label = chart_icon_map.get(chart_type, chart_type)
        col_label = " · ".join(selected_cols[:3]) + (" ..." if len(selected_cols) > 3 else "")

        # ---- Chart Display Card ----
        st.markdown(f"""
        <div class="chart-display-wrapper">
          <div class="chart-display-inner">
            <div class="chart-display-header">
              <div class="chart-display-title">📊 Interactive Chart</div>
              <span class="chart-type-badge">{chart_label}</span>
            </div>
            <div class="chart-display-divider"></div>
            <div class="chart-meta-strip">
              <span class="chart-meta-chip">📐 Columns: {col_label}</span>
              <span class="chart-meta-chip">🔢 Data Points: {len(df)}</span>
              <span class="chart-meta-chip">🎨 Multi-Color Series</span>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.plotly_chart(fig, use_container_width=True)

        # ---------------- AI SMART EXPLANATION (FIXED) ----------------
        with st.spinner("🤖 AI is analyzing your data..."):
            time.sleep(1.5)

        # Compute real stats
        series        = df[selected_col].dropna()
        avg           = series.mean()
        highest       = series.max()
        lowest        = series.min()
        total         = series.sum()
        count         = len(series)
        std_dev       = series.std()
        median        = series.median()
        range_val     = highest - lowest
        cv            = (std_dev / avg * 100) if avg != 0 else 0   # coefficient of variation

        # Index of the peak row (for context)
        peak_index    = series.idxmax()
        lowest_index  = series.idxmin()

        # --- Badge logic ---
        if cv > 50:
            badge = "⚡ Highly Volatile Data"
        elif highest > avg * 1.5:
            badge = "🚀 Strong Peak Detected"
        elif cv < 10:
            badge = "📊 Very Stable Data"
        elif series.is_monotonic_increasing:
            badge = "📈 Consistently Growing"
        elif series.is_monotonic_decreasing:
            badge = "📉 Consistently Declining"
        elif highest > avg * 1.1:
            badge = "📈 Growing Trend"
        else:
            badge = "⚖️ Balanced & Steady"

        # --- Dynamic description logic ---
        # Spread / volatility
        if cv > 50:
            spread_insight = (
                f"The data is <strong>highly volatile</strong> — values swing widely from "
                f"<strong>{lowest:.2f}</strong> all the way to <strong>{highest:.2f}</strong>, "
                f"a range of <strong>{range_val:.2f}</strong>. "
                f"This level of variation (CV: {cv:.1f}%) suggests irregular or unpredictable behaviour."
            )
        elif cv < 10:
            spread_insight = (
                f"The values are <strong>remarkably consistent</strong>, clustering tightly around the mean of "
                f"<strong>{avg:.2f}</strong> with very little deviation (CV: {cv:.1f}%). "
                f"This signals a stable, predictable pattern."
            )
        else:
            spread_insight = (
                f"Values show <strong>moderate variation</strong> (CV: {cv:.1f}%), ranging from "
                f"<strong>{lowest:.2f}</strong> to <strong>{highest:.2f}</strong> — "
                f"a spread of <strong>{range_val:.2f}</strong> across {count} data points."
            )

        # Trend direction
        if series.is_monotonic_increasing:
            trend_insight = "📈 The column shows a <strong>steady upward trend</strong> — every value is higher than the last, indicating consistent growth."
        elif series.is_monotonic_decreasing:
            trend_insight = "📉 The column shows a <strong>steady downward trend</strong> — values decline consistently from start to finish."
        else:
            # Check first-half vs second-half average
            mid = count // 2
            first_half_avg  = series.iloc[:mid].mean()
            second_half_avg = series.iloc[mid:].mean()
            if second_half_avg > first_half_avg * 1.05:
                trend_insight = f"📊 Values in the <strong>second half are higher</strong> on average ({second_half_avg:.2f}) than the first half ({first_half_avg:.2f}), suggesting a <strong>late-stage upswing</strong>."
            elif second_half_avg < first_half_avg * 0.95:
                trend_insight = f"📊 Values in the <strong>second half are lower</strong> on average ({second_half_avg:.2f}) than the first half ({first_half_avg:.2f}), suggesting a <strong>gradual slowdown</strong>."
            else:
                trend_insight = f"📊 No clear directional trend — the data <strong>fluctuates around the mean</strong> ({avg:.2f}) without a strong upward or downward movement."

        # Peak insight
        peak_insight = (
            f"🏆 The <strong>peak value of {highest:.2f}</strong> occurs at row <strong>{peak_index}</strong>, "
            f"which is <strong>{((highest - avg) / avg * 100):.1f}% above the average</strong>. "
            f"The lowest point ({lowest:.2f}) at row {lowest_index} sits "
            f"<strong>{((avg - lowest) / avg * 100):.1f}% below the average</strong>."
        )

        # Mean vs median
        if abs(avg - median) / (avg if avg != 0 else 1) > 0.1:
            skew_insight = (
                f"⚖️ The mean ({avg:.2f}) and median ({median:.2f}) differ noticeably, "
                f"hinting at <strong>{'right' if avg > median else 'left'}-skewed data</strong> — "
                f"a few {'high' if avg > median else 'low'} outliers are pulling the average."
            )
        else:
            skew_insight = (
                f"⚖️ The mean ({avg:.2f}) and median ({median:.2f}) are close together, "
                f"suggesting the data is <strong>evenly distributed</strong> without strong outliers."
            )

        # ---- AI Summary Card ----
        st.markdown(f"""
        <div class="ai-summary-wrapper">
          <div class="ai-summary-inner">
            <div class="ai-summary-header">
              <div class="ai-summary-title">🤖 AI Insight Engine</div>
              <span class="ai-summary-pill">✨ AI Summary</span>
            </div>
            <div class="ai-summary-divider"></div>
          </div>
        </div>
        <div class="ai-summary-body">

          <span class="ai-badge-new">{badge}</span>

          <div class="ai-stats-grid">
            <div class="ai-stat-chip">
              <div class="ai-stat-chip-label">📊 Average</div>
              <div class="ai-stat-chip-value">{avg:.2f}</div>
            </div>
            <div class="ai-stat-chip">
              <div class="ai-stat-chip-label">📍 Median</div>
              <div class="ai-stat-chip-value">{median:.2f}</div>
            </div>
            <div class="ai-stat-chip">
              <div class="ai-stat-chip-label">🔢 Total</div>
              <div class="ai-stat-chip-value">{total:.2f}</div>
              <div class="ai-stat-chip-sub">{count} rows</div>
            </div>
            <div class="ai-stat-chip">
              <div class="ai-stat-chip-label">🚀 Highest</div>
              <div class="ai-stat-chip-value">{highest:.2f}</div>
              <div class="ai-stat-chip-sub">row {peak_index}</div>
            </div>
            <div class="ai-stat-chip">
              <div class="ai-stat-chip-label">📉 Lowest</div>
              <div class="ai-stat-chip-value">{lowest:.2f}</div>
              <div class="ai-stat-chip-sub">row {lowest_index}</div>
            </div>
            <div class="ai-stat-chip">
              <div class="ai-stat-chip-label">📐 Std Dev</div>
              <div class="ai-stat-chip-value">{std_dev:.2f}</div>
              <div class="ai-stat-chip-sub">range {range_val:.2f}</div>
            </div>
          </div>

          <div class="ai-insight-block">{spread_insight}</div>
          <div class="ai-insight-block">{trend_insight}</div>
          <div class="ai-insight-block">{peak_insight}</div>
          <div class="ai-insight-block">{skew_insight}</div>

        </div>
        """, unsafe_allow_html=True)

    else:
        st.error("⚠ No numeric columns found in this file.")
