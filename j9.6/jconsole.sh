#!/bin/bash
#
# run jconsole (in terminal) from the J install directory

cd "$(dirname "$0")"
bin/jconsole "$@"
