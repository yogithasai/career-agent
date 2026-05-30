import streamlit as st
from agent import career_agent

st.title("AI Career Mentor Agent")

skills = st.text_area(
    "Enter your current skills"
)

goal = st.selectbox(
    "Career Goal",
    [
        "AI Engineer",
        "Data Scientist",
        "Software Engineer",
        "Cyber Security Engineer"
    ]
)

if st.button("Generate Roadmap"):

    st.write("🔍 Analyzing Skills")
    st.write("📊 Finding Skill Gaps")
    st.write("💡 Recommending Projects")
    st.write("🧠 Generating Roadmap")

    with st.spinner("Agent analyzing skills..."):
        response = career_agent(skills, goal)

    st.success("Analysis Complete")

    st.markdown(response)