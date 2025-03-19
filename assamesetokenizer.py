"""
Author: Dr. Kishore Kashyap
Department of Information Technology, Gauhati University
E-mail: kk@gauhati.ac.in
GitHub: https://github.com/KashyapKishore
"""

import re
import argparse
from typing import List

def tokenize_assamese(text: str) -> List[str]:
    """
    Tokenize Assamese text into words and punctuation.
    
    Args:
        text (str): Input text
    
    Returns:
        List[str]: List of tokens
    """
    tokens = []
    current_token = ""
    i = 0
    
    while i < len(text):
        char = text[i]
        
        # Handle spaces
        if char.isspace():
            if current_token:
                tokens.append(current_token)
                current_token = ""
        
        # Handle periods
        elif char == '.':
            # Check if period is part of abbreviation
            if i > 0 and is_abbreviation_period(text, i):
                # Add current token with period
                tokens.append(current_token + char)
                current_token = ""
            # Check if period is between numerals
            elif i > 0 and i < len(text) - 1 and is_period_between_numerals(text, i):
                current_token += char
                # Add the next numeral(s)
                i += 1
                while i < len(text) and is_assamese_numeral(text[i]):
                    current_token += text[i]
                    i += 1
                i -= 1  # Step back one since we'll increment at loop end
            else:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                tokens.append(char)
        
        # Handle colons
        elif char == ':':
            # Check if colon is part of time format
            if i > 0 and i < len(text) - 1 and is_time_format(text, i):
                current_token += char
                # Add the next numeral(s) until space or non-numeral/non-colon
                i += 1
                while i < len(text) and (is_assamese_numeral(text[i]) or text[i] == ':'):
                    current_token += text[i]
                    i += 1
                i -= 1  # Step back one since we'll increment at loop end
            else:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                tokens.append(char)
        
        # Handle apostrophes
        elif char == "'":
            # Check if apostrophe is part of word
            if i > 0 and i < len(text) - 1 and is_assamese_word_with_apostrophe(text, i):
                current_token += char
            else:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                tokens.append(char)
        
        # Handle quotation marks
        elif char == '"':
            # Always tokenize quotes separately
            if current_token:
                tokens.append(current_token)
            tokens.append(char)
            current_token = ""
            # Skip any following spaces
            i += 1
            while i < len(text) and text[i].isspace():
                i += 1
            i -= 1  # Step back one since we'll increment at loop end
        
        # Handle other punctuation
        elif char in ',!?।':
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
        
        # Handle all other characters
        else:
            current_token += char
        
        i += 1
    
    # Add any remaining token
    if current_token:
        tokens.append(current_token)
    
    return tokens

def is_assamese_word_with_apostrophe(text: str, pos: int) -> bool:
    """
    Check if apostrophe at given position is part of an Assamese word.
    
    Args:
        text (str): Input text
        pos (int): Position of apostrophe
    
    Returns:
        bool: True if apostrophe is part of word, False otherwise
    """
    if pos == 0 or pos == len(text) - 1:
        return False
    
    # Check if surrounded by Assamese characters
    prev_char = text[pos - 1]
    next_chars = text[pos + 1:pos + 2] if pos + 1 < len(text) else ''
    
    # Special case: অ' is a single character
    if prev_char == 'অ':
        return True
    
    # Check if previous and next characters are Assamese
    is_prev_assamese = bool(re.search(r'[\u0980-\u09FF]', prev_char))
    is_next_assamese = bool(re.search(r'[\u0980-\u09FF]', next_chars))
    
    return is_prev_assamese and is_next_assamese

def is_compound_word_hyphen(text: str, pos: int) -> bool:
    """
    Check if the hyphen at given position is part of a compound word.
    
    Args:
        text (str): Input text
        pos (int): Position of hyphen
    
    Returns:
        bool: True if hyphen joins compound word, False if it's for spacing
    """
    if pos == 0 or pos == len(text) - 1:
        return False
    
    # Check surrounding characters
    prev_char = text[pos - 1]
    next_char = text[pos + 1]
    
    # Assamese character ranges
    assamese_chars = set('অআইঈউঊঋঌএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযৰলৱশষসহড়ড়ঢ়ঢ়য়য়ৎংঃঁািীুূৃৄেৈোৌ্ৗ')
    
    # If both sides are Assamese characters or diacritics, it's a compound word
    is_compound = prev_char in assamese_chars and next_char in assamese_chars
    
    # Also check for common compound word patterns
    if pos > 1 and pos < len(text) - 2:
        prev_word = text[max(0, pos-5):pos].strip()
        next_word = text[pos+1:min(len(text), pos+6)].strip()
        compound_patterns = [
            ('উত্তৰ', 'পূৰ্ব'),
            ('দক্ষিণ', 'পূৰ্ব'),
            ('পূৰ্ব', 'পশ্চিম')
            # Add more common compound word patterns here
        ]
        for first, second in compound_patterns:
            if prev_word.endswith(first) and next_word.startswith(second):
                return True
    
    return is_compound

