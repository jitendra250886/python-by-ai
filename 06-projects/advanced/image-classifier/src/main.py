"""Simple image classifier using scikit-learn's digits dataset.

This module trains a model to classify handwritten digits (0-9) from the
built-in `load_digits` dataset. It demonstrates a basic image pipeline:
- Load dataset
- Flatten image data into feature vectors
- Split into train/validation sets
- Train a classifier
- Evaluate accuracy
- Save and reload the trained model
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

import joblib
import numpy as np
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


@dataclass
class ImageDatasetSplit:
    X_train: np.ndarray
    X_valid: np.ndarray
    y_train: np.ndarray
    y_valid: np.ndarray


def load_data(test_size: float = 0.2, random_state: int = 42) -> ImageDatasetSplit:
    """Load the digits dataset and create a train/validation split."""
    digits = load_digits()
    X = digits.images.reshape(len(digits.images), -1)  # flatten 8x8 images
    y = digits.target

    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    return ImageDatasetSplit(X_train=X_train, X_valid=X_valid, y_train=y_train, y_valid=y_valid)


def build_pipeline() -> Pipeline:
    """Build a preprocessing + classifier pipeline."""
    return Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(max_iter=1000, multi_class="auto")),
        ]
    )


def train_model(split: ImageDatasetSplit, pipeline: Pipeline) -> Pipeline:
    """Train the classifier on the training images."""
    pipeline.fit(split.X_train, split.y_train)
    return pipeline


def evaluate_model(split: ImageDatasetSplit, pipeline: Pipeline) -> Tuple[float, str]:
    """Evaluate accuracy and return a classification report."""
    y_pred = pipeline.predict(split.X_valid)
    acc = accuracy_score(split.y_valid, y_pred)
    report = classification_report(split.y_valid, y_pred)
    return acc, report


def save_model(pipeline: Pipeline, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, path)


def load_model(path: Path) -> Pipeline:
    return joblib.load(path)


def run() -> None:
    """Train and evaluate the image classifier, then save it to disk."""
    print("[1/4] Loading digit images...")
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

    model_path = Path(__file__).parent.parent / "model" / "digits_classifier.joblib"
    print(f"\nSaving model to: {model_path}")
    save_model(pipeline, model_path)
    print("Done.")


if __name__ == "__main__":
    run()
