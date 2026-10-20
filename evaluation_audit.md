# Retrospective audit of the saved pilot

The checks were packaged and rerun with Codex assistance on 20 October 2026. They inspect existing records; they do not rerun the image model or establish biological correctness.

| Saved evidence | Interpretation |
| --- | --- |
| 80 of 100 images have status `found`; threshold 0.75. | The recorded `detection_rate` of 0.8 is an image-selection fraction, not accuracy, precision or recall. |
| 245 candidate rows and 194 passing candidates and box-prompt rows. | These are model proposals; the counts do not establish verified organisms or segmentation quality. |
| Eight positive query views come from four source images also present in the search corpus. | Self-matching is possible. Exclude reference-source images and use separate capture groups in a future evaluation. |
| The negative-query list is empty. | This run cannot demonstrate a benefit from negative examples. |

The overlapping source identifiers are listed in `verification_report.json`. Run `python3 verify_evidence.py` to reproduce the checks.
