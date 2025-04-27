grammar MiniLua;

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
leitura    : 'leia' '(' IDENT ')' ';' ;
escrita    : 'escreva' '(' expr ')' ';' ;
atribuicao : IDENT '=' expr ';' ;
condicional: 'se' expr 'entao' bloco ('senao' bloco)? 'fim' ;
repeticao  : 'enquanto' expr 'faca' bloco 'fim' ;

/* Expressões */
expr : exprLogico ;

exprLogico
    : exprLogico '||' exprAnd   
    | exprAnd                   
    ;

exprAnd
    : exprAnd '&&' exprIgualdade  
    | exprIgualdade              
    ;

exprIgualdade
    : exprComparacao (('==' | '~=' | '<' | '<=' | '>' | '>=') exprComparacao)*
    ;

exprComparacao
    : exprAritmetica
    ;

exprAritmetica
    : exprAritmetica ('+'|'-') termo  
    | termo                          
    ;

termo
    : termo ('*'|'/') fator  
    | fator                
    ;

fator
    : '(' expr ')'       
    | '-' fator           
    | '!' fator         
    | literal            
    | IDENT              
    ;

/* Literais */
literal
    : INT
    | STRING
    ;

/* Tokens */
INT    : [0-9]+ ;
STRING : '"' (~["\\] | '\\' .)* '"' ;
IDENT  : [a-zA-Z_][a-zA-Z0-9_]* ;

/* Palavras Reservadas */
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '--' ~[\r\n]* -> skip ;