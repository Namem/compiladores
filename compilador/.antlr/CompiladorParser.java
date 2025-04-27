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
		INT_TIPO=9, STRING_TIPO=10, ID=11, INT=12, STRING=13, LPAREN=14, RPAREN=15, 
		SEMI=16, ASSIGN=17, PLUS=18, MINUS=19, MULT=20, DIV=21, AND=22, OR=23, 
		NOT=24, EQ=25, GT=26, LT=27, WS=28;
	public static final int
		RULE_programa = 0, RULE_comando = 1, RULE_declaracao = 2, RULE_atribuicao = 3, 
		RULE_entrada = 4, RULE_saida = 5, RULE_condicional = 6, RULE_repeticao = 7, 
		RULE_expressao = 8, RULE_tipo = 9;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "comando", "declaracao", "atribuicao", "entrada", "saida", 
			"condicional", "repeticao", "expressao", "tipo"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'leia'", "'escreva'", "'se'", "'senao'", "'entao'", "'fim'", "'enquanto'", 
			"'faca'", "'int'", "'string'", null, null, null, "'('", "')'", "';'", 
			"'='", "'+'", "'-'", "'*'", "'/'", "'&&'", "'||'", "'!'", "'=='", "'>'", 
			"'<'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LEIA", "ESCREVA", "SE", "SENAO", "ENTAO", "FIM", "ENQUANTO", "FACA", 
			"INT_TIPO", "STRING_TIPO", "ID", "INT", "STRING", "LPAREN", "RPAREN", 
			"SEMI", "ASSIGN", "PLUS", "MINUS", "MULT", "DIV", "AND", "OR", "NOT", 
			"EQ", "GT", "LT", "WS"
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
		public TerminalNode EOF() { return getToken(CompiladorParser.EOF, 0); }
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(23);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3726L) != 0)) {
				{
				{
				setState(20);
				comando();
				}
				}
				setState(25);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(26);
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
	public static class ComandoContext extends ParserRuleContext {
		public DeclaracaoContext declaracao() {
			return getRuleContext(DeclaracaoContext.class,0);
		}
		public AtribuicaoContext atribuicao() {
			return getRuleContext(AtribuicaoContext.class,0);
		}
		public EntradaContext entrada() {
			return getRuleContext(EntradaContext.class,0);
		}
		public SaidaContext saida() {
			return getRuleContext(SaidaContext.class,0);
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
		enterRule(_localctx, 2, RULE_comando);
		try {
			setState(34);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_TIPO:
			case STRING_TIPO:
				enterOuterAlt(_localctx, 1);
				{
				setState(28);
				declaracao();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(29);
				atribuicao();
				}
				break;
			case LEIA:
				enterOuterAlt(_localctx, 3);
				{
				setState(30);
				entrada();
				}
				break;
			case ESCREVA:
				enterOuterAlt(_localctx, 4);
				{
				setState(31);
				saida();
				}
				break;
			case SE:
				enterOuterAlt(_localctx, 5);
				{
				setState(32);
				condicional();
				}
				break;
			case ENQUANTO:
				enterOuterAlt(_localctx, 6);
				{
				setState(33);
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
	public static class DeclaracaoContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(CompiladorParser.ID, 0); }
		public TerminalNode SEMI() { return getToken(CompiladorParser.SEMI, 0); }
		public DeclaracaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracao; }
	}

	public final DeclaracaoContext declaracao() throws RecognitionException {
		DeclaracaoContext _localctx = new DeclaracaoContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declaracao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			tipo();
			setState(37);
			match(ID);
			setState(38);
			match(SEMI);
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
		public TerminalNode ID() { return getToken(CompiladorParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(CompiladorParser.ASSIGN, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(CompiladorParser.SEMI, 0); }
		public AtribuicaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atribuicao; }
	}

	public final AtribuicaoContext atribuicao() throws RecognitionException {
		AtribuicaoContext _localctx = new AtribuicaoContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_atribuicao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			match(ID);
			setState(41);
			match(ASSIGN);
			setState(42);
			expressao(0);
			setState(43);
			match(SEMI);
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
	public static class EntradaContext extends ParserRuleContext {
		public TerminalNode LEIA() { return getToken(CompiladorParser.LEIA, 0); }
		public TerminalNode LPAREN() { return getToken(CompiladorParser.LPAREN, 0); }
		public TerminalNode ID() { return getToken(CompiladorParser.ID, 0); }
		public TerminalNode RPAREN() { return getToken(CompiladorParser.RPAREN, 0); }
		public TerminalNode SEMI() { return getToken(CompiladorParser.SEMI, 0); }
		public EntradaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entrada; }
	}

	public final EntradaContext entrada() throws RecognitionException {
		EntradaContext _localctx = new EntradaContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_entrada);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			match(LEIA);
			setState(46);
			match(LPAREN);
			setState(47);
			match(ID);
			setState(48);
			match(RPAREN);
			setState(49);
			match(SEMI);
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
	public static class SaidaContext extends ParserRuleContext {
		public TerminalNode ESCREVA() { return getToken(CompiladorParser.ESCREVA, 0); }
		public TerminalNode LPAREN() { return getToken(CompiladorParser.LPAREN, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(CompiladorParser.RPAREN, 0); }
		public TerminalNode SEMI() { return getToken(CompiladorParser.SEMI, 0); }
		public SaidaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_saida; }
	}

	public final SaidaContext saida() throws RecognitionException {
		SaidaContext _localctx = new SaidaContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_saida);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			match(ESCREVA);
			setState(52);
			match(LPAREN);
			setState(53);
			expressao(0);
			setState(54);
			match(RPAREN);
			setState(55);
			match(SEMI);
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
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public TerminalNode ENTAO() { return getToken(CompiladorParser.ENTAO, 0); }
		public TerminalNode FIM() { return getToken(CompiladorParser.FIM, 0); }
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
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
			setState(57);
			match(SE);
			setState(58);
			expressao(0);
			setState(59);
			match(ENTAO);
			setState(63);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3726L) != 0)) {
				{
				{
				setState(60);
				comando();
				}
				}
				setState(65);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(73);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SENAO) {
				{
				setState(66);
				match(SENAO);
				setState(70);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3726L) != 0)) {
					{
					{
					setState(67);
					comando();
					}
					}
					setState(72);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
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
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public TerminalNode FACA() { return getToken(CompiladorParser.FACA, 0); }
		public TerminalNode FIM() { return getToken(CompiladorParser.FIM, 0); }
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public RepeticaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_repeticao; }
	}

	public final RepeticaoContext repeticao() throws RecognitionException {
		RepeticaoContext _localctx = new RepeticaoContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_repeticao);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			match(ENQUANTO);
			setState(78);
			expressao(0);
			setState(79);
			match(FACA);
			setState(83);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3726L) != 0)) {
				{
				{
				setState(80);
				comando();
				}
				}
				setState(85);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(86);
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
	public static class ExpressaoContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(CompiladorParser.NOT, 0); }
		public List<ExpressaoContext> expressao() {
			return getRuleContexts(ExpressaoContext.class);
		}
		public ExpressaoContext expressao(int i) {
			return getRuleContext(ExpressaoContext.class,i);
		}
		public TerminalNode LPAREN() { return getToken(CompiladorParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(CompiladorParser.RPAREN, 0); }
		public TerminalNode INT() { return getToken(CompiladorParser.INT, 0); }
		public TerminalNode STRING() { return getToken(CompiladorParser.STRING, 0); }
		public TerminalNode ID() { return getToken(CompiladorParser.ID, 0); }
		public TerminalNode MULT() { return getToken(CompiladorParser.MULT, 0); }
		public TerminalNode DIV() { return getToken(CompiladorParser.DIV, 0); }
		public TerminalNode PLUS() { return getToken(CompiladorParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(CompiladorParser.MINUS, 0); }
		public TerminalNode AND() { return getToken(CompiladorParser.AND, 0); }
		public TerminalNode OR() { return getToken(CompiladorParser.OR, 0); }
		public TerminalNode EQ() { return getToken(CompiladorParser.EQ, 0); }
		public ExpressaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressao; }
	}

	public final ExpressaoContext expressao() throws RecognitionException {
		return expressao(0);
	}

	private ExpressaoContext expressao(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressaoContext _localctx = new ExpressaoContext(_ctx, _parentState);
		ExpressaoContext _prevctx = _localctx;
		int _startState = 16;
		enterRecursionRule(_localctx, 16, RULE_expressao, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				{
				setState(89);
				match(NOT);
				setState(90);
				expressao(6);
				}
				break;
			case LPAREN:
				{
				setState(91);
				match(LPAREN);
				setState(92);
				expressao(0);
				setState(93);
				match(RPAREN);
				}
				break;
			case INT:
				{
				setState(95);
				match(INT);
				}
				break;
			case STRING:
				{
				setState(96);
				match(STRING);
				}
				break;
			case ID:
				{
				setState(97);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(123);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(121);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressaoContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expressao);
						setState(100);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(101);
						match(MULT);
						setState(102);
						expressao(13);
						}
						break;
					case 2:
						{
						_localctx = new ExpressaoContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expressao);
						setState(103);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(104);
						match(DIV);
						setState(105);
						expressao(12);
						}
						break;
					case 3:
						{
						_localctx = new ExpressaoContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expressao);
						setState(106);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(107);
						match(PLUS);
						setState(108);
						expressao(11);
						}
						break;
					case 4:
						{
						_localctx = new ExpressaoContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expressao);
						setState(109);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(110);
						match(MINUS);
						setState(111);
						expressao(10);
						}
						break;
					case 5:
						{
						_localctx = new ExpressaoContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expressao);
						setState(112);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(113);
						match(AND);
						setState(114);
						expressao(9);
						}
						break;
					case 6:
						{
						_localctx = new ExpressaoContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expressao);
						setState(115);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(116);
						match(OR);
						setState(117);
						expressao(8);
						}
						break;
					case 7:
						{
						_localctx = new ExpressaoContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expressao);
						setState(118);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(119);
						match(EQ);
						setState(120);
						expressao(6);
						}
						break;
					}
					} 
				}
				setState(125);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
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
	public static class TipoContext extends ParserRuleContext {
		public TerminalNode INT_TIPO() { return getToken(CompiladorParser.INT_TIPO, 0); }
		public TerminalNode STRING_TIPO() { return getToken(CompiladorParser.STRING_TIPO, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			_la = _input.LA(1);
			if ( !(_la==INT_TIPO || _la==STRING_TIPO) ) {
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
		case 8:
			return expressao_sempred((ExpressaoContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expressao_sempred(ExpressaoContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 12);
		case 1:
			return precpred(_ctx, 11);
		case 2:
			return precpred(_ctx, 10);
		case 3:
			return precpred(_ctx, 9);
		case 4:
			return precpred(_ctx, 8);
		case 5:
			return precpred(_ctx, 7);
		case 6:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001c\u0081\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0001\u0000\u0005\u0000\u0016\b\u0000"+
		"\n\u0000\f\u0000\u0019\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001#\b"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0005\u0006>\b\u0006\n\u0006\f\u0006A\t\u0006\u0001"+
		"\u0006\u0001\u0006\u0005\u0006E\b\u0006\n\u0006\f\u0006H\t\u0006\u0003"+
		"\u0006J\b\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0005\u0007R\b\u0007\n\u0007\f\u0007U\t\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0003\bc\b\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0005"+
		"\bz\b\b\n\b\f\b}\t\b\u0001\t\u0001\t\u0001\t\u0000\u0001\u0010\n\u0000"+
		"\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0000\u0001\u0001\u0000\t\n"+
		"\u008b\u0000\u0017\u0001\u0000\u0000\u0000\u0002\"\u0001\u0000\u0000\u0000"+
		"\u0004$\u0001\u0000\u0000\u0000\u0006(\u0001\u0000\u0000\u0000\b-\u0001"+
		"\u0000\u0000\u0000\n3\u0001\u0000\u0000\u0000\f9\u0001\u0000\u0000\u0000"+
		"\u000eM\u0001\u0000\u0000\u0000\u0010b\u0001\u0000\u0000\u0000\u0012~"+
		"\u0001\u0000\u0000\u0000\u0014\u0016\u0003\u0002\u0001\u0000\u0015\u0014"+
		"\u0001\u0000\u0000\u0000\u0016\u0019\u0001\u0000\u0000\u0000\u0017\u0015"+
		"\u0001\u0000\u0000\u0000\u0017\u0018\u0001\u0000\u0000\u0000\u0018\u001a"+
		"\u0001\u0000\u0000\u0000\u0019\u0017\u0001\u0000\u0000\u0000\u001a\u001b"+
		"\u0005\u0000\u0000\u0001\u001b\u0001\u0001\u0000\u0000\u0000\u001c#\u0003"+
		"\u0004\u0002\u0000\u001d#\u0003\u0006\u0003\u0000\u001e#\u0003\b\u0004"+
		"\u0000\u001f#\u0003\n\u0005\u0000 #\u0003\f\u0006\u0000!#\u0003\u000e"+
		"\u0007\u0000\"\u001c\u0001\u0000\u0000\u0000\"\u001d\u0001\u0000\u0000"+
		"\u0000\"\u001e\u0001\u0000\u0000\u0000\"\u001f\u0001\u0000\u0000\u0000"+
		"\" \u0001\u0000\u0000\u0000\"!\u0001\u0000\u0000\u0000#\u0003\u0001\u0000"+
		"\u0000\u0000$%\u0003\u0012\t\u0000%&\u0005\u000b\u0000\u0000&\'\u0005"+
		"\u0010\u0000\u0000\'\u0005\u0001\u0000\u0000\u0000()\u0005\u000b\u0000"+
		"\u0000)*\u0005\u0011\u0000\u0000*+\u0003\u0010\b\u0000+,\u0005\u0010\u0000"+
		"\u0000,\u0007\u0001\u0000\u0000\u0000-.\u0005\u0001\u0000\u0000./\u0005"+
		"\u000e\u0000\u0000/0\u0005\u000b\u0000\u000001\u0005\u000f\u0000\u0000"+
		"12\u0005\u0010\u0000\u00002\t\u0001\u0000\u0000\u000034\u0005\u0002\u0000"+
		"\u000045\u0005\u000e\u0000\u000056\u0003\u0010\b\u000067\u0005\u000f\u0000"+
		"\u000078\u0005\u0010\u0000\u00008\u000b\u0001\u0000\u0000\u00009:\u0005"+
		"\u0003\u0000\u0000:;\u0003\u0010\b\u0000;?\u0005\u0005\u0000\u0000<>\u0003"+
		"\u0002\u0001\u0000=<\u0001\u0000\u0000\u0000>A\u0001\u0000\u0000\u0000"+
		"?=\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000\u0000@I\u0001\u0000\u0000"+
		"\u0000A?\u0001\u0000\u0000\u0000BF\u0005\u0004\u0000\u0000CE\u0003\u0002"+
		"\u0001\u0000DC\u0001\u0000\u0000\u0000EH\u0001\u0000\u0000\u0000FD\u0001"+
		"\u0000\u0000\u0000FG\u0001\u0000\u0000\u0000GJ\u0001\u0000\u0000\u0000"+
		"HF\u0001\u0000\u0000\u0000IB\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000"+
		"\u0000JK\u0001\u0000\u0000\u0000KL\u0005\u0006\u0000\u0000L\r\u0001\u0000"+
		"\u0000\u0000MN\u0005\u0007\u0000\u0000NO\u0003\u0010\b\u0000OS\u0005\b"+
		"\u0000\u0000PR\u0003\u0002\u0001\u0000QP\u0001\u0000\u0000\u0000RU\u0001"+
		"\u0000\u0000\u0000SQ\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000"+
		"TV\u0001\u0000\u0000\u0000US\u0001\u0000\u0000\u0000VW\u0005\u0006\u0000"+
		"\u0000W\u000f\u0001\u0000\u0000\u0000XY\u0006\b\uffff\uffff\u0000YZ\u0005"+
		"\u0018\u0000\u0000Zc\u0003\u0010\b\u0006[\\\u0005\u000e\u0000\u0000\\"+
		"]\u0003\u0010\b\u0000]^\u0005\u000f\u0000\u0000^c\u0001\u0000\u0000\u0000"+
		"_c\u0005\f\u0000\u0000`c\u0005\r\u0000\u0000ac\u0005\u000b\u0000\u0000"+
		"bX\u0001\u0000\u0000\u0000b[\u0001\u0000\u0000\u0000b_\u0001\u0000\u0000"+
		"\u0000b`\u0001\u0000\u0000\u0000ba\u0001\u0000\u0000\u0000c{\u0001\u0000"+
		"\u0000\u0000de\n\f\u0000\u0000ef\u0005\u0014\u0000\u0000fz\u0003\u0010"+
		"\b\rgh\n\u000b\u0000\u0000hi\u0005\u0015\u0000\u0000iz\u0003\u0010\b\f"+
		"jk\n\n\u0000\u0000kl\u0005\u0012\u0000\u0000lz\u0003\u0010\b\u000bmn\n"+
		"\t\u0000\u0000no\u0005\u0013\u0000\u0000oz\u0003\u0010\b\npq\n\b\u0000"+
		"\u0000qr\u0005\u0016\u0000\u0000rz\u0003\u0010\b\tst\n\u0007\u0000\u0000"+
		"tu\u0005\u0017\u0000\u0000uz\u0003\u0010\b\bvw\n\u0005\u0000\u0000wx\u0005"+
		"\u0019\u0000\u0000xz\u0003\u0010\b\u0006yd\u0001\u0000\u0000\u0000yg\u0001"+
		"\u0000\u0000\u0000yj\u0001\u0000\u0000\u0000ym\u0001\u0000\u0000\u0000"+
		"yp\u0001\u0000\u0000\u0000ys\u0001\u0000\u0000\u0000yv\u0001\u0000\u0000"+
		"\u0000z}\u0001\u0000\u0000\u0000{y\u0001\u0000\u0000\u0000{|\u0001\u0000"+
		"\u0000\u0000|\u0011\u0001\u0000\u0000\u0000}{\u0001\u0000\u0000\u0000"+
		"~\u007f\u0007\u0000\u0000\u0000\u007f\u0013\u0001\u0000\u0000\u0000\t"+
		"\u0017\"?FISby{";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}