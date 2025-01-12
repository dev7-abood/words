import json

# Function to extract unique words from a file line by line
def extract_words_to_json(input_file, output_file, min_length=5):
    try:
        # Read the text file
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Initialize a list to store unique words with their index
        words_with_index = []
        words_seen = set()

        # Process each line
        for line in lines:
            # Split words and filter by length
            words = line.strip().split()
            for word in words:
                # Remove punctuation, normalize case, and filter by length
                cleaned_word = ''.join(char for char in word if char.isalnum()).lower()
                if len(cleaned_word) >= min_length and cleaned_word not in words_seen:
                    words_with_index.append((len(words_with_index), cleaned_word))
                    words_seen.add(cleaned_word)

        # Sort the words list by index (natural order already maintained)
        words_with_index.sort(key=lambda x: x[0])

        # Extract only words in their original order
        sorted_words = [word for _, word in words_with_index]

        # Write the words to a JSON file
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump({"words": sorted_words}, json_file, ensure_ascii=False, indent=4)

        print(f"Successfully extracted {len(sorted_words)} unique words to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = 'input.txt'  # Replace with your text file path
output_file = 'output.json'  # Replace with your desired JSON file path
extract_words_to_json(input_file, output_file)
