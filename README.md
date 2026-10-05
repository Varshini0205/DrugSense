# DrugSense

## Patient Drug Review Analysis & Medical Condition Classification System

DrugSense is an **NLP + Machine Learning web application** that analyzes patient drug reviews, extracts structured information from natural language, and predicts the associated medical condition using a machine-learning classification model.

The system combines a modular **NLP pipeline**, **machine-learning classification**, **Flask backend**, and **interactive web dashboard** into one end-to-end application.

> **Medical Disclaimer:** DrugSense is an educational and research-oriented system. Its outputs should not be interpreted as a medical diagnosis, clinical recommendation, or medically verified causal relationship.

---

## ✨ Features

### 🧠 Advanced NLP Pipeline

DrugSense includes a modular NLP pipeline with **23 components**:

- Text preprocessing
- Sentence analysis
- Drug, condition, and symptom extraction
- Entity normalization
- Negation detection
- Uncertainty detection
- Medication dosage extraction
- Medication frequency extraction
- Medication duration extraction
- Severity detection
- Relation extraction
- Causality detection
- Side-effect detection
- Coreference resolution
- Experiencer detection
- Discourse analysis
- Sentiment analysis
- Aspect-based sentiment analysis
- Treatment-response detection
- Comparative change detection
- Event extraction
- Temporal information extraction
- Timeline construction
- Semantic similarity

All components are integrated through a central NLP pipeline.

---

## 🤖 Machine Learning

DrugSense uses machine learning to classify the medical condition associated with a patient drug review.

### Classification Pipeline

```text
Patient Review
      ↓
Text Preprocessing
      ↓
TF-IDF Feature Extraction
      ↓
Linear Support Vector Machine
      ↓
Predicted Medical Condition
```

The project includes experiments with:

- Logistic Regression
- Linear SVM
- TF-IDF unigram and bigram features
- Model comparison
- Condition-level error analysis
- Confusion analysis
- Class-imbalance analysis

### Final Memory-Safe Model

| Property | Value |
|---|---|
| Algorithm | Linear SVM |
| Feature Representation | TF-IDF |
| TF-IDF Features | 100,000 |
| Number of Classes | 791 |
| Accuracy | **76.76%** |
| Macro F1 | **50.90%** |
| Weighted F1 | **76.94%** |

> These metrics describe performance on the project's validation data and do not represent clinical performance.

---

## 🌐 Web Application

DrugSense provides an interactive Flask-based dashboard for analyzing patient reviews.

### Dashboard Features

- **Review Analysis**
- **NLP Analysis**
- **Condition Prediction**
- **Dataset Analytics**
- **Model Analytics**
- Medication information
- Symptoms and side effects
- Treatment response
- Sentiment analysis
- Temporal information
- Causal relationships
- Extracted entities

---

## 📁 Project Structure

```text

DrugSense/
│
├── app.py
├── stats.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── ml/
│   ├── __init__.py
│   ├── ml_pipeline.py
│   └── ml_predictor.py
│
├── nlp/
│   ├── __init__.py
│   │
│   ├── pipeline.py
│   ├── text_preprocessing.py
│   ├── sentence_analysis.py
│   ├── entity_extraction.py
│   ├── entity_normalization.py
│   ├── negation_detection.py
│   ├── uncertainty_detection.py
│   ├── medication_details.py
│   ├── severity_detection.py
│   ├── sentiment_analysis.py
│   ├── aspect_sentiment.py
│   ├── treatment_response.py
│   ├── temporal_information.py
│   ├── relation_extraction.py
│   ├── causality.py
│   ├── side_effects.py
│   ├── coreference.py
│   ├── experiencer.py
│   ├── discourse.py
│   ├── comparative.py
│   ├── events.py
│   ├── timeline.py
│   ├── semantic.py
│   │
│   └── tests/
│       └── ... NLP component tests
│
├── scripts/
│   ├── clean_dataset.py
│   ├── quality_check.py
│   ├── fix_leakage.py
│   ├── verify_final_split.py
│   ├── inspect_conflicts.py
│   ├── remove_conflicting_labels.py
│   ├── prepare_text.py
│   ├── check_text.py
│   ├── split_data.py
│   ├── clean_condition_names.py
│   ├── train_model.py
│   ├── train_final_model.py
│   ├── evaluate_model.py
│   ├── error_analysis.py
│   ├── cleanup_project.py
│   └── ... other ML/data-analysis scripts
│
├── tests/
│   ├── run_tests.py
│   ├── test_app.py
│   ├── test_app_errors.py
│   ├── test_app_validation.py
│   ├── test_ml_model_failure.py
│   ├── test_ml_pipeline.py
│   ├── test_ml_pipeline_errors.py
│   ├── test_ml_predictor.py
│   ├── test_multiple_reviews.py
│   ├── test_nlp_component_errors.py
│   ├── test_nlp_failure.py
│   ├── test_nlp_partial_failure.py
│   ├── test_prediction.py
│   ├── test_real_review.py
│   ├── test_stats.py
│   └── test_top_predictions.py
│
├── data/
│   ├── drugsComTrain_raw.csv
│   ├── drugsComTest_raw.csv
│   ├── clean_train.csv
│   ├── clean_test.csv
│   ├── final_train.csv
│   ├── final_test.csv
│   ├── model_train.csv
│   ├── model_test.csv
│   ├── text_train.csv
│   ├── text_test.csv
│   ├── train_split.csv
│   ├── validation_split.csv
│   ├── clean_train_split.csv
│   ├── clean_validation_split.csv
│   ├── fixed_train_split.csv
│   └── fixed_validation_split.csv
│
├── models/
│   ├── final_tfidf_vectorizer.joblib
│   └── final_svm_model.joblib
│
├── templates/
│   ├── index.html
│   └── analytics.html
│
├── static/
│   ├── style.css
│   └── app.js
│
└── archive/
    ├── models/
    │   ├── clean_svm_model.joblib
    │   ├── clean_tfidf_vectorizer.joblib
    │   ├── logistic_model.joblib
    │   ├── svm_model.joblib
    │   └── tfidf_vectorizer.joblib
    │
    └── analysis/
        ├── condition_error_confidence.csv
        ├── condition_error_rates.csv
        ├── confusion_matrix.csv
        ├── confusion_matrix.png
        ├── error_pairs.csv
        ├── final_condition_report.csv
        ├── final_confusion_matrix.csv
        ├── model_errors.csv
        ├── model_comparison.csv
        ├── top_confusion_pairs.csv
        ├── clean_svm_report.csv
        └── svm_condition_report.csv
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Varshini0205/DrugSense.git
cd DrugSense
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

Open the application in your browser:

**http://127.0.0.1:5000**

---

## 🔍 Example

### Input Review

> I started taking metformin 500 mg twice daily for my diabetes three weeks ago. After two days, the medication caused severe nausea and moderate dizziness, but it helped improve my diabetes.

### Extracted Information

| Category | Result |
|---|---|
| Medication | Metformin |
| Dosage | 500 mg |
| Frequency | Twice daily |
| Duration | Three weeks |
| Condition | Diabetes |
| Symptoms | Nausea, Dizziness |
| Severity | Severe, Moderate |
| Treatment Response | Improved |
| Relation | Metformin → caused → Nausea |

The NLP pipeline converts unstructured patient text into structured information that can be displayed by the application.

---

## 📊 Model Comparison

| Model | Accuracy | Macro F1 | Weighted F1 |
|---|---:|---:|---:|
| Logistic Regression | 63.60% | 9.07% | 57.94% |
| Linear SVM | 81.29% | 56.10% | 80.15% |
| Cleaned Linear SVM | 81.73% | 60.08% | 80.83% |
| Final Memory-Safe Linear SVM | **76.76%** | **50.90%** | **76.94%** |

The final memory-safe model uses fewer TF-IDF features to make prediction more practical on ordinary hardware.

---

## 🧪 Testing

DrugSense includes tests covering:

- NLP components
- NLP pipeline integration
- Machine-learning prediction
- ML failure handling
- Flask API validation
- Application error handling
- Multiple-review processing
- Dataset statistics
- Model statistics
- Partial NLP component failures

### Test Result

**174 tests passed**

Run the complete test suite with:

```bash
pytest -q
```

---

## 🔬 Data & ML Workflow

```text
Raw Dataset
      ↓
