# PDF Page Extractor 📄✂️

A lightweight Python utility to extract a specific range of pages from a PDF file and save them into a new document.

## 🚀 Prerequisites

* **Python 3.x** installed on your system.
* The source PDF file should be named `pdf1.pdf` and placed in the project root folder.

## 🛠️ Installation & Setup

This project uses a **Virtual Environment** to keep dependencies isolated and avoid global installations.

1. **Clone or download** this repository.
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:

   ```bash
    Windows: venv\Scripts\activate
    ```
   macOS/Linux:

   ```bash
    source venv/bin/activate
   ```
   Install the required library:
   ```bash
    pip install pypdf
    ```

   💻 How to Use
   Ensure your source file is named pdf1.pdf.

   Run the script:
   ```bash
    python pdf-slicer.py
    ```

   Customizing the Range
   To change the starting page or the number of pages to extract, open pdf-slicer.py and edit the variables at the bottom:
   ```bash
    # Example: Start at page 20 and extract 20 pages
    START_PAGE = 20
    PAGE_COUNT = 20
    ```

   📂 Project Structure
   - `pdf-slicer.py` - Main Python script.
   - `pdf1.pdf` - Your source PDF file.
   - `README.md` - Documentation.
   - `.gitignore` - Tells Git to ignore the venv/ folder.
