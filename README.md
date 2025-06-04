# Group_size: Code for Mitigating Algorithmic Bias through Sampling

## Project Overview
This repository contains the implementation code supporting the paper titled  
**"Mitigating Algorithmic Bias through Sampling: The Role of Group Size and Sample Selection"**  
presented at BIAS 2025 workshop at SIGIR 2025. The code includes various SMOTE-based sampling techniques to mitigate algorithmic bias related to protected attributes, focusing on group size adjustments and sample selection strategies.

## Installation Instructions
To set up the environment, please ensure you have:

- Python 3.8 or higher
- Required Python packages listed in `requirements.txt`

### You can install dependencies by running:
pip install -r requirements.txt

### Contact:
For questions or feedback, please contact:
- Maliheh Heidarpour-Shahrezaei
- Email: maliheh.heidarpour@dkit.ie


 ##  Hyperparameters 
This work utilises Fair-SMOTE, a fairness-aware oversampling method developed by Chakraborty et al., for synthetic data generation. Fair-SMOTE preserves inter-feature associations and applies type-specific extrapolation logic to Boolean, categorical, and numeric features.

Key hyperparameters and settings used:

- `k` (number of neighbours): **3**  
  Used to identify nearest neighbours during SMOTE interpolation.

- `f` (mutation amount): **0.8**  
  Controls how far synthetic samples are placed between parents.

- `cr` (crossover frequency): **0.8**  
  Determinesthe  frequency of crossover between features for interpolation.

- **Parent Selection Strategies:**
  - `US_SM`: Uniform Sampling from underrepresented groups based on demographic parity.
  - `PS_SM`: Preferential Sampling near the classifier's decision boundary.
  - `WPS_SM`: Weighted Preferential Sampling, with weights based on distance from the decision boundary.
  - UP-prefixed versions (e.g., `UP_US_SM`): Apply each strategy to only the underprivileged (UP) group.
  - B-prefixed versions (e.g., `B_WPS_SM`): Balance all groups to the size of the largest group.

- **Classifiers Used:**
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Gradient Boosting
  - Support Vector Machine (SVM)  
  All with default settings from `sklearn` unless otherwise noted.

- **Reproducibility:**
  - All experiments were repeated across **50 random seeds** for statistical robustness.

Please refer to code comments in the respective sampling strategy folders for further fine-grained hyperparameter settings and implementation logic.

- ## Acknowledgements

Parts of the sample generation and balanced group size logic are adapted from:

- [Fair-SMOTE by Joymallya Chakraborty](https://github.com/joymallyac/Fair-SMOTE/tree/master)

The underprivileged group size handling (UP group size) is inspired by:

- [FAWOS by Teresa Lazar](https://github.com/teresalazar13/FAWOS/tree/master)

We thank the original authors for sharing their code, which was instrumental in supporting our experiments and extending the fairness-aware sampling framework.

---

## Data

Datasets used in this project include publicly available benchmarks such as the **Adult Income** dataset.

> **Note:** Due to privacy and licensing constraints, datasets are **not** included in this repository.

To use the datasets:
- Download them from their original sources (e.g., UCI repository).
- Preprocess them using the provided `data_preprocessing.py` script.

---

## License

This repository is licensed under the **MIT License**.
For details, see the [LICENSE](./LICENSE) file.
