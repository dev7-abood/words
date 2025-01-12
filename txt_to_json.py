import json

# Function to extract unique words from a file
def extract_words_to_json(input_file, output_file, min_length=5):
    try:
        # Read the text file
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Create a set to store unique words
        unique_words = set()

        # Process each line
        for line in lines:
            # Split words and filter by length
            words = line.strip().split()
            for word in words:
                # Remove punctuation and filter by length
                cleaned_word = ''.join(char for char in word if char.isalnum())
                if len(cleaned_word) >= min_length:
                    unique_words.add(cleaned_word)

        # Convert the set to a list and sort it
        words_list = sorted(unique_words)

        # Write the words to a JSON file
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump({"words": words_list}, json_file, ensure_ascii=False, indent=4)

        print(f"Successfully extracted {len(words_list)} unique words to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = 'input.txt'  # Replace with your text file path
output_file = 'got_words.json'  # Replace with your desired JSON file path
extract_words_to_json(input_file, output_file)
