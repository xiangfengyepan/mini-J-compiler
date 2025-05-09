ANTLR=antlr4
GRAMMAR=g.g4
GEN_FILES=gLexer.py gParser.py gVisitor.py


all: venv pristine test help

antlr: $(GEN_FILES)

$(GEN_FILES): $(GRAMMAR)
	$(ANTLR) -Dlanguage=Python3 -no-listener -visitor $(GRAMMAR)

clean:
	rm -f *.pyc *.class $(GEN_FILES)

realclean: clean
	rm -f g.tokens g.interp gLexer.tokens gLexer.interp gListener.py

pristine: realclean
	rm -rf __pycache__ .antlr

venv:
	@echo "Creates a virtual environment and installs dependencies, this may take a while"
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip && pip install antlr4-python3-runtime==4.13.2 numpy

runfile: antlr
	. venv/bin/activate && python3 g.py $(FILE) $(ARGS)

run: antlr
	. venv/bin/activate && python3 g.py ../tests/programa.j $(ARGS)

test: antlr
	../myTest

# TODO
help:
	@echo "Makefile to manage ANTLR execution and compiler testing."
	@echo ""
	@echo "Usage:"
	@echo "  make [command] [arguments]"
	@echo ""
	@echo "Available commands:"
	@echo "  all          Runs everything: venv, pristine, and run"
	@echo "  antlr        Generates the .py files from the grammar file $(GRAMMAR)"
	@echo "  clean        Removes temporary files like .pyc and .class"
	@echo "  realclean    Removes temporary files and ANTLR-generated files"
	@echo "  pristine     Performs a full cleanup"
	@echo "  venv         Creates a virtual environment and installs dependencies"
	@echo "  runfile      Runs g.py with specified FILE and ARGS"
	@echo "  run          Runs g.py with the default test file (../tests/programa.j) and ARGS"
	@echo "  test         Runs myTest script"
	@echo "  help         Displays this help message"
	@echo ""
	@echo "Arguments for 'run' and 'runfile':"
	@echo "  FILE=<path>    Path to the input file (default: ../tests/programa.j)"
	@echo "  ARGS=<args>    Additional arguments for g.py (optional)"
	@echo ""
	@echo "Examples:"
	@echo "  make run"
	@echo "  make runfile FILE='example.j'"
	@echo "  make run ARGS='--debug --test'"
	@echo "  make runfile FILE='example.j' ARGS='--test'"
	@echo "  make clean"
	@echo "  make help"

.PHONY: venv

