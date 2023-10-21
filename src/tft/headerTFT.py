def read_and_convert_txt_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()

        # Split the data by lines
        lines = data.split('\n')

        class_data = {}
        current_class = None

        for line in lines:
            line = line.strip()
            if line:
                if line.endswith('{'):
                    current_class = line[:-1]
                    class_data[current_class] = []
                elif line == '}':
                    current_class = None
                elif current_class is not None:
                    class_data[current_class].append(line)

        # Convert the class data to a list of tuples
        class_tuples = []
        for champ_class, champs in class_data.items():
            for champ in champs:
                class_tuples.append((champ_class, champ))

        return class_tuples

    except FileNotFoundError:
        return None

# Example usage:
filename = 'src/tft/champions.txt'
class_tuples = read_and_convert_txt_file(filename)
if class_tuples:
    for class_name, champion in class_tuples:
        print(f"{class_name}: {champion}")
else:
    print(f"File '{filename}' not found.")

print(class_tuples)



