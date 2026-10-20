# Yuva Intern: Data Science Internship — Week 3 Deliverables
## Task: Python-Based Machine Learning Model Development and Evaluation Plan

This folder contains the complete deliverables for **Week 3** of the **Yuva Intern Data Science Internship**.

---

## 📁 Week 3 Deliverables Overview

| File Name | Format | Description |
| :--- | :---: | :--- |
| **`YuvaIntern_Week3_ML_Model_Development_Plan.docx`** | `.docx` | **Primary Deliverable:** Comprehensive, executive-grade Word document containing the step-by-step machine learning development plan, tables, and 5 embedded high-resolution figures. |
| **`Week3_ML_Model_Development_and_Evaluation_Plan.docx`** | `.docx` | Duplicate copy matching assignment naming convention. |
| **`YuvaIntern_Week3_ML_Model_Development_Plan.pdf`** | `.pdf` | **Companion PDF Deliverable (8 Pages):** High-resolution PDF generated directly via Microsoft Word. |
| **`Week3_ML_Model_Development_and_Evaluation_Plan.pdf`** | `.pdf` | Duplicate PDF copy for submission. |
| **`figures/`** | Directory | 5 publication-grade high-resolution (300 DPI) figures. |
| **`generate_diagrams.py`** | `.py` | Standalone Python script to generate all 5 Week 3 figures. |
| **`generate_week3_doc.py`** | `.py` | Python automation script to compile the formatted `.docx` deliverable. |

---

## 📊 Embedded Strategic Figures (300 DPI)

1. **`fig1_ml_development_lifecycle.png`**: End-to-End Machine Learning Model Development & Validation Lifecycle (Problem Definition $\to$ Feature Pipeline $\to$ Model Tournament $\to$ Bayesian HPO $\to$ Threshold Calibration $\to$ MLOps Serving $\to$ Continuous Drift Retraining).
2. **`fig2_model_selection_tournament.png`**: Evolutionary Model Selection Tournament & Benchmarking Matrix (Comparing Logistic Regression, Random Forest, CatBoost, LightGBM, and Champion Stacking Ensemble across PR-AUC, Latency, and Explainability).
3. **`fig3_hyperparameter_optuna_workflow.png`**: Bayesian Hyperparameter Optimization Framework via Optuna (TPE search algorithm, median pruner, and 100-trial convergence history curve reaching optimal PR-AUC = 0.864).
4. **`fig4_validation_strategy_timeline.png`**: Rigorous Temporal Cross-Validation vs Flawed Shuffled Splitting (Visual comparison highlighting fatal future-to-past data leakage in shuffled k-fold vs zero-leakage Purged Group TimeSeries Split).
5. **`fig5_ml_timeline_gantt.png`**: Week 3 Machine Learning Development Workload Allocation (**Allocating 32.5 Total Engineering Hours** across 6 Phases).

---

## 🛠️ How to Re-generate Deliverables

```bash
# Generate Week 3 diagrams
python Week-03/generate_diagrams.py

# Generate Week 3 Word documents
python Week-03/generate_week3_doc.py
```
