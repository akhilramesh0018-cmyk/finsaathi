import streamlit as st
import datetime

st.set_page_config(page_title="FinSaathi", page_icon="💰", layout="centered")

# ============================================================
#  ANONYMOUS USAGE LOGGING (no personal data ever stored)
# ============================================================
def log_anonymous_usage(user_type, score, lang_used):
    """
    Saves ONLY: timestamp, user type, score, language.
    Never saves name, salary, expenses, or any personal detail.
    Fails silently if not configured — app still works without it.
    """
    try:
        import gspread
        from google.oauth2.service_account import Credentials

        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_info(
            dict(st.secrets["gcp_service_account"]), scopes=scopes
        )
        client = gspread.authorize(creds)
        sheet = client.open_by_key(st.secrets["sheet"]["sheet_id"]).sheet1

        sheet.append_row([
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            user_type,
            score,
            lang_used
        ])
    except Exception:
        # If secrets aren't set up yet, or sheet is unreachable —
        # the app must continue working normally for the user.
        pass

# ============================================================
#  LANGUAGE TOGGLE
# ============================================================
lang = st.selectbox("🌐 Language / ಭಾಷೆ", ["English", "ಕನ್ನಡ"])
KN = (lang == "ಕನ್ನಡ")

# ============================================================
#  PRIVACY DISCLAIMER — always visible, builds trust
# ============================================================
if KN:
    st.caption("🔒 ನಿಮ್ಮ ಗೌಪ್ಯತೆ ನಮಗೆ ಮುಖ್ಯ: ನಾವು ನಿಮ್ಮ ಹೆಸರು, ಆದಾಯ, ಅಥವಾ ಯಾವುದೇ ವೈಯಕ್ತಿಕ ಮಾಹಿತಿಯನ್ನು ಸಂಗ್ರಹಿಸುವುದಿಲ್ಲ ಅಥವಾ ಉಳಿಸುವುದಿಲ್ಲ. ಎಲ್ಲಾ ಲೆಕ್ಕಾಚಾರಗಳು ನಿಮ್ಮ ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಮಾತ್ರ ನಡೆಯುತ್ತವೆ ಮತ್ತು ನೀವು ಪುಟವನ್ನು ಮುಚ್ಚಿದ ತಕ್ಷಣ ಅಳಿಸಲಾಗುತ್ತದೆ.")
else:
    st.caption("🔒 Your privacy matters to us: We do NOT store your name, income, or any personal information. All calculations happen only in your browser and are deleted the moment you close this page.")

# ============================================================
#  INPUT LABELS (already working — kept as-is)
# ============================================================
if not KN:
    title = "💰 FinSaathi"
    subtitle = "Your Personal Financial Health Score Card"
    lbl_name = "Your name"
    lbl_type = "What do you primarily do?"
    type_opts = ["🌾 Farmer", "🏪 Small Business", "👷 Self-Employed", "💼 Salaried"]
    lbl_salary = "Monthly income (Rs)"
    lbl_expense = "Monthly expenses (Rs)"
    lbl_emi = "Monthly EMI (Rs, enter 0 if none)"
    lbl_emergency = "Emergency fund / savings (Rs)"
    lbl_dep = "Number of dependents"
    lbl_invest = "Do you invest in MF / SIP / FD?"
    invest_opts = ["No", "Yes"]
    lbl_invest_amt = "Monthly investment amount (Rs)"
    lbl_health = "Do you have health insurance?"
    health_opts = ["No", "Yes — only myself", "Yes — full family"]
    lbl_life = "Do you have life insurance or term plan?"
    life_opts = ["No", "Yes — LIC / endowment", "Yes — term plan"]
    lbl_debt = "Any other informal debt? (relatives, chit fund)"
    debt_opts = ["No other debt", "Yes — less than 1 month income",
                 "Yes — 1 to 6 months income", "Yes — more than 6 months income"]
    lbl_goal = "Your main financial goal?"
    goal_opts = ["Buy a house", "Children education", "Start or grow business",
                 "Retirement planning", "Debt clearance", "Build emergency fund"]
    lbl_btn = "🔍 Calculate My Financial Health Score"
    lbl_report = "📊 Financial Health Report"
    lbl_analysis = "📋 Detailed Analysis"
    lbl_advice = "💡 Personalised Advice"
    lbl_schemes = "🏛️ Recommended Schemes For You"
    lbl_footer = "Built with ❤️ by FinSaathi | Free • Neutral • Trustworthy"
    lbl_name_warn = "Please enter your name first!"
    lbl_saving = "Monthly Saving"
    lbl_savings_rate = "Savings Rate"
    lbl_emi_burden = "EMI Burden"
    lbl_benefit = "Benefit"
    lbl_apply = "How to apply"
    lbl_great = "You are doing great! Keep it up."
    lbl_income_type = "How does your income usually come?"
    income_type_opts = ["Regular monthly income", "Seasonal — comes at harvest/crop sale time"]
    lbl_seasonal_income = "Total income from last harvest/season (Rs)"
    lbl_crop_duration = "How many months does this income need to cover? (until next harvest)"
    lbl_harvests = "Number of harvests / income cycles per year"
    lbl_effective_income_note = "Calculated effective monthly income"
