# Рекурсивні функції, алгоритми та приклади їх застосування

## Завдання 1
Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, переміщає їх до нової директорії та сортує в піддиректорії, назви яких базуються на розширенні файлів.

## Приклад:

```
PS> .\copy_sort_recursively.py -src_dir C:\AMD\Chipset_Software -dest_dir C:\Temp\HW-03

Copied: C:\AMD\Chipset_Software\Packages\IODriver\I2C\I2C Driver\W11x64\amdi2c.inf -> C:\Temp\HW-03\inf\amdi2c.inf
Copied: C:\AMD\Chipset_Software\Packages\IODriver\I2C\I2C Driver\W11x64\amdi2c.sys -> C:\Temp\HW-03\sys\amdi2c.sys
Copied: C:\AMD\Chipset_Software\Packages\IODriver\I2C\I2C Driver\W11x64\README.txt -> C:\Temp\HW-03\txt\README.txt
Copied: C:\AMD\Chipset_Software\Packages\IODriver\I2C\I2C Driver\WTx64\amdi2c.cat -> C:\Temp\HW-03\cat\amdi2c.cat
Copied: C:\AMD\Chipset_Software\Packages\IODriver\I2C\I2C Driver\WTx64\amdi2c.inf -> C:\Temp\HW-03\inf\amdi2c.inf
Copied: C:\AMD\Chipset_Software\Packages\IODriver\I2C\I2C Driver\WTx64\amdi2c.sys -> C:\Temp\HW-03\sys\amdi2c.sys
Copied: C:\AMD\Chipset_Software\Packages\IODriver\I2C\I2C Driver\WTx64\Readme.txt -> C:\Temp\HW-03\txt\Readme.txt
```

## Завдання 2
Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха» за умови, що користувач повинен мати можливість вказати рівень рекурсії.

## Приклад:

```
PS> .\koch_snowflake.py
Enter the recursion level for the Koch snowflake: 4
```