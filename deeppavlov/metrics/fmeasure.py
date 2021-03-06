# Copyright 2017 Neural Networks and Deep Learning lab, MIPT
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from itertools import chain

from sklearn.metrics import f1_score

from deeppavlov.core.common.metrics_registry import register_metric
from deeppavlov.models.ner.evaluation import precision_recall_f1


@register_metric('ner_f1')
def ner_f1(y_true, y_predicted):
    _, y_predicted = zip(*y_predicted)
    y_true = list(chain(*y_true))
    y_predicted = list(chain(*y_predicted))
    results = precision_recall_f1(y_true,
                                  y_predicted,
                                  print_results=False)
    f1 = results['__total__']['f1']
    return f1

@register_metric('f1')
def round_f1(y_true, y_predicted):
    """
    Calculates F1 measure.

    Args:
        y_true: list of true values
        y_predicted: list of predicted values

    Returns:
        F1 score
    """
    predictions = [round(x) for x in y_predicted]
    return f1_score(y_true, predictions)

