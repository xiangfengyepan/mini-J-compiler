
# Projecte: Intèrpret del Llenguatge G (mini J) amb ANTLR, numpy i Python

Aquest projecte és un intèrpret per al llenguatge **G** que es una versio simplificada de J, 
implementat utilitzant **ANTLR** per a l'anàlisi lèxic i sintàctic, **Python** i **numpy**  per a l'avaluació. 
L'intèrpret permet executar programes escrits en J, amb funcionalitats com depuració, visualització de l'arbre de sintaxi i avaluació interactiva.

## Requisits

- Python 3.x
- ANTLR 4 (per generar els fitxers del lexer, parser i visitor)
- NumPy (per operacions aritmètiques i gestió d'arrays)
- Eines addicionals: `python3-venv` `make`, `dos2unix`, `delta`, `jconsole` (versió 9.6)

## Guia d'Instal·lació i Execució

**1. Instal·la les utilitats necessàries**

   Per garantir el funcionament correcte de `myTest`, instal·la els paquets requerits:

   ```bash
   sudo apt update && sudo apt install -y dos2unix delta
   ```
   dos2unix: Converteix els finals de línia entre formats DOS/Windows i UNIX
   delta: Millorador de visualització de diffs

**2a. Execució ràpida**:
   Pots directament executar 

   ```bash
   make
   ```
   Aixo crear el entorn virtual amb les dependencies juntament amb el test i finalment el make help

**2b. Execució manual**:
Instal·la l'entorn virtual i les dependències
   ```bash
   make venv
   ```

Genera nomes els fitxers d'ANTLR

   ```bash
   make antlr
   ```

Verifica que tot estigui llest executant una prova amb el program per defecte programa.j

   ```bash
   make run
   ```

---

## Arxius del Projecte

| Arxiu | Descripció |
|-------|-----------|
| `g.g4` | Gramàtica del llenguatge definida amb ANTLR |
| `TreeVisitor.py` | Visitor que imprimeix l'arbre del programa (mode `--tree`) |
| `EvalVisitor.py` | Visitor que avalua el programa |
| `OperatorRegistry.py` | Mòdul per gestionar operadors, composició de funcions i piles per els parametres |
| `utils.py` | Eines per a la depuració, errors listenners i el format del output del programa |
| `g.py` | Script principal que executa el llenguatge amb diferents modes (`--debug`, `--tree`, `--ia`, --test) |
| `Makefile` | Automatitza la generació, neteja i execució de l'intèrpret |
| `myTest` | Script per a l'automatització de proves de l'intèrpret |


## Ús del interpret

### Comandes `make` disponibles:

| Comanda    | Descripció |
|------------|-------------|
| `make venv`    | Crea l'entorn virtual i instal·la les dependències |
| `make antlr`   | Genera els fitxers d'ANTLR a partir de `g.g4` |
| `make run ARGS<...>`     | Executa l'intèrpret amb el fitxer de prova per defecte (`../tests/programa.j`) i amb els argunets que lis donis |
| `make runfile FILE=<arxiu.j> ARGS=<...>` | Executa l'intèrpret amb un fitxer específic i arguments addicionals |
| `make clean`   | Elimina fitxers temporals generats com `.pyc` i `.class` |
| `make pristine`| Realitza una neteja completa eliminant fitxers generats per ANTLR |
| `make realclean` | Neteja fitxers temporals i fitxers generats per ANTLR |
| `make test`    | Executa les proves automatitzades amb el script `myTest` |
| `make help`    | Mostra l'ajuda del Makefile |

---

### Execució de l'Intèrpret

Per executar l'intèrpret, pots utilitzar les següents comandes:

**1. Executar programa.j**

`make run ARGS=''` utilitzarà el fitxer per defecte, que és el mateix que executar:

```bash
make run ARGS='' === make runfile FILE="programa.j" ARGS=''
```

**2. Executar un fitxer J**

```bash
make runfile FILE='arxiu.j' ARGS=''
```

Aquesta comanda executarà el programa definit en el fitxer `.j` especificat. Pots afegir arguments opcionals com 
- `--ia`: interactive execution
- `--test`: generate .out
- `--debug`: print enter and exit visit
- `--tree`: print program tree estructure

**3. Executar el programa amb arguments**

```bash
make runfile FILE='arxiu.j' ARGS='--debug -- tree'
```

Aquesta comanda executarà el programa en mode depuració i tree, mostrant informació detallada del la estructura del programa i durant l'execució.

**Notes importants sobre els arguments:**

- Els arguments `--test`, `--ia`, `--debug` i `--tree` poden ser afegits a qualsevol de les comandes, make run o make runfile. Tambe es poden combinar amb certes restricions. Per exemple, pots utilitzar `make run ARGS='--debug --test'`, `make runfile ARGS='--debug'`, etc.
  
- **Incompatibilitat d'arguments**: El mode `--test` és incompatible amb `--ia` i `--tree` perquè el mode `--test` redirigeix el resultat a un fitxer (`.out`), mentre que els altres modes imprimeixen el resultat directament a la terminal.


---

## Decisions de Disseny

- **Composició d'Operadors**: El sistema admet operadors binaris i unitaris. També es poden compondre múltiples operadors dins de funcions. Els paràmetres de les funcions compostes es guarden en una pila (stack), igual que el paràmetre en la crida de la funció. D’aquesta manera, es guarden els valors i les funcions per separat per facilitar la crida a la funció. Les funcions tenen forma de llista per dividir les funcions compostes amb l’operador **'@:'**.

- **Operadors unaris i binaris**: Al fitxer **OperatorRegister.py** es guarden els operadors bàsics, com per exemple **'+'**, com a funcions lambda per ser cridades posteriorment dins de `<operator>Aritmetic`. Això permet reutilitzar-les a l’hora de definir funcions.

- **Tests**: El projecte inclou un conjunt de proves automatitzades que es poden executar amb `make test` per verificar el bon funcionament de l’intèrpret.

- **Gramàtica**:
  El programa es divideix en *statements*, els quals poden ser una expressió o una declaració.
  - Per a les expressions: estan separades les operacions aritmètiques en (unària, binària i *fold*).
  - Per a les declaracions: les variables i les funcions es declaren de manera separada per simplicitat, tot i que podrien anar juntes. Igual que amb les operacions aritmètiques, la declaració de funcions també es divideix en (unària, binària i *fold*) que són `simpleOperators`, i després `composeOperators` amb l’operador **'@:'**.


---


- Operadors amb flip doble fold
- Funcions amb un màxim d'un paràmetre?
- 2 | ]? -> 2 |
- `_ +` com a operador unari?
- ^: i -: no funcionen correctament...
- Recursivitat?
- Entrada d'usuari?
- Què hauria d'incloure el README?
- Funcions llargues, sintaxi de codi, comentaris?
- dos2unix?
- format codi?