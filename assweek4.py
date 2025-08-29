try:
    filename = input("Enter the filename to read: ")

    
    with open(filename, "r") as f:
        text = f.read()

    word_count = len(text.split())

    
    processed_text = text.upper()

    
    with open("output.txt", "w") as f:
        f.write(processed_text)
        f.write("\n")
        f.write(f"Word Count: {word_count}\n")

    
    print(" output.txt created successfully!")

except FileNotFoundError:
    print(" Error: The file you entered does not exist.")
except IOError:
    print(" Error: There was a problem reading the file.")
