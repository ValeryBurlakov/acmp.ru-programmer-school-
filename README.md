# 1  A + B
## Требуется сложить два целых числа А и В.
### Входные данные

В единственной строке входного файла INPUT.TXT записаны два натуральных числа через пробел. Значения чисел не превышают 109.
### Выходные данные

В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — сумму чисел А и В.
Пример
№	INPUT.TXT_____________	OUTPUT.TXT
*	2 3	   ________________     5


# 2 Сумма
## Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.
### Входные данные

В единственной строке входного файла INPUT.TXT записано единственное целое число N, не превышающее по абсолютной величине 104.
### Выходные данные

В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — сумму чисел, расположенных между 1 и N включительно.
Пример
- №	INPUT.TXT.........OUTPUT.TXT
* 5	    ___________________      15
* -5       __________________     -14  


# 3 Пятью пять - двадцать пять!
## Вася и Петя учатся в школе в одном классе. Недавно Петя поведал Васе о хитром способе возведения в квадрат натуральных чисел, оканчивающихся на цифру 5. Теперь Вася может с легкостью возводить в квадрат двузначные (и даже некоторые трехзначные) числа, оканчивающиеся на 5. Способ заключается в следующем: для возведения в квадрат числа, оканчивающегося на 5 достаточно умножить число, полученное из исходного вычеркиванием последней пятерки на следующее по порядку число, затем остается лишь приписать «25» к получившемуся результату справа. Например, для того, чтобы возвести число 125 в квадрат достаточно 12 умножить на 13 и приписать 25, т.е. приписывая к числу 12*13=156 число 25, получаем результат 15625, т.е. 1252=15625. Напишите программу, возводящую число, оканчивающееся на 5, в квадрат для того, чтобы Вася смог проверить свои навыки.

### Входные данные

В единственной строке входного файла INPUT.TXT записано одно натуральное число А, оканчивающееся на цифру 5, не превышающее 4*105.
### Выходные данные

В выходной файл OUTPUT.TXT выведите одно натуральное число - A2 без лидирующих нулей.
Примеры
-	INPUT.TXT	_________OUTPUT.TXT
* 	5________________	25
* 75________________	5625
* 4255_____________	18105025


# 108 Неглухой телефон
 ## Возможно, что Вы когда то играли в игру «Глухой телефон», либо слышали о ней. В этой игре участникам приходится передавать информацию друг другу различными способами: словесно, образно, бывает даже приходится писать левой рукой текст, который другой участник команды должен будет прочитать. Так же известно, что практически никогда передаваемая информация не доходит до конечного адресата. Обозначим за Fi(x) функцию, которая преобразует текст передаваемой информации x в ту, которую получит участник i+1 от участника i. Тогда последний n-й участник получит данные y, которые будут выражаться следующей формулой:

y = Fn-1(Fn-2(…F2(F1(x))))

## Но Вам необходимо исключить какие-либо внешние факторы, которые могут исказить исходную информацию и Вы должны реализовать программу «неглухой телефон», которая сможет безошибочно доставлять исходные данные, т.е. в нашем случае функция Fi(x) = x для всех i от 1 до n-1.
## Входные данные

В единственной строке входного файла INPUT.TXT записано натуральное число от 1 до 100.
## Выходные данные

В выходной файл OUTPUT.TXT нужно вывести в точности то же число, которое задано во входном файле.
Пример
* INPUT.TXT__________	OUTPUT.TXT
* 5	_____________________5

# 903 Бисер

В шкатулке хранится разноцветный бисер (или бусины). Все бусины имеют одинаковую форму, размер и вес. Бусины могут быть одного из N различных цветов. В шкатулке много бусин каждого цвета.

Требуется определить минимальное число бусин, которые можно не глядя вытащить из шкатулки так, чтобы среди них гарантированно были две бусины одного цвета.
Входные данные

Входной файл INPUT.TXT содержит одно натуральное число N - количество цветов бусин (1 ≤ N ≤ 109).
Выходные данные

В выходной файл OUTPUT.TXT выведите ответ на поставленную задачу.
Пример
* INPUT.TXT	_____OUTPUT.TXT
* 3	__________________4


# 942 Олимпиада
(Время: 1 сек. Память: 16 Мб Сложность: 2%)

Трое студентов, пятикурсник, третьекурсник и первокурсник, живут в одной комнате общежития и любят участвовать в соревнованиях по программированию по правилам ACM. У каждого из них свой подход к решению задач. Пятикурсник решает все задачи строго по порядку - сначала первую, затем вторую, и так до последней. Третьекурсник решает задачи строго в обратном порядке – сначала последнюю, затем предпоследнюю, и так до первой. А первокурсник сначала решает самую простую задачу, затем – самую простую из оставшихся задач, и так до самой сложной. Сложность задачи определяется временем, необходимым для её решения. Для решения одной и той же задачи наши студенты тратят одинаковое количество времени.

