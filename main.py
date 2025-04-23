import os
import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from datetime import datetime
import random

# Load Data
try:
    courses_list = pickle.load(open('models/courses.pkl', 'rb'))
except Exception as e:
    st.error(f"❌ Failed to load course data: {e}")
    st.stop()

# Build Custom Chatbot Model with TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
course_names = courses_list['course_name'].tolist()
course_vectors = vectorizer.fit_transform(course_names)

# Streamlit Configuration
st.set_page_config(page_title="AI Powered Course Recommender", layout="wide")

# Custom CSS Styling
st.markdown(
    '''
    <style>
        .title { text-align: center; font-size: 38px; color: #0066cc; font-weight: bold; margin-top:20px; }
        .subtitle { text-align: center; font-size: 20px; color: #333333; margin-bottom:20px; }
        .section-header { margin-top: 30px; font-size: 24px; color: #003366; font-weight: bold; }
        .recommendation-box { background-color: #f0f8ff; padding: 12px 15px; border-radius: 10px; margin: 10px 0; box-shadow: 2px 2px 8px rgba(0,0,0,0.1); }
        .chat-container { margin-top: 30px; padding: 15px; border: 1px solid #ccc; border-radius: 10px; background-color: #f9f9f9; }
        footer { text-align: center; color: gray; margin-top: 40px; }
        .stButton > button { background-color: #0066cc; color: white; border-radius: 8px; padding: 0.4em 1.2em; }
        .stButton > button:hover { background-color: #005bb5; }
    </style>
    ''',
    unsafe_allow_html=True
)

