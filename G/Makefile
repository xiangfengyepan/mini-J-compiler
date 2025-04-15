ANTLR=antlr4
GRAMMAR=g.g4
GEN_FILES=gLexer.py gParser.py gVisitor.py

all: $(GEN_FILES)

$(GEN_FILES): $(GRAMMAR)
	$(ANTLR) -Dlanguage=Python3 -visitor $(GRAMMAR)

clean:
	rm -f *.pyc *.class $(GEN_FILES)

realclean: clean
	rm -f g.tokens g.interp gLexer.tokens gLexer.interp gListener.py

pristine: realclean
	rm -rf __pycache__ .antlr

venv:
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip && pip install antlr4-python3-runtime==4.13.2 numpy

run: all
	. venv/bin/activate && python3 g.py ../tests/programa.j

.PHONY: venv

