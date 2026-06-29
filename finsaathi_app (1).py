import streamlit as st

st.set_page_config(page_title="FinSaathi", page_icon="💰", layout="centered")

# Language toggle
lang = st.selectbox("🌐 Language / ಭಾಷೆ", ["English", "ಕನ್ನಡ"])

if lang == "English":
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
    debt_opts = ["No other debt", "Yes — less than 1 month income", "Yes — 1 to 6 months income", "Yes — more than 6 months income"]
    lbl_goal = "Your main financial goal?"
    goal_opts = ["Buy a house", "Children education", "Start or grow business", "Retirement planning", "Debt clearance", "Build emergency fund"]
    lbl_btn = "🔍 Calculate My Financial Health Score"
    lbl_report = "📊 Financial Health Report"
    lbl_analysis = "📋 Detailed Analysis"
    lbl_advice = "💡 Personalised Advice"
    lbl_schemes = "🏛️ Recommended Schemes For You"
    lbl_footer = "Built with ❤️ by FinSaathi | Free • Neutral • Trustworthy"
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
    debt_opts = ["ಸಾಲ ಇಲ್ಲ", "ಹೌದು — 1 ತಿಂಗಳ ಆದಾಯಕ್ಕಿಂತ ಕಡಿಮೆ", "ಹೌದು — 1 ರಿಂದ 6 ತಿಂಗಳ ಆದಾಯ", "ಹೌದು — 6 ತಿಂಗಳ ಆದಾಯಕ್ಕಿಂತ ಹೆಚ್ಚು"]
    lbl_goal = "ನಿಮ್ಮ ಪ್ರಮುಖ ಆರ್ಥಿಕ ಗುರಿ?"
    goal_opts = ["ಮನೆ ಕೊಳ್ಳುವುದು", "ಮಕ್ಕಳ ಶಿಕ್ಷಣ", "ವ್ಯಾಪಾರ ಪ್ರಾರಂಭಿಸುವುದು", "ನಿವೃತ್ತಿ ಯೋಜನೆ", "ಸಾಲ ತೀರಿಸುವುದು", "ತುರ್ತು ನಿಧಿ ನಿರ್ಮಾಣ"]
    lbl_btn = "🔍 ನನ್ನ ಆರ್ಥಿಕ ಆರೋಗ್ಯ ಸ್ಕೋರ್ ಲೆಕ್ಕ ಹಾಕಿ"
    lbl_report = "📊 ಆರ್ಥಿಕ ಆರೋಗ್ಯ ವರದಿ"
    lbl_analysis = "📋 ವಿವರವಾದ ವಿಶ್ಲೇಷಣೆ"
    lbl_advice = "💡 ವೈಯಕ್ತಿಕ ಸಲಹೆ"
    lbl_schemes = "🏛️ ಶಿಫಾರಸು ಮಾಡಿದ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು"
    lbl_footer = "FinSaathi ❤️ | ಉಚಿತ • ತಟಸ್ಥ • ವಿಶ್ವಾಸಾರ್ಹ"

# Header
st.title(title)
st.subheader(subtitle)
st.divider()

# Inputs
name = st.text_input(lbl_name)
user_type = st.selectbox(lbl_type, type_opts)
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

