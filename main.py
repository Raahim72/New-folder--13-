def get_user_input():
    result = ""
    num_sentences = int(input("How many sentences would you like to concatenate? "))
    
    for i in range(num_sentences):
        sentence = input(f"Enter sentence {i+1}: ")
        punctuation = input("Do you want to add punctuation (y/n)? ").strip().lower()
        
        if punctuation == 'y':
            mark = input("Enter the punctuation mark you want to add (e.g., '.', '!', '?'): ").strip()
            sentence += mark
        
        result += sentence + " "
    
    return result.strip()

def modify_case(text):
    choice = input("Do you want the text in uppercase or lowercase? (Enter 'U' for uppercase, 'L' for lowercase): ").strip().lower()
    
    if choice == 'u':
        return text.upper()
    elif choice == 'l':
        return text.lower()
    else:
        print("Invalid choice! Returning text as is.")
        return text

def main():
    print("Welcome to the Sentence Concatenator Program!")
    
    while True:
        concatenated_text = get_user_input()
        modified_text = modify_case(concatenated_text)
        
        print("\nConcatenated Text:")
        print(modified_text)
        
        continue_choice = input("\nDo you want to concatenate more sentences? (y/n): ").strip().lower()
        
        if continue_choice != 'y':
            print("Thank you for using the Sentence Concatenator Program. Goodbye!")
            break

if __name__ == "__main__":
    main()
