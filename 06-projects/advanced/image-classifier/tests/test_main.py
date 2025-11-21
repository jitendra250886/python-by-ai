import numpy as np
import pytest

from image_classifier.src import main as img_main  # type: ignore[import]


def test_load_data_shapes() -> None:
    split = img_main.load_data(test_size=0.25, random_state=0)
    # Digits dataset has 1797 samples and 64 features (8x8 images flattened).
    assert split.X_train.shape[1] == 64
    assert split.X_valid.shape[1] == 64
    assert split.X_train.shape[0] + split.X_valid.shape[0] == 1797


def test_train_and_evaluate_classifier() -> None:
    split = img_main.load_data(test_size=0.2, random_state=42)
    pipeline = img_main.build_pipeline()
    trained = img_main.train_model(split, pipeline)
    acc, _ = img_main.evaluate_model(split, trained)
    # Expect reasonably high accuracy on digits.
    assert acc > 0.8


def test_save_and_load_classifier(tmp_path) -> None:
    split = img_main.load_data(test_size=0.2, random_state=42)
    pipeline = img_main.build_pipeline()
    trained = img_main.train_model(split, pipeline)

    model_path = tmp_path / "digits_classifier.joblib"
    img_main.save_model(trained, model_path)

    loaded = img_main.load_model(model_path)
    preds = loaded.predict(split.X_valid)
    assert preds.shape == split.y_valid.shape
