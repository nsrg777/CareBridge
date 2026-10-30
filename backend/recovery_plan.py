import re


def extract_section(text, heading, next_heading=None):

    pattern = re.escape(heading)

    if next_heading:
        next_pattern = re.escape(next_heading)
        regex = pattern + r"(.*?)" + next_pattern
    else:
        regex = pattern + r"(.*)"

    match = re.search(
        regex,
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        return match.group(1).strip()

    return "Not found in document"


def generate_recovery_plan(text):

    diagnosis = extract_section(
        text,
        "1. Discharge diagnosis",
        "2. Medication instructions"
    )

    medications = extract_section(
        text,
        "2. Medication instructions",
        "3. Activity and recovery notes"
    )

    recovery = extract_section(
        text,
        "3. Activity and recovery notes",
        "4. Follow-up"
    )

    follow_up = extract_section(
        text,
        "4. Follow-up",
        "5. Seek medical help"
    )

    warning_signs = extract_section(
        text,
        "5. Seek medical help",
        "END OF FICTIONAL SAMPLE"
    )

    return {
        "diagnosis": diagnosis,
        "medications": medications,
        "recovery_instructions": recovery,
        "follow_up": follow_up,
        "warning_signs": warning_signs
    }