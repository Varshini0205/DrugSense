# Find medicine dose, frequency, and treatment duration.
# These details help describe how a medicine was used.

import re


DOSAGE_PATTERN = re.compile(
    r"\b\d+(?:\.\d+)?\s*(?:mg|mcg|g|ml|mL|mg/ml|%)\b",
    re.IGNORECASE,
)

FREQUENCY_PATTERNS = [
    r"\bonce\s+(?:a|per)\s+day\b",
    r"\btwice\s+(?:a|per)\s+day\b",
    r"\bthree times\s+(?:a|per)\s+day\b",
    r"\bfour times\s+(?:a|per)\s+day\b",
    r"\bonce\s+daily\b",
    r"\btwice\s+daily\b",
    r"\bthree times\s+daily\b",
    r"\bfour times\s+daily\b",
    r"\bevery\s+\d+\s+(?:hours?|days?)\b",
]

NUMBER_WORDS = (
    "one|two|three|four|five|six|seven|eight|nine|ten|"
    "eleven|twelve|thirteen|fourteen|fifteen|sixteen|"
    "seventeen|eighteen|nineteen|twenty"
)

DURATION_PATTERN = re.compile(
    rf"\b(?:for\s+)?(?:\d+|{NUMBER_WORDS})\s*"
    r"(?:day|days|week|weeks|month|months|year|years)\b",
    re.IGNORECASE,
)


def extract_dosages(text):
    """Find medicine dosage amounts."""

    if not isinstance(text, str):
        return []

    return [match.group(0) for match in DOSAGE_PATTERN.finditer(text)]


def extract_frequencies(text):
    """Find how often medicine is taken."""

    if not isinstance(text, str):
        return []

    matches = []

    for pattern in FREQUENCY_PATTERNS:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            matches.append((match.start(), match.group(0)))

    matches.sort(key=lambda item: item[0])

    return [value for _, value in matches]


def extract_durations(text):
    """Find how long medicine was used."""

    if not isinstance(text, str):
        return []

    return [match.group(0) for match in DURATION_PATTERN.finditer(text)]


def extract_medication_details(text):
    """Extract dosage, frequency, and duration."""

    return {
        "dosages": extract_dosages(text),
        "frequencies": extract_frequencies(text),
        "durations": extract_durations(text),
    }


if __name__ == "__main__":
    review = (
        "I take 500 mg twice daily for two weeks. "
        "Then I take 250 mg once daily for 5 days."
    )

    print(extract_medication_details(review))