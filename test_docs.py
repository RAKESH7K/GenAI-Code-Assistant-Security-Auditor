from modules import read_python_file, generate_docstring

# 1. Define the file we want to document (the dummy file you made)
target_file = "my_functions.py"

print(f"📄 Reading {target_file}...")
code_content = read_python_file(target_file)

if code_content:
    print("🤖 Asking Gemini to write documentation...")
    
    # 2. Call your new function
    docstring = generate_docstring(code_content)
    
    # 3. Show the result
    print("\n--- ✨ GENERATED DOCSTRING ✨ ---")
    print(docstring)
    print("---------------------------------")
else:
    print("❌ Could not read file. Did you create 'my_functions.py'?")