import streamlit as st
from app import calculate_total, calculate_discount

st.set_page_config(page_title="Price & Discount Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Price & Discount Calculator")
st.write("Calculate the total amount and discounted price easily.")

# Inputs
col1, col2 = st.columns(2)
with col1:
    price = st.number_input("Item Price ($)", min_value=0.0, value=100.0, step=1.0)
with col2:
    quantity = st.number_input("Quantity", min_value=1, value=2, step=1)

discount = st.slider("Discount (%)", min_value=0.0, max_value=100.0, value=10.0, step=1.0)

# Calculations
total = calculate_total(price, quantity)
final_amount = calculate_discount(total, discount)
savings = total - final_amount

st.divider()

# Results
st.subheader("Calculation Summary")
res1, res2, res3 = st.columns(3)
res1.metric("Total Amount", f"${total:,.2f}")
res2.metric("Discount Applied", f"${savings:,.2f}", delta=f"-{discount:.0f}%")
res3.metric("Final Amount", f"${final_amount:,.2f}")

if savings > 0:
    st.success(f"You save ${savings:,.2f} with this discount!")
