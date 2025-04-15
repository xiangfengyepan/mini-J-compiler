ANTLR=antlr4
GRAMMAR=g.g4
GEN_FILES=gLexer.py gParser.py gVisitor.py

# Target per generar els fitxers de codi
all: $(GEN_FILES)

# Regla per generar els fitxers Python amb ANTLR
$(GEN_FILES): $(GRAMMAR)
	$(ANTLR) -Dlanguage=Python3 -visitor $(GRAMMAR)

# Netegem els fitxers generats per ANTLR
clean:
	rm -f *.pyc *.class $(GEN_FILES)

# Netegem completament tot, incloent fitxers auxiliars generats
realclean: clean
	rm -f g.tokens g.interp gLexer.tokens gLexer.interp gListener.py

# Netegem també les dades d'ANTL i __pycache__
pristine: realclean
	rm -rf __pycache__ .antlr

# Crea un entorn virtual amb pip i instala les dependències
venv:
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip && pip install antlr4-python3-runtime==4.13.2

# Executa el codi de Python després de generar tot
run: all
	. venv/bin/activate && python3 g.py ../tests/programa.j
