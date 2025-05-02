import streamlit as st
from agent_graph import run_policy_assistant

st.title("📜 AI Policy Understanding Assistant")

uploaded_file = st.file_uploader("Upload your insurance policy (PDF)", type=["pdf"])
query = st.text_input("What would you like to know from this policy?")
user_age = st.slider("Your Age", 18, 100, 34)
user_location = st.text_input("Your Location", value="Texas")
user_plan = st.selectbox("Your Plan Type", ["Basic", "Standard", "Premium"])
print(f"user_age = {user_age} | user_location = {user_location} | user_plan = {user_plan}")
if st.button("Understand My Policy") and uploaded_file and query:
    output = run_policy_assistant(uploaded_file, query, {
        "age": user_age, "location": user_location, "plan": user_plan
    })
    st.subheader("📄 Answer")
    st.write(output["Explanation"])
    st.subheader("💡 Personalized Tip")
    st.write(output["Personalized_Tip"])
    # st.subheader("📌 Clause Reference")
    # st.write(output["Relevant Clause"])
    st.subheader("🔁 Was this helpful?")
    feedback = st.radio("Feedback", ["👍 Yes", "👎 No"])
    # Optionally store feedback here
