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

- `01_eda.ipynb` — The notebook starts by loading `titanic.csv` into a pandas DataFrame and then executes these key code steps:
  - Inspect data shape, data types, and the first rows to understand column contents.
  - Count missing values and document which columns need cleaning.
  - Apply missing-value handling rules in code: numeric columns use median imputation, categorical columns use mode, and columns with excessive missingness are dropped.
  - Create univariate plots with Matplotlib/Seaborn such as histograms for `age`, `fare`, and bar charts for `sex` and `pclass`.
  - Create bivariate visualizations to compare survival rates by `sex`, `pclass`, `age`, and `fare`.
  - Build a correlation matrix and render it as a heatmap to highlight relationships between numeric features.
  - Save each figure with `plt.savefig(...)` into the `charts/` folder so the visuals are preserved outside the notebook.
  - Export summary tables and cleaned subsets as CSV files when useful for later modeling.

- `02_modeling.ipynb` — This notebook loads the same cleaned dataset and follows a structured modeling workflow:
  - Drop direct target proxies and redundant columns before modeling to prevent leakage and keep features meaningful.
  - Use `train_test_split(..., stratify=y)` so the target distribution is preserved between training and test sets.
  - Define preprocessing pipelines using `ColumnTransformer`:
    - Numeric branch: impute missing values with `SimpleImputer(strategy='median')`, then scale numeric features with `StandardScaler`.
    - Categorical branch: impute missing values with `SimpleImputer(strategy='most_frequent')`, then encode with `OneHotEncoder(handle_unknown='ignore')`.
  - Construct full model pipelines with `imblearn.pipeline.Pipeline` for each classifier, enabling consistent preprocessing plus modeling in one object.
  - Train baseline classifiers and compare metrics:
    - Logistic Regression
    - Decision Tree
    - Random Forest
  - Run imbalance handling experiments using class weighting and SMOTE oversampling. The notebook compares results from:
    - baseline model
    - `class_weight='balanced'` model
    - SMOTE pipeline with oversampling in the training data
  - Evaluate models using confusion matrices, classification reports, ROC AUC, and feature importance where applicable.
  - Perform a separate regression subtask for `fare` using a similar preprocessing pipeline and `LinearRegression`; report MAE, RMSE, and R².
  - Use `GridSearchCV` to tune Random Forest hyperparameters and print the best parameters and cross-validation results.
  - Persist the recommended production pipeline with `joblib.dump(best_pipeline, 'analytics/best_titanic_pipeline.pkl')`.
  - Demonstrate how to reload the pipeline with `joblib.load(...)` and make predictions on new data.

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


