// Generated from E:/Studia/AGH/Semestr 4/ISI/TKIK/tkik/grammar/CircuitryLexer.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class CircuitryLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SUBCIRCUIT=1, END=2, LET=3, OP=4, TRANSIENT=5, PULSE=6, ID=7, NUMBER=8, 
		UNIT=9, EQ=10, COLON=11, COMMA=12, LPAREN=13, RPAREN=14, LBRACE=15, RBRACE=16, 
		RARROW=17, NEWLINE=18, WS=19, COMMENT=20;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"SUBCIRCUIT", "END", "LET", "OP", "TRANSIENT", "PULSE", "ID", "NUMBER", 
			"UNIT", "EQ", "COLON", "COMMA", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
			"RARROW", "NEWLINE", "WS", "COMMENT", "DIGIT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'subcircuit'", "'end'", "'let'", "'op'", "'transient'", "'pulse'", 
			null, null, null, "'='", "':'", "','", "'('", "')'", "'{'", "'}'", "'->'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SUBCIRCUIT", "END", "LET", "OP", "TRANSIENT", "PULSE", "ID", "NUMBER", 
			"UNIT", "EQ", "COLON", "COMMA", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
			"RARROW", "NEWLINE", "WS", "COMMENT"
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


	public CircuitryLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "CircuitryLexer.g4"; }

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
		"\u0004\u0000\u0014\u0092\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0005\u0006T\b\u0006"+
		"\n\u0006\f\u0006W\t\u0006\u0001\u0007\u0004\u0007Z\b\u0007\u000b\u0007"+
		"\f\u0007[\u0001\u0007\u0001\u0007\u0004\u0007`\b\u0007\u000b\u0007\f\u0007"+
		"a\u0003\u0007d\b\u0007\u0001\u0007\u0003\u0007g\b\u0007\u0001\b\u0001"+
		"\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001"+
		"\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0003\u0011}\b\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0012\u0004\u0012\u0082\b\u0012\u000b\u0012\f"+
		"\u0012\u0083\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0005\u0013"+
		"\u008a\b\u0013\n\u0013\f\u0013\u008d\t\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0014\u0001\u0014\u0000\u0000\u0015\u0001\u0001\u0003\u0002\u0005\u0003"+
		"\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015"+
		"\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012"+
		"%\u0013\'\u0014)\u0000\u0001\u0000\u0006\u0003\u0000AZ__az\u0004\u0000"+
		"09AZ__az\n\u0000FGKKMNPPfgkkmnppuu\u03bc\u03bc\u0002\u0000\t\t  \u0002"+
		"\u0000\n\n\r\r\u0001\u000009\u0098\u0000\u0001\u0001\u0000\u0000\u0000"+
		"\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000"+
		"\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000"+
		"\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f"+
		"\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013"+
		"\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017"+
		"\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b"+
		"\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f"+
		"\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000"+
		"\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000"+
		"\u0000\u0001+\u0001\u0000\u0000\u0000\u00036\u0001\u0000\u0000\u0000\u0005"+
		":\u0001\u0000\u0000\u0000\u0007>\u0001\u0000\u0000\u0000\tA\u0001\u0000"+
		"\u0000\u0000\u000bK\u0001\u0000\u0000\u0000\rQ\u0001\u0000\u0000\u0000"+
		"\u000fY\u0001\u0000\u0000\u0000\u0011h\u0001\u0000\u0000\u0000\u0013j"+
		"\u0001\u0000\u0000\u0000\u0015l\u0001\u0000\u0000\u0000\u0017n\u0001\u0000"+
		"\u0000\u0000\u0019p\u0001\u0000\u0000\u0000\u001br\u0001\u0000\u0000\u0000"+
		"\u001dt\u0001\u0000\u0000\u0000\u001fv\u0001\u0000\u0000\u0000!x\u0001"+
		"\u0000\u0000\u0000#|\u0001\u0000\u0000\u0000%\u0081\u0001\u0000\u0000"+
		"\u0000\'\u0087\u0001\u0000\u0000\u0000)\u0090\u0001\u0000\u0000\u0000"+
		"+,\u0005s\u0000\u0000,-\u0005u\u0000\u0000-.\u0005b\u0000\u0000./\u0005"+
		"c\u0000\u0000/0\u0005i\u0000\u000001\u0005r\u0000\u000012\u0005c\u0000"+
		"\u000023\u0005u\u0000\u000034\u0005i\u0000\u000045\u0005t\u0000\u0000"+
		"5\u0002\u0001\u0000\u0000\u000067\u0005e\u0000\u000078\u0005n\u0000\u0000"+
		"89\u0005d\u0000\u00009\u0004\u0001\u0000\u0000\u0000:;\u0005l\u0000\u0000"+
		";<\u0005e\u0000\u0000<=\u0005t\u0000\u0000=\u0006\u0001\u0000\u0000\u0000"+
		">?\u0005o\u0000\u0000?@\u0005p\u0000\u0000@\b\u0001\u0000\u0000\u0000"+
		"AB\u0005t\u0000\u0000BC\u0005r\u0000\u0000CD\u0005a\u0000\u0000DE\u0005"+
		"n\u0000\u0000EF\u0005s\u0000\u0000FG\u0005i\u0000\u0000GH\u0005e\u0000"+
		"\u0000HI\u0005n\u0000\u0000IJ\u0005t\u0000\u0000J\n\u0001\u0000\u0000"+
		"\u0000KL\u0005p\u0000\u0000LM\u0005u\u0000\u0000MN\u0005l\u0000\u0000"+
		"NO\u0005s\u0000\u0000OP\u0005e\u0000\u0000P\f\u0001\u0000\u0000\u0000"+
		"QU\u0007\u0000\u0000\u0000RT\u0007\u0001\u0000\u0000SR\u0001\u0000\u0000"+
		"\u0000TW\u0001\u0000\u0000\u0000US\u0001\u0000\u0000\u0000UV\u0001\u0000"+
		"\u0000\u0000V\u000e\u0001\u0000\u0000\u0000WU\u0001\u0000\u0000\u0000"+
		"XZ\u0003)\u0014\u0000YX\u0001\u0000\u0000\u0000Z[\u0001\u0000\u0000\u0000"+
		"[Y\u0001\u0000\u0000\u0000[\\\u0001\u0000\u0000\u0000\\c\u0001\u0000\u0000"+
		"\u0000]_\u0005.\u0000\u0000^`\u0003)\u0014\u0000_^\u0001\u0000\u0000\u0000"+
		"`a\u0001\u0000\u0000\u0000a_\u0001\u0000\u0000\u0000ab\u0001\u0000\u0000"+
		"\u0000bd\u0001\u0000\u0000\u0000c]\u0001\u0000\u0000\u0000cd\u0001\u0000"+
		"\u0000\u0000df\u0001\u0000\u0000\u0000eg\u0003\u0011\b\u0000fe\u0001\u0000"+
		"\u0000\u0000fg\u0001\u0000\u0000\u0000g\u0010\u0001\u0000\u0000\u0000"+
		"hi\u0007\u0002\u0000\u0000i\u0012\u0001\u0000\u0000\u0000jk\u0005=\u0000"+
		"\u0000k\u0014\u0001\u0000\u0000\u0000lm\u0005:\u0000\u0000m\u0016\u0001"+
		"\u0000\u0000\u0000no\u0005,\u0000\u0000o\u0018\u0001\u0000\u0000\u0000"+
		"pq\u0005(\u0000\u0000q\u001a\u0001\u0000\u0000\u0000rs\u0005)\u0000\u0000"+
		"s\u001c\u0001\u0000\u0000\u0000tu\u0005{\u0000\u0000u\u001e\u0001\u0000"+
		"\u0000\u0000vw\u0005}\u0000\u0000w \u0001\u0000\u0000\u0000xy\u0005-\u0000"+
		"\u0000yz\u0005>\u0000\u0000z\"\u0001\u0000\u0000\u0000{}\u0005\r\u0000"+
		"\u0000|{\u0001\u0000\u0000\u0000|}\u0001\u0000\u0000\u0000}~\u0001\u0000"+
		"\u0000\u0000~\u007f\u0005\n\u0000\u0000\u007f$\u0001\u0000\u0000\u0000"+
		"\u0080\u0082\u0007\u0003\u0000\u0000\u0081\u0080\u0001\u0000\u0000\u0000"+
		"\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u0081\u0001\u0000\u0000\u0000"+
		"\u0083\u0084\u0001\u0000\u0000\u0000\u0084\u0085\u0001\u0000\u0000\u0000"+
		"\u0085\u0086\u0006\u0012\u0000\u0000\u0086&\u0001\u0000\u0000\u0000\u0087"+
		"\u008b\u0005#\u0000\u0000\u0088\u008a\b\u0004\u0000\u0000\u0089\u0088"+
		"\u0001\u0000\u0000\u0000\u008a\u008d\u0001\u0000\u0000\u0000\u008b\u0089"+
		"\u0001\u0000\u0000\u0000\u008b\u008c\u0001\u0000\u0000\u0000\u008c\u008e"+
		"\u0001\u0000\u0000\u0000\u008d\u008b\u0001\u0000\u0000\u0000\u008e\u008f"+
		"\u0006\u0013\u0000\u0000\u008f(\u0001\u0000\u0000\u0000\u0090\u0091\u0007"+
		"\u0005\u0000\u0000\u0091*\u0001\u0000\u0000\u0000\t\u0000U[acf|\u0083"+
		"\u008b\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}