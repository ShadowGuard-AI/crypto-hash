import argparse
import hashlib
import logging
import os
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_argparse():
    """
    Sets up the command line argument parser.
    """
    parser = argparse.ArgumentParser(
        description="File and text hashing utilities for basic cryptographic operations."
    )
    parser.add_argument(
        "-t", "--text",
        help="Hash a given text string.",
        type=str
    )
    parser.add_argument(
        "-f", "--file",
        help="Hash the contents of a specified file.",
        type=str
    )
    parser.add_argument(
        "-a", "--algorithm",
        help="The hashing algorithm to use (default: sha256).",
        # algorithms_available also lists the SHAKE functions, whose
        # hexdigest() requires a length argument this tool never passes,
        # so offering them only set up a run that always failed. Offer the
        # fixed-length digests, which are what a hex digest tool can print.
        choices=sorted(a for a in hashlib.algorithms_available
                       if not a.startswith("shake")),
        default="sha256"
    )
    parser.add_argument(
        "-q", "--quiet",
        help="Suppress logging output.",
        action="store_true"
    )
    return parser

def hash_text(text, algorithm):
    """
    Hashes the given text using the specified algorithm.
    """
    try:
        logging.info(f"Hashing text with algorithm: {algorithm}")
        hasher = hashlib.new(algorithm)
        hasher.update(text.encode('utf-8'))
        return hasher.hexdigest()
    except ValueError as e:
        logging.error(f"Invalid hashing algorithm: {algorithm}")
        raise

def hash_file(filepath, algorithm):
    """
    Hashes the contents of a file using the specified algorithm.
    """
    if not os.path.isfile(filepath):
        logging.error(f"File not found: {filepath}")
        raise FileNotFoundError(f"File not found: {filepath}")
    try:
        logging.info(f"Hashing file '{filepath}' with algorithm: {algorithm}")
        hasher = hashlib.new(algorithm)
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except ValueError as e:
        logging.error(f"Invalid hashing algorithm: {algorithm}")
        raise

def main():
    """
    Main function to handle the CLI and perform hashing operations.
    """
    parser = setup_argparse()
    args = parser.parse_args()

    if args.quiet:
        logging.disable(logging.CRITICAL)

    if args.text is not None and args.file is not None:
        # The if/elif below used to hash the text and silently ignore a
        # file given in the same command, which is an easy mistake to miss
        # in a script. Refuse the combination instead of picking a winner.
        parser.error("Use only one of --text or --file, not both.")

    # is-not-None, not truthiness: -t "" asks for the hash of the empty
    # string, a well defined digest, and used to be refused as no input.
    if args.text is not None:
        try:
            result = hash_text(args.text, args.algorithm)
            print(f"Hashed text: {result}")
        except Exception as e:
            logging.error(f"Error hashing text: {e}")
            sys.exit(1)

    elif args.file is not None:
        try:
            result = hash_file(args.file, args.algorithm)
            print(f"Hashed file: {result}")
        except Exception as e:
            logging.error(f"Error hashing file: {e}")
            sys.exit(1)

    else:
        logging.error("No input provided. Use --text or --file options.")
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()