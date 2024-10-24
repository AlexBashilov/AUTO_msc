# Приёмочные автотесты для проекта TMS
## Стек
Среда: **Python 3.12.5**  
Фреймворки: 
- [PyTest](https://pytest.org/)
- [Selenium with Python](https://selenium-python.readthedocs.io/) 


## Установка необходимого ПО
1. Скачиваем [**JetBrains PyCharm Community**](https://www.jetbrains.com/ru-ru/pycharm/download/)
2. [для Windows] Устанавливаем [Git](https://git-scm.com/download/win)
3. Клонируем проект
    - Выбираем репорзиторий -> Кнопка "**Клонировать**" -> "Клонировать с помощью SSH или HTTP" -> Копировать
    ![](img/clone_git_01.png)

    - Открываем PyCharm -> Projects -> Get from VSC
    ![](img/clone_git_02.png)

    - Вставляем скопированные данные в URL -> Clone.
    ![](img/clone_git_03.png)

4. Уставливаем виртуальное окружение для Python в PyCharm

    - Меню File -> Settings -> Projects:tests - Python Interpreter -> Add
    ![](img/py_1.png)

    - Virtual Environment -> Ok.  
    ![](img/py_2.png)

5. Далее открываем консоль (вкладка меню снизу - **Terminal**) и проверяем, что у нас есть префикс **(venv)** в консоли
\- виртуальное окружение для Python установилось.
6. Установить все библиотеке из файла requirements.txt
```pip install -r requirements.txt```
7. Если мы видим "ворнинг" после выполнения установок фреймворков, то можно обновить установщик **pip** для этого
виртуального окружения.  
```WARNING: You are using pip version 21.3.1; however, version 22.1.2 is available.```  
![](img/py_3.png)  
  
    В Windows это будет выглядеть примерно так:  
    ```C:\Git\pdm\tests\venv\Scripts\python.exe -m pip install --upgrade pip```.
8. Скопировать файл .env (в этом файле указанны все переменные окружения, которые нужны для корректной работы автотестов, но значения для них не указаны)
    - Вставить файл в корень проекта (там же, где расположен .env) переименовав его в .env.local - в этом файле мы указываем все значения переменных окружения
9. Можно запускать автотесты
## Полезные материалы по теме

- [Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575/promo)
