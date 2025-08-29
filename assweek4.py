
with open("input.txt", "w") as f:
    f.write("Python is powerful.\n")
    f.write("It is widely used in data science.\n")
    f.write("Artificial Intelligence is growing fast.\n")
    f.write("Programming improves problem solving skills.\n")
    f.write("Learning Python is fun!\n")

with open("input.txt", "r") as f:
    text = f.read()

word_count = len(text.split())
processed_text = text.upper()

with open("output.txt", "w") as f:
    f.write(processed_text)
    f.write("\n")
    f.write(f"Word Count: {word_count}\n")


print("✅ output.txt created successfully!")
