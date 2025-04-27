grammar Compilador;

/* Regras de Início */
programa : bloco EOF ;

bloco : (comando)* ;

comando
    : leitura
    | escrita
    | atribuicao
    | condicional
    | repeticao
    ;

/* Comandos */
leitura    : LEIA ABREPAR IDENT FECHAPAR PONTOVIRGULA ;
escrita    : ESCREVA ABREPAR expr FECHAPAR PONTOVIRGULA ;
atribuicao : IDENT ATRIBUICAO expr PONTOVIRGULA ;
condicional: SE expr ENTAO bloco (SENAO bloco)? FIM ;
repeticao  : ENQUANTO expr FACA bloco FIM ;

/* Expressões */
expr : exprLogico ;

exprLogico
    : exprLogico OU exprAnd   
    | exprAnd                   
    ;

exprAnd
    : exprAnd E exprIgualdade  
    | exprIgualdade              
    ;

exprIgualdade
    : exprComparacao ( (IGUAL | DIFERENTE | MENOR | MENORIGUAL | MAIOR | MAIORIGUAL) exprComparacao )*
    ;

exprComparacao
    : exprAritmetica
    ;

exprAritmetica
    : exprAritmetica (SOMA|SUB) termo  
    | termo                          
    ;

termo
    : termo (MULT|DIV) fator  
    | fator                
    ;

fator
    : ABREPAR expr FECHAPAR       
    | SUB fator           
    | NAO fator         
    | literal            
    | IDENT              
    ;

/* Literais */
literal
    : INT
    | STRING
    ;

/* Palavras Reservadas (ANTES DO IDENT) */
LEIA    : 'leia';
ESCREVA : 'escreva';
SE      : 'se';
SENAO   : 'senao';
ENTAO   : 'entao';
FIM     : 'fim';
ENQUANTO: 'enquanto';
FACA    : 'faca';

/* Tokens Literais */
INT    : [0-9]+ ;
STRING : '"' (~["\\] | '\\' .)* '"' ;

/* Identificadores */
IDENT  : [a-zA-Z_][a-zA-Z0-9_]* ;

/* Operadores e Símbolos */
ABREPAR     : '(';
FECHAPAR    : ')';
PONTOVIRGULA: ';';
ATRIBUICAO  : '=';
SOMA        : '+';
SUB         : '-';
MULT        : '*';
DIV         : '/';
E           : '&&';
OU          : '||';
NAO         : '!';
IGUAL       : '==';
DIFERENTE   : '~=';
MAIOR       : '>';
MENOR       : '<';
MAIORIGUAL  : '>=';
MENORIGUAL  : '<=';

/* Espaços e Comentários */
WS          : [ \t\r\n]+ -> skip ;
COMENTARIO  : '--' ~[\r\n]* -> skip ;
