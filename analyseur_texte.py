import unittest
from projet_test import analyze_texte  # Remplace "analyseur_texte" par le nom de ton fichier

class TestAnalyserTexte(unittest.TestCase):

    def test_longueur_texte(self):
        texte = "Bonjour à tous !"
        resultat = analyze_texte(texte)
        self.assertEqual(resultat['nombre_caracteres'], 17)  # Inclut les espaces et la ponctuation

    def test_nombre_mots(self):
        texte = "Les outils technologiques modernes sont fascinants."
        resultat = analyze_texte(texte)
        self.assertEqual(resultat['nombre_mots'], 6)

    def test_nombre_phrases(self):
        texte = "Les outils technologiques modernes sont fascinants. Ils sont utiles !"
        resultat = analyze_texte(texte)
        self.assertEqual(resultat['nombre_phrases'], 2)

    def test_frequence_mots(self):
        texte = "Les outils sont utiles. Les outils modernes."
        resultat = analyze_texte(texte)
        frequence_attendue = {
            "les": 2,
            "outils": 2,
            "sont": 1,
            "utiles": 1,
            "modernes": 1
        }
        self.assertEqual(resultat['frequence_mots'], frequence_attendue)

if __name__ == '__main__':
    unittest.main()
