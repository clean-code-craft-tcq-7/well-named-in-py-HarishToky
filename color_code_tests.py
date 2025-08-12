from color_code_utils import get_color_from_pair_number, get_pair_number_from_color
from color_code_report import generate_text_manual, generate_csv_report
import tempfile, os

def test_number_to_pair(pair_number, expected_major_color, expected_minor_color):
    major_color, minor_color = get_color_from_pair_number(pair_number)
    assert major_color == expected_major_color
    assert minor_color == expected_minor_color

def test_pair_to_number(major_color, minor_color, expected_pair_number):
    pair_number = get_pair_number_from_color(major_color, minor_color)
    assert pair_number == expected_pair_number

def run_all_tests():
    # Original conversion tests
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)

    # New report tests
    manual_lines = generate_text_manual().splitlines()
    assert len(manual_lines) == 25
    assert manual_lines[0] == " 1 - White Blue"
    assert manual_lines[-1] == "25 - Violet Slate"

    tmp_file = tempfile.NamedTemporaryFile(delete=False)
    tmp_file.close()
    generate_csv_report(tmp_file.name)
    with open(tmp_file.name) as f:
        lines = f.read().splitlines()
    assert len(lines) == 26  # header + 25
    assert lines[1] == "1,White,Blue"
    assert lines[-1] == "25,Violet,Slate"
    os.remove(tmp_file.name)

    print("All tests passed ✅")

if __name__ == "__main__":
    run_all_tests()
