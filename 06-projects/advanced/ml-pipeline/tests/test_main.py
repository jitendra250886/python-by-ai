import numpy as np
import pytest

from ml_pipeline.src import main as ml_main  # type: ignore[import]


def test_load_data_shapes() -> None:
    split = ml_main.load_data(test_size=0.25, random_state=0)
    # Iris has 150 samples, 4 features and 3 classes.
    assert split.X_train.shape[1] == 4
    assert split.X_valid.shape[1] == 4
    assert split.X_train.shape[0] + split.X_valid.shape[0] == 150


def test_build_pipeline_and_train() -> None:
    split = ml_main.load_data(test_size=0.2, random_state=42)
    pipeline = ml_main.build_pipeline()
    trained = ml_main.train_model(split, pipeline)
    acc, _ = ml_main.evaluate_model(split, trained)
    # On Iris, a simple logistic regression should achieve decent accuracy.
    assert acc > 0.7


def test_save_and_load_model(tmp_path) -> None:
    split = ml_main.load_data(test_size=0.2, random_state=42)
    pipeline = ml_main.build_pipeline()
    trained = ml_main.train_model(split, pipeline)

    model_path = tmp_path / "iris_pipeline.joblib"
    ml_main.save_model(trained, model_path)

    loaded = ml_main.load_model(model_path)
    # Predictions from loaded model should be same shape as validation labels.
    y_pred = loaded.predict(split.X_valid)
    assert y_pred.shape == split.y_valid.shape