Ваша задача – по описанию соревнований по программированию определить, кто из студентов победит. Напомним, что по правилам ACM побеждает участник, за 300 минут решивший больше всего задач, а при равенстве количества задач – набравший меньше штрафного времени.

Наши студенты – очень сильные программисты, и при решении задач они не делают неправильных попыток. Поэтому за задачу начисляется штраф в размере количества минут от начала соревнования до её посылки на проверку. Если же и количество штрафного времени совпадает – то студент со старшего курса уступает победу студенту с младшего курса.
Входные данные

Первая строка входного файла INPUT.TXT содержит натуральное число N (N ≤ 10) – количество задач. Во второй строке записаны через пробел N натуральных чисел – количество минут, необходимое для решения каждой задачи. Время решения задачи не превосходит 300 минут.
Выходные данные

В выходной файл OUTPUT.TXT выведите номер курса студента, одержавшего победу в олимпиаде.
Примеры
*	INPUT.TXT	______________OUTPUT.TXT
* 1_3_
40 30 60	_1___________2_4
10 20 30 40	_____1
## Пояснение к примерам

В первом тесте пятикурсник набрал 240 штрафных минут (40 + 70 + 130), третьекурсник – 280 (60 + 90 + 130), первокурсник - 230 минут (30 + 70 + 130).

Во втором тесте третьекурсник набрал 300 минут, а первокурсник и пятикурсник – 200 минут. Но пятикурсник уступил первокурснику. 

# 25 Больше-меньше
(Время: 1 сек. Память: 16 Мб Сложность: 3%)

Одна из основных операций с числами – их сравнение. Мы подозреваем, что вы в совершенстве владеете этой операцией и можете сравнивать любые числа, в том числе и целые. В данной задаче необходимо сравнить два целых числа.
Входные данные

В двух строчках входного файла INPUT.TXT записаны числа A и B, не превосходящие по абсолютной величине 2×109.
Выходные данные

Запишите в выходной файл OUTPUT.TXT один символ "<", если A < B, ">", если A > B и "=", если A=B.
Примеры
*	INPUT.TXT____________OUTPUT.TXT
*	5 7	_________________________<_____
* -7-12______________________	>
* 13 13____________________	=


# 766 Орешки
(Время: 1 сек. Память: 16 Мб Сложность: 3%)

Белочка собрала в лесу N шишек c орешками. Белочка очень привередливо выбирала шишки, и брала только те, в которых ровно M орешков. Также известно, что для пропитания зимой ей необходимо не менее K орешков. Определите, хватит ли на зиму орешков белочке.
Входные данные

Первая строка входного файла INPUT.TXT содержит три натуральных числа через пробел: N, M и K (N, M ≤ 100, K ≤ 10 000).
Выходные данные

В выходной файл OUTPUT.TXT выведите «YES» если белочке хватит орешков и «NO» в противном случае.
Примеры
* 	INPUT.TXT________	OUTPUT.TXT
* 	4 5 20	______________YES
* 	4 5 21	_____________NO
* 	3 2 1	______________YES

# 195 Эния
(Время: 1 сек. Память: 16 Мб Сложность: 3%)

Неспокойно сейчас на стапелях шестого дока межгалактического порта планеты Торна. Всего через месяц закончится реконструкция малого броненесущего корвета “Эния”. И снова этому боевому кораблю и его доблестной команде предстоят тяжелые бои за контроль над плутониевыми рудниками Сибелиуса. Работа не прекращается ни на секунду, лазерные сварочные аппараты работают круглые сутки. От непрерывной работы плавятся шарниры роботов-ремонтников. Но задержаться нельзя ни на секунду.

И вот в этой суматохе обнаруживается, что термозащитные панели корвета вновь требуют срочной обработки сульфидом тория. Известно, что на обработку одного квадратного метра панели требуется 1 нанограмм сульфида. Всего необходимо обработать N прямоугольных панелей размером A на B метров. Вам необходимо как можно скорее подсчитать, сколько всего сульфида необходимо на обработку всех панелей “Энии”. И не забудьте, что панели требуют обработки с обеих сторон.
Входные данные

Первая строка входного файла INPUT.TXT содержит 3 целых положительных числа через пробел: N (N ≤ 100), A (A ≤ 100), B (B ≤ 100)
Выходные данные