if st.button(lbl_btn):

    if name.strip() == "":
        st.warning("Please enter your name! / ದಯವಿಟ್ಟು ಹೆಸರು ನಮೂದಿಸಿ!")
    else:
        monthly_saving = salary - expense - emi
        expense_ratio = (expense / salary * 100) if salary > 0 else 0
        savings_rate = (monthly_saving / salary * 100) if salary > 0 else 0
        emi_burden = (emi / salary * 100) if salary > 0 else 0
        months_covered = (emergency / expense) if expense > 0 else 0
        emergency_target = 6 + max(0, int(dependents) - 2)

        score = 0
        reasons = []
        advice = []
        schemes = []

        # Rule 1 — Savings rate (20 pts)
        if savings_rate >= 30:
            score += 20
            reasons.append(("✅", f"Savings rate {round(savings_rate,1)}% — Excellent"))
        elif savings_rate >= 20:
            score += 14
            reasons.append(("🟡", f"Savings rate {round(savings_rate,1)}% — Moderate"))
        elif savings_rate >= 10:
            score += 7
            reasons.append(("🟠", f"Savings rate {round(savings_rate,1)}% — Low"))
            advice.append("Save at least 20% of your monthly income")
        else:
            score += 2
            reasons.append(("❌", f"Savings rate {round(savings_rate,1)}% — Critical"))
            advice.append("Savings are very low — review all expenses urgently")

        # Rule 2 — EMI burden (15 pts)
        if emi_burden == 0:
            score += 15
            reasons.append(("✅", "No EMI burden — Excellent"))
        elif emi_burden <= 30:
            score += 15
            reasons.append(("✅", f"EMI {round(emi_burden,1)}% of income — Healthy"))
        elif emi_burden <= 40:
            score += 8
            reasons.append(("🟡", f"EMI {round(emi_burden,1)}% of income — Manageable"))
            advice.append("Avoid new loans until current EMI is cleared")
        else:
            score += 0
            reasons.append(("❌", f"EMI {round(emi_burden,1)}% of income — High risk"))
            advice.append("EMI burden very high — consider loan restructuring at your bank")

        # Rule 3 — Emergency fund (15 pts)
        if months_covered >= emergency_target:
            score += 15
            reasons.append(("✅", f"Emergency fund covers {round(months_covered,1)} months — Excellent"))
        elif months_covered >= 3:
            score += 8
            reasons.append(("🟡", f"Emergency fund {round(months_covered,1)} months — Needs improvement"))
            gap = round((emergency_target * expense) - emergency)
            advice.append(f"Need Rs {gap:,} more to reach {emergency_target} months emergency fund")
        else:
            score += 2
            reasons.append(("❌", f"Emergency fund only {round(months_covered,1)} months — Critical"))
            gap = round((emergency_target * expense) - emergency)
            advice.append(f"Build emergency fund urgently — need Rs {gap:,} more")

        # Rule 4 — Investment (15 pts)
        if monthly_investment > 0:
            inv_rate = (monthly_investment / salary * 100)
            if inv_rate >= 20:
                score += 15
                reasons.append(("✅", f"Investing {round(inv_rate,1)}% of income — Strong"))
            elif inv_rate >= 10:
                score += 10
                reasons.append(("🟡", f"Investing {round(inv_rate,1)}% of income — Good"))
            else:
                score += 5
                reasons.append(("🟠", f"Investing {round(inv_rate,1)}% of income — Increase this"))
                advice.append("Increase SIP to at least 10% of monthly income")
        else:
            score += 0
            reasons.append(("❌", "No investments — Wealth not growing"))
            advice.append("Start SIP of even Rs 500/month in any index fund today")

        # Rule 5 — Expense ratio (10 pts)
        if expense_ratio <= 40:
            score += 10
            reasons.append(("✅", f"Expense ratio {round(expense_ratio,1)}% — Very controlled"))
        elif expense_ratio <= 60:
            score += 6
            reasons.append(("🟡", f"Expense ratio {round(expense_ratio,1)}% — Acceptable"))
        else:
            score += 0
            reasons.append(("❌", f"Expense ratio {round(expense_ratio,1)}% — Too high"))
            advice.append("Track daily expenses for 30 days to find where money is leaking")

        # Rule 6 — Health insurance (10 pts)
        if health_ins == health_opts[2]:
            score += 10
            reasons.append(("✅", "Full family health insurance — Excellent"))
        elif health_ins == health_opts[1]:
            score += 5
            reasons.append(("🟡", "Health insurance for self only — Extend to family"))
            advice.append("Extend health insurance to cover full family — one hospitalisation can wipe savings")
        else:
            score += 0
            reasons.append(("❌", "No health insurance — High financial risk"))
            advice.append("Get health insurance immediately — check Ayushman Bharat (PMJAY) eligibility — it is FREE for eligible families")
            schemes.append({
                "name": "Ayushman Bharat PMJAY",
                "benefit": "Free hospitalisation up to Rs 5 lakh per year for eligible families",
                "action": "Check eligibility at pmjay.gov.in or visit nearest CSC centre"
            })

        # Rule 7 — Life insurance (8 pts)
        if life_ins == life_opts[2]:
            score += 8
            reasons.append(("✅", "Term plan in place — Family is protected"))
        elif life_ins == life_opts[1]:
            score += 4
            reasons.append(("🟡", "LIC/endowment — Consider adding a term plan"))
            advice.append("Add a term plan for Rs 1 crore coverage at just Rs 800-1000/month")
        else:
            score += 0
            reasons.append(("❌", "No life insurance — Family unprotected"))
            advice.append("Get term life insurance — if you are sole earner this is not optional")

        # Rule 8 — Informal debt (7 pts)
        if other_debt == debt_opts[0]:
            score += 7
            reasons.append(("✅", "No informal debt — Clean financial position"))
        elif other_debt == debt_opts[1]:
            score += 4
            reasons.append(("🟡", "Small informal debt — Manageable"))
            advice.append("Clear informal debts first — they carry high hidden interest")
        elif other_debt == debt_opts[2]:
            score += 1
            reasons.append(("🟠", "Significant informal debt — Needs attention"))
            advice.append("Create a repayment plan for informal debt immediately")
        else:
            score += 0
            reasons.append(("❌", "Heavy informal debt — Severely impacts financial health"))
            advice.append("Visit your bank for debt consolidation loan at lower formal interest rate")

        # Scheme recommendations by user type
        if "🌾" in user_type or "ರೈತ" in user_type:
            schemes.append({
                "name": "Kisan Credit Card (KCC) / ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್",
                "benefit": "Working capital up to Rs 3 lakh at 7% interest after subvention",
                "action": "Visit nearest bank with land documents and Aadhaar card"
            })
            schemes.append({
                "name": "PM-KISAN / ಪಿಎಂ ಕಿಸಾನ್",
                "benefit": "Rs 6,000 per year direct to your bank account in 3 instalments",
                "action": "Check status at pmkisan.gov.in or nearest CSC"
            })
            schemes.append({
                "name": "PM Fasal Bima Yojana (PMFBY)",
                "benefit": "Crop insurance against drought, flood and pest at very low premium",
                "action": "Apply through your bank or nearest CSC before crop season starts"
            })

        if "🏪" in user_type or "👷" in user_type or "ವ್ಯಾಪಾರ" in user_type or "ಉದ್ಯೋಗಿ" in user_type:
            schemes.append({
                "name": "PM MUDRA Loan / ಮುದ್ರಾ ಸಾಲ",
                "benefit": "Collateral-free loan — Shishu up to Rs 50K, Kishore up to Rs 5L, Tarun up to Rs 10L",
                "action": "Apply at any bank or visit mudra.org.in"
            })
            schemes.append({
                "name": "PMEGP — PM Employment Generation Programme",
                "benefit": "Subsidy of 15 to 35% on project cost for new business units",
                "action": "Apply online at kviconline.gov.in"
            })

        if "house" in goal.lower() or "ಮನೆ" in goal:
            schemes.append({
                "name": "PMAY — Pradhan Mantri Awas Yojana",
                "benefit": "Home loan interest subsidy up to Rs 2.67 lakh for eligible families",
                "action": "Apply through your bank or visit pmaymis.gov.in"
            })

        # Display results
        st.header(f"{lbl_report} — {name}")

        if score >= 85:
            st.success(f"🏆 Score: {score} / 100 — EXCELLENT financial health!")
        elif score >= 70:
            st.success(f"👍 Score: {score} / 100 — GOOD financial health")
        elif score >= 50:
            st.warning(f"⚠️ Score: {score} / 100 — FAIR — needs attention")
        else:
            st.error(f"🚨 Score: {score} / 100 — AT RISK — take action now")

        col1, col2, col3 = st.columns(3)
        col1.metric("Monthly Saving", f"Rs {round(monthly_saving):,}")
        col2.metric("Savings Rate", f"{round(savings_rate,1)}%")
        col3.metric("EMI Burden", f"{round(emi_burden,1)}%")

        st.divider()
        st.subheader(lbl_analysis)
        for icon, reason in reasons:
            st.write(f"{icon} {reason}")

        st.divider()
        if advice:
            st.subheader(lbl_advice)
            for tip in advice:
                st.info(f"→ {tip}")
        else:
            st.success("→ You are doing great! Keep it up.")

        if schemes:
            st.divider()
            st.subheader(lbl_schemes)
            for s in schemes:
                with st.expander(f"📋 {s['name']}"):
                    st.write(f"**Benefit:** {s['benefit']}")
                    st.write(f"**How to apply:** {s['action']}")

        st.divider()
        st.caption(lbl_footer)
