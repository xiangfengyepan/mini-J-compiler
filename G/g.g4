grammar g;

program: statement+;

statement
    : expr NEWLINE
    | funcDef
    ;

funcDef: ID ASSIGN expr NEWLINE;

expr
    : '(' expr ')'                          # parent
    | expr op=COMPOSE expr                  # composition
    | ID expr*                              # funcCall
    | op=(NEG|PLUS|MINUS|IDENTITY) expr     # unary
    | expr op=(MUL|DIV|MOD) expr            # aritmetic
    | expr op=(PLUS|MINUS) expr             # aritmetic
    | expr op=(EQUAL|NEG|LT|GT|LE|GE) expr  # relational
    | expr op=AND expr                      # logical
    | expr op=OR expr                       # logical
    | IDENTITY                              # identity
    | ID                                    # variable
    | INTVAL                                # value
    | FLOATVAL                              # value
    ;

ASSIGN      : '=:' ;
EQUAL       : '=' ;
LT          : '<';
GT          : '>';
LE          : '<=';
GE          : '>=';

AND         : '&';
OR          : '/';
NEG         : '~';

PLUS        : '+' ;
MINUS       : '-';
MUL         : '*';
DIV         : '%';
MOD         : '|';

IDENTITY    : ']' ;
COMPOSE     : '@:';  

INTVAL    : ('0'..'9')+ ;
FLOATVAL  : ('0'..'9')+ '.' ('0'..'9')+ ;
ID        : ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;

// Strings (in quotes) with escape sequences
STRING    : '"' ( ESC_SEQ | ~('\\'|'"') )* '"' ;

fragment
ESC_SEQ   : '\\' ('b'|'t'|'n'|'f'|'r'|'"'|'\''|'\\') ;

NEWLINE : '\r'? '\n' ;

COMMENT: 'NB.' ~[\r\n]* -> skip;

WS        : [ \t\r]+ -> skip ;    

