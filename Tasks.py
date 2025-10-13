#Task1
try:
    with open("D:/Python/Exception/sample.txt", "r") as file:
        content = file.readlines()
        for line in content:
            print(line.strip())
except Exception as e:
    print("An error occurred:", e)


#Task2
user_input = input("Give input: ")
try:
    with open("D:/Python/Exception/output.txt", "w") as file:
        file.write(user_input + "\n")
        print("Data written to file successfully.")
    additional_data= "This is whole addition which will be appended"
    with open("D:/Python/Exception/output.txt", "a") as file:
        file.write(additional_data)
        print("Additional data appended to file successfully.\n Check the file to see the changes.")

    with open("D:/Python/Exception/output.txt", "r") as file:
        content = file.readlines()
        for line in content:
            print(line.strip())

except Exception as e:
    print("An error occurred:", e)





    