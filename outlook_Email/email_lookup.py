import pandas as pd

# Load the first Excel file (Usernames only)
df_users = pd.read_excel("excel1.xlsx")  # Assume column name is 'username'

# Load the second Excel file (Full names with usernames)
df_full_names = pd.read_excel("excel2.xlsx")  # Assume columns are 'username' and 'full_name'

# Normalize usernames (lowercase and strip spaces)
df_users["username"] = df_users["username"].str.lower().str.strip()
df_full_names["username"] = df_full_names["username"].str.lower().str.strip()

# Merge data to find matching full names
df_merged = df_users.merge(df_full_names, on="username", how="left")

# Save the merged result to a new Excel file
df_merged.to_excel("matched_users.xlsx", index=False)

print("✅ Matching complete! Check 'matched_users.xlsx'.")
