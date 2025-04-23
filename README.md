# Course Recommendation System 🚀

A Dockerized machine learning-based web application that recommends similar courses from a dataset of over 3,000 courses on Coursera. The app uses text vectorization and cosine similarity to provide personalized course recommendations based on user input.

## Features 🔥
- Data preprocessing and cleaning
- Vectorization of course descriptions and skills using `sklearn`
- Cosine similarity-based course recommendation engine
- Interactive web interface built with `Streamlit`
- Fully Dockerized for easy deployment

## Table of Contents 📑
- [Installation](#installation )
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Docker](#docker)
- [Contributing](#contributing)
- [Contact](#contact)

## Installation 🛠️

To run the project locally, follow these steps:

1. Clone the repository:
   ```bash
  
   cd Course-Recommendation-System
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # Mac/Linux
   .\env\Scripts\activate   # Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Project Structure 🗂️

```
Course-Recommendation-System/
├── Data/
│   └── Coursera.csv                                  # Coursera dataset
├── models/
│   ├── course_list.pkl                               # Precomputed similarity matrix
│   └── courses.pkl                                   # Processed course list
├── main.py                                           # Streamlit app script
├── CourseRecommendationSystem.py                     # Data preprocessing and model training script 
├── requirements.txt                                  # Python dependencies
├── Dockerfile                                        # Docker configuration
└── README.md                                         # Project README file
```

## Usage ⚙️

1. **Run the preprocessing and model training script**:
   ```bash
   python CourseRecommendationSystem.py
   ```

2. **Run the Streamlit application**:
   ```bash
   streamlit run main.py
   ```

3. **Navigate to the local URL (http://localhost:8501)** to use the web app.

## Docker Hub 🐳

To directly use the project from Docker Hub

1. **Pull the pre-built Docker image**:
   ```bash
   docker pull ganeshpinnamaneni/course-recommendation-system:latest
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 8501:8501 ganeshpinnamaneni/course-recommendation-system:latest
   ```

3. **Access the web app** at [http://localhost:8501](http://localhost:8501).


## Contributing 🤝

We welcome contributions to improve the Course Recommendation System. Here's how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.



