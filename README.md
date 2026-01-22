# protein-function-classification-ml
Machine learning project for predicting protein functional classes from amino acid sequences using sequence-derived physicochemical features. Includes data preprocessing, feature engineering, model comparison, evaluation, and interpretation.
# Protein Function Classification using Machine Learning

## Problem Definition
This project addresses a binary classification task: predicting whether a protein functions as an enzyme based solely on its amino acid sequence.

Proteins are labeled as enzymes if they possess an Enzyme Commission (EC) number in UniProt, and as non-enzymes otherwise. Only reviewed (Swiss-Prot) protein sequences are used to ensure label reliability.

## Overview
This project applies supervised machine learning techniques to predict protein functional classes from amino acid sequences using sequence-derived features.

## Dataset
Protein sequences and functional annotations obtained from UniProt.

## Methods
- Feature extraction from amino acid sequences
- Supervised ML models (Logistic Regression, Random Forest)
- Model evaluation using accuracy and F1-score

## Results
A Random Forest classifier achieved ~90% accuracy in distinguishing enzyme and non-enzyme proteins using sequence-derived features, significantly outperforming a Logistic Regression baseline.

## Tools
Python, scikit-learn, BioPython, pandas, numpy
