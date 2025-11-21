"""End-to-end Machine Learning pipeline example.

This module implements a small ML workflow using scikit-learn:
- Load a tabular dataset (Iris from sklearn)
- Split into train/validation sets
- Build a preprocessing + model pipeline
- Train and evaluate the model
- Save and reload the trained pipeline

The code is structured in functions so it can be tested easily.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


@dataclass
class DatasetSplit:
    X_train: np.ndarray
    X_valid: np.ndarray
    y_train: np.ndarray
    y_valid: np.ndarray


def load_data(test_size: float = 0.2, random_state: int = 42) -> DatasetSplit:
    """Load the Iris dataset and split into train/validation sets."""
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    return DatasetSplit(X_train=X_train, X_valid=X_valid, y_train=y_train, y_valid=y_valid)


def build_pipeline() -> Pipeline:
    """Create a sklearn Pipeline with preprocessing and classifier."""
    return Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "clf",
                LogisticRegression(max_iter=1000, multi_class="auto", n_jobs=None),
            ),
        ]
    )


def train_model(split: DatasetSplit, pipeline: Pipeline) -> Pipeline:
    """Fit the pipeline on the training data and return it."""
    pipeline.fit(split.X_train, split.y_train)
    return pipeline


def evaluate_model(split: DatasetSplit, pipeline: Pipeline) -> Tuple[float, str]:
    """Evaluate the pipeline on the validation split.

    Returns accuracy and a text classification report.
    """
    y_pred = pipeline.predict(split.X_valid)
    acc = accuracy_score(split.y_valid, y_pred)
    report = classification_report(split.y_valid, y_pred)
    return acc, report


def save_model(pipeline: Pipeline, path: Path) -> None:
    """Persist the trained pipeline to disk using joblib."""
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, path)


def load_model(path: Path) -> Pipeline:
    """Load a previously saved pipeline from disk."""
    return joblib.load(path)


def run() -> None:
    """Run the full ML pipeline and print evaluation metrics."""
    print("[1/4] Loading data...")
    split = load_data()
    print(f"  Train size: {split.X_train.shape}, Valid size: {split.X_valid.shape}")

    print("[2/4] Building pipeline...")
    pipeline = build_pipeline()

    print("[3/4] Training model...")
    pipeline = train_model(split, pipeline)

    print("[4/4] Evaluating model...")
    acc, report = evaluate_model(split, pipeline)
    print(f"\nValidation accuracy: {acc:.3f}\n")
    print("Classification report:")
    print(report)

    model_path = Path(__file__).parent.parent / "model" / "iris_pipeline.joblib"
    print(f"\nSaving model to: {model_path}")
    save_model(pipeline, model_path)
    print("Done.")


if __name__ == "__main__":
    run()
