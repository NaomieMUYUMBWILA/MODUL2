from data_storage import DataStorage 
 
def test_data_storage(): 
    # Test de création et lecture 
    db = DataStorage("test_data.json") 
    db.create("test_key", {"valeur": 42}) 
    assert db.read("test_key") == {"valeur": 42} 
     
    # Test de mise à jour 
    db.update("test_key", {"valeur": 100}) 
    assert db.read("test_key")["valeur"] == 100 
     
    # Test de suppression 
    db.delete("test_key") 
    assert db.read("test_key") is None 
     
    # Nettoyage 
    import os 
    os.remove("test_data.json") 
    print("Tous les tests passés avec succès!") 
 
if __name__ == "__main__": 
    test_data_storage()