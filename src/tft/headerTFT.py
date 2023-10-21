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

def make_classes(filename):
    temp_classes = read_and_convert_txt_file(filename)
 
    allClasses = []
    for i in range(len(temp_classes)):
        class_tuples = [temp_classes[i][0]]
        for j in range(len(temp_classes)):
            if temp_classes[i][1] == temp_classes[j][1] and temp_classes[i][0] != temp_classes[j][0]:
                #print(f"{temp_classes[i]}, {temp_classes[j]}")
                class_tuples.append(f"{temp_classes[j][0]}")
        champName = f"{temp_classes[i][1]}"

        allClasses.append((champName, class_tuples))

    return allClasses
