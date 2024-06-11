import csv
import os

def extract_and_write_data_to_csv(directory, output_csv='output.csv'):
    """
    Extracts data from .txt files from the Ecopia HMS-3000 Hall Effect measurements and aggregates  
    them into a .csv file. 

    Args:
    - directory (str): The path to the directory containing the .txt files.
    - output_csv (str): The name of the output CSV file. Defaults to 'output.csv'.

    Returns:
    - None
    """
    # Check directory exists
    if not os.path.isdir(directory):
        raise ValueError(f"The directory {directory} does not exist.")

    # Extracts current, bulk carrier concentration, mobility and sheet carrier concentration
    columns = ['I[mA]', 'Nb[/cm^3]', 'u[cm^2/Vs]', 'NS[/cm^2]']

    # Path to the output CSV file in the specified directory
    output_csv_path = os.path.join(directory, output_csv)

    # Create a CSV writer
    with open(output_csv_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()

        # Iterate over all files in the specified directory
        for filename in os.listdir(directory):
            # Only process .txt files
            if filename.endswith('.txt'):
                file_path = os.path.join(directory, filename)

                # Open each file
                with open(file_path, 'r') as file:
                    lines = file.readlines()

                    # Initialize variables to store the desired data
                    data1_line = None
                    data2_line = None

                    # Find the lines with the desired data
                    for i in range(len(lines)):
                        if 'I[mA]' in lines[i]:
                            data1_line = lines[i+1].strip().split()

                        if 'Nb[/cm^3]' in lines[i]:
                            data2_line = lines[i+1].strip().split()

                    # Ensure data lines were found before writing to CSV
                    if data1_line and data2_line:
                        # Map the data to the column names
                        data = {
                            'I[mA]': data1_line[0],
                            'Nb[/cm^3]': data2_line[0],
                            'u[cm^2/Vs]': data2_line[1],
                            'NS[/cm^2]': data2_line[6]
                        }

                        # Write the data to the CSV file
                        writer.writerow(data)

# Example usage
extract_and_write_data_to_csv('your\path\here')
