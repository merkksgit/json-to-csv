#!/usr/bin/env python3

import pandas as pd
import sys
import os


def convert_to_xlsx(input_file, output_file):
    """Convert JSON to Excel (XLSX) format without flattening nested structures."""
    df = pd.read_json(input_file)
    df.to_excel(output_file, index=False)
    print(f"JSON file successfully converted to XLSX: {output_file}")


def convert_to_csv_basic(input_file, output_file):
    """Convert JSON to CSV (basic) - may not handle nested objects properly."""
    df = pd.read_json(input_file)
    df.to_csv(output_file, sep=",", index=False)
    print(f"JSON file successfully converted to CSV: {output_file}")


def convert_to_csv_flattened(input_file, output_file):
    """Convert nested JSON to flattened CSV with transposed structure."""
    df = pd.read_json(input_file)
    df = df.T
    df.reset_index(inplace=True)
    df.rename(columns={"index": "id"}, inplace=True)
    df.to_csv(output_file, index=False)
    print(f"JSON file successfully converted to flattened CSV: {output_file}")


def convert_to_xlsx_flattened(input_file, output_file):
    """Convert nested JSON to flattened Excel with transposed structure."""
    df = pd.read_json(input_file)
    df = df.T
    df.reset_index(inplace=True)
    df.rename(columns={"index": "id"}, inplace=True)
    df.to_excel(output_file, index=False)
    print(f"JSON file successfully converted to flattened XLSX: {output_file}")


def main():
    # Check if input file is provided
    if len(sys.argv) < 2:
        print("Usage: convert <input_file.json>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found!")
        sys.exit(1)

    # Check if input file is JSON
    if not input_file.lower().endswith(".json"):
        print("Error: Input file must be a JSON file!")
        sys.exit(1)

    # Display conversion options
    print("\nSelect conversion format:")
    print("1. Excel (XLSX) - Converts JSON directly to Excel format")
    print("2. Excel (Flattened) - Flattened Excel with transposed structure")
    print(
        "3. CSV (Basic) - Simple CSV conversion (may not handle nested objects properly)"
    )
    print(
        "4. CSV (Flattened) - Flattened CSV with transposed structure (ideal for BigQuery)"
    )

    # Get user choice
    choice = input("\nEnter your choice (1-4): ").strip()

    # Get base filename without extension
    base_name = os.path.splitext(input_file)[0]

    # Process based on choice
    if choice == "1":
        output_file = f"{base_name}.xlsx"
        convert_to_xlsx(input_file, output_file)
    elif choice == "2":
        output_file = f"{base_name}.xlsx"
        convert_to_xlsx_flattened(input_file, output_file)
    elif choice == "3":
        output_file = f"{base_name}.csv"
        convert_to_csv_basic(input_file, output_file)
    elif choice == "4":
        output_file = f"{base_name}.csv"
        convert_to_csv_flattened(input_file, output_file)
    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")
        sys.exit(1)


if __name__ == "__main__":
    main()
