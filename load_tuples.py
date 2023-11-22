import csv

def getRecords(path_):
    try:
        # Initialize an empty list to store tuples (records)
        data = []

        # Open the CSV file and read its content line by line and append to the data list
        with open(path_, mode='r', newline='') as file:
            csv_file = csv.reader(file)
            # Skip the header row
            next(csv_file)
            # Iterate through each row in the CSV file
            for row in csv_file:

                # replace empty strings  with None
                modified_row = tuple(None if x == '' else x for x in row)

                data.append(tuple(modified_row))

            # Move the cursor back to the start of the file
            file.seek(0)

        print("{} Records have been successfully retrieved from the CSV file.".format(len(data)))
        return data
    
        

    except FileNotFoundError:
        print("File not found at path {path_}. Please check the file path.".format(path_))
        return []

    except Exception as e:
        print("An error occurred: {e}".format(e))
        return []