Data Cleaning
      ↓
Duplicate & Missing-Value Checks
      ↓
Review Leakage Analysis
      ↓
Conflicting-Label Analysis
      ↓
Text Preparation
      ↓
Train / Validation Split
      ↓
TF-IDF
      ↓
Model Training
      ↓
Model Evaluation
```

The project specifically checks for **review-text leakage and conflicting labels** before model training.

This helps prevent duplicated or conflicting review information from incorrectly influencing model evaluation.

---

## 🧹 Data Quality & Leakage Handling

The project includes dedicated preprocessing and validation scripts for:

- Missing-value handling
- Duplicate detection
- Review-text overlap analysis
- Conflicting-label detection
- Condition-name quality checks
- Text cleaning
- Dataset validation
- Train/validation splitting

The ML workflow avoids fitting the TF-IDF vectorizer on the validation data.

---

## 🔒 Model & Dataset Files

Large files are intentionally excluded from GitHub.

Excluded files include:

- Trained ML models
- Dataset CSV files
- Archived experiments
- Python virtual environment
- Python cache files

The final trained SVM model is approximately **585 MB**, while an earlier experimental model was several GB.

Therefore, the repository contains the:

- NLP implementation
- ML training code
- ML evaluation code
- ML prediction code
- Flask application
- Frontend
- Tests

Large trained model artifacts and datasets are excluded through `.gitignore`.

---

## 🛡️ Medical Safety

DrugSense is designed as a **research and educational NLP/ML application**.

The system:

- Does **not** diagnose patients.
- Does **not** provide treatment recommendations.
- Does **not** replace medical professionals.
- Does **not** establish medically verified causality.
- Does **not** claim clinical effectiveness.
- Reports information detected from the review text and underlying dataset.

For example:

```text
metformin → caused → nausea
```

represents a relationship detected or reported in the review text.

It should **not** be interpreted as medically verified causation.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| Flask | Web backend |
| scikit-learn | Machine Learning |
| Pandas | Data processing |
| NumPy | Numerical processing |
| SciPy | Scientific computing |
| Joblib | Model serialization |
| Matplotlib | Analysis and visualization |
| pytest | Automated testing |
| HTML | Frontend structure |
| CSS | Frontend styling |
| JavaScript | Frontend interaction |

---

## 📌 Project Highlights

- **23 modular NLP components**
- **791 medical-condition classes**
- **100,000 TF-IDF features in the final model**
- **174 automated tests**
- Leakage and data-quality analysis
- Condition-level model evaluation
- Flask REST API
- Interactive analytics dashboard
- Modular and testable NLP architecture

---

## 👩‍💻 Author

**Varshini**

### GitHub

https://github.com/Varshini0205

### Project Repository

https://github.com/Varshini0205/DrugSense

---

## 📌 Project Status

### DrugSense — Core Development Complete

DrugSense currently includes the complete:

**NLP Pipeline → ML Classification → Flask Backend → Interactive Dashboard → Testing Framework**

The project is intended for **research, educational, and portfolio purposes**.

---
```
