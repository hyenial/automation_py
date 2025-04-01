Outlook Email Lookup Automation

📌 Overview

This Python script automates the process of retrieving work email addresses for employees by searching the Outlook Global Address List (GAL). It reads a list of full names from an Excel file, searches for corresponding email addresses in Outlook, and saves the results back to a new Excel file.

🔹 Features

Reads employee names from an Excel file

Searches for work emails in Outlook's Global Address List (GAL)

Saves the results (including emails) back to an Excel file

Fully automated—no need for manual searching in Outlook

🚀 Prerequisites

Windows OS (with Microsoft Outlook installed)

Python 3.8+

Required Python Packages:

pip install pandas pywin32

Corporate Network Access: Ensure that you are connected to your company's network for GAL access.

🛠 Setup Instructions

Clone or Download the Script

Update the Excel File Path: Edit the script to specify the correct path to your input and output Excel files.

Ensure Outlook is Running: Open Outlook before running the script.

Run the Script:

python outlook_email_lookup.py

📄 Usage

The script expects an Excel file containing a column named Full Name.

After execution, it creates an output Excel file with an additional Work Email column.

📂 Example Input (Excel)

Full Name

John Doe

Alice King

Bob Smith

📂 Example Output (Excel)

Full Name

Work Email

John Doe

john.doe@yourcompany.com

Alice King

alice.king@yourcompany.com

Bob Smith

Not Found

🔧 Troubleshooting

Emails Not Found? Try printing entry.Name to check how names are stored in Outlook.

Permission Errors? Ensure Outlook is installed and running.

win32com.client Not Found? Install it via pip install pywin32.

🏆 Author

Developed by Harun

📜 License

This script is provided under the MIT License.

