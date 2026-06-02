# WiFi CSI Fall Attack-Safety Demo Status Summary



## Current Status



This experiment has completed the first reproducible clean-to-FGSM attack-safety workflow using SenseFi, UT-HAR, and LeNet.



The current implementation demonstrates a window-level research pipeline:



```text

clean WiFi CSI activity-recognition baseline

-> clean prediction export

-> clean fall-vs-non-fall safety-proxy metrics

-> software-level FGSM perturbation

-> attacked prediction export

-> clean-vs-attacked safety-proxy metrics

-> FGSM epsilon sweep

-> summary figures

```



This is not the final thesis experiment. It is a reproducible implementation baseline and research demonstration.



---



## Repository Role



This work belongs in the implementation repository:



```text

secure-wifi-csi-healthcare-sensing

```



The companion evidence and literature-mapping repository is:



```text

ai-ml-wifi-sensing-hub

```



The evidence hub explains why safety-oriented metrics matter. This implementation repo shows how to calculate them.



---



## Baseline Configuration



```text

Benchmark: SenseFi / WiFi-CSI-Sensing-Benchmark

Dataset: UT_HAR_data

Model: LeNet

Device: CPU

Short baseline epochs: 5

Original SenseFi training setting: 200 epochs

Prediction split: SenseFi validation+test loader

Rows evaluated: 996

```



---



## Class Mapping



UT-HAR contains seven activity classes:



```text

0 = lie down

1 = fall

2 = walk

3 = pickup

4 = run

5 = sit down

6 = stand up

```



The binary safety-proxy mapping is:



```text

fall = class 1

non-fall = classes 0, 2, 3, 4, 5, 6

```



---



## Clean Baseline Result



The shortened clean baseline improved over five epochs:



```text

Epoch 01/5 | test_acc=0.2942

Epoch 02/5 | test_acc=0.2942

Epoch 03/5 | test_acc=0.4207

Epoch 04/5 | test_acc=0.5161

Epoch 05/5 | test_acc=0.6596

```



This confirms that the local SenseFi UT-HAR LeNet pipeline runs successfully and that the model learns useful structure from the processed CSI data.



---



## Clean Fall Safety-Proxy Metrics



```text

Total windows: 996

Fall windows: 89

Non-fall windows: 907



TP / detected falls: 57

FN / missed falls: 32

FP / false fall alarms: 32

TN / correct non-falls: 875



Accuracy: 0.9357

Recall / sensitivity: 0.6404

Missed fall rate: 0.3596

Specificity: 0.9647

False positive rate: 0.0353

Precision: 0.6404

F1-score: 0.6404

Balanced accuracy: 0.8026

```



---



## FGSM Attack Setting



The first attacked evaluation used:



```text

Attack type: FGSM

Attack level: software-level adversarial perturbation

Attack target: processed UT-HAR CSI tensors

Epsilon: 0.030

```



This is not a physical-world attack, SDR attack, packet injection attack, preamble manipulation attack, or over-the-air validation.



---



## FGSM-Attacked Fall Safety-Proxy Metrics at Epsilon 0.030



```text

TP / detected falls: 0

FN / missed falls: 89

FP / false fall alarms: 119

TN / correct non-falls: 788



Recall / sensitivity: 0.0000

Missed fall rate: 1.0000

Precision: 0.0000

F1-score: 0.0000

Balanced accuracy: 0.4344

```



---



## Clean-to-FGSM Degradation at Epsilon 0.030



```text

Missed fall rate change: +0.6404

False alarm count change: +87

Recall change: -0.6404

F1-score change: -0.6404

```



This shows that adversarial degradation can be translated into fall-focused safety-proxy terms, not only general accuracy drop.



---



## FGSM Epsilon Sweep



The epsilon sweep tested:



```text

epsilon = 0.000

epsilon = 0.005

epsilon = 0.010

epsilon = 0.020

epsilon = 0.030

```



Summary:



| Epsilon | Seven-Class Accuracy | Missed Fall Rate | False Fall Alarms | Recall / Sensitivity | F1-Score | Prediction Change Rate |

|---:|---:|---:|---:|---:|---:|---:|

| 0.000 | 0.6596 | 0.3596 | 32 | 0.6404 | 0.6404 | 0.0000 |

