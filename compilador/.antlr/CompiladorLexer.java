// Generated from /home/namem/Área de trabalho/Compiladores/compilador/Compilador.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class CompiladorLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LEIA=1, ESCREVA=2, SE=3, SENAO=4, ENTAO=5, FIM=6, ENQUANTO=7, FACA=8, 
		INT_TIPO=9, STRING_TIPO=10, ID=11, INT=12, STRING=13, LPAREN=14, RPAREN=15, 
		SEMI=16, ASSIGN=17, PLUS=18, MINUS=19, MULT=20, DIV=21, AND=22, OR=23, 
		NOT=24, EQ=25, GT=26, LT=27, WS=28;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"LEIA", "ESCREVA", "SE", "SENAO", "ENTAO", "FIM", "ENQUANTO", "FACA", 
			"INT_TIPO", "STRING_TIPO", "ID", "INT", "STRING", "LPAREN", "RPAREN", 
			"SEMI", "ASSIGN", "PLUS", "MINUS", "MULT", "DIV", "AND", "OR", "NOT", 
			"EQ", "GT", "LT", "WS"
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


	public CompiladorLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Compilador.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u001c\u00ad\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0002\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a"+
		"\u0002\u001b\u0007\u001b\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\n\u0001\n\u0005\nu\b\n\n\n\f\nx\t\n\u0001\u000b"+
		"\u0004\u000b{\b\u000b\u000b\u000b\f\u000b|\u0001\f\u0001\f\u0005\f\u0081"+
		"\b\f\n\f\f\f\u0084\t\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001"+
		"\u000e\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0011\u0001"+
		"\u0011\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0014\u0001"+
		"\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0019\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001b\u0004\u001b\u00a8"+
		"\b\u001b\u000b\u001b\f\u001b\u00a9\u0001\u001b\u0001\u001b\u0001\u0082"+
		"\u0000\u001c\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b"+
		"\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b"+
		"\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016"+
		"-\u0017/\u00181\u00193\u001a5\u001b7\u001c\u0001\u0000\u0004\u0003\u0000"+
		"AZ__az\u0004\u000009AZ__az\u0001\u000009\u0003\u0000\t\n\r\r  \u00b0\u0000"+
		"\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000"+
		"\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000"+
		"\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r"+
		"\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011"+
		"\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015"+
		"\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019"+
		"\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d"+
		"\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001"+
		"\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000"+
		"\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000"+
		"\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000\u0000\u0000/"+
		"\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u00003\u0001\u0000"+
		"\u0000\u0000\u00005\u0001\u0000\u0000\u0000\u00007\u0001\u0000\u0000\u0000"+
		"\u00019\u0001\u0000\u0000\u0000\u0003>\u0001\u0000\u0000\u0000\u0005F"+
		"\u0001\u0000\u0000\u0000\u0007I\u0001\u0000\u0000\u0000\tO\u0001\u0000"+
		"\u0000\u0000\u000bU\u0001\u0000\u0000\u0000\rY\u0001\u0000\u0000\u0000"+
		"\u000fb\u0001\u0000\u0000\u0000\u0011g\u0001\u0000\u0000\u0000\u0013k"+
		"\u0001\u0000\u0000\u0000\u0015r\u0001\u0000\u0000\u0000\u0017z\u0001\u0000"+
		"\u0000\u0000\u0019~\u0001\u0000\u0000\u0000\u001b\u0087\u0001\u0000\u0000"+
		"\u0000\u001d\u0089\u0001\u0000\u0000\u0000\u001f\u008b\u0001\u0000\u0000"+
		"\u0000!\u008d\u0001\u0000\u0000\u0000#\u008f\u0001\u0000\u0000\u0000%"+
		"\u0091\u0001\u0000\u0000\u0000\'\u0093\u0001\u0000\u0000\u0000)\u0095"+
		"\u0001\u0000\u0000\u0000+\u0097\u0001\u0000\u0000\u0000-\u009a\u0001\u0000"+
		"\u0000\u0000/\u009d\u0001\u0000\u0000\u00001\u009f\u0001\u0000\u0000\u0000"+
		"3\u00a2\u0001\u0000\u0000\u00005\u00a4\u0001\u0000\u0000\u00007\u00a7"+
		"\u0001\u0000\u0000\u00009:\u0005l\u0000\u0000:;\u0005e\u0000\u0000;<\u0005"+
		"i\u0000\u0000<=\u0005a\u0000\u0000=\u0002\u0001\u0000\u0000\u0000>?\u0005"+
		"e\u0000\u0000?@\u0005s\u0000\u0000@A\u0005c\u0000\u0000AB\u0005r\u0000"+
		"\u0000BC\u0005e\u0000\u0000CD\u0005v\u0000\u0000DE\u0005a\u0000\u0000"+
		"E\u0004\u0001\u0000\u0000\u0000FG\u0005s\u0000\u0000GH\u0005e\u0000\u0000"+
		"H\u0006\u0001\u0000\u0000\u0000IJ\u0005s\u0000\u0000JK\u0005e\u0000\u0000"+
		"KL\u0005n\u0000\u0000LM\u0005a\u0000\u0000MN\u0005o\u0000\u0000N\b\u0001"+
		"\u0000\u0000\u0000OP\u0005e\u0000\u0000PQ\u0005n\u0000\u0000QR\u0005t"+
		"\u0000\u0000RS\u0005a\u0000\u0000ST\u0005o\u0000\u0000T\n\u0001\u0000"+
		"\u0000\u0000UV\u0005f\u0000\u0000VW\u0005i\u0000\u0000WX\u0005m\u0000"+
		"\u0000X\f\u0001\u0000\u0000\u0000YZ\u0005e\u0000\u0000Z[\u0005n\u0000"+
		"\u0000[\\\u0005q\u0000\u0000\\]\u0005u\u0000\u0000]^\u0005a\u0000\u0000"+
		"^_\u0005n\u0000\u0000_`\u0005t\u0000\u0000`a\u0005o\u0000\u0000a\u000e"+
		"\u0001\u0000\u0000\u0000bc\u0005f\u0000\u0000cd\u0005a\u0000\u0000de\u0005"+
		"c\u0000\u0000ef\u0005a\u0000\u0000f\u0010\u0001\u0000\u0000\u0000gh\u0005"+
		"i\u0000\u0000hi\u0005n\u0000\u0000ij\u0005t\u0000\u0000j\u0012\u0001\u0000"+
		"\u0000\u0000kl\u0005s\u0000\u0000lm\u0005t\u0000\u0000mn\u0005r\u0000"+
		"\u0000no\u0005i\u0000\u0000op\u0005n\u0000\u0000pq\u0005g\u0000\u0000"+
		"q\u0014\u0001\u0000\u0000\u0000rv\u0007\u0000\u0000\u0000su\u0007\u0001"+
		"\u0000\u0000ts\u0001\u0000\u0000\u0000ux\u0001\u0000\u0000\u0000vt\u0001"+
		"\u0000\u0000\u0000vw\u0001\u0000\u0000\u0000w\u0016\u0001\u0000\u0000"+
		"\u0000xv\u0001\u0000\u0000\u0000y{\u0007\u0002\u0000\u0000zy\u0001\u0000"+
		"\u0000\u0000{|\u0001\u0000\u0000\u0000|z\u0001\u0000\u0000\u0000|}\u0001"+
		"\u0000\u0000\u0000}\u0018\u0001\u0000\u0000\u0000~\u0082\u0005\"\u0000"+
		"\u0000\u007f\u0081\t\u0000\u0000\u0000\u0080\u007f\u0001\u0000\u0000\u0000"+
		"\u0081\u0084\u0001\u0000\u0000\u0000\u0082\u0083\u0001\u0000\u0000\u0000"+
		"\u0082\u0080\u0001\u0000\u0000\u0000\u0083\u0085\u0001\u0000\u0000\u0000"+
		"\u0084\u0082\u0001\u0000\u0000\u0000\u0085\u0086\u0005\"\u0000\u0000\u0086"+
		"\u001a\u0001\u0000\u0000\u0000\u0087\u0088\u0005(\u0000\u0000\u0088\u001c"+
		"\u0001\u0000\u0000\u0000\u0089\u008a\u0005)\u0000\u0000\u008a\u001e\u0001"+
		"\u0000\u0000\u0000\u008b\u008c\u0005;\u0000\u0000\u008c \u0001\u0000\u0000"+
		"\u0000\u008d\u008e\u0005=\u0000\u0000\u008e\"\u0001\u0000\u0000\u0000"+
		"\u008f\u0090\u0005+\u0000\u0000\u0090$\u0001\u0000\u0000\u0000\u0091\u0092"+
		"\u0005-\u0000\u0000\u0092&\u0001\u0000\u0000\u0000\u0093\u0094\u0005*"+
		"\u0000\u0000\u0094(\u0001\u0000\u0000\u0000\u0095\u0096\u0005/\u0000\u0000"+
		"\u0096*\u0001\u0000\u0000\u0000\u0097\u0098\u0005&\u0000\u0000\u0098\u0099"+
		"\u0005&\u0000\u0000\u0099,\u0001\u0000\u0000\u0000\u009a\u009b\u0005|"+
		"\u0000\u0000\u009b\u009c\u0005|\u0000\u0000\u009c.\u0001\u0000\u0000\u0000"+
		"\u009d\u009e\u0005!\u0000\u0000\u009e0\u0001\u0000\u0000\u0000\u009f\u00a0"+
		"\u0005=\u0000\u0000\u00a0\u00a1\u0005=\u0000\u0000\u00a12\u0001\u0000"+
		"\u0000\u0000\u00a2\u00a3\u0005>\u0000\u0000\u00a34\u0001\u0000\u0000\u0000"+
		"\u00a4\u00a5\u0005<\u0000\u0000\u00a56\u0001\u0000\u0000\u0000\u00a6\u00a8"+
		"\u0007\u0003\u0000\u0000\u00a7\u00a6\u0001\u0000\u0000\u0000\u00a8\u00a9"+
		"\u0001\u0000\u0000\u0000\u00a9\u00a7\u0001\u0000\u0000\u0000\u00a9\u00aa"+
		"\u0001\u0000\u0000\u0000\u00aa\u00ab\u0001\u0000\u0000\u0000\u00ab\u00ac"+
		"\u0006\u001b\u0000\u0000\u00ac8\u0001\u0000\u0000\u0000\u0005\u0000v|"+
		"\u0082\u00a9\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}