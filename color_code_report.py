import csv
from color_code_constants import MAJOR_COLORS, MINOR_COLORS
from color_code_utils import get_color_from_pair_number

def generate_text_manual():
    lines = []
    total_pairs = len(MAJOR_COLORS) * len(MINOR_COLORS)
    for pair_number in range(1, total_pairs + 1):
        major, minor = get_color_from_pair_number(pair_number)
        lines.append(f"{pair_number:2} - {major} {minor}")
    return "\n".join(lines)

def generate_csv_report(file_path):
    total_pairs = len(MAJOR_COLORS) * len(MINOR_COLORS)
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Pair Number", "Major Color", "Minor Color"])
        for pair_number in range(1, total_pairs + 1):
            major, minor = get_color_from_pair_number(pair_number)
            writer.writerow([pair_number, major, minor])