| 0.005 | 0.4116 | 0.7416 | 40 | 0.2584 | 0.3026 | 0.2871 |

| 0.010 | 0.2390 | 0.9888 | 45 | 0.0112 | 0.0148 | 0.4839 |

| 0.020 | 0.0622 | 1.0000 | 100 | 0.0000 | 0.0000 | 0.6827 |

| 0.030 | 0.0100 | 1.0000 | 119 | 0.0000 | 0.0000 | 0.7440 |



---



## Main Figure



The combined summary figure is:



```text

figures/fgsm_epsilon_combined_safety_summary.png

```



Supporting figures are:



```text

figures/fgsm_epsilon_vs_missed_fall_rate.png

figures/fgsm_epsilon_vs_false_alarm_count.png

figures/fgsm_epsilon_vs_recall.png

figures/fgsm_epsilon_vs_f1_score.png

```



---



## Main Takeaway



The first complete experiment shows that a WiFi CSI fall-related activity-recognition model can be evaluated using safety-proxy metrics before and after adversarial perturbation.



The key research contribution is not only showing an accuracy drop. The stronger contribution is translating model degradation into fall-focused safety-proxy outcomes:



```text

missed fall windows

false fall alarms

recall loss

F1-score loss

reduced alert trustworthiness

```



This supports the broader thesis motivation that adversarial robustness for healthcare-relevant WiFi sensing should be evaluated using safety-oriented metrics, not only conventional machine-learning or attack-success metrics.



---



## Claim Boundary



This experiment is a window-level research implementation baseline.



It is not:



```text

clinical validation

medical-device validation

real patient deployment

diagnostic evidence

regulatory evaluation

physical-layer attack validation

packet-level attack validation

preamble-level attack validation

SDR validation

over-the-air validation

event-level fall validation

long-lie validation

```



The current result should be interpreted as a reproducible software pipeline for translating adversarial model degradation into fall-focused safety-proxy metrics.

---

## PGD Single-Epsilon Attack Phase

The experiment now includes a first Projected Gradient Descent (PGD) attack phase.

PGD was implemented as a software-level iterative adversarial perturbation applied to processed UT-HAR CSI tensors. This phase extends the previous clean and FGSM workflow by adding a stronger iterative attack setting.

PGD configuration:

```text
epsilon = 0.030
alpha = 0.005
pgd_steps = 10
epochs = 5
device = CPU
```

Generated files:

```text
scripts/export_pgd_predictions_short.py
scripts/compute_pgd_safety_metrics.py
results/pgd_predictions_short_epsilon_0_03.csv
results/pgd_safety_proxy_metrics_epsilon_0_03.csv
notes/pgd_prediction_export_log.md
notes/pgd_safety_proxy_metrics_log.md
```

PGD safety-proxy metrics at `epsilon = 0.030`:

```text
total windows: 996
fall windows: 89
non-fall windows: 907

TP detected falls: 0
FN missed falls: 89
FP false fall alarms: 115
TN correct non-falls: 792

seven-class accuracy: 0.0000
binary accuracy: 0.7952
recall / sensitivity: 0.0000
missed fall rate: 1.0000
specificity: 0.8732
false positive rate: 0.1268
precision: 0.0000
F1-score: 0.0000
balanced accuracy: 0.4366
```

Clean-to-PGD safety degradation:

```text
detected falls decreased from 57 to 0
missed falls increased from 32 to 89
false fall alarms increased from 32 to 115
recall decreased from 0.6404 to 0.0000
missed fall rate increased from 0.3596 to 1.0000
F1-score decreased from 0.6404 to 0.0000
balanced accuracy decreased from 0.8026 to 0.4366
```

At this epsilon, PGD caused complete loss of fall recall in the window-level fall-vs-non-fall safety-proxy evaluation.

This result should not be interpreted as a full FGSM-vs-PGD comparison yet. A PGD epsilon sweep and a direct FGSM-vs-PGD comparison table are still needed before making broader claims about relative attack strength across epsilon values.

Claim boundary: this is not clinical validation, medical-device validation, diagnostic evidence, regulatory evaluation, real patient deployment evidence, event-level fall detection validation, long-lie validation, physical-layer attack validation, packet-level attack validation, preamble-level attack validation, SDR validation, or over-the-air validation.
