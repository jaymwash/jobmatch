import spacy
import subprocess
import importlib.util

def load_spacy_model():
    model_name = "en_core_web_sm"
    if not importlib.util.find_spec(model_name):
        subprocess.run(["python", "-m", "spacy", "download", model_name])
    return spacy.load(model_name)

nlp = load_spacy_model()
