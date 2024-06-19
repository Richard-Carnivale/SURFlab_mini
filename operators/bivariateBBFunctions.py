from math import factorial
import math
import numpy as np

"""
    SCALER MATRICES ARE DEFINED PRIOR TO COMPUTATION FOR BETTER PERFORMANCE
"""
#TODO: Change the lookup table from string lookup to pair lookup
matrixLUT = {
	"33": np.array([
		[1,2,1,],
		[2,4,2,],
		[1,2,1,],
	]),
	"23": np.array([
		[1,2,1,],
		[1,2,1,],
	]),
	"32": np.array([
		[1,1,],
		[2,2,],
		[1,1,],
	]),
	"44": np.array([
		[1,3,3,1,],
		[3,9,9,3,],
		[3,9,9,3,],
		[1,3,3,1,],
	]),
	"34": np.array([
		[1,3,3,1,],
		[2,6,6,2,],
		[1,3,3,1,],
	]),
	"43": np.array([
		[1,2,1,],
		[3,6,3,],
		[3,6,3,],
		[1,2,1,],
	]),
	"55": np.array([
		[1,4,6,4,1,],
		[4,16,24,16,4,],
		[6,24,36,24,6,],
		[4,16,24,16,4,],
		[1,4,6,4,1,],
	]),
	"45": np.array([
		[1,4,6,4,1,],
		[3,12,18,12,3,],
		[3,12,18,12,3,],
		[1,4,6,4,1,],
	]),
	"54": np.array([
		[1,3,3,1,],
		[4,12,12,4,],
		[6,18,18,6,],
		[4,12,12,4,],
		[1,3,3,1,],
	]),
	"66": np.array([
		[1,5,10,10,5,1,],
		[5,25,50,50,25,5,],
		[10,50,100,100,50,10,],
		[10,50,100,100,50,10,],
		[5,25,50,50,25,5,],
		[1,5,10,10,5,1,],
	]),
	"56": np.array([
		[1,5,10,10,5,1,],
		[4,20,40,40,20,4,],
		[6,30,60,60,30,6,],
		[4,20,40,40,20,4,],
		[1,5,10,10,5,1,],
	]),
	"65": np.array([
		[1,4,6,4,1,],
		[5,20,30,20,5,],
		[10,40,60,40,10,],
		[10,40,60,40,10,],
		[5,20,30,20,5,],
		[1,4,6,4,1,],
	]),
	"77": np.array([
		[1,6,15,20,15,6,1,],
		[6,36,90,120,90,36,6,],
		[15,90,225,300,225,90,15,],
		[20,120,300,400,300,120,20,],
		[15,90,225,300,225,90,15,],
		[6,36,90,120,90,36,6,],
		[1,6,15,20,15,6,1,],
	]),
	"88": np.array([
		[1,7,21,35,35,21,7,1,],
		[7,49,147,245,245,147,49,7,],
		[21,147,441,735,735,441,147,21,],
		[35,245,735,1225,1225,735,245,35,],
		[35,245,735,1225,1225,735,245,35,],
		[21,147,441,735,735,441,147,21,],
		[7,49,147,245,245,147,49,7,],
		[1,7,21,35,35,21,7,1,],
	]),
	"99": np.array([
		[1,8,28,56,70,56,28,8,1,],
		[8,64,224,448,560,448,224,64,8,],
		[28,224,784,1568,1960,1568,784,224,28,],
		[56,448,1568,3136,3920,3136,1568,448,56,],
		[70,560,1960,3920,4900,3920,1960,560,70,],
		[56,448,1568,3136,3920,3136,1568,448,56,],
		[28,224,784,1568,1960,1568,784,224,28,],
		[8,64,224,448,560,448,224,64,8,],
		[1,8,28,56,70,56,28,8,1,],
	]),
	"1010": np.array([
		[1,9,36,84,126,126,84,36,9,1,],
		[9,81,324,756,1134,1134,756,324,81,9,],
		[36,324,1296,3024,4536,4536,3024,1296,324,36,],
		[84,756,3024,7056,10584,10584,7056,3024,756,84,],
		[126,1134,4536,10584,15876,15876,10584,4536,1134,126,],
		[126,1134,4536,10584,15876,15876,10584,4536,1134,126,],
		[84,756,3024,7056,10584,10584,7056,3024,756,84,],
		[36,324,1296,3024,4536,4536,3024,1296,324,36,],
		[9,81,324,756,1134,1134,756,324,81,9,],
		[1,9,36,84,126,126,84,36,9,1,],
	]),
	"1111": np.array([
		[1,10,45,120,210,252,210,120,45,10,1,],
		[10,100,450,1200,2100,2520,2100,1200,450,100,10,],
		[45,450,2025,5400,9450,11340,9450,5400,2025,450,45,],
		[120,1200,5400,14400,25200,30240,25200,14400,5400,1200,120,],
		[210,2100,9450,25200,44100,52920,44100,25200,9450,2100,210,],
		[252,2520,11340,30240,52920,63504,52920,30240,11340,2520,252,],
		[210,2100,9450,25200,44100,52920,44100,25200,9450,2100,210,],
		[120,1200,5400,14400,25200,30240,25200,14400,5400,1200,120,],
		[45,450,2025,5400,9450,11340,9450,5400,2025,450,45,],
		[10,100,450,1200,2100,2520,2100,1200,450,100,10,],
		[1,10,45,120,210,252,210,120,45,10,1,],
	]),
	"1212": np.array([
		[1,11,55,165,330,462,462,330,165,55,11,1,],
		[11,121,605,1815,3630,5082,5082,3630,1815,605,121,11,],
		[55,605,3025,9075,18150,25410,25410,18150,9075,3025,605,55,],
		[165,1815,9075,27225,54450,76230,76230,54450,27225,9075,1815,165,],
		[330,3630,18150,54450,108900,152460,152460,108900,54450,18150,3630,330,],
		[462,5082,25410,76230,152460,213444,213444,152460,76230,25410,5082,462,],
		[462,5082,25410,76230,152460,213444,213444,152460,76230,25410,5082,462,],
		[330,3630,18150,54450,108900,152460,152460,108900,54450,18150,3630,330,],
		[165,1815,9075,27225,54450,76230,76230,54450,27225,9075,1815,165,],
		[55,605,3025,9075,18150,25410,25410,18150,9075,3025,605,55,],
		[11,121,605,1815,3630,5082,5082,3630,1815,605,121,11,],
		[1,11,55,165,330,462,462,330,165,55,11,1,],
	]),
	"1313": np.array([
		[1,12,66,220,495,792,924,792,495,220,66,12,1,],
		[12,144,792,2640,5940,9504,11088,9504,5940,2640,792,144,12,],
		[66,792,4356,14520,32670,52272,60984,52272,32670,14520,4356,792,66,],
		[220,2640,14520,48400,108900,174240,203280,174240,108900,48400,14520,2640,220,],
		[495,5940,32670,108900,245025,392040,457380,392040,245025,108900,32670,5940,495,],
		[792,9504,52272,174240,392040,627264,731808,627264,392040,174240,52272,9504,792,],
		[924,11088,60984,203280,457380,731808,853776,731808,457380,203280,60984,11088,924,],
		[792,9504,52272,174240,392040,627264,731808,627264,392040,174240,52272,9504,792,],
		[495,5940,32670,108900,245025,392040,457380,392040,245025,108900,32670,5940,495,],
		[220,2640,14520,48400,108900,174240,203280,174240,108900,48400,14520,2640,220,],
		[66,792,4356,14520,32670,52272,60984,52272,32670,14520,4356,792,66,],
		[12,144,792,2640,5940,9504,11088,9504,5940,2640,792,144,12,],
		[1,12,66,220,495,792,924,792,495,220,66,12,1,],
	]),
	"1414": np.array([
		[1,13,78,286,715,1287,1716,1716,1287,715,286,78,13,1,],
		[13,169,1014,3718,9295,16731,22308,22308,16731,9295,3718,1014,169,13,],
		[78,1014,6084,22308,55770,100386,133848,133848,100386,55770,22308,6084,1014,78,],
		[286,3718,22308,81796,204490,368082,490776,490776,368082,204490,81796,22308,3718,286,],
		[715,9295,55770,204490,511225,920205,1226940,1226940,920205,511225,204490,55770,9295,715,],
		[1287,16731,100386,368082,920205,1656369,2208492,2208492,1656369,920205,368082,100386,16731,1287,],
		[1716,22308,133848,490776,1226940,2208492,2944656,2944656,2208492,1226940,490776,133848,22308,1716,],
		[1716,22308,133848,490776,1226940,2208492,2944656,2944656,2208492,1226940,490776,133848,22308,1716,],
		[1287,16731,100386,368082,920205,1656369,2208492,2208492,1656369,920205,368082,100386,16731,1287,],
		[715,9295,55770,204490,511225,920205,1226940,1226940,920205,511225,204490,55770,9295,715,],
		[286,3718,22308,81796,204490,368082,490776,490776,368082,204490,81796,22308,3718,286,],
		[78,1014,6084,22308,55770,100386,133848,133848,100386,55770,22308,6084,1014,78,],
		[13,169,1014,3718,9295,16731,22308,22308,16731,9295,3718,1014,169,13,],
		[1,13,78,286,715,1287,1716,1716,1287,715,286,78,13,1,],
	]),
	"1515": np.array([
		[1,14,91,364,1001,2002,3003,3432,3003,2002,1001,364,91,14,1,],
		[14,196,1274,5096,14014,28028,42042,48048,42042,28028,14014,5096,1274,196,14,],
		[91,1274,8281,33124,91091,182182,273273,312312,273273,182182,91091,33124,8281,1274,91,],
		[364,5096,33124,132496,364364,728728,1093092,1249248,1093092,728728,364364,132496,33124,5096,364,],
		[1001,14014,91091,364364,1002001,2004002,3006003,3435432,3006003,2004002,1002001,364364,91091,14014,1001,],
		[2002,28028,182182,728728,2004002,4008004,6012006,6870864,6012006,4008004,2004002,728728,182182,28028,2002,],
		[3003,42042,273273,1093092,3006003,6012006,9018009,10306296,9018009,6012006,3006003,1093092,273273,42042,3003,],
		[3432,48048,312312,1249248,3435432,6870864,10306296,11778624,10306296,6870864,3435432,1249248,312312,48048,3432,],
		[3003,42042,273273,1093092,3006003,6012006,9018009,10306296,9018009,6012006,3006003,1093092,273273,42042,3003,],
		[2002,28028,182182,728728,2004002,4008004,6012006,6870864,6012006,4008004,2004002,728728,182182,28028,2002,],
		[1001,14014,91091,364364,1002001,2004002,3006003,3435432,3006003,2004002,1002001,364364,91091,14014,1001,],
		[364,5096,33124,132496,364364,728728,1093092,1249248,1093092,728728,364364,132496,33124,5096,364,],
		[91,1274,8281,33124,91091,182182,273273,312312,273273,182182,91091,33124,8281,1274,91,],
		[14,196,1274,5096,14014,28028,42042,48048,42042,28028,14014,5096,1274,196,14,],
		[1,14,91,364,1001,2002,3003,3432,3003,2002,1001,364,91,14,1,],
	]),
	"1616": np.array([
		[1,15,105,455,1365,3003,5005,6435,6435,5005,3003,1365,455,105,15,1,],
		[15,225,1575,6825,20475,45045,75075,96525,96525,75075,45045,20475,6825,1575,225,15,],
		[105,1575,11025,47775,143325,315315,525525,675675,675675,525525,315315,143325,47775,11025,1575,105,],
		[455,6825,47775,207025,621075,1366365,2277275,2927925,2927925,2277275,1366365,621075,207025,47775,6825,455,],
		[1365,20475,143325,621075,1863225,4099095,6831825,8783775,8783775,6831825,4099095,1863225,621075,143325,20475,1365,],
		[3003,45045,315315,1366365,4099095,9018009,15030015,19324305,19324305,15030015,9018009,4099095,1366365,315315,45045,3003,],
		[5005,75075,525525,2277275,6831825,15030015,25050025,32207175,32207175,25050025,15030015,6831825,2277275,525525,75075,5005,],
		[6435,96525,675675,2927925,8783775,19324305,32207175,41409225,41409225,32207175,19324305,8783775,2927925,675675,96525,6435,],
		[6435,96525,675675,2927925,8783775,19324305,32207175,41409225,41409225,32207175,19324305,8783775,2927925,675675,96525,6435,],
		[5005,75075,525525,2277275,6831825,15030015,25050025,32207175,32207175,25050025,15030015,6831825,2277275,525525,75075,5005,],
		[3003,45045,315315,1366365,4099095,9018009,15030015,19324305,19324305,15030015,9018009,4099095,1366365,315315,45045,3003,],
		[1365,20475,143325,621075,1863225,4099095,6831825,8783775,8783775,6831825,4099095,1863225,621075,143325,20475,1365,],
		[455,6825,47775,207025,621075,1366365,2277275,2927925,2927925,2277275,1366365,621075,207025,47775,6825,455,],
		[105,1575,11025,47775,143325,315315,525525,675675,675675,525525,315315,143325,47775,11025,1575,105,],
		[15,225,1575,6825,20475,45045,75075,96525,96525,75075,45045,20475,6825,1575,225,15,],
		[1,15,105,455,1365,3003,5005,6435,6435,5005,3003,1365,455,105,15,1,],
	]),
	"1717": np.array([
		[1,16,120,560,1820,4368,8008,11440,12870,11440,8008,4368,1820,560,120,16,1,],
		[16,256,1920,8960,29120,69888,128128,183040,205920,183040,128128,69888,29120,8960,1920,256,16,],
		[120,1920,14400,67200,218400,524160,960960,1372800,1544400,1372800,960960,524160,218400,67200,14400,1920,120,],
		[560,8960,67200,313600,1019200,2446080,4484480,6406400,7207200,6406400,4484480,2446080,1019200,313600,67200,8960,560,],
		[1820,29120,218400,1019200,3312400,7949760,14574560,20820800,23423400,20820800,14574560,7949760,3312400,1019200,218400,29120,1820,],
		[4368,69888,524160,2446080,7949760,19079424,34978944,49969920,56216160,49969920,34978944,19079424,7949760,2446080,524160,69888,4368,],
		[8008,128128,960960,4484480,14574560,34978944,64128064,91611520,103062960,91611520,64128064,34978944,14574560,4484480,960960,128128,8008,],
		[11440,183040,1372800,6406400,20820800,49969920,91611520,130873600,147232800,130873600,91611520,49969920,20820800,6406400,1372800,183040,11440,],
		[12870,205920,1544400,7207200,23423400,56216160,103062960,147232800,165636900,147232800,103062960,56216160,23423400,7207200,1544400,205920,12870,],
		[11440,183040,1372800,6406400,20820800,49969920,91611520,130873600,147232800,130873600,91611520,49969920,20820800,6406400,1372800,183040,11440,],
		[8008,128128,960960,4484480,14574560,34978944,64128064,91611520,103062960,91611520,64128064,34978944,14574560,4484480,960960,128128,8008,],
		[4368,69888,524160,2446080,7949760,19079424,34978944,49969920,56216160,49969920,34978944,19079424,7949760,2446080,524160,69888,4368,],
		[1820,29120,218400,1019200,3312400,7949760,14574560,20820800,23423400,20820800,14574560,7949760,3312400,1019200,218400,29120,1820,],
		[560,8960,67200,313600,1019200,2446080,4484480,6406400,7207200,6406400,4484480,2446080,1019200,313600,67200,8960,560,],
		[120,1920,14400,67200,218400,524160,960960,1372800,1544400,1372800,960960,524160,218400,67200,14400,1920,120,],
		[16,256,1920,8960,29120,69888,128128,183040,205920,183040,128128,69888,29120,8960,1920,256,16,],
		[1,16,120,560,1820,4368,8008,11440,12870,11440,8008,4368,1820,560,120,16,1,],
	]),
	"1818": np.array([
		[1,17,136,680,2380,6188,12376,19448,24310,24310,19448,12376,6188,2380,680,136,17,1,],
		[17,289,2312,11560,40460,105196,210392,330616,413270,413270,330616,210392,105196,40460,11560,2312,289,17,],
		[136,2312,18496,92480,323680,841568,1683136,2644928,3306160,3306160,2644928,1683136,841568,323680,92480,18496,2312,136,],
		[680,11560,92480,462400,1618400,4207840,8415680,13224640,16530800,16530800,13224640,8415680,4207840,1618400,462400,92480,11560,680,],
		[2380,40460,323680,1618400,5664400,14727440,29454880,46286240,57857800,57857800,46286240,29454880,14727440,5664400,1618400,323680,40460,2380,],
		[6188,105196,841568,4207840,14727440,38291344,76582688,120344224,150430280,150430280,120344224,76582688,38291344,14727440,4207840,841568,105196,6188,],
		[12376,210392,1683136,8415680,29454880,76582688,153165376,240688448,300860560,300860560,240688448,153165376,76582688,29454880,8415680,1683136,210392,12376,],
		[19448,330616,2644928,13224640,46286240,120344224,240688448,378224704,472780880,472780880,378224704,240688448,120344224,46286240,13224640,2644928,330616,19448,],
		[24310,413270,3306160,16530800,57857800,150430280,300860560,472780880,590976100,590976100,472780880,300860560,150430280,57857800,16530800,3306160,413270,24310,],
		[24310,413270,3306160,16530800,57857800,150430280,300860560,472780880,590976100,590976100,472780880,300860560,150430280,57857800,16530800,3306160,413270,24310,],
		[19448,330616,2644928,13224640,46286240,120344224,240688448,378224704,472780880,472780880,378224704,240688448,120344224,46286240,13224640,2644928,330616,19448,],
		[12376,210392,1683136,8415680,29454880,76582688,153165376,240688448,300860560,300860560,240688448,153165376,76582688,29454880,8415680,1683136,210392,12376,],
		[6188,105196,841568,4207840,14727440,38291344,76582688,120344224,150430280,150430280,120344224,76582688,38291344,14727440,4207840,841568,105196,6188,],
		[2380,40460,323680,1618400,5664400,14727440,29454880,46286240,57857800,57857800,46286240,29454880,14727440,5664400,1618400,323680,40460,2380,],
		[680,11560,92480,462400,1618400,4207840,8415680,13224640,16530800,16530800,13224640,8415680,4207840,1618400,462400,92480,11560,680,],
		[136,2312,18496,92480,323680,841568,1683136,2644928,3306160,3306160,2644928,1683136,841568,323680,92480,18496,2312,136,],
		[17,289,2312,11560,40460,105196,210392,330616,413270,413270,330616,210392,105196,40460,11560,2312,289,17,],
		[1,17,136,680,2380,6188,12376,19448,24310,24310,19448,12376,6188,2380,680,136,17,1,],
	]),
	"1919": np.array([
		[1,18,153,816,3060,8568,18564,31824,43758,48620,43758,31824,18564,8568,3060,816,153,18,1,],
		[18,324,2754,14688,55080,154224,334152,572832,787644,875160,787644,572832,334152,154224,55080,14688,2754,324,18,],
		[153,2754,23409,124848,468180,1310904,2840292,4869072,6694974,7438860,6694974,4869072,2840292,1310904,468180,124848,23409,2754,153,],
		[816,14688,124848,665856,2496960,6991488,15148224,25968384,35706528,39673920,35706528,25968384,15148224,6991488,2496960,665856,124848,14688,816,],
		[3060,55080,468180,2496960,9363600,26218080,56805840,97381440,133899480,148777200,133899480,97381440,56805840,26218080,9363600,2496960,468180,55080,3060,],
		[8568,154224,1310904,6991488,26218080,73410624,159056352,272668032,374918544,416576160,374918544,272668032,159056352,73410624,26218080,6991488,1310904,154224,8568,],
		[18564,334152,2840292,15148224,56805840,159056352,344622096,590780736,812323512,902581680,812323512,590780736,344622096,159056352,56805840,15148224,2840292,334152,18564,],
		[31824,572832,4869072,25968384,97381440,272668032,590780736,1012766976,1392554592,1547282880,1392554592,1012766976,590780736,272668032,97381440,25968384,4869072,572832,31824,],
		[43758,787644,6694974,35706528,133899480,374918544,812323512,1392554592,1914762564,2127513960,1914762564,1392554592,812323512,374918544,133899480,35706528,6694974,787644,43758,],
		[48620,875160,7438860,39673920,148777200,416576160,902581680,1547282880,2127513960,2363904400,2127513960,1547282880,902581680,416576160,148777200,39673920,7438860,875160,48620,],
		[43758,787644,6694974,35706528,133899480,374918544,812323512,1392554592,1914762564,2127513960,1914762564,1392554592,812323512,374918544,133899480,35706528,6694974,787644,43758,],
		[31824,572832,4869072,25968384,97381440,272668032,590780736,1012766976,1392554592,1547282880,1392554592,1012766976,590780736,272668032,97381440,25968384,4869072,572832,31824,],
		[18564,334152,2840292,15148224,56805840,159056352,344622096,590780736,812323512,902581680,812323512,590780736,344622096,159056352,56805840,15148224,2840292,334152,18564,],
		[8568,154224,1310904,6991488,26218080,73410624,159056352,272668032,374918544,416576160,374918544,272668032,159056352,73410624,26218080,6991488,1310904,154224,8568,],
		[3060,55080,468180,2496960,9363600,26218080,56805840,97381440,133899480,148777200,133899480,97381440,56805840,26218080,9363600,2496960,468180,55080,3060,],
		[816,14688,124848,665856,2496960,6991488,15148224,25968384,35706528,39673920,35706528,25968384,15148224,6991488,2496960,665856,124848,14688,816,],
		[153,2754,23409,124848,468180,1310904,2840292,4869072,6694974,7438860,6694974,4869072,2840292,1310904,468180,124848,23409,2754,153,],
		[18,324,2754,14688,55080,154224,334152,572832,787644,875160,787644,572832,334152,154224,55080,14688,2754,324,18,],
		[1,18,153,816,3060,8568,18564,31824,43758,48620,43758,31824,18564,8568,3060,816,153,18,1,],
	])
}