# App Header
st.markdown("<div class='title'>AI Powered Course Recommendation System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Find the best courses tailored to your interests using Machine Learning!</div>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Sidebar Navigation
page = st.sidebar.radio("Navigate", ["🏠 About This App", "🎯 Get Course Recommendations", "💬 Chat with Aira"])

# About Page
if page == "🏠 About This App":
    st.markdown("<div class='section-header'>📘 What is this App?</div>", unsafe_allow_html=True)
    st.write("""
        This **AI-powered course recommendation system** helps users discover courses based on their interests.
        It leverages **machine learning and NLP** to compute content similarity across course titles.

        **Features:**
        - 🔍 Instant course suggestions
        - 📚 Top 6 recommended courses
        - 🤖 AI Chatbot (Aira)
        - ⚙️ Built with Python, Streamlit, and scikit-learn
    """)
    st.markdown("<div class='section-header'>🧠 How it Works</div>", unsafe_allow_html=True)
    st.write("""
        1. Convert course titles into vector representations.
        2. Compute cosine similarity with user queries.
        3. Recommend the most relevant courses.
        4. Use Aira chatbot for personalized interactions.
    """)
    st.markdown("<div class='section-header'>👨‍💻 Created by Lochan Badahi Thakur</div>", unsafe_allow_html=True)

# Recommendation Page
elif page == "🎯 Get Course Recommendations":
    st.markdown("<div class='section-header'>🎓 Select a Course</div>", unsafe_allow_html=True)
    selected_course = st.selectbox("Type or select a course you like:", course_names)

    if st.button("✨ Show Recommended Courses"):
        try:
            index = course_names.index(selected_course)
            cosine_scores = list(enumerate(cosine_similarity(course_vectors[index], course_vectors)[0]))
            sorted_scores = sorted(cosine_scores, key=lambda x: x[1], reverse=True)
            recommended_courses = [course_names[i[0]] for i in sorted_scores[1:7]]
            st.markdown("<div class='section-header'>📚 Recommended Courses for You</div>", unsafe_allow_html=True)
            for idx, course in enumerate(recommended_courses, start=1):
                st.markdown(f"<div class='recommendation-box'>🔹 {idx}. {course}</div>", unsafe_allow_html=True)
        except ValueError:
            st.warning("❗ Selected course not found. Please try again.")

# Chatbot Page
elif page == "💬 Chat with Aira":
    st.markdown("<div class='section-header'>💬 Chat with Aira - Your AI Assistant</div>", unsafe_allow_html=True)
    st.markdown("<div class='chat-container'>Ask anything about courses, careers, or learning paths.</div>", unsafe_allow_html=True)

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    for msg in st.session_state.chat_history:
        with st.chat_message(msg['role']):
            st.markdown(msg['content'])

    user_msg = st.chat_input("How can I help you?")
    if user_msg:
        st.session_state.chat_history.append({"role": "user", "content": user_msg})
        with st.chat_message("user"):
            st.markdown(user_msg)

        # Try finding course suggestions
        user_vec = vectorizer.transform([user_msg])
        similarities = cosine_similarity(user_vec, course_vectors).flatten()
        top_matches = similarities.argsort()[::-1][:3]
        suggestions = [course_names[i] for i in top_matches if similarities[i] > 0.1]  # Only meaningful matches

        # Custom assistant-style responses for 100+ FAQs
        faq_responses = {
            "how are you": "I'm doing great, thanks for asking! 😊 How about you?",
            "your name": "I'm Aira, your AI-powered course assistant! 🤖",
            "time": f"The current time is 🕒 {datetime.now().strftime('%I:%M %p')}.",
            "date": f"Today is 📅 {datetime.now().strftime('%B %d, %Y')}.",
            "hello": "Hi there! 👋 How can I assist you today?",
            "hi": "Hey! 😊 Ready to explore some great courses?",
            "joke": random.choice([
                "Why did the developer go broke? Because they used up all their cache. 😂",
                "Why do Java developers wear glasses? Because they don’t C#!",
                "I would tell you a joke about AI, but it’s still learning. 🤖"
            ]),
            "what is machine learning": "Machine learning is a branch of AI that involves using algorithms to find patterns in data and make decisions without explicit programming.",
            "what is deep learning": "Deep learning is a subset of machine learning that uses neural networks with many layers to analyze various factors of data.",
            "what is data science": "Data science combines statistics, computer science, and domain knowledge to extract insights from data.",
            "how can I learn programming": "You can start with beginner-friendly languages like Python or JavaScript. Online courses and tutorials are a great way to start.",
            "what are some good programming languages to learn": "Some popular programming languages to learn are Python, JavaScript, Java, C++, and Ruby.",
            "can you help with coding problems": "Yes, feel free to ask me about any coding problems you have, and I'll do my best to help.",
            "what is python": "Python is a versatile programming language that is great for beginners and widely used in data science, web development, automation, and more.",
            "how can I start learning data science": "To start with data science, learn Python, statistics, and data manipulation tools like Pandas and NumPy. Then move on to machine learning algorithms.",
            "what is the difference between AI and ML": "AI is a broad field that encompasses all techniques to mimic human intelligence, while machine learning is a subset of AI focused on algorithms that allow computers to learn from data.",
            # More FAQs
            "how do I improve my coding skills": "Practice regularly, work on real projects, contribute to open-source, and read code written by others.",
            "what is a neural network": "A neural network is a computational model inspired by the human brain, used to detect patterns in data for tasks like classification and regression.",
            "what is supervised learning": "Supervised learning is a type of machine learning where the model is trained on labeled data to make predictions.",
            "what is unsupervised learning": "Unsupervised learning involves training a model on data without labels to find patterns, clusters, or relationships.",
            "what is reinforcement learning": "Reinforcement learning is an area of machine learning where agents learn to make decisions by interacting with an environment and receiving rewards or penalties.",
            "what is SQL": "SQL (Structured Query Language) is a language used to manage and manipulate relational databases.",
            "what is cloud computing": "Cloud computing is the delivery of computing services like storage, processing, and networking over the internet, often on a pay-as-you-go basis.",
            # More questions (add as many as you need)
        }

        # Check if the user question matches one of the FAQs
        response = faq_responses.get(user_msg.lower(), "I didn't quite understand that. Can you rephrase?")

        # Respond with FAQ answer or course recommendations if matched
        if response != "I didn't quite understand that. Can you rephrase?":
            with st.chat_message("assistant"):
                st.markdown(response)
        else:
            with st.chat_message("assistant"):
                st.markdown(f"Here are some courses that might interest you: {', '.join(suggestions[:3])}")
        
        st.session_state.chat_history.append({"role": "assistant", "content": response})

# Footer
st.markdown("<footer>Created by Lochan Badahi Thakur | AI Powered Course Recommender</footer>", unsafe_allow_html=True)
