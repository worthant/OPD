# Laboratory work 6
```python
Based on the variant given by the teacher, develop and explore the operation of a data exchange software complex
in interrupt mode. The main program should modify the contents of a specified memory cell (X), which should be 
represented as a signed number. The range of allowable values for changing X should be limited by a given function
F(X) and the design features of the data register of external device(ВУ) (8-bit signed representation). 
The interrupt processing program should output the modified value of X to the data register of external device(ВУ)
according to the assignment variant, as well as ignore all unprocessed interrupts.
```
# Var 3105
|.pdf|.docx | additional_task |
|---|---|---|
| [report](./docs/report.pdf) | [report](./docs/report.docx) | [additional_task](./additional_task.asm)|

![Задание](./docs/task.png)

## Additional task
```python
Вводить символы с `ВУ Клавиатура` в кодировке по варианту.
Каждый символ транслировать в кодировку CP866 и только потом сохранять в память. 
По окончанию ввода, вывести всю строку на `ВУ Принтер`.
```
