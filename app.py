import os
import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Learning Roadmap Generator",
    page_icon="🎓",
    layout="wide"
)

MODEL_NAME = "openai/gpt-oss-120b"

SYSTEM_PROMPT = """
You are an expert AI learning-roadmap architect.

Create personalized, realistic, structured, and practical learning
roadmaps for users.

The roadmap must:
1. Adapt to the user's current skill level.
2. Respect the user's available learning duration.
3. Consider the user's learning goal.
4. Organize learning into logical phases.
5. Explain topics in each phase.
6. Include practical exercises.
7. Include projects appropriate for the user's level.
8. Include milestones.
9. Include a realistic weekly learning schedule.
10. Recommend useful learning resources.
11. Clearly identify the final project.
12. Make the roadmap achievable within the available time.
13. Prioritize practical, project-based learning.

Use clear Markdown formatting.
Do not overload the learner with unrealistic amounts of content.
Do not invent specific URLs.
"""


def get_api_key():
    try:
        if "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

    return os.getenv("GROQ_API_KEY")


def generate_roadmap(domain, level, duration, goal):

    domain = domain.strip()
    duration = duration.strip()

    if not domain:
        return "⚠️ Please enter a learning domain."

    if not duration:
        return "⚠️ Please enter your available learning time."

    if not level:
        return "⚠️ Please select your skill level."

    if not goal:
        return "⚠️ Please select your learning goal."

    api_key = get_api_key()

    if not api_key:
        return (
            "⚠️ **Groq API key is not configured.**\n\n"
            "Open your Streamlit app settings → Secrets "
            "and add your `GROQ_API_KEY`."
        )

    prompt = f"""
Create a personalized learning roadmap using the following learner information:

Learning Domain:
{domain}

Current Skill Level:
{level}

Available Learning Time:
{duration}

Learning Goal:
{goal}

Create the roadmap with this structure:

# 🎯 Learning Goal
Explain what the learner should be able to achieve by the end.

# 📋 Prerequisites
List the knowledge or skills the learner should already have.

# 🗺️ Roadmap Overview
Give a short overview of the complete learning journey.

# 📚 Learning Phases
For each phase include:
- Phase name
- Estimated duration
- Topics to learn
- Skills to develop
- Practical exercises
- Project
- Milestone

Create as many phases as realistically necessary for the available duration.

# 📅 Weekly Learning Schedule
Break the roadmap into a realistic week-by-week schedule.

# 🛠️ Projects
Recommend practical projects that increase in difficulty.

# 📚 Recommended Resources
Recommend useful resource types such as documentation, courses,
tutorials, books, practice platforms, and YouTube channels.
Do not invent specific URLs.

# 🏆 Final Project
Suggest one substantial final project matching the learner's level and goal.

# 🚀 Next Steps
Explain what the learner should do after completing the roadmap.

Make the roadmap realistic for the available time and specifically
tailored to the selected learning goal.
"""

    try:
        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.4
        )

        return response.choices[0].message.content

    except Exception as e:
        return (
            "⚠️ **Unable to generate the roadmap.**\n\n"
            f"Error: `{str(e)}`"
        )


# -----------------------------
# Streamlit UI
# -----------------------------

st.title("🎓 AI Learning Roadmap Generator")

st.write(
    "Generate a personalized learning roadmap based on your "
    "domain, skill level, available time, and learning goal."
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    domain = st.text_input(
        "📚 Learning Domain",
        placeholder="e.g. Machine Learning"
    )

    level = st.selectbox(
        "📊 Skill Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )


with col2:

    duration = st.text_input(
        "⏳ Learning Duration",
        placeholder="e.g. 3 months"
    )

    goal = st.selectbox(
        "🎯 Learning Goal",
        [
            "General Knowledge",
            "University / Academic",
            "Build Projects",
            "Internship Preparation",
            "Job Preparation",
            "Freelancing",
            "Career Transition"
        ]
    )


st.divider()

if st.button(
    "🚀 Generate Roadmap",
    type="primary",
    use_container_width=True
):

    with st.spinner("🧠 Creating your personalized roadmap..."):

        roadmap = generate_roadmap(
            domain,
            level,
            duration,
            goal
        )

    st.subheader("🗺️ Your Personalized Roadmap")

    st.markdown(roadmap)


st.divider()

st.caption("Powered by Groq + Streamlit")