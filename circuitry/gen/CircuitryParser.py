# Generated from ../grammar/CircuitryParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,67,641,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,1,0,5,0,110,8,0,10,0,12,0,113,9,0,1,0,5,0,116,8,0,10,0,
        12,0,119,9,0,1,0,5,0,122,8,0,10,0,12,0,125,9,0,1,0,5,0,128,8,0,10,
        0,12,0,131,9,0,1,0,5,0,134,8,0,10,0,12,0,137,9,0,1,0,1,0,1,1,1,1,
        1,1,1,1,5,1,145,8,1,10,1,12,1,148,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,165,8,2,1,3,1,3,1,3,1,3,5,
        3,171,8,3,10,3,12,3,174,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,5,5,186,8,5,10,5,12,5,189,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,5,9,210,8,9,10,9,12,
        9,213,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,4,10,222,8,10,11,10,
        12,10,223,3,10,226,8,10,1,11,1,11,1,12,1,12,3,12,232,8,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,3,13,243,8,13,1,13,1,13,1,
        13,1,13,1,14,1,14,1,14,5,14,252,8,14,10,14,12,14,255,9,14,1,15,1,
        15,1,15,3,15,260,8,15,1,16,1,16,1,16,1,16,1,16,1,16,3,16,268,8,16,
        1,17,1,17,3,17,272,8,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,
        1,18,3,18,283,8,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,5,19,292,8,
        19,10,19,12,19,295,9,19,1,20,1,20,1,20,3,20,300,8,20,1,21,1,21,1,
        21,1,21,1,21,1,21,3,21,308,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,3,22,319,8,22,1,23,1,23,1,24,1,24,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,338,8,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,5,25,361,8,25,10,25,12,25,
        364,9,25,1,26,1,26,1,26,3,26,369,8,26,1,26,1,26,1,27,1,27,1,27,5,
        27,376,8,27,10,27,12,27,379,9,27,1,27,1,27,1,27,5,27,384,8,27,10,
        27,12,27,387,9,27,1,27,1,27,1,27,5,27,392,8,27,10,27,12,27,395,9,
        27,1,27,1,27,1,27,5,27,400,8,27,10,27,12,27,403,9,27,3,27,405,8,
        27,1,28,1,28,1,28,1,28,1,29,1,29,1,30,1,30,1,30,1,30,1,30,5,30,418,
        8,30,10,30,12,30,421,9,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,440,8,31,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,5,32,449,8,32,10,32,12,32,452,9,32,
        1,32,3,32,455,8,32,1,32,1,32,1,32,1,32,5,32,461,8,32,10,32,12,32,
        464,9,32,1,32,3,32,467,8,32,3,32,469,8,32,1,33,1,33,1,34,1,34,1,
        34,1,35,1,35,1,35,5,35,479,8,35,10,35,12,35,482,9,35,1,35,1,35,1,
        35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,3,36,494,8,36,1,36,1,36,1,
        36,1,36,3,36,500,8,36,1,36,1,36,1,36,5,36,505,8,36,10,36,12,36,508,
        9,36,1,36,1,36,1,37,1,37,3,37,514,8,37,1,38,1,38,1,39,1,39,1,39,
        1,39,1,39,1,39,5,39,524,8,39,10,39,12,39,527,9,39,1,39,3,39,530,
        8,39,1,39,1,39,1,40,1,40,1,40,1,40,5,40,538,8,40,10,40,12,40,541,
        9,40,1,41,1,41,1,41,5,41,546,8,41,10,41,12,41,549,9,41,1,42,1,42,
        1,42,1,42,3,42,555,8,42,1,42,1,42,1,42,1,42,1,42,1,43,1,43,1,43,
        5,43,565,8,43,10,43,12,43,568,9,43,1,44,1,44,1,44,3,44,573,8,44,
        1,45,5,45,576,8,45,10,45,12,45,579,9,45,1,45,1,45,1,46,1,46,1,46,
        1,46,1,47,1,47,1,47,1,47,3,47,591,8,47,1,47,1,47,1,47,1,47,1,47,
        5,47,598,8,47,10,47,12,47,601,9,47,1,47,1,47,1,48,1,48,1,48,5,48,
        608,8,48,10,48,12,48,611,9,48,1,49,1,49,1,49,3,49,616,8,49,1,50,
        1,50,1,50,3,50,621,8,50,1,50,1,50,1,50,1,51,1,51,1,52,1,52,1,52,
        1,53,1,53,1,53,1,53,1,53,1,53,1,53,1,53,1,53,1,53,1,53,0,1,50,54,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,
        90,92,94,96,98,100,102,104,106,0,7,2,0,7,8,64,64,1,0,28,29,1,0,21,
        27,1,0,9,10,1,0,7,8,1,0,15,20,1,0,57,59,672,0,111,1,0,0,0,2,140,
        1,0,0,0,4,164,1,0,0,0,6,166,1,0,0,0,8,177,1,0,0,0,10,181,1,0,0,0,
        12,192,1,0,0,0,14,196,1,0,0,0,16,204,1,0,0,0,18,206,1,0,0,0,20,225,
        1,0,0,0,22,227,1,0,0,0,24,229,1,0,0,0,26,240,1,0,0,0,28,248,1,0,
        0,0,30,259,1,0,0,0,32,261,1,0,0,0,34,269,1,0,0,0,36,280,1,0,0,0,
        38,288,1,0,0,0,40,299,1,0,0,0,42,301,1,0,0,0,44,318,1,0,0,0,46,320,
        1,0,0,0,48,322,1,0,0,0,50,337,1,0,0,0,52,365,1,0,0,0,54,404,1,0,
        0,0,56,406,1,0,0,0,58,410,1,0,0,0,60,412,1,0,0,0,62,439,1,0,0,0,
        64,441,1,0,0,0,66,470,1,0,0,0,68,472,1,0,0,0,70,475,1,0,0,0,72,490,
        1,0,0,0,74,513,1,0,0,0,76,515,1,0,0,0,78,517,1,0,0,0,80,533,1,0,
        0,0,82,542,1,0,0,0,84,550,1,0,0,0,86,561,1,0,0,0,88,569,1,0,0,0,
        90,577,1,0,0,0,92,582,1,0,0,0,94,586,1,0,0,0,96,604,1,0,0,0,98,612,
        1,0,0,0,100,617,1,0,0,0,102,625,1,0,0,0,104,627,1,0,0,0,106,630,
        1,0,0,0,108,110,3,2,1,0,109,108,1,0,0,0,110,113,1,0,0,0,111,109,
        1,0,0,0,111,112,1,0,0,0,112,117,1,0,0,0,113,111,1,0,0,0,114,116,
        3,4,2,0,115,114,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,
        1,0,0,0,118,123,1,0,0,0,119,117,1,0,0,0,120,122,3,104,52,0,121,120,
        1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,129,
        1,0,0,0,125,123,1,0,0,0,126,128,3,100,50,0,127,126,1,0,0,0,128,131,
        1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,135,1,0,0,0,131,129,
        1,0,0,0,132,134,3,106,53,0,133,132,1,0,0,0,134,137,1,0,0,0,135,133,
        1,0,0,0,135,136,1,0,0,0,136,138,1,0,0,0,137,135,1,0,0,0,138,139,
        5,0,0,1,139,1,1,0,0,0,140,141,5,44,0,0,141,146,5,64,0,0,142,143,
        5,35,0,0,143,145,5,64,0,0,144,142,1,0,0,0,145,148,1,0,0,0,146,144,
        1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,146,1,0,0,0,149,150,
        5,33,0,0,150,3,1,0,0,0,151,165,3,6,3,0,152,165,3,10,5,0,153,165,
        3,14,7,0,154,165,3,24,12,0,155,165,3,34,17,0,156,165,3,44,22,0,157,
        165,3,64,32,0,158,165,3,68,34,0,159,165,3,70,35,0,160,165,3,72,36,
        0,161,165,3,78,39,0,162,165,3,84,42,0,163,165,3,94,47,0,164,151,
        1,0,0,0,164,152,1,0,0,0,164,153,1,0,0,0,164,154,1,0,0,0,164,155,
        1,0,0,0,164,156,1,0,0,0,164,157,1,0,0,0,164,158,1,0,0,0,164,159,
        1,0,0,0,164,160,1,0,0,0,164,161,1,0,0,0,164,162,1,0,0,0,164,163,
        1,0,0,0,165,5,1,0,0,0,166,167,5,36,0,0,167,172,3,8,4,0,168,169,5,
        35,0,0,169,171,3,8,4,0,170,168,1,0,0,0,171,174,1,0,0,0,172,170,1,
        0,0,0,172,173,1,0,0,0,173,175,1,0,0,0,174,172,1,0,0,0,175,176,5,
        33,0,0,176,7,1,0,0,0,177,178,5,64,0,0,178,179,5,21,0,0,179,180,3,
        50,25,0,180,9,1,0,0,0,181,182,5,37,0,0,182,187,3,12,6,0,183,184,
        5,35,0,0,184,186,3,12,6,0,185,183,1,0,0,0,186,189,1,0,0,0,187,185,
        1,0,0,0,187,188,1,0,0,0,188,190,1,0,0,0,189,187,1,0,0,0,190,191,
        5,33,0,0,191,11,1,0,0,0,192,193,5,64,0,0,193,194,5,21,0,0,194,195,
        3,50,25,0,195,13,1,0,0,0,196,197,3,16,8,0,197,198,5,64,0,0,198,199,
        5,21,0,0,199,200,3,50,25,0,200,201,5,34,0,0,201,202,3,18,9,0,202,
        203,5,33,0,0,203,15,1,0,0,0,204,205,5,64,0,0,205,17,1,0,0,0,206,
        211,3,20,10,0,207,208,5,35,0,0,208,210,3,20,10,0,209,207,1,0,0,0,
        210,213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,19,1,0,0,0,213,
        211,1,0,0,0,214,226,5,64,0,0,215,216,5,64,0,0,216,217,5,14,0,0,217,
        226,5,64,0,0,218,221,5,64,0,0,219,220,5,13,0,0,220,222,3,22,11,0,
        221,219,1,0,0,0,222,223,1,0,0,0,223,221,1,0,0,0,223,224,1,0,0,0,
        224,226,1,0,0,0,225,214,1,0,0,0,225,215,1,0,0,0,225,218,1,0,0,0,
        226,21,1,0,0,0,227,228,7,0,0,0,228,23,1,0,0,0,229,231,5,40,0,0,230,
        232,5,64,0,0,231,230,1,0,0,0,231,232,1,0,0,0,232,233,1,0,0,0,233,
        234,5,34,0,0,234,235,3,18,9,0,235,236,5,3,0,0,236,237,3,28,14,0,
        237,238,5,4,0,0,238,239,5,33,0,0,239,25,1,0,0,0,240,242,5,40,0,0,
        241,243,5,64,0,0,242,241,1,0,0,0,242,243,1,0,0,0,243,244,1,0,0,0,
        244,245,5,3,0,0,245,246,3,28,14,0,246,247,5,4,0,0,247,27,1,0,0,0,
        248,253,3,30,15,0,249,250,5,35,0,0,250,252,3,30,15,0,251,249,1,0,
        0,0,252,255,1,0,0,0,253,251,1,0,0,0,253,254,1,0,0,0,254,29,1,0,0,
        0,255,253,1,0,0,0,256,260,3,32,16,0,257,260,3,26,13,0,258,260,3,
        36,18,0,259,256,1,0,0,0,259,257,1,0,0,0,259,258,1,0,0,0,260,31,1,
        0,0,0,261,262,3,16,8,0,262,263,5,64,0,0,263,264,5,21,0,0,264,267,
        3,50,25,0,265,266,5,34,0,0,266,268,5,42,0,0,267,265,1,0,0,0,267,
        268,1,0,0,0,268,33,1,0,0,0,269,271,5,41,0,0,270,272,5,64,0,0,271,
        270,1,0,0,0,271,272,1,0,0,0,272,273,1,0,0,0,273,274,5,34,0,0,274,
        275,3,18,9,0,275,276,5,3,0,0,276,277,3,38,19,0,277,278,5,4,0,0,278,
        279,5,33,0,0,279,35,1,0,0,0,280,282,5,41,0,0,281,283,5,64,0,0,282,
        281,1,0,0,0,282,283,1,0,0,0,283,284,1,0,0,0,284,285,5,3,0,0,285,
        286,3,38,19,0,286,287,5,4,0,0,287,37,1,0,0,0,288,293,3,40,20,0,289,
        290,5,35,0,0,290,292,3,40,20,0,291,289,1,0,0,0,292,295,1,0,0,0,293,
        291,1,0,0,0,293,294,1,0,0,0,294,39,1,0,0,0,295,293,1,0,0,0,296,300,
        3,42,21,0,297,300,3,26,13,0,298,300,3,36,18,0,299,296,1,0,0,0,299,
        297,1,0,0,0,299,298,1,0,0,0,300,41,1,0,0,0,301,302,3,16,8,0,302,
        303,5,64,0,0,303,304,5,21,0,0,304,307,3,50,25,0,305,306,5,34,0,0,
        306,308,5,42,0,0,307,305,1,0,0,0,307,308,1,0,0,0,308,43,1,0,0,0,
        309,310,5,64,0,0,310,311,3,46,23,0,311,312,5,33,0,0,312,319,1,0,
        0,0,313,314,5,64,0,0,314,315,3,48,24,0,315,316,3,50,25,0,316,317,
        5,33,0,0,317,319,1,0,0,0,318,309,1,0,0,0,318,313,1,0,0,0,319,45,
        1,0,0,0,320,321,7,1,0,0,321,47,1,0,0,0,322,323,7,2,0,0,323,49,1,
        0,0,0,324,325,6,25,-1,0,325,326,5,32,0,0,326,338,3,50,25,8,327,338,
        3,52,26,0,328,329,5,1,0,0,329,330,3,50,25,0,330,331,5,2,0,0,331,
        338,1,0,0,0,332,338,5,62,0,0,333,338,5,63,0,0,334,338,5,55,0,0,335,
        338,5,56,0,0,336,338,5,64,0,0,337,324,1,0,0,0,337,327,1,0,0,0,337,
        328,1,0,0,0,337,332,1,0,0,0,337,333,1,0,0,0,337,334,1,0,0,0,337,
        335,1,0,0,0,337,336,1,0,0,0,338,362,1,0,0,0,339,340,10,15,0,0,340,
        341,5,12,0,0,341,361,3,50,25,15,342,343,10,14,0,0,343,344,7,3,0,
        0,344,361,3,50,25,15,345,346,10,13,0,0,346,347,5,11,0,0,347,361,
        3,50,25,14,348,349,10,12,0,0,349,350,7,4,0,0,350,361,3,50,25,13,
        351,352,10,11,0,0,352,353,7,5,0,0,353,361,3,50,25,12,354,355,10,
        10,0,0,355,356,5,30,0,0,356,361,3,50,25,11,357,358,10,9,0,0,358,
        359,5,31,0,0,359,361,3,50,25,10,360,339,1,0,0,0,360,342,1,0,0,0,
        360,345,1,0,0,0,360,348,1,0,0,0,360,351,1,0,0,0,360,354,1,0,0,0,
        360,357,1,0,0,0,361,364,1,0,0,0,362,360,1,0,0,0,362,363,1,0,0,0,
        363,51,1,0,0,0,364,362,1,0,0,0,365,366,5,64,0,0,366,368,5,1,0,0,
        367,369,3,54,27,0,368,367,1,0,0,0,368,369,1,0,0,0,369,370,1,0,0,
        0,370,371,5,2,0,0,371,53,1,0,0,0,372,377,3,56,28,0,373,374,5,35,
        0,0,374,376,3,56,28,0,375,373,1,0,0,0,376,379,1,0,0,0,377,375,1,
        0,0,0,377,378,1,0,0,0,378,405,1,0,0,0,379,377,1,0,0,0,380,385,3,
        58,29,0,381,382,5,35,0,0,382,384,3,58,29,0,383,381,1,0,0,0,384,387,
        1,0,0,0,385,383,1,0,0,0,385,386,1,0,0,0,386,405,1,0,0,0,387,385,
        1,0,0,0,388,393,3,58,29,0,389,390,5,35,0,0,390,392,3,58,29,0,391,
        389,1,0,0,0,392,395,1,0,0,0,393,391,1,0,0,0,393,394,1,0,0,0,394,
        396,1,0,0,0,395,393,1,0,0,0,396,401,3,56,28,0,397,398,5,35,0,0,398,
        400,3,56,28,0,399,397,1,0,0,0,400,403,1,0,0,0,401,399,1,0,0,0,401,
        402,1,0,0,0,402,405,1,0,0,0,403,401,1,0,0,0,404,372,1,0,0,0,404,
        380,1,0,0,0,404,388,1,0,0,0,405,55,1,0,0,0,406,407,5,64,0,0,407,
        408,5,21,0,0,408,409,3,50,25,0,409,57,1,0,0,0,410,411,3,50,25,0,
        411,59,1,0,0,0,412,413,5,1,0,0,413,414,3,62,31,0,414,415,5,2,0,0,
        415,419,5,3,0,0,416,418,3,4,2,0,417,416,1,0,0,0,418,421,1,0,0,0,
        419,417,1,0,0,0,419,420,1,0,0,0,420,422,1,0,0,0,421,419,1,0,0,0,
        422,423,5,4,0,0,423,61,1,0,0,0,424,425,3,50,25,0,425,426,3,66,33,
        0,426,427,3,50,25,0,427,440,1,0,0,0,428,429,3,50,25,0,429,430,5,
        30,0,0,430,431,3,50,25,0,431,440,1,0,0,0,432,433,3,50,25,0,433,434,
        5,31,0,0,434,435,3,50,25,0,435,440,1,0,0,0,436,437,5,32,0,0,437,
        440,3,50,25,0,438,440,3,50,25,0,439,424,1,0,0,0,439,428,1,0,0,0,
        439,432,1,0,0,0,439,436,1,0,0,0,439,438,1,0,0,0,440,63,1,0,0,0,441,
        442,5,45,0,0,442,443,5,1,0,0,443,444,3,62,31,0,444,454,5,2,0,0,445,
        455,3,4,2,0,446,450,5,3,0,0,447,449,3,4,2,0,448,447,1,0,0,0,449,
        452,1,0,0,0,450,448,1,0,0,0,450,451,1,0,0,0,451,453,1,0,0,0,452,
        450,1,0,0,0,453,455,5,4,0,0,454,445,1,0,0,0,454,446,1,0,0,0,455,
        468,1,0,0,0,456,466,5,46,0,0,457,467,3,4,2,0,458,462,5,3,0,0,459,
        461,3,4,2,0,460,459,1,0,0,0,461,464,1,0,0,0,462,460,1,0,0,0,462,
        463,1,0,0,0,463,465,1,0,0,0,464,462,1,0,0,0,465,467,5,4,0,0,466,
        457,1,0,0,0,466,458,1,0,0,0,467,469,1,0,0,0,468,456,1,0,0,0,468,
        469,1,0,0,0,469,65,1,0,0,0,470,471,7,5,0,0,471,67,1,0,0,0,472,473,
        5,48,0,0,473,474,3,60,30,0,474,69,1,0,0,0,475,476,5,49,0,0,476,480,
        5,3,0,0,477,479,3,4,2,0,478,477,1,0,0,0,479,482,1,0,0,0,480,478,
        1,0,0,0,480,481,1,0,0,0,481,483,1,0,0,0,482,480,1,0,0,0,483,484,
        5,4,0,0,484,485,5,48,0,0,485,486,5,1,0,0,486,487,3,62,31,0,487,488,
        5,2,0,0,488,489,5,33,0,0,489,71,1,0,0,0,490,491,5,47,0,0,491,493,
        5,1,0,0,492,494,3,74,37,0,493,492,1,0,0,0,493,494,1,0,0,0,494,495,
        1,0,0,0,495,496,5,33,0,0,496,497,3,62,31,0,497,499,5,33,0,0,498,
        500,3,76,38,0,499,498,1,0,0,0,499,500,1,0,0,0,500,501,1,0,0,0,501,
        502,5,2,0,0,502,506,5,3,0,0,503,505,3,4,2,0,504,503,1,0,0,0,505,
        508,1,0,0,0,506,504,1,0,0,0,506,507,1,0,0,0,507,509,1,0,0,0,508,
        506,1,0,0,0,509,510,5,4,0,0,510,73,1,0,0,0,511,514,3,12,6,0,512,
        514,3,44,22,0,513,511,1,0,0,0,513,512,1,0,0,0,514,75,1,0,0,0,515,
        516,3,44,22,0,516,77,1,0,0,0,517,518,5,52,0,0,518,519,5,1,0,0,519,
        520,3,50,25,0,520,521,5,2,0,0,521,525,5,3,0,0,522,524,3,80,40,0,
        523,522,1,0,0,0,524,527,1,0,0,0,525,523,1,0,0,0,525,526,1,0,0,0,
        526,529,1,0,0,0,527,525,1,0,0,0,528,530,3,82,41,0,529,528,1,0,0,
        0,529,530,1,0,0,0,530,531,1,0,0,0,531,532,5,4,0,0,532,79,1,0,0,0,
        533,534,5,53,0,0,534,535,3,50,25,0,535,539,5,34,0,0,536,538,3,4,
        2,0,537,536,1,0,0,0,538,541,1,0,0,0,539,537,1,0,0,0,539,540,1,0,
        0,0,540,81,1,0,0,0,541,539,1,0,0,0,542,543,5,54,0,0,543,547,5,34,
        0,0,544,546,3,4,2,0,545,544,1,0,0,0,546,549,1,0,0,0,547,545,1,0,
        0,0,547,548,1,0,0,0,548,83,1,0,0,0,549,547,1,0,0,0,550,551,5,38,
        0,0,551,552,5,64,0,0,552,554,5,1,0,0,553,555,3,86,43,0,554,553,1,
        0,0,0,554,555,1,0,0,0,555,556,1,0,0,0,556,557,5,2,0,0,557,558,5,
        3,0,0,558,559,3,90,45,0,559,560,5,4,0,0,560,85,1,0,0,0,561,566,3,
        88,44,0,562,563,5,35,0,0,563,565,3,88,44,0,564,562,1,0,0,0,565,568,
        1,0,0,0,566,564,1,0,0,0,566,567,1,0,0,0,567,87,1,0,0,0,568,566,1,
        0,0,0,569,572,5,64,0,0,570,571,5,21,0,0,571,573,3,50,25,0,572,570,
        1,0,0,0,572,573,1,0,0,0,573,89,1,0,0,0,574,576,3,4,2,0,575,574,1,
        0,0,0,576,579,1,0,0,0,577,575,1,0,0,0,577,578,1,0,0,0,578,580,1,
        0,0,0,579,577,1,0,0,0,580,581,3,92,46,0,581,91,1,0,0,0,582,583,5,
        39,0,0,583,584,3,50,25,0,584,585,5,33,0,0,585,93,1,0,0,0,586,587,
        5,43,0,0,587,588,5,64,0,0,588,590,5,1,0,0,589,591,3,96,48,0,590,
        589,1,0,0,0,590,591,1,0,0,0,591,592,1,0,0,0,592,593,5,2,0,0,593,
        594,5,34,0,0,594,595,3,18,9,0,595,599,5,3,0,0,596,598,3,4,2,0,597,
        596,1,0,0,0,598,601,1,0,0,0,599,597,1,0,0,0,599,600,1,0,0,0,600,
        602,1,0,0,0,601,599,1,0,0,0,602,603,5,4,0,0,603,95,1,0,0,0,604,609,
        3,98,49,0,605,606,5,35,0,0,606,608,3,98,49,0,607,605,1,0,0,0,608,
        611,1,0,0,0,609,607,1,0,0,0,609,610,1,0,0,0,610,97,1,0,0,0,611,609,
        1,0,0,0,612,615,5,64,0,0,613,614,5,21,0,0,614,616,3,50,25,0,615,
        613,1,0,0,0,615,616,1,0,0,0,616,99,1,0,0,0,617,618,3,102,51,0,618,
        620,5,1,0,0,619,621,3,54,27,0,620,619,1,0,0,0,620,621,1,0,0,0,621,
        622,1,0,0,0,622,623,5,2,0,0,623,624,5,33,0,0,624,101,1,0,0,0,625,
        626,7,6,0,0,626,103,1,0,0,0,627,628,5,60,0,0,628,629,5,64,0,0,629,
        105,1,0,0,0,630,631,5,61,0,0,631,632,5,64,0,0,632,633,5,21,0,0,633,
        634,5,1,0,0,634,635,5,62,0,0,635,636,5,35,0,0,636,637,5,62,0,0,637,
        638,5,2,0,0,638,639,5,33,0,0,639,107,1,0,0,0,57,111,117,123,129,
        135,146,164,172,187,211,223,225,231,242,253,259,267,271,282,293,
        299,307,318,337,360,362,368,377,385,393,401,404,419,439,450,454,
        462,466,468,480,493,499,506,513,525,529,539,547,554,566,572,577,
        590,599,609,615,620
    ]

