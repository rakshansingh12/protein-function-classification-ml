import joblib
from Bio.SeqUtils import ProtParam


rf = joblib.load("models/random_forest_protein_classifier.joblib")

def extract_features(sequence):
    analyzer = ProtParam.ProteinAnalysis(sequence)
    return [
        len(sequence),
        analyzer.molecular_weight(),
        analyzer.isoelectric_point(),
        analyzer.aromaticity(),
        analyzer.gravy()
    ]


sequence = "MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHF"

features = extract_features(sequence)
prediction = rf.predict([features])

print("Enzyme" if prediction[0] == 1 else "Non-enzyme")
