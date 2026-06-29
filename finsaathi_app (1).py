
import streamlit as st

# Page config
st.set_page_config(page_title="FinSaathi", page_icon="💰")

# Header
st.title("💰 FinSaathi")
st.subheader("ಕನ್ನಡದಲ್ಲಿ ನಿಮ್ಮ ಹಣಕಾಸಿನ ಗೆಳೆಯ")
st.write("Your personal Financial Health Score Card")
st.divider()

# Input section
st.header("Enter your details")

name = st.text_input("Your name / ನಿಮ್ಮ ಹೆಸರು")
salary = st.number_input("Monthly salary (Rs) / ಮಾಸಿಕ ವೇತನ",
                          min_value=0, value=50000, step=1000)
expense = st.number_input("Monthly expenses (Rs) / ಮಾಸಿಕ ಖರ್ಚು",
                           min_value=0, value=30000, step=1000)
emi = st.number_input("Monthly EMI (Rs, 0 if none) / ಮಾಸಿಕ EMI",
                       min_value=0, value=0, step=500)
emergency = st.number_input("Emergency fund savings (Rs) / ತುರ್ತು ನಿಧಿ",
                             min_value=0, value=100000, step=5000)
invest = st.selectbox("Do you invest in MF/SIP/FD? / ಹೂಡಿಕೆ ಮಾಡುತ್ತೀರಾ?",
                       ["No / ಇಲ್ಲ", "Yes / ಹೌದು"])

monthly_investment = 0
if invest == "Yes / ಹೌದು":
    monthly_investment = st.number_input("Monthly investment (Rs) / ಮಾಸಿಕ ಹೂಡಿಕೆ",
                                          min_value=0, value=2000, step=500)

st.divider()

if st.button("🔍 Calculate my Financial Health Score"):

    if name == "":
        st.warning("Please enter your name first!")
    else:
        monthly_saving = salary - expense - emi
        expense_ratio = (expense / salary) * 100 if salary > 0 else 0
        score = 0
        reasons = []
        advice = []

        savings_rate = (monthly_saving / salary) * 100 if salary > 0 else 0
        if savings_rate >= 30:
            score += 30
            reasons.append(("✅", f"Savings rate {round(savings_rate,1)}% — Excellent"))
        elif savings_rate >= 20:
            score += 20
            reasons.append(("🟡", f"Savings rate {round(savings_rate,1)}% — Moderate"))
        else:
            score += 5
            reasons.append(("❌", f"Savings rate {round(savings_rate,1)}% — Needs improvement"))
            advice.append("Try to save at least 20% of your salary every month")

        emi_burden = (emi / salary) * 100 if salary > 0 else 0
        if emi_burden == 0:
            score += 20
            reasons.append(("✅", "No EMI burden — Excellent"))
        elif emi_burden <= 30:
            score += 20
            reasons.append(("✅", f"EMI is {round(emi_burden,1)}% of salary — Healthy"))
        elif emi_burden <= 40:
            score += 10
            reasons.append(("🟡", f"EMI is {round(emi_burden,1)}% of salary — Manageable"))
        else:
            score += 0
            reasons.append(("❌", f"EMI is {round(emi_burden,1)}% of salary — High risk"))
            advice.append("Avoid taking new loans until EMI burden reduces")

        months_covered = emergency / expense if expense > 0 else 0
        if months_covered >= 6:
            score += 20
            reasons.append(("✅", f"Emergency fund covers {round(months_covered,1)} months — Excellent"))
        elif months_covered >= 3:
            score += 12
            reasons.append(("🟡", f"Emergency fund covers {round(months_covered,1)} months — Needs improvement"))
            gap = round((6 * expense) - emergency)
            advice.append(f"Build emergency fund — need Rs {gap:,} more to reach 6 months")
        else:
            score += 3
            reasons.append(("❌", f"Emergency fund only {round(months_covered,1)} months — Critical gap"))
            gap = round((6 * expense) - emergency)
            advice.append(f"Build emergency fund urgently — need Rs {gap:,} more")

        if monthly_investment > 0:
            inv_rate = (monthly_investment / salary) * 100
            if inv_rate >= 20:
                score += 20
                reasons.append(("✅", f"Investing {round(inv_rate,1)}% of salary — Strong habit"))
            elif inv_rate >= 10:
                score += 12
                reasons.append(("🟡", f"Investing {round(inv_rate,1)}% of salary — Good start"))
            else:
                score += 5
                reasons.append(("🟡", f"Investing {round(inv_rate,1)}% of salary — Increase amount"))
                advice.append("Try to increase your SIP to at least 10% of salary")
        else:
            score += 0
            reasons.append(("❌", "No investments found"))
            advice.append("Start a SIP of even Rs 500/month in any index fund today")

        if expense_ratio <= 40:
            score += 10
            reasons.append(("✅", f"Expense ratio {round(expense_ratio,1)}% — Very controlled"))
        elif expense_ratio <= 60:
            score += 6
            reasons.append(("🟡", f"Expense ratio {round(expense_ratio,1)}% — Acceptable"))
        else:
            score += 0
            reasons.append(("❌", f"Expense ratio {round(expense_ratio,1)}% — Too high"))
            advice.append("Track daily expenses for 30 days to find where money is going")

        st.header(f"📊 {name} Financial Health Report")

        if score >= 85:
            st.success(f"🏆 Score: {score}/100 — EXCELLENT!")
        elif score >= 70:
            st.success(f"👍 Score: {score}/100 — GOOD")
        elif score >= 50:
            st.warning(f"⚠️ Score: {score}/100 — FAIR")
        else:
            st.error(f"🚨 Score: {score}/100 — AT RISK")

        st.write(f"**Monthly saving: Rs {round(monthly_saving):,}**")
        st.divider()

        st.subheader("📋 Detailed Analysis")
        for icon, reason in reasons:
            st.write(f"{icon} {reason}")

        st.divider()

        if advice:
            st.subheader("💡 Personalised Advice")
            for tip in advice:
                st.info(f"→ {tip}")
        else:
            st.success("→ You are doing great! Keep it up.")

        st.divider()
        st.caption("Built with ❤️ by FinSaathi | ಕನ್ನಡದಲ್ಲಿ ನಿಮ್ಮ ಹಣಕಾಸಿನ ಗೆಳೆಯ")
