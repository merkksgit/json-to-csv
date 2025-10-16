# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A simple interactive CLI tool that converts JSON files to CSV or Excel formats. The single-file script (`convert.py`) handles three conversion methods with different nested data handling strategies.

## Dependencies

Install dependencies with:
```bash
pip install -r requirements.txt
```

Required packages:
- `pandas` - Core data manipulation
- `openpyxl` - Required for Excel (.xlsx) conversion only

## Running the Script

```bash
python3 convert.py <input_file.json>
```

The script prompts for format selection (1-3) interactively.

## Architecture Notes

The script is structured as a single-file CLI with three conversion functions:

1. **`convert_to_xlsx()`** - Uses `pd.read_json()` → `to_excel()` directly, preserving nested JSON structures as-is in Excel cells
2. **`convert_to_csv_basic()`** - Uses `pd.read_json()` → `to_csv()` directly, but nested objects may appear as stringified values in single columns
3. **`convert_to_csv_flattened()`** - Transposes the DataFrame (`.T`) and resets the index, converting nested JSON keys into rows. This method is specifically designed for BigQuery uploads where the JSON structure is: `{"id1": {...attributes...}, "id2": {...attributes...}}`

**Key behavior**: Option 3 assumes JSON is structured with IDs as top-level keys. It transposes so each ID becomes a row and nested attributes become columns.

## Output Behavior

- Output files use the input filename with changed extension (e.g., `data.json` → `data.xlsx` or `data.csv`)
- Files are saved in the same directory as the input file
- The script validates file existence and JSON extension before processing
