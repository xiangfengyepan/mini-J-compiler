#!/bin/bash
#
# run JQt from the J install directory.
#
# the Qt IDE must already be installed.

cd "$(dirname "$0")"
bin/jqt "$@"
