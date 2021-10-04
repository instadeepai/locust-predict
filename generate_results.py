import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tqdm import tqdm

from locusts.data import load_data, preprocess_data
from locusts.models import logistic_regression, random_forest, xgboost_regressor

BUCKETIZE = True
N_ITERS = 150
DATASETS = [
    "ep_random",
    "random",
]

for dataset in tqdm(DATASETS):
    data_train, data_test = load_data(dataset)

    data_train, train_target = preprocess_data(
        data_train, start_day=7, bucketize=BUCKETIZE
    )
    data_test, test_target = preprocess_data(
        data_test, start_day=7, bucketize=BUCKETIZE
    )

    print(f"Train features: {data_train.shape}, Train labels: {train_target.shape}")
    print(f"Test features: {data_test.shape}, Test labels: {test_target.shape}")

    logistic_val, logistic_test = [], []
    xgb_val, xgb_test = [], []
    rf_val, rf_test = [], []

    for _ in tqdm(range(N_ITERS)):
        seed = np.random.randint(1e9)
        np.random.seed(seed)

        train_x, val_x, train_y, val_y = train_test_split(
            data_train, train_target, test_size=0.2, random_state=seed
        )

        # Logistic Regression
        # ===================
        _, lr_val_results, lr_test_results = logistic_regression(
            train_x, train_y, val_x, val_y, data_test, test_target, seed=seed
        )
        logistic_val.append(lr_val_results)
        logistic_test.append(lr_test_results)

        # XGBoost
        # =======
        _, xgb_val_results, xgb_test_results = xgboost_regressor(
            train_x, train_y, val_x, val_y, data_test, test_target, seed=seed
        )
        xgb_val.append(xgb_val_results)
        xgb_test.append(xgb_test_results)

        # Random Forest
        # =============
        _, rf_val_results, rf_test_results = random_forest(
            train_x, train_y, val_x, val_y, data_test, test_target, seed=seed
        )
        rf_val.append(rf_val_results)
        rf_test.append(rf_test_results)

    pd.DataFrame(logistic_val).to_csv(f"{dataset}_logistic_val.csv", index=False)
    pd.DataFrame(logistic_test).to_csv(f"{dataset}_logistic_test.csv", index=False)

    pd.DataFrame(xgb_val).to_csv(f"{dataset}_xgb_val.csv", index=False)
    pd.DataFrame(xgb_test).to_csv(f"{dataset}_xgb_test.csv", index=False)

    pd.DataFrame(rf_val).to_csv(f"{dataset}_rf_val.csv", index=False)
    pd.DataFrame(rf_test).to_csv(f"{dataset}_rf_test.csv", index=False)