else:
    title = "💰 ಫಿನ್‌ಸಾಥಿ"
    subtitle = "ನಿಮ್ಮ ವೈಯಕ್ತಿಕ ಆರ್ಥಿಕ ಆರೋಗ್ಯ ಸ್ಕೋರ್ ಕಾರ್ಡ್"
    lbl_name = "ನಿಮ್ಮ ಹೆಸರು"
    lbl_type = "ನೀವು ಮುಖ್ಯವಾಗಿ ಏನು ಮಾಡುತ್ತೀರಿ?"
    type_opts = ["🌾 ರೈತ", "🏪 ಸಣ್ಣ ವ್ಯಾಪಾರ", "👷 ಸ್ವಯಂ ಉದ್ಯೋಗಿ", "💼 ಸಂಬಳದಾರ"]
    lbl_salary = "ಮಾಸಿಕ ಆದಾಯ (ರೂ)"
    lbl_expense = "ಮಾಸಿಕ ಖರ್ಚು (ರೂ)"
    lbl_emi = "ಮಾಸಿಕ EMI (ರೂ, ಇಲ್ಲದಿದ್ದರೆ 0)"
    lbl_emergency = "ತುರ್ತು ನಿಧಿ / ಉಳಿತಾಯ (ರೂ)"
    lbl_dep = "ಅವಲಂಬಿತರ ಸಂಖ್ಯೆ"
    lbl_invest = "ನೀವು MF / SIP / FD ನಲ್ಲಿ ಹೂಡಿಕೆ ಮಾಡುತ್ತೀರಾ?"
    invest_opts = ["ಇಲ್ಲ", "ಹೌದು"]
    lbl_invest_amt = "ಮಾಸಿಕ ಹೂಡಿಕೆ ಮೊತ್ತ (ರೂ)"
    lbl_health = "ಆರೋಗ್ಯ ವಿಮೆ ಇದೆಯೇ?"
    health_opts = ["ಇಲ್ಲ", "ಹೌದು — ನನಗೆ ಮಾತ್ರ", "ಹೌದು — ಇಡೀ ಕುಟುಂಬಕ್ಕೆ"]
    lbl_life = "ಜೀವ ವಿಮೆ ಅಥವಾ ಟರ್ಮ್ ಪ್ಲಾನ್ ಇದೆಯೇ?"
    life_opts = ["ಇಲ್ಲ", "ಹೌದು — LIC", "ಹೌದು — ಟರ್ಮ್ ಪ್ಲಾನ್"]
    lbl_debt = "ಬೇರೆ ಅನೌಪಚಾರಿಕ ಸಾಲ ಇದೆಯೇ?"
    debt_opts = ["ಸಾಲ ಇಲ್ಲ", "ಹೌದು — 1 ತಿಂಗಳ ಆದಾಯಕ್ಕಿಂತ ಕಡಿಮೆ",
                 "ಹೌದು — 1 ರಿಂದ 6 ತಿಂಗಳ ಆದಾಯ", "ಹೌದು — 6 ತಿಂಗಳ ಆದಾಯಕ್ಕಿಂತ ಹೆಚ್ಚು"]
    lbl_goal = "ನಿಮ್ಮ ಪ್ರಮುಖ ಆರ್ಥಿಕ ಗುರಿ?"
    goal_opts = ["ಮನೆ ಕೊಳ್ಳುವುದು", "ಮಕ್ಕಳ ಶಿಕ್ಷಣ", "ವ್ಯಾಪಾರ ಪ್ರಾರಂಭಿಸುವುದು",
                 "ನಿವೃತ್ತಿ ಯೋಜನೆ", "ಸಾಲ ತೀರಿಸುವುದು", "ತುರ್ತು ನಿಧಿ ನಿರ್ಮಾಣ"]
    lbl_btn = "🔍 ನನ್ನ ಆರ್ಥಿಕ ಆರೋಗ್ಯ ಸ್ಕೋರ್ ಲೆಕ್ಕ ಹಾಕಿ"
    lbl_report = "📊 ಆರ್ಥಿಕ ಆರೋಗ್ಯ ವರದಿ"
    lbl_analysis = "📋 ವಿವರವಾದ ವಿಶ್ಲೇಷಣೆ"
    lbl_advice = "💡 ವೈಯಕ್ತಿಕ ಸಲಹೆ"
    lbl_schemes = "🏛️ ಶಿಫಾರಸು ಮಾಡಿದ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು"
    lbl_footer = "FinSaathi ❤️ | ಉಚಿತ • ತಟಸ್ಥ • ವಿಶ್ವಾಸಾರ್ಹ"
    lbl_name_warn = "ದಯವಿಟ್ಟು ಮೊದಲು ನಿಮ್ಮ ಹೆಸರು ನಮೂದಿಸಿ!"
    lbl_saving = "ಮಾಸಿಕ ಉಳಿತಾಯ"
    lbl_savings_rate = "ಉಳಿತಾಯ ದರ"
    lbl_emi_burden = "EMI ಹೊರೆ"
    lbl_benefit = "ಪ್ರಯೋಜನ"
    lbl_apply = "ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ವಿಧಾನ"
    lbl_great = "ನೀವು ಅದ್ಭುತವಾಗಿ ಮಾಡುತ್ತಿದ್ದೀರಿ! ಮುಂದುವರಿಯಿರಿ."
    lbl_income_type = "ನಿಮ್ಮ ಆದಾಯ ಸಾಮಾನ್ಯವಾಗಿ ಹೇಗೆ ಬರುತ್ತದೆ?"
    income_type_opts = ["ನಿಯಮಿತ ಮಾಸಿಕ ಆದಾಯ", "ಋತುಮಾನ — ಸುಗ್ಗಿ/ಬೆಳೆ ಮಾರಾಟದ ಸಮಯದಲ್ಲಿ ಬರುತ್ತದೆ"]
    lbl_seasonal_income = "ಕಳೆದ ಸುಗ್ಗಿ/ಋತುವಿನ ಒಟ್ಟು ಆದಾಯ (ರೂ)"
    lbl_crop_duration = "ಈ ಆದಾಯ ಎಷ್ಟು ತಿಂಗಳುಗಳಿಗೆ ಸಾಕಾಗಬೇಕು? (ಮುಂದಿನ ಸುಗ್ಗಿಯವರೆಗೆ)"
    lbl_harvests = "ವರ್ಷಕ್ಕೆ ಎಷ್ಟು ಸುಗ್ಗಿ / ಆದಾಯ ಚಕ್ರಗಳು"
    lbl_effective_income_note = "ಲೆಕ್ಕ ಹಾಕಿದ ಪರಿಣಾಮಕಾರಿ ಮಾಸಿಕ ಆದಾಯ"

