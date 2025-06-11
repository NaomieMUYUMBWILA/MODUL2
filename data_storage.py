import json 
import os 
 
class DataStorage: 
    def __init__(self, file_path='data.json'): 
        self.file_path = file_path 
        self.data = {} 
        self.load_data() 
     
    def load_data(self): 
        """Charge les données depuis le fichier JSON""" 
        try: 
            if os.path.exists(self.file_path) and os.path.getsize(self.file_path) > 0: 
                with open(self.file_path, 'r') as f: 
                    self.data = json.load(f) 
            else: 
                self.data = {} 
        except (FileNotFoundError, json.JSONDecodeError) as e: 
            print(f"Erreur lors du chargement : {e}") 
            self.data = {} 
     
    def save_data(self): 
        """Sauvegarde les données dans le fichier JSON""" 
        try: 
            with open(self.file_path, 'w') as f: 
                json.dump(self.data, f, indent=4) 
        except IOError as e: 
            print(f"Erreur lors de la sauvegarde : {e}") 
     
    def create(self, key, value): 
        """Ajoute une nouvelle entrée avec sauvegarde automatique""" 
        self.data[key] = value 
        self.save_data() 
     
    def read(self, key=None): 
        """Lit une entrée ou toutes les entrées""" 
        if key: 
            return self.data.get(key) 
        return self.data 
     
    def update(self, key, value): 
        """Modifie une entrée avec sauvegarde automatique""" 
        if key in self.data: 
            self.data[key] = value 
            self.save_data() 
        else: 
            raise KeyError(f"Clé '{key}' introuvable") 
     
    def delete(self, key): 
        """Supprime une entrée avec sauvegarde automatique""" 
        if key in self.data: 
            del self.data[key] 
            self.save_data() 
        else: 
            raise KeyError(f"Clé '{key}' introuvable")