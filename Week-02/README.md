# Yuva Intern: Data Science Internship — Week 2 Deliverables
## Task: Exploratory Data Analysis (EDA) and Visualization Framework Design

This folder contains the complete deliverables for **Week 2** of the **Yuva Intern Data Science Internship**.

---

## 📁 Week 2 Deliverables Overview

| File Name | Format | Description |
| :--- | :---: | :--- |
| **`YuvaIntern_Week2_EDA_Visualization_Framework.docx`** | `.docx` | **Primary Deliverable:** Comprehensive, executive-grade Word document containing the full EDA and visualization framework, tables, and 5 embedded high-resolution figures. |
| **`Week2_EDA_and_Visualization_Framework_Design.docx`** | `.docx` | Duplicate copy matching assignment naming convention. |
| **`YuvaIntern_Week2_EDA_Visualization_Framework.pdf`** | `.pdf` | **Companion PDF Deliverable (10 Pages):** High-resolution PDF generated directly via Microsoft Word. |
| **`Week2_EDA_and_Visualization_Framework_Design.pdf`** | `.pdf` | Duplicate PDF copy for submission. |
| **`figures/`** | Directory | 5 publication-grade high-resolution (300 DPI) figures. |
| **`generate_diagrams.py`** | `.py` | Standalone Python script to generate all 5 Week 2 figures. |
| **`generate_week2_doc.py`** | `.py` | Python automation script to compile the formatted `.docx` deliverable. |

---

## 📊 Embedded Strategic Figures (300 DPI)

1. **`fig1_eda_lifecycle_framework.png`**: Universal Exploratory Data Analysis (EDA) Lifecycle Framework (Ingestion $\to$ Profiling $\to$ Univariate $\to$ Bivariate $\to$ Multivariate $\to$ Quality/Anomalies $\to$ Synthesis Dossier).
2. **`fig2_missing_data_decision_tree.png`**: Missing Data Diagnostic & Imputation Decision Architecture (MCAR, MAR, MNAR detection and optimal statistical/ML treatment algorithms).
3. **`fig3_eda_visual_catalog_mockup.png`**: Publication-Grade Exploratory Visualization Archetypes (Histogram+KDE density, Composite Violin-Boxplot, Correlation Heatmap, Hexbin Scatter Regression).
4. **`fig4_outlier_detection_taxonomy.png`**: Comprehensive Outlier Detection & Anomaly Treatment Taxonomy (Parametric Z/MAD, Tukey Fences, Isolation Forest, Spatial Winsorization).
5. **`fig5_eda_timeline_gantt.png`**: Week 2 EDA & Visualization Framework Workload Allocation (**Allocating 32.5 Total Engineering Hours** across 6 Phases).

---

## 🛠️ How to Re-generate Deliverables

```bash
# Generate Week 2 diagrams
python Week-02/generate_diagrams.py

# Generate Week 2 Word documents
python Week-02/generate_week2_doc.py
```
