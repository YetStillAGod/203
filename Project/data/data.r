import kagglehub

# Download latest version
path = kagglehub.dataset_download("missionjee/car-sales-report")

print("Path to dataset files:", path)