В выходной файл OUTPUT.TXT нужно вывести единственное число – вес необходимого для обработки сульфида тория в нанограммах.
Примеры
*	INPUT.TXT	--------------------OUTPUT.TXT
*	5 2 3==================	60
*	14 23 5	================3220

 ## 773 Гулливер
(Время: 1 сек. Память: 16 Мб Сложность: 4%)

Из книги Джонатана Свифта мы знаем, что тот Гулливер посетил страну «Лилипутию», где живут лилипуты, окруженные вещами, животными и заводами небольшого размера. Сначала лилипуты боялись Гулливера, но позже они поняли, что такое соседство приносит им большую выгоду, и они стали помогать ему. Например, лилипуты делали кровать для Гулливера из своих маленьких матрацев, сшитых вместе. Лилипутам были известны размеры Гулливера. Довольно быстро они смогли просчитать количество матрацев, необходимых для шитья большого матраца. Но у них постоянно возникали сложности с их небольшим ростом и стеля постель, они иногда не могли сшить достаточно толстый матрац.
Входные данные

Входной файл INPUT.TXT содержит два целых числа, которые разделены пробелом: K – коэффициент, отражающий во сколько раз Гулливер больше лилипутов, и M – количество слоев матрацев (2 ≤ K, M ≤ 100).
Выходные данные

В выходной файл OUTPUT.TXT выведите количество матрацев лилипутов, необходимых для построения матраца для Гулливера.
Примеры
*	INPUT.TXT	OUTPUT.TXT
*	2 2	~~~~~~~~~~8
*	12 4	~~~~~~~576


## 33 Два бандита
(Время: 1 сек. Память: 16 Мб Сложность: 4%)

Бандиты Гарри и Ларри отдыхали на природе. Решив пострелять, они выставили на бревно несколько банок из-под кока-колы (не больше 10). Гарри начал простреливать банки по порядку, начиная с самой левой, Ларри — с самой правой. В какой-то момент получилось так, что они одновременно прострелили одну и ту же последнюю банку.

Гарри возмутился и сказал, что Ларри должен ему кучу денег за то, что тот лишил его удовольствия прострелить несколько банок. В ответ Ларри сказал, что Гарри должен ему еще больше денег по тем же причинам. Они стали спорить кто кому сколько должен, но никто из них не помнил сколько банок было в начале, а искать простреленные банки по всей округе было неохота. Каждый из них помнил только, сколько банок прострелил он сам.

Определите по этим данным, сколько банок не прострелил Гарри и сколько банок не прострелил Ларри.
Входные данные

В единственной строке входного файла INPUT.TXT записано 2 числа — количество банок, простреленных Гарри и Ларри соответственно.
Выходные данные

В файл OUTPUT.TXT выведите 2 числа — количество банок, не простреленных Гарри и Ларри соответственно.
Пример
*	INPUT.TXT~~~~	OUTPUT.TXT
*	4 7	~~~~~~~~~~~~~6 3

# 21 Зарплата
(Время: 1 сек. Память: 16 Мб Сложность: 4%)

В отделе работают 3 сотрудника, которые получают заработную плату в рублях. Требуется определить: на сколько зарплата самого высокооплачиваемого из них отличается от самого низкооплачиваемого.
Входные данные

В единственной строке входного файла INPUT.TXT записаны размеры зарплат всех сотрудников через пробел. Каждая заработная плата – это натуральное число, не превышающее 105.
Выходные данные

В выходной файл OUTPUT.TXT необходимо вывести одно целое число — разницу между максимальной и минимальной зарплатой.
Примеры
*	INPUT.TXT	~~~~~OUTPUT.TXT
*	100 500 1000	~~~900
*	36 11 20	~~~~~~~25


## 4 Игра
(Время: 1 сек. Память: 16 Мб Сложность: 4%)