class CircuitryParser ( Parser ):

    grammarFileName = "CircuitryParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", "'.'", "'->'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'='", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'^='", "'++'", 
                     "'--'", "'&&'", "'||'", "'!'", "';'", "':'", "','", 
                     "'alias'", "'let'", "'fn'", "'return'", "'series'", 
                     "'parallel'", "'reversed'", "'subcircuit'", "'import'", 
                     "'if'", "'else'", "'for'", "'while'", "'do'", "'break'", 
                     "'continue'", "'switch'", "'case'", "'default'", "'true'", 
                     "'false'", "'transient'", "'ac'", "'dc'", "'measure'", 
                     "'pos'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACKET", "RBRACKET", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "MODULO", "EXPONENT", "DOT", "RARROW", "EQUAL", 
                      "NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", 
                      "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "EXP_ASSIGN", "INC", "DEC", 
                      "AND", "OR", "NOT", "SEMICOLON", "COLON", "COMMA", 
                      "ALIAS", "LET", "FN", "RETURN", "SERIES", "PARALLEL", 
                      "REVERSED", "SUBCIRCUIT", "IMPORT", "IF", "ELSE", 
                      "FOR", "WHILE", "DO", "BREAK", "CONTINUE", "SWITCH", 
                      "CASE", "DEFAULT", "TRUE", "FALSE", "TRANSIENT", "AC", 
                      "DC", "MEASURE", "POS", "FLOAT_LITERAL", "STRING_LITERAL", 
                      "ID", "LINE_COMMENT", "MULTILINE_COMMENT", "WS" ]

    RULE_program = 0
    RULE_importStatement = 1
    RULE_topologyStatement = 2
    RULE_aliasStatement = 3
    RULE_aliasAssignment = 4
    RULE_letStatement = 5
    RULE_letAssignment = 6
    RULE_componentStatement = 7
    RULE_componentType = 8
    RULE_nodeList = 9
    RULE_nodeMapping = 10
    RULE_dottedNode = 11
    RULE_seriesStatement = 12
    RULE_nestedSeriesStatement = 13
    RULE_seriesBody = 14
    RULE_seriesElement = 15
    RULE_seriesAssignment = 16
    RULE_parallelStatement = 17
    RULE_nestedParallelStatement = 18
    RULE_parallelBody = 19
    RULE_parallelElement = 20
    RULE_parallelAssignment = 21
    RULE_assignmentStatement = 22
    RULE_unaryAssignmentOperator = 23
    RULE_binaryAssignmentOperator = 24
    RULE_expr = 25
    RULE_functionCall = 26
    RULE_functionCallArgs = 27
    RULE_functionCallKeywordArg = 28
    RULE_functionCallPositionalArg = 29
    RULE_conditionWithBlock = 30
    RULE_booleanExpr = 31
    RULE_ifStatement = 32
    RULE_relationalOperator = 33
    RULE_whileStatement = 34
    RULE_doWhileStatement = 35
    RULE_forStatement = 36
    RULE_forInit = 37
    RULE_forUpdate = 38
    RULE_switchStatement = 39
    RULE_caseStatement = 40
    RULE_defaultStatement = 41
    RULE_functionDefinition = 42
    RULE_functionParams = 43
    RULE_functionParam = 44
    RULE_functionBody = 45
    RULE_returnStatement = 46
    RULE_subcircuitDefinition = 47
    RULE_subcircuitParams = 48
    RULE_subcircuitParam = 49
    RULE_simulationStatement = 50
    RULE_simulationType = 51
    RULE_measurementStatement = 52
    RULE_drawingStatement = 53

    ruleNames =  [ "program", "importStatement", "topologyStatement", "aliasStatement", 
                   "aliasAssignment", "letStatement", "letAssignment", "componentStatement", 
                   "componentType", "nodeList", "nodeMapping", "dottedNode", 
                   "seriesStatement", "nestedSeriesStatement", "seriesBody", 
                   "seriesElement", "seriesAssignment", "parallelStatement", 
                   "nestedParallelStatement", "parallelBody", "parallelElement", 
                   "parallelAssignment", "assignmentStatement", "unaryAssignmentOperator", 
                   "binaryAssignmentOperator", "expr", "functionCall", "functionCallArgs", 
                   "functionCallKeywordArg", "functionCallPositionalArg", 
                   "conditionWithBlock", "booleanExpr", "ifStatement", "relationalOperator", 
                   "whileStatement", "doWhileStatement", "forStatement", 
                   "forInit", "forUpdate", "switchStatement", "caseStatement", 
                   "defaultStatement", "functionDefinition", "functionParams", 
                   "functionParam", "functionBody", "returnStatement", "subcircuitDefinition", 
                   "subcircuitParams", "subcircuitParam", "simulationStatement", 
                   "simulationType", "measurementStatement", "drawingStatement" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    LBRACE=3
    RBRACE=4
    LBRACKET=5
    RBRACKET=6
    PLUS=7
    MINUS=8
    MULTIPLY=9
    DIVIDE=10
    MODULO=11
    EXPONENT=12
    DOT=13
    RARROW=14
    EQUAL=15
    NOT_EQUAL=16
    LESS=17
    GREATER=18
    LESS_EQUAL=19
    GREATER_EQUAL=20
    ASSIGN=21
    ADD_ASSIGN=22
    SUB_ASSIGN=23
    MUL_ASSIGN=24
    DIV_ASSIGN=25
    MOD_ASSIGN=26
    EXP_ASSIGN=27
    INC=28
    DEC=29
    AND=30
    OR=31
    NOT=32
    SEMICOLON=33
    COLON=34
    COMMA=35
    ALIAS=36
    LET=37
    FN=38
    RETURN=39
    SERIES=40
    PARALLEL=41
    REVERSED=42
    SUBCIRCUIT=43
    IMPORT=44
    IF=45
    ELSE=46
    FOR=47
    WHILE=48
    DO=49
    BREAK=50
    CONTINUE=51
    SWITCH=52
    CASE=53
    DEFAULT=54
    TRUE=55
    FALSE=56
    TRANSIENT=57
    AC=58
    DC=59
    MEASURE=60
    POS=61
    FLOAT_LITERAL=62
    STRING_LITERAL=63
    ID=64
    LINE_COMMENT=65
    MULTILINE_COMMENT=66
    WS=67

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CircuitryParser.EOF, 0)

        def importStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.ImportStatementContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.ImportStatementContext,i)


        def topologyStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.TopologyStatementContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.TopologyStatementContext,i)


        def measurementStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.MeasurementStatementContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.MeasurementStatementContext,i)


        def simulationStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.SimulationStatementContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.SimulationStatementContext,i)


        def drawingStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.DrawingStatementContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.DrawingStatementContext,i)


        def getRuleIndex(self):
            return CircuitryParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CircuitryParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 108
                self.importStatement()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & 268516023) != 0):
                self.state = 114
                self.topologyStatement()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==60:
                self.state = 120
                self.measurementStatement()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1008806316530991104) != 0):
                self.state = 126
                self.simulationStatement()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==61:
                self.state = 132
                self.drawingStatement()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
            self.match(CircuitryParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(CircuitryParser.IMPORT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitryParser.ID)
            else:
                return self.getToken(CircuitryParser.ID, i)

        def SEMICOLON(self):
            return self.getToken(CircuitryParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitryParser.COMMA)
            else:
                return self.getToken(CircuitryParser.COMMA, i)

        def getRuleIndex(self):
            return CircuitryParser.RULE_importStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportStatement" ):
                listener.enterImportStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportStatement" ):
                listener.exitImportStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportStatement" ):
                return visitor.visitImportStatement(self)
            else:
                return visitor.visitChildren(self)




    def importStatement(self):

        localctx = CircuitryParser.ImportStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_importStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(CircuitryParser.IMPORT)
            self.state = 141
            self.match(CircuitryParser.ID)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 142
                self.match(CircuitryParser.COMMA)
                self.state = 143
                self.match(CircuitryParser.ID)
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
            self.match(CircuitryParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopologyStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aliasStatement(self):
            return self.getTypedRuleContext(CircuitryParser.AliasStatementContext,0)


        def letStatement(self):
            return self.getTypedRuleContext(CircuitryParser.LetStatementContext,0)


        def componentStatement(self):
            return self.getTypedRuleContext(CircuitryParser.ComponentStatementContext,0)


        def seriesStatement(self):
            return self.getTypedRuleContext(CircuitryParser.SeriesStatementContext,0)


        def parallelStatement(self):
            return self.getTypedRuleContext(CircuitryParser.ParallelStatementContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(CircuitryParser.AssignmentStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(CircuitryParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(CircuitryParser.WhileStatementContext,0)


        def doWhileStatement(self):
            return self.getTypedRuleContext(CircuitryParser.DoWhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(CircuitryParser.ForStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(CircuitryParser.SwitchStatementContext,0)


        def functionDefinition(self):
            return self.getTypedRuleContext(CircuitryParser.FunctionDefinitionContext,0)


        def subcircuitDefinition(self):
            return self.getTypedRuleContext(CircuitryParser.SubcircuitDefinitionContext,0)


        def getRuleIndex(self):
            return CircuitryParser.RULE_topologyStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopologyStatement" ):
                listener.enterTopologyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopologyStatement" ):
                listener.exitTopologyStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopologyStatement" ):
                return visitor.visitTopologyStatement(self)
            else:
                return visitor.visitChildren(self)




    def topologyStatement(self):

        localctx = CircuitryParser.TopologyStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_topologyStatement)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.aliasStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.letStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.componentStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self.seriesStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 155
                self.parallelStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 156
                self.assignmentStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 157
                self.ifStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 158
                self.whileStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 159
                self.doWhileStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 160
                self.forStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 161
                self.switchStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 162
                self.functionDefinition()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 163
                self.subcircuitDefinition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AliasStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALIAS(self):
            return self.getToken(CircuitryParser.ALIAS, 0)

        def aliasAssignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.AliasAssignmentContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.AliasAssignmentContext,i)


        def SEMICOLON(self):
            return self.getToken(CircuitryParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitryParser.COMMA)
            else:
                return self.getToken(CircuitryParser.COMMA, i)

        def getRuleIndex(self):
            return CircuitryParser.RULE_aliasStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAliasStatement" ):
                listener.enterAliasStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAliasStatement" ):
                listener.exitAliasStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAliasStatement" ):
                return visitor.visitAliasStatement(self)
            else:
                return visitor.visitChildren(self)




    def aliasStatement(self):

        localctx = CircuitryParser.AliasStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_aliasStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(CircuitryParser.ALIAS)
            self.state = 167
            self.aliasAssignment()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 168
                self.match(CircuitryParser.COMMA)
                self.state = 169
                self.aliasAssignment()
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 175
            self.match(CircuitryParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AliasAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CircuitryParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CircuitryParser.ExprContext,0)


        def getRuleIndex(self):
            return CircuitryParser.RULE_aliasAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAliasAssignment" ):
                listener.enterAliasAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAliasAssignment" ):
                listener.exitAliasAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAliasAssignment" ):
                return visitor.visitAliasAssignment(self)
            else:
                return visitor.visitChildren(self)




    def aliasAssignment(self):

        localctx = CircuitryParser.AliasAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_aliasAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(CircuitryParser.ID)
            self.state = 178
            self.match(CircuitryParser.ASSIGN)
            self.state = 179
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(CircuitryParser.LET, 0)

        def letAssignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.LetAssignmentContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.LetAssignmentContext,i)


        def SEMICOLON(self):
            return self.getToken(CircuitryParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitryParser.COMMA)
            else:
                return self.getToken(CircuitryParser.COMMA, i)

        def getRuleIndex(self):
            return CircuitryParser.RULE_letStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetStatement" ):
                listener.enterLetStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetStatement" ):
                listener.exitLetStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetStatement" ):
                return visitor.visitLetStatement(self)
            else:
                return visitor.visitChildren(self)




    def letStatement(self):

        localctx = CircuitryParser.LetStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_letStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(CircuitryParser.LET)
            self.state = 182
            self.letAssignment()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 183
                self.match(CircuitryParser.COMMA)
                self.state = 184
                self.letAssignment()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 190
            self.match(CircuitryParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CircuitryParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CircuitryParser.ExprContext,0)


        def getRuleIndex(self):
            return CircuitryParser.RULE_letAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetAssignment" ):
                listener.enterLetAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetAssignment" ):
                listener.exitLetAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetAssignment" ):
                return visitor.visitLetAssignment(self)
            else:
                return visitor.visitChildren(self)




    def letAssignment(self):

        localctx = CircuitryParser.LetAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_letAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(CircuitryParser.ID)
            self.state = 193
            self.match(CircuitryParser.ASSIGN)
            self.state = 194
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComponentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def componentType(self):
            return self.getTypedRuleContext(CircuitryParser.ComponentTypeContext,0)


        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CircuitryParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CircuitryParser.ExprContext,0)


        def COLON(self):
            return self.getToken(CircuitryParser.COLON, 0)

        def nodeList(self):
            return self.getTypedRuleContext(CircuitryParser.NodeListContext,0)


        def SEMICOLON(self):
            return self.getToken(CircuitryParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CircuitryParser.RULE_componentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponentStatement" ):
                listener.enterComponentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponentStatement" ):
                listener.exitComponentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComponentStatement" ):
                return visitor.visitComponentStatement(self)
            else:
                return visitor.visitChildren(self)




    def componentStatement(self):

        localctx = CircuitryParser.ComponentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_componentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.componentType()
            self.state = 197
            self.match(CircuitryParser.ID)
            self.state = 198
            self.match(CircuitryParser.ASSIGN)
            self.state = 199
            self.expr(0)
            self.state = 200
            self.match(CircuitryParser.COLON)
            self.state = 201
            self.nodeList()
            self.state = 202
            self.match(CircuitryParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComponentTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def getRuleIndex(self):
            return CircuitryParser.RULE_componentType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponentType" ):
                listener.enterComponentType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponentType" ):
                listener.exitComponentType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComponentType" ):
                return visitor.visitComponentType(self)
            else:
                return visitor.visitChildren(self)




    def componentType(self):

        localctx = CircuitryParser.ComponentTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_componentType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(CircuitryParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nodeMapping(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.NodeMappingContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.NodeMappingContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitryParser.COMMA)
            else:
                return self.getToken(CircuitryParser.COMMA, i)

        def getRuleIndex(self):
            return CircuitryParser.RULE_nodeList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodeList" ):
                listener.enterNodeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodeList" ):
                listener.exitNodeList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNodeList" ):
                return visitor.visitNodeList(self)
            else:
                return visitor.visitChildren(self)




    def nodeList(self):

        localctx = CircuitryParser.NodeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_nodeList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.nodeMapping()
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 207
                self.match(CircuitryParser.COMMA)
                self.state = 208
                self.nodeMapping()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeMappingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CircuitryParser.RULE_nodeMapping

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SubNodeContext(NodeMappingContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitryParser.NodeMappingContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)
        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitryParser.DOT)
            else:
                return self.getToken(CircuitryParser.DOT, i)
        def dottedNode(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.DottedNodeContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.DottedNodeContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubNode" ):
                listener.enterSubNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubNode" ):
                listener.exitSubNode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubNode" ):
                return visitor.visitSubNode(self)
            else:
                return visitor.visitChildren(self)


    class RemappedNodeContext(NodeMappingContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitryParser.NodeMappingContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitryParser.ID)
            else:
                return self.getToken(CircuitryParser.ID, i)
        def RARROW(self):
            return self.getToken(CircuitryParser.RARROW, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRemappedNode" ):
                listener.enterRemappedNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRemappedNode" ):
                listener.exitRemappedNode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRemappedNode" ):
                return visitor.visitRemappedNode(self)
            else:
                return visitor.visitChildren(self)


    class DirectNodeContext(NodeMappingContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitryParser.NodeMappingContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirectNode" ):
                listener.enterDirectNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirectNode" ):
                listener.exitDirectNode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirectNode" ):
                return visitor.visitDirectNode(self)
            else:
                return visitor.visitChildren(self)



    def nodeMapping(self):

        localctx = CircuitryParser.NodeMappingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_nodeMapping)
        self._la = 0 # Token type
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = CircuitryParser.DirectNodeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(CircuitryParser.ID)
                pass

            elif la_ == 2:
                localctx = CircuitryParser.RemappedNodeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(CircuitryParser.ID)
                self.state = 216
                self.match(CircuitryParser.RARROW)
                self.state = 217
                self.match(CircuitryParser.ID)
                pass

            elif la_ == 3:
                localctx = CircuitryParser.SubNodeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 218
                self.match(CircuitryParser.ID)
                self.state = 221 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 219
                    self.match(CircuitryParser.DOT)
                    self.state = 220
                    self.dottedNode()
                    self.state = 223 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==13):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DottedNodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def PLUS(self):
            return self.getToken(CircuitryParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(CircuitryParser.MINUS, 0)

        def getRuleIndex(self):
            return CircuitryParser.RULE_dottedNode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDottedNode" ):
                listener.enterDottedNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDottedNode" ):
                listener.exitDottedNode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDottedNode" ):
                return visitor.visitDottedNode(self)
            else:
                return visitor.visitChildren(self)




    def dottedNode(self):

        localctx = CircuitryParser.DottedNodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dottedNode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            _la = self._input.LA(1)
            if not(((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & 144115188075855875) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeriesStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SERIES(self):
            return self.getToken(CircuitryParser.SERIES, 0)

        def COLON(self):
            return self.getToken(CircuitryParser.COLON, 0)

        def nodeList(self):
            return self.getTypedRuleContext(CircuitryParser.NodeListContext,0)


        def LBRACE(self):
            return self.getToken(CircuitryParser.LBRACE, 0)

        def seriesBody(self):
            return self.getTypedRuleContext(CircuitryParser.SeriesBodyContext,0)


        def RBRACE(self):
            return self.getToken(CircuitryParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(CircuitryParser.SEMICOLON, 0)

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def getRuleIndex(self):
            return CircuitryParser.RULE_seriesStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeriesStatement" ):
                listener.enterSeriesStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeriesStatement" ):
                listener.exitSeriesStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeriesStatement" ):
                return visitor.visitSeriesStatement(self)
            else:
                return visitor.visitChildren(self)




    def seriesStatement(self):

        localctx = CircuitryParser.SeriesStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_seriesStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(CircuitryParser.SERIES)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 230
                self.match(CircuitryParser.ID)


            self.state = 233
            self.match(CircuitryParser.COLON)
            self.state = 234
            self.nodeList()
            self.state = 235
            self.match(CircuitryParser.LBRACE)
            self.state = 236
            self.seriesBody()
            self.state = 237
            self.match(CircuitryParser.RBRACE)
            self.state = 238
            self.match(CircuitryParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NestedSeriesStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SERIES(self):
            return self.getToken(CircuitryParser.SERIES, 0)

        def LBRACE(self):
            return self.getToken(CircuitryParser.LBRACE, 0)

        def seriesBody(self):
            return self.getTypedRuleContext(CircuitryParser.SeriesBodyContext,0)


        def RBRACE(self):
            return self.getToken(CircuitryParser.RBRACE, 0)

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def getRuleIndex(self):
            return CircuitryParser.RULE_nestedSeriesStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNestedSeriesStatement" ):
                listener.enterNestedSeriesStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNestedSeriesStatement" ):
                listener.exitNestedSeriesStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNestedSeriesStatement" ):
                return visitor.visitNestedSeriesStatement(self)
            else:
                return visitor.visitChildren(self)




    def nestedSeriesStatement(self):

        localctx = CircuitryParser.NestedSeriesStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_nestedSeriesStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(CircuitryParser.SERIES)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 241
                self.match(CircuitryParser.ID)


            self.state = 244
            self.match(CircuitryParser.LBRACE)
            self.state = 245
            self.seriesBody()
            self.state = 246
            self.match(CircuitryParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeriesBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seriesElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.SeriesElementContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.SeriesElementContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitryParser.COMMA)
            else:
                return self.getToken(CircuitryParser.COMMA, i)

        def getRuleIndex(self):
            return CircuitryParser.RULE_seriesBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeriesBody" ):
                listener.enterSeriesBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeriesBody" ):
                listener.exitSeriesBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeriesBody" ):
                return visitor.visitSeriesBody(self)
            else:
                return visitor.visitChildren(self)




    def seriesBody(self):

        localctx = CircuitryParser.SeriesBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_seriesBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.seriesElement()
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 249
                self.match(CircuitryParser.COMMA)
                self.state = 250
                self.seriesElement()
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeriesElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seriesAssignment(self):
            return self.getTypedRuleContext(CircuitryParser.SeriesAssignmentContext,0)


        def nestedSeriesStatement(self):
            return self.getTypedRuleContext(CircuitryParser.NestedSeriesStatementContext,0)


        def nestedParallelStatement(self):
            return self.getTypedRuleContext(CircuitryParser.NestedParallelStatementContext,0)


        def getRuleIndex(self):
            return CircuitryParser.RULE_seriesElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeriesElement" ):
                listener.enterSeriesElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeriesElement" ):
                listener.exitSeriesElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeriesElement" ):
                return visitor.visitSeriesElement(self)
            else:
                return visitor.visitChildren(self)




    def seriesElement(self):

        localctx = CircuitryParser.SeriesElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_seriesElement)
        try:
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.seriesAssignment()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.nestedSeriesStatement()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.nestedParallelStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeriesAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def componentType(self):
            return self.getTypedRuleContext(CircuitryParser.ComponentTypeContext,0)


        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CircuitryParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CircuitryParser.ExprContext,0)


        def COLON(self):
            return self.getToken(CircuitryParser.COLON, 0)

        def REVERSED(self):
            return self.getToken(CircuitryParser.REVERSED, 0)

        def getRuleIndex(self):
            return CircuitryParser.RULE_seriesAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeriesAssignment" ):
                listener.enterSeriesAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeriesAssignment" ):
                listener.exitSeriesAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeriesAssignment" ):
                return visitor.visitSeriesAssignment(self)
            else:
                return visitor.visitChildren(self)




    def seriesAssignment(self):

        localctx = CircuitryParser.SeriesAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_seriesAssignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.componentType()
            self.state = 262
            self.match(CircuitryParser.ID)
            self.state = 263
            self.match(CircuitryParser.ASSIGN)
            self.state = 264
            self.expr(0)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 265
                self.match(CircuitryParser.COLON)
                self.state = 266
                self.match(CircuitryParser.REVERSED)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParallelStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARALLEL(self):
            return self.getToken(CircuitryParser.PARALLEL, 0)

        def COLON(self):
            return self.getToken(CircuitryParser.COLON, 0)

        def nodeList(self):
            return self.getTypedRuleContext(CircuitryParser.NodeListContext,0)


        def LBRACE(self):
            return self.getToken(CircuitryParser.LBRACE, 0)

        def parallelBody(self):
            return self.getTypedRuleContext(CircuitryParser.ParallelBodyContext,0)


        def RBRACE(self):
            return self.getToken(CircuitryParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(CircuitryParser.SEMICOLON, 0)

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def getRuleIndex(self):
            return CircuitryParser.RULE_parallelStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParallelStatement" ):
                listener.enterParallelStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParallelStatement" ):
                listener.exitParallelStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParallelStatement" ):
                return visitor.visitParallelStatement(self)
            else:
                return visitor.visitChildren(self)




    def parallelStatement(self):

        localctx = CircuitryParser.ParallelStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parallelStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(CircuitryParser.PARALLEL)
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 270
                self.match(CircuitryParser.ID)


            self.state = 273
            self.match(CircuitryParser.COLON)
            self.state = 274
            self.nodeList()
            self.state = 275
            self.match(CircuitryParser.LBRACE)
            self.state = 276
            self.parallelBody()
            self.state = 277
            self.match(CircuitryParser.RBRACE)
            self.state = 278
            self.match(CircuitryParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NestedParallelStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARALLEL(self):
            return self.getToken(CircuitryParser.PARALLEL, 0)

        def LBRACE(self):
            return self.getToken(CircuitryParser.LBRACE, 0)

        def parallelBody(self):
            return self.getTypedRuleContext(CircuitryParser.ParallelBodyContext,0)


        def RBRACE(self):
            return self.getToken(CircuitryParser.RBRACE, 0)

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def getRuleIndex(self):
            return CircuitryParser.RULE_nestedParallelStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNestedParallelStatement" ):
                listener.enterNestedParallelStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNestedParallelStatement" ):
                listener.exitNestedParallelStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNestedParallelStatement" ):
                return visitor.visitNestedParallelStatement(self)
            else:
                return visitor.visitChildren(self)




    def nestedParallelStatement(self):

        localctx = CircuitryParser.NestedParallelStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_nestedParallelStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(CircuitryParser.PARALLEL)
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 281
                self.match(CircuitryParser.ID)


            self.state = 284
            self.match(CircuitryParser.LBRACE)
            self.state = 285
            self.parallelBody()
            self.state = 286
            self.match(CircuitryParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParallelBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parallelElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.ParallelElementContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.ParallelElementContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitryParser.COMMA)
            else:
                return self.getToken(CircuitryParser.COMMA, i)

        def getRuleIndex(self):
            return CircuitryParser.RULE_parallelBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParallelBody" ):
                listener.enterParallelBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParallelBody" ):
                listener.exitParallelBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParallelBody" ):
                return visitor.visitParallelBody(self)
            else:
                return visitor.visitChildren(self)




    def parallelBody(self):

        localctx = CircuitryParser.ParallelBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_parallelBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.parallelElement()
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 289
                self.match(CircuitryParser.COMMA)
                self.state = 290
                self.parallelElement()
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParallelElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parallelAssignment(self):
            return self.getTypedRuleContext(CircuitryParser.ParallelAssignmentContext,0)


        def nestedSeriesStatement(self):
            return self.getTypedRuleContext(CircuitryParser.NestedSeriesStatementContext,0)


        def nestedParallelStatement(self):
            return self.getTypedRuleContext(CircuitryParser.NestedParallelStatementContext,0)


        def getRuleIndex(self):
            return CircuitryParser.RULE_parallelElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParallelElement" ):
                listener.enterParallelElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParallelElement" ):
                listener.exitParallelElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParallelElement" ):
                return visitor.visitParallelElement(self)
            else:
                return visitor.visitChildren(self)




    def parallelElement(self):

        localctx = CircuitryParser.ParallelElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_parallelElement)
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.parallelAssignment()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.nestedSeriesStatement()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 3)
                self.state = 298
                self.nestedParallelStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParallelAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def componentType(self):
            return self.getTypedRuleContext(CircuitryParser.ComponentTypeContext,0)


        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CircuitryParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CircuitryParser.ExprContext,0)


        def COLON(self):
            return self.getToken(CircuitryParser.COLON, 0)

        def REVERSED(self):
            return self.getToken(CircuitryParser.REVERSED, 0)

        def getRuleIndex(self):
            return CircuitryParser.RULE_parallelAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParallelAssignment" ):
                listener.enterParallelAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParallelAssignment" ):
                listener.exitParallelAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParallelAssignment" ):
                return visitor.visitParallelAssignment(self)
            else:
                return visitor.visitChildren(self)




    def parallelAssignment(self):

        localctx = CircuitryParser.ParallelAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_parallelAssignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.componentType()
            self.state = 302
            self.match(CircuitryParser.ID)
            self.state = 303
            self.match(CircuitryParser.ASSIGN)
            self.state = 304
            self.expr(0)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 305
                self.match(CircuitryParser.COLON)
                self.state = 306
                self.match(CircuitryParser.REVERSED)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def unaryAssignmentOperator(self):
            return self.getTypedRuleContext(CircuitryParser.UnaryAssignmentOperatorContext,0)


        def SEMICOLON(self):
            return self.getToken(CircuitryParser.SEMICOLON, 0)

        def binaryAssignmentOperator(self):
            return self.getTypedRuleContext(CircuitryParser.BinaryAssignmentOperatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(CircuitryParser.ExprContext,0)


        def getRuleIndex(self):
            return CircuitryParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = CircuitryParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assignmentStatement)
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(CircuitryParser.ID)
                self.state = 310
                self.unaryAssignmentOperator()
                self.state = 311
                self.match(CircuitryParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.match(CircuitryParser.ID)
                self.state = 314
                self.binaryAssignmentOperator()
                self.state = 315
                self.expr(0)
                self.state = 316
                self.match(CircuitryParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryAssignmentOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INC(self):
            return self.getToken(CircuitryParser.INC, 0)

        def DEC(self):
            return self.getToken(CircuitryParser.DEC, 0)

        def getRuleIndex(self):
            return CircuitryParser.RULE_unaryAssignmentOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryAssignmentOperator" ):
                listener.enterUnaryAssignmentOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryAssignmentOperator" ):
                listener.exitUnaryAssignmentOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryAssignmentOperator" ):
                return visitor.visitUnaryAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def unaryAssignmentOperator(self):

        localctx = CircuitryParser.UnaryAssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_unaryAssignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryAssignmentOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(CircuitryParser.ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(CircuitryParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(CircuitryParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(CircuitryParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(CircuitryParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(CircuitryParser.MOD_ASSIGN, 0)

        def EXP_ASSIGN(self):
            return self.getToken(CircuitryParser.EXP_ASSIGN, 0)

        def getRuleIndex(self):
            return CircuitryParser.RULE_binaryAssignmentOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryAssignmentOperator" ):
                listener.enterBinaryAssignmentOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryAssignmentOperator" ):
                listener.exitBinaryAssignmentOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryAssignmentOperator" ):
                return visitor.visitBinaryAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def binaryAssignmentOperator(self):

        localctx = CircuitryParser.BinaryAssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_binaryAssignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 266338304) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CircuitryParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitryParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.ExprContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.ExprContext,i)

        def AND(self):
            return self.getToken(CircuitryParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class TrueLiteralExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitryParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(CircuitryParser.TRUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrueLiteralExpr" ):
                listener.enterTrueLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrueLiteralExpr" ):
                listener.exitTrueLiteralExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrueLiteralExpr" ):
                return visitor.visitTrueLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitryParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class FalseLiteralExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitryParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(CircuitryParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalseLiteralExpr" ):
                listener.enterFalseLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalseLiteralExpr" ):
                listener.exitFalseLiteralExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalseLiteralExpr" ):
                return visitor.visitFalseLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class StringLiteralExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitryParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_LITERAL(self):
            return self.getToken(CircuitryParser.STRING_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteralExpr" ):
                listener.enterStringLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteralExpr" ):
                listener.exitStringLiteralExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteralExpr" ):
                return visitor.visitStringLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelationalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitryParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.ExprContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.ExprContext,i)

        def EQUAL(self):
            return self.getToken(CircuitryParser.EQUAL, 0)
        def NOT_EQUAL(self):
            return self.getToken(CircuitryParser.NOT_EQUAL, 0)
        def LESS(self):
            return self.getToken(CircuitryParser.LESS, 0)
        def GREATER(self):
            return self.getToken(CircuitryParser.GREATER, 0)
        def LESS_EQUAL(self):
            return self.getToken(CircuitryParser.LESS_EQUAL, 0)
        def GREATER_EQUAL(self):
            return self.getToken(CircuitryParser.GREATER_EQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpr" ):
                listener.enterRelationalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpr" ):
                listener.exitRelationalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)


    class ExpExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitryParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.ExprContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.ExprContext,i)

        def EXPONENT(self):
            return self.getToken(CircuitryParser.EXPONENT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpExpr" ):
                listener.enterExpExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpExpr" ):
                listener.exitExpExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpExpr" ):
                return visitor.visitExpExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitryParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.ExprContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.ExprContext,i)

        def OR(self):
            return self.getToken(CircuitryParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitryParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.ExprContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.ExprContext,i)

        def MULTIPLY(self):
            return self.getToken(CircuitryParser.MULTIPLY, 0)
        def DIVIDE(self):
            return self.getToken(CircuitryParser.DIVIDE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class FloatLiteralExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitryParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_LITERAL(self):
            return self.getToken(CircuitryParser.FLOAT_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatLiteralExpr" ):
                listener.enterFloatLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatLiteralExpr" ):
                listener.exitFloatLiteralExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatLiteralExpr" ):
                return visitor.visitFloatLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitryParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(CircuitryParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(CircuitryParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class ModExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitryParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.ExprContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.ExprContext,i)

        def MODULO(self):
            return self.getToken(CircuitryParser.MODULO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModExpr" ):
                listener.enterModExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModExpr" ):
                listener.exitModExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModExpr" ):
                return visitor.visitModExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitryParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(CircuitryParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(CircuitryParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(CircuitryParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitryParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.ExprContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(CircuitryParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(CircuitryParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CircuitryParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(CircuitryParser.FunctionCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCallExpr" ):
                listener.enterFuncCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCallExpr" ):
                listener.exitFuncCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallExpr" ):
                return visitor.visitFuncCallExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CircuitryParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                localctx = CircuitryParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 325
                self.match(CircuitryParser.NOT)
                self.state = 326
                self.expr(8)
                pass

            elif la_ == 2:
                localctx = CircuitryParser.FuncCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 327
                self.functionCall()
                pass

            elif la_ == 3:
                localctx = CircuitryParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 328
                self.match(CircuitryParser.LPAREN)
                self.state = 329
                self.expr(0)
                self.state = 330
                self.match(CircuitryParser.RPAREN)
                pass

            elif la_ == 4:
                localctx = CircuitryParser.FloatLiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 332
                self.match(CircuitryParser.FLOAT_LITERAL)
                pass

            elif la_ == 5:
                localctx = CircuitryParser.StringLiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 333
                self.match(CircuitryParser.STRING_LITERAL)
                pass

            elif la_ == 6:
                localctx = CircuitryParser.TrueLiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 334
                self.match(CircuitryParser.TRUE)
                pass

            elif la_ == 7:
                localctx = CircuitryParser.FalseLiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 335
                self.match(CircuitryParser.FALSE)
                pass

            elif la_ == 8:
                localctx = CircuitryParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 336
                self.match(CircuitryParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 362
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 360
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = CircuitryParser.ExpExprContext(self, CircuitryParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 339
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 340
                        self.match(CircuitryParser.EXPONENT)
                        self.state = 341
                        self.expr(15)
                        pass

                    elif la_ == 2:
                        localctx = CircuitryParser.MulDivExprContext(self, CircuitryParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 342
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 343
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 344
                        self.expr(15)
                        pass

                    elif la_ == 3:
                        localctx = CircuitryParser.ModExprContext(self, CircuitryParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 345
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 346
                        self.match(CircuitryParser.MODULO)
                        self.state = 347
                        self.expr(14)
                        pass

                    elif la_ == 4:
                        localctx = CircuitryParser.AddSubExprContext(self, CircuitryParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 348
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 349
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 350
                        self.expr(13)
                        pass

                    elif la_ == 5:
                        localctx = CircuitryParser.RelationalExprContext(self, CircuitryParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 351
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 352
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 353
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = CircuitryParser.AndExprContext(self, CircuitryParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 354
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 355
                        localctx.op = self.match(CircuitryParser.AND)
                        self.state = 356
                        self.expr(11)
                        pass

                    elif la_ == 7:
                        localctx = CircuitryParser.OrExprContext(self, CircuitryParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 357
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 358
                        localctx.op = self.match(CircuitryParser.OR)
                        self.state = 359
                        self.expr(10)
                        pass

             
                self.state = 364
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CircuitryParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CircuitryParser.RPAREN, 0)

        def functionCallArgs(self):
            return self.getTypedRuleContext(CircuitryParser.FunctionCallArgsContext,0)


        def getRuleIndex(self):
            return CircuitryParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = CircuitryParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(CircuitryParser.ID)
            self.state = 366
            self.match(CircuitryParser.LPAREN)
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & -2251799811537764351) != 0):
                self.state = 367
                self.functionCallArgs()


            self.state = 370
            self.match(CircuitryParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCallKeywordArg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.FunctionCallKeywordArgContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.FunctionCallKeywordArgContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitryParser.COMMA)
            else:
                return self.getToken(CircuitryParser.COMMA, i)

        def functionCallPositionalArg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.FunctionCallPositionalArgContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.FunctionCallPositionalArgContext,i)


        def getRuleIndex(self):
            return CircuitryParser.RULE_functionCallArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallArgs" ):
                listener.enterFunctionCallArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallArgs" ):
                listener.exitFunctionCallArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallArgs" ):
                return visitor.visitFunctionCallArgs(self)
            else:
                return visitor.visitChildren(self)




    def functionCallArgs(self):

        localctx = CircuitryParser.FunctionCallArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_functionCallArgs)
        self._la = 0 # Token type
        try:
            self.state = 404
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.functionCallKeywordArg()
                self.state = 377
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==35:
                    self.state = 373
                    self.match(CircuitryParser.COMMA)
                    self.state = 374
                    self.functionCallKeywordArg()
                    self.state = 379
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.functionCallPositionalArg()
                self.state = 385
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==35:
                    self.state = 381
                    self.match(CircuitryParser.COMMA)
                    self.state = 382
                    self.functionCallPositionalArg()
                    self.state = 387
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 388
                self.functionCallPositionalArg()
                self.state = 393
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==35:
                    self.state = 389
                    self.match(CircuitryParser.COMMA)
                    self.state = 390
                    self.functionCallPositionalArg()
                    self.state = 395
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 396
                self.functionCallKeywordArg()
                self.state = 401
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==35:
                    self.state = 397
                    self.match(CircuitryParser.COMMA)
                    self.state = 398
                    self.functionCallKeywordArg()
                    self.state = 403
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallKeywordArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CircuitryParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CircuitryParser.ExprContext,0)


        def getRuleIndex(self):
            return CircuitryParser.RULE_functionCallKeywordArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallKeywordArg" ):
                listener.enterFunctionCallKeywordArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallKeywordArg" ):
                listener.exitFunctionCallKeywordArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallKeywordArg" ):
                return visitor.visitFunctionCallKeywordArg(self)
            else:
                return visitor.visitChildren(self)




    def functionCallKeywordArg(self):

        localctx = CircuitryParser.FunctionCallKeywordArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_functionCallKeywordArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(CircuitryParser.ID)
            self.state = 407
            self.match(CircuitryParser.ASSIGN)
            self.state = 408
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallPositionalArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CircuitryParser.ExprContext,0)


        def getRuleIndex(self):
            return CircuitryParser.RULE_functionCallPositionalArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallPositionalArg" ):
                listener.enterFunctionCallPositionalArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallPositionalArg" ):
                listener.exitFunctionCallPositionalArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallPositionalArg" ):
                return visitor.visitFunctionCallPositionalArg(self)
            else:
                return visitor.visitChildren(self)




    def functionCallPositionalArg(self):

        localctx = CircuitryParser.FunctionCallPositionalArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_functionCallPositionalArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionWithBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(CircuitryParser.LPAREN, 0)

        def booleanExpr(self):
            return self.getTypedRuleContext(CircuitryParser.BooleanExprContext,0)


        def RPAREN(self):
            return self.getToken(CircuitryParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(CircuitryParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CircuitryParser.RBRACE, 0)

        def topologyStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.TopologyStatementContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.TopologyStatementContext,i)


        def getRuleIndex(self):
            return CircuitryParser.RULE_conditionWithBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionWithBlock" ):
                listener.enterConditionWithBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionWithBlock" ):
                listener.exitConditionWithBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionWithBlock" ):
                return visitor.visitConditionWithBlock(self)
            else:
                return visitor.visitChildren(self)




    def conditionWithBlock(self):

        localctx = CircuitryParser.ConditionWithBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_conditionWithBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(CircuitryParser.LPAREN)
            self.state = 413
            self.booleanExpr()
            self.state = 414
            self.match(CircuitryParser.RPAREN)
            self.state = 415
            self.match(CircuitryParser.LBRACE)
            self.state = 419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & 268516023) != 0):
                self.state = 416
                self.topologyStatement()
                self.state = 421
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 422
            self.match(CircuitryParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.ExprContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.ExprContext,i)


        def relationalOperator(self):
            return self.getTypedRuleContext(CircuitryParser.RelationalOperatorContext,0)


        def AND(self):
            return self.getToken(CircuitryParser.AND, 0)

        def OR(self):
            return self.getToken(CircuitryParser.OR, 0)

        def NOT(self):
            return self.getToken(CircuitryParser.NOT, 0)

        def getRuleIndex(self):
            return CircuitryParser.RULE_booleanExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanExpr" ):
                listener.enterBooleanExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanExpr" ):
                listener.exitBooleanExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanExpr" ):
                return visitor.visitBooleanExpr(self)
            else:
                return visitor.visitChildren(self)




    def booleanExpr(self):

        localctx = CircuitryParser.BooleanExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_booleanExpr)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.expr(0)
                self.state = 425
                self.relationalOperator()
                self.state = 426
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.expr(0)
                self.state = 429
                self.match(CircuitryParser.AND)
                self.state = 430
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 432
                self.expr(0)
                self.state = 433
                self.match(CircuitryParser.OR)
                self.state = 434
                self.expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 436
                self.match(CircuitryParser.NOT)
                self.state = 437
                self.expr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 438
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CircuitryParser.IF, 0)

        def LPAREN(self):
            return self.getToken(CircuitryParser.LPAREN, 0)

        def booleanExpr(self):
            return self.getTypedRuleContext(CircuitryParser.BooleanExprContext,0)


        def RPAREN(self):
            return self.getToken(CircuitryParser.RPAREN, 0)

        def topologyStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.TopologyStatementContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.TopologyStatementContext,i)


        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitryParser.LBRACE)
            else:
                return self.getToken(CircuitryParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitryParser.RBRACE)
            else:
                return self.getToken(CircuitryParser.RBRACE, i)

        def ELSE(self):
            return self.getToken(CircuitryParser.ELSE, 0)

        def getRuleIndex(self):
            return CircuitryParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = CircuitryParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(CircuitryParser.IF)
            self.state = 442
            self.match(CircuitryParser.LPAREN)
            self.state = 443
            self.booleanExpr()
            self.state = 444
            self.match(CircuitryParser.RPAREN)
            self.state = 454
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36, 37, 38, 40, 41, 43, 45, 47, 48, 49, 52, 64]:
                self.state = 445
                self.topologyStatement()
                pass
            elif token in [3]:
                self.state = 446
                self.match(CircuitryParser.LBRACE)
                self.state = 450
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & 268516023) != 0):
                    self.state = 447
                    self.topologyStatement()
                    self.state = 452
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 453
                self.match(CircuitryParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 456
                self.match(CircuitryParser.ELSE)
                self.state = 466
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [36, 37, 38, 40, 41, 43, 45, 47, 48, 49, 52, 64]:
                    self.state = 457
                    self.topologyStatement()
                    pass
                elif token in [3]:
                    self.state = 458
                    self.match(CircuitryParser.LBRACE)
                    self.state = 462
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & 268516023) != 0):
                        self.state = 459
                        self.topologyStatement()
                        self.state = 464
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 465
                    self.match(CircuitryParser.RBRACE)
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(CircuitryParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(CircuitryParser.NOT_EQUAL, 0)

        def LESS(self):
            return self.getToken(CircuitryParser.LESS, 0)

        def GREATER(self):
            return self.getToken(CircuitryParser.GREATER, 0)

        def LESS_EQUAL(self):
            return self.getToken(CircuitryParser.LESS_EQUAL, 0)

        def GREATER_EQUAL(self):
            return self.getToken(CircuitryParser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return CircuitryParser.RULE_relationalOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalOperator" ):
                listener.enterRelationalOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalOperator" ):
                listener.exitRelationalOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalOperator" ):
                return visitor.visitRelationalOperator(self)
            else:
                return visitor.visitChildren(self)




    def relationalOperator(self):

        localctx = CircuitryParser.RelationalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_relationalOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(CircuitryParser.WHILE, 0)

        def conditionWithBlock(self):
            return self.getTypedRuleContext(CircuitryParser.ConditionWithBlockContext,0)


        def getRuleIndex(self):
            return CircuitryParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = CircuitryParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(CircuitryParser.WHILE)
            self.state = 473
            self.conditionWithBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(CircuitryParser.DO, 0)

        def LBRACE(self):
            return self.getToken(CircuitryParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CircuitryParser.RBRACE, 0)

        def WHILE(self):
            return self.getToken(CircuitryParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(CircuitryParser.LPAREN, 0)

        def booleanExpr(self):
            return self.getTypedRuleContext(CircuitryParser.BooleanExprContext,0)


        def RPAREN(self):
            return self.getToken(CircuitryParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(CircuitryParser.SEMICOLON, 0)

        def topologyStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.TopologyStatementContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.TopologyStatementContext,i)


        def getRuleIndex(self):
            return CircuitryParser.RULE_doWhileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhileStatement" ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhileStatement" ):
                listener.exitDoWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoWhileStatement" ):
                return visitor.visitDoWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def doWhileStatement(self):

        localctx = CircuitryParser.DoWhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_doWhileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(CircuitryParser.DO)
            self.state = 476
            self.match(CircuitryParser.LBRACE)
            self.state = 480
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & 268516023) != 0):
                self.state = 477
                self.topologyStatement()
                self.state = 482
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 483
            self.match(CircuitryParser.RBRACE)
            self.state = 484
            self.match(CircuitryParser.WHILE)
            self.state = 485
            self.match(CircuitryParser.LPAREN)
            self.state = 486
            self.booleanExpr()
            self.state = 487
            self.match(CircuitryParser.RPAREN)
            self.state = 488
            self.match(CircuitryParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CircuitryParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(CircuitryParser.LPAREN, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitryParser.SEMICOLON)
            else:
                return self.getToken(CircuitryParser.SEMICOLON, i)

        def booleanExpr(self):
            return self.getTypedRuleContext(CircuitryParser.BooleanExprContext,0)


        def RPAREN(self):
            return self.getToken(CircuitryParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(CircuitryParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CircuitryParser.RBRACE, 0)

        def forInit(self):
            return self.getTypedRuleContext(CircuitryParser.ForInitContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(CircuitryParser.ForUpdateContext,0)


        def topologyStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.TopologyStatementContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.TopologyStatementContext,i)


        def getRuleIndex(self):
            return CircuitryParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = CircuitryParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.match(CircuitryParser.FOR)
            self.state = 491
            self.match(CircuitryParser.LPAREN)
            self.state = 493
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 492
                self.forInit()


            self.state = 495
            self.match(CircuitryParser.SEMICOLON)
            self.state = 496
            self.booleanExpr()
            self.state = 497
            self.match(CircuitryParser.SEMICOLON)
            self.state = 499
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 498
                self.forUpdate()


            self.state = 501
            self.match(CircuitryParser.RPAREN)
            self.state = 502
            self.match(CircuitryParser.LBRACE)
            self.state = 506
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & 268516023) != 0):
                self.state = 503
                self.topologyStatement()
                self.state = 508
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 509
            self.match(CircuitryParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def letAssignment(self):
            return self.getTypedRuleContext(CircuitryParser.LetAssignmentContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(CircuitryParser.AssignmentStatementContext,0)


        def getRuleIndex(self):
            return CircuitryParser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = CircuitryParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_forInit)
        try:
            self.state = 513
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.letAssignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
                self.assignmentStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(CircuitryParser.AssignmentStatementContext,0)


        def getRuleIndex(self):
            return CircuitryParser.RULE_forUpdate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForUpdate" ):
                listener.enterForUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForUpdate" ):
                listener.exitForUpdate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = CircuitryParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.assignmentStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(CircuitryParser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(CircuitryParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(CircuitryParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(CircuitryParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(CircuitryParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CircuitryParser.RBRACE, 0)

        def caseStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.CaseStatementContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.CaseStatementContext,i)


        def defaultStatement(self):
            return self.getTypedRuleContext(CircuitryParser.DefaultStatementContext,0)


        def getRuleIndex(self):
            return CircuitryParser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStatement" ):
                return visitor.visitSwitchStatement(self)
            else:
                return visitor.visitChildren(self)




    def switchStatement(self):

        localctx = CircuitryParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(CircuitryParser.SWITCH)
            self.state = 518
            self.match(CircuitryParser.LPAREN)
            self.state = 519
            self.expr(0)
            self.state = 520
            self.match(CircuitryParser.RPAREN)
            self.state = 521
            self.match(CircuitryParser.LBRACE)
            self.state = 525
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 522
                self.caseStatement()
                self.state = 527
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 529
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 528
                self.defaultStatement()


            self.state = 531
            self.match(CircuitryParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(CircuitryParser.CASE, 0)

        def expr(self):
            return self.getTypedRuleContext(CircuitryParser.ExprContext,0)


        def COLON(self):
            return self.getToken(CircuitryParser.COLON, 0)

        def topologyStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.TopologyStatementContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.TopologyStatementContext,i)


        def getRuleIndex(self):
            return CircuitryParser.RULE_caseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseStatement" ):
                listener.enterCaseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseStatement" ):
                listener.exitCaseStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseStatement" ):
                return visitor.visitCaseStatement(self)
            else:
                return visitor.visitChildren(self)




    def caseStatement(self):

        localctx = CircuitryParser.CaseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_caseStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.match(CircuitryParser.CASE)
            self.state = 534
            self.expr(0)
            self.state = 535
            self.match(CircuitryParser.COLON)
            self.state = 539
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & 268516023) != 0):
                self.state = 536
                self.topologyStatement()
                self.state = 541
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(CircuitryParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(CircuitryParser.COLON, 0)

        def topologyStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.TopologyStatementContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.TopologyStatementContext,i)


        def getRuleIndex(self):
            return CircuitryParser.RULE_defaultStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultStatement" ):
                listener.enterDefaultStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultStatement" ):
                listener.exitDefaultStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefaultStatement" ):
                return visitor.visitDefaultStatement(self)
            else:
                return visitor.visitChildren(self)




    def defaultStatement(self):

        localctx = CircuitryParser.DefaultStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_defaultStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(CircuitryParser.DEFAULT)
            self.state = 543
            self.match(CircuitryParser.COLON)
            self.state = 547
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & 268516023) != 0):
                self.state = 544
                self.topologyStatement()
                self.state = 549
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FN(self):
            return self.getToken(CircuitryParser.FN, 0)

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CircuitryParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CircuitryParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(CircuitryParser.LBRACE, 0)

        def functionBody(self):
            return self.getTypedRuleContext(CircuitryParser.FunctionBodyContext,0)


        def RBRACE(self):
            return self.getToken(CircuitryParser.RBRACE, 0)

        def functionParams(self):
            return self.getTypedRuleContext(CircuitryParser.FunctionParamsContext,0)


        def getRuleIndex(self):
            return CircuitryParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefinition" ):
                return visitor.visitFunctionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def functionDefinition(self):

        localctx = CircuitryParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.match(CircuitryParser.FN)
            self.state = 551
            self.match(CircuitryParser.ID)
            self.state = 552
            self.match(CircuitryParser.LPAREN)
            self.state = 554
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 553
                self.functionParams()


            self.state = 556
            self.match(CircuitryParser.RPAREN)
            self.state = 557
            self.match(CircuitryParser.LBRACE)
            self.state = 558
            self.functionBody()
            self.state = 559
            self.match(CircuitryParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionParam(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.FunctionParamContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.FunctionParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitryParser.COMMA)
            else:
                return self.getToken(CircuitryParser.COMMA, i)

        def getRuleIndex(self):
            return CircuitryParser.RULE_functionParams

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionParams" ):
                listener.enterFunctionParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionParams" ):
                listener.exitFunctionParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionParams" ):
                return visitor.visitFunctionParams(self)
            else:
                return visitor.visitChildren(self)




    def functionParams(self):

        localctx = CircuitryParser.FunctionParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_functionParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.functionParam()
            self.state = 566
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 562
                self.match(CircuitryParser.COMMA)
                self.state = 563
                self.functionParam()
                self.state = 568
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CircuitryParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CircuitryParser.ExprContext,0)


        def getRuleIndex(self):
            return CircuitryParser.RULE_functionParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionParam" ):
                listener.enterFunctionParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionParam" ):
                listener.exitFunctionParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionParam" ):
                return visitor.visitFunctionParam(self)
            else:
                return visitor.visitChildren(self)




    def functionParam(self):

        localctx = CircuitryParser.FunctionParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_functionParam)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(CircuitryParser.ID)
            self.state = 572
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 570
                self.match(CircuitryParser.ASSIGN)
                self.state = 571
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnStatement(self):
            return self.getTypedRuleContext(CircuitryParser.ReturnStatementContext,0)


        def topologyStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.TopologyStatementContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.TopologyStatementContext,i)


        def getRuleIndex(self):
            return CircuitryParser.RULE_functionBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionBody" ):
                listener.enterFunctionBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionBody" ):
                listener.exitFunctionBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionBody" ):
                return visitor.visitFunctionBody(self)
            else:
                return visitor.visitChildren(self)




    def functionBody(self):

        localctx = CircuitryParser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_functionBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & 268516023) != 0):
                self.state = 574
                self.topologyStatement()
                self.state = 579
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 580
            self.returnStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CircuitryParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(CircuitryParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(CircuitryParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CircuitryParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = CircuitryParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 582
            self.match(CircuitryParser.RETURN)
            self.state = 583
            self.expr(0)
            self.state = 584
            self.match(CircuitryParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubcircuitDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBCIRCUIT(self):
            return self.getToken(CircuitryParser.SUBCIRCUIT, 0)

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CircuitryParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CircuitryParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(CircuitryParser.COLON, 0)

        def nodeList(self):
            return self.getTypedRuleContext(CircuitryParser.NodeListContext,0)


        def LBRACE(self):
            return self.getToken(CircuitryParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CircuitryParser.RBRACE, 0)

        def subcircuitParams(self):
            return self.getTypedRuleContext(CircuitryParser.SubcircuitParamsContext,0)


        def topologyStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.TopologyStatementContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.TopologyStatementContext,i)


        def getRuleIndex(self):
            return CircuitryParser.RULE_subcircuitDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubcircuitDefinition" ):
                listener.enterSubcircuitDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubcircuitDefinition" ):
                listener.exitSubcircuitDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubcircuitDefinition" ):
                return visitor.visitSubcircuitDefinition(self)
            else:
                return visitor.visitChildren(self)




    def subcircuitDefinition(self):

        localctx = CircuitryParser.SubcircuitDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_subcircuitDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            self.match(CircuitryParser.SUBCIRCUIT)
            self.state = 587
            self.match(CircuitryParser.ID)
            self.state = 588
            self.match(CircuitryParser.LPAREN)
            self.state = 590
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 589
                self.subcircuitParams()


            self.state = 592
            self.match(CircuitryParser.RPAREN)
            self.state = 593
            self.match(CircuitryParser.COLON)
            self.state = 594
            self.nodeList()
            self.state = 595
            self.match(CircuitryParser.LBRACE)
            self.state = 599
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & 268516023) != 0):
                self.state = 596
                self.topologyStatement()
                self.state = 601
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 602
            self.match(CircuitryParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubcircuitParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subcircuitParam(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircuitryParser.SubcircuitParamContext)
            else:
                return self.getTypedRuleContext(CircuitryParser.SubcircuitParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitryParser.COMMA)
            else:
                return self.getToken(CircuitryParser.COMMA, i)

        def getRuleIndex(self):
            return CircuitryParser.RULE_subcircuitParams

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubcircuitParams" ):
                listener.enterSubcircuitParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubcircuitParams" ):
                listener.exitSubcircuitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubcircuitParams" ):
                return visitor.visitSubcircuitParams(self)
            else:
                return visitor.visitChildren(self)




    def subcircuitParams(self):

        localctx = CircuitryParser.SubcircuitParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_subcircuitParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.subcircuitParam()
            self.state = 609
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 605
                self.match(CircuitryParser.COMMA)
                self.state = 606
                self.subcircuitParam()
                self.state = 611
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubcircuitParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CircuitryParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CircuitryParser.ExprContext,0)


        def getRuleIndex(self):
            return CircuitryParser.RULE_subcircuitParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubcircuitParam" ):
                listener.enterSubcircuitParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubcircuitParam" ):
                listener.exitSubcircuitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubcircuitParam" ):
                return visitor.visitSubcircuitParam(self)
            else:
                return visitor.visitChildren(self)




    def subcircuitParam(self):

        localctx = CircuitryParser.SubcircuitParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_subcircuitParam)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self.match(CircuitryParser.ID)
            self.state = 615
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 613
                self.match(CircuitryParser.ASSIGN)
                self.state = 614
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimulationStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simulationType(self):
            return self.getTypedRuleContext(CircuitryParser.SimulationTypeContext,0)


        def LPAREN(self):
            return self.getToken(CircuitryParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CircuitryParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(CircuitryParser.SEMICOLON, 0)

        def functionCallArgs(self):
            return self.getTypedRuleContext(CircuitryParser.FunctionCallArgsContext,0)


        def getRuleIndex(self):
            return CircuitryParser.RULE_simulationStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimulationStatement" ):
                listener.enterSimulationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimulationStatement" ):
                listener.exitSimulationStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimulationStatement" ):
                return visitor.visitSimulationStatement(self)
            else:
                return visitor.visitChildren(self)




    def simulationStatement(self):

        localctx = CircuitryParser.SimulationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_simulationStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
            self.simulationType()
            self.state = 618
            self.match(CircuitryParser.LPAREN)
            self.state = 620
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & -2251799811537764351) != 0):
                self.state = 619
                self.functionCallArgs()


            self.state = 622
            self.match(CircuitryParser.RPAREN)
            self.state = 623
            self.match(CircuitryParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimulationTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AC(self):
            return self.getToken(CircuitryParser.AC, 0)

        def DC(self):
            return self.getToken(CircuitryParser.DC, 0)

        def TRANSIENT(self):
            return self.getToken(CircuitryParser.TRANSIENT, 0)

        def getRuleIndex(self):
            return CircuitryParser.RULE_simulationType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimulationType" ):
                listener.enterSimulationType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimulationType" ):
                listener.exitSimulationType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimulationType" ):
                return visitor.visitSimulationType(self)
            else:
                return visitor.visitChildren(self)




    def simulationType(self):

        localctx = CircuitryParser.SimulationTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_simulationType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 625
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1008806316530991104) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MeasurementStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MEASURE(self):
            return self.getToken(CircuitryParser.MEASURE, 0)

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def getRuleIndex(self):
            return CircuitryParser.RULE_measurementStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeasurementStatement" ):
                listener.enterMeasurementStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeasurementStatement" ):
                listener.exitMeasurementStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMeasurementStatement" ):
                return visitor.visitMeasurementStatement(self)
            else:
                return visitor.visitChildren(self)




    def measurementStatement(self):

        localctx = CircuitryParser.MeasurementStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_measurementStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 627
            self.match(CircuitryParser.MEASURE)
            self.state = 628
            self.match(CircuitryParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DrawingStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POS(self):
            return self.getToken(CircuitryParser.POS, 0)

        def ID(self):
            return self.getToken(CircuitryParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CircuitryParser.ASSIGN, 0)

        def LPAREN(self):
            return self.getToken(CircuitryParser.LPAREN, 0)

        def FLOAT_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(CircuitryParser.FLOAT_LITERAL)
            else:
                return self.getToken(CircuitryParser.FLOAT_LITERAL, i)

        def COMMA(self):
            return self.getToken(CircuitryParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(CircuitryParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(CircuitryParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CircuitryParser.RULE_drawingStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawingStatement" ):
                listener.enterDrawingStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawingStatement" ):
                listener.exitDrawingStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrawingStatement" ):
                return visitor.visitDrawingStatement(self)
            else:
                return visitor.visitChildren(self)




    def drawingStatement(self):

        localctx = CircuitryParser.DrawingStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_drawingStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 630
            self.match(CircuitryParser.POS)
            self.state = 631
            self.match(CircuitryParser.ID)
            self.state = 632
            self.match(CircuitryParser.ASSIGN)
            self.state = 633
            self.match(CircuitryParser.LPAREN)
            self.state = 634
            self.match(CircuitryParser.FLOAT_LITERAL)
            self.state = 635
            self.match(CircuitryParser.COMMA)
            self.state = 636
            self.match(CircuitryParser.FLOAT_LITERAL)
            self.state = 637
            self.match(CircuitryParser.RPAREN)
            self.state = 638
            self.match(CircuitryParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[25] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 9)
         




