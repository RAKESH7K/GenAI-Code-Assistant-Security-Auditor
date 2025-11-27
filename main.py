
import sys
from pathlib import Path
from modules import start_chat,audit_code, get_code_file ,generate_docstring , review_code ,read_file ,select_files_from_List

def main():

    if len(sys.argv) < 2:
        print("please enter the file name properly")
        print("Usage python main.py <your-filename>")
        return ()

    target = Path(sys.argv[1])

    if target.is_dir():
        print(f"the {target} is an directory")
        program_files = get_code_file(target)

        if not program_files:
            print("error no python files found inside the folder")
            return ()
        file_to_review = select_files_from_List(program_files)
        if not file_to_review:
            return ()
    elif target.is_file():
        file_to_review = target
    else:
        print("ERROR!: Input is not a valid file or directory")
        return ()
    
    script_location = Path(__file__).parent
    
    print(f"processing the file {file_to_review}")
    code_content = read_file(file_to_review)
    if code_content is not None:
        if "--doc" in sys.argv:
            print("Generating document")
            review = generate_docstring(code_content)
            output_fileName = script_location/f"{file_to_review.stem}_doc.txt"
        elif "--audit" in sys.argv:
            print("auditing the code")
            review = audit_code(code_content)
            output_fileName = script_location/f"{file_to_review.stem}_audit.txt"
        elif "--chat" in sys.argv:
            start_chat(code_content)
            print("chat session ended")
            return()
        else:
             print("code to review takes")
             review = review_code(code_content)
             output_fileName = script_location/f"{file_to_review.stem}_review.txt"

        if review is not None:
            print("--- 🚀 CODE REVIEW START 🚀 ---")
            print(review)
            print("--- 🚀 CODE REVIEW End 🚀 ---")
            print(f"DEBUG: The file name varible is{output_fileName}")

            with open(output_fileName, 'w', encoding='utf-8')as file:
                file.write(review)
        else:
            print("Failed to get Gemini_API review ")

    else:
        print(f"failed to read file{file_to_review}")


if __name__ == "__main__":
    main()
