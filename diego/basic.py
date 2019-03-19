#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
/Users/charleslai/PycharmProjects/diego/.vscode/diego.basic.py was created on 2019/03/18.
file in :relativeFile
Author: Charles_Lai
Email: lai.bluejay@gmail.com
"""
BINARY_CLASSIFICATION = 1
MULTICLASS_CLASSIFICATION = 2
MULTILABEL_CLASSIFICATION = 3
REGRESSION = 4

REGRESSION_TASKS = [REGRESSION]
CLASSIFICATION_TASKS = [BINARY_CLASSIFICATION, MULTICLASS_CLASSIFICATION,
                        MULTILABEL_CLASSIFICATION]

TASK_TYPES = REGRESSION_TASKS + CLASSIFICATION_TASKS

TASK_TYPES_TO_STRING = \
    {BINARY_CLASSIFICATION: 'binary.classification',
     MULTICLASS_CLASSIFICATION: 'multiclass.classification',
     MULTILABEL_CLASSIFICATION: 'multilabel.classification',
     REGRESSION: 'regression'}

STRING_TO_TASK_TYPES = \
    {'binary.classification': BINARY_CLASSIFICATION,
     'multiclass.classification': MULTICLASS_CLASSIFICATION,
     'multilabel.classification': MULTILABEL_CLASSIFICATION,
     'regression': REGRESSION}

