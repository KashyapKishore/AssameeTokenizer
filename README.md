# Assamese Tokenizer

A specialized tokenizer for the Assamese language that handles language-specific features and nuances.

## Author

**Dr. Kishore Kashyap**  
Department of Information Technology, Gauhati University  
Email: kk@gauhati.ac.in  
GitHub: [KashyapKishore](https://github.com/KashyapKishore)

## Overview

This tokenizer is specifically designed for Assamese text processing, addressing the unique linguistic characteristics of the Assamese language. It provides accurate tokenization by handling language-specific features such as:

- Compound words with hyphens
- Apostrophes within words
- Abbreviations with periods
- Time formats with colons
- Numerals and decimal points
- Special punctuation marks (including '।', the Assamese sentence separator)
- Quotation marks and other punctuation

## Features

- **Language-Specific Tokenization**: Handles Assamese-specific character sets and linguistic patterns
- **Smart Punctuation Handling**: Differentiates between punctuation marks that are part of words and those that are separate tokens
- **Compound Word Recognition**: Identifies and preserves compound words connected by hyphens
- **Abbreviation Detection**: Recognizes common Assamese abbreviations
- **Time Format Preservation**: Maintains time formats as single tokens
- **Decimal Number Handling**: Keeps decimal numbers as single tokens
- **Preprocessing**: Includes text normalization and cleaning specifically for Assamese text
- **Interactive Mode**: Allows for detailed analysis of tokenization results
- **File Processing**: Supports batch processing of text files

## Installation

```bash
git clone https://github.com/KashyapKishore/AssameseTokenizer.git
cd AssameseTokenizer
```

No additional dependencies are required beyond the Python standard library.

## Usage

The script can be run in two modes: `interactive` (for single sentences) and `tokenize` (for file processing).

### Interactive Mode

1.  **Run the script in interactive mode with a text input:**

    ```bash
    python assamesetokenizer.py --mode interactive --text "এইটো এটা উদাহৰণ বাক্য। ৯:৩০:১৫ বজাত ৰেলখন আহিব।"
    ```

    This will output:

    ```
    Preprocessed text: এইটো এটা উদাহৰণ বাক্য । ৯:৩০:১৫ বজাত ৰেলখন আহিব ।

    Tokenization Analysis:
    Input text: এইটো এটা উদাহৰণ বাক্য । ৯:৩০:১৫ বজাত ৰেলখন আহিব ।
    Tokens: ['এইটো', 'এটা', 'উদাহৰণ', 'বাক্য', '।', '৯:৩০:১৫', 'বজাত', 'ৰেলখন', 'আহিব', '।']
    Token boundaries: এইটো | এটা | উদাহৰণ | বাক্য | । | ৯:৩০:১৫ | বজাত | ৰেলখন | আহিব | ।
    Number of tokens: 10

    Character-level analysis:
    এইটো|এটা|উদাহৰণ|বাক্য|।|৯:৩০:১৫|বজাত|ৰেলখন|আহিব|।
    ```

2. Now you can test different assamese sentences to observe the character level anaysis and the tokenization.

### Tokenize File Mode

1.  **Prepare your input file:**
    Create a text file (e.g., `input.txt`) containing Assamese text, with each sentence on a new line.

    ```
    অসম এখন ৰাজ্য।
    ইয়াত বহুত নদী আছে।
    ব্ৰহ্মপুত্ৰ অসমৰ ডাঙৰ নদী।
    ```

2.  **Run the script in tokenize mode:**

    ```bash
    python assamesetokenizer.py --mode tokenize --src input.txt --tgt output.txt
    ```

    This will process the `input.txt` file, tokenize the text, and save the tokenized output to `output.txt`.

3.  **Check the output file:**
    The `output.txt` file will contain the tokenized text, with each token separated by a space.

    ```
    অসম এখন ৰাজ্য ।
    ইয়াত বহুত নদী আছে ।
    ব্ৰহ্মপুত্ৰ অসমৰ ডাঙৰ নদী ।
    ```
### Programmatic Usage

You can also use the Assamese tokenizer directly within your Python code. Here's how you can import and use the `tokenize_assamese` and `preprocess_text` functions:

1.  **Import the module:**

    ```python
    from assamese_tokenizer import tokenize_assamese, preprocess_text
    ```
    **Note:** make sure the `assamese-tokenizer.py` is in the same directory of your python file or added in the system path. if you want to use it as a module, rename the `assamese-tokenizer.py` to `assamese_tokenizer.py`

2.  **Preprocess and tokenize your text:**

    ```python
    assamese_text = "এইটো এটা উদাহৰণ বাক্য। ৯:৩০:১৫ বজাত ৰেলখন আহিব।"
    
    # Preprocess the text
    preprocessed_text = preprocess_text(assamese_text)
    print(f"Preprocessed text: {preprocessed_text}")
    
    # Tokenize the text
    tokens = tokenize_assamese(preprocessed_text)
    print(f"Tokens: {tokens}")
    ```

    This will output:

    ```
    Preprocessed text: এইটো এটা উদাহৰণ বাক্য । ৯:৩০:১৫ বজাত ৰেলখন আহিব ।
    Tokens: ['এইটো', 'এটা', 'উদাহৰণ', 'বাক্য', '।', '৯:৩০:১৫', 'বজাত', 'ৰেলখন', 'আহিব', '।']
    ```
3. You can also tokenize a file.
    ```python
    from assamese_tokenizer import tokenize_file

    input_file = "input.txt"
    output_file = "output.txt"

    tokenize_file(input_file, output_file)
    ```
    This will tokenize the input file and produce the tokenized output file.
```

## Technical Details

### Tokenization Process

1. **Preprocessing**: Normalizes text, handles special characters, and prepares for tokenization
2. **Character-by-Character Analysis**: Examines each character in context to determine token boundaries
3. **Special Case Handling**: Applies rules for language-specific features
4. **Token Extraction**: Produces a list of tokens based on the analysis

### Special Cases Handled

- **Apostrophes**: Identifies when apostrophes are part of words (e.g., "অ'")
- **Hyphens**: Determines whether hyphens connect compound words or serve as separate punctuation
- **Periods**: Distinguishes between sentence-ending periods, abbreviation periods, and decimal points
- **Colons**: Identifies time formats versus other uses of colons
- **Quotation Marks**: Handles quotation marks as separate tokens

## Applications

This tokenizer is particularly useful for:

- Natural Language Processing (NLP) for Assamese
- Machine Translation systems
- Text-to-Speech applications
- Information Retrieval systems
- Linguistic research on Assamese text

## Contributing

Contributions to improve the tokenizer are welcome. Please feel free to submit pull requests or open issues to suggest improvements or report bugs.


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use this tokenizer in your research, please cite:

```
Kashyap, K. (2025). Assamese Tokenizer: A specialized tokenizer for Assamese language processing.
GitHub repository: https://github.com/KashyapKishore/AssameseTokenizer
```

## Acknowledgments

- Department of Information Technology, Gauhati University
- Contributors to Assamese language processing research
