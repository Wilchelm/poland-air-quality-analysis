import os
import pandas as pd

# 1. Definiowanie folderu z danymi i pliku wyjściowego
data_folder = "pomiary"
output_file = 'pomiary.csv'

if os.path.exists(output_file):
    os.remove(output_file)

# Sprawdzenie czy folder istnieje
if not os.path.exists(data_folder):
    print(f"Błąd: Folder '{data_folder}' nie istnieje!")
    exit()

# Pobranie listy plików z podfolderu Pomiary
files = [f for f in os.listdir(data_folder) if f.endswith('.xlsx')]

# 2. Czyszczenie i nadpisywanie plików Excel w folderze Pomiary
for file in files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_excel(file_path)

    while df.columns[0] != "Kod stacji":
        if df.columns[0] == "Data pomiaru":
            break
        new_column_names = df.iloc[0]
        df.columns = new_column_names
        df = df[1:]
    
    if df.columns[0] == "Kod stacji":
        df.columns = df.columns.str.replace("Kod stacji", "Data pomiaru", regex=False)
        
    df['Data pomiaru'] = pd.to_datetime(df['Data pomiaru'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
    df_cleaned = df.dropna(subset=['Data pomiaru'])
    df_cleaned.to_excel(file_path, index=False)

# 3. Przetwarzanie danych i transformacja do formatu pionowego (melt)
all_data = []

for file in files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_excel(file_path)
    
    # Wyciąganie typu pomiaru z nazwy pliku (np. z "2013_As(PM10)_24g" wyciąga "As(PM10)")
    file_name, _ = os.path.splitext(file)
    parts = file_name.split('_')
    
    if len(parts) >= 2:
        raw_typ = parts[1]  # Pobiera np. "As(PM10)"
    else:
        raw_typ = "Nieznany"

    # Zmiana struktury tabeli (szeroka -> długa)
    df_long = df.melt(id_vars=['Data pomiaru'], var_name='Kod stacji', value_name='Wartość pomiaru')
    df_long = df_long.dropna(subset=['Wartość pomiaru'])
    
    # Formatowanie daty do formatu tekstowego YYYY-MM-DD
    df_long['Data pomiaru'] = pd.to_datetime(df_long['Data pomiaru']).dt.strftime('%Y-%m-%d')
    
    # Dodanie kolumny Typ pomiaru (bez modyfikacji spacji)
    df_long['Typ pomiaru'] = raw_typ
    
    # Tworzenie Id pomiaru na podstawie oryginalnego typu
    df_long['Id pomiaru'] = df_long['Data pomiaru'] + "_" + raw_typ + "_" + df_long['Kod stacji']
   
    all_data.append(df_long)

# 4. Łączenie i zapis do pliku CSV
if all_data:
    concatenated_df = pd.concat(all_data, axis=0, ignore_index=True)

    # Uporządkowanie kolumn w żądanej kolejności
    final_df = concatenated_df[['Id pomiaru',
                                'Data pomiaru',
                                'Typ pomiaru',
                                'Wartość pomiaru',
                                'Kod stacji']]

    # ---------- Konwersja string → float ----------
    # Jeśli w kolumnie mogą występować nie‑numeryczne znaki, użyj errors='coerce'
    final_df['Wartość pomiaru'] = pd.to_numeric(final_df['Wartość pomiaru'],
                                                 errors='coerce')
    # (jeśli jesteś pewny, że wszystkie wartości są liczbowe, możesz też:
    # final_df['Wartość pomiaru'] = final_df['Wartość pomiaru'].astype(float))

    # Zapis do CSV (separator średnik, przecinek jako separator dziesiętny)
    final_df.to_csv(output_file,
                    index=False,
                    sep=';',
                    decimal='.')
    print(f"Sukces! Dane zostały zapisane do pliku: {output_file}")
else:
    print("Nie znaleziono żadnych danych do przetworzenia.")

