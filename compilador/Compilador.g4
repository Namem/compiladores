grammar Compilador;

// REGRAS DE PARSER
programa: (comando)* EOF;

comando
    : declaracao
    | atribuicao
    | entrada
    | saida
    | condicional
    | repeticao
    ;

declaracao
    : tipo ID SEMI
    ;

atribuicao
    : ID ASSIGN expressao SEMI
    ;

entrada
    : LEIA LPAREN ID RPAREN SEMI
    ;

saida
    : ESCREVA LPAREN expressao RPAREN SEMI
    ;

condicional
    : SE expressao ENTAO (comando)* (SENAO (comando)*)? FIM
    ;

repeticao
    : ENQUANTO expressao FACA (comando)* FIM
    ;

expressao
    : expressao MULT expressao
    | expressao DIV expressao
    | expressao PLUS expressao
    | expressao MINUS expressao
    | expressao AND expressao
    | expressao OR expressao
    | NOT expressao
    | expressao EQ expressao
    | LPAREN expressao RPAREN
    | INT
    | STRING
    | ID
    ;

tipo
    : INT_TIPO
    | STRING_TIPO
    ;

// TOKENS DE LÉXICO
LEIA: 'leia';
ESCREVA: 'escreva';
SE: 'se';
SENAO: 'senao';
ENTAO: 'entao';
FIM: 'fim';
ENQUANTO: 'enquanto';
FACA: 'faca';

INT_TIPO: 'int';
STRING_TIPO: 'string';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
STRING: '"' .*? '"';

LPAREN: '(';
RPAREN: ')';
SEMI: ';';
ASSIGN: '=';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
AND: '&&';
OR: '||';
NOT: '!';
EQ: '==';
GT: '>';
LT: '<';

WS: [ \t\r\n]+ -> skip;
