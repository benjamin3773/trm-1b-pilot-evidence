# TRM Assignment 1B pilot evidence

This repository supports the DINOv3 pilot discussion in Sections 3.4 and 5.4 of the Learning Reflection. It provides portable copies of four archived record files, a small reproducible audit, and the proposed augmentation design discussed in Section 4.4.

These are development-pilot records. They do not demonstrate personal course completion, independent biological validation, multi-species performance, or a completed augmentation experiment.

## Files

| File | What it supports |
| --- | --- |
| [analytics.json](analytics.json) | Recorded model settings and aggregate counts. |
| [results_images.csv](results_images.csv) | 100 image-level rows, including 80 selected images. |
| [results_candidates.csv](results_candidates.csv) | 245 retained candidate rows. |
| [sam_box_prompts.csv](sam_box_prompts.csv) | 194 threshold-passing box prompts. |
| [evaluation_audit.md](evaluation_audit.md) | Interpretation of the recorded metrics and reference overlap. |
| [verification_report.json](verification_report.json) | Results of the archive consistency and overlap checks. |
| [verify_evidence.py](verify_evidence.py) | Standard-library script that reproduces those checks. |
| [augmentation_protocol.md](augmentation_protocol.md) | Proposed research design, not an executed experiment. |
| [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) | Original file hashes and a record of the portable-copy transformations. |

## Reproduce the audit

Run Python 3 from this folder:

```bash
python3 verify_evidence.py
```

Expected: 100 image rows; 80 selected images; 245 candidate rows; 194 passing candidates and prompt rows; eight positive query views from four source images, all four also present in the search corpus; zero negative queries. The selection fraction is 0.8, not verified accuracy or recall.

## Privacy and provenance

The original local files are unchanged. These publication copies omit precise coordinates, pose metadata, source-image URLs and local computer paths. Three path references in `analytics.json` use the portable CSV filenames. Counts, query identifiers, settings, scores and candidate coordinates are preserved. Candidate coordinates are pixel locations inside an image, not geographic coordinates.

Raw and derived imagery, the HTML gallery, the student report, signatures and personal completion records are not distributed here. This repository does not grant rights to the underlying imagery. The original checksums and exact removed-column list are in `SOURCE_MANIFEST.json`.

Packaging, technical tables and the retrospective archive checks were prepared with Codex assistance on 20 October 2026. They do not constitute the student's personal learning reflection. Any course-completion or learning-history claims require the student's own records and verification.
