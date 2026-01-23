# protein-function-classification-ml
Machine learning project for predicting protein functional classes from amino acid sequences using sequence-derived physicochemical features. Includes data preprocessing, feature engineering, model comparison, evaluation, and interpretation.
# Protein Function Classification using Machine Learning

## Problem Definition
This project addresses a binary classification task: predicting whether a protein functions as an enzyme based solely on its amino acid sequence.

Proteins are labeled as enzymes if they possess an Enzyme Commission (EC) number in UniProt, and as non-enzymes otherwise. Only reviewed (Swiss-Prot) protein sequences are used to ensure label reliability.

This project addresses a binary classification problem:

Class 1 (Enzyme): Proteins annotated with an Enzyme Commission (EC) number

Class 0 (Non-enzyme): Proteins without an EC number

The goal is to determine whether a protein is an enzyme using only its amino acid sequence, without relying on structural or homology-based information.

## Overview

This project applies supervised machine learning techniques to predict whether a protein functions as an enzyme based only on its amino acid sequence. Using sequence-derived physicochemical and compositional features, the project demonstrates how classical machine learning models can capture biologically meaningful patterns in protein sequences.

## Dataset
Source: UniProt Knowledgebase (UniProtKB)

Entries: Reviewed (Swiss-Prot) proteins only

Labels:

Enzymes: Proteins with EC numbers

Non-enzymes: Proteins without EC numbers

Preprocessing:

Removed sequences containing ambiguous or unsupported amino acids (e.g., O, U, X, B, Z)

Filtered out very short sequences

Balanced the dataset by undersampling to ensure equal class representation

After cleaning and balancing, the dataset contained an equal number of enzyme and non-enzyme protein sequences.


## Machine Learning Models
1. Logistic Regression (Baseline)

Linear classifier

Feature scaling applied

Used to establish a baseline performance

2. Random Forest Classifier

Ensemble, non-linear model

Captures feature interactions

Provides feature importance for interpretation

## Model Evaluation
Models were evaluated on a held-out test set using:

Accuracy

Precision

Recall

F1-score

Confusion matrices

## Results
A Random Forest classifier achieved ~90% accuracy in distinguishing enzyme and non-enzyme proteins using sequence-derived features, significantly outperforming a Logistic Regression baseline.
Feature importance analysis revealed that structural and physicochemical properties, along with key catalytic amino acids, were the dominant factors distinguishing enzymes from non-enzymes.


## Tools
Python, scikit-learn, BioPython, pandas, numpy