def is_assamese_numeral(char: str) -> bool:
    """
    Check if character is an Assamese numeral (০-৯).
    
    Args:
        char (str): Character to check
    
    Returns:
        bool: True if character is Assamese numeral
    """
    return '\u09E6' <= char <= '\u09EF'  # ০-৯

def is_assamese_letter(char: str) -> bool:
    """
    Check if character is an Assamese letter (non-numeral).
    
    Args:
        char (str): Character to check
    
    Returns:
        bool: True if character is Assamese letter
    """
    # Assamese Unicode ranges excluding numerals
    return bool(re.search(r'[\u0980-\u09E5\u09F0-\u09FF]', char))

def is_period_between_numerals(text: str, pos: int) -> bool:
    """
    Check if a period at the given position is between numerals.
    
    Args:
        text (str): Input text
        pos (int): Position of period
    
    Returns:
        bool: True if period is between numerals
    """
    if pos == 0 or pos == len(text) - 1:
        return False
    
    prev_char = text[pos - 1]
    next_char = text[pos + 1]
    
    return is_assamese_numeral(prev_char) and is_assamese_numeral(next_char)

def is_time_format(text: str, pos: int) -> bool:
    """
    Check if the colon at given position is part of a time format (e.g. ৯:৩:১).
    
    Args:
        text (str): Input text
        pos (int): Position of colon
    
    Returns:
        bool: True if colon is part of time format, False otherwise
    """
    if pos == 0 or pos == len(text) - 1:
        return False
    
    # Must have numerals on both sides
    prev_char = text[pos - 1]
    next_char = text[pos + 1]
    
    if not (is_assamese_numeral(prev_char) and is_assamese_numeral(next_char)):
        return False
    
    # Check for valid time format patterns
    # Look backwards for start of number sequence
    start = pos - 1
    while start > 0 and is_assamese_numeral(text[start - 1]):
        start -= 1
    
    # Look forwards for end of number/colon sequence
    end = pos + 1
    while end < len(text) - 1:
        next_char = text[end + 1]
        if not (is_assamese_numeral(next_char) or next_char == ':'):
            break
        end += 1
    
    # Extract the potential time format
    time_str = text[start:end + 1]
    
    # Check if it matches time format patterns
    parts = time_str.split(':')
    if len(parts) > 3:  # More than hours:minutes:seconds
        return False
        
    # All parts should be 1-2 digit numerals
    for part in parts:
        if not part or len(part) > 2 or not all(is_assamese_numeral(c) for c in part):
            return False
    
    return True

def is_abbreviation_period(text: str, pos: int) -> bool:
    """
    Check if the period at given position is part of an abbreviation.
    
    Args:
        text (str): Input text
        pos (int): Position of period
    
    Returns:
        bool: True if period is part of abbreviation, False otherwise
    """
    # Must have a character before
    if pos == 0:
        return False
    
    prev_char = text[pos - 1]
    
    # Assamese character ranges
    assamese_chars = set('অআইঈউঊঋঌএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযৰলৱশষসহড়ড়ঢ়ঢ়য়য়ৎংঃঁািীুূৃৄেৈোৌ্ৗ')
    
    # For abbreviations, we expect previous char to be Assamese
    if prev_char in assamese_chars:
        # End of text is valid
        if pos == len(text) - 1:
            return True
            
        next_char = text[pos + 1]
        # Space followed by Assamese char is valid
        if next_char.isspace():
            if pos + 2 < len(text) and text[pos + 2] in assamese_chars:
                return True
        # Directly followed by Assamese char is also valid
        elif next_char in assamese_chars:
            return True
            
    return False

