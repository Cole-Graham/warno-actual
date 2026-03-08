import ast
import csv
import sys

# To run, enter path_of_reverse_divisionrules.py path_of_newdivisionrrules_you_want NameOfCSV.csv

def availability_to_string(av_list):
    return "/".join(str(x) for x in av_list)


def transports_to_string(transports):
    if not transports:
        return ""

    cleaned = [t for t in transports if t is not None]

    if not cleaned:
        return ""

    return ";".join(cleaned)


def parse_division_name(var_name):
    """
    Converts 'US_airborne_newdivisionrules'
    into 'US Airborne'
    """
    name = var_name.replace("_newdivisionrules", "")
    parts = name.split("_")

    nation = parts[0]
    division = " ".join(parts[1:]).title()

    return f"{nation} {division}"


def extract_units_from_file(py_file):
    with open(py_file, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=py_file)

    divisions = []

    for node in tree.body:
        if isinstance(node, ast.Assign):

            var_name = node.targets[0].id

            if not var_name.endswith("_newdivisionrules"):
                continue

            division_name = parse_division_name(var_name)
            data = ast.literal_eval(node.value)

            divisions.append((division_name, data))

    return divisions


def write_csv(divisions, output_file):

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        for division_name, categories in divisions:

            # Division header
            writer.writerow([division_name])

            for category, units in categories.items():

                # Category header
                writer.writerow([category.upper()])

                # Column header
                writer.writerow(["Name", "ndf namespace", "Cards", "Availability", "Transports"])

                for entry in units:

                    unit_name = entry[0]
                    cards = entry[1]
                    availability = availability_to_string(entry[2])

                    transports = ""
                    if len(entry) >= 4:
                        transports = transports_to_string(entry[3])

                    writer.writerow([
                        unit_name,
                        unit_name,
                        cards,
                        availability,
                        transports
                    ])

                writer.writerow([])  # blank line between categories


def main():
    if len(sys.argv) != 3:
        print("Usage: python reverse_divisionrules.py input.py output.csv")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    divisions = extract_units_from_file(input_file)
    write_csv(divisions, output_file)

    print(f"CSV written to {output_file}")


if __name__ == "__main__":
    main()