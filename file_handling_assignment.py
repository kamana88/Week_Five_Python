try:
    # Task 1: File Creation
    with open("my_file.txt", "w") as file:
        file.write("This is the first line.\n")
        file.write("Second line with a number: 42\n")
        file.write("Third line: Hello, World!\n")

    # Task 2: File Reading and Display
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("File contents:")
        print(content)

    # Task 3: File Appending
    with open("my_file.txt", "a") as file:
        file.write("Fourth line appended.\n")
        file.write("Fifth line appended: 3.14\n")
        file.write("Sixth line appended: Goodbye!\n")

    # Display the updated file contents
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nUpdated file contents:")
        print(content)

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"Error: {str(e)}")
finally:
    print("\nScript execution completed.")