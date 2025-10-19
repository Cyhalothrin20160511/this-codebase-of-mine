import json
import os

def parse_data_file(filepath):
    """
    Parse a WordNet data file (e.g. data.noun, data.verb)
    and extract synset offset, POS, lemmas, and gloss.
    """
    entries = []
    pos = filepath.split(".")[-1]  # get part of speech from filename

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # Skip comments and empty lines
            if not line or line.startswith("#"):
                continue

            # Each valid data line contains " | " separating the gloss
            if " | " not in line:
                continue

            data_part, gloss = line.split(" | ", 1)
            data_fields = data_part.split()

            offset = data_fields[0]

            try:
                # w_cnt is in hexadecimal (number of words in synset)
                w_cnt_hex = data_fields[3]
                w_cnt = int(w_cnt_hex, 16)
            except Exception:
                continue

            lemmas = []
            idx = 4
            for _ in range(w_cnt):
                lemma = data_fields[idx].replace("_", " ")
                lemmas.append(lemma)
                idx += 2  # skip lemma and its lex_id

            entries.append({
                "offset": offset,
                "pos": pos,
                "lemmas": lemmas,
                "gloss": gloss.strip()
            })

    return entries


def extract_all_wordnet_data(directory="dict"):
    """
    Parse all WordNet data.* files in the given directory.
    """
    all_entries = []
    for fname in os.listdir(directory):
        if fname.startswith("data.") and not fname.endswith(".json"):
            filepath = os.path.join(directory, fname)
            print(f"Parsing {filepath} ...")
            all_entries.extend(parse_data_file(filepath))

    print(f"Total entries parsed: {len(all_entries)}")
    return all_entries


if __name__ == "__main__":
    output_file = "wordnet_data.json"

    # Parse all data.* files inside ./dict/
    entries = extract_all_wordnet_data("dict")

    # Save as JSON
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(entries)} entries to {output_file}")
