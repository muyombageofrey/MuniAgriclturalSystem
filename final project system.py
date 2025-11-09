# Muni Farm Agricultural System - Arua, Uganda
# Developed by Year Two Students

import sqlite3
from datetime import datetime

class MuniFarmSystem:
    def __init__(self):
        self.db = sqlite3.connect("muni_farm_system.db")
        self.cursor = self.db.cursor()
        self.create_database()

    def create_database(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS crops (
                id INTEGER PRIMARY KEY,
                crop_name TEXT,
                planting TEXT,
                duration TEXT,
                harvest TEXT,
                soil TEXT,
                problem TEXT,
                solution TEXT
            )
        ''')
        self.db.commit()

        # Insert data only once
        self.cursor.execute("SELECT COUNT(*) FROM crops")
        if self.cursor.fetchone()[0] == 0:
            crops = [
                ("Maize", "March–April, August–September", "3–4 months", "June–July, Nov–Dec",
                 "Loamy soil", "Drought and pests (like fall armyworm)", 
                 "Plant early, use pest-resistant varieties, apply organic manure."),
                 
                ("Beans", "March–April, August–September", "2–3 months", "June, November",
                 "Well-drained soil", "Root rot and aphids", 
                 "Avoid waterlogging, use clean seeds, spray with mild pesticides."),
                 
                ("Groundnuts", "March–April", "3–4 months", "July–August",
                 "Sandy soil", "Leaf spot and rosette virus", 
                 "Use disease-free seed, rotate crops, avoid overcrowding."),
                 
                ("Cassava", "All year (best April or August)", "10–12 months", "After 10 months",
                 "Any fertile soil", "Cassava mosaic disease and mealybugs", 
                 "Use resistant varieties, remove infected plants early."),
                 
                ("Sorghum", "March–April, August–September", "3–4 months", "June–July, Nov–Dec",
                 "Loamy or sandy soil", "Birds and drought", 
                 "Use bird nets, plant early, practice intercropping."),
                 
                ("Sweet Potatoes", "April–May, September", "4–5 months", "Aug–Sept, January",
                 "Sandy soil", "Weevils and drought", 
                 "Use clean vines, harvest early, irrigate during dry spells."),
                 
                ("Millet", "March–April, August–September", "3 months", "June–July, November",
                 "Sandy soil", "Stem borer and drought", 
                 "Plant early and use pest traps."),
                 
                ("Vegetables", "Throughout the year (with irrigation)", "1–3 months", "All year",
                 "Fertile soil", "Wilting and insect attack", 
                 "Water regularly, use organic compost and safe pesticides.")
            ]
            self.cursor.executemany('''
                INSERT INTO crops (crop_name, planting, duration, harvest, soil, problem, solution)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', crops)
            self.db.commit()

    def show_overview(self):
        print("\nMUNI FARM AGRICULTURAL SYSTEM - ARUA, UGANDA")
        print("=" * 60)
        print("Crops Commonly Grown in Arua:\n")

        self.cursor.execute("SELECT crop_name FROM crops")
        crops = [row[0] for row in self.cursor.fetchall()]
        print(", ".join(crops))
        print("\n")

        print("Seasonal Calendar for Arua:")
        print("  • March – May       : First Rainy Season (Good for planting most crops)")
        print("  • June – July       : Short Dry Season (Irrigation may be needed)")
        print("  • August – October  : Second Rainy Season (Good for second planting)")
        print("  • November – February: Long Dry Season (Best for harvesting, dryland crops)")
        print("=" * 60)

    def crop_info(self):
        while True:
            crop = input("\nEnter crop name to view details (or 'quit' to exit): ").strip()
            if crop.lower() == "quit":
                print("\nThank you for using Muni Farm System!")
                break

            self.cursor.execute("SELECT * FROM crops WHERE crop_name LIKE ?", (crop,))
            result = self.cursor.fetchone()
            if result:
                print(f"\nCrop Details for {result[1]}:")
                print(f"  Planting Period : {result[2]}")
                print(f"  Duration        : {result[3]}")
                print(f"  Harvest Time    : {result[4]}")
                print(f"  Soil Type       : {result[5]}")
                print(f"  Common Problems : {result[6]}")
                print(f"  Solutions       : {result[7]}")
            else:
                print(f"'{crop}' not found in database. Please check spelling or try another crop.")

    def close(self):
        self.db.close()


def main():
    system = MuniFarmSystem()
    try:
        system.show_overview()
        system.crop_info()
    finally:
        system.close()


if __name__ == "__main__":
    main()
