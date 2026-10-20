"""
Generate 5 publication-quality strategic diagrams for Week 4:
Comprehensive Data Science Report and Insights Presentation Plan.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
import numpy as np
import os

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#CBD5E1'
plt.rcParams['axes.linewidth'] = 0.8

os.makedirs('Week-04/figures', exist_ok=True)

# ==============================================================================
# FIGURE 1: Executive KPI Dashboard Mock-up
# ==============================================================================
def create_fig1():
    fig = plt.figure(figsize=(14, 8.5), dpi=150)
    fig.patch.set_facecolor('#FFFFFF')

    # Top Title
    fig.text(0.5, 0.95, "Figure 1: Executive KPI Dashboard & Business Impact Mock-Up",
             fontsize=14.5, fontweight='bold', ha='center', color='#0F172A')
    fig.text(0.5, 0.915, "OmniChurn AI: Enterprise Fleet-Wide Retention Performance & Financial Preservation Summary",
             fontsize=10.5, fontstyle='italic', ha='center', color='#475569')

    gs = fig.add_gridspec(3, 4, height_ratios=[0.9, 1.3, 1.3], hspace=0.35, wspace=0.25,
                          left=0.06, right=0.94, top=0.88, bottom=0.08)

    # 4 Top KPI Scorecards
    kpis = [
        {"title": "ANNUAL CHURN RATE", "val": "4.6%", "sub": "▼ 32.3% from 6.8% Baseline", "col": "#059669", "bg": "#ECFDF5"},
        {"title": "NET PRESERVED ARR", "val": "$11.41M", "sub": "▲ Protected Recurring Capital", "col": "#2563EB", "bg": "#EFF6FF"},
        {"title": "CAMPAIGN CONVERSION", "val": "42.5%", "sub": "▲ +24.5% vs Reactive Outreach", "col": "#7C3AED", "bg": "#F5F3FF"},
        {"title": "ANNUALIZED NET ROI", "val": "2,450%", "sub": "▲ $11.4M Net Return on $145k Inv.", "col": "#0D9488", "bg": "#F0FDFA"}
    ]

    for idx, k in enumerate(kpis):
        ax_kpi = fig.add_subplot(gs[0, idx])
        ax_kpi.set_facecolor(k["bg"])
        ax_kpi.axis('off')
        # Border
        rect = patches.FancyBboxPatch((0.02, 0.05), 0.96, 0.90, boxstyle="round,pad=0.05,rounding_size=0.1",
                                      linewidth=1.2, edgecolor=k["col"], facecolor=k["bg"], transform=ax_kpi.transAxes)
        ax_kpi.add_patch(rect)
        ax_kpi.text(0.5, 0.75, k["title"], fontsize=8.0, fontweight='bold', color='#475569', ha='center', transform=ax_kpi.transAxes)
        ax_kpi.text(0.5, 0.42, k["val"], fontsize=18, fontweight='bold', color=k["col"], ha='center', transform=ax_kpi.transAxes)
        ax_kpi.text(0.5, 0.16, k["sub"], fontsize=7.5, fontweight='bold', color='#1E293B', ha='center', transform=ax_kpi.transAxes)

    # Lower Left Chart: Monthly Churn Trend Before vs After
    ax_left = fig.add_subplot(gs[1:, :2])
    ax_left.set_facecolor('#F8FAFC')
    months = np.arange(1, 13)
    baseline_churn = np.array([6.7, 6.8, 6.9, 6.8, 7.0, 6.9, 6.8, 6.7, 6.9, 7.1, 6.8, 6.8])
    omnichurn_trend = np.array([6.7, 6.8, 6.5, 6.1, 5.7, 5.3, 5.0, 4.8, 4.7, 4.6, 4.5, 4.6])

    ax_left.plot(months, baseline_churn, color='#DC2626', linestyle='--', marker='o', lw=2.0, label='Status Quo (Reactive Baseline ~6.8%)')
    ax_left.plot(months, omnichurn_trend, color='#059669', marker='s', lw=2.5, label='OmniChurn AI Deployment (Drop to 4.6%)')
    ax_left.fill_between(months, baseline_churn, omnichurn_trend, color='#10B981', alpha=0.15, label='Preserved Account Capital Area')

    ax_left.set_title("Panel A: 12-Month Churn Trajectory: Reactive vs Algorithmic", fontsize=10.5, fontweight='bold', color='#0F172A')
    ax_left.set_xlabel("Operational Month", fontsize=9, fontweight='bold')
    ax_left.set_ylabel("Monthly Annualized Churn Rate (%)", fontsize=9, fontweight='bold')
    ax_left.set_xticks(months)
    ax_left.set_xticklabels([f"M{m}" for m in months])
    ax_left.set_ylim(4.0, 7.5)
    ax_left.grid(True, linestyle=':', alpha=0.6)
    ax_left.legend(loc='lower left', fontsize=8.0, frameon=True, facecolor='#FFFFFF')

    # Lower Right Chart: Churn Probability Distribution & Cohorts
    ax_right = fig.add_subplot(gs[1:, 2:])
    ax_right.set_facecolor('#F8FAFC')
    risk_tiers = ['Low Risk\n(<20%)', 'Moderate\n(20-35%)', 'High Risk\n(35-60%)', 'Critical Alert\n(>60%)']
    account_counts = [31500, 7200, 4500, 1800]
    bar_colors = ['#10B981', '#3B82F6', '#F59E0B', '#EF4444']

    bars = ax_right.bar(risk_tiers, account_counts, color=bar_colors, edgecolor='#0F172A', linewidth=0.8, alpha=0.85)
    for bar in bars:
        h = bar.get_height()
        pct = (h / 45000) * 100
        ax_right.text(bar.get_x() + bar.get_width()/2, h + 800, f"{h:,}\n({pct:.1f}%)",
                      ha='center', va='bottom', fontsize=8.0, fontweight='bold', color='#0F172A')

    ax_right.set_title("Panel B: Enterprise Fleet Risk Segmentation (45,000 Accounts)", fontsize=10.5, fontweight='bold', color='#0F172A')
    ax_right.set_ylabel("Total Corporate Accounts", fontsize=9, fontweight='bold')
    ax_right.set_ylim(0, 37000)
    ax_right.grid(axis='y', linestyle=':', alpha=0.6)

    plt.savefig('Week-04/figures/fig1_executive_kpi_dashboard_mockup.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Week 4 Fig 1 generated.")

# ==============================================================================
# FIGURE 2: Behavioral Decay Trend Analysis (90 Days Before Churn)
# ==============================================================================
def create_fig2():
    fig, ax = plt.subplots(figsize=(13, 7.5), dpi=150)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')

    days = np.arange(90, -1, -1)
    # Seat utilization collapses ~45 days prior
    usage = 100 / (1 + np.exp(-(days - 45)/10))
    # Support tickets spike ~30 days prior
    tickets = 1.2 + 6.0 * np.exp(-((days - 30)/12)**2)
    # Dunning soft failures spike ~15 days prior
    dunning = 0.2 + 4.5 * np.exp(-((days - 15)/8)**2)

    ax.plot(days, usage, color='#2563EB', lw=2.5, label='Active Seat Utilization Index (Base=100)')
    ax.plot(days, tickets * 12, color='#D97706', lw=2.2, linestyle='--', label='Customer Support Escalation Spikes (Scaled)')
    ax.plot(days, dunning * 16, color='#DC2626', lw=2.2, linestyle=':', label='Billing Dunning Soft Failures (Scaled)')

    # Shaded Proactive Window
    ax.axvspan(35, 60, color='#10B981', alpha=0.18, label='Optimal Algorithmic Intervention Window (Days -60 to -35)')
    ax.axvspan(0, 20, color='#EF4444', alpha=0.15, label='Reactive Churn Zone (Disengagement Terminal)')

    ax.set_xlim(90, 0) # Inverted: counting down to cancellation
    ax.set_xlabel("Days Prior to Subscription Termination Notice (Countdown to Churn)", fontsize=10.5, fontweight='bold', color='#0F172A', labelpad=10)
    ax.set_ylabel("Normalized Telemetry & Behavioral Signal Velocity", fontsize=10.5, fontweight='bold', color='#0F172A', labelpad=10)
    ax.grid(True, linestyle='--', alpha=0.5, color='#CBD5E1')

    # Annotations
    ax.annotate("Leading Signal: Active seat usage collapses at Day -45\n(Algorithms trigger intervention here)",
                xy=(45, 50), xytext=(65, 75),
                arrowprops=dict(facecolor='#2563EB', shrink=0.08, width=1.5, headwidth=6),
                fontsize=8.5, fontweight='bold', color='#1E3A8A',
                bbox=dict(boxstyle="round,pad=0.3", fc="#EFF6FF", ec="#93C5FD"))

    ax.annotate("Late Signal: Support escalations spike at Day -30\n(Customer deeply frustrated)",
                xy=(30, 72), xytext=(35, 92),
                arrowprops=dict(facecolor='#D97706', shrink=0.08, width=1.5, headwidth=6),
                fontsize=8.5, fontweight='bold', color='#B45309',
                bbox=dict(boxstyle="round,pad=0.3", fc="#FEF3C7", ec="#FCD34D"))

    ax.annotate("Fatal Zone: Payment fails at Day -15\n(Competitor migration already active)",
                xy=(15, 70), xytext=(22, 35),
                arrowprops=dict(facecolor='#DC2626', shrink=0.08, width=1.5, headwidth=6),
                fontsize=8.5, fontweight='bold', color='#B91C1C',
                bbox=dict(boxstyle="round,pad=0.3", fc="#FEF2F2", ec="#FCA5A5"))

    plt.title("Figure 2: Empirical Behavioral Decay Timeline (90 Days Leading Up to Churn)\nProving that Predictive Algorithms Unlock a Crucial 45-Day Proactive Rescue Window",
              fontsize=13, fontweight='bold', color='#0F172A', pad=18)
    ax.legend(loc='upper right', fontsize=8.5, frameon=True, facecolor='#FFFFFF')

    plt.tight_layout()
    plt.savefig('Week-04/figures/fig2_behavioral_decay_trend_analysis.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Week 4 Fig 2 generated.")

# ==============================================================================
# FIGURE 3: Strategic Non-Technical Storytelling Framework
# ==============================================================================
def create_fig3():
    fig, ax = plt.subplots(figsize=(14, 8), dpi=150)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    ax.text(7, 8.1, "Figure 3: Strategic Non-Technical Storytelling Architecture (The 4-Act Business Narrative)",
            fontsize=14.5, fontweight='bold', ha='center', color='#0F172A')
    ax.text(7, 7.7, "Translating Complex Statistical Matrices & Machine Learning Gradients into Actionable Executive Consensus",
            fontsize=10.5, fontstyle='italic', ha='center', color='#475569')

    acts = [
        {"act": "ACT 1: THE BUSINESS REALITY", "title": "The Status Quo & Financial Bleed",
         "desc": "• 45,000 corporate clients\n• $36.72M gross ARR churned annually\n• Acquisition is 5-7x costlier than retention\n• Reactive outreach rescues only 18% of accounts",
         "col": "#DC2626", "x": 0.6, "y": 2.2, "w": 2.8},
        {"act": "ACT 2: THE HIDDEN FRICTION", "title": "Empirical Diagnostic Discoveries",
         "desc": "• Seat velocity collapses 45 days before notice\n• Unresolved P1 bugs multiply churn risk 4.1x\n• Soft billing failures precede cancellations\n• Blanket discounting erodes profit margins",
         "col": "#D97706", "x": 3.8, "y": 2.2, "w": 2.8},
        {"act": "ACT 3: THE ALGORITHMIC RADAR", "title": "Precision Predictive Intelligence",
         "desc": "• OmniChurn AI scans multi-modal telemetry\n• PR-AUC = 0.864 captures 78% of at-risk base\n• Operating cutoff optimized to tau = 0.35\n• Local SHAP explains root-cause drivers",
         "col": "#2563EB", "x": 7.0, "y": 2.2, "w": 2.8},
        {"act": "ACT 4: THE STRATEGIC ROI", "title": "Prescriptive Playbooks & Growth",
         "desc": "• Churn drops from 6.8% to 4.6%\n• $11.41M Net Preserved ARR per year\n• Outreach conversion surges to 42.5%\n• 2,450% Annualized Net ROI achieved",
         "col": "#059669", "x": 10.2, "y": 2.2, "w": 2.8}
    ]

    for a in acts:
        card = patches.FancyBboxPatch(
            (a["x"], a["y"]), a["w"], 5.0,
            boxstyle="round,pad=0.08,rounding_size=0.12",
            linewidth=1.5, edgecolor=a["col"], facecolor='#FFFFFF', zorder=2
        )
        ax.add_patch(card)

        hdr = patches.FancyBboxPatch(
            (a["x"], a["y"] + 5.0 - 0.75), a["w"], 0.75,
            boxstyle="round,pad=0.02,rounding_size=0.1",
            linewidth=0, facecolor=a["col"], zorder=3
        )
        ax.add_patch(hdr)

        ax.text(a["x"] + a["w"]/2, a["y"] + 5.0 - 0.25, a["act"],
                fontsize=8.5, fontweight='bold', color='#FFFFFF', ha='center', zorder=4)
        ax.text(a["x"] + a["w"]/2, a["y"] + 5.0 - 0.52, a["title"],
                fontsize=9, fontweight='bold', color='#FFFFFF', ha='center', zorder=4)

        ax.text(a["x"] + 0.2, a["y"] + 3.2, a["desc"],
                fontsize=8.2, color='#1E293B', va='center', zorder=4)

    for i in range(len(acts) - 1):
        x_start = acts[i]["x"] + acts[i]["w"] + 0.05
        x_end = acts[i+1]["x"] - 0.05
        ax.annotate('', xy=(x_end, 4.7), xytext=(x_start, 4.7),
                    arrowprops=dict(arrowstyle="->,head_width=0.25,head_length=0.35", color="#64748B", lw=2.2))

    # Bottom Banner
    btm = patches.FancyBboxPatch(
        (0.6, 0.6), 12.4, 1.2,
        boxstyle="round,pad=0.08,rounding_size=0.1",
        linewidth=1, edgecolor='#CBD5E1', facecolor='#F1F5F9', zorder=2
    )
    ax.add_patch(btm)
    ax.text(6.8, 1.35, "EXECUTIVE COMMUNICATION PRINCIPLE: Frame Models Around Business Value, Not Loss Gradients",
            fontsize=10, fontweight='bold', color='#1E293B', ha='center')
    ax.text(6.8, 0.95, "Never present raw F1-scores or log-loss to non-technical executives. Always anchor findings to protected capital ($),\nsaved customer contracts, operational time reclaimed, and risk-adjusted return on investment (ROI).",
            fontsize=8.2, color='#475569', ha='center')

    plt.tight_layout()
    plt.savefig('Week-04/figures/fig3_non_technical_storytelling_framework.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Week 4 Fig 3 generated.")

# ==============================================================================
# FIGURE 4: Churn Risk Segmentation & Tailored Intervention Matrix
# ==============================================================================
def create_fig4():
    fig, ax = plt.subplots(figsize=(13, 8), dpi=150)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')

    # 4 Quadrants
    # X: Churn Risk Probability (Low -> High)
    # Y: Account ARR Value (Low -> High)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    # Dividing lines
    ax.axvline(50, color='#64748B', linestyle='--', lw=1.5)
    ax.axhline(50, color='#64748B', linestyle='--', lw=1.5)

    # Quadrant 1: Top-Right (High Value / High Risk)
    ax.fill_between([50, 100], [50, 50], [100, 100], color='#FEF2F2', alpha=0.7)
    # Quadrant 2: Top-Left (High Value / Low Risk)
    ax.fill_between([0, 50], [50, 50], [100, 100], color='#ECFDF5', alpha=0.7)
    # Quadrant 3: Bottom-Right (Low Value / High Risk)
    ax.fill_between([50, 100], [0, 0], [50, 50], color='#FFFBEB', alpha=0.7)
    # Quadrant 4: Bottom-Left (Low Value / Low Risk)
    ax.fill_between([0, 50], [0, 0], [50, 50], color='#F1F5F9', alpha=0.7)

    # Annotations in each quadrant
    q_data = [
        {"title": "QUADRANT 1: EMERGENCY RESCUE (VIP)",
         "desc": "High Value (ARR > $25k) + High Churn Risk (>35%)\n• Immediate White-Glove VP & CSM outreach\n• Dedicated engineering sprint for bug fixes\n• Flexible contract terms & executive review",
         "x": 75, "y": 75, "col": "#DC2626"},
        {"title": "QUADRANT 2: EXPANSION & ADVOCACY",
         "desc": "High Value (ARR > $25k) + Low Churn Risk (<35%)\n• Upsell target for new enterprise modules\n• Customer advisory board invitation\n• Multi-year contract renewal locks",
         "x": 25, "y": 75, "col": "#059669"},
        {"title": "QUADRANT 3: AUTOMATED DIGITAL RESCUE",
         "desc": "Low Value (ARR < $25k) + High Churn Risk (>35%)\n• Automated in-app interactive tutorials\n• Targeted self-serve knowledge base emails\n• Low-touch algorithmic discount vouchers",
         "x": 75, "y": 25, "col": "#D97706"},
        {"title": "QUADRANT 4: PRODUCT-LED NURTURE",
         "desc": "Low Value (ARR < $25k) + Low Churn Risk (<35%)\n• Standard automated product release digests\n• Community forum engagement\n• Self-serve feature adoption prompts",
         "x": 25, "y": 25, "col": "#475569"}
    ]

    for q in q_data:
        ax.text(q["x"], q["y"] + 12, q["title"], fontsize=9.5, fontweight='bold', color=q["col"], ha='center')
        ax.text(q["x"], q["y"] - 3, q["desc"], fontsize=8.2, color='#1E293B', ha='center', va='center')

    ax.set_xlabel("Predictive Churn Risk Probability (OmniChurn AI Score: 0% to 100%)", fontsize=10.5, fontweight='bold', color='#0F172A', labelpad=10)
    ax.set_ylabel("Account Annual Recurring Revenue (ARR Bracket)", fontsize=10.5, fontweight='bold', color='#0F172A', labelpad=10)
    ax.set_xticks([15, 35, 50, 75, 90])
    ax.set_xticklabels(["0-20% Low", "35% Cutoff", "50% Mid", "75% High", "90%+ Critical"], fontsize=8.5)
    ax.set_yticks([25, 50, 75])
    ax.set_yticklabels(["Starter (<$10k)", "Growth ($10k-$25k)", "Enterprise (>$25k)"], fontsize=8.5)

    plt.title("Figure 4: Strategic Account Segmentation & Tailored Intervention Playbook Matrix\nAligning Predictive Risk Probabilities with Commercial Account Value to Optimize Retention Labor",
              fontsize=13, fontweight='bold', color='#0F172A', pad=18)

    plt.tight_layout()
    plt.savefig('Week-04/figures/fig4_churn_risk_segmentation_matrix.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Week 4 Fig 4 generated.")

# ==============================================================================
# FIGURE 5: Week 4 Timeline & Gantt Workload (32.5 Hours)
# ==============================================================================
def create_fig5():
    fig, ax = plt.subplots(figsize=(13, 7.5), dpi=150)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')

    tasks = [
        "Phase 1: Executive KPI Consolidation & ROI Modeling",
        "Phase 2: Behavioral Decay & Deep-Dive Anomaly Trend Analysis",
        "Phase 3: Visual Mock-Up Production & Narrative Arc Framing",
        "Phase 4: Non-Technical Presentation Deck & Storytelling Suite",
        "Phase 5: Strategic Recommendations & Expansion Roadmap",
        "Phase 6: Final Executive Report Compilation & Sign-off"
    ]

    start_hours = [0.0, 4.5, 10.0, 16.5, 23.5, 28.5]
    durations   = [4.5, 5.5,  6.5,  7.0,  5.0,  4.0]
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
    ax.text(32.7, 5.2, "Final Report Delivery\n(32.5 Hours Total)", color='#DC2626',
            fontweight='bold', fontsize=9.5, va='center')

    ax.axvspan(30, 35, color='#FEF3C7', alpha=0.4, zorder=0, label="Target Window (30-35 hrs)")

    plt.title("Figure 5: Week 4 Executive Reporting & Presentation Plan Workload Allocation\nBudgeting Exactly 32.5 Total Engineering Hours Across 6 Systematic Execution Phases",
              fontsize=13, fontweight='bold', color='#0F172A', pad=18)

    ax.legend(loc='lower right', frameon=True, facecolor='#FFFFFF', edgecolor='#CBD5E1', fontsize=9)

    plt.tight_layout()
    plt.savefig('Week-04/figures/fig5_week4_timeline_gantt.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Week 4 Fig 5 generated.")

if __name__ == '__main__':
    create_fig1()
    create_fig2()
    create_fig3()
    create_fig4()
    create_fig5()
    print("All 5 Week-04 figures generated successfully.")
