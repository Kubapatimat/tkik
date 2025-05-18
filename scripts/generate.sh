#!/bin/bash
set -e
cd "$(dirname "$0")"
java -jar ./antlr-4.13.2-complete.jar -o ../circuitry/gen/ -listener -visitor -Dlanguage=Python3 -lib ../grammar/ ../grammar/CircuitryParser.g4 ../grammar/CircuitryLexer.g4