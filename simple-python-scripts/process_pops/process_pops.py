import os
import re
import math
from collections import defaultdict


def script1(text):
    """Script 1: Merge same (pop_type, culture, religion) and sum their sizes"""
    pattern = re.compile(
        r'(\w+)\s*=\s*\{\s*'
        r'culture\s*=\s*(\w+)\s*'
        r'religion\s*=\s*(\w+)\s*'
        r'size\s*=\s*(\d+)\s*\}',
        re.MULTILINE
    )

    merged = defaultdict(int)
    for pop_type, culture, religion, size in pattern.findall(text):
        merged[(pop_type, culture, religion)] += int(size)

    output_lines = []
    for (pop_type, culture, religion), total in merged.items():
        block = f"""{pop_type} = {{
    culture = {culture}
    religion = {religion}
    size = {total}
}}"""
        output_lines.append(block)
    
    return "\n\n".join(output_lines)


def script2(text):
    """Script 2: Replace, filter, and round sizes"""
    def round_up_to_5(n):
        return int(math.ceil(n / 5.0)) * 5

    pattern = re.compile(
        r'(\w+)\s*=\s*\{\s*'
        r'culture\s*=\s*(\w+)\s*'
        r'religion\s*=\s*(\w+)\s*'
        r'size\s*=\s*(\d+)\s*\}',
        re.MULTILINE
    )

    data = defaultdict(dict)
    for pop_type, culture, religion, size in pattern.findall(text):
        # Replace "capitalists" with "aristocrats"
        if pop_type == "capitalists":
            pop_type = "aristocrats"
        # Skip "clerks"
        if pop_type == "clerks":
            continue
        data[culture][pop_type] = (religion, int(size))

    output_lines = []
    for culture in sorted(data.keys()):
        for pop_type in sorted(data[culture].keys()):
            religion, size = data[culture][pop_type]
            size_rounded = round_up_to_5(size)
            block = f"""{pop_type} = {{
    culture = {culture}
    religion = {religion}
    size = {size_rounded}
}}"""
            output_lines.append(block)

    return "\n\n".join(output_lines)


def main():
    import sys

    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Build the full path to pops.txt in the same directory
    pops_path = os.path.join(script_dir, "pops.txt")

    # Read input file
    if not os.path.exists(pops_path):
        print(f"File not found: {pops_path}")
        sys.exit(1)

    with open(pops_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Ask user which script to run
    choice = input("Select script to run (1 or 2): ").strip()

    if choice == "1":
        result = script1(text)
    elif choice == "2":
        result = script2(text)
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

    # Overwrite the file with the processed content
    with open(pops_path, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"Done! {pops_path} has been updated.")


if __name__ == "__main__":
    main()
