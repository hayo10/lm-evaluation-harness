from lm_eval.api.registry import AGGREGATION_REGISTRY, METRIC_REGISTRY, register_metric

def rouge_scores_fn(items):  # This is a passthrough function
    return items

def process_results(doc, results):
    metrics = "rouge_scores"
    scores = {}
    scores[metrics] = (results, doc, metrics)

    if metrics not in METRIC_REGISTRY:
            print('hi')
            register_metric(
                metric=metrics,
                higher_is_better=True,
                output_type="generate_until",
                aggregation="rouge_agg",
            )(rouge_scores_fn)
    return scores