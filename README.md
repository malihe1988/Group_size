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
Key hyperparameters used in the experiments include:

- **SMOTE neighbors**: Typically set to `5` (default), but adjustable depending on the sampling technique.
- **Classifier parameters**: Logistic Regression using default settings from `scikit-learn` unless otherwise noted.
- Other technique-specific parameters are documented in the code comments.

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
