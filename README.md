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

### Command Line Interface

The tokenizer can be used from the command line with the following options:

```bash
python assamese-tokenizer.py --input input.txt --output tokenized.txt
python assamese-tokenizer.py --interactive
```

#### Arguments

- `--input`, `-i`: Input file containing Assamese text
- `--output`, `-o`: Output file for tokenized text
- `--interactive`, `-int`: Run in interactive mode for testing single sentences
- `--help`, `-h`: Show help message

### Interactive Mode

Interactive mode allows you to test the tokenizer with individual sentences:

```bash
python assamese-tokenizer.py --interactive
```

This will prompt you to enter Assamese text and will display detailed tokenization results.

### Programmatic Usage

You can also import and use the tokenizer in your Python code:

```python
from assamese_tokenizer import tokenize_assamese, preprocess_text

# Preprocess and tokenize text
text = "অসমীয়া ভাষাৰ এটা উদাহৰণ।"
preprocessed_text = preprocess_text(text)
tokens = tokenize_assamese(preprocessed_text)

print(tokens)
# Output: ['অসমীয়া', 'ভাষাৰ', 'এটা', 'উদাহৰণ', '।']
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

## Examples

Input:
```
ড৹ কিশোৰ কাশ্যপে গৌহাটী বিশ্ববিদ্যালয়ত কাম কৰে।
```

Output:
```
['ড৹', 'কিশোৰ', 'কাশ্যপে', 'গৌহাটী', 'বিশ্ববিদ্যালয়ত', 'কাম', 'কৰে', '।']
```

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