"""
    ALGORITHMS FOR MANIPULATING BERNSTEIN BEZIER POLYNOMIALS
"""
#Helper function for combinations, in the form of nChoosek
def comb(n,k):
	return math.factorial(n) / (math.factorial(n-k) * math.factorial(k))

#If a scaler isn't found in the LUT, this function will be called to add a scaler to the LUT
def createScaler(u, v):
	scalerMatrix = np.zeros((v+1,u+1))
	for i in range(0,v+1):
		for j in range(0,u+1):
			scalerMatrix[i][j] = comb(u, j) * comb(v,i)
	return scalerMatrix

#Take the derivative of a bernstein polynomial in the u direction
def bbUDir(poly): 
    #matrix math
    leftCols = poly[:, :len(poly[0]) - 1]
    rightCols = poly[:, 1:]
    colDirs = rightCols - leftCols
    return colDirs * (len(poly[0]) - 1)

#Take the derivative of a bernstein polynomial in the v direction
def bbVDir(poly):
    upRows = poly[:len(poly)-1,:]
    botRows = poly[1:,:]
    rowDirs = botRows - upRows
    return rowDirs * (len(poly)-1)

#multiply two bernstein polynomials
def bbMult(poly1, poly2):
	scalerKey1 = str(len(poly1)) + str(len(poly1[0]))
	scalerKey2 = str(len(poly2)) + str(len(poly2[0]))
	#if our matrices are not in the lookup table, make them and add them to the table
	if scalerKey1 not in matrixLUT:
		matrixLUT[scalerKey1] = createScaler(len(poly1[0])-1, len(poly1)-1)
	if scalerKey2 not in matrixLUT:
		matrixLUT[scalerKey2] = createScaler(len(poly2[0])-1, len(poly2)-1)
	#lookup our scaler matrices and multiply them elementwise to our coeficient matrices
	scaledPoly1 = poly1 * matrixLUT[scalerKey1]	
	scaledPoly2 = poly2 * matrixLUT[scalerKey2]
	#create an empty matrix of degree u = un+um, v = vn+vm
	#where n and m are the degree of the two polynomials
	newScaledPoly = np.zeros((len(scaledPoly1)+len(scaledPoly2)-1, len(scaledPoly1[0]) + len(scaledPoly2[0]) - 1))
	descalerKey = str(len(newScaledPoly)) + str(len(newScaledPoly[0])) 
	#multiply the polynomials
	for vi in range(0, len(poly1)):
		for ui in range(0, len(poly1[0])):
			for vj in range(0, len(poly2)):
				for uj in range(0, len(poly2[0])):
					newScaledPoly[vi+vj][ui+uj] = newScaledPoly[vi+vj][ui+uj] + scaledPoly1[vi][ui] * scaledPoly2[vj][uj]
	
	if (descalerKey not in matrixLUT):
		matrixLUT[descalerKey] = createScaler(len(newScaledPoly[0]) - 1,len(newScaledPoly) - 1)
	#descale our matrix to get the new coefficient matrix and return it
	return newScaledPoly / matrixLUT[descalerKey]

