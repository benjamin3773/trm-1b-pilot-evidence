#!/usr/bin/env python3
"""Reproduce archive counts and query-source overlap using Python's standard library."""
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parent

def read_rows(name):
    with (ROOT / name).open(newline="") as stream:
        return list(csv.DictReader(stream))

def main():
    analytics = json.loads((ROOT / "analytics.json").read_text())
    images = read_rows("results_images.csv")
    candidates = read_rows("results_candidates.csv")
    prompts = read_rows("sam_box_prompts.csv")
    assert len(images) == analytics["scored_images"] == 100
    assert len(candidates) == analytics["retained_candidates"] == 245
    assert len(prompts) == analytics["passing_candidates"] == 194
    found = sum(row["status"] == "found" for row in images)
    assert found == analytics["found_images"] == 80
    passing = sum(row["passes_threshold"].lower() == "true" for row in candidates)
    assert passing == 194
    assert all(float(row["score"]) >= analytics["min_score"] for row in prompts)
    sources = sorted({query.rsplit("_obj", 1)[0] for query in analytics["positive_queries"]})
    image_names = {Path(row["image_name"]).stem for row in images}
    overlap = sorted(set(sources) & image_names)
    assert len(sources) == len(overlap) == 4
    result = {
        "images": len(images),
        "found_images": found,
        "selection_fraction": found / len(images),
        "retained_candidates": len(candidates),
        "passing_candidates": passing,
        "box_prompt_rows": len(prompts),
        "positive_query_views": len(analytics["positive_queries"]),
        "unique_query_source_images": len(sources),
        "query_source_images_also_in_search": overlap,
        "negative_query_count": len(analytics["negative_queries"]),
        "interpretation": "Archive consistency and overlap checks only. Selection fraction is not verified accuracy, precision or recall."
    }
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
