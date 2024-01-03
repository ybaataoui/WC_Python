import argparse
import sys

def ccwc(filename=None, count_bytes=False, count_lines=False, count_words=False, count_chars=False):
    try:
        if filename:
            with open(filename, 'rb') as file:
                content = file.read()
        else:
            # If no filename is specified, read from standard input
            content = sys.stdin.buffer.read()

        byte_count = len(content)
        line_count = content.count(b'\n') + 1  # Counting lines by finding occurrences of newline character
        word_count = len(content.split())
        char_count = len(content)

        # Check if no options are provided, or if -c, -l, and -w options are specified
        if not (count_bytes or count_lines or count_words or count_chars):
            result = f"{line_count} {word_count} {byte_count} {filename if filename else ''}"
        else:
            result = f"{line_count if count_lines else ''} {word_count if count_words else ''} {byte_count if count_bytes else ''} {char_count if count_chars else ''} {filename if filename else ''}"
        
        print(result.strip())

    except FileNotFoundError:
        print(f"Error: {filename} not found")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A simple version of wc for Coding Challenges.')
    parser.add_argument('filename', nargs='?', help='Specify the filename to process. If not provided, reads from standard input.')
    parser.add_argument('-c', dest='count_bytes', action='store_true', help='Count the number of bytes in the file.')
    parser.add_argument('-l', dest='count_lines', action='store_true', help='Count the number of lines in the file.')
    parser.add_argument('-w', dest='count_words', action='store_true', help='Count the number of words in the file.')
    parser.add_argument('-m', dest='count_chars', action='store_true', help='Count the number of characters in the file (equivalent to -c if locale does not support multibyte characters).')

    args = parser.parse_args()
    ccwc(args.filename, args.count_bytes, args.count_lines, args.count_words, args.count_chars)
