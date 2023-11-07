# Generated from resources\parserGrammar\PythonLexer.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


if "." in __name__:
    from .PythonLexerBase import PythonLexerBase
else:
    from PythonLexerBase import PythonLexerBase

def serializedATN():
    return [
        4,0,113,910,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,
        84,2,85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,
        91,7,91,2,92,7,92,2,93,7,93,2,94,7,94,2,95,7,95,2,96,7,96,2,97,7,
        97,2,98,7,98,2,99,7,99,2,100,7,100,2,101,7,101,2,102,7,102,2,103,
        7,103,2,104,7,104,2,105,7,105,2,106,7,106,2,107,7,107,2,108,7,108,
        2,109,7,109,2,110,7,110,2,111,7,111,2,112,7,112,2,113,7,113,2,114,
        7,114,2,115,7,115,2,116,7,116,2,117,7,117,2,118,7,118,2,119,7,119,
        2,120,7,120,2,121,7,121,2,122,7,122,2,123,7,123,2,124,7,124,1,0,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,
        1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,24,
        1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,
        1,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,31,
        1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,
        1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,
        1,35,1,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,38,1,38,1,38,
        1,39,1,39,1,39,1,40,1,40,1,40,1,41,1,41,1,42,1,42,1,42,1,42,1,42,
        1,42,1,42,1,42,1,43,1,43,1,44,1,44,1,44,1,44,1,44,1,45,1,45,1,46,
        1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,50,1,50,1,51,1,51,1,51,1,51,
        1,52,1,52,1,53,1,53,1,54,1,54,1,55,1,55,1,56,1,56,1,57,1,57,1,57,
        1,58,1,58,1,59,1,59,1,60,1,60,1,61,1,61,1,62,1,62,1,62,1,63,1,63,
        1,63,1,64,1,64,1,65,1,65,1,66,1,66,1,67,1,67,1,68,1,68,1,68,1,69,
        1,69,1,70,1,70,1,71,1,71,1,72,1,72,1,72,1,73,1,73,1,73,1,74,1,74,
        1,74,1,75,1,75,1,75,1,76,1,76,1,76,1,77,1,77,1,78,1,78,1,78,1,79,
        1,79,1,79,1,80,1,80,1,80,1,81,1,81,1,81,1,82,1,82,1,82,1,83,1,83,
        1,83,1,84,1,84,1,84,1,85,1,85,1,85,1,86,1,86,1,86,1,87,1,87,1,87,
        1,88,1,88,1,88,1,88,1,89,1,89,1,89,1,89,1,90,1,90,1,90,1,90,1,91,
        1,91,1,91,1,91,1,92,1,92,1,92,3,92,608,8,92,1,92,1,92,3,92,612,8,
        92,3,92,614,8,92,1,92,1,92,3,92,618,8,92,1,92,1,92,3,92,622,8,92,
        1,92,1,92,3,92,626,8,92,1,92,1,92,3,92,630,8,92,3,92,632,8,92,1,
        93,1,93,5,93,636,8,93,10,93,12,93,639,9,93,1,93,4,93,642,8,93,11,
        93,12,93,643,3,93,646,8,93,1,94,1,94,1,94,4,94,651,8,94,11,94,12,
        94,652,1,95,1,95,1,95,4,95,658,8,95,11,95,12,95,659,1,96,1,96,1,
        96,4,96,665,8,96,11,96,12,96,666,1,97,1,97,4,97,671,8,97,11,97,12,
        97,672,3,97,675,8,97,1,97,1,97,1,98,1,98,1,99,1,99,1,100,1,100,1,
        101,1,101,1,102,1,102,1,103,1,103,1,104,1,104,1,105,1,105,5,105,
        695,8,105,10,105,12,105,698,9,105,1,106,1,106,5,106,702,8,106,10,
        106,12,106,705,9,106,1,106,1,106,1,106,1,106,1,107,1,107,1,107,1,
        107,1,108,4,108,716,8,108,11,108,12,108,717,1,108,1,108,1,109,1,
        109,5,109,724,8,109,10,109,12,109,727,9,109,1,109,1,109,1,110,1,
        110,1,110,1,110,3,110,735,8,110,1,110,5,110,738,8,110,10,110,12,
        110,741,9,110,1,110,1,110,1,110,1,110,1,110,3,110,748,8,110,1,110,
        5,110,751,8,110,10,110,12,110,754,9,110,1,110,3,110,757,8,110,1,
        111,1,111,1,111,1,111,1,111,5,111,764,8,111,10,111,12,111,767,9,
        111,1,111,1,111,1,111,1,111,1,111,1,111,1,111,1,111,5,111,777,8,
        111,10,111,12,111,780,9,111,1,111,1,111,1,111,3,111,785,8,111,1,
        112,1,112,1,112,1,112,3,112,791,8,112,3,112,793,8,112,1,113,3,113,
        796,8,113,1,113,1,113,1,114,4,114,801,8,114,11,114,12,114,802,1,
        114,3,114,806,8,114,1,114,1,114,3,114,810,8,114,1,114,4,114,813,
        8,114,11,114,12,114,814,1,114,3,114,818,8,114,1,115,5,115,821,8,
        115,10,115,12,115,824,9,115,1,115,1,115,4,115,828,8,115,11,115,12,
        115,829,1,115,4,115,833,8,115,11,115,12,115,834,1,115,3,115,838,
        8,115,1,116,1,116,1,116,5,116,843,8,116,10,116,12,116,846,9,116,
        1,116,1,116,1,116,1,116,5,116,852,8,116,10,116,12,116,855,9,116,
        1,116,3,116,858,8,116,1,117,1,117,1,117,1,117,1,117,5,117,865,8,
        117,10,117,12,117,868,9,117,1,117,1,117,1,117,1,117,1,117,1,117,
        1,117,1,117,5,117,878,8,117,10,117,12,117,881,9,117,1,117,1,117,
        1,117,3,117,886,8,117,1,118,1,118,3,118,890,8,118,1,119,3,119,893,
        8,119,1,120,3,120,896,8,120,1,121,3,121,899,8,121,1,122,1,122,1,
        122,1,123,1,123,3,123,906,8,123,1,124,3,124,909,8,124,4,765,778,
        866,879,0,125,1,4,3,5,5,6,7,7,9,8,11,9,13,10,15,11,17,12,19,13,21,
        14,23,15,25,16,27,17,29,18,31,19,33,20,35,21,37,22,39,23,41,24,43,
        25,45,26,47,27,49,28,51,29,53,30,55,31,57,32,59,33,61,34,63,35,65,
        36,67,37,69,38,71,39,73,40,75,41,77,42,79,43,81,44,83,45,85,46,87,
        47,89,48,91,49,93,50,95,51,97,52,99,53,101,54,103,55,105,56,107,
        57,109,58,111,59,113,60,115,61,117,62,119,63,121,64,123,65,125,66,
        127,67,129,68,131,69,133,70,135,71,137,72,139,73,141,74,143,75,145,
        76,147,77,149,78,151,79,153,80,155,81,157,82,159,83,161,84,163,85,
        165,86,167,87,169,88,171,89,173,90,175,91,177,92,179,93,181,94,183,
        95,185,96,187,97,189,98,191,99,193,100,195,101,197,102,199,103,201,
        104,203,105,205,106,207,107,209,108,211,109,213,110,215,111,217,
        112,219,113,221,0,223,0,225,0,227,0,229,0,231,0,233,0,235,0,237,
        0,239,0,241,0,243,0,245,0,247,0,249,0,1,0,25,2,0,85,85,117,117,2,
        0,70,70,102,102,2,0,82,82,114,114,2,0,66,66,98,98,1,0,49,57,1,0,
        48,57,2,0,79,79,111,111,1,0,48,55,2,0,88,88,120,120,3,0,48,57,65,
        70,97,102,1,0,48,49,2,0,74,74,106,106,2,0,9,9,32,32,2,0,10,10,12,
        13,4,0,10,10,13,13,39,39,92,92,4,0,10,10,13,13,34,34,92,92,1,0,92,
        92,2,0,69,69,101,101,2,0,43,43,45,45,5,0,0,9,11,12,14,38,40,91,93,
        127,5,0,0,9,11,12,14,33,35,91,93,127,2,0,0,91,93,127,1,0,0,127,148,
        0,48,57,768,879,1155,1158,1425,1465,1467,1469,1471,1471,1473,1474,
        1476,1477,1479,1479,1552,1557,1611,1630,1632,1641,1648,1648,1750,
        1756,1759,1764,1767,1768,1770,1773,1776,1785,1809,1809,1840,1866,
        1958,1968,2305,2307,2364,2364,2366,2381,2385,2388,2402,2403,2406,
        2415,2433,2435,2492,2492,2494,2500,2503,2504,2507,2509,2519,2519,
        2530,2531,2534,2543,2561,2563,2620,2620,2622,2626,2631,2632,2635,
        2637,2662,2673,2689,2691,2748,2748,2750,2757,2759,2761,2763,2765,
        2786,2787,2790,2799,2817,2819,2876,2876,2878,2883,2887,2888,2891,
        2893,2902,2903,2918,2927,2946,2946,3006,3010,3014,3016,3018,3021,
        3031,3031,3046,3055,3073,3075,3134,3140,3142,3144,3146,3149,3157,
        3158,3174,3183,3202,3203,3260,3260,3262,3268,3270,3272,3274,3277,
        3285,3286,3302,3311,3330,3331,3390,3395,3398,3400,3402,3405,3415,
        3415,3430,3439,3458,3459,3530,3530,3535,3540,3542,3542,3544,3551,
        3570,3571,3633,3633,3636,3642,3655,3662,3664,3673,3761,3761,3764,
        3769,3771,3772,3784,3789,3792,3801,3864,3865,3872,3881,3893,3893,
        3895,3895,3897,3897,3902,3903,3953,3972,3974,3975,3984,3991,3993,
        4028,4038,4038,4140,4146,4150,4153,4160,4169,4182,4185,4959,4959,
        4969,4977,5906,5908,5938,5940,5970,5971,6002,6003,6070,6099,6109,
        6109,6112,6121,6155,6157,6160,6169,6313,6313,6432,6443,6448,6459,
        6470,6479,6576,6592,6600,6601,6608,6617,6679,6683,7616,7619,8255,
        8256,8276,8276,8400,8412,8417,8417,8421,8427,12330,12335,12441,12442,
        43010,43010,43014,43014,43019,43019,43043,43047,64286,64286,65024,
        65039,65056,65059,65075,65076,65101,65103,65296,65305,65343,65343,
        295,0,65,90,95,95,97,122,170,170,181,181,186,186,192,214,216,246,
        248,577,592,705,710,721,736,740,750,750,890,890,902,902,904,906,
        908,908,910,929,931,974,976,1013,1015,1153,1162,1230,1232,1273,1280,
        1295,1329,1366,1369,1369,1377,1415,1488,1514,1520,1522,1569,1594,
        1600,1610,1646,1647,1649,1747,1749,1749,1765,1766,1774,1775,1786,
        1788,1791,1791,1808,1808,1810,1839,1869,1901,1920,1957,1969,1969,
        2308,2361,2365,2365,2384,2384,2392,2401,2429,2429,2437,2444,2447,
        2448,2451,2472,2474,2480,2482,2482,2486,2489,2493,2493,2510,2510,
        2524,2525,2527,2529,2544,2545,2565,2570,2575,2576,2579,2600,2602,
        2608,2610,2611,2613,2614,2616,2617,2649,2652,2654,2654,2674,2676,
        2693,2701,2703,2705,2707,2728,2730,2736,2738,2739,2741,2745,2749,
        2749,2768,2768,2784,2785,2821,2828,2831,2832,2835,2856,2858,2864,
        2866,2867,2869,2873,2877,2877,2908,2909,2911,2913,2929,2929,2947,
        2947,2949,2954,2958,2960,2962,2965,2969,2970,2972,2972,2974,2975,
        2979,2980,2984,2986,2990,3001,3077,3084,3086,3088,3090,3112,3114,
        3123,3125,3129,3168,3169,3205,3212,3214,3216,3218,3240,3242,3251,
        3253,3257,3261,3261,3294,3294,3296,3297,3333,3340,3342,3344,3346,
        3368,3370,3385,3424,3425,3461,3478,3482,3505,3507,3515,3517,3517,
        3520,3526,3585,3632,3634,3635,3648,3654,3713,3714,3716,3716,3719,
        3720,3722,3722,3725,3725,3732,3735,3737,3743,3745,3747,3749,3749,
        3751,3751,3754,3755,3757,3760,3762,3763,3773,3773,3776,3780,3782,
        3782,3804,3805,3840,3840,3904,3911,3913,3946,3976,3979,4096,4129,
        4131,4135,4137,4138,4176,4181,4256,4293,4304,4346,4348,4348,4352,
        4441,4447,4514,4520,4601,4608,4680,4682,4685,4688,4694,4696,4696,
        4698,4701,4704,4744,4746,4749,4752,4784,4786,4789,4792,4798,4800,
        4800,4802,4805,4808,4822,4824,4880,4882,4885,4888,4954,4992,5007,
        5024,5108,5121,5740,5743,5750,5761,5786,5792,5866,5870,5872,5888,
        5900,5902,5905,5920,5937,5952,5969,5984,5996,5998,6000,6016,6067,
        6103,6103,6108,6108,6176,6263,6272,6312,6400,6428,6480,6509,6512,
        6516,6528,6569,6593,6599,6656,6678,7424,7615,7680,7835,7840,7929,
        7936,7957,7960,7965,7968,8005,8008,8013,8016,8023,8025,8025,8027,
        8027,8029,8029,8031,8061,8064,8116,8118,8124,8126,8126,8130,8132,
        8134,8140,8144,8147,8150,8155,8160,8172,8178,8180,8182,8188,8305,
        8305,8319,8319,8336,8340,8450,8450,8455,8455,8458,8467,8469,8469,
        8472,8477,8484,8484,8486,8486,8488,8488,8490,8497,8499,8505,8508,
        8511,8517,8521,8544,8579,11264,11310,11312,11358,11392,11492,11520,
        11557,11568,11621,11631,11631,11648,11670,11680,11686,11688,11694,
        11696,11702,11704,11710,11712,11718,11720,11726,11728,11734,11736,
        11742,12293,12295,12321,12329,12337,12341,12344,12348,12353,12438,
        12443,12447,12449,12538,12540,12543,12549,12588,12593,12686,12704,
        12727,12784,12799,13312,19893,19968,40891,40960,42124,43008,43009,
        43011,43013,43015,43018,43020,43042,44032,55203,63744,64045,64048,
        64106,64112,64217,64256,64262,64275,64279,64285,64285,64287,64296,
        64298,64310,64312,64316,64318,64318,64320,64321,64323,64324,64326,
        64433,64467,64829,64848,64911,64914,64967,65008,65019,65136,65140,
        65142,65276,65313,65338,65345,65370,65382,65470,65474,65479,65482,
        65487,65490,65495,65498,65500,948,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,
        0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,
        0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,
        0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,
        0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,
        0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,
        0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,
        0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,
        0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,
        0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,
        1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,
        0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,
        0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,0,
        133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,0,139,1,0,0,0,0,141,1,0,
        0,0,0,143,1,0,0,0,0,145,1,0,0,0,0,147,1,0,0,0,0,149,1,0,0,0,0,151,
        1,0,0,0,0,153,1,0,0,0,0,155,1,0,0,0,0,157,1,0,0,0,0,159,1,0,0,0,
        0,161,1,0,0,0,0,163,1,0,0,0,0,165,1,0,0,0,0,167,1,0,0,0,0,169,1,
        0,0,0,0,171,1,0,0,0,0,173,1,0,0,0,0,175,1,0,0,0,0,177,1,0,0,0,0,
        179,1,0,0,0,0,181,1,0,0,0,0,183,1,0,0,0,0,185,1,0,0,0,0,187,1,0,
        0,0,0,189,1,0,0,0,0,191,1,0,0,0,0,193,1,0,0,0,0,195,1,0,0,0,0,197,
        1,0,0,0,0,199,1,0,0,0,0,201,1,0,0,0,0,203,1,0,0,0,0,205,1,0,0,0,
        0,207,1,0,0,0,0,209,1,0,0,0,0,211,1,0,0,0,0,213,1,0,0,0,0,215,1,
        0,0,0,0,217,1,0,0,0,0,219,1,0,0,0,1,251,1,0,0,0,3,255,1,0,0,0,5,
        262,1,0,0,0,7,268,1,0,0,0,9,273,1,0,0,0,11,280,1,0,0,0,13,289,1,
        0,0,0,15,292,1,0,0,0,17,299,1,0,0,0,19,306,1,0,0,0,21,309,1,0,0,
        0,23,314,1,0,0,0,25,319,1,0,0,0,27,325,1,0,0,0,29,329,1,0,0,0,31,
        332,1,0,0,0,33,336,1,0,0,0,35,341,1,0,0,0,37,349,1,0,0,0,39,354,
        1,0,0,0,41,361,1,0,0,0,43,368,1,0,0,0,45,371,1,0,0,0,47,375,1,0,
        0,0,49,379,1,0,0,0,51,382,1,0,0,0,53,388,1,0,0,0,55,394,1,0,0,0,
        57,398,1,0,0,0,59,403,1,0,0,0,61,412,1,0,0,0,63,418,1,0,0,0,65,424,
        1,0,0,0,67,430,1,0,0,0,69,436,1,0,0,0,71,441,1,0,0,0,73,446,1,0,
        0,0,75,452,1,0,0,0,77,455,1,0,0,0,79,458,1,0,0,0,81,461,1,0,0,0,
        83,464,1,0,0,0,85,466,1,0,0,0,87,474,1,0,0,0,89,476,1,0,0,0,91,481,
        1,0,0,0,93,483,1,0,0,0,95,485,1,0,0,0,97,487,1,0,0,0,99,489,1,0,
        0,0,101,491,1,0,0,0,103,493,1,0,0,0,105,497,1,0,0,0,107,499,1,0,
        0,0,109,501,1,0,0,0,111,503,1,0,0,0,113,505,1,0,0,0,115,507,1,0,
        0,0,117,510,1,0,0,0,119,512,1,0,0,0,121,514,1,0,0,0,123,516,1,0,
        0,0,125,518,1,0,0,0,127,521,1,0,0,0,129,524,1,0,0,0,131,526,1,0,
        0,0,133,528,1,0,0,0,135,530,1,0,0,0,137,532,1,0,0,0,139,535,1,0,
        0,0,141,537,1,0,0,0,143,539,1,0,0,0,145,541,1,0,0,0,147,544,1,0,
        0,0,149,547,1,0,0,0,151,550,1,0,0,0,153,553,1,0,0,0,155,556,1,0,
        0,0,157,558,1,0,0,0,159,561,1,0,0,0,161,564,1,0,0,0,163,567,1,0,
        0,0,165,570,1,0,0,0,167,573,1,0,0,0,169,576,1,0,0,0,171,579,1,0,
        0,0,173,582,1,0,0,0,175,585,1,0,0,0,177,588,1,0,0,0,179,592,1,0,
        0,0,181,596,1,0,0,0,183,600,1,0,0,0,185,631,1,0,0,0,187,645,1,0,
        0,0,189,647,1,0,0,0,191,654,1,0,0,0,193,661,1,0,0,0,195,674,1,0,
        0,0,197,678,1,0,0,0,199,680,1,0,0,0,201,682,1,0,0,0,203,684,1,0,
        0,0,205,686,1,0,0,0,207,688,1,0,0,0,209,690,1,0,0,0,211,692,1,0,
        0,0,213,699,1,0,0,0,215,710,1,0,0,0,217,715,1,0,0,0,219,721,1,0,
        0,0,221,756,1,0,0,0,223,784,1,0,0,0,225,792,1,0,0,0,227,795,1,0,
        0,0,229,817,1,0,0,0,231,837,1,0,0,0,233,857,1,0,0,0,235,885,1,0,
        0,0,237,889,1,0,0,0,239,892,1,0,0,0,241,895,1,0,0,0,243,898,1,0,
        0,0,245,900,1,0,0,0,247,905,1,0,0,0,249,908,1,0,0,0,251,252,5,100,
        0,0,252,253,5,101,0,0,253,254,5,102,0,0,254,2,1,0,0,0,255,256,5,
        114,0,0,256,257,5,101,0,0,257,258,5,116,0,0,258,259,5,117,0,0,259,
        260,5,114,0,0,260,261,5,110,0,0,261,4,1,0,0,0,262,263,5,114,0,0,
        263,264,5,97,0,0,264,265,5,105,0,0,265,266,5,115,0,0,266,267,5,101,
        0,0,267,6,1,0,0,0,268,269,5,102,0,0,269,270,5,114,0,0,270,271,5,
        111,0,0,271,272,5,109,0,0,272,8,1,0,0,0,273,274,5,105,0,0,274,275,
        5,109,0,0,275,276,5,112,0,0,276,277,5,111,0,0,277,278,5,114,0,0,
        278,279,5,116,0,0,279,10,1,0,0,0,280,281,5,110,0,0,281,282,5,111,
        0,0,282,283,5,110,0,0,283,284,5,108,0,0,284,285,5,111,0,0,285,286,
        5,99,0,0,286,287,5,97,0,0,287,288,5,108,0,0,288,12,1,0,0,0,289,290,
        5,97,0,0,290,291,5,115,0,0,291,14,1,0,0,0,292,293,5,103,0,0,293,
        294,5,108,0,0,294,295,5,111,0,0,295,296,5,98,0,0,296,297,5,97,0,
        0,297,298,5,108,0,0,298,16,1,0,0,0,299,300,5,97,0,0,300,301,5,115,
        0,0,301,302,5,115,0,0,302,303,5,101,0,0,303,304,5,114,0,0,304,305,
        5,116,0,0,305,18,1,0,0,0,306,307,5,105,0,0,307,308,5,102,0,0,308,
        20,1,0,0,0,309,310,5,101,0,0,310,311,5,108,0,0,311,312,5,105,0,0,
        312,313,5,102,0,0,313,22,1,0,0,0,314,315,5,101,0,0,315,316,5,108,
        0,0,316,317,5,115,0,0,317,318,5,101,0,0,318,24,1,0,0,0,319,320,5,
        119,0,0,320,321,5,104,0,0,321,322,5,105,0,0,322,323,5,108,0,0,323,
        324,5,101,0,0,324,26,1,0,0,0,325,326,5,102,0,0,326,327,5,111,0,0,
        327,328,5,114,0,0,328,28,1,0,0,0,329,330,5,105,0,0,330,331,5,110,
        0,0,331,30,1,0,0,0,332,333,5,116,0,0,333,334,5,114,0,0,334,335,5,
        121,0,0,335,32,1,0,0,0,336,337,5,78,0,0,337,338,5,111,0,0,338,339,
        5,110,0,0,339,340,5,101,0,0,340,34,1,0,0,0,341,342,5,102,0,0,342,
        343,5,105,0,0,343,344,5,110,0,0,344,345,5,97,0,0,345,346,5,108,0,
        0,346,347,5,108,0,0,347,348,5,121,0,0,348,36,1,0,0,0,349,350,5,119,
        0,0,350,351,5,105,0,0,351,352,5,116,0,0,352,353,5,104,0,0,353,38,
        1,0,0,0,354,355,5,101,0,0,355,356,5,120,0,0,356,357,5,99,0,0,357,
        358,5,101,0,0,358,359,5,112,0,0,359,360,5,116,0,0,360,40,1,0,0,0,
        361,362,5,108,0,0,362,363,5,97,0,0,363,364,5,109,0,0,364,365,5,98,
        0,0,365,366,5,100,0,0,366,367,5,97,0,0,367,42,1,0,0,0,368,369,5,
        111,0,0,369,370,5,114,0,0,370,44,1,0,0,0,371,372,5,97,0,0,372,373,
        5,110,0,0,373,374,5,100,0,0,374,46,1,0,0,0,375,376,5,110,0,0,376,
        377,5,111,0,0,377,378,5,116,0,0,378,48,1,0,0,0,379,380,5,105,0,0,
        380,381,5,115,0,0,381,50,1,0,0,0,382,383,5,99,0,0,383,384,5,108,
        0,0,384,385,5,97,0,0,385,386,5,115,0,0,386,387,5,115,0,0,387,52,
        1,0,0,0,388,389,5,121,0,0,389,390,5,105,0,0,390,391,5,101,0,0,391,
        392,5,108,0,0,392,393,5,100,0,0,393,54,1,0,0,0,394,395,5,100,0,0,
        395,396,5,101,0,0,396,397,5,108,0,0,397,56,1,0,0,0,398,399,5,112,
        0,0,399,400,5,97,0,0,400,401,5,115,0,0,401,402,5,115,0,0,402,58,
        1,0,0,0,403,404,5,99,0,0,404,405,5,111,0,0,405,406,5,110,0,0,406,
        407,5,116,0,0,407,408,5,105,0,0,408,409,5,110,0,0,409,410,5,117,
        0,0,410,411,5,101,0,0,411,60,1,0,0,0,412,413,5,98,0,0,413,414,5,
        114,0,0,414,415,5,101,0,0,415,416,5,97,0,0,416,417,5,107,0,0,417,
        62,1,0,0,0,418,419,5,97,0,0,419,420,5,115,0,0,420,421,5,121,0,0,
        421,422,5,110,0,0,422,423,5,99,0,0,423,64,1,0,0,0,424,425,5,97,0,
        0,425,426,5,119,0,0,426,427,5,97,0,0,427,428,5,105,0,0,428,429,5,
        116,0,0,429,66,1,0,0,0,430,431,5,112,0,0,431,432,5,114,0,0,432,433,
        5,105,0,0,433,434,5,110,0,0,434,435,5,116,0,0,435,68,1,0,0,0,436,
        437,5,101,0,0,437,438,5,120,0,0,438,439,5,101,0,0,439,440,5,99,0,
        0,440,70,1,0,0,0,441,442,5,84,0,0,442,443,5,114,0,0,443,444,5,117,
        0,0,444,445,5,101,0,0,445,72,1,0,0,0,446,447,5,70,0,0,447,448,5,
        97,0,0,448,449,5,108,0,0,449,450,5,115,0,0,450,451,5,101,0,0,451,
        74,1,0,0,0,452,453,5,99,0,0,453,454,5,104,0,0,454,76,1,0,0,0,455,
        456,5,99,0,0,456,457,5,117,0,0,457,78,1,0,0,0,458,459,5,99,0,0,459,
        460,5,120,0,0,460,80,1,0,0,0,461,462,5,99,0,0,462,463,5,122,0,0,
        463,82,1,0,0,0,464,465,5,104,0,0,465,84,1,0,0,0,466,467,5,109,0,
        0,467,468,5,101,0,0,468,469,5,97,0,0,469,470,5,115,0,0,470,471,5,
        117,0,0,471,472,5,114,0,0,472,473,5,101,0,0,473,86,1,0,0,0,474,475,
        5,117,0,0,475,88,1,0,0,0,476,477,5,115,0,0,477,478,5,119,0,0,478,
        479,5,97,0,0,479,480,5,112,0,0,480,90,1,0,0,0,481,482,5,115,0,0,
        482,92,1,0,0,0,483,484,5,116,0,0,484,94,1,0,0,0,485,486,5,120,0,
        0,486,96,1,0,0,0,487,488,5,121,0,0,488,98,1,0,0,0,489,490,5,122,
        0,0,490,100,1,0,0,0,491,492,5,46,0,0,492,102,1,0,0,0,493,494,5,46,
        0,0,494,495,5,46,0,0,495,496,5,46,0,0,496,104,1,0,0,0,497,498,5,
        96,0,0,498,106,1,0,0,0,499,500,5,42,0,0,500,108,1,0,0,0,501,502,
        5,44,0,0,502,110,1,0,0,0,503,504,5,58,0,0,504,112,1,0,0,0,505,506,
        5,59,0,0,506,114,1,0,0,0,507,508,5,42,0,0,508,509,5,42,0,0,509,116,
        1,0,0,0,510,511,5,61,0,0,511,118,1,0,0,0,512,513,5,124,0,0,513,120,
        1,0,0,0,514,515,5,94,0,0,515,122,1,0,0,0,516,517,5,38,0,0,517,124,
        1,0,0,0,518,519,5,60,0,0,519,520,5,60,0,0,520,126,1,0,0,0,521,522,
        5,62,0,0,522,523,5,62,0,0,523,128,1,0,0,0,524,525,5,43,0,0,525,130,
        1,0,0,0,526,527,5,45,0,0,527,132,1,0,0,0,528,529,5,47,0,0,529,134,
        1,0,0,0,530,531,5,37,0,0,531,136,1,0,0,0,532,533,5,47,0,0,533,534,
        5,47,0,0,534,138,1,0,0,0,535,536,5,126,0,0,536,140,1,0,0,0,537,538,
        5,60,0,0,538,142,1,0,0,0,539,540,5,62,0,0,540,144,1,0,0,0,541,542,
        5,61,0,0,542,543,5,61,0,0,543,146,1,0,0,0,544,545,5,62,0,0,545,546,
        5,61,0,0,546,148,1,0,0,0,547,548,5,60,0,0,548,549,5,61,0,0,549,150,
        1,0,0,0,550,551,5,60,0,0,551,552,5,62,0,0,552,152,1,0,0,0,553,554,
        5,33,0,0,554,555,5,61,0,0,555,154,1,0,0,0,556,557,5,64,0,0,557,156,
        1,0,0,0,558,559,5,45,0,0,559,560,5,62,0,0,560,158,1,0,0,0,561,562,
        5,43,0,0,562,563,5,61,0,0,563,160,1,0,0,0,564,565,5,45,0,0,565,566,
        5,61,0,0,566,162,1,0,0,0,567,568,5,42,0,0,568,569,5,61,0,0,569,164,
        1,0,0,0,570,571,5,64,0,0,571,572,5,61,0,0,572,166,1,0,0,0,573,574,
        5,47,0,0,574,575,5,61,0,0,575,168,1,0,0,0,576,577,5,37,0,0,577,578,
        5,61,0,0,578,170,1,0,0,0,579,580,5,38,0,0,580,581,5,61,0,0,581,172,
        1,0,0,0,582,583,5,124,0,0,583,584,5,61,0,0,584,174,1,0,0,0,585,586,
        5,94,0,0,586,587,5,61,0,0,587,176,1,0,0,0,588,589,5,60,0,0,589,590,
        5,60,0,0,590,591,5,61,0,0,591,178,1,0,0,0,592,593,5,62,0,0,593,594,
        5,62,0,0,594,595,5,61,0,0,595,180,1,0,0,0,596,597,5,42,0,0,597,598,
        5,42,0,0,598,599,5,61,0,0,599,182,1,0,0,0,600,601,5,47,0,0,601,602,
        5,47,0,0,602,603,5,61,0,0,603,184,1,0,0,0,604,614,7,0,0,0,605,607,
        7,1,0,0,606,608,7,2,0,0,607,606,1,0,0,0,607,608,1,0,0,0,608,614,
        1,0,0,0,609,611,7,2,0,0,610,612,7,1,0,0,611,610,1,0,0,0,611,612,
        1,0,0,0,612,614,1,0,0,0,613,604,1,0,0,0,613,605,1,0,0,0,613,609,
        1,0,0,0,613,614,1,0,0,0,614,617,1,0,0,0,615,618,3,221,110,0,616,
        618,3,223,111,0,617,615,1,0,0,0,617,616,1,0,0,0,618,632,1,0,0,0,
        619,621,7,3,0,0,620,622,7,2,0,0,621,620,1,0,0,0,621,622,1,0,0,0,
        622,626,1,0,0,0,623,624,7,2,0,0,624,626,7,3,0,0,625,619,1,0,0,0,
        625,623,1,0,0,0,626,629,1,0,0,0,627,630,3,233,116,0,628,630,3,235,
        117,0,629,627,1,0,0,0,629,628,1,0,0,0,630,632,1,0,0,0,631,613,1,
        0,0,0,631,625,1,0,0,0,632,186,1,0,0,0,633,637,7,4,0,0,634,636,7,
        5,0,0,635,634,1,0,0,0,636,639,1,0,0,0,637,635,1,0,0,0,637,638,1,
        0,0,0,638,646,1,0,0,0,639,637,1,0,0,0,640,642,5,48,0,0,641,640,1,
        0,0,0,642,643,1,0,0,0,643,641,1,0,0,0,643,644,1,0,0,0,644,646,1,
        0,0,0,645,633,1,0,0,0,645,641,1,0,0,0,646,188,1,0,0,0,647,648,5,
        48,0,0,648,650,7,6,0,0,649,651,7,7,0,0,650,649,1,0,0,0,651,652,1,
        0,0,0,652,650,1,0,0,0,652,653,1,0,0,0,653,190,1,0,0,0,654,655,5,
        48,0,0,655,657,7,8,0,0,656,658,7,9,0,0,657,656,1,0,0,0,658,659,1,
        0,0,0,659,657,1,0,0,0,659,660,1,0,0,0,660,192,1,0,0,0,661,662,5,
        48,0,0,662,664,7,3,0,0,663,665,7,10,0,0,664,663,1,0,0,0,665,666,
        1,0,0,0,666,664,1,0,0,0,666,667,1,0,0,0,667,194,1,0,0,0,668,675,
        3,229,114,0,669,671,7,5,0,0,670,669,1,0,0,0,671,672,1,0,0,0,672,
        670,1,0,0,0,672,673,1,0,0,0,673,675,1,0,0,0,674,668,1,0,0,0,674,
        670,1,0,0,0,675,676,1,0,0,0,676,677,7,11,0,0,677,196,1,0,0,0,678,
        679,3,229,114,0,679,198,1,0,0,0,680,681,5,40,0,0,681,200,1,0,0,0,
        682,683,5,41,0,0,683,202,1,0,0,0,684,685,5,123,0,0,685,204,1,0,0,
        0,686,687,5,125,0,0,687,206,1,0,0,0,688,689,5,91,0,0,689,208,1,0,
        0,0,690,691,5,93,0,0,691,210,1,0,0,0,692,696,3,249,124,0,693,695,
        3,247,123,0,694,693,1,0,0,0,695,698,1,0,0,0,696,694,1,0,0,0,696,
        697,1,0,0,0,697,212,1,0,0,0,698,696,1,0,0,0,699,703,5,92,0,0,700,
        702,7,12,0,0,701,700,1,0,0,0,702,705,1,0,0,0,703,701,1,0,0,0,703,
        704,1,0,0,0,704,706,1,0,0,0,705,703,1,0,0,0,706,707,3,227,113,0,
        707,708,1,0,0,0,708,709,6,106,0,0,709,214,1,0,0,0,710,711,3,227,
        113,0,711,712,1,0,0,0,712,713,6,107,0,0,713,216,1,0,0,0,714,716,
        7,12,0,0,715,714,1,0,0,0,716,717,1,0,0,0,717,715,1,0,0,0,717,718,
        1,0,0,0,718,719,1,0,0,0,719,720,6,108,0,0,720,218,1,0,0,0,721,725,
        5,35,0,0,722,724,8,13,0,0,723,722,1,0,0,0,724,727,1,0,0,0,725,723,
        1,0,0,0,725,726,1,0,0,0,726,728,1,0,0,0,727,725,1,0,0,0,728,729,
        6,109,0,0,729,220,1,0,0,0,730,739,5,39,0,0,731,734,5,92,0,0,732,
        735,3,227,113,0,733,735,9,0,0,0,734,732,1,0,0,0,734,733,1,0,0,0,
        735,738,1,0,0,0,736,738,8,14,0,0,737,731,1,0,0,0,737,736,1,0,0,0,
        738,741,1,0,0,0,739,737,1,0,0,0,739,740,1,0,0,0,740,742,1,0,0,0,
        741,739,1,0,0,0,742,757,5,39,0,0,743,752,5,34,0,0,744,747,5,92,0,
        0,745,748,3,227,113,0,746,748,9,0,0,0,747,745,1,0,0,0,747,746,1,
        0,0,0,748,751,1,0,0,0,749,751,8,15,0,0,750,744,1,0,0,0,750,749,1,
        0,0,0,751,754,1,0,0,0,752,750,1,0,0,0,752,753,1,0,0,0,753,755,1,
        0,0,0,754,752,1,0,0,0,755,757,5,34,0,0,756,730,1,0,0,0,756,743,1,
        0,0,0,757,222,1,0,0,0,758,759,5,39,0,0,759,760,5,39,0,0,760,761,
        5,39,0,0,761,765,1,0,0,0,762,764,3,225,112,0,763,762,1,0,0,0,764,
        767,1,0,0,0,765,766,1,0,0,0,765,763,1,0,0,0,766,768,1,0,0,0,767,
        765,1,0,0,0,768,769,5,39,0,0,769,770,5,39,0,0,770,785,5,39,0,0,771,
        772,5,34,0,0,772,773,5,34,0,0,773,774,5,34,0,0,774,778,1,0,0,0,775,
        777,3,225,112,0,776,775,1,0,0,0,777,780,1,0,0,0,778,779,1,0,0,0,
        778,776,1,0,0,0,779,781,1,0,0,0,780,778,1,0,0,0,781,782,5,34,0,0,
        782,783,5,34,0,0,783,785,5,34,0,0,784,758,1,0,0,0,784,771,1,0,0,
        0,785,224,1,0,0,0,786,793,8,16,0,0,787,790,5,92,0,0,788,791,3,227,
        113,0,789,791,9,0,0,0,790,788,1,0,0,0,790,789,1,0,0,0,791,793,1,
        0,0,0,792,786,1,0,0,0,792,787,1,0,0,0,793,226,1,0,0,0,794,796,5,
        13,0,0,795,794,1,0,0,0,795,796,1,0,0,0,796,797,1,0,0,0,797,798,5,
        10,0,0,798,228,1,0,0,0,799,801,7,5,0,0,800,799,1,0,0,0,801,802,1,
        0,0,0,802,800,1,0,0,0,802,803,1,0,0,0,803,806,1,0,0,0,804,806,3,
        231,115,0,805,800,1,0,0,0,805,804,1,0,0,0,806,807,1,0,0,0,807,809,
        7,17,0,0,808,810,7,18,0,0,809,808,1,0,0,0,809,810,1,0,0,0,810,812,
        1,0,0,0,811,813,7,5,0,0,812,811,1,0,0,0,813,814,1,0,0,0,814,812,
        1,0,0,0,814,815,1,0,0,0,815,818,1,0,0,0,816,818,3,231,115,0,817,
        805,1,0,0,0,817,816,1,0,0,0,818,230,1,0,0,0,819,821,7,5,0,0,820,
        819,1,0,0,0,821,824,1,0,0,0,822,820,1,0,0,0,822,823,1,0,0,0,823,
        825,1,0,0,0,824,822,1,0,0,0,825,827,5,46,0,0,826,828,7,5,0,0,827,
        826,1,0,0,0,828,829,1,0,0,0,829,827,1,0,0,0,829,830,1,0,0,0,830,
        838,1,0,0,0,831,833,7,5,0,0,832,831,1,0,0,0,833,834,1,0,0,0,834,
        832,1,0,0,0,834,835,1,0,0,0,835,836,1,0,0,0,836,838,5,46,0,0,837,
        822,1,0,0,0,837,832,1,0,0,0,838,232,1,0,0,0,839,844,5,39,0,0,840,
        843,3,239,119,0,841,843,3,245,122,0,842,840,1,0,0,0,842,841,1,0,
        0,0,843,846,1,0,0,0,844,842,1,0,0,0,844,845,1,0,0,0,845,847,1,0,
        0,0,846,844,1,0,0,0,847,858,5,39,0,0,848,853,5,34,0,0,849,852,3,
        241,120,0,850,852,3,245,122,0,851,849,1,0,0,0,851,850,1,0,0,0,852,
        855,1,0,0,0,853,851,1,0,0,0,853,854,1,0,0,0,854,856,1,0,0,0,855,
        853,1,0,0,0,856,858,5,34,0,0,857,839,1,0,0,0,857,848,1,0,0,0,858,
        234,1,0,0,0,859,860,5,39,0,0,860,861,5,39,0,0,861,862,5,39,0,0,862,
        866,1,0,0,0,863,865,3,237,118,0,864,863,1,0,0,0,865,868,1,0,0,0,
        866,867,1,0,0,0,866,864,1,0,0,0,867,869,1,0,0,0,868,866,1,0,0,0,
        869,870,5,39,0,0,870,871,5,39,0,0,871,886,5,39,0,0,872,873,5,34,
        0,0,873,874,5,34,0,0,874,875,5,34,0,0,875,879,1,0,0,0,876,878,3,
        237,118,0,877,876,1,0,0,0,878,881,1,0,0,0,879,880,1,0,0,0,879,877,
        1,0,0,0,880,882,1,0,0,0,881,879,1,0,0,0,882,883,5,34,0,0,883,884,
        5,34,0,0,884,886,5,34,0,0,885,859,1,0,0,0,885,872,1,0,0,0,886,236,
        1,0,0,0,887,890,3,243,121,0,888,890,3,245,122,0,889,887,1,0,0,0,
        889,888,1,0,0,0,890,238,1,0,0,0,891,893,7,19,0,0,892,891,1,0,0,0,
        893,240,1,0,0,0,894,896,7,20,0,0,895,894,1,0,0,0,896,242,1,0,0,0,
        897,899,7,21,0,0,898,897,1,0,0,0,899,244,1,0,0,0,900,901,5,92,0,
        0,901,902,7,22,0,0,902,246,1,0,0,0,903,906,3,249,124,0,904,906,7,
        23,0,0,905,903,1,0,0,0,905,904,1,0,0,0,906,248,1,0,0,0,907,909,7,
        24,0,0,908,907,1,0,0,0,909,250,1,0,0,0,57,0,607,611,613,617,621,
        625,629,631,637,643,645,652,659,666,672,674,696,703,717,725,734,
        737,739,747,750,752,756,765,778,784,790,792,795,802,805,809,814,
        817,822,829,834,837,842,844,851,853,857,866,879,885,889,892,895,
        898,905,908,1,0,1,0
    ]