# ============================================================
#  HEADER
# ============================================================
st.title(title)
st.subheader(subtitle)
st.divider()

# ============================================================
#  INPUTS
# ============================================================
name = st.text_input(lbl_name)
user_type = st.selectbox(lbl_type, type_opts)

is_farmer = "🌾" in user_type
seasonal_risk_flag = False  # used later for an extra scoring rule

if is_farmer:
    income_type = st.radio(lbl_income_type, income_type_opts)
    is_seasonal = (income_type == income_type_opts[1])

    if is_seasonal:
        seasonal_total = st.number_input(lbl_seasonal_income, min_value=0, value=120000, step=5000)
        crop_duration = st.number_input(lbl_crop_duration, min_value=1, max_value=12, value=4, step=1)
        harvests_per_year = st.number_input(lbl_harvests, min_value=1, max_value=12, value=1, step=1)

        # Effective monthly income = seasonal lump sum spread over the months it must cover
        salary = round(seasonal_total / crop_duration) if crop_duration > 0 else 0

        st.caption(f"💡 {lbl_effective_income_note}: Rs {salary:,}")

        # A farmer with only 1 harvest/year and a short crop duration carries higher cash-flow risk
        if harvests_per_year == 1 and crop_duration <= 6:
            seasonal_risk_flag = True
    else:
        salary = st.number_input(lbl_salary, min_value=0, value=50000, step=1000)
else:
    salary = st.number_input(lbl_salary, min_value=0, value=50000, step=1000)

expense = st.number_input(lbl_expense, min_value=0, value=25000, step=500)
emi = st.number_input(lbl_emi, min_value=0, value=0, step=500)
emergency = st.number_input(lbl_emergency, min_value=0, value=50000, step=5000)
dependents = st.number_input(lbl_dep, min_value=0, value=2, step=1)
invest_ans = st.selectbox(lbl_invest, invest_opts)

monthly_investment = 0
if invest_ans == invest_opts[1]:
    monthly_investment = st.number_input(lbl_invest_amt, min_value=0, value=2000, step=500)

health_ins = st.selectbox(lbl_health, health_opts)
life_ins = st.selectbox(lbl_life, life_opts)
other_debt = st.selectbox(lbl_debt, debt_opts)
goal = st.selectbox(lbl_goal, goal_opts)

st.divider()

