import string
from collections import Counter

def analyze_text(text):
    # Supprimer la ponctuation et mettre le texte en minuscule
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    
    # Découper le texte en mots
    words = cleaned_text.split()
    
    # Calcul des statistiques
    num_characters = len(text)  # Inclut les espaces et la ponctuation
    num_words = len(words)
    num_sentences = text.count('.') + text.count('!') + text.count('?')
    word_frequencies = Counter(words)
    
    # Résultats
    results = {
        "Nombre de caractères (incluant espaces)": num_characters,
        "Nombre de mots": num_words,
        "Nombre de phrases": num_sentences,
        "Fréquence des mots": word_frequencies
    }
    return results

def display_results(results):
    print("Statistiques du texte :")
    print(f"- Nombre de caractères : {results['Nombre de caractères (incluant espaces)']}")
    print(f"- Nombre de mots : {results['Nombre de mots']}")
    print(f"- Nombre de phrases : {results['Nombre de phrases']}")
    print("- Fréquence des mots :")
    for word, freq in results['Fréquence des mots'].most_common():
        print(f"  {word}: {freq}")

# Exemple d'utilisation
if __name__ == "__main__":
    print("Bienvenue dans l'analyseur de texte !")
    user_text = input("Entrez un texte pour l'analyse :\n")
    stats = analyze_text(user_text)
    display_results(stats)
