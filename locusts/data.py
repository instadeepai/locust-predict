import numpy as np
import pandas as pd

non_temporal_columns = [
    "sand_0.5cm_mean",
    "sand_5.15cm_mean",
    "clay_0.5cm_mean",
    "clay_5.15cm_mean",
    "silt_0.5cm_mean",
    "silt_5.15cm_mean",
]
temporal_variables = [
    "AvgSurfT_inst",
    "Albedo_inst",
    "SoilMoi0_10cm_inst",
    "SoilMoi10_40cm_inst",
    "SoilTMP0_10cm_inst",
    "SoilTMP10_40cm_inst",
    "Tveg_tavg",
    "Wind_f_inst",
    "Rainf_f_tavg",
    "Tair_f_inst",
    "Qair_f_inst",
    "Psurf_f_inst",
]


def grouplen(sequence, chunk_size):
    return list(zip(*[iter(sequence)] * chunk_size))


def preprocess_data(data, start_day=0, days=6, drop_true_absence=True, bucketize=True):
    """Bucketize temporal columns"""
    if drop_true_absence:
        data = data[data["presence"] != 2]
    dfs = []
    for temp_variable in temporal_variables:
        if bucketize:
            columns = [f"{temp_variable}_{i}" for i in range(start_day, 95 + 1)]
            chunks = grouplen(columns, days)
            agg_list = list(map(lambda x: data[list(x)].mean(axis=1), chunks))
            df = pd.concat(agg_list, axis=1)
            df.columns = [
                f"{temp_variable}_bucket_{i}" for i in range(1, df.shape[1] + 1)
            ]
        else:
            columns = [f"{temp_variable}_{i}" for i in range(start_day, 95 + 1)]
            df = data[columns]
        dfs.append(df)
    dfs.append(data[non_temporal_columns])
    return pd.concat(dfs, axis=1), data["presence"]


def load_data(dataset, path="data"):
    data_train = pd.read_csv(f"{path}/train_val_{dataset}.csv", index_col=0)
    data_test = pd.read_csv(f"{path}/test_{dataset}.csv", index_col=0)

    missing_in_train = [n for n in data_test.columns if n not in data_train.columns]
    missing_in_test = [n for n in data_train.columns if n not in data_test.columns]

    print(f"Train missing {len(missing_in_train)} columns")
    print(f"Test missing {len(missing_in_test)} columns")

    data_test = data_test.drop(columns=missing_in_train)
    data_train = data_train.drop(columns=missing_in_test)

    cats = data_train.select_dtypes(np.integer).columns.tolist()
    objects = data_train.select_dtypes(np.object).columns.tolist()
    floats = data_train.select_dtypes(np.float).columns.tolist()
    assert len(cats) + len(objects) + len(floats) == len(data_train.columns)

    print("Objects:", objects)
    print("Categoricals:", cats)
    print("Floats:", floats[:10])

    data_train.dropna(inplace=True)
    data_test.dropna(inplace=True)
    assert not data_train.isnull().sum().sum()
    assert not data_test.isnull().sum().sum()

    return data_train, data_test