# ============================================================
#  CALCULATE
# ============================================================
if st.button(lbl_btn):

    if name.strip() == "":
        st.warning(lbl_name_warn)
    else:
        monthly_saving = salary - expense - emi
        expense_ratio = (expense / salary * 100) if salary > 0 else 0
        savings_rate = (monthly_saving / salary * 100) if salary > 0 else 0
        emi_burden = (emi / salary * 100) if salary > 0 else 0
        months_covered = (emergency / expense) if expense > 0 else 0
        emergency_target = 6 + max(0, int(dependents) - 2)

        score = 0
        reasons = []   # each item: (icon, english_text, kannada_text)
        advice = []
        schemes = []

        # ---------- Rule 1 — Savings rate (20 pts) ----------
        if savings_rate >= 30:
            score += 20
            reasons.append(("✅",
                f"Savings rate {round(savings_rate,1)}% — Excellent",
                f"ಉಳಿತಾಯ ದರ {round(savings_rate,1)}% — ಅತ್ಯುತ್ತಮ"))
        elif savings_rate >= 20:
            score += 14
            reasons.append(("🟡",
                f"Savings rate {round(savings_rate,1)}% — Moderate",
                f"ಉಳಿತಾಯ ದರ {round(savings_rate,1)}% — ಸಾಧಾರಣ"))
        elif savings_rate >= 10:
            score += 7
            reasons.append(("🟠",
                f"Savings rate {round(savings_rate,1)}% — Low",
                f"ಉಳಿತಾಯ ದರ {round(savings_rate,1)}% — ಕಡಿಮೆ"))
            advice.append(("Save at least 20% of your monthly income",
                            "ನಿಮ್ಮ ಮಾಸಿಕ ಆದಾಯದ ಕನಿಷ್ಠ 20% ಉಳಿತಾಯ ಮಾಡಿ"))
        else:
            score += 2
            reasons.append(("❌",
                f"Savings rate {round(savings_rate,1)}% — Critical",
                f"ಉಳಿತಾಯ ದರ {round(savings_rate,1)}% — ಗಂಭೀರ"))
            advice.append(("Savings are very low — review all expenses urgently",
                            "ಉಳಿತಾಯ ಬಹಳ ಕಡಿಮೆ — ಎಲ್ಲಾ ಖರ್ಚುಗಳನ್ನು ತಕ್ಷಣ ಪರಿಶೀಲಿಸಿ"))

        # ---------- Rule 2 — EMI burden (15 pts) ----------
        if emi_burden == 0:
            score += 15
            reasons.append(("✅", "No EMI burden — Excellent", "EMI ಹೊರೆ ಇಲ್ಲ — ಅತ್ಯುತ್ತಮ"))
        elif emi_burden <= 30:
            score += 15
            reasons.append(("✅",
                f"EMI {round(emi_burden,1)}% of income — Healthy",
                f"EMI ಆದಾಯದ {round(emi_burden,1)}% — ಆರೋಗ್ಯಕರ"))
        elif emi_burden <= 40:
            score += 8
            reasons.append(("🟡",
                f"EMI {round(emi_burden,1)}% of income — Manageable",
                f"EMI ಆದಾಯದ {round(emi_burden,1)}% — ನಿರ್ವಹಿಸಬಹುದು"))
            advice.append(("Avoid new loans until current EMI is cleared",
                            "ಈಗಿನ EMI ಮುಗಿಯುವವರೆಗೆ ಹೊಸ ಸಾಲ ತಪ್ಪಿಸಿ"))
        else:
            score += 0
            reasons.append(("❌",
                f"EMI {round(emi_burden,1)}% of income — High risk",
                f"EMI ಆದಾಯದ {round(emi_burden,1)}% — ಹೆಚ್ಚಿನ ಅಪಾಯ"))
            advice.append(("EMI burden very high — consider loan restructuring at your bank",
                            "EMI ಹೊರೆ ಬಹಳ ಹೆಚ್ಚು — ನಿಮ್ಮ ಬ್ಯಾಂಕ್‌ನಲ್ಲಿ ಸಾಲ ಪುನರ್ರಚನೆ ಪರಿಗಣಿಸಿ"))

        # ---------- Rule 3 — Emergency fund (15 pts) ----------
        if months_covered >= emergency_target:
            score += 15
            reasons.append(("✅",
                f"Emergency fund covers {round(months_covered,1)} months — Excellent",
                f"ತುರ್ತು ನಿಧಿ {round(months_covered,1)} ತಿಂಗಳುಗಳಿಗೆ ಸಾಕು — ಅತ್ಯುತ್ತಮ"))
        elif months_covered >= 3:
            score += 8
            gap = round((emergency_target * expense) - emergency)
            reasons.append(("🟡",
                f"Emergency fund {round(months_covered,1)} months — Needs improvement",
                f"ತುರ್ತು ನಿಧಿ {round(months_covered,1)} ತಿಂಗಳುಗಳು — ಸುಧಾರಣೆ ಬೇಕು"))
            advice.append((f"Need Rs {gap:,} more to reach {emergency_target} months emergency fund",
                            f"{emergency_target} ತಿಂಗಳ ತುರ್ತು ನಿಧಿ ತಲುಪಲು ಇನ್ನೂ ರೂ {gap:,} ಬೇಕು"))
        else:
            score += 2
            gap = round((emergency_target * expense) - emergency)
            reasons.append(("❌",
                f"Emergency fund only {round(months_covered,1)} months — Critical",
                f"ತುರ್ತು ನಿಧಿ ಕೇವಲ {round(months_covered,1)} ತಿಂಗಳುಗಳು — ಗಂಭೀರ ಕೊರತೆ"))
            advice.append((f"Build emergency fund urgently — need Rs {gap:,} more",
                            f"ತುರ್ತು ನಿಧಿಯನ್ನು ತಕ್ಷಣ ನಿರ್ಮಿಸಿ — ಇನ್ನೂ ರೂ {gap:,} ಬೇಕು"))

        # ---------- Rule 4 — Investment (15 pts) ----------
        if monthly_investment > 0:
            inv_rate = (monthly_investment / salary * 100)
            if inv_rate >= 20:
                score += 15
                reasons.append(("✅",
                    f"Investing {round(inv_rate,1)}% of income — Strong",
                    f"ಆದಾಯದ {round(inv_rate,1)}% ಹೂಡಿಕೆ — ಬಲಿಷ್ಠ"))
            elif inv_rate >= 10:
                score += 10
                reasons.append(("🟡",
                    f"Investing {round(inv_rate,1)}% of income — Good",
                    f"ಆದಾಯದ {round(inv_rate,1)}% ಹೂಡಿಕೆ — ಉತ್ತಮ"))
            else:
                score += 5
                reasons.append(("🟠",
                    f"Investing {round(inv_rate,1)}% of income — Increase this",
                    f"ಆದಾಯದ {round(inv_rate,1)}% ಹೂಡಿಕೆ — ಹೆಚ್ಚಿಸಿ"))
                advice.append(("Increase SIP to at least 10% of monthly income",
                                "SIP ಅನ್ನು ಮಾಸಿಕ ಆದಾಯದ ಕನಿಷ್ಠ 10% ಗೆ ಹೆಚ್ಚಿಸಿ"))
        else:
            score += 0
            reasons.append(("❌", "No investments — Wealth not growing",
                                   "ಹೂಡಿಕೆ ಇಲ್ಲ — ಸಂಪತ್ತು ಬೆಳೆಯುತ್ತಿಲ್ಲ"))
            advice.append(("Start SIP of even Rs 500/month in any index fund today",
                            "ಇಂದೇ ಯಾವುದಾದರೂ ಇಂಡೆಕ್ಸ್ ಫಂಡ್‌ನಲ್ಲಿ ರೂ 500/ಮಾಸಿಕ SIP ಪ್ರಾರಂಭಿಸಿ"))

        # ---------- Rule 5 — Expense ratio (10 pts) ----------
        if expense_ratio <= 40:
            score += 5
            reasons.append(("✅",
                f"Expense ratio {round(expense_ratio,1)}% — Very controlled",
                f"ಖರ್ಚು ಅನುಪಾತ {round(expense_ratio,1)}% — ಚೆನ್ನಾಗಿ ನಿಯಂತ್ರಿತ"))
        elif expense_ratio <= 60:
            score += 3
            reasons.append(("🟡",
                f"Expense ratio {round(expense_ratio,1)}% — Acceptable",
                f"ಖರ್ಚು ಅನುಪಾತ {round(expense_ratio,1)}% — ಸ್ವೀಕಾರಾರ್ಹ"))
        else:
            score += 0
            reasons.append(("❌",
                f"Expense ratio {round(expense_ratio,1)}% — Too high",
                f"ಖರ್ಚು ಅನುಪಾತ {round(expense_ratio,1)}% — ಹೆಚ್ಚು"))
            advice.append(("Track daily expenses for 30 days to find where money is leaking",
                            "ಹಣ ಎಲ್ಲಿ ಖರ್ಚಾಗುತ್ತಿದೆ ಎಂದು ತಿಳಿಯಲು 30 ದಿನ ದಿನನಿತ್ಯದ ಖರ್ಚು ದಾಖಲಿಸಿ"))

        # ---------- Rule 6 — Health insurance (10 pts) ----------
        if health_ins == health_opts[2]:
            score += 10
            reasons.append(("✅", "Full family health insurance — Excellent",
                                   "ಇಡೀ ಕುಟುಂಬಕ್ಕೆ ಆರೋಗ್ಯ ವಿಮೆ — ಅತ್ಯುತ್ತಮ"))
        elif health_ins == health_opts[1]:
            score += 5
            reasons.append(("🟡", "Health insurance for self only — Extend to family",
                                   "ನಿಮಗೆ ಮಾತ್ರ ಆರೋಗ್ಯ ವಿಮೆ — ಕುಟುಂಬಕ್ಕೂ ವಿಸ್ತರಿಸಿ"))
            advice.append(("Extend health insurance to cover full family — one hospitalisation can wipe savings",
                            "ಇಡೀ ಕುಟುಂಬಕ್ಕೆ ಆರೋಗ್ಯ ವಿಮೆ ವಿಸ್ತರಿಸಿ — ಒಂದು ಆಸ್ಪತ್ರೆ ಖರ್ಚು ಎಲ್ಲಾ ಉಳಿತಾಯ ಕಳೆದುಕೊಳ್ಳಬಹುದು"))
        else:
            score += 0
            reasons.append(("❌", "No health insurance — High financial risk",
                                   "ಆರೋಗ್ಯ ವಿಮೆ ಇಲ್ಲ — ಹೆಚ್ಚಿನ ಆರ್ಥಿಕ ಅಪಾಯ"))
            advice.append(("Get health insurance immediately — check Ayushman Bharat (PMJAY) eligibility — it is FREE for eligible families",
                            "ತಕ್ಷಣ ಆರೋಗ್ಯ ವಿಮೆ ಪಡೆಯಿರಿ — ಆಯುಷ್ಮಾನ್ ಭಾರತ್ (PMJAY) ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ — ಅರ್ಹ ಕುಟುಂಬಗಳಿಗೆ ಉಚಿತ"))
            schemes.append({
                "name_en": "Ayushman Bharat PMJAY",
                "name_kn": "ಆಯುಷ್ಮಾನ್ ಭಾರತ್ PMJAY",
                "benefit_en": "Free hospitalisation up to Rs 5 lakh per year for eligible families",
                "benefit_kn": "ಅರ್ಹ ಕುಟುಂಬಗಳಿಗೆ ವರ್ಷಕ್ಕೆ ರೂ 5 ಲಕ್ಷದವರೆಗೆ ಉಚಿತ ಆಸ್ಪತ್ರೆ ಚಿಕಿತ್ಸೆ",
                "action_en": "Check eligibility at pmjay.gov.in or visit nearest CSC centre",
                "action_kn": "pmjay.gov.in ನಲ್ಲಿ ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ ಅಥವಾ ಹತ್ತಿರದ CSC ಕೇಂದ್ರಕ್ಕೆ ಭೇಟಿ ನೀಡಿ"
            })

        # ---------- Rule 7 — Life insurance (8 pts) ----------
        if life_ins == life_opts[2]:
            score += 8
            reasons.append(("✅", "Term plan in place — Family is protected",
                                   "ಟರ್ಮ್ ಪ್ಲಾನ್ ಇದೆ — ಕುಟುಂಬ ಸುರಕ್ಷಿತ"))
        elif life_ins == life_opts[1]:
            score += 4
            reasons.append(("🟡", "LIC/endowment — Consider adding a term plan",
                                   "LIC/ಎಂಡೋಮೆಂಟ್ — ಟರ್ಮ್ ಪ್ಲಾನ್ ಸೇರಿಸುವುದನ್ನು ಪರಿಗಣಿಸಿ"))
            advice.append(("Add a term plan for Rs 1 crore coverage at just Rs 800-1000/month",
                            "ಕೇವಲ ರೂ 800-1000/ಮಾಸಿಕಕ್ಕೆ ರೂ 1 ಕೋಟಿ ಕವರೇಜ್‌ನ ಟರ್ಮ್ ಪ್ಲಾನ್ ಸೇರಿಸಿ"))
        else:
            score += 0
            reasons.append(("❌", "No life insurance — Family unprotected",
                                   "ಜೀವ ವಿಮೆ ಇಲ್ಲ — ಕುಟುಂಬ ಅಸುರಕ್ಷಿತ"))
            advice.append(("Get term life insurance — if you are sole earner this is not optional",
                            "ಟರ್ಮ್ ಜೀವ ವಿಮೆ ಪಡೆಯಿರಿ — ನೀವು ಏಕೈಕ ಆದಾಯ ಗಳಿಸುವವರಾಗಿದ್ದರೆ ಇದು ಕಡ್ಡಾಯ"))

        # ---------- Rule 8 — Informal debt (7 pts) ----------
        if other_debt == debt_opts[0]:
            score += 2
            reasons.append(("✅", "No informal debt — Clean financial position",
                                   "ಅನೌಪಚಾರಿಕ ಸಾಲ ಇಲ್ಲ — ಸ್ವಚ್ಛ ಆರ್ಥಿಕ ಸ್ಥಿತಿ"))
        elif other_debt == debt_opts[1]:
            score += 1
            reasons.append(("🟡", "Small informal debt — Manageable",
                                   "ಸಣ್ಣ ಅನೌಪಚಾರಿಕ ಸಾಲ — ನಿರ್ವಹಿಸಬಹುದು"))
            advice.append(("Clear informal debts first — they carry high hidden interest",
                            "ಮೊದಲು ಅನೌಪಚಾರಿಕ ಸಾಲ ತೀರಿಸಿ — ಅವುಗಳಲ್ಲಿ ಹೆಚ್ಚಿನ ಗುಪ್ತ ಬಡ್ಡಿ ಇರುತ್ತದೆ"))
        elif other_debt == debt_opts[2]:
            score += 1
            reasons.append(("🟠", "Significant informal debt — Needs attention",
                                   "ಗಮನಾರ್ಹ ಅನೌಪಚಾರಿಕ ಸಾಲ — ಗಮನ ಬೇಕು"))
            advice.append(("Create a repayment plan for informal debt immediately",
                            "ಅನೌಪಚಾರಿಕ ಸಾಲಕ್ಕೆ ತಕ್ಷಣ ಮರುಪಾವತಿ ಯೋಜನೆ ರೂಪಿಸಿ"))
        else:
            score += 0
            reasons.append(("❌", "Heavy informal debt — Severely impacts financial health",
                                   "ಭಾರೀ ಅನೌಪಚಾರಿಕ ಸಾಲ — ಆರ್ಥಿಕ ಆರೋಗ್ಯದ ಮೇಲೆ ತೀವ್ರ ಪರಿಣಾಮ"))
            advice.append(("Visit your bank for debt consolidation loan at lower formal interest rate",
                            "ಕಡಿಮೆ ಔಪಚಾರಿಕ ಬಡ್ಡಿ ದರದ ಸಾಲ ಕ್ರೋಡೀಕರಣಕ್ಕಾಗಿ ನಿಮ್ಮ ಬ್ಯಾಂಕ್‌ಗೆ ಭೇಟಿ ನೀಡಿ"))

        # ---------- Rule 9 — Seasonal cash-flow risk (10 pts, farmers only) ----------
        if is_farmer and is_seasonal:
            if harvests_per_year >= 2:
                score += 10
                reasons.append(("✅",
                    f"{harvests_per_year} harvests/year — income spread across the year, lower risk",
                    f"ವರ್ಷಕ್ಕೆ {harvests_per_year} ಸುಗ್ಗಿಗಳು — ಆದಾಯ ವರ್ಷವಿಡೀ ಹರಡಿದೆ, ಕಡಿಮೆ ಅಪಾಯ"))
            elif not seasonal_risk_flag:
                score += 7
                reasons.append(("🟡",
                    "Single harvest, but income covers a longer period — moderate risk",
                    "ಒಂದು ಸುಗ್ಗಿ, ಆದರೆ ಆದಾಯ ದೀರ್ಘಾವಧಿಗೆ ಸಾಕು — ಮಧ್ಯಮ ಅಪಾಯ"))
            else:
                score += 3
                reasons.append(("❌",
                    "Single harvest covering a short period — high cash-flow risk between harvests",
                    "ಒಂದೇ ಸುಗ್ಗಿ ಕಡಿಮೆ ಅವಧಿಗೆ — ಸುಗ್ಗಿಗಳ ನಡುವೆ ಹೆಚ್ಚಿನ ಹಣಕಾಸಿನ ಅಪಾಯ"))
                advice.append(("Your income depends heavily on one harvest — consider a second crop cycle, allied income (dairy/poultry), or KCC to bridge lean months",
                                "ನಿಮ್ಮ ಆದಾಯ ಒಂದೇ ಸುಗ್ಗಿಯ ಮೇಲೆ ಹೆಚ್ಚು ಅವಲಂಬಿತವಾಗಿದೆ — ಎರಡನೇ ಬೆಳೆ, ಪರ್ಯಾಯ ಆದಾಯ (ಹೈನುಗಾರಿಕೆ/ಕೋಳಿ) ಅಥವಾ ಕೊರತೆಯ ತಿಂಗಳುಗಳಿಗೆ KCC ಪರಿಗಣಿಸಿ"))
        elif is_farmer:
            # Farmer chose "regular monthly income" — give full points, no penalty
            score += 10
            reasons.append(("✅", "Regular income pattern — stable cash flow",
                                   "ನಿಯಮಿತ ಆದಾಯ ಮಾದರಿ — ಸ್ಥಿರ ಹಣಕಾಸು ಹರಿವು"))
        else:
            # Non-farmers — this risk dimension doesn't apply, give full points
            score += 10

        # ---------- Scheme recommendations ----------
        if "🌾" in user_type:
            schemes.append({
                "name_en": "Kisan Credit Card (KCC)", "name_kn": "ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್",
                "benefit_en": "Working capital up to Rs 3 lakh at 7% interest after subvention",
                "benefit_kn": "ಸಬ್ಸಿಡಿ ನಂತರ 7% ಬಡ್ಡಿಯಲ್ಲಿ ರೂ 3 ಲಕ್ಷದವರೆಗೆ ಕಾರ್ಯ ಬಂಡವಾಳ",
                "action_en": "Visit nearest bank with land documents and Aadhaar card",
                "action_kn": "ಭೂ ದಾಖಲೆಗಳು ಮತ್ತು ಆಧಾರ್ ಕಾರ್ಡ್‌ನೊಂದಿಗೆ ಹತ್ತಿರದ ಬ್ಯಾಂಕ್‌ಗೆ ಭೇಟಿ ನೀಡಿ"
            })
            schemes.append({
                "name_en": "PM-KISAN", "name_kn": "ಪಿಎಂ ಕಿಸಾನ್",
                "benefit_en": "Rs 6,000 per year direct to your bank account in 3 instalments",
                "benefit_kn": "ವರ್ಷಕ್ಕೆ ರೂ 6,000 ನೇರವಾಗಿ ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ 3 ಕಂತುಗಳಲ್ಲಿ",
                "action_en": "Check status at pmkisan.gov.in or nearest CSC",
                "action_kn": "pmkisan.gov.in ನಲ್ಲಿ ಅಥವಾ ಹತ್ತಿರದ CSC ನಲ್ಲಿ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಿ"
            })
            schemes.append({
                "name_en": "PM Fasal Bima Yojana (PMFBY)", "name_kn": "ಪಿಎಂ ಫಸಲ್ ಬಿಮಾ ಯೋಜನೆ",
                "benefit_en": "Crop insurance against drought, flood and pest at very low premium",
                "benefit_kn": "ಬರ, ಪ್ರವಾಹ ಮತ್ತು ಕೀಟಗಳ ವಿರುದ್ಧ ಬಹಳ ಕಡಿಮೆ ಪ್ರೀಮಿಯಂನಲ್ಲಿ ಬೆಳೆ ವಿಮೆ",
                "action_en": "Apply through your bank or nearest CSC before crop season starts",
                "action_kn": "ಬೆಳೆ ಋತು ಪ್ರಾರಂಭವಾಗುವ ಮೊದಲು ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಅಥವಾ CSC ಮೂಲಕ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ"
            })

        if "🏪" in user_type or "👷" in user_type:
            schemes.append({
                "name_en": "PM MUDRA Loan", "name_kn": "ಮುದ್ರಾ ಸಾಲ",
                "benefit_en": "Collateral-free loan — Shishu up to Rs 50K, Kishore up to Rs 5L, Tarun up to Rs 10L",
                "benefit_kn": "ಭದ್ರತೆ ಇಲ್ಲದ ಸಾಲ — ಶಿಶು ರೂ 50K, ಕಿಶೋರ್ ರೂ 5L, ತರುಣ್ ರೂ 10L ವರೆಗೆ",
                "action_en": "Apply at any bank or visit mudra.org.in",
                "action_kn": "ಯಾವುದೇ ಬ್ಯಾಂಕ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ಅಥವಾ mudra.org.in ಗೆ ಭೇಟಿ ನೀಡಿ"
            })
            schemes.append({
                "name_en": "PMEGP", "name_kn": "PMEGP — ಪ್ರಧಾನ ಮಂತ್ರಿ ಉದ್ಯೋಗ ಸೃಷ್ಟಿ ಕಾರ್ಯಕ್ರಮ",
                "benefit_en": "Subsidy of 15 to 35% on project cost for new business units",
                "benefit_kn": "ಹೊಸ ವ್ಯಾಪಾರ ಘಟಕಗಳಿಗೆ ಪ್ರಾಜೆಕ್ಟ್ ವೆಚ್ಚದ 15 ರಿಂದ 35% ಸಬ್ಸಿಡಿ",
                "action_en": "Apply online at kviconline.gov.in",
                "action_kn": "kviconline.gov.in ನಲ್ಲಿ ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ"
            })

        if goal in ("Buy a house", "ಮನೆ ಕೊಳ್ಳುವುದು"):
            schemes.append({
                "name_en": "PMAY — Pradhan Mantri Awas Yojana", "name_kn": "PMAY — ಪ್ರಧಾನ ಮಂತ್ರಿ ಆವಾಸ್ ಯೋಜನೆ",
                "benefit_en": "Home loan interest subsidy up to Rs 2.67 lakh for eligible families",
                "benefit_kn": "ಅರ್ಹ ಕುಟುಂಬಗಳಿಗೆ ಗೃಹ ಸಾಲದ ಬಡ್ಡಿ ಸಬ್ಸಿಡಿ ರೂ 2.67 ಲಕ್ಷದವರೆಗೆ",
                "action_en": "Apply through your bank or visit pmaymis.gov.in",
                "action_kn": "ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಮೂಲಕ ಅಥವಾ pmaymis.gov.in ಗೆ ಭೇಟಿ ನೀಡಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ"
            })

        # ============================================================
        #  DISPLAY RESULTS — fully language aware
        # ============================================================

        # Log ONLY anonymous aggregate data — no personal details
        log_anonymous_usage(user_type, score, lang)

        st.header(f"{lbl_report} — {name}")

        if score >= 85:
            st.success(f"🏆 {'ಸ್ಕೋರ್' if KN else 'Score'}: {score} / 100 — {'ಅತ್ಯುತ್ತಮ ಆರ್ಥಿಕ ಆರೋಗ್ಯ!' if KN else 'EXCELLENT financial health!'}")
        elif score >= 70:
            st.success(f"👍 {'ಸ್ಕೋರ್' if KN else 'Score'}: {score} / 100 — {'ಉತ್ತಮ ಆರ್ಥಿಕ ಆರೋಗ್ಯ' if KN else 'GOOD financial health'}")
        elif score >= 50:
            st.warning(f"⚠️ {'ಸ್ಕೋರ್' if KN else 'Score'}: {score} / 100 — {'ಸಾಧಾರಣ — ಗಮನ ಬೇಕು' if KN else 'FAIR — needs attention'}")
        else:
            st.error(f"🚨 {'ಸ್ಕೋರ್' if KN else 'Score'}: {score} / 100 — {'ಅಪಾಯದಲ್ಲಿದೆ — ಈಗಲೇ ಕ್ರಮ ತೆಗೆದುಕೊಳ್ಳಿ' if KN else 'AT RISK — take action now'}")

        col1, col2, col3 = st.columns(3)
        col1.metric(lbl_saving, f"Rs {round(monthly_saving):,}")
        col2.metric(lbl_savings_rate, f"{round(savings_rate,1)}%")
        col3.metric(lbl_emi_burden, f"{round(emi_burden,1)}%")

        st.divider()
        st.subheader(lbl_analysis)
        for icon, text_en, text_kn in reasons:
            st.write(f"{icon} {text_kn if KN else text_en}")

        st.divider()
        if advice:
            st.subheader(lbl_advice)
            for tip_en, tip_kn in advice:
                st.info(f"→ {tip_kn if KN else tip_en}")
        else:
            st.success(f"→ {lbl_great}")

        if schemes:
            st.divider()
            st.subheader(lbl_schemes)
            for s in schemes:
                name_show = s["name_kn"] if KN else s["name_en"]
                with st.expander(f"📋 {name_show}"):
                    st.write(f"**{lbl_benefit}:** {s['benefit_kn'] if KN else s['benefit_en']}")
                    st.write(f"**{lbl_apply}:** {s['action_kn'] if KN else s['action_en']}")

        st.divider()
        st.caption(lbl_footer)
