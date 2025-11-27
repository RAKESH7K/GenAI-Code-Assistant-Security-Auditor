from pathlib import Path

def get_code_file(folder):
    target = Path(folder)
    extenstions = ["*.py","*.c","*.cpp","*.java", "*.js"]
    all_file = []
    for ext in extenstions:
        all_file.extend(target.glob(ext))
    return all_file

def select_files_from_List(file_list):
    print("\n--- 🔎 program Files Found ---")
    for index, file in enumerate(file_list):
        print(f"[{index + 1}] {file.name}")
    print("-----------------------------")

    try:
        user_choice = int(input("ENTER the file number to review: "))
        corrected_index = user_choice - 1
        
        # Check if the number is valid (Safety check!)
        if 0 <= corrected_index < len(file_list):
            return file_list[corrected_index]
        else:
            print("❌ Invalid number selected.")
            return None
    except ValueError:
        print("❌ Please enter a valid number.")
        return None