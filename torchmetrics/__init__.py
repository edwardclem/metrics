r"""Root package info."""
import logging as __logging
import os

from torchmetrics.__about__ import *  # noqa: F401, F403

_logger = __logging.getLogger("torchmetrics")
_logger.addHandler(__logging.StreamHandler())
_logger.setLevel(__logging.INFO)

_PACKAGE_ROOT = os.path.dirname(__file__)
_PROJECT_ROOT = os.path.dirname(_PACKAGE_ROOT)

from torchmetrics import functional  # noqa: E402
from torchmetrics.aggregation import CatMetric, MaxMetric, MeanMetric, MinMetric, SumMetric  # noqa: E402
from torchmetrics.audio import PIT, SDR, SI_SDR, SI_SNR, SNR  # noqa: E402
from torchmetrics.classification import (  # noqa: E402, F401
    AUC,
    AUROC,
    F1,
    ROC,
    Accuracy,
    AveragePrecision,
    BinnedAveragePrecision,
    BinnedPrecisionRecallCurve,
    BinnedRecallAtFixedPrecision,
    CalibrationError,
    CohenKappa,
    ConfusionMatrix,
    FBeta,
    HammingDistance,
    Hinge,
    IoU,
    JaccardIndex,
    KLDivergence,
    MatthewsCorrcoef,
    Precision,
    PrecisionRecallCurve,
    Recall,
    Specificity,
    StatScores,
)
from torchmetrics.image import PSNR, SSIM  # noqa: E402
from torchmetrics.metric import Metric  # noqa: E402
from torchmetrics.metric_collections import MetricCollection  # noqa: E402
from torchmetrics.regression import (  # noqa: E402
    CosineSimilarity,
    ExplainedVariance,
    MeanAbsoluteError,
    MeanAbsolutePercentageError,
    MeanSquaredError,
    MeanSquaredLogError,
    PearsonCorrcoef,
    R2Score,
    SpearmanCorrcoef,
    SymmetricMeanAbsolutePercentageError,
    TweedieDevianceScore,
)
from torchmetrics.retrieval import (  # noqa: E402
    RetrievalFallOut,
    RetrievalHitRate,
    RetrievalMAP,
    RetrievalMRR,
    RetrievalNormalizedDCG,
    RetrievalPrecision,
    RetrievalRecall,
    RetrievalRPrecision,
)
from torchmetrics.text import (  # noqa: E402
    TER,
    WER,
    BLEUScore,
    CharErrorRate,
    CHRFScore,
    MatchErrorRate,
    SacreBLEUScore,
    SQuAD,
    WordInfoLost,
    WordInfoPreserved,
)
from torchmetrics.wrappers import BootStrapper, MetricTracker, MinMaxMetric, MultioutputWrapper  # noqa: E402

__all__ = [
    "functional",
    "Accuracy",
    "AUC",
    "AUROC",
    "AveragePrecision",
    "BinnedAveragePrecision",
    "BinnedPrecisionRecallCurve",
    "BinnedRecallAtFixedPrecision",
    "BLEUScore",
    "BootStrapper",
    "CalibrationError",
    "CatMetric",
    "CHRFScore",
    "CohenKappa",
    "ConfusionMatrix",
    "CosineSimilarity",
    "TweedieDevianceScore",
    "ExplainedVariance",
    "F1",
    "FBeta",
    "HammingDistance",
    "Hinge",
    "JaccardIndex",
    "KLDivergence",
    "MatthewsCorrcoef",
    "MaxMetric",
    "MeanAbsoluteError",
    "MeanAbsolutePercentageError",
    "MeanMetric",
    "MeanSquaredError",
    "MeanSquaredLogError",
    "Metric",
    "MetricCollection",
    "MetricTracker",
    "MinMaxMetric",
    "MinMetric",
    "MultioutputWrapper",
    "PearsonCorrcoef",
    "PIT",
    "Precision",
    "PrecisionRecallCurve",
    "PSNR",
    "R2Score",
    "Recall",
    "RetrievalFallOut",
    "RetrievalHitRate",
    "RetrievalMAP",
    "RetrievalMRR",
    "RetrievalNormalizedDCG",
    "RetrievalPrecision",
    "RetrievalRecall",
    "RetrievalRPrecision",
    "ROC",
    "SacreBLEUScore",
    "SDR",
    "SI_SDR",
    "SI_SNR",
    "SNR",
    "SpearmanCorrcoef",
    "Specificity",
    "SQuAD",
    "SSIM",
    "StatScores",
    "SumMetric",
    "SymmetricMeanAbsolutePercentageError",
    "TER",
    "WER",
    "CharErrorRate",
    "MatchErrorRate",
    "WordInfoLost",
    "WordInfoPreserved",
]
