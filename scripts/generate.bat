@echo off
pushd "%~dp0"
java -jar .\antlr-4.13.2-complete.jar -Dlanguage=Python3 -o ..\grammar\ ..\grammar\CircuitryLexer.g4
java -jar .\antlr-4.13.2-complete.jar -Dlanguage=Python3 -o ..\grammar\ ..\grammar\CircuitryParser.g4