У цьому репозиторії реалізовано вирішення 5 завдань з використанням алгоритму backtracking: судоку солвер, солвер лабіринту, солвер кросворду, солвер крипаретичних пазлів і розфарбування графу.

## Судоку солвер
Вирішення головоломки ‘‘Судоку’’ розміром 9х9 складається з модуля sudoku.py і текстового файлу sudoku.txt. В файлі sudoku.txt міститься початковий стан судоку - 9 рядків, які складаються з 9 елементів. Пуста позиція позначається як 0. Судоку вирішується за допомогою методі бектрекінгу. В модулі sudoku.py знаходяться класи і методи, які необхідні для вирішення головоломки і виведення цього рішення на екран користувача. 



## Cолвер лабіринту
Структура цієї частини проекту складається з шістьох модулів: arrays.py, lliststack.py, buildmaze.py, maze.py, maze_game.py, menu.py. Для того щоб програма успішно виконалася потрібно викликати функцію run з модуля menu.py, передавши їй наступні аргументи: назву вхідного файлу, параметри розширення екрану (ширину і висоту) і розмір одного блоку з лабіринту. Вхідний файл повинен містити лабіринт (приклад вхідного файлу - файл ‘mazefile.txt’). Стіни лабіринту повинні бути позначені символом ‘*’, а вільні позиції пробілом. Причому вхід лабіринту повинен бути позначений символом ‘0’, а вихід символом ‘1’.

## Солвер кросворду 
Ми вирішили підійти до проблеми розв’язування кросворду з боку використання алгоритму бектрекінгу. Користувач отримує два файли crossword.py та crossword.txt. Перший містить в собі код програми, а інший – інформацію про параметри кросворду. 

## Солвер крипаретичних пазлів
Розв'язок крипаритичного рівняння з 3 слів. Задача являє собою рівняння з 3 слів, кожне з яких має певну кількість букв, причому сума кількості різних букв усіх рьох слів має бути < 10. Кожну букву потрібно закодувати такою цифрою, щоб сума чисел які відповідають першим двом словам була рівною числу, що відповідає третьому слову.

## Розфарбування графу

Задача полягає у знаходжені мінімальної кількості кольорів для розфарбування графа так, щоб між вершинами з однаковими кольорами не бкло ребер. 

