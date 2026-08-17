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

https://github.com/user-attachments/assets/1a0f807e-b01c-4788-bae3-89fb1650c120

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

### 1. Environment Setup

Ensure Python 3.x is installed and install the required dependencies:

```bash
pip install pandas openpyxl geopy
```

### 2. Data Acquisition (Manual Step)

> **Important:** Raw data files are not included in this repository. You must download them manually from the **[GIOŚ Air Quality Bank](https://powietrze.gios.gov.pl/pjp/archives)**.

* **Step A:** Place `Metadane oraz kody stacji i stanowisk pomiarowych.xlsx` directly into the `dane` folder.
* **Step B:** Place the downloaded annual measurement ZIP archives into the `dane\Tutaj_umiesc_pliki_ZIP_z_danymi` subfolder.

### 3. Execute ETL Pipeline

Navigate to the `dane` folder and run the orchestration script by double-clicking `run.cmd`. This will generate the required `.csv` files for the report.

### 4. Power BI Configuration (Required to load data)

Since the project uses the Power BI Project (`.pbip`) format, you must update the data source path to match your local machine.

1.  Open `analiza-jakosci-powietrza-w-polsce-2013-2023.pbip` in **Power BI Desktop**.
2.  On the **Home** tab, click the **Transform Data** dropdown and select **Edit Parameters**.
3.  In the `FolderPath` parameter field, paste the absolute path to **main project folder** (the root folder where the `.pbip` file is located).
    * *Example:* `C:\Users\YourName\Documents\Project`
    * **Note:** *Do **NOT** point this to the `dane` folder. It must be the parent folder.*
4.  Click **OK**, then click **Apply Changes**.
5.  Click **Refresh now** to load the data into the model.
   
## Data Attribution & Licensing

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0). The full legal text is available in the LICENSE file in this repository.

* **Air Quality Data:** Sourced from the official Air Quality Database (Bank Danych o Jakości Powietrza) provided by the Chief Inspectorate for Environmental Protection (GIOŚ), Poland.

* **Geocoding Data:** Spatial features are mapped using the Nominatim API via `geopy`. Data © OpenStreetMap contributors (licensed under the Open Database License - ODbL).

#### Disclaimer of Warranty

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


---

## Wersja Polska

Kompleksowy projekt Business Intelligence i Data Engineering. Projekt obejmuje pełny cykl życia danych – od zdefiniowania problemu analitycznego i pozyskania surowych danych, po automatyzację potoków ETL w języku Python oraz budowę interaktywnych raportów Power BI do analizy trendów jakości powietrza i wzorców sezonowych.

## Prezentacja Wideo

https://github.com/user-attachments/assets/1a0f807e-b01c-4788-bae3-89fb1650c120

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

### 1. Konfiguracja Środowiska

Upewnij się, że masz zainstalowany Python 3.x i zainstaluj wymagane biblioteki:

```bash
pip install pandas openpyxl geopy
```

### 2. Przygotowanie Danych

> **Ważne:** Dane surowe nie są częścią repozytorium. Musisz pobrać je ręcznie ze strony **[Banku Danych o Jakości Powietrza GIOŚ](https://powietrze.gios.gov.pl/pjp/archives)**.

* **Krok A:** Umieść plik `Metadane oraz kody stacji i stanowisk pomiarowych.xlsx` bezpośrednio w folderze `dane`.
* **Krok B:** Archiwa ZIP z pomiarami rocznymi umieść w podfolderze `dane\Tutaj_umiesc_pliki_ZIP_z_danymi`.

### 3. Uruchomienie ETL

Uruchom skrypt automatyzujący, dwukrotnie klikając w `run.cmd` w folderze `dane`. Skrypt przetworzy pliki i wygeneruje niezbędne pliki `.csv`.

### 4. Konfiguracja Raportu Power BI (Wymagane do załadowania danych)

Ponieważ projekt korzysta z formatu (`.pbip`), musisz wskazać aktualną ścieżkę do folderu z danymi na swoim komputerze.

1.  Otwórz `analiza-jakosci-powietrza-w-polsce-2013-2023.pbip` w **Power BI Desktop**.
2.  Na karcie **Narzędzia główne** kliknij rozwijane menu **Przekształć dane** i wybierz **Edytuj parametry**.
3.  W polu parametru `FolderPath` wklej pełną ścieżkę do **głównego folderu projektu** (tego, w którym znajduje się plik `.pbip`).
    * *Przykład:* `C:\Users\TwojaNazwa\Documents\Projekt`
    * **Uwaga:** *Nie wskazuj bezpośrednio folderu `dane`. Parametr musi wskazywać na folder nadrzędny.*
4.  Kliknij **OK**, a następnie **Zastosuj zmiany**.
5.  Kliknij **Odśwież teraz**, aby załadować dane do modelu.
   
## Atrybucja Danych i Licencje

Ten projekt jest objęty licencją GNU Affero General Public License v3.0 (AGPL-3.0). Pełny tekst prawny znajduje się w pliku LICENSE w tym repozytorium.

* **Dane o Jakości Powietrza:** Pochodzą z oficjalnego Banku Danych o Jakości Powietrza udostępnionego przez Główny Inspektorat Ochrony Środowiska (GIOŚ).

* **Geokodowanie:** Dane przestrzenne są mapowane za pomocą API Nominatim przy użyciu biblioteki `geopy`. Dane © OpenStreetMap contributors (na licencji Open Database License - ODbL).

  #### Wyłączenie Odpowiedzialności (Disclaimer)
  
OPROGRAMOWANIE JEST DOSTARCZANE "TAKIM, JAKIE JEST" (AS IS), BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ LUB DOROZUMIANEJ. W ŻADNYM WYPADKU AUTORZY LUB WŁAŚCICIELE PRAW AUTORSKICH NIE PONOSZĄ ODPOWIEDZIALNOŚCI Z TYTUŁU JAKICHKOLWIEK ROSZCZEŃ, SZKÓD LUB INNEJ ODPOWIEDZIALNOŚCI WYNIKAJĄCEJ Z KORZYSTANIA Z OPROGRAMOWANIA.

