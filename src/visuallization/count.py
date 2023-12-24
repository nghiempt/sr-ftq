import pandas as pd

# Load the CSV file
file_path = '/Users/nghiempt/Observation/sr-ftq/src/visuallization/data_collected_regular.csv'  # Replace with the actual file path
df = pd.read_csv(file_path)

# Specify the category you want to analyze (e.g., "Art & Design")
category_to_analyze = "Art & Design"

# Filter the DataFrame for the specified category
category_df = df[df['category_name'] == category_to_analyze]

# Get the unique app names in the category
unique_apps = category_df['app_name'].unique()

# Initialize counters for regular and irregular data types
regular_data_types = set()
irregular_data_types = set()

# Iterate through each app in the category
for app_name in unique_apps:
    app_data = category_df[category_df['app_name'] == app_name]
    
    # Count the unique data types for the app
    data_types_count = app_data['data_type'].value_counts()
    
    # Determine if it's regular or irregular based on the criteria (e.g., >50%)
    total_apps = len(app_data)
    for data_type, count in data_types_count.items():
        if count > total_apps / 2:
            regular_data_types.add(data_type)
        else:
            irregular_data_types.add(data_type)

# Print the regular and irregular data types
print("Regular Data Types:")
print(regular_data_types)
print("\nIrregular Data Types:")
print(irregular_data_types)
