#!/bin/sh
#
# update the J engine
#
# run from the J install directory

cd "$(dirname "$0")"

bin/jconsole -js "exit je_update_jpacman_ load 'pacman'"
bin/jconsole -js "exit echo JVERSION"
