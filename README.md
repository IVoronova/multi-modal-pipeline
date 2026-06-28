# Multi-Modal Data Pipeline

A data pipeline that ingests and merges multiple data types into a unified dataset.

## What it does
- Loads sensor readings from a CSV file
- Loads patient metadata from a JSON file
- Merges both sources into a single unified DataFrame

## Libraries Used
- Pandas
- NumPy

## How to run
```bash
python create_data.py  # generates the data files
python pipeline.py     # runs the pipeline
```