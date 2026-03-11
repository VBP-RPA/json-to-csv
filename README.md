# Centrepoint JSON-to-CSV Generator

A Python utility that extracts user request data (create, modify, terminate) by parsing Snapforms responses in `.json` into templated `.csv` outputs.

## Setup

1. Install dependencies
   ```bash
   python -m pip install -r requirements.txt
   ```
2. Copy the sample environment file and configure your paths.
   ```bash
   cp example.env .env
   ```
3. Update the `.env` file with the appropriate directories:
   - `JSON_CREATE_DIR`
   - `JSON_MODIFY_DIR`
   - `JSON_TERMINATE_DIR`
   - `CSV_OUTPUT_DIR`
  
## Usage

Run the main script:

```bash
python main.py
```

The script will iterate over all `.json` files in the configured directories and generate corresponding `.csv` outputs.
