# json-to-csv

JSON to CSV/Excel converter with support for nested data flattening. An interactive command-line tool that converts JSON files to multiple formats.

## Features

- **Excel (XLSX)** - Converts JSON directly to Excel format, preserving nested structures
- **Excel (Flattened)** - Flattened Excel with transposed structure (data arranged vertically)
- **CSV (Basic)** - Simple CSV conversion (nested objects may not flatten properly)
- **CSV (Flattened)** - Transposes nested JSON structures, ideal for BigQuery uploads
- **Parquet** - Efficient columnar storage format, ideal for analytics and data processing
- **Parquet (Flattened)** - Flattened Parquet with transposed structure, combining efficiency with restructured data

## Installation

1. Clone the repository:

```bash
git clone https://github.com/merkksgit/json-to-csv.git
cd json-to-csv
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python3 convert.py <input_file.json>
```

The script will prompt you to select a conversion format (1-6).

### Example

```bash
python3 convert.py scores_data.json
```

Then select your desired format:

```
Select conversion format:
1. Excel (XLSX) - Converts JSON directly to Excel format
2. Excel (Flattened) - Flattened Excel with transposed structure
3. CSV (Basic) - Simple CSV conversion (may not handle nested objects properly)
4. CSV (Flattened) - Flattened CSV with transposed structure (ideal for BigQuery)
5. Parquet - Efficient columnar format (ideal for analytics)
6. Parquet (Flattened) - Flattened Parquet with transposed structure

Enter your choice (1-6): 4
```

### Global Installation (Optional)

To run the script from anywhere as a command:

1. Copy the script to your local scripts directory:

```bash
cp convert.py ~/.local/scripts/convert
chmod +x ~/.local/scripts/convert
```

2. Make sure `~/.local/scripts` is in your PATH:

```bash
export PATH="$HOME/.local/scripts:$PATH"
```

Add this to your `~/.bashrc` or `~/.zshrc` to make it permanent.

3. Run from anywhere:

```bash
convert filetoconvert.json
```

## Requirements

- Python 3.6+
- pandas
- openpyxl (for Excel conversion)

## Output

The converted file will be saved in the same directory as the input file with the appropriate extension:

- Excel: `filename.xlsx`
- CSV: `filename.csv`
- Parquet: `filename.parquet`
