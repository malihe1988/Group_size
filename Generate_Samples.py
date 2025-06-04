import pandas as pd
import random
from sklearn.neighbors import NearestNeighbors as NN

def get_ngbr(df, knn):
    rand_sample_idx = random.randint(0, df.shape[0] - 1)
    parent_candidate = df.iloc[rand_sample_idx]
    if df.shape[0] < 2:
        return parent_candidate, parent_candidate, parent_candidate, parent_candidate
    ngbr = knn.kneighbors(parent_candidate.values.reshape(1, -1), return_distance=False)
    candidates = [df.iloc[ngbr[0][i]] if i < len(ngbr[0]) else parent_candidate for i in range(3)]
    return parent_candidate, candidates[0], candidates[1], candidates[2]

def generate_samples(no_of_samples, df, df_name):
    total_data = df.values.tolist()
    num_samples = df.shape[0]
    n_neighbors = min(3, num_samples - 1)
    
    if n_neighbors < 1:
        n_neighbors = 1

    knn = NN(n_neighbors=n_neighbors, algorithm='auto').fit(df)

    for _ in range(no_of_samples):
        cr = 0.8
        f = 0.8
        parent_candidate, child_candidate_1, child_candidate_2, child_candidate_3 = get_ngbr(df, knn)
        new_candidate = []

        for key, value in parent_candidate.items():
            if isinstance(parent_candidate[key], bool):
                new_candidate.append(parent_candidate[key] if cr < random.random() else not parent_candidate[key])
            elif isinstance(parent_candidate[key], str):
                new_candidate.append(random.choice([parent_candidate[key], child_candidate_1[key], child_candidate_2[key], child_candidate_3[key]]))
            elif isinstance(parent_candidate[key], list):
                temp_lst = []
                for i, each in enumerate(parent_candidate[key]):
                    temp_lst.append(parent_candidate[key][i] if cr < random.random() else
                                    int(parent_candidate[key][i] + f * (child_candidate_1[key][i] - child_candidate_2[key][i])))
                new_candidate.append(temp_lst)
            else:
                new_candidate.append(abs(parent_candidate[key] + f * (child_candidate_1[key] - child_candidate_2[key])))

        total_data.append(new_candidate)

    final_df = pd.DataFrame(total_data)

    # Rename columns based on the dataset
    column_mappings = {
        'Adult': {0: "age", 1: "education-num", 2: "race", 3: "sex", 4: "capital-gain", 5: "capital-loss", 6: "hours-per-week", 7: "Probability"},
        'Compas': {0: "sex", 1: "age_cat", 2: "race", 3: "priors_count", 4: "c_charge_degree", 5: "Probability"},
        'Default': {0: "LIMIT_BAL", 1: "sex", 2: "EDUCATION", 3: "MARRIAGE", 4: "AGE", 5: "PAY_0", 6: "PAY_2", 7: "PAY_3", 8: "PAY_4", 9: "PAY_5", 10: "PAY_6", 11: "BILL_AMT1", 12: "BILL_AMT2", 13: "BILL_AMT3", 14: "BILL_AMT4", 15: "BILL_AMT5", 16: "BILL_AMT6", 17: "PAY_AMT1", 18: "PAY_AMT2", 19: "PAY_AMT3", 20: "PAY_AMT4", 21: "PAY_AMT5", 22: "PAY_AMT6", 23: "Probability"},
        'German': {0: "sex", 1: "age", 2: "credit_history=Delay", 3: "credit_history=None/Paid", 4: "credit_history=Other", 5: "savings=500+", 6: "savings=<500", 7: "savings=Unknown/None", 8: "employment=1-4 years", 9: "employment=4+ years", 10: "employment=Unemployed", 11: "Probability"},
        'Heart': {0: "age", 1: "sex", 2: "cp", 3: "trestbps", 4: "chol", 5: "fbs", 6: "restecg", 7: "thalach", 8: "exang", 9: "oldpeak", 10: "slope", 11: "ca", 12: "thal", 13: "Probability"},
        'Bank': {0: "age", 1: "default", 2: "balance", 3: "housing", 4: "loan", 5: "day", 6: "duration", 7: "campaign", 8: "pdays", 9: "previous", 10: "Probability"},
        'Titanic': {0: "Pclass", 1: "sex", 2: "Age", 3: "SibSp", 4: "Parch", 5: "Fare", 6: "Probability"},
        'Student': {0: 'sex', 1: 'age', 2: 'Medu', 3: 'Fedu', 4: 'traveltime', 5: 'studytime', 6: 'failures', 7: 'schoolsup', 8: 'famsup', 9: 'paid', 10: 'activities', 11: 'nursery', 12: 'higher', 13: 'internet', 14: 'romantic', 15: 'famrel', 16: 'freetime', 17: 'goout', 18: 'Dalc', 19: 'Walc', 20: 'health', 21: 'absences', 22: 'G1', 23: 'G2', 24: 'Probability'},
        'Openuni': {0: 'code_module', 1: 'code_presentation', 2: 'sex', 3: 'region', 4: 'highest_education', 5: 'imd_band', 6: 'age', 7: 'num_of_prev_attempts', 8: 'studied_credits', 9: 'disability', 10: 'Probability'},
        'Lawschool': {0: 'decile1b', 1: 'decile3', 2: 'lsat', 3: 'ugpa', 4: 'zfygpa', 5: 'zgpa', 6: 'fulltime', 7: 'fam_inc', 8: 'sex', 9: 'tier', 10: 'race', 11: 'Probability'},
        'Diabetes': {0: 'race', 1: 'sex', 2: 'age', 3: 'time_in_hospital', 4: 'num_procedures', 5: 'num_medications', 6: 'number_outpatient', 7: 'number_emergency', 8: 'number_inpatient', 9: 'metformin', 10: 'chlorpropamide', 11: 'glimepiride', 12: 'rosiglitazone', 13: 'acarbose', 14: 'miglitol', 15: 'diabetesMed', 16: 'Probability'},
        'Diabete2': {0: 'Probability', 1: 'HighBP', 2: 'HighChol', 3: 'CholCheck', 4: 'BMI', 5: 'Smoker', 6: 'Stroke', 7: 'HeartDiseaseorAttack', 8: 'PhysActivity', 9: 'Fruits', 10: 'Veggies', 11: 'HvyAlcoholConsump', 12: 'AnyHealthcare', 13: 'NoDocbcCost', 14: 'GenHlth', 15: 'MentHlth', 16: 'PhysHlth', 17: 'DiffWalk', 18: 'sex', 19: 'Age', 20: 'Education', 21: 'Income'}
    }
    
    final_df = final_df.rename(columns=column_mappings.get(df_name, {}), errors="raise")

    return final_df
