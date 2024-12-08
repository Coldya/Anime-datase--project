import pandas as pd

# Load your dataset
file_path = "anime-dataset-2023.csv"  # Replace with the path to your dataset
dataset = pd.read_csv(file_path)

# Check the current size of the dataset
dataset_size = dataset.memory_usage(deep=True).sum() / (1024 * 1024)  # Convert bytes to MB
print(f"Original dataset size: {dataset_size:.2f} MB")

# Determine the fraction of rows to keep to meet the 10 MB limit
target_size_mb = 10
fraction_to_keep = target_size_mb / dataset_size if dataset_size > target_size_mb else 1.0

# Reduce the dataset size by sampling
reduced_dataset = dataset.sample(frac=fraction_to_keep, random_state=42)

# Save the reduced dataset
output_path = "anime-dataset-2023-reduced.csv"
reduced_dataset.to_csv(output_path, index=False)
print(f"Reduced dataset saved to: {output_path}")

# Check the new size of the dataset
reduced_size = reduced_dataset.memory_usage(deep=True).sum() / (1024 * 1024)  # Size in MB
print(f"Reduced dataset size: {reduced_size:.2f} MB")