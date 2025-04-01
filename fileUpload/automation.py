import papermill as pm
import time

# List of all notebooks to execute
notebooks = [
    #"file1.ipynb",
    #"file2.ipynb",
    #"file3.ipynb",
    "file4.ipynb",
    "file5.ipynb",
    "file6.ipynb"
]

successful_notebooks = []  # Store successful notebooks with execution times
failed_notebooks = []  # Store failed notebook names
start_time = time.time()  # Start overall execution timer

# Function to format time in hours and minutes
def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    return f"{hours} hrs {minutes} min" if hours else f"{minutes} min"

# Execute each notebook
for notebook in notebooks:
    output_notebook = f"output_{notebook}"  # Prevent overwriting
    print(f"🔄 Running {notebook}...")

    try:
        notebook_start_time = time.time()  # Start time for individual notebook
        pm.execute_notebook(notebook, output_notebook, log_output=True)
        notebook_end_time = time.time()  # End time for individual notebook
        
        execution_time = notebook_end_time - notebook_start_time  # Time in seconds
        formatted_time = format_time(execution_time)
        successful_notebooks.append((notebook, formatted_time))  # Log success
        print(f"✅ {notebook} executed successfully! (Time: {formatted_time})")
    except Exception as e:
        print(f"❌ Execution failed for {notebook}: {e}")
        failed_notebooks.append(notebook)  # Log failure

end_time = time.time()  # End overall timer
total_execution_time = end_time - start_time  # Total time in seconds
formatted_total_time = format_time(total_execution_time)

# Print execution summary
print("\n🎯 **Execution Summary**")
if successful_notebooks:
    print("\n✅ Successfully executed notebooks:")
    for nb, exec_time in successful_notebooks:
        print(f"- {nb} (Time: {exec_time})")

if failed_notebooks:
    print("\n⚠️ The following notebooks failed:")
    for nb in failed_notebooks:
        print(f"- {nb}")

# Print total execution time
print(f"\n⏳ **Total execution time:** {formatted_total_time}")
