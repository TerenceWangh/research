# coding=utf-8
# coding=utf-8
# Copyright 2020 SevenDim. All Rights Reserved.
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
# ==============================================================================
"""Research is base on TF-Slim for models."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# pylint:disable=g-bad-import-order,wildcard-import
from research.layers import *
from research.ops.variables import *

from research.ops import arg_scope as arg_scope_lib

# Move explicit import after wild-card imports to prevent accidental
# overwrites (such as summaries). Also use import x syntax, to directly
# access file, rather than previously imported symbols.

from research.data import data_decoder
from research.data import data_provider
from research.data import dataset
from research.data import dataset_data_provider
from research.data import parallel_reader
from research.data import prefetch_queue
from research.data import tfexample_decoder
from research.data import queues

import research.summaries as summaries
import research.model_analyzer as model_analyzer
import research.learning as learning
import research.evaluation as evaluation

import research.losses as losses
import research.metrics as metrics

from research.training import evaluation as train_eval
from research.training import training as training

arg_scope = arg_scope_lib.arg_scope
add_arg_scope = arg_scope_lib.add_arg_scope
current_arg_scope = arg_scope_lib.current_arg_scope
has_arg_scope = arg_scope_lib.has_arg_scope
arg_scoped_arguments = arg_scope_lib.arg_scoped_arguments
arg_scope_func_key = arg_scope_lib.arg_scope_func_key
