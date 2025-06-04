# Group_size: Code for Mitigating Algorithmic Bias through Sampling

## Project Overview
This repository contains the implementation code supporting the paper titled  
**"Mitigating Algorithmic Bias through Sampling: The Role of Group Size and Sample Selection"**  
presented at BIAS 2025 workshop at SIGIR 2025. The code includes various SMOTE-based sampling techniques to mitigate algorithmic bias related to protected attributes, focusing on group size adjustments and sample selection strategies.

## Installation Instructions
To set up the environment, please ensure you have:

- Python 3.8 or higher
- Required Python packages listed in `requirements.txt`

You can install dependencies by running:
```bash
pip install -r requirements.txt

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