def preprocess_text(text: str) -> str:
    """
    Preprocess text with special handling for Assamese text features.
    
    Args:
        text (str): Input text
    
    Returns:
        str: Preprocessed text
    """
    # Normalize 
    text = text.replace('\u2018', "'")  # Left single quote to regular
    text = text.replace('\u2019', "'")  # Right single quote to regular
    text = text.replace('\u201c', '"')  # Left double quote to regular
    text = text.replace('\u201d', '"')  # Right double quote to regular
    text = text.replace('\u0983', ':')  # Visargha to colon
    text = text.replace('র', 'ৰ')  # Bengali 'র'to Assamese 'ৰ'
    text = text.replace('য়', 'য়')  # Replace য+় with য়
    text = text.replace('1', '১')  # Replace য+় with য়
    text = text.replace('2', '২')
    text = text.replace('3', '৩')
    text = text.replace('4', '৪')
    text = text.replace('5', '৫')
    text = text.replace('6', '৬')
    text = text.replace('7', '৭')
    text = text.replace('8', '৮')
    text = text.replace('9', '৯')
    text = text.replace('0', '০')
    # First, handle quotes by adding spaces around them
    processed_chars = []
    for i, char in enumerate(text):
        # Check if current char is Assamese numeral and next char is Assamese letter
        if i < len(text) - 1 and is_assamese_numeral(char) and is_assamese_letter(text[i+1]):
            processed_chars.append(char)
            processed_chars.append(' ')  # Add space between numeral and letter
        elif char == '"':
            # Add space before quote if previous char isn't space
            if i > 0 and not text[i-1].isspace():
                processed_chars.append(' ')
            processed_chars.append(char)
            # Add space after quote if next char isn't space
            if i < len(text)-1 and not text[i+1].isspace():
                processed_chars.append(' ')
        else:
            processed_chars.append(char)
    text = ''.join(processed_chars)
    
    # Handle obvious punctuation marks, excluding period and colon
    punctuation_marks = ['।', ',', '!', '?', ';', '%']
    for mark in punctuation_marks:
        text = text.replace(mark, f' {mark} ')
    
    # Handle parentheses while preserving content
    for left, right in [('(', ')'), ('[', ']'), ('{', '}'), ('«', '»')]:
        text = text.replace(left, f' {left} ')
        text = text.replace(right, f' {right} ')
    
    # Special handling for apostrophes, hyphens, periods, and colons
    processed_text = []
    i = 0
    while i < len(text):
        if text[i] == "'":
            # Check if it's part of an Assamese word
            if is_assamese_word_with_apostrophe(text, i):
                processed_text.append(text[i])
            else:
                processed_text.append(' ' + text[i] + ' ')
        elif text[i] == '-':
            # Check if it's part of a compound word
            #if is_compound_word_hyphen(text, i):
            #    processed_text.append(text[i])
            #else:
                processed_text.append(' ' + text[i] + ' ')
        elif text[i] == '.':
            # Keep period if it's part of abbreviation or between numerals
            if (i > 0 and 
                (is_abbreviation_period(text, i) or 
                 is_period_between_numerals(text, i))):
                processed_text.append(text[i])
            else:
                processed_text.append(' ' + text[i] + ' ')
        elif text[i] == ':':
            # Keep colon if it's part of a time format
            if i > 0 and i < len(text) - 1 and is_time_format(text, i):
                processed_text.append(text[i])
            else:
                processed_text.append(' ' + text[i] + ' ')
        else:
            processed_text.append(text[i])
        i += 1
    
    text = ''.join(processed_text)
    
    # Normalize spaces - replace multiple spaces with single space
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

def tokenize_file(src_file: str, tgt_file: str) -> None:
    """
    Tokenize source file and save the results.
    
    Args:
        src_file (str): Input text file with Assamese text
        tgt_file (str): Output file for tokenized text
    """
    # Read source file
    with open(src_file, 'r', encoding='utf-8') as f:
        src_texts = [line.strip() for line in f if line.strip()]
    
    # Process each text
    processed_texts = []
    tokenized_texts = []
    for text in src_texts:
        # Preprocess text
        text = preprocess_text(text)
        processed_texts.append(text)
        
        # Tokenize text
        tokens = tokenize_assamese(text)
        # Join tokens with single space and ensure no consecutive spaces
        tokenized_text = ' '.join(tokens)
        tokenized_text = ' '.join(tokenized_text.split())  # Remove consecutive spaces
        tokenized_texts.append(tokenized_text)
    
    # Write tokenized output
    with open(tgt_file, 'w', encoding='utf-8') as f:
        for text in tokenized_texts:
            f.write(text + '\n')
    
    print(f"\nTokenization complete!")
    print(f"Source text: {src_file}")
    print(f"Tokenized output saved to: {tgt_file}")

def interactive_tokenize(text: str) -> List[str]:
    """
    Tokenize a single sentence and show detailed analysis.
    
    Args:
        text (str): Input text to tokenize
    
    Returns:
        List[str]: List of tokens
    """
    # Preprocess text
    preprocessed_text = preprocess_text(text)
    print(f"\nPreprocessed text: {preprocessed_text}")
    
    # Tokenize text
    tokens = tokenize_assamese(preprocessed_text)
    
    # Print analysis
    print(f"\nTokenization Analysis:")
    print(f"Input text: {preprocessed_text}")
    print(f"Tokens: {tokens}")
    print(f"Token boundaries: {' | '.join(tokens)}")
    print(f"Number of tokens: {len(tokens)}")
    
    # Print character-level analysis
    print(f"\nCharacter-level analysis:")
    print('|'.join(tokens))
    
    return tokens

def main():
    """Main function to parse arguments and tokenize data."""
    parser = argparse.ArgumentParser(description="Tokenize Assamese text")
    
    parser.add_argument(
        "--mode",
        type=str,
        choices=['tokenize', 'interactive'],
        default='interactive',
        help="Mode: 'tokenize' to process a file, 'interactive' for single sentences"
    )
    parser.add_argument(
        "--text",
        type=str,
        help="Text to tokenize in interactive mode"
    )
    parser.add_argument(
        "--src", 
        type=str, 
        help="Source text file (raw text)"
    )
    parser.add_argument(
        "--tgt", 
        type=str, 
        help="Target text file (tokenized output)"
    )
    
    args = parser.parse_args()
    
    if args.mode == 'tokenize':
        if not args.src or not args.tgt:
            parser.error("--src and --tgt are required for 'tokenize' mode")
        tokenize_file(args.src, args.tgt)
    else:  # interactive mode
        if not args.text:
            parser.error("--text is required for interactive mode")
        interactive_tokenize(args.text)

if __name__ == "__main__":
    main()
