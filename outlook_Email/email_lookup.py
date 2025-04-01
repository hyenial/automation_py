import win32com.client
import pandas as pd

# Load Excel file
file_path = "path/to/your/excel_file.xlsx"  # Change this to your actual file path
sheet_name = "Sheet1"  # Change if needed

df = pd.read_excel(file_path, sheet_name=sheet_name)

# Ensure columns exist
if "Full Name" not in df.columns:
    raise ValueError("Excel file must contain a 'Full Name' column.")

# Initialize Outlook
outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")
address_list = namespace.AddressLists.Item("Global Address List")  # Company contacts
entries = address_list.AddressEntries

# Function to find work email by full name
def get_email(full_name):
    for entry in entries:
        if entry.Name.lower() == full_name.lower():
            return entry.Address
    return "Not Found"

# Apply function to each full name
df["Work Email"] = df["Full Name"].apply(get_email)

# Save results back to Excel
output_file = "path/to/output_file.xlsx"  # Change path if needed
df.to_excel(output_file, index=False)

print(f"✅ Email lookup completed. Results saved to {output_file}")
