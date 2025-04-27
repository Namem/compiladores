// Generated from /home/namem/Área de trabalho/Compiladores/compilador/Compilador.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class CompiladorParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LEIA=1, ESCREVA=2, SE=3, SENAO=4, ENTAO=5, FIM=6, ENQUANTO=7, FACA=8, 
		INT=9, STRING=10, IDENT=11, ABREPAR=12, FECHAPAR=13, PONTOVIRGULA=14, 
		ATRIBUICAO=15, SOMA=16, SUB=17, MULT=18, DIV=19, E=20, OU=21, NAO=22, 
		IGUAL=23, DIFERENTE=24, MAIOR=25, MENOR=26, MAIORIGUAL=27, MENORIGUAL=28, 
		WS=29, COMENTARIO=30;
	public static final int
		RULE_programa = 0, RULE_bloco = 1, RULE_comando = 2, RULE_leitura = 3, 
		RULE_escrita = 4, RULE_atribuicao = 5, RULE_condicional = 6, RULE_repeticao = 7, 
		RULE_expr = 8, RULE_exprLogico = 9, RULE_exprAnd = 10, RULE_exprIgualdade = 11, 
		RULE_exprComparacao = 12, RULE_exprAritmetica = 13, RULE_termo = 14, RULE_fator = 15, 
		RULE_literal = 16;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "bloco", "comando", "leitura", "escrita", "atribuicao", "condicional", 
			"repeticao", "expr", "exprLogico", "exprAnd", "exprIgualdade", "exprComparacao", 
			"exprAritmetica", "termo", "fator", "literal"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'leia'", "'escreva'", "'se'", "'senao'", "'entao'", "'fim'", "'enquanto'", 
			"'faca'", null, null, null, "'('", "')'", "';'", "'='", "'+'", "'-'", 
			"'*'", "'/'", "'&&'", "'||'", "'!'", "'=='", "'~='", "'>'", "'<'", "'>='", 
			"'<='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LEIA", "ESCREVA", "SE", "SENAO", "ENTAO", "FIM", "ENQUANTO", "FACA", 
			"INT", "STRING", "IDENT", "ABREPAR", "FECHAPAR", "PONTOVIRGULA", "ATRIBUICAO", 
			"SOMA", "SUB", "MULT", "DIV", "E", "OU", "NAO", "IGUAL", "DIFERENTE", 
			"MAIOR", "MENOR", "MAIORIGUAL", "MENORIGUAL", "WS", "COMENTARIO"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Compilador.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CompiladorParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public BlocoContext bloco() {
			return getRuleContext(BlocoContext.class,0);
		}
		public TerminalNode EOF() { return getToken(CompiladorParser.EOF, 0); }
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			bloco();
			setState(35);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlocoContext extends ParserRuleContext {
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public BlocoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloco; }
	}

	public final BlocoContext bloco() throws RecognitionException {
		BlocoContext _localctx = new BlocoContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_bloco);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2190L) != 0)) {
				{
				{
				setState(37);
				comando();
				}
				}
				setState(42);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComandoContext extends ParserRuleContext {
		public LeituraContext leitura() {
			return getRuleContext(LeituraContext.class,0);
		}
		public EscritaContext escrita() {
			return getRuleContext(EscritaContext.class,0);
		}
		public AtribuicaoContext atribuicao() {
			return getRuleContext(AtribuicaoContext.class,0);
		}
		public CondicionalContext condicional() {
			return getRuleContext(CondicionalContext.class,0);
		}
		public RepeticaoContext repeticao() {
			return getRuleContext(RepeticaoContext.class,0);
		}
		public ComandoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando; }
	}

	public final ComandoContext comando() throws RecognitionException {
		ComandoContext _localctx = new ComandoContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_comando);
		try {
			setState(48);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEIA:
				enterOuterAlt(_localctx, 1);
				{
				setState(43);
				leitura();
				}
				break;
			case ESCREVA:
				enterOuterAlt(_localctx, 2);
				{
				setState(44);
				escrita();
				}
				break;
			case IDENT:
				enterOuterAlt(_localctx, 3);
				{
				setState(45);
				atribuicao();
				}
				break;
			case SE:
				enterOuterAlt(_localctx, 4);
				{
				setState(46);
				condicional();
				}
				break;
			case ENQUANTO:
				enterOuterAlt(_localctx, 5);
				{
				setState(47);
				repeticao();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LeituraContext extends ParserRuleContext {
		public TerminalNode LEIA() { return getToken(CompiladorParser.LEIA, 0); }
		public TerminalNode ABREPAR() { return getToken(CompiladorParser.ABREPAR, 0); }
		public TerminalNode IDENT() { return getToken(CompiladorParser.IDENT, 0); }
		public TerminalNode FECHAPAR() { return getToken(CompiladorParser.FECHAPAR, 0); }
		public TerminalNode PONTOVIRGULA() { return getToken(CompiladorParser.PONTOVIRGULA, 0); }
		public LeituraContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_leitura; }
	}

	public final LeituraContext leitura() throws RecognitionException {
		LeituraContext _localctx = new LeituraContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_leitura);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			match(LEIA);
			setState(51);
			match(ABREPAR);
			setState(52);
			match(IDENT);
			setState(53);
			match(FECHAPAR);
			setState(54);
			match(PONTOVIRGULA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EscritaContext extends ParserRuleContext {
		public TerminalNode ESCREVA() { return getToken(CompiladorParser.ESCREVA, 0); }
		public TerminalNode ABREPAR() { return getToken(CompiladorParser.ABREPAR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode FECHAPAR() { return getToken(CompiladorParser.FECHAPAR, 0); }
		public TerminalNode PONTOVIRGULA() { return getToken(CompiladorParser.PONTOVIRGULA, 0); }
		public EscritaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_escrita; }
	}

	public final EscritaContext escrita() throws RecognitionException {
		EscritaContext _localctx = new EscritaContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_escrita);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			match(ESCREVA);
			setState(57);
			match(ABREPAR);
			setState(58);
			expr();
			setState(59);
			match(FECHAPAR);
			setState(60);
			match(PONTOVIRGULA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtribuicaoContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(CompiladorParser.IDENT, 0); }
		public TerminalNode ATRIBUICAO() { return getToken(CompiladorParser.ATRIBUICAO, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode PONTOVIRGULA() { return getToken(CompiladorParser.PONTOVIRGULA, 0); }
		public AtribuicaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atribuicao; }
	}

	public final AtribuicaoContext atribuicao() throws RecognitionException {
		AtribuicaoContext _localctx = new AtribuicaoContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_atribuicao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			match(IDENT);
			setState(63);
			match(ATRIBUICAO);
			setState(64);
			expr();
			setState(65);
			match(PONTOVIRGULA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondicionalContext extends ParserRuleContext {
		public TerminalNode SE() { return getToken(CompiladorParser.SE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode ENTAO() { return getToken(CompiladorParser.ENTAO, 0); }
		public List<BlocoContext> bloco() {
			return getRuleContexts(BlocoContext.class);
		}
		public BlocoContext bloco(int i) {
			return getRuleContext(BlocoContext.class,i);
		}
		public TerminalNode FIM() { return getToken(CompiladorParser.FIM, 0); }
		public TerminalNode SENAO() { return getToken(CompiladorParser.SENAO, 0); }
		public CondicionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicional; }
	}

	public final CondicionalContext condicional() throws RecognitionException {
		CondicionalContext _localctx = new CondicionalContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_condicional);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(SE);
			setState(68);
			expr();
			setState(69);
			match(ENTAO);
			setState(70);
			bloco();
			setState(73);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SENAO) {
				{
				setState(71);
				match(SENAO);
				setState(72);
				bloco();
				}
			}

			setState(75);
			match(FIM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RepeticaoContext extends ParserRuleContext {
		public TerminalNode ENQUANTO() { return getToken(CompiladorParser.ENQUANTO, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode FACA() { return getToken(CompiladorParser.FACA, 0); }
		public BlocoContext bloco() {
			return getRuleContext(BlocoContext.class,0);
		}
		public TerminalNode FIM() { return getToken(CompiladorParser.FIM, 0); }
		public RepeticaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_repeticao; }
	}

	public final RepeticaoContext repeticao() throws RecognitionException {
		RepeticaoContext _localctx = new RepeticaoContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_repeticao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			match(ENQUANTO);
			setState(78);
			expr();
			setState(79);
			match(FACA);
			setState(80);
			bloco();
			setState(81);
			match(FIM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public ExprLogicoContext exprLogico() {
			return getRuleContext(ExprLogicoContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			exprLogico(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprLogicoContext extends ParserRuleContext {
		public ExprAndContext exprAnd() {
			return getRuleContext(ExprAndContext.class,0);
		}
		public ExprLogicoContext exprLogico() {
			return getRuleContext(ExprLogicoContext.class,0);
		}
		public TerminalNode OU() { return getToken(CompiladorParser.OU, 0); }
		public ExprLogicoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprLogico; }
	}

	public final ExprLogicoContext exprLogico() throws RecognitionException {
		return exprLogico(0);
	}

	private ExprLogicoContext exprLogico(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprLogicoContext _localctx = new ExprLogicoContext(_ctx, _parentState);
		ExprLogicoContext _prevctx = _localctx;
		int _startState = 18;
		enterRecursionRule(_localctx, 18, RULE_exprLogico, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(86);
			exprAnd(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(93);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExprLogicoContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exprLogico);
					setState(88);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(89);
					match(OU);
					setState(90);
					exprAnd(0);
					}
					} 
				}
				setState(95);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprAndContext extends ParserRuleContext {
		public ExprIgualdadeContext exprIgualdade() {
			return getRuleContext(ExprIgualdadeContext.class,0);
		}
		public ExprAndContext exprAnd() {
			return getRuleContext(ExprAndContext.class,0);
		}
		public TerminalNode E() { return getToken(CompiladorParser.E, 0); }
		public ExprAndContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprAnd; }
	}

	public final ExprAndContext exprAnd() throws RecognitionException {
		return exprAnd(0);
	}

	private ExprAndContext exprAnd(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprAndContext _localctx = new ExprAndContext(_ctx, _parentState);
		ExprAndContext _prevctx = _localctx;
		int _startState = 20;
		enterRecursionRule(_localctx, 20, RULE_exprAnd, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(97);
			exprIgualdade();
			}
			_ctx.stop = _input.LT(-1);
			setState(104);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExprAndContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exprAnd);
					setState(99);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(100);
					match(E);
					setState(101);
					exprIgualdade();
					}
					} 
				}
				setState(106);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprIgualdadeContext extends ParserRuleContext {
		public List<ExprComparacaoContext> exprComparacao() {
			return getRuleContexts(ExprComparacaoContext.class);
		}
		public ExprComparacaoContext exprComparacao(int i) {
			return getRuleContext(ExprComparacaoContext.class,i);
		}
		public List<TerminalNode> IGUAL() { return getTokens(CompiladorParser.IGUAL); }
		public TerminalNode IGUAL(int i) {
			return getToken(CompiladorParser.IGUAL, i);
		}
		public List<TerminalNode> DIFERENTE() { return getTokens(CompiladorParser.DIFERENTE); }
		public TerminalNode DIFERENTE(int i) {
			return getToken(CompiladorParser.DIFERENTE, i);
		}
		public List<TerminalNode> MENOR() { return getTokens(CompiladorParser.MENOR); }
		public TerminalNode MENOR(int i) {
			return getToken(CompiladorParser.MENOR, i);
		}
		public List<TerminalNode> MENORIGUAL() { return getTokens(CompiladorParser.MENORIGUAL); }
		public TerminalNode MENORIGUAL(int i) {
			return getToken(CompiladorParser.MENORIGUAL, i);
		}
		public List<TerminalNode> MAIOR() { return getTokens(CompiladorParser.MAIOR); }
		public TerminalNode MAIOR(int i) {
			return getToken(CompiladorParser.MAIOR, i);
		}
		public List<TerminalNode> MAIORIGUAL() { return getTokens(CompiladorParser.MAIORIGUAL); }
		public TerminalNode MAIORIGUAL(int i) {
			return getToken(CompiladorParser.MAIORIGUAL, i);
		}
		public ExprIgualdadeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprIgualdade; }
	}

	public final ExprIgualdadeContext exprIgualdade() throws RecognitionException {
		ExprIgualdadeContext _localctx = new ExprIgualdadeContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_exprIgualdade);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			exprComparacao();
			setState(112);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(108);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 528482304L) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(109);
					exprComparacao();
					}
					} 
				}
				setState(114);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprComparacaoContext extends ParserRuleContext {
		public ExprAritmeticaContext exprAritmetica() {
			return getRuleContext(ExprAritmeticaContext.class,0);
		}
		public ExprComparacaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprComparacao; }
	}

	public final ExprComparacaoContext exprComparacao() throws RecognitionException {
		ExprComparacaoContext _localctx = new ExprComparacaoContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_exprComparacao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			exprAritmetica(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprAritmeticaContext extends ParserRuleContext {
		public TermoContext termo() {
			return getRuleContext(TermoContext.class,0);
		}
		public ExprAritmeticaContext exprAritmetica() {
			return getRuleContext(ExprAritmeticaContext.class,0);
		}
		public TerminalNode SOMA() { return getToken(CompiladorParser.SOMA, 0); }
		public TerminalNode SUB() { return getToken(CompiladorParser.SUB, 0); }
		public ExprAritmeticaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprAritmetica; }
	}

	public final ExprAritmeticaContext exprAritmetica() throws RecognitionException {
		return exprAritmetica(0);
	}

	private ExprAritmeticaContext exprAritmetica(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprAritmeticaContext _localctx = new ExprAritmeticaContext(_ctx, _parentState);
		ExprAritmeticaContext _prevctx = _localctx;
		int _startState = 26;
		enterRecursionRule(_localctx, 26, RULE_exprAritmetica, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(118);
			termo(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(125);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExprAritmeticaContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exprAritmetica);
					setState(120);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(121);
					_la = _input.LA(1);
					if ( !(_la==SOMA || _la==SUB) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(122);
					termo(0);
					}
					} 
				}
				setState(127);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermoContext extends ParserRuleContext {
		public FatorContext fator() {
			return getRuleContext(FatorContext.class,0);
		}
		public TermoContext termo() {
			return getRuleContext(TermoContext.class,0);
		}
		public TerminalNode MULT() { return getToken(CompiladorParser.MULT, 0); }
		public TerminalNode DIV() { return getToken(CompiladorParser.DIV, 0); }
		public TermoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termo; }
	}

	public final TermoContext termo() throws RecognitionException {
		return termo(0);
	}

	private TermoContext termo(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		TermoContext _localctx = new TermoContext(_ctx, _parentState);
		TermoContext _prevctx = _localctx;
		int _startState = 28;
		enterRecursionRule(_localctx, 28, RULE_termo, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(129);
			fator();
			}
			_ctx.stop = _input.LT(-1);
			setState(136);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new TermoContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_termo);
					setState(131);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(132);
					_la = _input.LA(1);
					if ( !(_la==MULT || _la==DIV) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(133);
					fator();
					}
					} 
				}
				setState(138);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FatorContext extends ParserRuleContext {
		public TerminalNode ABREPAR() { return getToken(CompiladorParser.ABREPAR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode FECHAPAR() { return getToken(CompiladorParser.FECHAPAR, 0); }
		public TerminalNode SUB() { return getToken(CompiladorParser.SUB, 0); }
		public FatorContext fator() {
			return getRuleContext(FatorContext.class,0);
		}
		public TerminalNode NAO() { return getToken(CompiladorParser.NAO, 0); }
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode IDENT() { return getToken(CompiladorParser.IDENT, 0); }
		public FatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fator; }
	}

	public final FatorContext fator() throws RecognitionException {
		FatorContext _localctx = new FatorContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_fator);
		try {
			setState(149);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ABREPAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(139);
				match(ABREPAR);
				setState(140);
				expr();
				setState(141);
				match(FECHAPAR);
				}
				break;
			case SUB:
				enterOuterAlt(_localctx, 2);
				{
				setState(143);
				match(SUB);
				setState(144);
				fator();
				}
				break;
			case NAO:
				enterOuterAlt(_localctx, 3);
				{
				setState(145);
				match(NAO);
				setState(146);
				fator();
				}
				break;
			case INT:
			case STRING:
				enterOuterAlt(_localctx, 4);
				{
				setState(147);
				literal();
				}
				break;
			case IDENT:
				enterOuterAlt(_localctx, 5);
				{
				setState(148);
				match(IDENT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(CompiladorParser.INT, 0); }
		public TerminalNode STRING() { return getToken(CompiladorParser.STRING, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==STRING) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 9:
			return exprLogico_sempred((ExprLogicoContext)_localctx, predIndex);
		case 10:
			return exprAnd_sempred((ExprAndContext)_localctx, predIndex);
		case 13:
			return exprAritmetica_sempred((ExprAritmeticaContext)_localctx, predIndex);
		case 14:
			return termo_sempred((TermoContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean exprLogico_sempred(ExprLogicoContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean exprAnd_sempred(ExprAndContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean exprAritmetica_sempred(ExprAritmeticaContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean termo_sempred(TermoContext _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001e\u009a\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0005\u0001\'\b\u0001\n\u0001\f\u0001*\t\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u00021\b\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006J\b"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t"+
		"\u0001\t\u0001\t\u0001\t\u0005\t\\\b\t\n\t\f\t_\t\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0005\ng\b\n\n\n\f\nj\t\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0005\u000bo\b\u000b\n\u000b\f\u000br\t\u000b\u0001"+
		"\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0005\r|\b"+
		"\r\n\r\f\r\u007f\t\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0005\u000e\u0087\b\u000e\n\u000e\f\u000e\u008a\t\u000e"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u0096\b\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0000\u0004\u0012\u0014\u001a\u001c"+
		"\u0011\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018"+
		"\u001a\u001c\u001e \u0000\u0004\u0001\u0000\u0017\u001c\u0001\u0000\u0010"+
		"\u0011\u0001\u0000\u0012\u0013\u0001\u0000\t\n\u0097\u0000\"\u0001\u0000"+
		"\u0000\u0000\u0002(\u0001\u0000\u0000\u0000\u00040\u0001\u0000\u0000\u0000"+
		"\u00062\u0001\u0000\u0000\u0000\b8\u0001\u0000\u0000\u0000\n>\u0001\u0000"+
		"\u0000\u0000\fC\u0001\u0000\u0000\u0000\u000eM\u0001\u0000\u0000\u0000"+
		"\u0010S\u0001\u0000\u0000\u0000\u0012U\u0001\u0000\u0000\u0000\u0014`"+
		"\u0001\u0000\u0000\u0000\u0016k\u0001\u0000\u0000\u0000\u0018s\u0001\u0000"+
		"\u0000\u0000\u001au\u0001\u0000\u0000\u0000\u001c\u0080\u0001\u0000\u0000"+
		"\u0000\u001e\u0095\u0001\u0000\u0000\u0000 \u0097\u0001\u0000\u0000\u0000"+
		"\"#\u0003\u0002\u0001\u0000#$\u0005\u0000\u0000\u0001$\u0001\u0001\u0000"+
		"\u0000\u0000%\'\u0003\u0004\u0002\u0000&%\u0001\u0000\u0000\u0000\'*\u0001"+
		"\u0000\u0000\u0000(&\u0001\u0000\u0000\u0000()\u0001\u0000\u0000\u0000"+
		")\u0003\u0001\u0000\u0000\u0000*(\u0001\u0000\u0000\u0000+1\u0003\u0006"+
		"\u0003\u0000,1\u0003\b\u0004\u0000-1\u0003\n\u0005\u0000.1\u0003\f\u0006"+
		"\u0000/1\u0003\u000e\u0007\u00000+\u0001\u0000\u0000\u00000,\u0001\u0000"+
		"\u0000\u00000-\u0001\u0000\u0000\u00000.\u0001\u0000\u0000\u00000/\u0001"+
		"\u0000\u0000\u00001\u0005\u0001\u0000\u0000\u000023\u0005\u0001\u0000"+
		"\u000034\u0005\f\u0000\u000045\u0005\u000b\u0000\u000056\u0005\r\u0000"+
		"\u000067\u0005\u000e\u0000\u00007\u0007\u0001\u0000\u0000\u000089\u0005"+
		"\u0002\u0000\u00009:\u0005\f\u0000\u0000:;\u0003\u0010\b\u0000;<\u0005"+
		"\r\u0000\u0000<=\u0005\u000e\u0000\u0000=\t\u0001\u0000\u0000\u0000>?"+
		"\u0005\u000b\u0000\u0000?@\u0005\u000f\u0000\u0000@A\u0003\u0010\b\u0000"+
		"AB\u0005\u000e\u0000\u0000B\u000b\u0001\u0000\u0000\u0000CD\u0005\u0003"+
		"\u0000\u0000DE\u0003\u0010\b\u0000EF\u0005\u0005\u0000\u0000FI\u0003\u0002"+
		"\u0001\u0000GH\u0005\u0004\u0000\u0000HJ\u0003\u0002\u0001\u0000IG\u0001"+
		"\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000JK\u0001\u0000\u0000\u0000"+
		"KL\u0005\u0006\u0000\u0000L\r\u0001\u0000\u0000\u0000MN\u0005\u0007\u0000"+
		"\u0000NO\u0003\u0010\b\u0000OP\u0005\b\u0000\u0000PQ\u0003\u0002\u0001"+
		"\u0000QR\u0005\u0006\u0000\u0000R\u000f\u0001\u0000\u0000\u0000ST\u0003"+
		"\u0012\t\u0000T\u0011\u0001\u0000\u0000\u0000UV\u0006\t\uffff\uffff\u0000"+
		"VW\u0003\u0014\n\u0000W]\u0001\u0000\u0000\u0000XY\n\u0002\u0000\u0000"+
		"YZ\u0005\u0015\u0000\u0000Z\\\u0003\u0014\n\u0000[X\u0001\u0000\u0000"+
		"\u0000\\_\u0001\u0000\u0000\u0000][\u0001\u0000\u0000\u0000]^\u0001\u0000"+
		"\u0000\u0000^\u0013\u0001\u0000\u0000\u0000_]\u0001\u0000\u0000\u0000"+
		"`a\u0006\n\uffff\uffff\u0000ab\u0003\u0016\u000b\u0000bh\u0001\u0000\u0000"+
		"\u0000cd\n\u0002\u0000\u0000de\u0005\u0014\u0000\u0000eg\u0003\u0016\u000b"+
		"\u0000fc\u0001\u0000\u0000\u0000gj\u0001\u0000\u0000\u0000hf\u0001\u0000"+
		"\u0000\u0000hi\u0001\u0000\u0000\u0000i\u0015\u0001\u0000\u0000\u0000"+
		"jh\u0001\u0000\u0000\u0000kp\u0003\u0018\f\u0000lm\u0007\u0000\u0000\u0000"+
		"mo\u0003\u0018\f\u0000nl\u0001\u0000\u0000\u0000or\u0001\u0000\u0000\u0000"+
		"pn\u0001\u0000\u0000\u0000pq\u0001\u0000\u0000\u0000q\u0017\u0001\u0000"+
		"\u0000\u0000rp\u0001\u0000\u0000\u0000st\u0003\u001a\r\u0000t\u0019\u0001"+
		"\u0000\u0000\u0000uv\u0006\r\uffff\uffff\u0000vw\u0003\u001c\u000e\u0000"+
		"w}\u0001\u0000\u0000\u0000xy\n\u0002\u0000\u0000yz\u0007\u0001\u0000\u0000"+
		"z|\u0003\u001c\u000e\u0000{x\u0001\u0000\u0000\u0000|\u007f\u0001\u0000"+
		"\u0000\u0000}{\u0001\u0000\u0000\u0000}~\u0001\u0000\u0000\u0000~\u001b"+
		"\u0001\u0000\u0000\u0000\u007f}\u0001\u0000\u0000\u0000\u0080\u0081\u0006"+
		"\u000e\uffff\uffff\u0000\u0081\u0082\u0003\u001e\u000f\u0000\u0082\u0088"+
		"\u0001\u0000\u0000\u0000\u0083\u0084\n\u0002\u0000\u0000\u0084\u0085\u0007"+
		"\u0002\u0000\u0000\u0085\u0087\u0003\u001e\u000f\u0000\u0086\u0083\u0001"+
		"\u0000\u0000\u0000\u0087\u008a\u0001\u0000\u0000\u0000\u0088\u0086\u0001"+
		"\u0000\u0000\u0000\u0088\u0089\u0001\u0000\u0000\u0000\u0089\u001d\u0001"+
		"\u0000\u0000\u0000\u008a\u0088\u0001\u0000\u0000\u0000\u008b\u008c\u0005"+
		"\f\u0000\u0000\u008c\u008d\u0003\u0010\b\u0000\u008d\u008e\u0005\r\u0000"+
		"\u0000\u008e\u0096\u0001\u0000\u0000\u0000\u008f\u0090\u0005\u0011\u0000"+
		"\u0000\u0090\u0096\u0003\u001e\u000f\u0000\u0091\u0092\u0005\u0016\u0000"+
		"\u0000\u0092\u0096\u0003\u001e\u000f\u0000\u0093\u0096\u0003 \u0010\u0000"+
		"\u0094\u0096\u0005\u000b\u0000\u0000\u0095\u008b\u0001\u0000\u0000\u0000"+
		"\u0095\u008f\u0001\u0000\u0000\u0000\u0095\u0091\u0001\u0000\u0000\u0000"+
		"\u0095\u0093\u0001\u0000\u0000\u0000\u0095\u0094\u0001\u0000\u0000\u0000"+
		"\u0096\u001f\u0001\u0000\u0000\u0000\u0097\u0098\u0007\u0003\u0000\u0000"+
		"\u0098!\u0001\u0000\u0000\u0000\t(0I]hp}\u0088\u0095";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}