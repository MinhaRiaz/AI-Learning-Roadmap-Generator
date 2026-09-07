# 🎓 AI Learning Roadmap Generator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-learning-roadmap-generator.streamlit.app/)

An AI-powered **Learning Roadmap Generator** that creates personalized, practical, and structured learning plans based on a learner's **domain, skill level, available learning duration, and learning goal**.

The application uses **Groq's API** with the **GPT-OSS 120B** model to generate customized learning roadmaps and is deployed using **Streamlit Community Cloud**.

---

## 🚀 Live Application

👉 **Use the AI Learning Roadmap Generator:**
**[Open Live App](YOUR_STREAMLIT_APP_URL)**

> Replace `YOUR_STREAMLIT_APP_URL` with your actual Streamlit URL after deployment.

Example:

```text
https://your-app-name.streamlit.app
```

Streamlit Community Cloud provides each deployed application with a unique `streamlit.app` URL.

---

## ✨ Features

### 📚 Personalized Learning Roadmaps

Generate a customized roadmap based on:

* Learning domain
* Current skill level
* Available learning duration
* Learning goal

### 📊 Skill Levels

Choose from:

* Beginner
* Intermediate
* Advanced

### 🎯 Learning Goals

The application supports:

* General Knowledge
* University / Academic
* Build Projects
* Internship Preparation
* Job Preparation
* Freelancing
* Career Transition

### 🗺️ Structured Learning Phases

The AI organizes the learning journey into logical phases containing:

* Phase name
* Estimated duration
* Topics to learn
* Skills to develop
* Practical exercises
* Projects
* Milestones

### 📅 Weekly Learning Schedule

The generated roadmap includes a realistic week-by-week learning schedule based on the learner's available duration.

### 🛠️ Project-Based Learning

The application recommends practical projects that gradually increase in difficulty.

### 🏆 Final Project

Each roadmap includes a substantial final project aligned with the learner's:

* Skill level
* Learning domain
* Learning goal

### 📚 Resource Recommendations

The AI recommends useful learning resource types such as:

* Documentation
* Courses
* Tutorials
* Books
* Practice platforms
* YouTube channels

---

## 🧠 How It Works

The application follows this workflow:

```text
User Input
    │
    ├── Learning Domain
    ├── Skill Level
    ├── Learning Duration
    └── Learning Goal
            │
            ▼
      Prompt Construction
            │
            ▼
        Groq API
            │
            ▼
      GPT-OSS 120B Model
            │
            ▼
   Personalized Roadmap
            │
            ▼
      Streamlit Interface
```

---

## 🛠️ Technologies Used

| Technology                | Purpose                      |
| ------------------------- | ---------------------------- |
| Python                    | Application development      |
| Streamlit                 | Web interface and deployment |
| Groq API                  | AI model API                 |
| GPT-OSS 120B              | Roadmap generation           |
| GitHub                    | Source code management       |
| Streamlit Community Cloud | Application deployment       |

---

## 📁 Project Structure

```text
AI-Learning-Roadmap/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml.example
```

### File Description

**`app.py`**
Main Streamlit application containing the user interface and AI roadmap-generation logic.

**`requirements.txt`**
Contains the Python dependencies required by the application.

**`README.md`**
Project documentation.

**`.gitignore`**
Prevents sensitive and unnecessary files from being uploaded to GitHub.

**`.streamlit/secrets.toml.example`**
Example configuration showing how the Groq API key should be stored. The real `secrets.toml` file must not be committed to GitHub.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project directory:

```bash
cd AI-Learning-Roadmap
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 API Configuration

This application requires a **Groq API key**.

### Local Development

You can set the API key as an environment variable.

#### Windows PowerShell

```powershell
$env:GROQ_API_KEY="your_groq_api_key"
```

Then run the application:

```bash
streamlit run app.py
```

---

## ☁️ Streamlit Deployment

The application can be deployed directly from GitHub using **Streamlit Community Cloud**.

### Step 1 — Upload Project to GitHub

Create a GitHub repository and upload:

```text
app.py
requirements.txt
README.md
.gitignore
.streamlit/secrets.toml.example
```

Do **not** upload your actual API key.

---

### Step 2 — Open Streamlit Community Cloud

Go to:

**https://share.streamlit.io/**

Sign in and connect your GitHub account. Streamlit's current deployment flow allows you to select your repository, branch, and entrypoint file.

---

### Step 3 — Create the Application

Select:

```text
Repository: Your GitHub Repository
Branch: main
Main file: app.py
```

Then click:

```text
Deploy
```

---

### Step 4 — Add the Groq API Key

After deployment, open the application's settings and go to **Secrets**.

Add:

```toml
GROQ_API_KEY = "your_actual_groq_api_key"
```

Streamlit recommends storing credentials through its Secrets management rather than committing them to your Git repository.

---

## 🔐 Security

**Never upload your real Groq API key to GitHub.**

Do not commit:

```text
.streamlit/secrets.toml
```

The `.gitignore` file prevents the actual secrets file from being accidentally committed.

Only the example file should be included:

```text
.streamlit/secrets.toml.example
```

---

## 🧪 Example

### User Input

```text
Learning Domain:
Machine Learning

Skill Level:
Beginner

Learning Duration:
3 months

Learning Goal:
Build Projects
```

### AI Output

The application generates:

```text
🎯 Learning Goal

📋 Prerequisites

🗺️ Roadmap Overview

📚 Learning Phases

📅 Weekly Learning Schedule

🛠️ Projects

📚 Recommended Resources

🏆 Final Project

🚀 Next Steps
```

---

## 🎯 Example Use Cases

This application can be used by:

* 🎓 University students
* 💻 Beginners learning programming
* 🤖 AI/ML learners
* 👩‍💻 Developers learning new technologies
* 🚀 Students preparing for internships
* 💼 Job seekers
* 🧑‍💻 Freelancers
* 🔄 Professionals transitioning into a new career

---

## 🔮 Future Improvements

Possible future features include:

* ⏱️ Hours-per-day learning preferences
* 📈 Learning progress tracking
* ✅ Interactive task checklists
* 📝 AI-generated quizzes
* 🧪 Skill assessments
* 📄 Export roadmap as PDF
* 💾 Save and download roadmaps
* 🔗 Verified learning-resource links
* 🔄 Roadmap refinement based on progress
* 🤖 Multi-stage AI workflow
* 👤 User authentication
* 📊 Learning analytics
* 🎯 Personalized milestone tracking

---

## 🔄 AI Workflow

The current application uses a single AI generation stage:

```text
User Requirements
       ↓
Prompt Engineering
       ↓
Groq API
       ↓
GPT-OSS 120B
       ↓
Personalized Roadmap
```

A future version can expand this into a multi-stage AI workflow:

```text
User Profile
     ↓
Planning Agent
     ↓
Content Generation
     ↓
Assessment
     ↓
Review
     ↓
Refinement
     ↓
Final Learning Roadmap
```

---

## 📌 Project Goal

The goal of this project is to make learning more **personalized, structured, practical, and achievable** by using generative AI to create learning roadmaps according to an individual's goals, skill level, and available time.

---

## 👩‍💻 Author

**Minha Bibi**

Computer Science Student | AI & Generative AI Enthusiast

---

## ⭐ Support

If you find this project useful, consider giving the GitHub repository a ⭐.
