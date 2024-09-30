import os

def create_lama_file():
    file_name = input("Voer een naam in voor de .lama-bestand (zonder extensie): ")
    file_path = f"{file_name}.lama"
    
    # Maak het .lama-bestand
    with open(file_path, 'w') as f:
        f.write("")  # Maak een leeg bestand aan

    # Open het bestand met nano
    os.system(f"nano {file_path}")

def run_lama_file():
    file_path = input("Voer het pad in naar de .lama-bestand: ")
    
    # Controleer of het bestand bestaat en de juiste extensie heeft
    if os.path.isfile(file_path) and file_path.endswith('.lama'):
        # Voer het lama_runner.py script uit met het .lama-bestand als argument
        os.system(f"python lama_runner.py {file_path}")
    else:
        print("Ongeldig bestandspad of bestand is geen .lama-bestand.")

def main():
    print("Kies een optie:")
    print("1. Maak een nieuwe .lama-bestand aan")
    print("2. Voer een bestaand .lama-bestand uit")
    
    choice = input("Voer uw keuze in (1 of 2): ")

    if choice == '1':
        create_lama_file()
    elif choice == '2':
        run_lama_file()
    else:
        print("Ongeldige keuze. Probeer het opnieuw.")

if __name__ == "__main__":
    main()
