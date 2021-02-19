#! /usr/bin/env bash
# SPDX-License-Identifier: zlib-acknowledgement

# NOTE(Ryan): W0311 --> Ignore spaces as tabs
pylint ~/prog/personal/ser/ser.py \
  --disable=W0311 \
  --rcfile=~/prog/personal/ser/misc/pylintrc \
  -j $(getconf _NPROCESSORS_ONLN)
