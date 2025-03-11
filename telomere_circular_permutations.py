#!/usr/bin/env python3

def is_valid_sequence(seq):
    return all(base in "ACGTU" for base in seq.upper())


def circular_permutations(seq):
    return [seq[i:] + seq[:i] for i in range(len(seq))]


def complement_sequence(seq):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C", "U": "A"}  # For RNA, U -> A
    return "".join(complement[base] for base in seq.upper())


def highlight_sequence(sequence, known_repeat):
    if known_repeat in sequence:
        return sequence.replace(known_repeat, f'\033[91m{known_repeat}\033[0m')  # ANSI escape code for red
    return sequence


def process_sequence(known_repeat, input_seq):
    known_repeat = known_repeat.upper()
    input_seq = input_seq.upper()

    if not is_valid_sequence(known_repeat) or not is_valid_sequence(input_seq):
        print("Invalid input! Only DNA and RNA sequences are allowed.")
        return

    print("\nAncestral/Known repeat:", known_repeat)
    print("\nInput sequence (positive strand) in 5' to 3' direction:", input_seq)

    # 1. Circular permutations of the input sequence
    print("Circular permutations of the positive strand:")
    for perm in circular_permutations(input_seq):
        print(highlight_sequence(perm, known_repeat))

    # 2. Find complementary sequence and reverse it
    comp_seq = complement_sequence(input_seq)
    rev_comp_seq = comp_seq[::-1]

    print("\nComplementary sequence (negative strand) in 5' to 3' direction:", rev_comp_seq)

    # 3. Circular permutations of the complementary strand
    print("\nCircular permutations of the negative strand:")
    for perm in circular_permutations(rev_comp_seq):
        print(highlight_sequence(perm, known_repeat))


# Example usage
known_repeat = input("Enter the Ancestral/Known repeat: ").strip()
input_seq = input("Enter the DNA or RNA sequence: ").strip()
process_sequence(known_repeat, input_seq)
