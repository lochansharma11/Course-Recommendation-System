import React from 'react';
import './App.css';

function App() {
  return (
    <div>
      {/* Header */}
      <header className="header">
        <nav className="navbar">
          <div className="logo">
            <a href="/">AI COURSE RECOMMENDATION SYSTEM</a>
          </div>
          <ul className="nav-list">
            <li><a href="/">Home</a></li>
            <li><a href="#about">About</a></li>
            <li>
              <a href="http://localhost:8501/" className="btn-nav" target="_blank" rel="noopener noreferrer">
                Recommend
              </a>
            </li>
          </ul>
        </nav>
      </header>

      {/* Hero Section */}
      <section className="hero">
        <div className="hero-content">
          <h1>Personalized Course Recommendations Powered by AI</h1>
          <p>Get personalized course suggestions based on your skills and interests.</p>
          <a href="http://localhost:8501/" className="btn" target="_blank" rel="noopener noreferrer">
            Get Recommended Courses
          </a>
        </div>
      </section>

      {/* About Section */}
      <section id="about" className="about">
        <h2>About Our Course Recommendation System</h2>
        <p>
          Our AI-powered recommendation system suggests courses tailored to your learning preferences,
          helping you advance in the most efficient way possible.
          Our platform leverages artificial intelligence to analyze user behavior, past course interactions,
          trending skills, and academic goals to provide customized course suggestions.
          Whether you’re a student aiming to strengthen your academic foundation or a professional looking
          to upskill or pivot your career, our recommender system ensures you are always learning the
          right thing at the right time. With real-time updates and intuitive design, it’s like having a
          personal career coach in your browser.
        </p>
      </section>
    </div>
  );
}

export default App;