В свободное время одноклассники Вася и Петя любят играть в различные логические игры: морской бой, крестики-нолики, шахматы, шашки и многое другое. Ребята уже испробовали и поиграли во всевозможные классические игры подобного рода, включая компьютерные. Однажды им захотелось сыграть во что-нибудь новое, но ничего подходящего найти не удалось. Тогда Петя придумал следующую игру «Угадайка»: Играют двое участников. Первый загадывает любое трехзначное число, такое что первая и последняя цифры отличаются друг от друга более чем на единицу. Далее загадавший число игрок переворачивает загаданное число, меняя первую и последнюю цифры местами, таким образом получая еще одно число. Затем из максимального из полученных двух чисел вычитается минимальное. Задача второго игрока – угадать по первой цифре полученного в результате вычитания числа само это число. Например, если Вася загадал число 487, то перестановкой первой и последней цифры он получит число 784. После чего ему придется вычесть из 784 число 487, в результате чего получится число 297, которое и должен отгадать Петя по указанной первой цифре «2», взятой из этого числа. Петя успевает лучше Васи по математике, поэтому практически всегда выигрывает в играх такого типа. Но в данном случае Петя схитрил и специально придумал такую игру, в которой он не проиграет Васе в любом случае. Дело в том, что придуманная Петей игра имеет выигрышную стратегию, которая заключается в следующем: искомое число всегда является трехзначным и вторая его цифра всегда равна девяти, а для получения значения последней достаточно отнять от девяти первую, т.е. в рассмотренном выше случае последняя цифра равна 9-2=7. Помогите Пете еще упростить процесс отгадывания числа по заданной его первой цифре, написав соответствующую программу.
Входные данные

В единственной строке входного файла INPUT.TXT задана единственная цифра К, соответствующая первой цифре полученного Васей в результате вычитания наименьшего загаданного Васей значения из наибольшего.
Выходные данные

В выходной файл OUTPUT.TXT нужно вывести значение полученной Васей разности.
Примеры
*	INPUT.TXT~~~~~~~~	OUTPUT.TXT
*	5	~~~~~~~~~~~~~~~~~594
*	2	~~~~~~~~~~~~~~~~~297
*	7	~~~~~~~~~~~~~~~~~792


# 8 Арифметика
(Время: 1 сек. Память: 16 Мб Сложность: 5%)

В прошлом году Вася пошел в школу и научился считать. В этом году он изучил таблицу умножения и теперь умеет перемножать любые числа от 1 до 10 без ошибок. Друг Петя рассказал ему про системы счисления, отличные от десятичной. В частности, про двоичную, восьмеричную и даже шестнадцатеричную. Теперь Вася без труда (но уже с помощью листка и ручки) может перемножать числа от 1 до 10 и в этих системах, используя перевод из нестандартной системы в десятичную и обратно из десятичной. Например, если Васе нужно перемножить числа 101 и 1001 в двоичной системе, то он сначала эти числа переводит в десятичное представление следующим образом:

(101)2=1*22+0*21+1*20=4+0+1=5

(1001)2=1*23+0*22+0*21+1*20=8+0+0+1=9

После чего перемножение чисел 5 и 9 Вася с легкостью производит в десятичной системе счисления в уме и получает число 45. Далее производится перевод из десятичной системы счисления в двоичную. Для этого Вася делит число 45 на 2 (порядок системы счисления), запоминая остатки от деления, до тех пор пока в результате не останется число 0:
Первод из десятичной системы счисления в двоичную

Ответ составляется из полученных остатков от деления путем их записи в обратном порядке. Таким образом Вася получает результат: (101)2 * (1001)2 = (101101)2. Но теперь Вася изучает таблицу умножения чисел от 1 до 100 в десятичной системе счисления, а поскольку запомнить такую таблицу очень сложно, то Васе придется очень долго ее зубрить. Составьте для Васи программу, которая поможет ему проверять свои знания.
Входные данные

Во входном файле INPUT.TXT записаны три натуральных числа A, B и C через пробел. Числа A и B ≤ 102, а C ≤ 106.
Выходные данные

В выходной файл нужно вывести YES в том случае, если A*B=C и вывести NO в противном случае.
Примеры
*	INPUT.TXT	~~~OUTPUT.TXT
*	8 54 432~~~~~~	YES
*	16 19 777	~~~~~~NO

# 61 Баскетбол
(Время: 1 сек. Память: 16 Мб Сложность: 5%)

Известны результаты каждой из 4х четвертей баскетбольной встречи. Нужно определить победителя матча. Побеждает команда, набравшая больше очков в течение всего матча.
Входные данные

Входной файл INPUT.TXT содержит 4 строки, в каждой строке находится два целых числа a и b – итоговый счет в соответствующей четверти. а – количество набранных очков за четверть первой командой, b – количество очков, набранных за четверть второй командой. (0 ≤ a,b ≤ 100).
Выходные данные

В выходной файл OUTPUT.TXT выведите номер выигравшей команды, в случае ничьей следует вывести «DRAW».
Примеры
*	INPUT.TXT~~~~~~~~~~~~~~	OUTPUT.TXT
*	(26 17)
(13 15)
(19 11)
(14 16 )	~~~~~~~1
*	(14 15)
17 18)
20 20)
15 17 )	~~~~~~~~2
*	(15 16)
(18 17)
(10 12)
(14 12 )	~~~~~~~~~DRAW