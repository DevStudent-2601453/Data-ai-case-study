# Analytics

This folder contains the exploratory data analysis (EDA) and predictive modeling work for the project. It focuses on the Titanic dataset used as a stable example for analysis, model experiments, and a saved production-ready pipeline artifact.

## What this analysis covers

- Exploratory Data Analysis (`01_eda.ipynb`): data loading, missing-value strategy, univariate and bivariate visualizations, feature engineering notes, and charts saved to the `charts/` folder.
- Predictive Modeling (`02_modeling.ipynb`): preprocessing pipelines, stratified train/test split, classifier experiments (Logistic Regression, Decision Tree, Random Forest), imbalance-handling experiments (class weights, SMOTE), hyperparameter search (GridSearchCV for Random Forest), regression subtask (predicting `fare`), model comparison tables, and final recommendation.
- Artifacts: a saved full pipeline `best_titanic_pipeline.pkl` that includes preprocessing and the chosen model for easy loading and inference.

## Project structure

```
analytics/
├── 01_eda.ipynb               # Notebook: exploratory data analysis and chart generation
├── 02_modeling.ipynb          # Notebook: modeling experiments, evaluation, and pipeline persistence
├── titanic.csv                # Cleaned dataset used by both notebooks
├── charts/                    # Generated figures and CSV summary files from EDA and modeling
├── best_titanic_pipeline.pkl  # Saved sklearn pipeline (preprocessing + chosen model)
├── requirements.txt          # Python package requirements for analytics workflows
└── README.md                  # Project documentation
```

## Notebooks explained

- `01_eda.ipynb` — Loads `titanic.csv` once at the top of the notebook and performs:
  - Missing value analysis with a clear handling policy (drop if small %, median/mode for 5–30%, drop column if >30%).
  - Univariate plots (histograms, boxplots), bivariate analysis (survival by `pclass`, `sex`, `age`), and correlation heatmaps.
  - Charts are saved to `charts/` for reporting and reproducibility.

- `02_modeling.ipynb` — Continues from the cleaned dataset and includes:
  - Feature selection that excludes direct target proxies (`alive`, duplicate columns) to avoid leakage.
  - A single, reproducible data load; stratified `train_test_split` to preserve target proportions.
  - `ColumnTransformer`-based preprocessing with numeric imputing/scaling and categorical imputation + one-hot encoding.
  - Training of three classifiers: Logistic Regression, Decision Tree, Random Forest.
  - Imbalance experiments: baseline, `class_weight='balanced'`, and SMOTE oversampling (using `imblearn.pipeline`).
  - Hyperparameter tuning for Random Forest with `GridSearchCV` (CV results printed and best estimator saved).
  - Regression subtask that models `fare` with a preprocessing pipeline and `LinearRegression` and reports MAE/RMSE/R².
  - Saves the best full pipeline to `best_titanic_pipeline.pkl` and demonstrates loading/predicting from it.

## How to run the analysis (quick)

1. Create and activate a virtual environment in the `analytics` folder or repository root:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

2. Install the analytics requirements:

```powershell
pip install -r analytics/requirements.txt
```

3. Open and run the notebooks in order:
   - `01_eda.ipynb`
   - `02_modeling.ipynb`

4. To load the saved pipeline in Python:

```python
import joblib
pipe = joblib.load("analytics/best_titanic_pipeline.pkl")
preds = pipe.predict(X_new)
```

## Modeling and preprocessing decisions (summary)

- Single data load: notebooks load `titanic.csv` once at the start to ensure reproducibility.
- Missing values: numeric columns use median; categorical use mode; columns with excessive missingness are dropped (documented in the notebooks).
- Leakage avoidance: obvious target proxies and redundant columns are excluded from `X`.
- Imbalance handling: experiments include `class_weight='balanced'` and SMOTE; comparisons of accuracy, precision, recall, F1, and ROC AUC are shown.
- Model persistence: the full pipeline (preprocessing + estimator) is saved with `joblib.dump` as `best_titanic_pipeline.pkl` for deployment/testing.

## Artifacts

- `titanic.csv` — cleaned dataset used by notebooks.
- `requirements.txt` — Python packages required for analytics notebooks and modeling.
- `charts/` — generated figures and tables from both EDA and modeling workflows.
- `best_titanic_pipeline.pkl` — full sklearn pipeline saved from `02_modeling.ipynb`.

### Charts and outputs in `charts/`

The following files are present in `analytics/charts/`:

- `age_boxplot.png`
- `age_fare_after_scaling.png`
- `age_fare_before_scaling.png`
- `age_histogram.png`
- `Baseline_confusion_from_estimator.png`
- `Class_Weight_=_balanced_confusion_from_estimator.png`
- `correlation_heatmap.png`
- `decision_tree.png`
- `Decision_Tree_confusion_from_estimator.png`
- `Decision_Tree_confusion_matrix.png`
- `fare_boxplot.png`
- `fare_histogram.png`
- `fare_vs_survival.png`
- `final_model_comparison.csv`
- `imbalance_comparison.csv`
- `Logistic_Regression_confusion_from_estimator.png`
- `Logistic_Regression_confusion_matrix.png`
- `model_comparison.csv`
- `Random_Forest_confusion_from_estimator.png`
- `Random_Forest_confusion_matrix.png`
- `residual_plot.png`
- `roc_curves.png`
- `SMOTE_confusion_from_estimator.png`
- `survival_by_class.png`
- `survival_by_class_and_sex.png`
- `survival_by_sex.png`

These files include:

- EDA visualizations for age, fare, survival, and correlation structure.
- Confusion matrices, ROC curve, and decision tree graph from model evaluation.
- Residual plot from the regression subtask.
- Comparison CSV files summarizing model metrics and imbalance-handling results.

If anything should be emphasized or reworded (for reports or a README used by non-technical reviewers), tell me which audience and I'll adapt the tone.
