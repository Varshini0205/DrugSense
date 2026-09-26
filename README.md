DrugSense
Patient Drug Review Analysis & Medical Condition Classification System

DrugSense is an NLP and machine-learning web application that analyzes patient drug reviews and extracts structured information such as medications, symptoms, side effects, treatment response, sentiment, temporal information, and causal relationships.

The system also uses a TF-IDF + Linear SVM model to classify the medical condition associated with a patient review.

Medical Disclaimer: DrugSense is an educational and research-oriented system. Its predictions and extracted information are based on the underlying dataset and NLP/ML models and should not be interpreted as a medical diagnosis, clinical recommendation, or medically verified causal relationship.

✨ Features
🧠 Advanced NLP Pipeline

DrugSense processes patient reviews through a modular NLP pipeline containing:

Text preprocessing
Sentence analysis
Drug, condition, and symptom extraction
Entity normalization
Negation detection
Uncertainty detection
Medication dosage extraction
Medication frequency extraction
Medication duration extraction
Severity detection
Relation extraction
Causality detection
Side-effect detection
Coreference resolution
Experiencer detection
Discourse-role classification
Sentiment analysis
Aspect-based sentiment analysis
Treatment-response detection
Comparative change detection
Event extraction
Temporal information extraction
Timeline construction
Semantic similarity

All components are orchestrated through a central NLP pipeline.

🤖 Machine Learning

DrugSense uses machine learning to classify the medical condition associated with a patient review.

Model Pipeline

Patient Review → Text Preprocessing → TF-IDF → Linear SVM → Predicted Condition

Several approaches were evaluated during development, including:

Logistic Regression
Linear SVM
TF-IDF unigram and bigram features
Model comparison
Condition-level error analysis
Confusion analysis
Class-imbalance analysis
Final Memory-Safe Model

The final practical model uses:

Algorithm: Linear Support Vector Machine
Feature representation: TF-IDF
TF-IDF features: 100,000
Number of classes: 791
Validation Results
Metric	Score
Accuracy	76.76%
Macro F1	50.90%
Weighted F1	76.94%

These results describe performance on the project's validation data and should not be interpreted as clinical performance.

🌐 Web Application

DrugSense provides an interactive Flask-based dashboard for analyzing patient reviews.

The application includes:

Review analysis workspace
NLP analysis
Medical condition prediction
Dataset analytics
Model analytics
Extracted entities
Medication details
Side-effect information
Treatment response
Sentiment analysis
Temporal information
Causal relationships
📁 Project Structure
DrugSense/
│
├── nlp/
│   ├── pipeline.py
│   ├── text_preprocessing.py
│   ├── sentence_analysis.py
│   ├── entity_extraction.py
│   ├── entity_normalization.py
│   ├── negation_detection.py
│   ├── uncertainty_detection.py
│   ├── medication_details.py
│   ├── severity_detection.py
│   ├── relation_extraction.py
│   ├── causality.py
│   ├── side_effects.py
│   ├── coreference.py
│   ├── experiencer.py
│   ├── discourse.py
│   ├── sentiment_analysis.py
│   ├── aspect_sentiment.py
│   ├── treatment_response.py
│   ├── comparative.py
│   ├── events.py
│   ├── temporal_information.py
│   ├── timeline.py
│   ├── semantic.py
│   └── tests/
│
├── static/
│   ├── app.js
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── analytics.html
│
├── app.py
├── ml_pipeline.py
├── ml_predictor.py
├── train_*.py
├── evaluate_*.py
├── compare_models.py
├── final_model_comparison.py
├── test_*.py
├── run_tests.py
├── requirements.txt
└── .gitignore

Large datasets, trained models, archives, and the Python virtual environment are intentionally excluded from the Git repository.

🚀 Installation
1. Clone the repository

Clone the DrugSense repository from GitHub and open the project directory.

2. Create a virtual environment

Create a Python virtual environment named venv inside the project.

3. Activate the virtual environment

On Windows PowerShell, activate the newly created environment using the standard venv activation command.

4. Install dependencies

Install all required Python packages using the project's requirements.txt file.

▶️ Running DrugSense

Start the Flask application using app.py.

Once the server starts, open the local Flask address shown in the terminal, typically:

http://127.0.0.1:5000

The DrugSense dashboard will then be available in your browser.

🔍 Example
Example Patient Review

I started taking metformin 500 mg twice daily for my diabetes three weeks ago. After two days, the medication caused severe nausea and moderate dizziness, but it helped improve my diabetes. I do not have headaches now. I think the metformin may be responsible for the side effects, although my condition has improved.

Example Extracted Information

Medication

Metformin

Dosage

500 mg

Frequency

Twice daily

Duration

Three weeks

Condition

Diabetes

Symptoms

Nausea
Dizziness
Headaches

Severity

Severe
Moderate

Treatment Response

Improved

Causal Relationship

Metformin → caused → nausea

Negation

No headaches

Uncertainty

May be responsible

The ML component additionally produces a condition prediction based on the trained classification model.

🔬 Data & Machine Learning Methodology

The project uses a patient drug-review dataset containing medication reviews and associated medical conditions.

The preprocessing workflow is:

Raw Dataset → Data Cleaning → Duplicate & Missing-Value Checks → Review Leakage Analysis → Conflicting-Label Analysis → Text Preparation → Train/Validation Split → TF-IDF → Model Training → Evaluation

Particular attention was given to data leakage caused by duplicate review text appearing across dataset splits.

The project also examines class imbalance and model performance across conditions with different numbers of training examples.

📊 Model Evaluation

Several models were evaluated during development.

Model	Accuracy	Macro F1	Weighted F1
Logistic Regression	63.60%	9.07%	57.94%
Linear SVM	81.29%	56.10%	80.15%
Cleaned Linear SVM	81.73%	60.08%	80.83%
Final Memory-Safe Linear SVM	76.76%	50.90%	76.94%

The final memory-safe model uses fewer TF-IDF features to make prediction practical on ordinary hardware.

🧪 Testing

DrugSense contains unit, NLP-component, ML, Flask backend, integration, and error-handling tests.

The completed project test suite contains 174 passing tests.

Testing covers:

NLP components
NLP pipeline integration
ML prediction
ML failure handling
Flask API validation
Application errors
Multiple-review processing
Dataset and model statistics
Partial NLP component failures
🛡️ Medical Safety

DrugSense is designed as a research and educational NLP/ML application.

The system:

Does not diagnose patients.
Does not replace a healthcare professional.
Does not provide treatment recommendations.
Does not establish medically verified causality.
Does not claim clinical effectiveness.

For example, an extracted relationship such as:

metformin → caused → nausea

represents a relationship reported or detected in the review text. It should not be interpreted as medically verified causation.

🔒 Data & Model Files

Large datasets and trained model artifacts are intentionally excluded from the GitHub repository.

The final trained SVM model is approximately 585 MB, while an earlier experimental model was several GB.

The repository therefore contains the NLP, ML, training, evaluation, prediction, and application code, while large datasets and model artifacts are excluded through .gitignore.

🧰 Technology Stack
Python
Flask
Pandas
NumPy
scikit-learn
SciPy
Joblib
Matplotlib
pytest
HTML
CSS
JavaScript
👩‍💻 Author

Varshini

GitHub: Varshini0205

Project Repository: DrugSense
