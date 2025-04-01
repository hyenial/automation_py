# Outlook Email Lookup Automation

## 📌 Overview

This Python script automates the process of retrieving work email addresses for employees by searching the Outlook Global Address List (GAL). It reads a list of full names from an Excel file, searches for corresponding email addresses in Outlook, and saves the results back to a new Excel file.

## 🔹 Features

- Reads employee names from an Excel file
- Searches for work emails in Outlook's Global Address List (GAL)
- Saves the results (including emails) back to an Excel file
- Fully automated—no need for manual searching in Outlook

## 🚀 Prerequisites

1. **Windows OS** (with Microsoft Outlook installed)
2. **Python 3.8+**
3. **Required Python Packages:**
   ```sh
   pip install pandas pywin32


## 🛠 Setup Instructions

1. **Clone or Download the Script.**
2. **Update the Excel File Path:** Edit the script to specify the correct path to your input and output Excel files.
3. **Ensure Outlook is Running:** Open Outlook before running the script.
4. **Run the Script:**
   ```sh
   python outlook_email_lookup.py
## 📄 Usage

- The script expects an Excel file containing a column named `Full Name`.
- After execution, it creates an output Excel file with an additional `Work Email` column.

## 📂 Example Input (Excel)

| Full Name  |
| ---------- |
| John Doe   |
| Alice King |
| Bob Smith  |

## 📂 Example Output (Excel)

| Full Name  | Work Email                                                       |
| ---------- | ---------------------------------------------------------------- |
| John Doe   | john.doe@yourcompany.com                                          |
| Alice King | alice.king@yourcompany.com                                        |
| Bob Smith  | Not Found                                                        |

## 🔧 Troubleshooting

- **Emails Not Found?** Try printing `entry.Name` to check how names are stored in Outlook.
- **Permission Errors?** Ensure Outlook is installed and running.
- **win32com.client Not Found?** Install it via `pip install pywin32`.
