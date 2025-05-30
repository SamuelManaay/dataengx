# DataEngX

Data engineering utilities for converting between CSV, Parquet, JSONL, and more.

## Features

- ✅ Convert Parquet to CSV
- ✅ Convert CSV to JSON (flat + nested)
- ✅ Split Parquet to multiple CSV chunks
- ✅ CSV to SQLite database
- ✅ Parquet to JSONL
- ✅ JSONL to CSV
- ✅ SQL-like querying on CSV using DuckDB
- ✅ Export DataFrame to multiple formats (CSV, Parquet, JSON)

## Installation

```bash
pip install .
```

## CLI Usage

### Convert Parquet to CSV
```bash
dataengx parquet-to-csv path/to/input.parquet output/ --filename optional_filename
```

### Convert CSV to JSON
```bash
dataengx csv-to-json path/to/input.csv path/to/output.json
```

More CLI commands coming soon...

## Python Usage

```python
from dataengx import (
    convert_parquet_to_csv,
    csv_to_json,
    csv_to_nested_json,
    split_parquet_to_csv,
    csv_to_sqlite,
    parquet_to_jsonl,
    jsonl_to_csv,
    query_csv_with_sql,
    export_dataframe
)

# Convert Parquet to CSV
convert_parquet_to_csv("data/data.parquet", "output/")

# Convert CSV to flat JSON
csv_to_json("data/data.csv", "output/data.json")

# Convert CSV to nested JSON
csv_to_nested_json("data/nested.csv", "output/nested.json")

# Split Parquet to multiple CSV files
split_parquet_to_csv("data/big.parquet", "output/splits", row_limit=5000)

# Convert CSV to SQLite database
csv_to_sqlite("data/input.csv", "output/output.sqlite")

# Convert Parquet to JSONL
parquet_to_jsonl("data/input.parquet", "output/data.jsonl")

# Convert JSONL to CSV
jsonl_to_csv("data/input.jsonl", "output/data.csv")

# Query CSV like SQL
query_csv_with_sql("SELECT * FROM 'data.csv' WHERE age > 25", csv_path="data/data.csv")

# Export a DataFrame to CSV
import pandas as pd
df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [30, 25]})
export_dataframe(df, "output", "people", fmt="csv")
```

