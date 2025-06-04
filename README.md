#Group_size: Code for Mitigating Algorithmic Bias through Sampling
##Project Overview
This repository contains the implementation of bias mitigation techniques described in the paper "Mitigating Algorithmic Bias through Sampling: The Role of Group Size and Sample Selection", accepted at BIAS 2025 workshop (SIGIR 2025).
The code implements various SMOTE-based preprocessing methods to mitigate algorithmic bias in classification tasks by adjusting group sizes and sample selection strategies. It includes experiments with Logistic Regression classifiers on multiple datasets, focusing on fairness metrics such as Demographic Parity and Equalized Odds.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##Installation Instructions
###1. Python Version:
This project is developed and tested with Python 3.8+.

###2.Dependencies:
Install required packages using pip: 
pip install -r requirements.txt

The requirements.txt includes:
*numpy
*pandas
*scikit-learn
*imbalanced-learn
*matplotlib
*seaborn
*scipy

##Data
The code uses publicly available datasets such as Adult Income, COMPAS, and others referenced in the paper.
Due to data privacy and licensing, raw datasets are not included in this repository.
Please download datasets from official sources or open repositories (links provided in the paper) and place them in the data/ folder.
Preprocessing scripts are provided to clean and prepare data before experiments.

##Contact
For questions or feedback, please contact:
Maliheh Heidarpour-Shahrezaei
Email: maliheh.heidarpour@dkit.ie
