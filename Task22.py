def count_names(file_path):
    name_count = {}
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                name = line.strip()
                if name in name_count:
                    name_count[name] += 1
                else:
                    name_count[name] = 1
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return {}

    return name_count

file_path = 'names.txt'  
name_counts = count_names(file_path)
if name_counts:
    for name, count in name_counts.items():
        print(f"{name}: {count}")
else:
    print("No data to display.")
