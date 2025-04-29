// Generated from /home/namem/Área de trabalho/Compiladores/compilador/Compilador.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CompiladorParser}.
 */
public interface CompiladorListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CompiladorParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(CompiladorParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(CompiladorParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorParser#bloco}.
	 * @param ctx the parse tree
	 */
	void enterBloco(CompiladorParser.BlocoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorParser#bloco}.
	 * @param ctx the parse tree
	 */
	void exitBloco(CompiladorParser.BlocoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorParser#comando}.
	 * @param ctx the parse tree
	 */
	void enterComando(CompiladorParser.ComandoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorParser#comando}.
	 * @param ctx the parse tree
	 */
	void exitComando(CompiladorParser.ComandoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorParser#leitura}.
	 * @param ctx the parse tree
	 */
	void enterLeitura(CompiladorParser.LeituraContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorParser#leitura}.
	 * @param ctx the parse tree
	 */
	void exitLeitura(CompiladorParser.LeituraContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorParser#escrita}.
	 * @param ctx the parse tree
	 */
	void enterEscrita(CompiladorParser.EscritaContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorParser#escrita}.
	 * @param ctx the parse tree
	 */
	void exitEscrita(CompiladorParser.EscritaContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorParser#atribuicao}.
	 * @param ctx the parse tree
	 */
	void enterAtribuicao(CompiladorParser.AtribuicaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorParser#atribuicao}.
	 * @param ctx the parse tree
	 */
	void exitAtribuicao(CompiladorParser.AtribuicaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorParser#condicional}.
	 * @param ctx the parse tree
	 */
	void enterCondicional(CompiladorParser.CondicionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorParser#condicional}.
	 * @param ctx the parse tree
	 */
	void exitCondicional(CompiladorParser.CondicionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorParser#repeticao}.
	 * @param ctx the parse tree
	 */
	void enterRepeticao(CompiladorParser.RepeticaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorParser#repeticao}.
	 * @param ctx the parse tree
	 */
	void exitRepeticao(CompiladorParser.RepeticaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(CompiladorParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(CompiladorParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorParser#exprLogico}.
	 * @param ctx the parse tree
	 */
	void enterExprLogico(CompiladorParser.ExprLogicoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorParser#exprLogico}.
	 * @param ctx the parse tree
	 */
	void exitExprLogico(CompiladorParser.ExprLogicoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorParser#exprAnd}.
	 * @param ctx the parse tree
	 */
	void enterExprAnd(CompiladorParser.ExprAndContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorParser#exprAnd}.
	 * @param ctx the parse tree
	 */
	void exitExprAnd(CompiladorParser.ExprAndContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorParser#exprIgualdade}.
	 * @param ctx the parse tree
	 */
	void enterExprIgualdade(CompiladorParser.ExprIgualdadeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorParser#exprIgualdade}.
	 * @param ctx the parse tree
	 */
	void exitExprIgualdade(CompiladorParser.ExprIgualdadeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorParser#exprComparacao}.
	 * @param ctx the parse tree
	 */
	void enterExprComparacao(CompiladorParser.ExprComparacaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorParser#exprComparacao}.
	 * @param ctx the parse tree
	 */
	void exitExprComparacao(CompiladorParser.ExprComparacaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorParser#exprAritmetica}.
	 * @param ctx the parse tree
	 */
	void enterExprAritmetica(CompiladorParser.ExprAritmeticaContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorParser#exprAritmetica}.
	 * @param ctx the parse tree
	 */
	void exitExprAritmetica(CompiladorParser.ExprAritmeticaContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorParser#termo}.
	 * @param ctx the parse tree
	 */
	void enterTermo(CompiladorParser.TermoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorParser#termo}.
	 * @param ctx the parse tree
	 */
	void exitTermo(CompiladorParser.TermoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorParser#fator}.
	 * @param ctx the parse tree
	 */
	void enterFator(CompiladorParser.FatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorParser#fator}.
	 * @param ctx the parse tree
	 */
	void exitFator(CompiladorParser.FatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(CompiladorParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(CompiladorParser.LiteralContext ctx);
}