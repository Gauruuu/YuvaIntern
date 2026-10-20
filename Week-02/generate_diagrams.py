"""
Generate 5 publication-quality strategic diagrams for Week 2:
Exploratory Data Analysis (EDA) and Visualization Framework Design.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
import numpy as np
import os

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#CBD5E1'
plt.rcParams['axes.linewidth'] = 0.8

os.makedirs('Week-02/figures', exist_ok=True)

# ==============================================================================
# FIGURE 1: Systematic EDA Lifecycle & Operational Framework
# ==============================================================================
def create_fig1():
    fig, ax = plt.subplots(figsize=(14, 8.5), dpi=150)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')

    ax.text(7, 8.6, "Figure 1: Universal Exploratory Data Analysis (EDA) Lifecycle Framework",
            fontsize=15, fontweight='bold', ha='center', color='#0F172A')
    ax.text(7, 8.2, "A Systematic, Multi-Stage Pipeline for Empirical Data Auditing, Pattern Discovery & Feature Ideation",
            fontsize=11, fontstyle='italic', ha='center', color='#475569')

    stages = [
        {"num": "Phase 1", "title": "Data Ingestion &\nInitial Profiling",
         "items": ["• Shape, schema & types", "• Memory footprint audit", "• Duplicate identification", "• Head/Tail verification"],
         "color": "#1E3A8A", "accent": "#3B82F6", "x": 0.5, "y": 4.8, "w": 2.2, "h": 2.8},
        {"num": "Phase 2", "title": "Univariate\nDistribution Audit",
         "items": ["• Central tendency & spread", "• Skewness & kurtosis tests", "• Normality testing (K-S)", "• Categorical cardinalities"],
         "color": "#0D9488", "accent": "#14B8A6", "x": 3.2, "y": 4.8, "w": 2.2, "h": 2.8},
        {"num": "Phase 3", "title": "Bivariate & Cross-\nFeature Analysis",
         "items": ["• Pearson/Spearman matrices", "• ANOVA & Kruskal-Wallis", "• Contingency & Chi-Square", "• Scatter & Hexbin trends"],
         "color": "#4338CA", "accent": "#6366F1", "x": 5.9, "y": 4.8, "w": 2.2, "h": 2.8},
        {"num": "Phase 4", "title": "Multivariate &\nDimensionality",
         "items": ["• Multi-collinearity (VIF)", "• Dimensionality (PCA/UMAP)", "• Cluster tendency (Hopkins)", "• High-order interactions"],
         "color": "#B45309", "accent": "#F59E0B", "x": 8.6, "y": 4.8, "w": 2.2, "h": 2.8},
        {"num": "Phase 5", "title": "Data Quality &\nAnomaly Treatment",
         "items": ["• MCAR/MAR/MNAR diagnosis", "• KNN/MICE imputation", "• Tukey IQR Winsorization", "• Isolation Forest outliers"],
         "color": "#047857", "accent": "#10B981", "x": 11.3, "y": 4.8, "w": 2.2, "h": 2.8}
    ]

    for s in stages:
        card = patches.FancyBboxPatch(
            (s["x"], s["y"]), s["w"], s["h"],
            boxstyle="round,pad=0.1,rounding_size=0.15",
            linewidth=1.2, edgecolor=s["accent"], facecolor='#FFFFFF', zorder=2
        )
        ax.add_patch(card)

        hdr = patches.FancyBboxPatch(
            (s["x"], s["y"] + s["h"] - 0.8), s["w"], 0.8,
            boxstyle="round,pad=0.05,rounding_size=0.12",
            linewidth=0, facecolor=s["color"], zorder=3
        )
        ax.add_patch(hdr)

        ax.text(s["x"] + 0.2, s["y"] + s["h"] - 0.25, s["num"],
                fontsize=10.5, fontweight='bold', color='#93C5FD', zorder=4)
        ax.text(s["x"] + s["w"]/2, s["y"] + s["h"] - 0.52, s["title"],
                fontsize=9, fontweight='bold', color='#FFFFFF', ha='center', va='center', zorder=4)

        for i, item in enumerate(s["items"]):
            ax.text(s["x"] + 0.15, s["y"] + s["h"] - 1.15 - (i * 0.35), item,
                    fontsize=8.2, color='#334155', zorder=4)

    # Horizontal flow arrows
    for i in range(len(stages) - 1):
        x_start = stages[i]["x"] + stages[i]["w"] + 0.05
        x_end = stages[i+1]["x"] - 0.05
        y_pos = 6.2
        ax.annotate('', xy=(x_end, y_pos), xytext=(x_start, y_pos),
                    arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.4",
                                    color="#0284C7", lw=2.5, zorder=5))

    # Synthesis Banner below
    synth_banner = patches.FancyBboxPatch(
        (0.5, 0.8), 13.0, 3.2,
        boxstyle="round,pad=0.1,rounding_size=0.15",
        linewidth=1, edgecolor='#94A3B8', facecolor='#F1F5F9', zorder=1
    )
    ax.add_patch(synth_banner)

    ax.text(7, 3.65, "SYNTHESIS: EXPLORATORY OUTPUTS & ARTIFACTS GOVERNANCE",
            fontsize=11, fontweight='bold', color='#1E293B', ha='center')

    # 3 Synthesis cards
    synth_cards = [
        {"x": 1.0, "w": 3.6, "title": "Data Quality Dossier", "desc": "• Complete missingness matrix\n• Outlier severity score index\n• Type-casting specification\n• Cleaning transformation code"},
        {"x": 5.2, "w": 3.6, "title": "Feature Hypothesis Matrix", "desc": "• Top non-linear interaction pairs\n• Recommended polynomial terms\n• Domain binning thresholds\n• High-leverage target predictors"},
        {"x": 9.4, "w": 3.6, "title": "Executive Storytelling Deck", "desc": "• Interactive Plotly dashboards\n• Strategic business trend charts\n• Risk-adjusted anomaly insights\n• Model readiness certification"}
    ]

    for c in synth_cards:
        c_box = patches.FancyBboxPatch(
            (c["x"], 1.1), c["w"], 2.2,
            boxstyle="round,pad=0.08,rounding_size=0.1",
            linewidth=0.8, edgecolor='#CBD5E1', facecolor='#FFFFFF', zorder=2
        )
        ax.add_patch(c_box)
        ax.text(c["x"] + c["w"]/2, 3.0, c["title"], fontsize=9.5, fontweight='bold', color='#1E3A8A', ha='center', zorder=3)
        ax.text(c["x"] + 0.2, 2.0, c["desc"], fontsize=8.2, color='#475569', va='center', zorder=3)

    # Arrows pointing down from Phase cards to Synthesis
    for s in [stages[0], stages[2], stages[4]]:
        ax.annotate('', xy=(s["x"] + s["w"]/2, 4.0), xytext=(s["x"] + s["w"]/2, 4.8),
                    arrowprops=dict(arrowstyle="->,head_width=0.25,head_length=0.35",
                                    color="#64748B", lw=1.8, linestyle=':', zorder=5))

    plt.tight_layout()
    plt.savefig('Week-02/figures/fig1_eda_lifecycle_framework.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Week 2 Fig 1 generated.")

# ==============================================================================
# FIGURE 2: Missing Data Diagnosis & Imputation Decision Architecture
# ==============================================================================
def create_fig2():
    fig, ax = plt.subplots(figsize=(13, 8.5), dpi=150)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 9)
    ax.axis('off')

    ax.text(6.5, 8.6, "Figure 2: Missing Data Diagnostic & Imputation Decision Architecture",
            fontsize=14.5, fontweight='bold', ha='center', color='#0F172A')
    ax.text(6.5, 8.2, "Algorithmic Decision Tree for Identifying Missingness Mechanisms and Selecting Optimal Treatment",
            fontsize=10.5, fontstyle='italic', ha='center', color='#475569')

    # Top Root: Missing Data Detected
    root = patches.FancyBboxPatch(
        (4.5, 7.0), 4.0, 0.9,
        boxstyle="round,pad=0.08,rounding_size=0.12",
        linewidth=1.5, edgecolor='#1E3A8A', facecolor='#1E3A8A', zorder=2
    )
    ax.add_patch(root)
    ax.text(6.5, 7.45, "Missing Values Detected in Feature Set\n(Audit Null Percentage & Missingness Matrix)",
            fontsize=9.5, fontweight='bold', color='#FFFFFF', ha='center', va='center', zorder=3)

    # 3 Mechanism Branches
    mechanisms = [
        {"name": "MCAR\n(Missing Completely at Random)",
         "desc": "P(Missing) is independent of observed\nand unobserved data.\nLittle's MCAR Test: p > 0.05",
         "x": 0.8, "y": 4.8, "w": 3.4, "h": 1.4, "color": "#0D9488"},
        {"name": "MAR\n(Missing at Random)",
         "desc": "P(Missing) depends on observed\nfeatures, but not on missing value itself.\nPredictable via logistic regression.",
         "x": 4.8, "y": 4.8, "w": 3.4, "h": 1.4, "color": "#2563EB"},
        {"name": "MNAR\n(Missing Not at Random)",
         "desc": "P(Missing) depends on unobserved\nlatent factors or the value itself.\n(e.g., high earners withholding income).",
         "x": 8.8, "y": 4.8, "w": 3.4, "h": 1.4, "color": "#D97706"}
    ]

    for m in mechanisms:
        box = patches.FancyBboxPatch(
            (m["x"], m["y"]), m["w"], m["h"],
            boxstyle="round,pad=0.08,rounding_size=0.1",
            linewidth=1.2, edgecolor=m["color"], facecolor='#FFFFFF', zorder=2
        )
        ax.add_patch(box)
        hdr = patches.FancyBboxPatch(
            (m["x"], m["y"] + m["h"] - 0.45), m["w"], 0.45,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            linewidth=0, facecolor=m["color"], zorder=3
        )
        ax.add_patch(hdr)
        ax.text(m["x"] + m["w"]/2, m["y"] + m["h"] - 0.22, m["name"].split('\n')[0],
                fontsize=9, fontweight='bold', color='#FFFFFF', ha='center', va='center', zorder=4)
        ax.text(m["x"] + m["w"]/2, m["y"] + 0.45, m["desc"],
                fontsize=7.8, color='#334155', ha='center', va='center', zorder=4)

    # Connect root to mechanisms
    ax.annotate('', xy=(2.5, 6.2), xytext=(5.5, 7.0),
                arrowprops=dict(arrowstyle="->,head_width=0.25,head_length=0.35", color="#1E3A8A", lw=1.8))
    ax.annotate('', xy=(6.5, 6.2), xytext=(6.5, 7.0),
                arrowprops=dict(arrowstyle="->,head_width=0.25,head_length=0.35", color="#1E3A8A", lw=1.8))
    ax.annotate('', xy=(10.5, 6.2), xytext=(7.5, 7.0),
                arrowprops=dict(arrowstyle="->,head_width=0.25,head_length=0.35", color="#1E3A8A", lw=1.8))

    # Treatment Decisions below each branch
    treatments = [
        {"x": 0.8, "y": 1.5, "w": 3.4, "h": 2.6, "title": "MCAR Treatment Strategy",
         "items": ["• Nulls < 3%: Listwise deletion\n  (Complete Case Analysis - CCA)",
                   "• Nulls 3-15%: Median (numerical)\n  or Mode (categorical) imputation",
                   "• Fast baseline for non-critical\n  operational covariates",
                   "• Verify variance preservation\n  via Kolmogorov-Smirnov test"]},
        {"x": 4.8, "y": 1.5, "w": 3.4, "h": 2.6, "title": "MAR Treatment Strategy",
         "items": ["• K-Nearest Neighbors (KNNImputer)\n  with distance weighting (k=5)",
                   "• Multivariate Imputation by Chained\n  Equations (MICE / IterativeImputer)",
                   "• Random Forest MissForest\n  algorithm for mixed tabular types",
                   "• Preserves multi-feature\n  covariance and correlation structures"]},
        {"x": 8.8, "y": 1.5, "w": 3.4, "h": 2.6, "title": "MNAR Treatment Strategy",
         "items": ["• Create explicit binary indicator\n  feature: is_missing_flag = True",
                   "• Explicit 'Unknown/Missing' category\n  token for categorical fields",
                   "• Pattern-mixture modeling or\n  domain-expert heuristic rules",
                   "• Treat missingness as informative\n  behavioral signal for ML"]}
    ]

    for t in treatments:
        box = patches.FancyBboxPatch(
            (t["x"], t["y"]), t["w"], t["h"],
            boxstyle="round,pad=0.08,rounding_size=0.1",
            linewidth=1.2, edgecolor='#94A3B8', facecolor='#F8FAFC', zorder=2
        )
        ax.add_patch(box)
        hdr = patches.FancyBboxPatch(
            (t["x"], t["y"] + t["h"] - 0.45), t["w"], 0.45,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            linewidth=0, facecolor='#1E293B', zorder=3
        )
        ax.add_patch(hdr)
        ax.text(t["x"] + t["w"]/2, t["y"] + t["h"] - 0.22, t["title"],
                fontsize=9, fontweight='bold', color='#FFFFFF', ha='center', va='center', zorder=4)

        for i, item in enumerate(t["items"]):
            ax.text(t["x"] + 0.15, t["y"] + t["h"] - 0.85 - (i * 0.45), item,
                    fontsize=8.0, color='#1E293B', zorder=4)

    # Connect mechanisms to treatments
    for m, t in zip(mechanisms, treatments):
        ax.annotate('', xy=(t["x"] + t["w"]/2, 4.1), xytext=(m["x"] + m["w"]/2, 4.8),
                    arrowprops=dict(arrowstyle="->,head_width=0.25,head_length=0.35", color=m["color"], lw=1.8))

    # Bottom summary alert
    btm_alert = patches.FancyBboxPatch(
        (2.0, 0.4), 9.0, 0.75,
        boxstyle="round,pad=0.05,rounding_size=0.1",
        linewidth=1, edgecolor='#10B981', facecolor='#ECFDF5', zorder=2
    )
    ax.add_patch(btm_alert)
    ax.text(6.5, 0.77, "✦ GOLDEN RULE OF PREPROCESSING: Fit Imputers STRICTLY on Training Folds",
            fontsize=9.5, fontweight='bold', color='#065F46', ha='center')
    ax.text(6.5, 0.55, "Never fit imputers on the entire dataset to prevent data leakage and target contamination.",
            fontsize=8.2, color='#047857', ha='center')

    plt.tight_layout()
    plt.savefig('Week-02/figures/fig2_missing_data_decision_tree.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Week 2 Fig 2 generated.")

# ==============================================================================
# FIGURE 3: Multi-Panel Exploratory Visual Showcase
# ==============================================================================
def create_fig3():
    fig = plt.figure(figsize=(14, 8.5), dpi=150)
    fig.patch.set_facecolor('#FFFFFF')

    # 4 Subplots (2x2 grid)
    gs = fig.add_gridspec(2, 2, hspace=0.32, wspace=0.25, left=0.07, right=0.95, top=0.90, bottom=0.08)

    # Subplot A: Histogram + KDE Distribution
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.set_facecolor('#F8FAFC')
    np.random.seed(42)
    # Mixture of two normals representing bimodal customer activity
    data_a = np.concatenate([np.random.normal(25, 6, 600), np.random.normal(55, 12, 400)])
    ax1.hist(data_a, bins=30, density=True, color='#93C5FD', edgecolor='#1E3A8A', alpha=0.7, label='Histogram Density')
    # KDE estimation
    from scipy.stats import gaussian_kde
    kde = gaussian_kde(data_a)
    x_grid = np.linspace(5, 95, 200)
    ax1.plot(x_grid, kde(x_grid), color='#1E3A8A', lw=2.5, label='KDE Density Curve')
    ax1.axvline(np.mean(data_a), color='#DC2626', linestyle='--', lw=1.8, label=f'Mean ({np.mean(data_a):.1f})')
    ax1.axvline(np.median(data_a), color='#059669', linestyle=':', lw=1.8, label=f'Median ({np.median(data_a):.1f})')
    ax1.set_title("Panel A: Univariate Density & Skewness Audit\n(Histogram + Kernel Density Estimation)", fontsize=10.5, fontweight='bold', color='#0F172A')
    ax1.set_xlabel("Account Activity Index (Continuous Score)", fontsize=8.5, fontweight='bold')
    ax1.set_ylabel("Probability Density", fontsize=8.5, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=7.8, frameon=True, facecolor='#FFFFFF')
    ax1.grid(True, linestyle=':', alpha=0.5)

    # Subplot B: Categorical Box & Violin Plot
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_facecolor('#F8FAFC')
    tiers = ['Tier 1: Starter', 'Tier 2: Growth', 'Tier 3: Enterprise']
    data_tiers = [
        np.random.gamma(2, 4, 300),
        np.random.gamma(4, 5, 300),
        np.random.gamma(7, 6, 300)
    ]
    parts = ax2.violinplot(data_tiers, positions=[1, 2, 3], showmeans=False, showmedians=False, showextrema=False)
    for i, pc in enumerate(parts['bodies']):
        pc.set_facecolor(['#60A5FA', '#34D399', '#FBBF24'][i])
        pc.set_edgecolor('#1E293B')
        pc.set_alpha(0.65)
    # Overlay compact box plots
    bp = ax2.boxplot(data_tiers, positions=[1, 2, 3], widths=0.2, patch_artist=True,
                     boxprops=dict(facecolor='#FFFFFF', edgecolor='#0F172A', linewidth=1.2),
                     medianprops=dict(color='#DC2626', linewidth=2),
                     whiskerprops=dict(color='#0F172A', linewidth=1.2),
                     capprops=dict(color='#0F172A', linewidth=1.2),
                     flierprops=dict(marker='o', markersize=3, markerfacecolor='#DC2626', alpha=0.5))
    ax2.set_xticks([1, 2, 3])
    ax2.set_xticklabels(tiers, fontsize=8.5, fontweight='bold')
    ax2.set_title("Panel B: Bivariate Categorical vs Continuous Spread\n(Composite Violin & Interquartile Boxplot)", fontsize=10.5, fontweight='bold', color='#0F172A')
    ax2.set_ylabel("Monthly Platform Telemetry Events (k)", fontsize=8.5, fontweight='bold')
    ax2.grid(True, linestyle=':', alpha=0.5)

    # Subplot C: Correlation Matrix Heatmap
    ax3 = fig.add_subplot(gs[1, 0])
    features = ['Recency', 'Frequency', 'Monetary', 'Ticket_Vol', 'CSAT', 'Tenure']
    # Realistic correlation matrix
    corr = np.array([
        [ 1.00, -0.62, -0.45,  0.38, -0.52, -0.31],
        [-0.62,  1.00,  0.78, -0.29,  0.64,  0.55],
        [-0.45,  0.78,  1.00, -0.18,  0.49,  0.68],
        [ 0.38, -0.29, -0.18,  1.00, -0.71, -0.12],
        [-0.52,  0.64,  0.49, -0.71,  1.00,  0.34],
        [-0.31,  0.55,  0.68, -0.12,  0.34,  1.00]
    ])
    cmap = mpl.colormaps['coolwarm']
    im = ax3.imshow(corr, cmap=cmap, vmin=-1, vmax=1)
    ax3.set_xticks(np.arange(len(features)))
    ax3.set_yticks(np.arange(len(features)))
    ax3.set_xticklabels(features, fontsize=8, fontweight='bold', rotation=35, ha='right')
    ax3.set_yticklabels(features, fontsize=8, fontweight='bold')
    for i in range(len(features)):
        for j in range(len(features)):
            val = corr[i, j]
            text_col = '#FFFFFF' if abs(val) > 0.6 else '#0F172A'
            ax3.text(j, i, f"{val:+.2f}", ha='center', va='center', color=text_col, fontsize=7.5, fontweight='bold')
    plt.colorbar(im, ax=ax3, fraction=0.046, pad=0.04)
    ax3.set_title("Panel C: Multivariate Correlation Structure\n(Pearson Correlation Matrix with Colormap)", fontsize=10.5, fontweight='bold', color='#0F172A')

    # Subplot D: Bivariate Scatter Regression with Hexbin/Marginal
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.set_facecolor('#F8FAFC')
    x = np.random.normal(50, 15, 450)
    y = 0.65 * x + np.random.normal(15, 8, 450)
    hb = ax4.hexbin(x, y, gridsize=25, cmap='Blues', mincnt=1, alpha=0.8)
    # Regression line
    m, b = np.polyfit(x, y, 1)
    x_line = np.linspace(15, 85, 100)
    ax4.plot(x_line, m*x_line + b, color='#DC2626', lw=2.2, label=f'Trend Fit (r = 0.74, slope = {m:.2f})')
    ax4.set_title("Panel D: Relational Density & Trend Analysis\n(Hexagonal Binning Scatter & Linear Fit)", fontsize=10.5, fontweight='bold', color='#0F172A')
    ax4.set_xlabel("Weekly Active Usage Velocity (%)", fontsize=8.5, fontweight='bold')
    ax4.set_ylabel("Account Expansion Revenue ($k)", fontsize=8.5, fontweight='bold')
    ax4.legend(loc='upper left', fontsize=7.8, frameon=True, facecolor='#FFFFFF')
    ax4.grid(True, linestyle=':', alpha=0.5)

    fig.suptitle("Figure 3: Publication-Grade Exploratory Visualization Archetypes\nDemonstrating Univariate, Bivariate, Correlation & Relational Analysis Formats",
                 fontsize=13, fontweight='bold', color='#0F172A', y=0.98)

    plt.savefig('Week-02/figures/fig3_eda_visual_catalog_mockup.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Week 2 Fig 3 generated.")

# ==============================================================================
# FIGURE 4: Outlier Detection & Anomaly Treatment Taxonomy
# ==============================================================================
def create_fig4():
    fig, ax = plt.subplots(figsize=(13, 8), dpi=150)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    ax.text(6.5, 8.1, "Figure 4: Comprehensive Outlier Detection & Treatment Taxonomy",
            fontsize=14.5, fontweight='bold', ha='center', color='#0F172A')
    ax.text(6.5, 7.7, "Comparing Statistical Thresholding, Proximity Models & Domain Mitigation Strategies",
            fontsize=10.5, fontstyle='italic', ha='center', color='#475569')

    # 3 Main Pillars
    pillars = [
        {
            "title": "1. Parametric & Statistical",
            "subtitle": "Univariate / Gaussian Assumptions",
            "color": "#1E3A8A", "x": 0.6, "y": 2.2, "w": 3.6, "h": 5.0,
            "methods": [
                "• Z-Score Thresholding:\n  Flag if |Z| > 3.0 standard deviations.\n  Requires Gaussian normality.",
                "• Modified Z-Score (MAD):\n  Utilizes Median Absolute Deviation.\n  Resistant to extreme masking.",
                "• Tukey's IQR Fences:\n  Inner Fences: Q1 - 1.5*IQR, Q3 + 1.5*IQR.\n  Outer Fences: Q1 - 3.0*IQR, Q3 + 3.0*IQR.\n  Non-parametric & distribution-agnostic."
            ]
        },
        {
            "title": "2. Proximity & Machine Learning",
            "subtitle": "Multivariate / Non-Linear Anomaly",
            "color": "#0D9488", "x": 4.7, "y": 2.2, "w": 3.6, "h": 5.0,
            "methods": [
                "• Isolation Forest (iForest):\n  Isolates anomalies by random partitioning.\n  Few splits = anomalous data points.\n  Scales linearly: O(n*t*psi).",
                "• Local Outlier Factor (LOF):\n  Measures local density relative to k-NN.\n  Identifies density-based outliers.",
                "• Mahalanobis Distance:\n  Accounts for covariance across dimensions.\n  Detects multivariate joint outliers."
            ]
        },
        {
            "title": "3. Domain Treatment Strategies",
            "subtitle": "Preserving Information & ML Stability",
            "color": "#7C3AED", "x": 8.8, "y": 2.2, "w": 3.6, "h": 5.0,
            "methods": [
                "• Spatial Winsorization:\n  Cap extreme values at 1st / 99th pct.\n  Preserves sample size without skew.",
                "• Power & Log Transformations:\n  Box-Cox / Yeo-Johnson transforms.\n  Compresses right-skewed fat tails.",
                "• Stratified Cohort Isolation:\n  Split VIP / Whale accounts into dedicated\n  sub-models rather than dropping them."
            ]
        }
    ]

    for p in pillars:
        box = patches.FancyBboxPatch(
            (p["x"], p["y"]), p["w"], p["h"],
            boxstyle="round,pad=0.1,rounding_size=0.15",
            linewidth=1.2, edgecolor=p["color"], facecolor='#FFFFFF', zorder=2
        )
        ax.add_patch(box)

        hdr = patches.FancyBboxPatch(
            (p["x"], p["y"] + p["h"] - 0.85), p["w"], 0.85,
            boxstyle="round,pad=0.03,rounding_size=0.12",
            linewidth=0, facecolor=p["color"], zorder=3
        )
        ax.add_patch(hdr)

        ax.text(p["x"] + p["w"]/2, p["y"] + p["h"] - 0.32, p["title"],
                fontsize=10, fontweight='bold', color='#FFFFFF', ha='center', zorder=4)
        ax.text(p["x"] + p["w"]/2, p["y"] + p["h"] - 0.62, p["subtitle"],
                fontsize=8, fontstyle='italic', color='#E0E7FF', ha='center', zorder=4)

        for i, m in enumerate(p["methods"]):
            ax.text(p["x"] + 0.2, p["y"] + p["h"] - 1.25 - (i * 1.25), m,
                    fontsize=8.0, color='#1E293B', zorder=4)

    # Bottom Decision Banner
    btm = patches.FancyBboxPatch(
        (0.6, 0.6), 11.8, 1.2,
        boxstyle="round,pad=0.08,rounding_size=0.1",
        linewidth=1, edgecolor='#CBD5E1', facecolor='#F1F5F9', zorder=2
    )
    ax.add_patch(btm)
    ax.text(6.5, 1.35, "EXECUTIVE OUTLIER POLICY: True Data Errors vs. Genuine Extreme Events",
            fontsize=10, fontweight='bold', color='#1E293B', ha='center')
    ax.text(6.5, 0.95, "Never blindly delete outliers. If extreme values represent high-value enterprise events (e.g. VIP clients),\napply Winsorization or robust loss functions (Huber Loss) to maintain business reality without destabilizing gradients.",
            fontsize=8.2, color='#475569', ha='center')

    plt.tight_layout()
    plt.savefig('Week-02/figures/fig4_outlier_detection_taxonomy.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Week 2 Fig 4 generated.")

# ==============================================================================
# FIGURE 5: EDA Timeline & Gantt Workload Distribution (32.5 Hours)
# ==============================================================================
def create_fig5():
    fig, ax = plt.subplots(figsize=(13, 7.5), dpi=150)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')

    tasks = [
        "Phase 1: Ingestion, Schema Auditing & Memory Profiling",
        "Phase 2: Univariate Statistical Testing & Normality Audits",
        "Phase 3: Bivariate Correlation & Cross-Tabulation Matrix",
        "Phase 4: Multivariate Dimensionality & Interaction Analysis",
        "Phase 5: Missing Data & Anomaly Engine Implementation",
        "Phase 6: Reporting Framework & Executive Visualization Deck"
    ]

    start_hours = [0.0, 4.0, 9.5, 16.0, 22.5, 28.0]
    durations   = [4.0, 5.5, 6.5,  6.5,  5.5,  4.5]
    colors = ['#1E3A8A', '#0D9488', '#2563EB', '#7C3AED', '#D97706', '#059669']

    y_pos = np.arange(len(tasks))

    for i, (task, start, dur, col) in enumerate(zip(tasks, start_hours, durations, colors)):
        ax.barh(i, dur, left=start, height=0.55, align='center',
                color=col, edgecolor='#0F172A', linewidth=0.8, alpha=0.9, zorder=3)
        ax.text(start + dur/2, i, f"{dur:.1f} hrs",
                ha='center', va='center', color='#FFFFFF', fontweight='bold', fontsize=9, zorder=4)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(tasks, fontsize=9.5, fontweight='bold', color='#1E293B')
    ax.invert_yaxis()

    ax.set_xlabel("Cumulative Project Workload Hours (Allocated Budget: 30 - 35 Hours)",
                  fontsize=10.5, fontweight='bold', color='#0F172A', labelpad=12)
    ax.set_xlim(0, 36)
    ax.set_xticks(np.arange(0, 37, 2))
    ax.grid(axis='x', linestyle='--', alpha=0.5, color='#94A3B8', zorder=1)

    ax.axvline(32.5, color='#DC2626', linestyle='-', linewidth=2, zorder=2)
    ax.text(32.7, 5.2, "Complete EDA Plan Delivery\n(32.5 Hours Total)", color='#DC2626',
            fontweight='bold', fontsize=9.5, va='center')

    ax.axvspan(30, 35, color='#FEF3C7', alpha=0.4, zorder=0, label="Target Window (30-35 hrs)")

    plt.title("Figure 5: Week 2 EDA & Visualization Framework Workload Allocation\nBudgeting Exactly 32.5 Total Engineering Hours Across 6 Systematic Execution Phases",
              fontsize=13, fontweight='bold', color='#0F172A', pad=18)

    ax.legend(loc='lower right', frameon=True, facecolor='#FFFFFF', edgecolor='#CBD5E1', fontsize=9)

    plt.tight_layout()
    plt.savefig('Week-02/figures/fig5_eda_timeline_gantt.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Week 2 Fig 5 generated.")

if __name__ == '__main__':
    create_fig1()
    create_fig2()
    create_fig3()
    create_fig4()
    create_fig5()
    print("All 5 Week-02 figures generated successfully.")