def bbDefIntegral(poly):
    return np.sum(poly) / (len(poly) * len(poly[0]))

class bbFunctions:
	@staticmethod
	def zerothMoment(xCoefs, yCoefs, zCoefs):
		dxdu = bbUDir(xCoefs)
		dydv = bbVDir(yCoefs)
		xuyv = bbMult(dxdu, dydv)
		dxdv = bbVDir(xCoefs)
		dydu = bbUDir(yCoefs)
		xvyu = bbMult(dxdv, dydu)
		n3 = xuyv - xvyu
		zn = bbMult(n3, zCoefs)
		return(bbDefIntegral(zn))
	@staticmethod
	def firstMoment(xCoefs, yCoefs, zCoefs):
		dxdu = bbUDir(xCoefs)
		dydv = bbVDir(yCoefs)
		xuyv = bbMult(dxdu, dydv)
		dxdv = bbVDir(xCoefs)
		dydu = bbUDir(yCoefs)
		xvyu = bbMult(dxdv, dydu)
		n3 = xuyv - xvyu
		zn = bbMult(n3, zCoefs)
		xz = bbMult(xCoefs, zCoefs)
		m1 = bbDefIntegral(bbMult(xz, n3))
		m2 = bbDefIntegral(bbMult(zn, yCoefs))
		m3 = bbDefIntegral(bbMult(zn, zCoefs)) / 2
		return m1,m2,m3
	@staticmethod
	def secondMoment(xCoefs, yCoefs, zCoefs, offset = np.array([0,0,0])):
		xCoefs = xCoefs - offset[0]
		yCoefs = yCoefs - offset[1]
		zCoefs = zCoefs - offset[2]
		dxdu = bbUDir(xCoefs)
		dydv = bbVDir(yCoefs)
		xuyv = bbMult(dxdu, dydv)
		dxdv = bbVDir(xCoefs)
		dydu = bbUDir(yCoefs)
		xvyu = bbMult(dxdv, dydu)
		n3 = xuyv - xvyu
		zn  = bbMult(n3, zCoefs)
		m1  = bbMult(zn, xCoefs)
		m2  = bbMult(zn, yCoefs)
		m3  = bbMult(zn, zCoefs)
		m11 = bbDefIntegral (bbMult(m1, xCoefs))
		m12 = bbDefIntegral (bbMult(m2, xCoefs))
		m13 = bbDefIntegral (bbMult(m3, xCoefs)) / 2
		m22 = bbDefIntegral (bbMult(m2, yCoefs))
		m23 = bbDefIntegral (bbMult(m3, yCoefs)) / 2
		m33 = bbDefIntegral (bbMult(m3, zCoefs)) / 3
		moi = np.array([
			[m11,m12,m13],
			[m12,m22,m23],
			[m13,m23,m33]
		])
		return moi
	
	@staticmethod
	def allMoments(xCoefs, yCoefs,zCoefs):
		#do everything at once because its more efficient
		#
		dxdu = bbUDir(xCoefs)
		dydv = bbVDir(yCoefs)
		xuyv = bbMult(dxdu, dydv)
		dxdv = bbVDir(xCoefs)
		dydu = bbUDir(yCoefs)
		xvyu = bbMult(dxdv, dydu)
		n3 = xuyv - xvyu
		zn  = bbMult(n3, zCoefs)
		#Volume calculations
		volume = bbDefIntegral(zn)
		#Center of mass calculations
		m1  = bbMult(zn, xCoefs)
		m2  = bbMult(zn, yCoefs)
		m3  = bbMult(zn, zCoefs)
		tM1 = bbDefIntegral(m1)
		tM2 = bbDefIntegral(m2)
		tM3 = bbDefIntegral(m3) / 2
		#Moment of inertia calculations, needs to be done at the origin apparently
		"""
		m11 = bbDefIntegral (bbMult(m1, xCoefs))
		m12 = bbDefIntegral (bbMult(m2, xCoefs))
		m13 = bbDefIntegral (bbMult(m3, xCoefs)) / 2 
		m22 = bbDefIntegral (bbMult(m2, yCoefs))
		m23 = bbDefIntegral (bbMult(m3, yCoefs)) / 2
		m32 = bbDefIntegral (bbMult(m2, zCoefs)) / 2
		m33 = bbDefIntegral (bbMult(m3, zCoefs)) / 3"""
		com = np.array([
			tM1, tM2, tM3
		])
		"""moi = np.array([
			[m11,m12,m13],
			[m12,m22,m23],
			[m13,m23,m33]
		])"""
		#Return numpy matrices so the numpy library can handle the elementwise addition of all moments calculated 
		# (should be faster than doing it in python)
		return volume, com