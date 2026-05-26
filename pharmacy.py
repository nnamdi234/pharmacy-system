pharmacy = {
    "Paracetamol": {
        "category":    "Painkiller",
        "price":       150,
        "stock":       100,
        "description": "Relieves mild to moderate pain and fever"
    },
    "Amoxicillin": {
        "category":    "Antibiotic",
        "price":       800,
        "stock":       40,
        "description": "Treats bacterial infections"
    },
    "Vitamin C": {
        "category":    "Supplement",
        "price":       300,
        "stock":       75,
        "description": "Boosts immune system"
    },
    "Ibuprofen": {
        "category":    "Painkiller",
        "price":       200,
        "stock":       60,
        "description": "Reduces inflammation, pain and fever"
    },
    "Metformin": {
        "category":    "Diabetes",
        "price":       500,
        "stock":       30,
        "description": "Controls blood sugar levels"
    },
    "Loratadine": {
        "category":    "Antihistamine",
        "price":       250,
        "stock":       5,
        "description": "Treats allergies and hay fever"
    },
    "Atorvastatin": {
        "category":    "Cholesterol",
        "price":       450,
        "stock":       50,
        "description": "Lowers cholesterol and reduces risk of heart disease"
    },
    "Omeprazole": {
        "category":    "Antacid",
        "price":       350,
        "stock":       80,
        "description": "Treats heartburn, acid reflux, and stomach ulcers"
    },
    "Amlodipine": {
        "category":    "Blood Pressure",
        "price":       300,
        "stock":       90,
        "description": "Treats high blood pressure and chest pain (angina)"
    },
    "Cetirizine": {
        "category":    "Antihistamine",
        "price":       180,
        "stock":       120,
        "description": "Relieves allergy symptoms like runny nose, sneezing, and itchy eyes"
    },
    "Azithromycin": {
        "category":    "Antibiotic",
        "price":       950,
        "stock":       25,
        "description": "Treats a wide variety of bacterial infections"
    }
}

def show_menu():
    print("")
    print(" Pharmacy system ")
    print(" 1. Add / Restock a drug ")
    print(" 2. Search for a drug")
    print(" 3. Dipense drug to customer")
    print(" 4. Restock a drug ")
    print(" 5. Remove a drug ")
    print(" 6. List all drugs ")
    print(" 7. Browse by category ")
    print(" 8. View sales log ")
    print(" 0. Exit ")








def main():
    print("")
    print(" Welcome to the Pharmacy System")
    print("" + str(len(pharmacy)) + " drugs loaded. ")

    show_menu()


main()