class PythonLexer(PythonLexerBase):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INDENT = 1
    DEDENT = 2
    LINE_BREAK = 3
    DEF = 4
    RETURN = 5
    RAISE = 6
    FROM = 7
    IMPORT = 8
    NONLOCAL = 9
    AS = 10
    GLOBAL = 11
    ASSERT = 12
    IF = 13
    ELIF = 14
    ELSE = 15
    WHILE = 16
    FOR = 17
    IN = 18
    TRY = 19
    NONE = 20
    FINALLY = 21
    WITH = 22
    EXCEPT = 23
    LAMBDA = 24
    OR = 25
    AND = 26
    NOT = 27
    IS = 28
    CLASS = 29
    YIELD = 30
    DEL = 31
    PASS = 32
    CONTINUE = 33
    BREAK = 34
    ASYNC = 35
    AWAIT = 36
    PRINT = 37
    EXEC = 38
    TRUE = 39
    FALSE = 40
    CONTROLLEDH = 41
    CONTROLLEDU = 42
    CONTROLLEDX = 43
    CONTROLLEDZ = 44
    HADAMARD = 45
    MEASURE = 46
    ORACLE = 47
    SWAP = 48
    S = 49
    T = 50
    X = 51
    Y = 52
    Z = 53
    DOT = 54
    ELLIPSIS = 55
    REVERSE_QUOTE = 56
    STAR = 57
    COMMA = 58
    COLON = 59
    SEMI_COLON = 60
    POWER = 61
    ASSIGN = 62
    OR_OP = 63
    XOR = 64
    AND_OP = 65
    LEFT_SHIFT = 66
    RIGHT_SHIFT = 67
    ADD = 68
    MINUS = 69
    DIV = 70
    MOD = 71
    IDIV = 72
    NOT_OP = 73
    LESS_THAN = 74
    GREATER_THAN = 75
    EQUALS = 76
    GT_EQ = 77
    LT_EQ = 78
    NOT_EQ_1 = 79
    NOT_EQ_2 = 80
    AT = 81
    ARROW = 82
    ADD_ASSIGN = 83
    SUB_ASSIGN = 84
    MULT_ASSIGN = 85
    AT_ASSIGN = 86
    DIV_ASSIGN = 87
    MOD_ASSIGN = 88
    AND_ASSIGN = 89
    OR_ASSIGN = 90
    XOR_ASSIGN = 91
    LEFT_SHIFT_ASSIGN = 92
    RIGHT_SHIFT_ASSIGN = 93
    POWER_ASSIGN = 94
    IDIV_ASSIGN = 95
    STRING = 96
    DECIMAL_INTEGER = 97
    OCT_INTEGER = 98
    HEX_INTEGER = 99
    BIN_INTEGER = 100
    IMAG_NUMBER = 101
    FLOAT_NUMBER = 102
    OPEN_PAREN = 103
    CLOSE_PAREN = 104
    OPEN_BRACE = 105
    CLOSE_BRACE = 106
    OPEN_BRACKET = 107
    CLOSE_BRACKET = 108
    NAME = 109
    LINE_JOIN = 110
    NEWLINE = 111
    WS = 112
    COMMENT = 113

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'return'", "'raise'", "'from'", "'import'", "'nonlocal'", 
            "'as'", "'global'", "'assert'", "'if'", "'elif'", "'else'", 
            "'while'", "'for'", "'in'", "'try'", "'None'", "'finally'", 
            "'with'", "'except'", "'lambda'", "'or'", "'and'", "'not'", 
            "'is'", "'class'", "'yield'", "'del'", "'pass'", "'continue'", 
            "'break'", "'async'", "'await'", "'print'", "'exec'", "'True'", 
            "'False'", "'ch'", "'cu'", "'cx'", "'cz'", "'h'", "'measure'", 
            "'u'", "'swap'", "'s'", "'t'", "'x'", "'y'", "'z'", "'.'", "'...'", 
            "'`'", "'*'", "','", "':'", "';'", "'**'", "'='", "'|'", "'^'", 
            "'&'", "'<<'", "'>>'", "'+'", "'-'", "'/'", "'%'", "'//'", "'~'", 
            "'<'", "'>'", "'=='", "'>='", "'<='", "'<>'", "'!='", "'@'", 
            "'->'", "'+='", "'-='", "'*='", "'@='", "'/='", "'%='", "'&='", 
            "'|='", "'^='", "'<<='", "'>>='", "'**='", "'//='", "'('", "')'", 
            "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "LINE_BREAK", "DEF", "RETURN", "RAISE", 
            "FROM", "IMPORT", "NONLOCAL", "AS", "GLOBAL", "ASSERT", "IF", 
            "ELIF", "ELSE", "WHILE", "FOR", "IN", "TRY", "NONE", "FINALLY", 
            "WITH", "EXCEPT", "LAMBDA", "OR", "AND", "NOT", "IS", "CLASS", 
            "YIELD", "DEL", "PASS", "CONTINUE", "BREAK", "ASYNC", "AWAIT", 
            "PRINT", "EXEC", "TRUE", "FALSE", "CONTROLLEDH", "CONTROLLEDU", 
            "CONTROLLEDX", "CONTROLLEDZ", "HADAMARD", "MEASURE", "ORACLE", 
            "SWAP", "S", "T", "X", "Y", "Z", "DOT", "ELLIPSIS", "REVERSE_QUOTE", 
            "STAR", "COMMA", "COLON", "SEMI_COLON", "POWER", "ASSIGN", "OR_OP", 
            "XOR", "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", 
            "DIV", "MOD", "IDIV", "NOT_OP", "LESS_THAN", "GREATER_THAN", 
            "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "AT", "ARROW", 
            "ADD_ASSIGN", "SUB_ASSIGN", "MULT_ASSIGN", "AT_ASSIGN", "DIV_ASSIGN", 
            "MOD_ASSIGN", "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", 
            "RIGHT_SHIFT_ASSIGN", "POWER_ASSIGN", "IDIV_ASSIGN", "STRING", 
            "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", 
            "IMAG_NUMBER", "FLOAT_NUMBER", "OPEN_PAREN", "CLOSE_PAREN", 
            "OPEN_BRACE", "CLOSE_BRACE", "OPEN_BRACKET", "CLOSE_BRACKET", 
            "NAME", "LINE_JOIN", "NEWLINE", "WS", "COMMENT" ]

    ruleNames = [ "DEF", "RETURN", "RAISE", "FROM", "IMPORT", "NONLOCAL", 
                  "AS", "GLOBAL", "ASSERT", "IF", "ELIF", "ELSE", "WHILE", 
                  "FOR", "IN", "TRY", "NONE", "FINALLY", "WITH", "EXCEPT", 
                  "LAMBDA", "OR", "AND", "NOT", "IS", "CLASS", "YIELD", 
                  "DEL", "PASS", "CONTINUE", "BREAK", "ASYNC", "AWAIT", 
                  "PRINT", "EXEC", "TRUE", "FALSE", "CONTROLLEDH", "CONTROLLEDU", 
                  "CONTROLLEDX", "CONTROLLEDZ", "HADAMARD", "MEASURE", "ORACLE", 
                  "SWAP", "S", "T", "X", "Y", "Z", "DOT", "ELLIPSIS", "REVERSE_QUOTE", 
                  "STAR", "COMMA", "COLON", "SEMI_COLON", "POWER", "ASSIGN", 
                  "OR_OP", "XOR", "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", 
                  "ADD", "MINUS", "DIV", "MOD", "IDIV", "NOT_OP", "LESS_THAN", 
                  "GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ_1", 
                  "NOT_EQ_2", "AT", "ARROW", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MULT_ASSIGN", "AT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                  "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", 
                  "RIGHT_SHIFT_ASSIGN", "POWER_ASSIGN", "IDIV_ASSIGN", "STRING", 
                  "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", 
                  "IMAG_NUMBER", "FLOAT_NUMBER", "OPEN_PAREN", "CLOSE_PAREN", 
                  "OPEN_BRACE", "CLOSE_BRACE", "OPEN_BRACKET", "CLOSE_BRACKET", 
                  "NAME", "LINE_JOIN", "NEWLINE", "WS", "COMMENT", "SHORT_STRING", 
                  "LONG_STRING", "LONG_STRING_ITEM", "RN", "EXPONENT_OR_POINT_FLOAT", 
                  "POINT_FLOAT", "SHORT_BYTES", "LONG_BYTES", "LONG_BYTES_ITEM", 
                  "SHORT_BYTES_CHAR_NO_SINGLE_QUOTE", "SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE", 
                  "LONG_BYTES_CHAR", "BYTES_ESCAPE_SEQ", "ID_CONTINUE", 
                  "ID_START" ]

    grammarFileName = "PythonLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


