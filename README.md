## 📦 Obsidian Export Script for Subfolders with Attachments Folder

Export one or more subfolders from an Obsidian vault – including all used images from your attachments folder – into a separate folder which mirrors the original Vault.

All done with a simple Python script, no external dependencies.

## ✨ Features

- Copies selected folders as-is
- Scans all contained `.md` files for image links like `![[image.png|jpg|jpeg]]`
- Copies only those images from your attachments folder
- Keeps result small and portable

## ⚙️ Requirements

- Python ≥ 3.6
- No external libraries required (only standard library)

## 🚀 Usage

1. Download the `export.py` file from this page. Click on `export.py` in file view above, then on the Download button in the top right above the code view.

2. Ensure you have Python ≥ 3.6 installed. You can run `python --version` in your terminal to check the installed version. If it returns 2.x, also try `python3 --version`. If that works, replace `python` with `python3` in the script below.

3. Run the script:

```bash
python export.py VAULT_ROOT ATTACHMENTS_FOLDER SOURCE_FOLDER [SOURCE_FOLDER ...] RESULT_ROOT
```

**Arguments:**

- `VAULT_ROOT` – absolute or relative path to your Obsidian vault root. Can use absolute and relative paths and paths may be quoted if they contain spaces etc.
- `ATTACHMENTS_FOLDER` – relative path (from vault root) to your attachments folder, e.g. `"Ω Backend/Attachments"`
- `SOURCE_FOLDER ...` – one or more folders (relative to vault root) you want to export
- `RESULT_ROOT` – path to the output folder, e.g. `here` to dump it next to the script

## 📂 Example

```bash
python export.py ~/vault "Ω Backend/Attachments" folder1 folder2/subfolder ~/vault_export
```

This will:

- Copy `folder1` and `folder2/subfolder` into `~/vault_export`
- Scan them for linked images
- Copy those images from `Ω Backend/Attachments` into `~/vault_export/Ω Backend/Attachments`

## ✅ Result structure

```
vault_export/
├── folder1/
├── folder2/
│   └── another/
└── Ω Backend/
    └── Attachments/
        ├── used1.png
        └── used2.jpg
```
