import xgboost as xgb
from sklearn import metrics, preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


def evaluate(trues, preds, probs):
    results = {}
    results["accuracy"] = metrics.accuracy_score(trues, preds)
    results["confusion_matrix"] = metrics.confusion_matrix(trues, preds)
    results["kappa"] = metrics.cohen_kappa_score(trues, preds)
    results["f1"] = metrics.f1_score(trues, preds)
    results["auc"] = metrics.roc_auc_score(trues, probs)
    return results


def logistic_regression(train_x, train_y, val_x, val_y, test_x, test_y, seed=None, return_scaler=False):
    "Logistic regression model with data scaling."
    scaler = preprocessing.StandardScaler()
    train_x_scaled = scaler.fit_transform(train_x)
    val_x_scaled = scaler.transform(val_x)
    test_x_scaled = scaler.transform(test_x)

    model = LogisticRegression(random_state=seed)
    model.fit(train_x_scaled, train_y)

    y_preds = model.predict(val_x_scaled)
    y_probs = model.predict_proba(val_x_scaled)[:, 1]
    logistic_val_results = evaluate(val_y, y_preds, y_probs)

    y_preds = model.predict(test_x_scaled)
    y_probs = model.predict_proba(test_x_scaled)[:, 1]
    logistic_test_results = evaluate(test_y, y_preds, y_probs)

    out = model, logistic_val_results, logistic_test_results
    if return_scaler:
        out = out + (scaler,)

    return out


def xgboost_regressor(train_x, train_y, val_x, val_y, test_x, test_y, seed=None):
    train_xgb = xgb.DMatrix(train_x, label=train_y)
    val_xgb = xgb.DMatrix(val_x, label=val_y)
    test_xgb = xgb.DMatrix(test_x)

    params = {
        "max_depth": 5,
        "eta": 0.3,
        "objective": "binary:logistic",
        "subsample": 0.7,
        "seed": seed,
    }
    model = xgb.train(params, train_xgb)
    y_probs = model.predict(val_xgb)
    y_preds = y_probs.round()
    xgb_val_results = evaluate(val_y, y_preds, y_probs)

    y_probs = model.predict(test_xgb)
    y_preds = y_probs.round()
    xgb_test_results = evaluate(test_y, y_preds, y_probs)

    return model, xgb_val_results, xgb_test_results


def random_forest(train_x, train_y, val_x, val_y, test_x, test_y, seed=None):
    model = RandomForestClassifier(
        n_estimators=200, max_depth=5, min_samples_leaf=50, n_jobs=-1, random_state=seed
    )
    model.fit(train_x, train_y)

    y_preds = model.predict(val_x)
    y_probs = model.predict_proba(val_x)[:, 1]
    rf_val_results = evaluate(val_y, y_preds, y_probs)

    y_preds = model.predict(test_x)
    y_probs = model.predict_proba(test_x)[:, 1]
    rf_test_results = evaluate(test_y, y_preds, y_probs)

    return model, rf_val_results, rf_test_results
