# Proposed augmentation protocol

Status: research design only. No classifier training or augmentation experiment is reported here.

| Item | Proposed approach |
| --- | --- |
| Comparison | Real-image training alone versus augmentation conditions. Exact augmentation procedures must be specified before execution. |
| Controls | Hold the classifier, real training examples and training budget consistent. |
| Eligibility | Proposed starting rules: 50 verified training positives per species and 20 positives across two reserved real test groups. These counts have not been achieved or checked by this archive. |
| Evaluation | Reserve real capture groups from training and tuning. Compare discrimination and calibration on these real test images. |
| Required outputs | Split records, exact augmentation settings, training logs, predictions and metric calculations. No gain is claimed. |

This design summary restates the existing learning reflection. It is not a record of course completion, a frozen protocol, a power analysis or an executed experiment.
