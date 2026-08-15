import csv
import time
import openpyxl
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderRateLimited

def get_address_from_coordinates(latitude, longitude, attempt=1, max_attempts=5):
    time.sleep(1)
    geolocator = geo
            
    try:
        lat_str = str(latitude).strip()
        lon_str = str(longitude).strip()
        
        location = geolocator.reverse(lat_str + ', ' + lon_str)
        print(f"[Reverse] Znaleziono: {location}")
        return location if location else None
        
    except GeocoderTimedOut:
        if attempt <= max_attempts:
            print(f"[Timeout] Próba {attempt}/{max_attempts} nieudana, ponawianie za 15s...")
            time.sleep(15)
            return get_address_from_coordinates(latitude, longitude, attempt=attempt + 1)
        raise Exception("Maksymalna liczba prób przekroczona (Timeout).")
        
    except GeocoderRateLimited:
        if attempt <= max_attempts:
            print(f"[RateLimit] Blokada 429. Próba {attempt}/{max_attempts} . Odpoczynek 20s...")
            time.sleep(20)
            return get_address_from_coordinates(latitude, longitude, attempt=attempt + 1)
        raise Exception("Maksymalna liczba prób przekroczona (Rate Limit).")
        
    except Exception as e:
        print(f"Wystąpił błąd w reverse: {e}")
        return None
    

def get_coordinates_from_address(address, attempt=1, max_attempts=5):
    time.sleep(1)
    geolocator = geo
    
    try:
        location = geolocator.geocode(address)
        print(f"[Geocode] Znaleziono: {location}")
        return (location.latitude, location.longitude) if location else None
        
    except GeocoderTimedOut:
        if attempt <= max_attempts:
            print(f"[Timeout] Próba {attempt}/{max_attempts} nieudana, ponawianie za 15s...")
            time.sleep(15)
            return get_coordinates_from_address(address, attempt=attempt + 1)
        raise Exception("Maksymalna liczba prób przekroczona (Timeout).")
        
    except GeocoderRateLimited:
        if attempt <= max_attempts:
            print(f"[RateLimit] Blokada 429. Próba {attempt}/{max_attempts} . Odpoczynek 20s...")
            time.sleep(20)
            return get_coordinates_from_address(address, attempt=attempt + 1)
        raise Exception("Maksymalna liczba prób przekroczona (Rate Limit).")
        
    except Exception as e:
        print(f"Wystąpił błąd w geocode: {e}")
        return None
    

def convert_xlsx_to_csv(xlsx_file, csv_file):
    workbook = openpyxl.load_workbook(xlsx_file)
    sheet = workbook.active
    
    with open(csv_file, mode='w', encoding="utf8", newline='') as f:
        for idx, row in enumerate(sheet.iter_rows(values_only=True)):
            if not row or row is None:
                continue
            
            # Kopiujemy wiersz, usuwamy entery i zamieniamy podwójne spacje na pojedyncze
            row_list = [
                str(cell).replace('\n', ' ').replace('\r', ' ').replace('  ', ' ').strip() 
                if cell is not None else '' 
                for cell in row
            ]
            
            # --- OBSŁUGA NAGŁÓWKA (PIERWSZY WIERSZ) ---
            if idx == 0 or 'szerokość' in str(row_list).lower() or 'wgs84' in str(row_list).lower():
                # Nadpisujemy nazwy ostatnich trzech kolumn na zgodne z Twoim wzorem starego pliku
                row_list[12] = "ul. Adres"
                row_list[13] = "Szerokość geograficzna"
                row_list[14] = "Długość geograficzna"
                
                line = ';'.join(row_list) + '\n'
                f.write(line)
                continue

            # --- PRZETWARZANIE DANYCH ---
            miejscowosc = row_list[11]  # Kolumna: Miejscowość
            ulica_raw = row_list[12]    # Kolumna: ul. Adres
            szerokosc = row_list[13]    # Kolumna: Szerokość geograficzna
            dlugosc = row_list[14]      # Kolumna: Długość geograficzna
            
            ulica = None
            if ulica_raw and ulica_raw != 'None':
                ulica_str = ulica_raw.strip()
                if ulica_str.lower().startswith('ul.'):
                    ulica = ulica_str.replace('ul.', '').strip()
                elif ' ' in ulica_str:
                    a = ulica_str.split(' ')[1:]
                    ulica = ' '.join(a)
                else:
                    ulica = ulica_str
            
            # --- [NOWOŚĆ] WYJĄTEK DLA KUŹNI NIEBOROWICKIEJ ---
            if miejscowosc == "Kuźnia Nieborowicka" and ulica == "Wiejska 12":
                print("[Wyjątek] Wykryto Kuźnię Nieborowicką. Wstawianie poprawnych współrzędnych z Google Maps.")
                szerokosc = "50.2084288"
                dlugosc = "18.6151873"

            # Przypadek 1: Brak współrzędnych (-999) -> Szukamy po adresie tekstowym (pominie Kuźnię, bo już ma przypisane współrzędne wyżej)
            elif (szerokosc == "-999" or szerokosc == "-999.0" or szerokosc == "") and ulica:
                address = f"{ulica}, {miejscowosc}, Poland"
                coordinates = get_coordinates_from_address(address)
                
                if coordinates is None:
                    address = f"{miejscowosc}, Poland"
                    coordinates = get_coordinates_from_address(address)
                    if coordinates is not None:
                        szerokosc, dlugosc = str(coordinates[0]), str(coordinates[1])
                else:
                    szerokosc, dlugosc = str(coordinates[0]), str(coordinates[1])
            
            # Przypadek 2: Są współrzędne, ale błąd adresu tekstowego
            if (not ulica or ulica == "" or ulica == "None") and szerokosc != "-999" and szerokosc != "-999.0" and szerokosc != "":
                location_obj = get_address_from_coordinates(szerokosc, dlugosc)
                if location_obj and 'address' in location_obj.raw:
                    address_dict = location_obj.raw['address']
                    road = address_dict.get('road', '')
                    house_number = address_dict.get('house_number', '')
                    ulica = f"{road} {house_number}".strip() if road else location_obj.address
                else:
                    ulica = "Nie znaleziono"

            # --- AKTUALIZACJA KOMÓREK W WIERSZU ---
            row_list[11] = str(miejscowosc) if miejscowosc is not None else ''
            
            if ulica and ulica != "None":
                row_list[12] = f"ul. {ulica}" if not ulica.startswith('ul.') else ulica
            else:
                row_list[12] = ''
                
            row_list[13] = str(szerokosc)
            row_list[14] = str(dlugosc)
            
            # Zapis wiersza do pliku
            line = ';'.join(row_list) + '\n'
            f.write(line)

print("Informacja: Dane geolokalizacyjne pochodzą z © OpenStreetMap (licencja ODbL).")

xlsx_file = 'Metadane oraz kody stacji i stanowisk pomiarowych.xlsx'
csv_file = 'Metadane oraz kody stacji i stanowisk pomiarowych.csv'

geo = Nominatim(user_agent="data_enrichment_app_missing_addresses_filler", timeout=10)

convert_xlsx_to_csv(xlsx_file, csv_file)
print("Conversion complete!")
