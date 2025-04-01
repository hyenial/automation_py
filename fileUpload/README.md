# 📘 Notebook Execution Automation

## 📌 Overview
This Python script automates the execution of multiple Jupyter notebooks using `papermill`. It logs execution time and provides a summary of successfully executed and failed notebooks.

## 🚀 Features
- Automates execution of multiple Jupyter notebooks.
- Logs execution time for each notebook.
- Provides a summary of successful and failed notebooks.
- Saves output notebooks with unique filenames to prevent overwriting.

## 🛠 Prerequisites
1. **Python 3.8+** installed on your system.
2. **Required Python Packages:**
   ```sh
   pip install papermill
   ```
3. **Jupyter Notebook Environment:** Ensure Jupyter is installed and configured.

## 📄 Usage
1. **Clone or download** the script.
2. **Update the list of notebooks** in the script (`notebooks` variable) with the paths to your Jupyter notebooks.
3. **Run the script:**
   ```sh
   python execute_notebooks.py
   ```

## 📂 Example Output
```
🔄 Running file4.ipynb...
✅ file4.ipynb executed successfully! (Time: 1 hr 20 min)
🔄 Running file5.ipynb...
✅ file5.ipynb executed successfully! (Time: 45 min)
🔄 Running file6.ipynb...
❌ Execution failed for file6.ipynb: [Error Message]

🎯 **Execution Summary**
✅ Successfully executed notebooks:
- file4.ipynb (Time: 1 hr 20 min)
- file5.ipynb (Time: 45 min)

⚠️ The following notebooks failed:
- file6.ipynb

⏳ **Total execution time:** 2 hrs 5 min
```

## 🔧 Troubleshooting
- **Execution failure?** Ensure Jupyter and `papermill` are properly installed.
- **Permission Errors?** Run the script with appropriate permissions.
- **Incorrect Notebook Path?** Verify that the notebook paths in the script are correct.

## 🏆 Author
Developed by Harun

## 📜 License
This script is provided under the MIT License.
