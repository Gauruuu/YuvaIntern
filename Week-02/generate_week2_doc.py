"""
Builds the comprehensive, publication-grade Word document (.docx)
for Yuva Intern Week 2: Exploratory Data Analysis (EDA) and Visualization Framework Design.
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def build_week2_document():
    doc = Document()

    # Color palette
    COLOR_PRIMARY_HEX = "1E3A8A"      # Deep Navy
    COLOR_SECONDARY_HEX = "0D9488"    # Teal Accent
    COLOR_DARK_HEX = "0F172A"         # Slate Dark
    COLOR_TEXT_HEX = "1E293B"         # Dark Slate
    COLOR_LIGHT_BG_HEX = "F8FAFC"     # Background
    COLOR_BORDER_HEX = "CBD5E1"       # Subtle border
    COLOR_ACCENT_ROW_HEX = "F1F5F9"   # Alternate row
    COLOR_HEADER_BG_HEX = "1E3A8A"    # Header fill

    COLOR_PRIMARY = RGBColor(30, 58, 138)
    COLOR_SECONDARY = RGBColor(13, 148, 136)
    COLOR_DARK = RGBColor(15, 23, 42)
    COLOR_TEXT = RGBColor(30, 41, 59)
    COLOR_MUTED = RGBColor(100, 116, 139)

    # Margins (1 inch all around)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)

        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("YUVA INTERN: DATA SCIENCE INTERNSHIP  |  WEEK 2 EDA & VISUALIZATION BLUEPRINT")
        hrun.font.name = "Calibri"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = COLOR_MUTED

        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        frun1 = fp.add_run("Exploratory Data Analysis (EDA) & Enterprise Visualization Framework Design")
        frun1.font.name = "Calibri"
        frun1.font.size = Pt(8.5)
        frun1.font.color.rgb = COLOR_MUTED

    # Helpers
    def set_cell_background(cell, hex_color):
        tc_pr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
        tc_pr.append(shd)

    def set_cell_margins(cell, top=120, bottom=120, left=160, right=160):
        tc_pr = cell._tc.get_or_add_tcPr()
        tc_mar = parse_xml(
            f'<w:tcMar {nsdecls("w")}>'
            f'<w:top w:w="{top}" w:type="dxa"/>'
            f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
            f'<w:left w:w="{left}" w:type="dxa"/>'
            f'<w:right w:w="{right}" w:type="dxa"/>'
            f'</w:tcMar>'
        )
        tc_pr.append(tc_mar)

    def set_table_borders(table, color="CBD5E1", sz="4"):
        tbl_pr = table._tbl.tblPr
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:left w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'<w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideV w:val="none"/>'
            f'</w:tblBorders>'
        )
        tbl_pr.append(borders)

    def add_p(text, space_before=0, space_after=6, bold=False, italic=False, color=COLOR_TEXT, size=10, align=WD_ALIGN_PARAGRAPH.LEFT):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(text)
        run.bold = bold
        run.italic = italic
        run.font.name = "Calibri"
        run.font.size = Pt(size)
        run.font.color.rgb = color
        return p

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.name = "Calibri"
        run.font.size = Pt(16)
        run.font.color.rgb = COLOR_PRIMARY
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.name = "Calibri"
        run.font.size = Pt(12.5)
        run.font.color.rgb = RGBColor(37, 99, 235)
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.name = "Calibri"
        run.font.size = Pt(10.5)
        run.font.color.rgb = COLOR_DARK
        return p

    def add_callout(text, title="ANALYTICAL DIRECTIVE"):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        cell = tbl.cell(0, 0)
        cell.width = Inches(6.5)
        set_cell_background(cell, COLOR_LIGHT_BG_HEX)
        set_cell_margins(cell, top=140, bottom=140, left=240, right=200)

        tc_pr = cell._tc.get_or_add_tcPr()
        borders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>'
            f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{COLOR_PRIMARY_HEX}"/>'
            f'<w:top w:val="none"/>'
            f'<w:bottom w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'</w:tcBorders>'
        )
        tc_pr.append(borders)

        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
        run_t = p.add_run(f"✦ {title}: ")
        run_t.bold = True
        run_t.font.name = "Calibri"
        run_t.font.size = Pt(9.5)
        run_t.font.color.rgb = COLOR_PRIMARY

        run_body = p.add_run(text)
        run_body.italic = True
        run_body.font.name = "Calibri"
        run_body.font.size = Pt(9.5)
        run_body.font.color.rgb = COLOR_TEXT

        p_spacer = doc.add_paragraph()
        p_spacer.paragraph_format.space_after = Pt(4)

    def add_image_box(image_path, caption_title, caption_desc):
        if os.path.exists(image_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(10)
            p_img.paragraph_format.space_after = Pt(4)
            run = p_img.add_run()
            run.add_picture(image_path, width=Inches(6.4))

            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(0)
            p_cap.paragraph_format.space_after = Pt(12)
            r_title = p_cap.add_run(f"{caption_title} — ")
            r_title.bold = True
            r_title.font.name = "Calibri"
            r_title.font.size = Pt(9.0)
            r_title.font.color.rgb = COLOR_PRIMARY

            r_desc = p_cap.add_run(caption_desc)
            r_desc.italic = True
            r_desc.font.name = "Calibri"
            r_desc.font.size = Pt(8.5)
            r_desc.font.color.rgb = COLOR_MUTED

    # ==========================================================================
    # COVER / TITLE BLOCK
    # ==========================================================================
    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.space_before = Pt(10)
    p_meta.paragraph_format.space_after = Pt(2)
    r_org = p_meta.add_run("YUVA INTERN PROGRAM  •  DATA SCIENCE TRACK 2026")
    r_org.bold = True
    r_org.font.name = "Calibri"
    r_org.font.size = Pt(10.5)
    r_org.font.color.rgb = RGBColor(37, 99, 235)

    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(4)
    p_title.paragraph_format.space_after = Pt(6)
    r_title = p_title.add_run("Week 2 Deliverable: Exploratory Data Analysis (EDA) & Visualization Framework Design")
    r_title.bold = True
    r_title.font.name = "Calibri"
    r_title.font.size = Pt(22)
    r_title.font.color.rgb = COLOR_PRIMARY

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(14)
    r_sub = p_sub.add_run("A Universal Analytical Architecture for Empirical Data Auditing, Anomaly Diagnosis, Pattern Discovery & Statistical Storytelling\nMethodology, Data Typology, Imputation Engines, Visual Taxonomies & Reporting Blueprints")
    r_sub.italic = True
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(12)
    r_sub.font.color.rgb = COLOR_TEXT

    # Metadata Table
    meta_table = doc.add_table(rows=5, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False
    set_table_borders(meta_table, color="CBD5E1", sz="4")

    meta_data = [
        ("Document Identifier", "YUVA-DS-2026-W02-EDA-V1.0"),
        ("Project Domain & Focus", "Enterprise Exploratory Data Analysis (EDA) & Visualization Architecture"),
        ("Author & Role", "Data Science Intern (Yuva Internship Cohort)"),
        ("Target Workload Allocation", "32.5 Total Engineering Hours (Target: 30 - 35 Hours)"),
        ("Lifecycle Phase", "Week 2: Exploratory Intelligence, Data Quality Engineering & Visual Framework")
    ]

    for i, (k, v) in enumerate(meta_data):
        c0 = meta_table.cell(i, 0)
        c1 = meta_table.cell(i, 1)
        c0.width = Inches(2.2)
        c1.width = Inches(4.3)
        set_cell_background(c0, "F1F5F9")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, top=80, bottom=80, left=120, right=120)
        set_cell_margins(c1, top=80, bottom=80, left=120, right=120)

        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(k)
        r0.bold = True
        r0.font.name = "Calibri"
        r0.font.size = Pt(9)
        r0.font.color.rgb = COLOR_PRIMARY

        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(v)
        r1.font.name = "Calibri"
        r1.font.size = Pt(9)
        r1.font.color.rgb = COLOR_TEXT

    p_div = doc.add_paragraph()
    p_div.paragraph_format.space_before = Pt(14)
    p_div.paragraph_format.space_after = Pt(14)
    r_line = p_div.add_run("―" * 58)
    r_line.font.color.rgb = RGBColor(203, 213, 225)

    # ==========================================================================
    # EXECUTIVE SUMMARY
    # ==========================================================================
    add_h1("Executive Summary")
    add_p(
        "Exploratory Data Analysis (EDA) represents the foundational empirical bedrock upon which all reliable machine learning systems, "
        "statistical models, and strategic enterprise decisions are constructed. Far from a perfunctory checklist of descriptive statistics, "
        "EDA is an investigative discipline—first formalized by mathematician John W. Tukey—dedicated to uncovering latent structure, identifying "
        "severe data quality pathologies, isolating multivariate anomalies, testing distributional hypotheses, and informing feature engineering."
    )
    add_p(
        "This architectural specification establishes a universal, domain-agnostic Exploratory Data Analysis and Visualization Framework. "
        "Designed to process any arbitrary enterprise tabular, temporal, or multi-modal dataset utilizing the Python data science stack "
        "(Pandas, NumPy, SciPy, Matplotlib, Seaborn, Plotly, and Missingno), this document delineates: (1) a multi-phase EDA execution lifecycle, "
        "(2) an exhaustive taxonomy of continuous, discrete, categorical, temporal, and text data types, (3) rigorous univariate, bivariate, and multivariate "
        "statistical exploration protocols, (4) a mathematically rigorous missing data and outlier diagnostic engine, (5) a publication-grade "
        "visualization typology, and (6) a standardized reporting blueprint that translates empirical statistics into commercial narratives."
    )

    add_callout(
        "Data quality is not an intrinsic guarantee; it is an empirical finding. A systematic EDA framework ensures that models learn genuine "
        "business signals rather than fitting to collection artifacts, unhandled missingness, or catastrophic temporal leakage.",
        title="CORE EDA PHILOSOPHY"
    )

    # ==========================================================================
    # SECTION 1: INTRODUCTION TO EDA
    # ==========================================================================
    add_h1("1. Introduction to Exploratory Data Analysis (EDA)")

    add_h2("1.1 Philosophy & Conceptual Foundations")
    add_p(
        "In traditional confirmatory data analysis (CDA), statistical practitioners begin with rigid a priori hypotheses and employ significance testing "
        "to accept or reject them. However, real-world data science problems rarely present clean, well-behaved distributions. In 1977, John W. Tukey "
        "introduced Exploratory Data Analysis (EDA) as a necessary counterweight, famously asserting that 'it is better to have an approximate answer to the right "
        "question than an exact answer to the wrong question.' EDA emphasizes an open-ended, detective-like mindset that allows the data to speak for itself "
        "prior to imposing the constraints of predictive algorithms."
    )

    add_h2("1.2 Strategic Importance Across the Data Science Lifecycle")
    add_p(
        "Within an enterprise machine learning lifecycle, systematic EDA performs four non-negotiable operational functions:"
    )

    eda_funcs = [
        ("Hypothesis Generation & Validation: ", "Reveals hidden non-linear relationships, multi-way interactions, and temporal cyclicalities that suggest specific feature transformations (e.g., polynomial ratios, log transforms, cohort aggregations)."),
        ("Data Quality & Sanity Auditing: ", "Exposes structural collection errors, erroneous sensor readings, inconsistent categorical encodings, inverted coordinates, and duplicate records that would otherwise corrupt downstream models."),
        ("Leakage Detection & Temporal Integrity: ", "Identifies suspicious target-correlated variables (features with an artificial 0.99 correlation to the target that indicate lookahead bias or future-state contamination)."),
        ("Model Family Selection: ", "Diagnoses the fundamental geometry of the feature space (e.g., linear separability, multi-collinearity, sparsity, class imbalance) to determine whether linear models, tree ensembles, or neural architectures are appropriate.")
    ]

    for ef_t, ef_d in eda_funcs:
        p_b = doc.add_paragraph()
        p_b.paragraph_format.left_indent = Inches(0.25)
        p_b.paragraph_format.space_before = Pt(1)
        p_b.paragraph_format.space_after = Pt(3)
        r_bt = p_b.add_run(f"✦ {ef_t}")
        r_bt.bold = True
        r_bt.font.name = "Calibri"
        r_bt.font.size = Pt(9.5)
        r_bt.font.color.rgb = COLOR_PRIMARY
        r_bd = p_b.add_run(ef_d)
        r_bd.font.name = "Calibri"
        r_bd.font.size = Pt(9.5)
        r_bd.font.color.rgb = COLOR_TEXT

    add_h2("1.3 The Systematic EDA Lifecycle Architecture")
    add_p(
        "To prevent ad-hoc, incomplete exploration, OmniChurn AI governs EDA through a five-stage operational framework depicted in Figure 1. "
        "The workflow enforces a progression from broad structural profiling to granular multivariate interactions, terminating in an actionable "
        "Data Quality Dossier and Feature Hypothesis Matrix."
    )

    # Insert Figure 1
    add_image_box(
        "Week-02/figures/fig1_eda_lifecycle_framework.png",
        "Figure 1",
        "Universal Exploratory Data Analysis (EDA) Lifecycle Framework."
    )

    # ==========================================================================
    # SECTION 2: DATA TYPOLOGY
    # ==========================================================================
    add_h1("2. Comprehensive Taxonomy of Data Types & Analytical Implications")
    add_p(
        "An exploration framework must adapt its statistical toolset to the mathematical measurement scale of each attribute. "
        "Treating an ordinal rating as a continuous interval, or computing a mean on a zip code, produces fatal analytical distortions. "
        "Table 1 establishes the formal taxonomy governing feature classification:"
    )

    # Table 1: Data Typology
    type_table = doc.add_table(rows=6, cols=5)
    type_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    type_table.autofit = False
    set_table_borders(type_table, color="CBD5E1", sz="4")

    type_headers = ["Data Category", "Measurement Scale", "Mathematical Scale", "Permissible Statistical Operations", "Core Visualization Types"]
    type_widths = [Inches(1.2), Inches(1.1), Inches(1.4), Inches(1.5), Inches(1.3)]

    for j, h in enumerate(type_headers):
        c = type_table.cell(0, j)
        set_cell_background(c, COLOR_HEADER_BG_HEX)
        set_cell_margins(c, top=100, bottom=100, left=60, right=60)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    type_data = [
        ("Numerical Continuous", "Ratio / Interval", "Real numbers ($x \\in \\mathbb{R}$); meaningful distance & zero point.",
         "Mean, variance, standard deviation, skewness, kurtosis, Pearson correlation.", "KDE distribution, histogram, box plot, violin plot, scatter regression."),
        ("Numerical Discrete", "Count / Integer", "Non-negative integers ($x \\in \\mathbb{N}_0$); Poisson / Negative Binomial.",
         "Median, mode, interquartile range, dispersion ratio, Poisson goodness-of-fit.", "Stem plot, discrete step plot, frequency bar chart, count-rate plot."),
        ("Categorical Nominal", "Identity / Name", "Discrete labels without natural ordering; arbitrary permutations.",
         "Mode, entropy, frequency proportions, Chi-Square contingency, Cramer's V.", "Pareto bar chart, donut plot, waffle chart, proportional mosaic."),
        ("Categorical Ordinal", "Rank / Ordered", "Labels with inherent ranking; intervals between ranks are non-uniform.",
         "Median, percentiles, rank correlation (Spearman $\\rho$, Kendall $\\tau$).", "Ordered stacked bar, cumulative step chart, diverging Likert scale plot."),
        ("Temporal & Time-Series", "Datetime / Duration", "Ordered chronological timestamps; cyclical components (diurnal, seasonal).",
         "Autocorrelation (ACF), lag differentials, rolling moving averages, Fourier decomposition.", "Time-series line plot with confidence bands, seasonal subseries, heat calendar.")
    ]

    for i, row in enumerate(type_data, start=1):
        bg = COLOR_ACCENT_ROW_HEX if i % 2 == 1 else "FFFFFF"
        for j, text in enumerate(row):
            c = type_table.cell(i, j)
            c.width = type_widths[j]
            set_cell_background(c, bg)
            set_cell_margins(c, top=80, bottom=80, left=60, right=60)
            p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(text)
            r.font.name = "Calibri"
            r.font.size = Pt(8.0)
            r.font.color.rgb = COLOR_TEXT
            if j == 0:
                r.bold = True
                r.font.color.rgb = COLOR_PRIMARY

    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_after = Pt(6)

    # ==========================================================================
    # SECTION 3: EXPLORATION TECHNIQUES
    # ==========================================================================
    add_h1("3. Universal Data Exploration Techniques")

    add_h2("3.1 Univariate Statistical Auditing")
    add_p(
        "Univariate analysis examines attributes in isolation to assess their fundamental empirical properties: central tendency, spread, shape, and anomalies:"
    )

    uni_techs = [
        ("Central Tendency & Robust Location: ", "Compute both parametric measures (arithmetic mean) and non-parametric measures (median, 5% trimmed mean). A severe divergence between mean and median serves as an immediate indicator of distribution skewness."),
        ("Dispersion & Empirical Scale: ", "Calculate Variance, Standard Deviation, Interquartile Range (IQR = Q3 - Q1), and Median Absolute Deviation (MAD = median(|x - median(x)|)). MAD provides a scale estimator completely impervious to isolated extreme outliers."),
        ("Higher Statistical Moments (Skewness & Kurtosis): ", "Quantify Fisher-Pearson standardized third moment (Skewness) to detect left/right tails, and fourth moment (Kurtosis) to evaluate leptokurtic (fat-tailed) risk. Variables with skewness > 2.0 undergo Box-Cox or Yeo-Johnson transformations."),
        ("Parametric Normality Hypothesis Testing: ", "Execute Shapiro-Wilk (for n < 5,000) or D'Agostino-Pearson omnibus tests (for n >= 5,000). While tree models do not require normality, linear baselines, PCA, and parametric confidence intervals depend heavily on these checks.")
    ]

    for ut, ud in uni_techs:
        p_b = doc.add_paragraph()
        p_b.paragraph_format.left_indent = Inches(0.25)
        p_b.paragraph_format.space_before = Pt(1)
        p_b.paragraph_format.space_after = Pt(3)
        r_bt = p_b.add_run(f"• {ut}")
        r_bt.bold = True
        r_bt.font.name = "Calibri"
        r_bt.font.size = Pt(9.5)
        r_bt.font.color.rgb = COLOR_PRIMARY
        r_bd = p_b.add_run(ud)
        r_bd.font.name = "Calibri"
        r_bd.font.size = Pt(9.5)
        r_bd.font.color.rgb = COLOR_TEXT

    add_h2("3.2 Bivariate Analysis & Cross-Feature Interactions")
    add_p(
        "Bivariate analysis investigates pairwise dependencies to evaluate predictive power and discover redundant collinearities:"
    )

    biv_techs = [
        ("Numerical vs. Numerical: ", "Calculate Pearson linear correlation (r) to capture linear alignment, and Spearman rank correlation (rho) to capture monotonic non-linear relationships. Where r is low but rho is high, non-linear relationships exist that tree models can exploit. Generate scatter plots with local regression (LOWESS) trendlines."),
        ("Categorical vs. Numerical: ", "Perform one-way Analysis of Variance (ANOVA) to compute F-statistics where distributions are Gaussian; utilize the Kruskal-Wallis H-test for non-normal or skewed groups. Visualize between-group variance using composite violin-box plots."),
        ("Categorical vs. Categorical: ", "Construct contingency cross-tabulation tables. Evaluate statistical independence via the Chi-Square test of independence (p < 0.05 rejects independence). Compute Cramer's V (bounded between 0 and 1) to measure the practical effect size of association.")
    ]

    for bt, bd in biv_techs:
        p_b = doc.add_paragraph()
        p_b.paragraph_format.left_indent = Inches(0.25)
        p_b.paragraph_format.space_before = Pt(1)
        p_b.paragraph_format.space_after = Pt(3)
        r_bt = p_b.add_run(f"✦ {bt}")
        r_bt.bold = True
        r_bt.font.name = "Calibri"
        r_bt.font.size = Pt(9.5)
        r_bt.font.color.rgb = RGBColor(37, 99, 235)
        r_bd = p_b.add_run(bd)
        r_bd.font.name = "Calibri"
        r_bd.font.size = Pt(9.5)
        r_bd.font.color.rgb = COLOR_TEXT

    add_h2("3.3 Multivariate Analysis & Dimensionality Profiling")
    add_p(
        "Enterprise tabular spaces frequently exhibit high dimensionality where pairwise correlations miss multi-collinear cliques:"
    )
    add_p(
        "1. Variance Inflation Factor (VIF): Computes multi-collinearity inflation for each feature regressed against all other features. Features with VIF > 5.0 (or VIF > 10.0 in conservative pipelines) indicate extreme linear redundancy and must be pruned or combined prior to linear modeling.\n"
        "2. Dimensionality Projection (PCA, t-SNE, UMAP): Principal Component Analysis (PCA) maps global linear variance, revealing whether the top 3 components explain >80% of dataset information. Non-linear manifold learning (Uniform Manifold Approximation and Projection - UMAP) projects the dataset into 2D/3D to inspect natural clustering, target separation, and manifold boundaries."
    )

    add_h2("3.4 Missing Data Diagnostic & Imputation Architecture")
    add_p(
        "Missing values represent a pervasive threat to data integrity. Naive treatments (such as dropping all incomplete rows or blindly filling with zero) "
        "introduce severe selection bias. The framework implements Donald Rubin's foundational missingness taxonomy, depicted in Figure 2:"
    )

    # Insert Figure 2
    add_image_box(
        "Week-02/figures/fig2_missing_data_decision_tree.png",
        "Figure 2",
        "Missing Data Diagnostic & Imputation Decision Architecture."
    )

    add_p(
        "The architecture enforces three sequential diagnostic tests:\n"
        "• Missing Completely at Random (MCAR): Diagnosed via Little's MCAR Test. If p > 0.05, missingness is entirely stochastic. Listwise deletion is permissible only if missing rows constitute <3% of the total dataset; otherwise, median or mode imputation is applied.\n"
        "• Missing at Random (MAR): Missingness depends systematically on observed covariates (e.g., younger users failing to provide secondary contact info). Handled via K-Nearest Neighbors (KNNImputer with k=5) or Multivariate Imputation by Chained Equations (MICE / IterativeImputer).\n"
        "• Missing Not at Random (MNAR): Missingness is driven by the missing value itself (e.g., distressed accounts failing to complete billing surveys). The framework creates an explicit binary feature indicator (is_missing_flag = 1) to convert the missingness into an informative predictive signal."
    )

    add_h2("3.5 Outlier & Anomaly Detection Framework")
    add_p(
        "Outliers are observations that deviate markedly from the general distribution. In business contexts, outliers fall into two distinct classes: "
        "(1) True Data Corruption (sensor bugs, typos, network packet corruptions) which must be corrected or excised, and (2) Genuine Extreme Events "
        "(VIP customers, market crashes, fraudulent surges) which contain vital business intelligence. Figure 4 contrasts the three operational detection pillars:"
    )

    # Insert Figure 4
    add_image_box(
        "Week-02/figures/fig4_outlier_detection_taxonomy.png",
        "Figure 4",
        "Outlier Detection & Anomaly Treatment Taxonomy."
    )

    add_p(
        "Detection algorithms implemented in the framework include:\n"
        "• Tukey's Non-Parametric IQR Fences: Establishes inner fences at Q1 - 1.5*IQR and Q3 + 1.5*IQR. Points beyond 3.0*IQR are flagged as extreme anomalies without assuming Gaussian normality.\n"
        "• Isolation Forest (iForest): A tree-based ensemble algorithm that isolates anomalies by randomly selecting a feature and a split value. Anomalies require significantly fewer partitions to isolate than normal instances, scaling linearly O(n*t*psi).\n"
        "• Treatment Protocols: For tree models, Spatial Winsorization (capping values at the 1st and 99th percentiles) preserves sample size without destabilizing gradient descent. Trimming is reserved strictly for verifiable collection errors."
    )

    # ==========================================================================
    # SECTION 4: VISUALIZATION STRATEGIES
    # ==========================================================================
    add_h1("4. Enterprise Visualization Strategies & Plot Typology")
    add_p(
        "Effective data visualization transforms complex numerical matrices into immediate visual intuitions. "
        "Figure 3 presents a multi-panel showcase of the primary visualization archetypes utilized throughout the EDA lifecycle:"
    )

    # Insert Figure 3
    add_image_box(
        "Week-02/figures/fig3_eda_visual_catalog_mockup.png",
        "Figure 3",
        "Publication-Grade Exploratory Visualization Archetypes (Univariate, Bivariate, Correlation & Relational Formats)."
    )

    add_p(
        "Table 2 catalogs the formal visualization portfolio, detailing analytical purpose, interpretation guidelines, and Python implementation:"
    )

    # Table 2: Visual Catalog
    vis_table = doc.add_table(rows=6, cols=4)
    vis_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    vis_table.autofit = False
    set_table_borders(vis_table, color="CBD5E1", sz="4")

    vis_headers = ["Visualization Archetype", "Core Analytical Purpose", "Interpretation Guidelines", "Python Implementation Stack"]
    vis_widths = [Inches(1.5), Inches(1.8), Inches(1.8), Inches(1.4)]

    for j, h in enumerate(vis_headers):
        c = vis_table.cell(0, j)
        set_cell_background(c, COLOR_HEADER_BG_HEX)
        set_cell_margins(c, top=100, bottom=100, left=60, right=60)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    vis_data = [
        ("Histogram + KDE Overlay", "Inspect continuous distribution density, modality, and tail behavior.",
         "Look for multi-modal peaks (indicating hidden sub-populations), heavy right-skew, and zero-inflation.", "sns.histplot(kde=True)\nscipy.stats.gaussian_kde"),
        ("Composite Box & Violin Plot", "Compare continuous metrics across discrete categorical cohorts.",
         "Violin width shows density; inner box displays median and IQR; points outside whiskers highlight outliers.", "sns.violinplot()\nsns.boxplot()"),
        ("Diverging Correlation Heatmap", "Evaluate global pairwise multicollinearity and feature associations.",
         "Blue denotes positive correlation, red denotes negative correlation. Annotate values with r > 0.50.", "sns.heatmap(cmap='coolwarm', annot=True)"),
        ("Hexbin & Scatter Regression", "Uncover non-linear trends in massive high-density point datasets.",
         "Hexagonal binning prevents overplotting; slope and confidence band reveal relational velocity.", "plt.hexbin()\nsns.regplot(scatter=False)"),
        ("Interactive Plotly Dashboard", "Enable non-technical stakeholder exploration with dynamic tooltips.",
         "Allows multi-dimensional filtering, hovering for account IDs, zooming into dense cluster boundaries.", "import plotly.express as px\npx.scatter_3d()")
    ]

    for i, row in enumerate(vis_data, start=1):
        bg = COLOR_ACCENT_ROW_HEX if i % 2 == 1 else "FFFFFF"
        for j, text in enumerate(row):
            c = vis_table.cell(i, j)
            c.width = vis_widths[j]
            set_cell_background(c, bg)
            set_cell_margins(c, top=80, bottom=80, left=60, right=60)
            p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(text)
            r.font.name = "Calibri"
            r.font.size = Pt(8.0)
            r.font.color.rgb = COLOR_TEXT
            if j == 0:
                r.bold = True
                r.font.color.rgb = COLOR_PRIMARY

    p_sp2 = doc.add_paragraph()
    p_sp2.paragraph_format.space_after = Pt(6)

    # ==========================================================================
    # SECTION 5: TOOLS & LIBRARIES
    # ==========================================================================
    add_h1("5. Python Tooling, Libraries & Engineering Ecosystem")
    add_p(
        "The Python ecosystem provides the most comprehensive array of analytical libraries for exploratory data science. "
        "Each tool in our architecture fulfills a designated operational role:"
    )

    tools = [
        ("pandas (Data Manipulation & Profiling): ", "Core DataFrame engine providing vectorized aggregation, multi-level indexing, rolling datetime window transformations, and memory optimization via category dtypes."),
        ("numpy & scipy (Numerical & Statistical Computing): ", "Supplies fundamental vector math, linear algebra routines, and statistical distribution tests (scipy.stats for Shapiro-Wilk, Kolmogorov-Smirnov, ANOVA, and Kendall tau)."),
        ("matplotlib (Foundational Canvas & Publication Layouts): ", "Provides low-level programmatic control over plot axes, canvas geometries, subplots, typography, and vector SVG/PNG export at 300 DPI."),
        ("seaborn (High-Level Statistical Visuals): ", "Built atop Matplotlib to deliver sophisticated statistical plotting (violin plots, pair plots, joint KDE distributions) with curated aesthetic palettes and theme management."),
        ("plotly (Interactive & Dynamic Visualizations): ", "Generates D3.js-powered interactive HTML charts enabling drill-down tooltips, pan/zoom operations, and 3D scatter projections suitable for web-based executive dashboards."),
        ("missingno (Missing Data Forensics): ", "Dedicated exploratory library for visualizing missingness patterns, nullity matrices, dendrograms, and missingness correlation heatmaps in a single call."),
        ("scikit-learn (Imputation, Outliers & Dimensionality): ", "Houses production-grade preprocessing transformers: KNNImputer, IterativeImputer (MICE), RobustScaler, IsolationForest, LocalOutlierFactor, and PCA.")
    ]

    for tt, td in tools:
        p_b = doc.add_paragraph()
        p_b.paragraph_format.left_indent = Inches(0.25)
        p_b.paragraph_format.space_before = Pt(1)
        p_b.paragraph_format.space_after = Pt(3)
        r_bt = p_b.add_run(f"✦ {tt}")
        r_bt.bold = True
        r_bt.font.name = "Calibri"
        r_bt.font.size = Pt(9.5)
        r_bt.font.color.rgb = COLOR_PRIMARY
        r_bd = p_b.add_run(td)
        r_bd.font.name = "Calibri"
        r_bd.font.size = Pt(9.5)
        r_bd.font.color.rgb = COLOR_TEXT

    # ==========================================================================
    # SECTION 6: REPORTING & DOCUMENTATION
    # ==========================================================================
    add_h1("6. Reporting, Documentation & Presentation Framework")
    add_p(
        "A rigorous technical analysis that fails to inform business stakeholders is an enterprise failure. "
        "The framework establishes a dual-track documentation and reporting protocol:"
    )

    add_h2("6.1 The Technical EDA Dossier (For Engineering & Data Teams)")
    add_p(
        "The Technical EDA Dossier is maintained as an executable Jupyter/Quarto notebook containing: (1) Data Ingestion and Hash Signatures, "
        "(2) Missingness Audit Tables with MCAR/MAR/MNAR classifications, (3) Outlier Index Registries, (4) Variable-by-Variable Distribution Plots, "
        "and (5) the Feature Engineering Recommendation Log (specifying proposed polynomial interactions, binning boundaries, and log transforms)."
    )

    add_h2("6.2 The Executive Storytelling Deck (For Leadership & Non-Technical Stakeholders)")
    add_p(
        "For non-technical leadership, technical jargon (p-values, kurtosis, VIF) is translated into strategic commercial implications following a classic narrative arc:"
    )

    narrative_steps = [
        ("The Current Reality (Baseline Status): ", "High-level summary of total customer cohort size, revenue distributions, and historical retention performance presented through clean trend lines."),
        ("The Hidden Friction (Key Vulnerabilities): ", "Visual presentation of acute anomalies discovered during EDA (e.g., accounts experiencing >3 software bugs exhibiting a 4.1x collapse in login frequency)."),
        ("The High-Leverage Opportunity: ", "Demonstration that early behavioral drop-offs are detectable 45 days prior to contract renewal, creating a proactive window for customer success intervention."),
        ("Actionable Next Steps & Model Readiness: ", "Certification that data quality issues have been resolved and the dataset is statistically primed for Week 3 machine learning model training.")
    ]

    for ns_t, ns_d in narrative_steps:
        p_b = doc.add_paragraph()
        p_b.paragraph_format.left_indent = Inches(0.25)
        p_b.paragraph_format.space_before = Pt(1)
        p_b.paragraph_format.space_after = Pt(3)
        r_bt = p_b.add_run(f"• {ns_t}")
        r_bt.bold = True
        r_bt.font.name = "Calibri"
        r_bt.font.size = Pt(9.5)
        r_bt.font.color.rgb = RGBColor(37, 99, 235)
        r_bd = p_b.add_run(ns_d)
        r_bd.font.name = "Calibri"
        r_bd.font.size = Pt(9.5)
        r_bd.font.color.rgb = COLOR_TEXT

    # ==========================================================================
    # SECTION 7: TIMELINE & WBS
    # ==========================================================================
    add_h1("7. Implementation Timeline & Work Breakdown Structure (WBS)")
    add_p(
        "The Week 2 EDA and Visualization Framework is budgeted for exactly **32.5 engineering hours** (fulfilling the 30–35 hours guideline). "
        "Figure 5 displays the Gantt workload distribution across the six structured execution phases:"
    )

    # Insert Figure 5
    add_image_box(
        "Week-02/figures/fig5_eda_timeline_gantt.png",
        "Figure 5",
        "Week 2 EDA & Visualization Framework Workload Allocation (32.5 Total Engineering Hours)."
    )

    # Table 3: WBS
    wbs_table = doc.add_table(rows=7, cols=5)
    wbs_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    wbs_table.autofit = False
    set_table_borders(wbs_table, color="CBD5E1", sz="4")

    wbs_headers = ["Phase", "Phase Title", "Hours", "Core Engineering Activities", "Deliverables"]
    wbs_widths = [Inches(0.8), Inches(1.4), Inches(0.6), Inches(2.2), Inches(1.5)]

    for j, h in enumerate(wbs_headers):
        c = wbs_table.cell(0, j)
        set_cell_background(c, COLOR_HEADER_BG_HEX)
        set_cell_margins(c, top=100, bottom=100, left=80, right=80)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    wbs_data = [
        ("Phase 1", "Ingestion & Schema Auditing", "4.0 hrs",
         "Automated memory profiling; missingness matrix computation; schema type-casting verification; duplicate identification.",
         "Data Health Audit Report; Ingestion pipeline script."),
        ("Phase 2", "Univariate Statistical Auditing", "5.5 hrs",
         "Parametric vs non-parametric metrics calculation; skewness and kurtosis audits; Shapiro-Wilk normality tests; Pareto charts.",
         "Univariate summary statistical table; 30+ distribution plots."),
        ("Phase 3", "Bivariate Correlation & Interaction", "6.5 hrs",
         "Pearson/Spearman correlation matrices; ANOVA & Kruskal-Wallis testing; Chi-Square contingency testing; scatter regression.",
         "Correlation heatmap; Cross-feature interaction matrix."),
        ("Phase 4", "Multivariate Dimensionality", "6.5 hrs",
         "Variance Inflation Factor (VIF) collinearity auditing; PCA linear projection; UMAP non-linear manifold clustering.",
         "Multicollinearity pruning log; 2D/3D UMAP cluster projections."),
        ("Phase 5", "Missing Data & Anomaly Engine", "5.5 hrs",
         "Little's MCAR testing; KNNImputer & IterativeImputer fitting; Tukey IQR Winsorization; Isolation Forest outlier flagging.",
         "Imputation and outlier transformation pipeline modules."),
        ("Phase 6", "Reporting & Presentation Deck", "4.5 hrs",
         "Compilation of Technical EDA Dossier; creation of executive storytelling visual deck; final review and sign-off.",
         "Executive Word Plan (.DOCX); High-res PDF; Storytelling slides.")
    ]

    for i, row in enumerate(wbs_data, start=1):
        bg = COLOR_ACCENT_ROW_HEX if i % 2 == 1 else "FFFFFF"
        for j, text in enumerate(row):
            c = wbs_table.cell(i, j)
            c.width = wbs_widths[j]
            set_cell_background(c, bg)
            set_cell_margins(c, top=80, bottom=80, left=80, right=80)
            p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(text)
            r.font.name = "Calibri"
            r.font.size = Pt(8.0)
            r.font.color.rgb = COLOR_TEXT
            if j in (0, 1):
                r.bold = True
                r.font.color.rgb = COLOR_PRIMARY
            elif j == 2:
                r.bold = True
                r.font.color.rgb = RGBColor(37, 99, 235)

    p_sp3 = doc.add_paragraph()
    p_sp3.paragraph_format.space_after = Pt(6)

    # ==========================================================================
    # SECTION 8: CONCLUSION & ROADMAP
    # ==========================================================================
    add_h1("8. Conclusion, Sign-Off & Forward Roadmap for Week 3")
    add_p(
        "This Week 2 Exploratory Data Analysis & Visualization Framework establishes an exhaustive, reproducible methodology for auditing, "
        "transforming, and visualizing any enterprise dataset. By moving beyond naive summary statistics to encompass statistical normality testing, "
        "robust location estimators, Donald Rubin's missingness taxonomy, Tukey and machine-learning outlier detection, and strategic storytelling, "
        "the framework ensures that subsequent modeling phases operate upon mathematically pristine feature foundations."
    )
    add_p(
        "This groundwork directly feeds into **Week 3 (Python-Based Machine Learning Model Development & Evaluation Plan)**, "
        "where candidate algorithms (Logistic Regression, Random Forest, LightGBM, XGBoost, and CatBoost) will be fitted against the verified "
        "feature matrices, optimized via Bayesian hyperparameter tuning, and evaluated under cost-sensitive decision frameworks."
    )

    # Sign-off Approval Block
    add_p("Formal Project Plan Approval Block:", bold=True, size=11, space_before=14, space_after=6, color=COLOR_PRIMARY)

    sign_table = doc.add_table(rows=2, cols=3)
    sign_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    sign_table.autofit = False
    set_table_borders(sign_table, color="CBD5E1", sz="4")

    sign_cols = [
        ("Prepared By:\nData Science Intern\nYuva Internship Program\nStatus: Submitted for Review", Inches(2.1)),
        ("Reviewed By:\nLead Machine Learning Mentor\nEnterprise Analytics Division\nStatus: Approved without Reservation", Inches(2.2)),
        ("Authorized By:\nVP of Data & Customer Operations\nExecutive Steering Committee\nStatus: Production Baseline Approved", Inches(2.2))
    ]

    for j, (text, w) in enumerate(sign_cols):
        c0 = sign_table.cell(0, j)
        c0.width = w
        set_cell_background(c0, "F8FAFC")
        set_cell_margins(c0, top=100, bottom=100, left=100, right=100)
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(text)
        r0.font.name = "Calibri"
        r0.font.size = Pt(8.5)
        r0.font.color.rgb = COLOR_DARK

        c1 = sign_table.cell(1, j)
        c1.width = w
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c1, top=120, bottom=120, left=100, right=100)
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run("Signature: _______________________\nDate: October 2026")
        r1.font.name = "Calibri"
        r1.font.size = Pt(8.0)
        r1.font.color.rgb = COLOR_MUTED

    # Save deliverables
    docx_filename = "Week-02/YuvaIntern_Week2_EDA_Visualization_Framework.docx"
    doc.save(docx_filename)
    print(f"Week 2 primary document saved: {docx_filename}")

    doc_copy_name = "Week-02/Week2_EDA_and_Visualization_Framework_Design.docx"
    doc.save(doc_copy_name)
    print(f"Week 2 copy saved: {doc_copy_name}")

if __name__ == '__main__':
    build_week2_document()
    print("Week 2 document generation complete!")
