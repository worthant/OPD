def calculate(DEBUG):
    source = open('output.txt')
    commands = []
    for str in source.readlines():
        str.rsplit()
        arr = []
        for i in range(0, len(str)):
            arr.append(str[i])
        mempl = arr[0] + arr[1] + arr[2]
        if arr[4] != '+':
            command = arr[4] + arr[5] + arr[6] + arr[7]
        else:
            command = arr[4] + arr[5] + arr[6] + arr[7] + arr[8]
        commands.append(mempl + ' ' + command)
        if DEBUG == True: print(commands)
    o = 0
    dircm = commands[o]
    while dircm[4] != '+':
        dirad = dircm[0] + dircm[1] + dircm[2]
        dirrcm = dircm[4] + dircm[5] + dircm[6] + dircm[7]
        print(dirad + ',' + dirrcm + ',', '-' + ',', "Переменная")
        o += 1
        dircm = commands[o]
    if DEBUG == True: print(o)
    while dircm[4] + dircm[5] + dircm[6] + dircm[7] != '0100':
        if dircm[4] == '+':
            dircm = dircm.replace('+', '')
        dirad = dircm[0] + dircm[1] + dircm[2]
        if DEBUG == True: print(dirad)
        dirrcm = dircm[4] + dircm[5] + dircm[6] + dircm[7]
        if DEBUG == True: print(dirad + ',' + dirrcm + ',')
        if dirrcm == '0200':
            print(dirad + ',' + dirrcm + ',', 'CLA' + ',', "Поместить 0 в аккумулятор")
        if dirrcm == '0280':
            print(dirad + ',' + dirrcm + ',', 'NOT' + ',',
                  'Поместить в аккумулятор результат логического отрицания значения аккумулятора')
        if dirrcm == '0300':
            print(dirad + ',' + dirrcm + ',', 'CLC' + ',', 'Поместить 0 в C')
        if dirrcm == '0380':
            print(dirad + ',' + dirrcm + ',', 'CMC' + ',', 'Поместить в C результат логического отрицания значения C')
        if dirrcm == '0400':
            print(dirad + ',' + dirrcm + ',', 'ROL' + ',', 'Циклический сдвиг влево')
        if dirrcm == '0480':
            print(dirad + ',' + dirrcm + ',', 'ROR' + ',', 'Циклический сдвиг вправо')
        if dirrcm == '0500':
            print(dirad + ',' + dirrcm + ',', 'ASL' + ',', 'Арифметический сдвиг влево')
        if dirrcm == '0580':
            print(dirad + ',' + dirrcm + ',', 'ASR' + ',', 'Арифместический сдвиг вправо')
        if dirrcm == '0600':
            print(dirad + ',' + dirrcm + ',', 'SXTB' + ',', 'Расширение знака младшего байта')
        if dirrcm == '0680':
            print(dirad + ',' + dirrcm + ',', 'SWAB' + ',', 'Обмен ст. и мл. байтов')
        if dirrcm == '0700':
            print(dirad + ',' + dirrcm + ',', 'INC' + ',', 'Добавить 1 к значению аккумулятора')
        if dirrcm == '0740':
            print(dirad + ',' + dirrcm + ',', 'DEC' + ',', 'Вычесть 1 из значения аккумулятора')
        if dirrcm == '0780':
            print(dirad + ',' + dirrcm + ',', 'NEG' + ',', 'Добавить 1 к логическому отрицанию аккумулятора')
        if dirrcm == '0800':
            print(dirad + ',' + dirrcm + ',', 'POP' + ',', '(SP+)->AC')
        if dirrcm == '0900':
            print(dirad + ',' + dirrcm + ',', 'POPF' + ',', '(SP+)->PS')
        if dirrcm == '0A00':
            print(dirad + ',' + dirrcm + ',', 'RET' + ',', '(SP)+->IP')
        if dirrcm == '0B00':
            print(dirad + ',' + dirrcm + ',', 'IRET' + ',', '(SP)+->PS, (SP)+->IP')
        if dirrcm == '0C00':
            print(dirad + ',' + dirrcm + ',', 'PUSH' + ',', 'AC->-(SP)')
        if dirrcm == '0D00':
            print(dirad + ',' + dirrcm + ',', 'PUSHF' + ',', 'PS->-(SP)')
        if dirrcm == '0E00':
            print(dirad + ',' + dirrcm + ',', 'SWAP' + ',', 'Обмен А и вершины стека')
        if dircm[4] == '1':
            if dircm[5] == '0':
                print(dirad + ',' + dirrcm + ',', 'DI' + ',', 'Запрет прерываний')
            if dircm[5] == '1':
                print(dirad + ',' + dirrcm + ',', 'EI' + ',', 'Разрешение прерывайний')
            if dircm[5] == '2':
                print(dirad + ',' + dirrcm + ',', 'IN REG' + ',', 'Чтение из регистров ВУ')
            if dircm[5] == '3':
                print(dirad + ',' + dirrcm + ',', 'OUT REG' + ',', 'Запись в регистры ВУ')
            if dircm[5] == '8':
                print(dirad + ',' + dirrcm + ',', 'INT NUM' + ',', 'Программное прерывание с заданным вектором')
        if dircm[4] == '2':
            if dircm[5] in range(0, 8):
                print(dirad + ',' + dirrcm + ',', 'AND ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Логическое умножение значения аккумулятора с содержимым ячейки памяти ' + dircm[5] + dircm[6] +
                      dircm[7])
            if dircm[5] == 'F':
                print(dirad + ',' + dirrcm + ',', 'AND ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Логическе умножение значения аккмулятора с числом ' + dircm[6] + dircm[7])
            if dircm[5] == '8':
                print(dirad + ',' + dirrcm + ',', 'AND ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Логическе умножение значения аккмулятора с содержимым ячeйки памяти MEM(IP+' + dircm[6] + dircm[
                          7] + ')')
            if dircm[5] == 'A':
                print(dirad + ',' + dirrcm + ',', 'AND ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Логическое умножение значения аккумулятора с содержимым ячейки памяти IP+' + dircm[6] + dircm[7],
                      'IP+1')
            if dircm[5] == 'B':
                print(dirad + ',' + dirrcm + ',', 'AND ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Логическое умножение значения аккумулятора с содержимым ячейки памяти IP+' + dircm[6] + dircm[
                          7] + '-1')
            if dircm[5] == 'C':
                print(dirad + ',' + dirrcm + ',', 'AND ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Логическое умножение значения аккумулятора с содержимым стека (SP+' + dircm[6] + dircm[7])
            if dircm[5] == 'E':
                print(dirad + ',' + dirrcm + ',', 'AND' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Логическое умножение значения аккумулятора с содержимым ячейки памяти IP+' + dircm[6] + dircm[7])
        if dircm[4] == '3':
            if dircm[5] in range(0, 8):
                print(dirad + ',' + dirrcm + ',', 'OR ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Логическое сложение значения аккумулятора с содержимым ячейки памяти ' + dircm[5] + dircm[6] +
                      dircm[7])
            if dircm[5] == 'F':
                print(dirad + ',' + dirrcm + ',', 'OR ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Логическе сложение значения аккмулятора с числом ' + dircm[6] + dircm[7])
            if dircm[5] == '8':
                print(dirad + ',' + dirrcm + ',', 'OR ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Логическе сложение значения аккмулятора с содержимым ячeйки памяти MEM(IP+' + dircm[6] + dircm[
                          7] + ')')
            if dircm[5] == 'A':
                print(dirad + ',' + dirrcm + ',', 'OR ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Логическое сложение значения аккумулятора с содержимым ячейки памяти IP+' + dircm[6] + dircm[7],
                      'IP+1')
            if dircm[5] == 'B':
                print(dirad + ',' + dirrcm + ',', 'OR ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Логическое сложение значения аккумулятора с содержимым ячейки памяти IP+' + dircm[6] + dircm[
                          7] + '-1')
            if dircm[5] == 'C':
                print(dirad + ',' + dirrcm + ',', 'OR ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Логическое сложение значения аккумулятора с содержимым стека (SP+' + dircm[6] + dircm[7])
            if dircm[5] == 'E':
                print(dirad + ',' + dirrcm + ',', 'OR' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Логическое сложение значения аккумулятора с содержимым ячейки памяти IP+' + dircm[6] + dircm[7])
        if dircm[4] == '4':
            if dircm[5] in range(0, 8):
                print(dirad + ',' + dirrcm + ',', 'ADD ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое сложение значения аккумулятора с содержимым ячейки памяти ' + dircm[5] + dircm[
                          6] + dircm[7])
            if dircm[5] == 'F':
                print(dirad + ',' + dirrcm + ',', 'ADD ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое сложение значения аккмулятора с числом ' + dircm[6] + dircm[7])
            if dircm[5] == '8':
                print(dirad + ',' + dirrcm + ',', 'ADD ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое сложение значения аккмулятора с содержимым ячeйки памяти MEM(IP+' + dircm[6] +
                      dircm[7] + ')')
            if dircm[5] == 'A':
                print(dirad + ',' + dirrcm + ',', 'ADD ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое сложение значения аккумулятора с содержимым ячейки памяти IP+' + dircm[6] + dircm[
                          7], 'IP+1')
            if dircm[5] == 'B':
                print(dirad + ',' + dirrcm + ',', 'ADD ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое сложение значения аккумулятора с содержимым ячейки памяти IP+' + dircm[6] + dircm[
                          7] + '-1')
            if dircm[5] == 'C':
                print(dirad + ',' + dirrcm + ',', 'ADD ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое сложение значения аккумулятора с содержимым стека (SP+' + dircm[6] + dircm[7])
            if dircm[5] == 'E':
                print(dirad + ',' + dirrcm + ',', 'ADD ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое сложение значения аккумулятора с содержимым ячейки памяти IP+' + dircm[6] + dircm[
                          7])
        if dircm[4] == '5':
            if dircm[5] in range(0, 8):
                print(dirad + ',' + dirrcm + ',', 'ADC ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое сложение значения аккумулятора с С и ссодержимым ячейки памяти' + dircm[5] +
                      dircm[6] + dircm[7])
            if dircm[5] == 'F':
                print(dirad + ',' + dirrcm + ',', 'ADС ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое сложение значения аккмулятора с С и с числом ' + dircm[6] + dircm[7])
            if dircm[5] == '8':
                print(dirad + ',' + dirrcm + ',', 'ADС ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое сложение значения аккмулятора с С и с содержимым ячeйки памяти MEM(IP+' + dircm[
                          6] + dircm[7] + ')')
            if dircm[5] == 'A':
                print(dirad + ',' + dirrcm + ',', 'ADС ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое сложение значения аккумулятора с С и с содержимым ячейки памяти IP+' + dircm[6] +
                      dircm[7], 'IP+1')
            if dircm[5] == 'B':
                print(dirad + ',' + dirrcm + ',', 'ADС ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое сложение значения аккумулятора с С и с содержимым ячейки памяти IP+' + dircm[6] +
                      dircm[7] + '-1')
            if dircm[5] == 'C':
                print(dirad + ',' + dirrcm + ',', 'ADС ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое сложение значения аккумулятора с С и с содержимым стека (SP+' + dircm[6] + dircm[
                          7])
            if dircm[5] == 'E':
                print(dirad + ',' + dirrcm + ',', 'ADС ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое сложение значения аккумулятора с С и с содержимым ячейки памяти IP+' + dircm[6] +
                      dircm[7])
        if dircm[4] == '6':
            if dircm[5] in range(0, 8):
                print(dirad + ',' + dirrcm + ',', 'SUB ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое вычитание значения аккумулятора и содержимого ячейки памяти' + dircm[5] + dircm[
                          6] + dircm[7])
            if dircm[5] == 'F':
                print(dirad + ',' + dirrcm + ',', 'SUB ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое вычитания значения аккмулятора с числом ' + dircm[6] + dircm[7])
            if dircm[5] == '8':
                print(dirad + ',' + dirrcm + ',', 'SUB ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое вычитание значения аккмулятора и содержимого ячeйки памяти MEM(IP+' + dircm[6] +
                      dircm[7] + ')')
            if dircm[5] == 'A':
                print(dirad + ',' + dirrcm + ',', 'SUB ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое сложение значения аккумулятора и содержимого ячейки памяти IP+' + dircm[6] +
                      dircm[7], 'IP+1')
            if dircm[5] == 'B':
                print(dirad + ',' + dirrcm + ',', 'SUB ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое сложение значения аккумулятора и содержимого ячейки памяти IP+' + dircm[6] +
                      dircm[7] + '-1')
            if dircm[5] == 'C':
                print(dirad + ',' + dirrcm + ',', 'SUB ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое сложение значения аккумулятора и содержимого стека (SP+' + dircm[6] + dircm[7])
            if dircm[5] == 'E':
                print(dirad + ',' + dirrcm + ',', 'SUB ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Арифметическое сложение значения аккумулятора и содержимого ячейки памяти IP+' + dircm[6] +
                      dircm[7])
        if dircm[4] == '7':
            if dircm[5] in range(0, 8):
                print(dirad + ',' + dirrcm + ',', 'CMP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Установить флаги по результату арифметического вычитания значения аккумулятора и содержимого ячейки памяти' +
                      dircm[5] + dircm[6] + dircm[7])
            if dircm[5] == 'F':
                print(dirad + ',' + dirrcm + ',', 'CMP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Установить флаги по результату арифметического вычитания значения аккмулятора с числом ' + dircm[
                          6] + dircm[7])
            if dircm[5] == '8':
                print(dirad + ',' + dirrcm + ',', 'CMP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Установить флаги по результату арифметического вычитания значения аккмулятора и содержимого ячeйки памяти MEM(IP+' +
                      dircm[6] + dircm[7] + ')')
            if dircm[5] == 'A':
                print(dirad + ',' + dirrcm + ',', 'CMP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Установить флаги по результату арифметического вычитания значения аккумулятора и содержимого ячейки памяти IP+' +
                      dircm[6] + dircm[7], 'IP+1')
            if dircm[5] == 'B':
                print(dirad + ',' + dirrcm + ',', 'CMP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Установить флаги по результату арифметического вычитания значения аккумулятора и содержимого ячейки памяти IP+' +
                      dircm[6] + dircm[7] + '-1')
            if dircm[5] == 'C':
                print(dirad + ',' + dirrcm + ',', 'CMP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Установить флаги по результату арифметического вычитания значения аккумулятора и содержимого стека (SP+' +
                      dircm[6] + dircm[7])
            if dircm[5] == 'E':
                print(dirad + ',' + dirrcm + ',', 'CMP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Установить флаги по результату арифметического вычитания значения аккумулятора и содержимого ячейки памяти IP+' +
                      dircm[6] + dircm[7])
        if dircm[4] == '8':
            if dircm[5] in range(0, 8):
                print(dirad + ',' + dirrcm + ',', 'LOOP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      dircm[5] + dircm[6] + dircm[7] + ' - 1 -> ' + dircm[5] + dircm[6] + dircm[7],
                      'Если ' + dircm[5] + dircm[6] + dircm[7] + ' <= 0, то IP + 1 -> IP')
            if dircm[5] == 'F':
                print(dirad + ',' + dirrcm + ',', 'LOOP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      dircm[6] + dircm[7] + ' - 1 -> MEM(IP-1)',
                      'Если ' + dircm[6] + dircm[7] + ' <= 0, то IP + 1 -> IP')
            if dircm[5] == '8':
                print(dirad + ',' + dirrcm + ',', 'LOOP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'MEM(IP+' + dircm[6] + dircm[7] + ' - 1 -> MEM(IP+' + dircm[6] + dircm[7],
                      'Если MEM(IP+' + dircm[6] + dircm[7] + ') <= 0, то IP + 1 -> IP')
            if dircm[5] == 'A':
                print(dirad + ',' + dirrcm + ',', 'LOOP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'MEM(IP+' + dircm[6] + dircm[7] + ') - 1 -> MEM(IP+' + dircm[6] + dircm[7] + ')',
                      'Если MEM(IP+' + dircm[6] + dircm[7] + ') <= 0, то IP + 1 ->IP, IP + 1 -> IP')
            if dircm[5] == 'B':
                print(dirad + ',' + dirrcm + ',', 'LOOP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'MEM(IP+' + dircm[6] + dircm[7] + ')-1 - 1 -> MEM(IP+' + dircm[6] + dircm[7] + ')-1',
                      'Если MEM(IP+' + dircm[6] + dircm[7] + ')-1 <= 0, то IP + 1 -> IP')
            if dircm[5] == 'C':
                print(dirad + ',' + dirrcm + ',', 'LOOP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      '(SP+' + dircm[6] + dircm[7] + ') - 1 -> (SP+' + dircm[6] + dircm[7] + ')',
                      'Если (SP+' + dircm[6] + dircm[7] + ') <= 0, то IP + 1 -> IP')
            if dircm[5] == 'E':
                print(dirad + ',' + dirrcm + ',', 'LOOP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'MEM(IP+' + dircm[6] + dircm[7] + ') - 1 -> MEM(IP+' + dircm[6] + dircm[7] + ')',
                      'Если MEM(IP+' + dircm[6] + dircm[7] + ') <= 0, то IP + 1 -> IP')
        if dircm[4] == 'A':
            if dircm[5] in range(0, 8):
                print(dirad + ',' + dirrcm + ',', 'LD ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить в аккумулятор значение ячейки памяти' + dircm[5] + dircm[6] + dircm[7])
            if dircm[5] == 'F':
                print(dirad + ',' + dirrcm + ',', 'LD ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить в аккмулятор число ' + dircm[6] + dircm[7])
            if dircm[5] == '8':
                print(dirad + ',' + dirrcm + ',', 'LD ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить в аккмулятор содержимое ячeйки памяти MEM(IP+' + dircm[6] + dircm[7] + ')')
            if dircm[5] == 'A':
                print(dirad + ',' + dirrcm + ',', 'LD ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить в аккмулятор содержимое ячейки памяти IP+' + dircm[6] + dircm[7], 'IP+1')
            if dircm[5] == 'B':
                print(dirad + ',' + dirrcm + ',', 'LD ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить в аккмулятор содержимое ячейки памяти IP+' + dircm[6] + dircm[7] + '-1')
            if dircm[5] == 'C':
                print(dirad + ',' + dirrcm + ',', 'LD ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить в аккмулятор содержимое стека (SP+' + dircm[6] + dircm[7])
            if dircm[5] == 'E':
                print(dirad + ',' + dirrcm + ',', 'LD ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить в аккмулятор содержимое ячейки памяти IP+' + dircm[6] + dircm[7])
        if dircm[4] == 'B':
            if dircm[5] in range(0, 8):
                print(dirad + ',' + dirrcm + ',', 'SWAM ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Поменять местами з   начение аккумулятора и значение ячейки памяти' + dircm[5] + dircm[6] +
                      dircm[7])
            if dircm[5] == 'F':
                print(dirad + ',' + dirrcm + ',', 'SWAM ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Поменять местами значение аккумулятора и число ' + dircm[6] + dircm[7])
            if dircm[5] == '8':
                print(dirad + ',' + dirrcm + ',', 'SWAM ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Поменять местами значение аккумулятора и содержимое ячeйки памяти MEM(IP+' + dircm[6] + dircm[
                          7] + ')')
            if dircm[5] == 'A':
                print(dirad + ',' + dirrcm + ',', 'SWAM ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Поменять местами значение аккумулятора и содержимое ячейки памяти IP+' + dircm[6] + dircm[7],
                      'IP+1')
            if dircm[5] == 'B':
                print(dirad + ',' + dirrcm + ',', 'SWAM ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Поменять местами значение аккумулятора и содержимое ячейки памяти IP+' + dircm[6] + dircm[
                          7] + '-1')
            if dircm[5] == 'C':
                print(dirad + ',' + dirrcm + ',', 'SWAM ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Поменять местами значение аккумулятора и содержимое стека (SP+' + dircm[6] + dircm[7])
            if dircm[5] == 'E':
                print(dirad + ',' + dirrcm + ',', 'SWAM ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Поменять местами значение аккумулятора и содержимое ячейки памяти IP+' + dircm[6] + dircm[7])
        if dircm[4] == 'С':
            if dircm[5] in range(0, 8):
                print(dirad + ',' + dirrcm + ',', 'JUMP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить в IP значение ячейки памяти' + dircm[5] + dircm[6] + dircm[7])
            if dircm[5] == 'F':
                print(dirad + ',' + dirrcm + ',', 'JUMP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить в IP число ' + dircm[6] + dircm[7])
            if dircm[5] == '8':
                print(dirad + ',' + dirrcm + ',', 'JUMP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить в IP содержимое ячeйки памяти MEM(IP+' + dircm[6] + dircm[7] + ')')
            if dircm[5] == 'A':
                print(dirad + ',' + dirrcm + ',', 'JUMP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить в IP содержимое ячейки памяти IP+' + dircm[6] + dircm[7], 'IP+1')
            if dircm[5] == 'B':
                print(dirad + ',' + dirrcm + ',', 'JUMP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить в IP содержимое ячейки памяти IP+' + dircm[6] + dircm[7] + '-1')
            if dircm[5] == 'C':
                print(dirad + ',' + dirrcm + ',', 'JUMP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить в IP содержимое стека (SP+' + dircm[6] + dircm[7])
            if dircm[5] == 'E':
                print(dirad + ',' + dirrcm + ',', 'JUMP ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить в IP содержимое ячейки памяти IP+' + dircm[6] + dircm[7])
        if dircm[4] == 'D':
            if dircm[5] in range(0, 8):
                print(dirad + ',' + dirrcm + ',', 'CALL ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'SP - 1 -> SP, IP -> (SP), Загрузить в IP значение ячейки памяти' + dircm[5] + dircm[6] + dircm[
                          7])
            if dircm[5] == 'F':
                print(dirad + ',' + dirrcm + ',', 'CALL ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'SP - 1 -> SP, IP -> (SP), Загрузить в IP число ' + dircm[6] + dircm[7])
            if dircm[5] == '8':
                print(dirad + ',' + dirrcm + ',', 'CALL ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'SP - 1 -> SP, IP -> (SP), Загрузить в IP содержимое ячeйки памяти MEM(IP+' + dircm[6] + dircm[
                          7] + ')')
            if dircm[5] == 'A':
                print(dirad + ',' + dirrcm + ',', 'CALL ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'SP - 1 -> SP, IP -> (SP), Загрузить в IP содержимое ячейки памяти IP+' + dircm[6] + dircm[7],
                      'IP+1')
            if dircm[5] == 'B':
                print(dirad + ',' + dirrcm + ',', 'CALL ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'SP - 1 -> SP, IP -> (SP), Загрузить в IP содержимое ячейки памяти IP+' + dircm[6] + dircm[
                          7] + '-1')
            if dircm[5] == 'C':
                print(dirad + ',' + dirrcm + ',', 'CALL ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'SP - 1 -> SP, IP -> (SP), Загрузить в IP содержимое стека (SP+' + dircm[6] + dircm[7] + ')')
            if dircm[5] == 'E':
                print(dirad + ',' + dirrcm + ',', 'CALL ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'SP - 1 -> SP, IP -> (SP), Загрузить в IP содержимое ячейки памяти IP+' + dircm[6] + dircm[7])
        if dircm[4] == 'E':
            if dircm[5] in range(0, 8):
                print(dirad + ',' + dirrcm + ',', 'ST ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить значение из аккумулятора в ячейку памяти ' + dircm[5] + dircm[6] + dircm[7])
            if dircm[5] == 'F':
                print(dirad + ',' + dirrcm + ',', 'ST ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить значение из аккумулятора в текущую ячейку памяти ' + dircm[6] + dircm[7])
            if dircm[5] == '8':
                print(dirad + ',' + dirrcm + ',', 'ST ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить значение из аккумулятора в ячейку памяти MEM(IP+' + dircm[6] + dircm[7] + ')')
            if dircm[5] == 'A':
                print(dirad + ',' + dirrcm + ',', 'ST ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить значение из аккумулятора в ячейку памяти IP+' + dircm[6] + dircm[7], 'IP+1')
            if dircm[5] == 'B':
                print(dirad + ',' + dirrcm + ',', 'ST ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить значение из аккумулятора в ячейку памяти IP+' + dircm[6] + dircm[7] + '-1')
            if dircm[5] == 'C':
                print(dirad + ',' + dirrcm + ',', 'ST ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить занчение из аккумулятора в ячейку памяти (SP+' + dircm[6] + dircm[7] + ')')
            if dircm[5] == 'E':
                print(dirad + ',' + dirrcm + ',', 'ST ' + dircm[5] + dircm[6] + dircm[7] + ',',
                      'Загрузить занчение из аккумулятора в ячейку памяти IP+' + dircm[6] + dircm[7])
        if dirrcm[0] == 'F':
            if dirrcm[1] == '0':
                print(dirad + ',' + dirrcm + ',', 'BEQ ' + dirrcm[2] + dirrcm[3] + ',',
                      'Переход если равенство на IP+' + dirrcm[2] + dirrcm[3])
            if dirrcm[1] == '1':
                print(dirad + ',' + dirrcm + ',', 'BNE ' + dirrcm[2] + dirrcm[3] + ',',
                      'Переход если неравенство на IP+' + dirrcm[2] + dirrcm[3])
            if dirrcm[1] == '2':
                print(dirad + ',' + dirrcm + ',', 'BMI ' + dirrcm[2] + dirrcm[3] + ',',
                      'Переход если минус на IP+' + dirrcm[2] + dirrcm[3])
            if dirrcm[1] == '3':
                print(dirad + ',' + dirrcm + ',', 'BPL ' + dirrcm[2] + dirrcm[3] + ',',
                      'Переход если плюс на IP+' + dirrcm[2] + dirrcm[3])
            if dirrcm[1] == '4':
                print(dirad + ',' + dirrcm + ',', 'BHIS ' + dirrcm[2] + dirrcm[3] + ',',
                      'Переход если перенос на IP+' + dirrcm[2] + dirrcm[3])
            if dirrcm[1] == '5':
                print(dirad + ',' + dirrcm + ',', 'BLO ' + dirrcm[2] + dirrcm[3] + ',',
                      'Переход если нет переноса на IP+' + dirrcm[2] + dirrcm[3])
            if dirrcm[1] == '6':
                print(dirad + ',' + dirrcm + ',', 'BVS ' + dirrcm[2] + dirrcm[3] + ',',
                      'Переход если переполнение на IP+' + dirrcm[2] + dirrcm[3])
            if dirrcm[1] == '7':
                print(dirad + ',' + dirrcm + ',', 'BVC ' + dirrcm[2] + dirrcm[3] + ',',
                      'Переход если нет переполнения на IP+' + dirrcm[2] + dirrcm[3])
            if dirrcm[1] == '8':
                print(dirad + ',' + dirrcm + ',', 'BLT ' + dirrcm[2] + dirrcm[3] + ',',
                      'Переход если меньше на IP+' + dirrcm[2] + dirrcm[3])
            if dirrcm[1] == '9':
                print(dirad + ',' + dirrcm + ',', 'BGE ' + dirrcm[2] + dirrcm[3] + ',',
                      'Переход если больше или равно на IP+' + dirrcm[2] + dirrcm[3])
        if o != len(source.readlines()):
            o += 1
            dircm = commands[o]
            if DEBUG == True: print(o)
        else:
            break
    while o != (len(commands)):
        dircm = commands[o]
        dirad = dircm[0] + dircm[1] + dircm[2]
        dirrcm = dircm[4] + dircm[5] + dircm[6] + dircm[7]
        if dirrcm == '0100':
            print(dirad + ',' + dirrcm + ',''HLT' + ',', "Переход в пультовый режим")
        else:
            print(dirad + ',' + dirrcm + ',', '-' + ',', "Переменная")
        o += 1


def convert():
    source = open('input.txt', 'r+')
    output = open('output.txt', 'r+')
    output.write('dontkillme\n')
    for s in source.readlines():
        print(len(s))
        if len(s) == 10:
            if s[3] == ':':
                s = s[:3] + ' ' + s[5:9]
            if s[4] == "+":
                s = s[:3] + ' ' + s[4:9]
            else:
                s = s[:3] + ' ' + s[4:8]
        else:
            if s[-1] == "\n":
                s = s[:3] + ' ' + s[3:8]
            s = s[:3] + ' ' + s[5:9]
        output.write(str(s) + '\n')
    print(output.readlines())


convert()
calculate(False)
