finsaathi_v2 = '''
import streamlit as st

st.set_page_config(page_title="FinSaathi", page_icon="💰", layout="centered")

# ── Language toggle ──────────────────────────────────────
lang = st.selectbox("🌐 Language / ಭಾಷೆ", ["English", "ಕನ್ನಡ"])

L = {
    "English": {
        "title": "💰 FinSaathi",
        "subtitle": "Your Personal Financial Health Score Card",
        "details": "📋 Enter Your Details",
        "name": "Your name",
        "usertype": "What do you primarily do?",
        "usertypes": ["🌾 Farmer", "🏪 Small Business", "👷 Self-Employed", "💼 Salaried"],
        "salary": "Monthly income (Rs)",
        "expense": "Monthly expenses (Rs)",
        "emi": "Monthly EMI / loan repayment (Rs, enter 0 if none)",
        "emergency": "Emergency fund / savings (Rs)",
        "dependents": "How many people depend on your income?",
        "invest": "Do you invest in MF / SIP / FD / RD?",
        "invest_opts": ["No", "Yes"],
        "invest_amt": "Monthly investment amount (Rs)",
        "health_ins": "Do you have health insurance?",
        "health_opts": ["No", "Yes — only myself", "Yes — full family covered"],
        "life_ins": "Do you have life insurance or term plan?",
        "life_opts": ["No", "Yes — LIC / endowment", "Yes — term plan"],
        "other_debt": "Any other debt? (informal loans, chit fund, relatives)",
        "debt_opts": ["No other debt", "Yes — less than 1 month income", "Yes — 1 to 6 months income", "Yes — more than 6 months income"],
        "goal": "Your main financial goal right now?",
        "goal_opts": ["Buy a house", "Children education", "Start or grow a business", "Retirement planning", "Debt clearance", "Build emergency fund"],
        "btn": "🔍 Calculate My Financial Health Score",
        "name_warn": "Please enter your name first!",
        "report": "📊 Financial Health Report",
        "saving": "Monthly saving",
        "analysis": "📋 Detailed Analysis",
        "advice": "💡 Personalised Advice",
        "great": "You are doing great! Keep it up.",
        "schemes": "🏛️ Recommended Government Schemes For You",
        "footer": "Built with ❤️ by FinSaathi | Free • Neutral • Trustworthy",
        "score_labels": {85: "🏆 EXCELLENT!", 70: "👍 GOOD", 50: "⚠️ FAIR", 0: "🚨 AT RISK"}
    },
    "ಕನ್ನಡ": {
        "title": "💰 ಫಿನ್‌ಸಾಥಿ",
        "subtitle": "ನಿಮ್ಮ ವೈಯಕ್ತಿಕ ಆರ್ಥಿಕ ಆರೋಗ್ಯ ಸ್ಕೋರ್ ಕಾರ್ಡ್",
        "details": "📋 ನಿಮ್ಮ ವಿವರಗಳನ್ನು ನಮೂದಿಸಿ",
        "name": "ನಿಮ್ಮ ಹೆಸರು",
        "usertype": "ನೀವು ಮುಖ್ಯವಾಗಿ ಏನು ಮಾಡುತ್ತೀರಿ?",
        "usertypes": ["🌾 ರೈತ", "🏪 ಸಣ್ಣ ವ್ಯಾಪಾರ", "👷 ಸ್ವಯಂ ಉದ್ಯೋಗಿ", "💼 ಸಂಬಳದಾರ"],
        "salary": "ಮಾಸಿಕ ಆದಾಯ (ರೂ)",
        "expense": "ಮಾಸಿಕ ಖರ್ಚು (ರೂ)",
        "emi": "ಮಾಸಿಕ EMI / ಸಾಲ ಮರುಪಾವತಿ (ರೂ, ಇಲ್ಲದಿದ್ದರೆ 0)",
        "emergency": "ತುರ್ತು ನಿಧಿ / ಉಳಿತಾಯ (ರೂ)",
        "dependents": "ನಿಮ್ಮ ಆದಾಯದ ಮೇಲೆ ಎಷ್ಟು ಜನ ಅವಲಂಬಿತ?",
        "invest": "ನೀವು MF / SIP / FD / RD ನಲ್ಲಿ ಹೂಡಿಕೆ ಮಾಡುತ್ತೀರಾ?",
        "invest_opts": ["ಇಲ್ಲ", "ಹೌದು"],
        "invest_amt": "ಮಾಸಿಕ ಹೂಡಿಕೆ ಮೊತ್ತ (ರೂ)",
        "health_ins": "ನಿಮಗೆ ಆರೋಗ್ಯ ವಿಮೆ ಇದೆಯೇ?",
        "health_opts": ["ಇಲ್ಲ", "ಹೌದು — ನನಗೆ ಮಾತ್ರ", "ಹೌದು — ಇಡೀ ಕುಟುಂಬಕ್ಕೆ"],
        "life_ins": "ನಿಮಗೆ ಜೀವ ವಿಮೆ ಅಥವಾ ಟರ್ಮ್ ಪ್ಲಾನ್ ಇದೆಯೇ?",
        "life_opts": ["ಇಲ್ಲ", "ಹೌದು — LIC / ಎಂಡೋಮೆಂಟ್", "ಹೌದು — ಟರ್ಮ್ ಪ್ಲಾನ್"],
        "other_debt": "ಬೇರೆ ಯಾವುದಾದರೂ ಸಾಲ ಇದೆಯೇ? (ಅನೌಪಚಾರಿಕ ಸಾಲ, ಚಿಟ್ ಫಂಡ್, ಸಂಬಂಧಿಕರಿಂದ)",
        "debt_opts": ["ಬೇರೆ ಸಾಲ ಇಲ್ಲ", "ಹೌದು — 1 ತಿಂಗಳ ಆದಾಯಕ್ಕಿಂತ ಕಡಿಮೆ", "ಹೌದು — 1 ರಿಂದ 6 ತಿಂಗಳ ಆದಾಯ", "ಹೌದು — 6 ತಿಂಗಳ ಆದಾಯಕ್ಕಿಂತ ಹೆಚ್ಚು"],
        "goal": "ನಿಮ್ಮ ಪ್ರಮುಖ ಆರ್ಥಿಕ ಗುರಿ?",
        "goal_opts": ["ಮನೆ ಕೊಳ್ಳುವುದು", "ಮಕ್ಕಳ ಶಿಕ್ಷಣ", "ವ್ಯಾಪಾರ ಪ್ರಾರಂಭಿಸುವುದು", "ನಿವೃತ್ತಿ ಯೋಜನೆ", "ಸಾಲ ತೀರಿಸುವುದು", "ತುರ್ತು ನಿಧಿ ನಿರ್ಮಾಣ"],
        "btn": "🔍 ನನ್ನ ಆರ್ಥಿಕ ಆರೋಗ್ಯ ಸ್ಕೋರ್ ಲೆಕ್ಕ ಹಾಕಿ",
        "name_warn": "ದಯವಿಟ್ಟು ಮೊದಲು ನಿಮ್ಮ ಹೆಸರು ನಮೂದಿಸಿ!",
        "report": "📊 ಆರ್ಥಿಕ ಆರೋಗ್ಯ ವರದಿ",
        "saving": "ಮಾಸಿಕ ಉಳಿತಾಯ",
        "analysis": "📋 ವಿವರವಾದ ವಿಶ್ಲೇಷಣೆ",
        "advice": "💡 ನಿಮಗಾಗಿ ವೈಯಕ್ತಿಕ ಸಲಹೆ",
        "great": "ನೀವು ಅದ್ಭುತವಾಗಿ ಮಾಡುತ್ತಿದ್ದೀರಿ! ಮುಂದುವರಿಯಿರಿ.",
        "schemes": "🏛️ ನಿಮಗಾಗಿ ಶಿಫಾರಸು ಮಾಡಿದ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು",
        "footer": "FinSaathi ❤️ ನಿರ್ಮಿಸಿದೆ | ಉಚಿತ • ತಟಸ್ಥ • ವಿಶ್ವಾಸಾರ್ಹ",
        "score_labels": {85: "🏆 ಅತ್ಯುತ್ತಮ!", 70: "👍 ಉತ್ತಮ", 50: "⚠️ ಸಾಧಾರಣ", 0: "🚨 ಅಪಾಯದಲ್ಲಿದೆ"}
    }
}

t = L[lang]

# ── Header ───────────────────────────────────────────────
st.title(t["title"])
st.subheader(t["subtitle"])
st.divider()

# ── Inputs ───────────────────────────────────────────────
st.header(t["details"])

name        = st.text_input(t["name"])
user_type   = st.selectbox(t["usertype"], t["usertypes"])
salary      = st.number_input(t["salary"],     min_value=0, value=50000, step=1000)
expense     = st.number_input(t["expense"],    min_value=0, value=25000, step=500)
emi         = st.number_input(t["emi"],        min_value=0, value=0,     step=500)
emergency   = st.number_input(t["emergency"],  min_value=0, value=50000, step=5000)
dependents  = st.number_input(t["dependents"], min_value=0, value=2,     step=1)
invest_ans  = st.selectbox(t["invest"], t["invest_opts"])

monthly_investment = 0
if invest_ans == t["invest_opts"][1]:
    monthly_investment = st.number_input(t["invest_amt"], min_value=0, value=2000, step=500)

health_ins  = st.selectbox(t["health_ins"],  t["health_opts"])
life_ins    = st.selectbox(t["life_ins"],    t["life_opts"])
other_debt  = st.selectbox(t["other_debt"],  t["debt_opts"])
goal        = st.selectbox(t["goal"],        t["goal_opts"])

st.divider()

# ── Calculate ────────────────────────────────────────────
if st.button(t["btn"]):

    if name.strip() == "":
        st.warning(t["name_warn"])
    else:
        monthly_saving = salary - expense - emi
        expense_ratio  = (expense / salary * 100) if salary > 0 else 0
        score   = 0
        reasons = []
        advice  = []
        schemes = []

        # Adjust emergency fund target based on dependents
        emergency_months_needed = 6 + max(0, int(dependents) - 2)

        # ── Rule 1 — Savings rate (20 pts) ───────────────
        savings_rate = (monthly_saving / salary * 100) if salary > 0 else 0
        if savings_rate >= 30:
            score += 20
            reasons.append(("✅", f"Savings rate {round(savings_rate,1)}% — Excellent"))
        elif savings_rate >= 20:
            score += 14
            reasons.append(("🟡", f"Savings rate {round(savings_rate,1)}% — Moderate"))
        elif savings_rate >= 10:
            score += 7
            reasons.append(("🟠", f"Savings rate {round(savings_rate,1)}% — Low"))
            advice.append("Try to save at least 20% of your monthly income")
        else:
            score += 2
            reasons.append(("❌", f"Savings rate {round(savings_rate,1)}% — Critical"))
            advice.append("Your savings are very low — review all expenses urgently")

        # ── Rule 2 — EMI burden (15 pts) ─────────────────
        emi_burden = (emi / salary * 100) if salary > 0 else 0
        if emi_burden == 0:
            score += 15
            reasons.append(("✅", "No EMI burden — Excellent"))
        elif emi_burden <= 30:
            score += 15
            reasons.append(("✅", f"EMI {round(emi_burden,1)}% of income — Healthy"))
        elif emi_burden <= 40:
            score += 8
            reasons.append(("🟡", f"EMI {round(emi_burden,1)}% of income — Manageable"))
            advice.append("Avoid taking new loans until this EMI is cleared")
        else:
            score += 0
            reasons.append(("❌", f"EMI {round(emi_burden,1)}% of income — High risk"))
            advice.append("EMI burden is very high — consider loan restructuring")

        # ── Rule 3 — Emergency fund (15 pts) ─────────────
        months_covered = (emergency / expense) if expense > 0 else 0
        if months_covered >= emergency_months_needed:
            score += 15
            reasons.append(("✅", f"Emergency fund covers {round(months_covered,1)} months — Excellent"))
        elif months_covered >= 3:
            score += 8
            reasons.append(("🟡", f"Emergency fund covers {round(months_covered,1)} months — Needs improvement"))
            gap = round((emergency_months_needed * expense) - emergency)
            advice.append(f"Build emergency fund — need Rs {gap:,} more to reach {emergency_months_needed} months (adjusted for your {int(dependents)} dependents)")
        else:
            score += 2
            reasons.append(("❌", f"Emergency fund only {round(months_covered,1)} months — Critical gap"))
            gap = round((emergency_months_needed * expense) - emergency)
            advice.append(f"Build emergency fund urgently — need Rs {gap:,} more")

        # ── Rule 4 — Investment habit (15 pts) ────────────
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
                advice.append("Increase your monthly SIP/investment to at least 10% of income")
        else:
            score += 0
            reasons.append(("❌", "No investments — Wealth is not growing"))
            advice.append("Start a SIP of even Rs 500/month in any index fund today")

        # ── Rule 5 — Expense ratio (10 pts) ──────────────
        if expense_ratio <= 40:
            score += 10
            reasons.append(("✅", f"Expense ratio {round(expense_ratio,1)}% — Very controlled"))
        elif expense_ratio <= 60:
            score += 6
            reasons.append(("🟡", f"Expense ratio {round(expense_ratio,1)}% — Acceptable"))
        else:
            score += 0
            reasons.append(("❌", f"Expense ratio {round(expense_ratio,1)}% — Too high"))
            advice.append("Track daily expenses for 30 days — find where money is leaking")

        # ── Rule 6 — Health insurance (10 pts) ───────────
        if health_ins == t["health_opts"][2]:
            score += 10
            reasons.append(("✅", "Full family health insurance — Excellent protection"))
        elif health_ins == t["health_opts"][1]:
            score += 5
            reasons.append(("🟡", "Health insurance for self only — Extend to family"))
            advice.append("Extend health insurance to cover your full family — one hospitalisation can wipe out all savings")
        else:
            score += 0
            reasons.append(("❌", "No health insurance — High financial risk"))
            advice.append("Get health insurance immediately — check if you qualify for Ayushman Bharat (PMJAY) which is free for eligible families")
            if "🌾" in user_type:
                schemes.append({
                    "name": "Ayushman Bharat PMJAY",
                    "benefit": "Free hospitalisation up to Rs 5 lakh/year for eligible families",
                    "action": "Check eligibility at pmjay.gov.in or visit your nearest CSC"
                })

        # ── Rule 7 — Life insurance (8 pts) ──────────────
        if life_ins == t["life_opts"][2]:
            score += 8
            reasons.append(("✅", "Term plan in place — Family is protected"))
        elif life_ins == t["life_opts"][1]:
            score += 4
            reasons.append(("🟡", "LIC/endowment policy — Consider adding a term plan"))
            advice.append("LIC endowment gives low coverage — add a term plan for Rs 1 crore at just Rs 800-1000/month")
        else:
            score += 0
            reasons.append(("❌", "No life insurance — Family has no protection"))
            advice.append("Get a term life insurance plan — if you are the sole earner, this is not optional")

        # ── Rule 8 — Other debt burden (7 pts) ───────────
        if other_debt == t["debt_opts"][0]:
            score += 7
            reasons.append(("✅", "No informal debt — Clean financial position"))
        elif other_debt == t["debt_opts"][1]:
            score += 4
            reasons.append(("🟡", "Small informal debt — Manageable"))
            advice.append("Clear informal debts first — they often carry very high hidden interest")
        elif other_debt == t["debt_opts"][2]:
            score += 1
            reasons.append(("🟠", "Significant informal debt — Needs attention"))
            advice.append("Informal debt of 1-6 months income is a serious burden — create a repayment plan")
        else:
            score += 0
            reasons.append(("❌", "Heavy informal debt — Financial health severely impacted"))
            advice.append("Informal debt above 6 months income is critical — visit your bank for a formal debt consolidation loan at lower interest")

        # ── Scheme recommendations ────────────────────────
        if "🌾" in user_type or "🌾" in user_type:
            schemes.append({
                "name": "Kisan Credit Card (KCC) / ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್",
                "benefit": "Working capital up to Rs 3 lakh at just 7% interest (after subvention)",
                "action": "Visit nearest bank branch with land documents and Aadhaar"
            })
            schemes.append({
                "name": "PM-KISAN / ಪಿಎಂ ಕಿಸಾನ್",
                "benefit": "Rs 6,000/year direct to your bank account — 3 instalments of Rs 2,000",
                "action": "Check eligibility and status at pmkisan.gov.in"
            })
            schemes.append({
                "name": "PM Fasal Bima Yojana (PMFBY)",
                "benefit": "Crop insurance against drought, flood, and pest damage at very low premium",
                "action": "Apply through your bank or nearest CSC before crop season"
            })

        if "🏪" in user_type or "👷" in user_type:
            schemes.append({
                "name": "PM MUDRA Loan / ಮುದ್ರಾ ಸಾಲ",
                "benefit": "Collateral-free business loan — Shishu (up to Rs 50K), Kishore (up to Rs 5L), Tarun (up to Rs 10L)",
                "action": "Apply at any bank, NBFC, or mudra.org.in"
            })
            schemes.append({
                "name": "PMEGP — Prime Minister Employment Generation Programme",
                "benefit": "Subsidy of 15-35% on project cost for new manufacturing/service units",
                "action": "Apply online at kviconline.gov.in"
            })

        if goal == t["goal_opts"][0] or goal == "ಮನೆ ಕೊಳ್ಳುವುದು":
            schemes.append({
                "name": "PMAY — Pradhan Mantri Awas Yojana",
                "benefit": "Home loan interest subsidy up to Rs 2.67 lakh for eligible families",
                "action": "Apply through your bank or pmaymis.gov.in"
            })

        if goal == t["goal_opts"][4] or goal == "ಸಾಲ ತೀರಿಸುವುದು":
            advice.insert(0, "Focus all extra savings on highest-interest debt first before investing")

        # ── Display results ───────────────────────────────
        st.header(f"{t['report']} — {name}")

        # Score card
        score_label = ""
        if score >= 85:
            st.success(f"🏆 Score: {score}/100 — {list(t['score_labels'].values())[0]}")
        elif score >= 70:
            st.success(f"👍 Score: {score}/100 — {list(t['score_labels'].values())[1]}")
        elif score >= 50:
            st.warning(f"⚠️ Score: {score}/100 — {list(t['score_labels'].values())[2]}")
        else:
            st.error(f"🚨 Score: {score}/100 — {list(t['score_labels'].values())[3]}")

        col1, col2, col3 = st.columns(3)
        col1.metric("Monthly Saving", f"Rs {round(monthly_saving):,}")
        col2.metric("Savings Rate", f"{round(savings_rate,1)}%")
        col3.metric("EMI Burden", f"{round(emi_burden,1)}%")

        st.divider()

        # Detailed analysis
        st.subheader(t["analysis"])
        for icon, reason in reasons:
            st.write(f"{icon} {reason}")

        st.divider()

        # Advice
        if advice:
            st.subheader(t["advice"])
            for tip in advice:
                st.info(f"→ {tip}")
        else:
            st.success(f"→ {t['great']}")

        # Scheme recommendations
        if schemes:
            st.divider()
            st.subheader(t["schemes"])
            for s in schemes:
                with st.expander(f"📋 {s[\'name\']}"):
                    st.write(f"**Benefit:** {s[\'benefit\']}")
                    st.write(f"**How to apply:** {s[\'action\']}")

        st.divider()
        st.caption(t["footer"])
'''
