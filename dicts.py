import dictStrings as ds
dictSam = { "Оператор If Else C#": ds.sIfElseCs,
            "Оператор Switch C#": ds.sSwitchCs,
            "Оператор while C#": ds.sWhileCs,
            "Оператор do while C#": ds.sDoWhileCs,
            "Оператор for C#": ds.sForCs,
            "Обьявление массива C#": ds.sCreateMasCs,
            "Инициализация массива C#": ds.sMasInitCs,
            "Пример сортировки C#": ds.sSortCs,

            "Конструкция if 🐍": "Оператор ветвления if позволяет выполнить определенный набор инструкций в зависимости от некоторого условия. После оператора if записывается выражение. Если это выражение истинно, то выполняются инструкции, определяемые данным оператором. После выражения нужно поставить двоеточие “:”.",
            "Конструкция if - else 🐍": "Бывают случаи, когда необходимо предусмотреть альтернативный вариант выполнения программы. Т.е. при истинном условии нужно выполнить один набор инструкций, при ложном – другой. Для этого используется конструкция if – else.",
            "Конструкция if - elif - else 🐍": "Для реализации выбора из нескольких альтернатив можно использовать конструкцию if – elif – else.",

            "Оператор for 🐍" : "Оператор for выполняет указанный набор инструкций заданное количество раз, которое определяется количеством элементов в наборе.",
            "Оператор while 🐍": "Оператор цикла while выполняет указанный набор инструкций до тех пор, пока условие цикла истинно. Истинность условия определяется также как и в операторе if. Синтаксис оператора while выглядит так:",
            "Операторы break и continue 🐍": "При работе с циклами используются операторы break  и continue. Оператор break предназначен для досрочного прерывания работы цикла while или for.Оператор continue запускает цикл заново, при этом код, расположенный после данного оператора, не выполняется.",

            "Создание массива 🐍": "Существует несколько способов создать массив",
            "Методы массивов 🐍": "В Python есть набор встроенных методов, которые вы можете использовать при работе с list. Важно не забывать: индексация массива начинается с нуля.",
            "Обход массивов 🐍": "Вариант только для python",

            "Оператор for 🔤": "Часто цикл for называют циклом со счетчиком. При использовании этого цикла число повторений известно заранее. В заголовке цикла указываются два значения. Количество итераций цикла определяется разностью между вторым и первым значением плюс единица. В Pascal тело цикла не должно содержать выражений, изменяющих счетчик. Цикл for существует в двух формах:",
            "Оператор while 🔤": "Цикл while является циклом с предусловием. В заголовке цикла находится логическое выражение. Если оно возвращает true, то тело цикла выполняется, если false – то нет. Количество повторений этого цикла не заранее неизвестно, он выполняется до тех пор, пока истинно условие",
            "Оператор repeat 🔤": "В цикле repeat логическое выражение стоит после тела цикла. Причем, в отличие от цикла while, здесь всё наоборот: в случае true происходит выход из цикла, в случае false – его повторение. Этот цикл имеет особенность: даже если условие вернёт true, тело цикла всё равно выполнится 1 раз",

            "Конструкция if-else 🔤": "Когда выполнение основной ветки программы доходит до условного оператора if-else, то в зависимости от результата логического выражения в его заголовке выполняются разные блоки кода. После выполнения одного из вложенных блоков кода, ход программы возвращается в основную ветку. Например, программа должна определять, ввел пользователь четное или нечетное число, и выводить на экран сообщение. Тогда программный код на языке Pascal может быть таким:",
            "Конструкция только с if 🔤": "Бывают неполные формы условных операторов. В таком случае вложенный в if блок кода выполняется только в случая true логическом выражении заголовка. В примере ниже, если переменная имеет значение меньше нуля, то ее значение изменяется. Если же значение переменной изначально больше нуля, то блок кода при операторе if вообще не выполняется, т.к. не соблюдено условие.",
            "Операторы then, begin, end 🔤": "В качестве условия может стоять любое выражение, результатом вычисления которого является одно из булевых значений. Непосредственно после then может стоять только один оператор. При необходимости выполнения нескольких операторов они должны быть заключены в операторные скобки begin-end. Пример программы, которая меняет значения переменных местами, только если эти значения различны:",

            "Зачем нужен массив? 🔤": "Предположим, что программа работает с большим количеством однотипных данных. Скажем около ста разных целых чисел нужно обработать, выполнив над ними те или иные вычисления. Как вы себе представляете 100 переменных в программе? И для каждой переменной нужно написать одно и тоже выражение вычисления значения? Это очень неэффективно. Есть более простое решение. Это использование такой структуры (типа) данных как массив. Массив представляет собой последовательность ячеек памяти, в которых хранятся однотипные данные. При этом существует всего одно имя переменной связанной с массивом, а обращение к конкретной ячейке происходит по ее индексу (номеру) в массиве.",
            "Как объявить массив? 🔤": "Помним, все элементы определенного массива имеют один и тот же тип. У разных массивов типы данных могут различаться. Например, один массив может состоять из чисел типа integer, а другой – из чисел типа real. Массив можно создать несколькими способами. Обращение к определенному элементу массива осуществляется путем указания имени переменной массива и в квадратных скобках индекса элемента.",
            "Чтение и запись в массив 🔤": "В примере ниже выделяется область памяти под массив из 11 символов. Их индексы от 1 до 11. В процессе выполнения программы пользователь вводит 11 любых символов (например, ‘q’, ’w’, ’e’, ’2’, ’t’, ’9’, ’u’, ’I’, ’I’, ’o’, ’p’), которые записываются в ячейки массива. Текущее значение переменной i в цикле for используется в качестве индекса массива. Второй цикл for отвечает за вывод элементов массива на экран."
             }

