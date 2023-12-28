from prototype.data.imagenet_evaluator import ImageNetEvaluator
from prototype.data.custom_evaluator import CustomEvaluator
from prototype.data.multiclass_evaluator import MultiClsEvaluator


def build_evaluator(cfg):
    evaluator = {
        'custom': CustomEvaluator,
        'imagenet': ImageNetEvaluator,
        'multiclass': MultiClsEvaluator,
    }[cfg['type']]
    return evaluator(**cfg['kwargs'])
