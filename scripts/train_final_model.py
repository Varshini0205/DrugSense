import os
import time
import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, f1_score


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRAIN_PATH = os.path.join(
    BASE_DIR,
    "data",
    "fixed_train_split.csv"
)

VALIDATION_PATH = os.path.join(
    BASE_DIR,
    "data",
    "fixed_validation_split.csv"
)

VECTOR_PATH = os.path.join(
    BASE_DIR,
    "models",
    "final_tfidf_vectorizer.joblib"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "final_svm_model.joblib"
)


print("=" * 70)
print("DRUGSENSE MEMORY-SAFE FINAL MODEL TRAINING")
print("=" * 70)

start_time = time.time()

print("\nLoading training data...")

train_df = pd.read_csv(TRAIN_PATH)
validation_df = pd.read_csv(VALIDATION_PATH)

train_df = train_df.dropna(
    subset=["review", "condition"]
)

validation_df = validation_df.dropna(
    subset=["review", "condition"]
)

X_train = train_df["review"].astype(str)
y_train = train_df["condition"].astype(str)

X_validation = validation_df["review"].astype(str)
y_validation = validation_df["condition"].astype(str)

print(f"Training rows   : {len(train_df):,}")
print(f"Validation rows : {len(validation_df):,}")
print(f"Conditions      : {y_train.nunique():,}")

print("\nBuilding TF-IDF vectorizer...")

vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    min_df=3,
    max_df=0.95,
    max_features=100000,
    sublinear_tf=True,
    strip_accents="unicode"
)

X_train_tfidf = vectorizer.fit_transform(X_train)

print(
    "Training TF-IDF shape:",
    X_train_tfidf.shape
)

print(
    "TF-IDF matrix type:",
    type(X_train_tfidf).__name__
)

print("\nTransforming validation data...")

X_validation_tfidf = vectorizer.transform(
    X_validation
)

print(
    "Validation TF-IDF shape:",
    X_validation_tfidf.shape
)

print("\nTraining Linear SVM...")

model = LinearSVC(
    C=1.0,
    class_weight="balanced",
    max_iter=2000
)

model.fit(
    X_train_tfidf,
    y_train
)

print("Training complete.")

print("\nEvaluating validation set...")

predictions = model.predict(
    X_validation_tfidf
)

accuracy = accuracy_score(
    y_validation,
    predictions
)

macro_f1 = f1_score(
    y_validation,
    predictions,
    average="macro",
    zero_division=0
)

weighted_f1 = f1_score(
    y_validation,
    predictions,
    average="weighted",
    zero_division=0
)

print("\n" + "=" * 70)
print("FINAL MODEL RESULTS")
print("=" * 70)

print(
    f"Accuracy    : {accuracy:.4f}"
)

print(
    f"Macro F1    : {macro_f1:.4f}"
)

print(
    f"Weighted F1 : {weighted_f1:.4f}"
)

print(
    f"Features    : {len(vectorizer.vocabulary_):,}"
)

print(
    f"Classes     : {len(model.classes_):,}"
)

print("\nSaving model artifacts...")

joblib.dump(
    vectorizer,
    VECTOR_PATH,
    compress=3
)

joblib.dump(
    model,
    MODEL_PATH,
    compress=3
)

print("\nSaved:")
print(
    f"  {VECTOR_PATH}"
)
print(
    f"  {MODEL_PATH}"
)

print(
    "\nTraining time: "
    f"{time.time() - start_time:.2f} seconds"
)

print("=" * 70)
print("TRAINING SUCCESSFUL")
print("=" * 70)
