# Build a simple timeline from the review.
# This keeps important events in the order they appear.

from nlp.events import extract_events
from nlp.temporal_information import extract_temporal_information


def build_timeline(text):
    """Build a simple event timeline."""

    if not isinstance(text, str) or not text.strip():
        return []

    events = extract_events(text)
    temporal_info = extract_temporal_information(text)

    timeline = []

    for event in events:
        item = {
            "event": event["event"],
            "expression": event["expression"],
            "position": event["start"],
            "temporal_information": [],
        }

        for temporal in temporal_info:
            if temporal["start"] >= event["start"] - 80:
                if temporal["start"] <= event["end"] + 80:
                    item["temporal_information"].append(
                        temporal
                    )

        timeline.append(item)

    timeline.sort(key=lambda item: item["position"])

    return timeline


if __name__ == "__main__":
    review = (
        "I started taking the medication. "
        "Three days later I developed nausea."
    )

    print(build_timeline(review))
