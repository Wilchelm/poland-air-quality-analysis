# Air Quality Analysis in Poland (2013–2023)

### Analiza Jakości Powietrza w Polsce (2013–2023)

---

Choose language / Wybierz język:

* [English Version](#english-version)
* [Wersja Polska](#wersja-polska)

---

## English Version

An end-to-end, production-grade Business Intelligence & Data Engineering project. This project covers the complete data lifecycle—from defining the analytical problem and sourcing raw data, to automating ETL pipelines in Python and building interactive Power BI dashboards to analyze air quality trends and seasonal patterns.

## Video Demonstration

> *Note: The video demonstration and the Power BI dashboard layout are presented in Polish.*

<video src="demo.mp4" width="100%" controls> Your browser does not support the video tag. </video>

## Key Technical Highlights

* **Full Project Ownership:** Managed the complete lifecycle of a data project, transforming raw, unstructured public sector datasets into a structured, enterprise-ready analytical asset.

* **Automated ETL Pipeline:** Engineered a robust data pipeline in Python (Pandas, Openpyxl) to extract data from nested ZIP archives and transform unstructured air quality records into a high-performance relational structure.

* **Resilient API Integration & Geocoding:** Implemented geopy (Nominatim) to dynamically enrich missing geographical coordinates and station addresses.

* **Star Schema & Relational Data Modeling:** Designed a clean star-schema model within Power BI to minimize data redundancy, utilizing cross-filtering and optimized DAX measures for high-performance aggregations.

##  Data Architecture & ETL Workflow (run.cmd)

The end-to-end data pipeline is encapsulated within a single-click orchestration script (run.cmd):

1.  **Extraction:** Automatically unpacks annual multi-station data packages from the landing directory.

2.  **Data Enrichment:** Resolves spatial data gaps by cross-referencing and geocoding monitoring stations via poprawa_adresu_dlugosci_i_szerokosci_geograficznej.py.

3.  **Normalization & Consolidation:** Transforms Excel workbooks (containing daily readings for various pollutants across multiple years) into a single, fully normalized fact table (pomiary.csv), optimized for high-performance BI modeling.

## Business Intelligence & Dashboard Insights

The report is architected into three strategic analytics layers:

* **Macro Trends (Executive Overview):** Visualizes 10-year historical micro-trends, featuring dynamic KPI tables comparing pollutant metrics (PM10, PM2.5, NO2, SO2) against strict WHO Air Quality Guidelines.

* **Spatial Analytics (Geographic Distribution):** Features an interactive map of monitoring stations with conditional formatting (Urban vs. Rural) and time-slicing (2013–2023) to identify areas with the highest pollutant concentrations.

* **Time-Series Seasonality (Heating Season Impact):** Pinpoints smog spikes during winter heating seasons using advanced DAX logic, treemaps, and dynamic card callouts.

## Installation & Reproduction

1. **Environment Setup:** Ensure Python 3.x is installed and install the required dependencies:

   ```bash
   pip install pandas openpyxl geopy
   ```
   
2. **Data Sourcing:** Place the following files in the `dane` folder:

   * `Metadane oraz kody stacji i stanowisk pomiarowych.xlsx` (from GIOŚ).

   * ZIP archives with annual measurements in `dane\Tutaj_umiesc_pliki_ZIP_z_danymi`.

3. **Execute ETL (Optional):** To see how the data is processed, run the orchestration script by double-clicking `run.cmd`.

4. **Load Report:** Open `analiza-jakosci-powietrza-w-polsce-2013-2023.pbip` in Power BI Desktop. The report is pre-loaded and ready for analysis.

   > **Note:** If you encounter a data source error, simply update the `FolderPath` parameter in Power Query to match your local `dane` directory path.
   
## Data Attribution & Licensing

* **Air Quality Data:** Sourced from the official Air Quality Database (Bank Danych o Jakości Powietrza) provided by the Chief Inspectorate for Environmental Protection (GIOŚ), Poland.

* **Geocoding Data:** Spatial features are mapped using the Nominatim API via `geopy`. Data © OpenStreetMap contributors (licensed under the Open Database License - ODbL).

---

## Wersja Polska

Kompleksowy projekt Business Intelligence i Data Engineering. Projekt obejmuje pełny cykl życia danych – od zdefiniowania problemu analitycznego i pozyskania surowych danych, po automatyzację potoków ETL w języku Python oraz budowę interaktywnych raportów Power BI do analizy trendów jakości powietrza i wzorców sezonowych.

## Prezentacja Wideo

<video src="demo.mp4" width="100%" controls> Twoja przeglądarka nie obsługuje tagu wideo. </video>

## Kluczowe Aspekty Techniczne

* **Pełna Odpowiedzialność za Projekt:** Zarządzanie pełnym cyklem życia projektu danych – od transformacji surowych, nieustrukturyzowanych zbiorów z sektora publicznego w ustrukturyzowany, gotowy do analizy zasób danych.

* **Zautomatyzowany Potok ETL:** Zbudowanie solidnego potoku danych w Python (Pandas, Openpyxl) w celu ekstrakcji danych z zagnieżdżonych archiwów ZIP i transformacji nieustrukturyzowanych rekordów w wysokowydajną strukturę relacyjną.

* **Integracja API i Geokodowanie:** Wykorzystanie biblioteki geopy (Nominatim) do dynamicznego uzupełniania brakujących współrzędnych geograficznych oraz adresów stacji pomiarowych.

* **Modelowanie Relacyjne (Star Schema):** Zaprojektowanie modelu typu „gwiazda” w Power BI w celu minimalizacji redundancji danych, z wykorzystaniem filtrowania krzyżowego i zoptymalizowanych miar DAX.

## Architektura Danych i Proces ETL (run.cmd)

Cały proces przetwarzania danych został zamknięty w jednym skrypcie automatyzującym (run.cmd):

1.  **Ekstrakcja:** Automatyczne wypakowywanie rocznych pakietów danych ze stacji pomiarowych z folderu wejściowego.

2.  **Wzbogacanie Danych:** Uzupełnianie luk w danych przestrzennych poprzez geokodowanie stacji przy użyciu skryptu poprawa_adresu_dlugosci_i_szerokosci_geograficznej.py.

3.  **Normalizacja i Konsolidacja:** Transformacja plików Excel (zawierających pomiary dobowe dla różnych substancji i lat) w jeden, w pełni znormalizowany plik faktów (pomiary.csv), zoptymalizowany pod kątem wydajności modeli BI.

## Analityka BI i kluczowe wnioski

Raport został zaprojektowany w trzech warstwach analitycznych:

* **Trendy Makro (Executive Overview):** Wizualizacja 10-letnich trendów historycznych i mikrotrendów, zawierająca dynamiczne tabele KPI porównujące stężenia zanieczyszczeń (PM10, PM2.5, NO2, SO2) z restrykcyjnymi normami WHO.

* **Analityka Przestrzenna (Rozkład Geograficzny):** Interaktywna mapa stacji pomiarowych z formatowaniem warunkowym (Miejska vs Wiejska) i filtrowaniem czasu (2013–2023) w celu identyfikacji obszarów o najwyższych stężeniach zanieczyszczeń.

* **Sezonowość (Wpływ Sezonu Grzewczego):** Identyfikacja skoków smogu podczas sezonów grzewczych przy użyciu zaawansowanej logiki DAX, map drzew (treemaps) oraz dynamicznych kart informacyjnych.

## Instalacja i Rekonstrukcja

1. **Konfiguracja Środowiska:** Upewnij się, że masz zainstalowany Python 3.x i zainstaluj wymagane biblioteki:
   
   ```bash
   pip install pandas openpyxl geopy
   ```

2. **Przygotowanie Danych:** Umieść poniższe pliki w folderze `dane`:

   * `Metadane oraz kody stacji i stanowisk pomiarowych.xlsx` (z GIOŚ).

   * Archiwa ZIP z pomiarami rocznymi w `dane\Tutaj_umiesc_pliki_ZIP_z_danymi`.

3. **Uruchomienie ETL (Opcjonalnie):** Aby zobaczyć, jak dane są przetwarzane, uruchom skrypt automatyzujący, dwukrotnie klikając w `run.cmd`.

4. **Eksploracja Raportu:** Otwórz `analiza-jakosci-powietrza-w-polsce-2013-2023.pbip` w Power BI Desktop. Raport jest wstępnie załadowany i gotowy do analizy.

   > **Uwaga:** Jeśli wystąpi błąd źródła danych, wystarczy zaktualizować parametr `FolderPath` w Power Query, wskazując lokalną ścieżkę do Twojego folderu `dane`.
   
## Atrybucja Danych i Licencje

* **Dane o Jakości Powietrza:** Pochodzą z oficjalnego Banku Danych o Jakości Powietrza udostępnionego przez Główny Inspektorat Ochrony Środowiska (GIOŚ).

* **Geokodowanie:** Dane przestrzenne są mapowane za pomocą API Nominatim przy użyciu biblioteki `geopy`. Dane © OpenStreetMap contributors (na licencji Open Database License - ODbL).