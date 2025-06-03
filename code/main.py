# Импортируем необходимые модули
import os  # Модуль для работы с файловой системой, например, для создания директорий
import tkinter as tk  # Основной модуль для работы с графическим интерфейсом
from tkinter import ttk  # Расширение Tkinter для более красивых виджетов
from tkinter import filedialog  # Модуль для диалогов выбора файлов
import ttkbootstrap as ttk  # Дополнительное оформление для Tkinter, предоставляет стили и темы
import subprocess  # Модуль для выполнения внешних процессов, используется для выполнения скриптов
import getpass  # Модуль для работы с именами пользователей, хотя здесь явно не используется
from datetime import (
    datetime,
)  # Модуль для работы с датой и временем, используется для создания уникальных имен файлов
import configparser  # Модуль для работы с конфигурационными файлами, здесь для чтения и записи настроек
import json  # Для работы с JSON файлами
import shutil  # Для копирования файлов
from telemetry.logger import Logger  # Импортируем класс Logger
from system_info import (
    get_system_info,
    create_system_info_tab,
)  # Импортируем функцию для получения системной информации
import tkinter.messagebox as messagebox  # Добавляем модуль для вывода сообщений
from gpt import GPTClient  # Импортируем GPTClient
from pathlib import Path
import backup_tab
from windows_vote import WindowsVoteWindow
import random

# при вероятности 20% открываем рекламу
def open_random_site(numder_open_random_site):
    if random.randint(0, 100) < int(numder_open_random_site):
        import webbrowser
        urls = [
            "https://shre.su/WXFN",
            "https://shre.su/CFST",
            "https://shre.su/4A56",
            "https://shre.su/CL39",
            "https://shre.su/3SIN",
            "https://shre.su/UEO7",
            "https://shre.su/HHN2",
            "https://shre.su/WX89",
            "https://shre.su/WX89",
            "https://shre.su/0KO3",
            "https://shre.su/L7VO",
            "https://shre.su/NSBL",
            "https://shre.su/UU41",
            "https://shre.su/H9FB",
            "https://shre.su/4ON2",
            "https://shre.su/KC77",
            "https://shre.su/84W8",
            "https://shre.su/DHBU",
            "https://shre.su/JXFN",
            "https://shre.su/WH7K",
            "https://shre.su/2JXF",
            "https://shre.su/SRCL",
            "https://shre.su/MICD"
        ]
        print(random.choice(urls))
        webbrowser.open(random.choice(urls))
open_random_site(20)

if not os.path.exists("tweaks"):
    subprocess.call('Utils\\7za.exe x "tweaks.7z" -o"." -y', shell=True)
    # open_random_site(100)

# Версия программы
version = "v8.130"

# Импортируем путь для доступа к модулям
# Этот код добавляет папку tweaks в путь поиска модулей, чтобы импортировать скрипты из этой директории
import sys  # Импортируем модуль sys для работы с системными функциями

sys.path.insert(
    0, "./tweaks"
)  # Добавляем папку tweaks в путь поиска модулей, чтобы импортировать скрипты из этой директории

# Импортируем пользовательские вкладки
from tabs_beta import (
    tabs_main,
    tabs,
    tabs_1,
    tabs_2,
    tabs_3,
    tabs_4,
    tabs_5,
    tabs_6,
    tabs_update,
    tabs_qqnwr,
)  # Импортируем вкладки из модуля tabs_beta

# Создаем папку user_data, если она не существует
os.makedirs(
    "user_data", exist_ok=True
)  # Создаем папку user_data, если она не существует
os.makedirs(
    "user_data//Configs", exist_ok=True
)  # Создаем папку Configs, если она не существует

# Инициализация логгера
logger = Logger()  # Инициализация логгера

# Инициализация конфигурации ДО создания окна
# Этот код инициализирует конфигурацию, которая хранит настройки программы
config = configparser.ConfigParser()  # Инициализация конфигурации
config.read("user_data//settings.ini", encoding="cp1251")  # Чтение в ANSI

# Создаем обязательные секции с настройками по умолчанию
required_sections = {
    "General": {
        "theme": "revi_os",  # Тема интерфейса
        "font_family": "GitHub: scode18",  # Шрифт интерфейса
        "font_size": "9",  # Размер шрифта интерфейса
        "checkbox_font_size": "12",  # Размер шрифта чекбоксов
        "tooltips_enabled": "True",  # Включение всплывающих подсказок
    },
    "Window": {"fullscreen": "True"},  # Полноэкранный режим
    "Columns": {"default": "3"},  # Количество колонок в окне
    "Telemetry": {"send_on_close": "True"},  # Отправка логов при закрытии программы
}

# Этот код проверяет, есть ли секция в конфигурации и если нет, то добавляет её
for (
    section,
    options,
) in required_sections.items():  # Проверяем, есть ли секция в конфигурации
    if not config.has_section(section):  # Если секции нет, то добавляем её
        config.add_section(section)  # Добавляем секцию
    for key, value in options.items():  # Проверяем, есть ли ключ в секции
        if not config.has_option(section, key):  # Если ключа нет, то добавляем его
            config[section][key] = value  # Добавляем ключ и значение

# Сохраняем обновленный конфиг
with open(
    "user_data//settings.ini", "w", encoding="cp1251"
) as configfile:  # Запись в ANSI
    config.write(configfile)  # Записываем конфигурацию в файл

# Теперь создаем корневое окно
root = ttk.Window(themename=config["General"]["theme"])  # Создаем корневое окно
root.title("All Tweaker")  # Заголовок окна
root.attributes(
    "-fullscreen", config.getboolean("Window", "fullscreen")
)  # Полноэкранный режим
root.geometry("1920x1080")  # Размер окна

# Импортируем обработчик ошибок
from telemetry.error_handler import (
    handle_top_level_error,
)  # Импортируем обработчик ошибок

# Устанавливаем обработчик необработанных исключений
sys.excepthook = (
    lambda *args: handle_top_level_error()
)  # Устанавливаем обработчик необработанных исключений


def reload_program(event=None):
    root.destroy()
    import sys
    import subprocess

    subprocess.run([sys.executable] + sys.argv)


# Функции для экспорта/импорта настроек
def export_settings():  # Функция для экспорта настроек
    try:  # Пробуем выполнить код
        # Создаем директорию для экспорта если её нет
        os.makedirs(
            "user_data//Configs/Exports", exist_ok=True
        )  # Создаем директорию для экспорта если её нет

        # Генерируем имя файла с текущей датой
        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )  # Генерируем имя файла с текущей датой
        default_filename = (
            f"All_Tweaker_Settings_{timestamp}.json"  # Имя файла по умолчанию
        )

        # Открываем диалог сохранения файла
        filename = filedialog.asksaveasfilename(
            initialdir="user_data//Configs/Exports",  # Директория по умолчанию
            initialfile=default_filename,  # Имя файла по умолчанию
            defaultextension=".json",  # Расширение файла по умолчанию
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],  # Типы файлов
        )

        if filename:
            # Создаем словарь с настройками
            settings_dict = {}  # Создаем словарь с настройками
            for section in config.sections():  # Проходим по всем секциям конфигурации
                settings_dict[section] = dict(
                    config[section]
                )  # Добавляем секцию и её настройки в словарь

            # Сохраняем настройки в JSON файл
            with open(
                filename, "w", encoding="utf-8"
            ) as f:  # Открываем файл для записи
                json.dump(
                    settings_dict, f, indent=4, ensure_ascii=False
                )  # Записываем настройки в файл

            # Копируем файлы конфигурации если они есть
            if os.path.exists(
                "user_data//Configs"
            ):  # Проверяем, есть ли директория Configs
                config_files = [
                    f for f in os.listdir("user_data//Configs") if f.endswith(".bat")
                ]  # Получаем все файлы с расширением .bat
                if config_files:  # Если есть файлы с расширением .bat
                    config_dir = (
                        os.path.splitext(filename)[0] + "_configs"
                    )  # Создаем директорию для файлов конфигурации
                    os.makedirs(
                        config_dir, exist_ok=True
                    )  # Создаем директорию для файлов конфигурации
                    for (
                        file
                    ) in config_files:  # Проходим по всем файлам с расширением .bat
                        shutil.copy2(
                            os.path.join("Configs", file), config_dir
                        )  # Копируем файлы конфигурации в директорию для файлов конфигурации

            print(
                "🎉 Настройки успешно экспортированы в", filename
            )  # Выводим сообщение о успешном экспорте настроек
            return True  # Возвращаем True
    except Exception as e:  # Если возникает ошибка
        print(
            f"❌ Ошибка при экспорте настроек: {str(e)}"
        )  # Выводим сообщение об ошибке
        return False  # Возвращаем False


def import_settings():  # Функция для импорта настроек
    try:  # Пробуем выполнить код
        # Открываем диалог выбора файла
        filename = filedialog.askopenfilename(
            initialdir="Configs/Exports",  # Директория по умолчанию
            title="Выберите файл настроек",  # Заголовок диалога
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],  # Типы файлов
        )

        if filename:
            # Читаем настройки из JSON файла
            with open(
                filename, "r", encoding="utf-8"
            ) as f:  # Открываем файл для чтения
                imported_settings = json.load(f)  # Загружаем настройки из JSON файла

            # Проверяем обязательные секции
            for (
                section,
                options,
            ) in (
                required_sections.items()
            ):  # Проходим по всем секциям в required_sections
                if (
                    section not in imported_settings
                ):  # Если секция не найдена в imported_settings
                    imported_settings[section] = (
                        options  # Добавляем секцию и её настройки в imported_settings
                    )
                else:
                    for (
                        key,
                        value,
                    ) in options.items():  # Проходим по всем ключам в options
                        if (
                            key not in imported_settings[section]
                        ):  # Если ключ не найден в imported_settings[section]
                            imported_settings[section][key] = (
                                value  # Добавляем ключ и его значение в imported_settings[section]
                            )

            # Обновляем конфигурацию
            for (
                section
            ) in imported_settings:  # Проходим по всем секциям в imported_settings
                if not config.has_section(section):  # Если секция не найдена в config
                    config.add_section(section)  # Добавляем секцию в config
                for key, value in imported_settings[
                    section
                ].items():  # Проходим по всем ключам в imported_settings[section]
                    config[section][key] = str(
                        value
                    )  # Добавляем ключ и его значение в config[section]

            # Сохраняем обновленную конфигурацию
            with open(
                "user_data//settings.ini", "w", encoding="utf-8"
            ) as configfile:  # Открываем файл для записи
                config.write(configfile)  # Записываем конфигурацию в файл

            # Импортируем файлы конфигурации если они есть
            config_dir = (
                os.path.splitext(filename)[0] + "_configs"
            )  # Создаем директорию для файлов конфигурации
            if os.path.exists(
                config_dir
            ):  # Проверяем, есть ли директория для файлов конфигурации
                os.makedirs(
                    "Configs", exist_ok=True
                )  # Создаем директорию для файлов конфигурации
                for file in os.listdir(
                    config_dir
                ):  # Проходим по всем файлам в директории для файлов конфигурации
                    if file.endswith(".bat"):  # Если файл имеет расширение .bat
                        shutil.copy2(
                            os.path.join(config_dir, file), "Configs"
                        )  # Копируем файлы конфигурации в директорию для файлов конфигурации

            # Перечитываем настройки
            config.read(
                "user_data//settings.ini", encoding="utf-8"
            )  # Читаем настройки из файла

            # Обновляем интерфейс
            update_theme()  # Обновляем тему интерфейса
            update_font()  # Обновляем шрифт интерфейса
            update_tooltip_state()  # Обновляем состояние всплывающих подсказок

            messagebox.showinfo(
                "✅ Успех", "🎉 Настройки успешно импортированы"
            )  # Выводим сообщение о успешном импорте настроек
            return True  # Возвращаем True
    except Exception as e:  # Если возникает ошибка
        messagebox.showerror(
            "❌ Ошибка", f"❌ Ошибка при импорте настроек: {str(e)}"
        )  # Выводим сообщение об ошибке
        return False  # Возвращаем False


# Инициализируем глобальную переменную для управления состоянием всплывающих подсказок
tooltips_enabled = True  # Состояние всплывающих подсказок

# В секции инициализации переменных добавить
fullscreen_var = tk.StringVar(
    value="Включено" if config.getboolean("Window", "fullscreen") else "Выключено"
)  # Состояние полноэкранного режима

# Словарь для сопоставления имен функций с пользовательскими названиями
function_to_tab_mapping = {
    "switch_to_main": "Главная",  # Имя функции для переключения на главную вкладку
    "switch_to_optimization": "Оптимизация",  # Имя функции для переключения на вкладку оптимизации
    "switch_to_drivers": "Драйверы",  # Имя функции для переключения на вкладку драйверов
    "switch_to_power": "Электропитание",  # Имя функции для переключения на вкладку электропитания
    "switch_to_clean": "Очистка",  # Имя функции для переключения на вкладку очистки
    "switch_to_other": "Другое",  # Имя функции для переключения на вкладку другое
    "switch_to_qqnwr": "QQNWR",  # Имя функции для переключения на вкладку QQNWR
    "switch_to_fixes": "Исправления",  # Имя функции для переключения на вкладку исправлений
    "switch_to_settings": "Настройки",  # Имя функции для переключения на вкладку настроек
    "switch_to_update": "Обновления",  # Имя функции для переключения на вкладку обновлений
    "switch_to_about": "О программе",  # Имя функции для переключения на вкладку о программе
    "switch_to_version": "Версия",  # Имя функции для переключения на вкладку версии
}

# В секции инициализации переменных добавить
initial_tab_var = tk.StringVar(
    value=function_to_tab_mapping.get(
        config.get("General", "initial_tab", fallback="switch_to_main"), "Главная"
    )
)  # Имя функции для переключения на главную вкладку

"""
+------------------------------------+
| Функция для обновления цветовой    |
| схемы интерфейса                   |
+------------------------------------+
"""


def update_colors():  # Функция для обновления цветовой схемы интерфейса
    try:  # Пробуем выполнить код
        with open(
            "user_data//settings.ini", "w", encoding="cp1251"
        ) as configfile:  # Открываем файл для записи
            config.write(configfile)  # Записываем конфигурацию в файл
        root.update()  # Обновляем интерфейс
    except Exception as e:  # Если возникает ошибка
        logger.log_error(
            "❌ Ошибка при обновлении цветов", exc_info=e
        )  # Выводим сообщение об ошибке


"""
+------------------------------------+
| Функция для получения имени кнопки |
| на основе имени вкладки            |
+------------------------------------+
"""


def get_button_name(
    tab_name,
):  # Функция для получения имени кнопки на основе имени вкладки
    """
    Функция для получения имени кнопки на основе имени вкладки.

    Эта функция выполняет следующие действия:
    1. Проверяет, в каком словаре вкладок находится tab_name
    2. Возвращает соответствующее имя кнопки

    Параметры:
    ----------
    tab_name : str
        Имя вкладки, для которой нужно получить имя кнопки

    Возвращает:
    -----------
    str
        Имя кнопки, соответствующее вкладке

    Пример использования:
    --------------------
    button_name = get_button_name("Оптимизация")  # Вернет "Оптимизация"

    Примечания:
    ----------
    - tabs_main - словарь с главными вкладками
    - tabs - словарь с вкладками оптимизации
    - tabs_1 - словарь с вкладками драйверов
    - tabs_2 - словарь с вкладками электропитания
    - tabs_3 - словарь с вкладками исправлений
    - tabs_4 - словарь с вкладками очистки
    - tabs_5 - словарь с другими вкладками
    - tabs_6 - словарь с вкладками настроек
    """
    # Проверяем, есть ли вкладка в словаре главных вкладок
    if tab_name in tabs_main:  # Если вкладка находится в словаре главных вкладок
        # Возвращаем имя кнопки для главных вкладок
        return "Главная"  # Возвращаем имя кнопки для главных вкладок
    # Проверяем, есть ли вкладка в словаре вкладок оптимизации
    elif tab_name in tabs:  # Если вкладка находится в словаре вкладок оптимизации
        # Возвращаем имя кнопки для вкладок оптимизации
        return "Оптимизация"  # Возвращаем имя кнопки для вкладок оптимизации
    # Проверяем, есть ли вкладка в словаре вкладок драйверов
    elif tab_name in tabs_1:  # Если вкладка находится в словаре вкладок драйверов
        # Возвращаем имя кнопки для вкладок драйверов
        return "Драйверы"  # Возвращаем имя кнопки для вкладок драйверов
    # Проверяем, есть ли вкладка в словаре вкладок электропитания
    elif tab_name in tabs_2:  # Если вкладка находится в словаре вкладок электропитания
        # Возвращаем имя кнопки для вкладок электропитания
        return "Электропитание"  # Возвращаем имя кнопки для вкладок электропитания
    # Проверяем, есть ли вкладка в словаре вкладок исправлений
    elif tab_name in tabs_3:  # Если вкладка находится в словаре вкладок исправлений
        # Возвращаем имя кнопки для вкладок исправлений
        return "Исправления"  # Возвращаем имя кнопки для вкладок исправлений
    # Проверяем, есть ли вкладка в словаре вкладок очистки
    elif tab_name in tabs_4:  # Если вкладка находится в словаре вкладок очистки
        # Возвращаем имя кнопки для вкладок очистки
        return "Очистка"  # Возвращаем имя кнопки для вкладок очистки
    # Проверяем, есть ли вкладка в словаре других вкладок
    elif tab_name in tabs_5:  # Если вкладка находится в словаре других вкладок
        # Возвращаем имя кнопки для других вкладок
        return "Другое"  # Возвращаем имя кнопки для других вкладок
    # Проверяем, есть ли вкладка в словаре вкладок настроек
    elif tab_name in tabs_qqnwr:  # Если вкладка находится в словаре вкладок QQNWR
        # Возвращаем имя кнопки для вкладок QQNWR
        return "QQNWR"  # Возвращаем имя кнопки для вкладок QQNWR
    elif tab_name in tabs_update:  # # Если вкладка находится в словаре других вкладок
        # Возвращаем имя кнопки для вкладок настроек
        return "Обновления"  # Возвращаем имя кнопки для вкладок настроек
    # Проверяем, есть ли вкладка в словаре вкладок настроек
    elif tab_name in tabs_6:  # Если вкладка находится в словаре вкладок настроек
        # Возвращаем имя кнопки для вкладок настроек
        return "Настройки"  # Возвращаем имя кнопки для вкладок настроек
    # Если вкладка не найдена ни в одном словаре
    return ""  # Возвращаем пустую строку


"""
+------------------------------------+
| Класс для создания всплывающих     |
| подсказок (ToolTip)                |
+------------------------------------+
"""


class ToolTip:  # Класс для создания всплывающих подсказок (ToolTip)
    def __init__(self, widget, filepath):  # Инициализация класса
        self.widget = widget  # Инициализируем widget
        self.filepath = filepath  # Инициализируем filepath
        self.tooltip = None  # Инициализируем tooltip
        self.widget.bind(
            "<Enter>", self.show_tooltip
        )  # Привязываем событие наведения к событию наведения
        self.widget.bind(
            "<Leave>", self.hide_tooltip
        )  # Привязываем событие наведения к событию наведения

        # Загружаем описания из файла
        self.descriptions = {}  # Инициализируем descriptions
        try:  # Пробуем выполнить код
            with open(
                "tweaks//descriptions.txt", "r", encoding="utf-8"
            ) as f:  # Открываем файл для чтения
                for line in f:  # Проходим по всем строкам в файле
                    if "=" in line:  # Если в строке есть '='
                        key, value = line.strip().split(
                            "=", 1
                        )  # Разделяем строку на ключ и значение
                        self.descriptions[key] = (
                            value  # Добавляем ключ и значение в descriptions
                        )
        except Exception as e:  # Если возникает ошибка
            print(
                f"❌ Ошибка при загрузке описаний: {str(e)}"
            )  # Выводим сообщение об ошибке

    def find_description(self, checkbox_name):  # Функция для поиска описания
        # Получаем имя файла из полного пути
        file_name = os.path.basename(
            checkbox_name
        )  # Получаем имя файла из полного пути

        # Сначала ищем точное совпадение
        if file_name in self.descriptions:  # Если имя файла находится в descriptions
            return self.descriptions[file_name]  # Возвращаем описание

        # Если точного совпадения нет, ищем частичное совпадение
        for key in self.descriptions:  # Проходим по всем ключам в descriptions
            if (
                key in file_name or file_name in key
            ):  # Если ключ находится в имени файла или имя файла находится в ключе
                return self.descriptions[key]  # Возвращаем описание
        return None  # Возвращаем None

    def format_description(self, text):  # Функция для форматирования описания
        # Разбиваем текст на предложения и добавляем перенос строки после каждой точки
        sentences = text.split(
            ". "
        )  # Разбиваем текст на предложения и добавляем перенос строки после каждой точки
        formatted_text = ".\n".join(
            sentences
        )  # Добавляем дополнительный перенос строки для лучшей читаемости
        return (
            formatted_text.replace("Плюсы:", "\nПлюсы:")
            .replace("Минусы:", "\nМинусы:")
            .replace("Рекомендуется", "\nРекомендуется")
        )  # Заменяем текст на форматированный текст

    def show_tooltip(self, event):  # Функция для отображения всплывающей подсказки
        global tooltips_enabled  # Объявляем переменную tooltips_enabled
        if not tooltips_enabled:  # Если всплывающие подсказки не включены
            return  # Возвращаем None

        x, y, _, _ = self.widget.bbox("insert")  # Получаем координаты виджета
        x += self.widget.winfo_rootx() + 25  # Увеличиваем смещение вправо
        y += self.widget.winfo_rooty() - 200  # Увеличиваем смещение вверх

        if x < 0:  # Если x меньше 0
            x = 0  # Устанавливаем x в 0
        if y < 0:  # Если y меньше 0
            y = 0  # Устанавливаем y в 0

        self.tooltip = tk.Toplevel(self.widget)  # Создаем всплывающее окно
        self.tooltip.wm_overrideredirect(True)  # Отключаем стандартные возможности окна

        tooltip_width = 600  # Устанавливаем ширину подсказки
        tooltip_height = 200  # Увеличиваем высоту подсказки
        self.tooltip.geometry(f"{tooltip_width}x{tooltip_height}+{x}+{y}")

        try:  # Пробуем выполнить код
            # Получаем имя чекбокса
            checkbox_name = self.widget["text"]  # Получаем имя чекбокса

            # Ищем описание
            description = self.find_description(checkbox_name)  # Получаем описание

            if description:  # Если описание есть
                # Форматируем описание, добавляя переносы строк
                formatted_description = self.format_description(
                    description
                )  # Форматируем описание
                label = tk.Label(
                    self.tooltip,  # Создаем метку
                    text=formatted_description,  # Устанавливаем текст метки
                    background="#190831",  # Темный фон
                    foreground="#32FBE2",  # Бирюзовый текст
                    relief="solid",  # Устанавливаем стиль рамки
                    borderwidth=3,  # Увеличиваем ширину рамки
                    highlightthickness=2,  # Добавляем толщину выделения
                    highlightbackground="#FFD700",  # Золотой цвет рамки
                    highlightcolor="#FFD700",  # Золотой цвет рамки при фокусе
                    wraplength=580,  # Устанавливаем максимальную ширину текста
                    justify=tk.LEFT,  # Выравнивание текста по левому краю
                    padx=10,  # Добавляем отступы
                    pady=10,  # Добавляем отступы
                )
            else:  # Если описания нет
                # Если описания нет, показываем содержимое файла
                current_tab = tab_control.select()  # Получаем текущую вкладку
                tab_text = tab_control.tab(
                    current_tab, "text"
                )  # Получаем текст вкладки
                button_name = get_button_name(tab_text)  # Получаем имя кнопки
                # Определяем папку для поиска файла
                base_folder = {
                    "Главная": "Главная",  # Главная
                    "Оптимизация": "Оптимизация",  # Оптимизация
                    "Драйверы": "Драйверы",  # Драйверы
                    "Электропитание": "Электропитание",  # Электропитание
                    "Исправления": "Исправления",  # Исправления
                    "Очистка": "Очистка",  # Очистка
                    "Другое": "Другое",  # Другое
                    "Настройки": "Настройки",  # Настройки
                    "Старые твики": "Старые твики",  # Старые твики
                    "QQNWR": "QQNWR",  # QQNWR
                }.get(button_name, button_name)  # Получаем имя папки

                rel_path = os.path.normpath(self.filepath).split(f"tweaks{os.sep}")[
                    -1
                ]  # Получаем путь к файлу
                full_path = os.path.join(
                    "tweaks", base_folder, rel_path
                )  # Получаем полный путь к файлу

                with open(full_path, "r", encoding="utf-8") as file:  # Открываем файл
                    file_content = file.read()  # Читаем содержимое файла
                    if (
                        len(file_content) > 1000
                    ):  # Если длина содержимого файла больше 1000 символов
                        file_content = (
                            file_content[:1000] + "..."
                        )  # Обрезаем содержимое файла
                    # Форматируем содержимое файла
                    formatted_content = self.format_description(
                        file_content
                    )  # Форматируем содержимое файла
                    label = tk.Label(
                        self.tooltip,  # Создаем метку
                        text=formatted_content,  # Устанавливаем текст метки
                        background="#190831",  # Темный фон
                        foreground="#32FBE2",  # Бирюзовый текст
                        relief="solid",  # Устанавливаем стиль рамки
                        borderwidth=3,  # Увеличиваем ширину рамки
                        highlightthickness=2,  # Добавляем толщину выделения
                        highlightbackground="#FFD700",  # Золотой цвет рамки
                        highlightcolor="#FFD700",  # Золотой цвет рамки при фокусе
                        wraplength=580,  # Устанавливаем максимальную ширину текста
                        justify=tk.LEFT,  # Выравнивание текста по левому краю
                        padx=10,  # Добавляем отступы
                        pady=10,  # Добавляем отступы
                    )

        except Exception as e:  # Если возникает ошибка
            error_message = f"Ошибка: {str(e)}"  # Сообщение об ошибке
            label = tk.Label(
                self.tooltip,  # Создаем метку
                text=error_message,  # Устанавливаем текст метки
                background="#190831",  # Темный фон
                foreground="#32FBE2",  # Бирюзовый текст
                relief="solid",  # Устанавливаем стиль рамки
                borderwidth=3,  # Увеличиваем ширину рамки
                highlightthickness=2,  # Добавляем толщину выделения
                highlightbackground="#FFD700",  # Золотой цвет рамки
                highlightcolor="#FFD700",  # Золотой цвет рамки при фокусе
                wraplength=580,  # Устанавливаем максимальную ширину текста
                justify=tk.LEFT,  # Выравнивание текста по левому краю
                padx=10,  # Добавляем отступы
                pady=10,  # Добавляем отступы
            )

        label.pack(fill=tk.BOTH, expand=True)  # Упаковываем метку

    def hide_tooltip(self, event):  # Функция для скрытия всплывающей подсказки
        if self.tooltip:  # Если всплывающая подсказка существует
            self.tooltip.destroy()  # Удаляем всплывающую подсказку
            self.tooltip = None  # Удаляем всплывающую подсказку
        self.tooltip = None  # Удаляем всплывающую подсказку


"""
+----------------------------------------------+
| Функция для выделения всех элементов в табах |
+----------------------------------------------+
"""


def select_all_for_tabs(tab_frame):  # Функция для выделения всех элементов в табах
    # Проходим по всем чекбоксам и устанавливаем их значение в True
    for checkbox in checkboxes.values():  # Проходим по всем чекбоксам
        checkbox.set(True)  # Устанавливаем состояние чекбокса в True


def switch_to_select():
    # Получаем текущую активную вкладку
    current_tab = tab_control.select()
    if not current_tab:
        return

    # Получаем имя текущей вкладки напрямую из tab_control
    current_tab_name = tab_control.tab(current_tab, "text")

    # Выделяем чекбоксы только в текущей вкладке
    for checkbox_name, checkbox_var in checkboxes.items():
        if get_tab_name(checkbox_name) == current_tab_name:
            checkbox_var.set(True)


"""
+----------------------------------------+
| Функция для выполнения старых скриптов |
+----------------------------------------+
"""
def offer_backup():
    """Предлагает пользователю создать бэкап реестра при запуске программы"""
    if messagebox.askyesno(
        "Резервное копирование",
        "Рекомендуется создать резервную копию реестра перед использованием твикера.\n\nСоздать резервную копию сейчас?",
        icon='warning'
    ):
        export_full_registry()

def execute_old():  # Функция для выполнения старых скриптов
    if config["General"].getboolean("ad_enabled", True):
        open_random_site(5)
    offer_backup()
    for checkbox_name, checkbox_var in checkboxes.items():  # Проходим по всем чекбоксам
        if checkbox_var.get():  # Если чекбокс включен
            tab_name = get_tab_name(checkbox_name)  # Получаем имя вкладки

            # Проверяем, что tab_name не None
            if tab_name is None:  # Если имя вкладки не определено
                logger.log_error(
                    f"Ошибка: Не удалось определить вкладку для {checkbox_name}"
                )  # Логируем ошибку
                continue  # Пропускаем текущий чекбокс

            # Определяем имя кнопки на основе словаря
            button_name = get_button_name(tab_name)  # Получаем имя кнопки

            # Формируем путь к скрипту
            tweak_path = f"tweaks\\{button_name}\\{tab_name}\\{checkbox_name}"  # Получаем путь к скрипту

            print(f"{checkbox_name} - {tweak_path}")  # Выводим путь к скрипту
            logger.log_tweak_execution(
                checkbox_name, tweak_path
            )  # Логируем выполнение скрипта

            """
            +----------------------------------------+
            | Запуск скриптов различных типов        |
            +----------------------------------------+
            """

            # Если скрипт имеет расширение .bat, .cmd или .exe
            if checkbox_name.endswith((".bat", ".cmd", ".exe")):
                subprocess.call(f'cmd /c "{tweak_path}"', shell=True)
                # os.system(f'cmd /c "{tweak_path}"')

            # Если скрипт имеет расширение .ps1
            elif checkbox_name.endswith(".ps1"):
                logger.log_info("использование JetBrains WinElevator")
                subprocess.run(
                    [
                        "Utils\\launcher.exe",
                        f'powershell.exe -ExecutionPolicy Bypass -File "{tweak_path}"',
                    ]
                )
                # os.system(f'powershell.exe -ExecutionPolicy Bypass -File "{tweak_path}"')

            # Если скрипт имеет расширение .reg
            elif checkbox_name.endswith(".reg"):
                subprocess.call(f'cmd /c "{tweak_path}"', shell=True)
                # os.system(f'cmd /c "{tweak_path}"')

            # Если скрипт имеет расширение .pow
            elif checkbox_name.endswith(".pow"):
                subprocess.call(f'powercfg /import "{tweak_path}"', shell=True)
                subprocess.call(f'cmd /c "{tweak_path}"', shell=True)
                # os.system(f'powercfg /import "{tweak_path}"')
                # os.system(f'cmd /c "{tweak_path}"')
                # отправка сообщения в телеграм
                from telemetry.telemetry_manager import TelemetryManager

                manager = TelemetryManager()
                manager.send_message(
                    f"✅ План питания {checkbox_name} импортирован\n\n"
                )

            # Если скрипт не имеет расширение .bat, .cmd, .exe, .ps1 или .reg
            else:
                subprocess.call(f'cmd /c "{tweak_path}"', shell=True)
                # os.system(f'cmd /c "{tweak_path}"')


"""
+------------------------------------+
| Функция для создания batch файла   |
| на основе выбранных чекбоксов      |
+------------------------------------+
"""


def create_batch_file(
    activated_checkboxes,
):  # Функция для создания batch файла на основе выбранных чекбоксов
    # """
    # Функция для создания batch файла на основе выбранных чекбоксов.

    # Эта функция выполняет следующие действия:
    # 1. Создает уникальное имя файла с текущей датой и временем
    # 2. Создает директорию Configs, если она не существует
    # 3. Записывает команды в batch файл для каждого выбранного чекбокса

    # Параметры:
    # ----------
    # activated_checkboxes : list
    #     Список имен выбранных чекбоксов

    # Возвращает:
    # -----------
    # str
    #     Путь к созданному batch файлу

    # Пример использования:
    # --------------------
    # filename = create_batch_file(["чекбокс1", "чекбокс2"])
    # # Создаст файл Configs\Config All Tweaker 2024-03-20 12-30-45.bat

    # Примечания:
    # ----------
    # - Batch файл - это текстовый файл с расширением .bat, содержащий команды для выполнения
    # - @echo off - отключает вывод команд в консоль
    # - chcp 65001 - устанавливает кодировку UTF-8 для корректного отображения русских символов
    # - cmd /c - выполняет команду и закрывает консоль
    # """
    # Создаем уникальное имя файла с текущей датой и временем
    # datetime.now() - текущая дата и время
    # strftime - форматирует дату и время в строку
    filename = f"Configs\\Config All Tweaker {datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.bat"  # Создаем уникальное имя файла с текущей датой и временем

    # Создаем директорию Configs, если она не существует
    # exist_ok=True - не вызывает ошибку, если директория уже существует
    os.makedirs(
        "Configs", exist_ok=True
    )  # Создаем директорию Configs, если она не существует

    # Открываем файл для записи в кодировке UTF-8
    with open(
        filename, "w", encoding="utf-8"
    ) as f:  # Открываем файл для записи в кодировке UTF-8
        # Записываем команду для отключения вывода команд
        f.write("@echo off\n")
        # Устанавливаем кодировку UTF-8
        f.write("chcp 65001\n")

        # Для каждого выбранного чекбокса
        for (
            checkbox_name,
            checkbox_var,
        ) in checkboxes.items():  # Проходим по всем чекбоксам
            # Если чекбокс выбран (его значение True)
            if checkbox_var.get():  # Если чекбокс выбран (его значение True)
                # Получаем имя вкладки для чекбокса
                tab_name = get_tab_name(
                    checkbox_name
                )  # Получаем имя вкладки для чекбокса

                # Получаем имя кнопки на основе имени вкладки
                button_name = get_button_name(
                    tab_name
                )  # Получаем имя кнопки на основе имени вкладки

                # Записываем команду для выполнения скрипта
                # tweaks\\{button_name}\\{tab_name}\\{checkbox_name} - путь к скрипту
                f.write(
                    f'cmd /c "tweaks\\{button_name}\\{tab_name}\\{checkbox_name}"\n'
                )  # Записываем команду для выполнения скрипта

    # Возвращаем путь к созданному файлу
    return filename


"""
+---------------------------------------------------+
| Функция для обновления списка файлов конфигурации |
+---------------------------------------------------+
"""


def update_config_file_list():  # Функция для обновления списка файлов конфигурации
    global config_file_values  # Объявляем переменную как глобальную
    config_file_values = [
        f for f in os.listdir("Configs") if f.endswith(".bat")
    ]  # Получаем список .bat файлов


"""
+------------------------------------+
| Основная функция выполнения        |
| конфигурационного файла            |
+------------------------------------+
"""


def execute():  # Основная функция выполнения конфигурационного файла
    # Собираем все выбранные чекбоксы
    activated_checkboxes = [
        checkbox_name
        for checkbox_name, checkbox_var in checkboxes.items()
        if checkbox_var.get()
    ]
    if (
        execute_function_var.get() == "Создать конфиг"
    ):  # Если функция выполнения - "Создать конфиг"
        filename = create_batch_file(
            activated_checkboxes
        )  # Создаем конфигурационный файл
        update_config_file_list()  # Обновляем список файлов конфигурации
    elif (
        execute_function_var.get() == "Выполнить"
    ):  # Если функция выполнения - "Выполнить"
        execute_old()  # Вызов функции для выполнения старых скриптов


"""
+------------------------------------+
| Функция для выполнения             |
| конфигурационного файла            |
+------------------------------------+
"""


def execute_config():  # Функция для выполнения конфигурационного файла
    selected_file = config_file_var.get()  # Получаем выбранный файл
    if selected_file:  # Если файл выбран
        print(f"Start Configs\\{selected_file}")  # Выводим путь к файлу
        subprocess.call(
            f'Utils\\launcher.exe "Configs\\{selected_file}"', shell=True
        )  # Выполняем файл


"""
+------------------------------------+
| Функция для получения имени вкладки|
| по имени чекбокса                  |
+------------------------------------+
"""


def get_tab_name(
    checkbox_name,
):  # Функция для получения имени вкладки по имени чекбокса
    """
    Функция для определения имени вкладки по имени чекбокса.

    Эта функция выполняет следующие действия:
    1. Проверяет, к какому словарю относится чекбокс
    2. Возвращает имя вкладки, в которой находится чекбокс

    Параметры:
    ----------
    checkbox_name : str
        Имя чекбокса, для которого нужно найти вкладку

    Возвращает:
    -----------
    str
        Имя вкладки, в которой находится чекбокс

    Пример использования:
    --------------------
    tab_name = get_tab_name("чекбокс1")
    # Возвращает "System" если чекбокс находится во вкладке System

    Примечания:
    ----------
    - Функция проверяет все словари: tabs_main, tabs, tabs_1, tabs_2, etc.
    - Если чекбокс не найден ни в одном словаре, возвращает None
    """
    # Проверяем все словари вкладок
    for tab_dict in [
        tabs_main,
        tabs,
        tabs_1,
        tabs_2,
        tabs_3,
        tabs_4,
        tabs_5,
        tabs_6,
        tabs_qqnwr,
        tabs_update,
    ]:  # Проходим по всем словарям вкладок
        for (
            tab_name,
            checkbox_list,
        ) in tab_dict.items():  # Проходим по всем вкладкам в словаре
            if (
                checkbox_name in checkbox_list
            ):  # Если чекбокс найден в списке чекбоксов вкладки
                return tab_name  # Возвращаем имя вкладки

    # Если чекбокс не найден ни в одном словаре, возвращаем None
    return None  # Возвращаем None


"""
+------------------------------------+
| Функция для перезапуска процесса   |
+------------------------------------+
"""


def collect_and_send():  # Функция для сбора и отправки телеметрии
    from telemetry.telemetry_manager import (
        TelemetryManager,
    )  # Импортируем класс TelemetryManager из модуля telemetry_manager

    manager = TelemetryManager()  # Создаем экземпляр класса TelemetryManager
    logger.logger.info(
        "Начало сбора и отправки телеметрии..."
    )  # Логируем начало сбора и отправки телеметрии
    if manager.collect_telemetry_data():  # Если телеметрия успешно собрана
        logger.logger.info(
            "Телеметрия успешно собрана и отправлена"
        )  # Логируем успешное собрание и отправку телеметрии
        print(
            "Телеметрия успешно собрана и отправлена"
        )  # Выводим сообщение о успешном собрании и отправке телеметрии
    else:  # Если телеметрия не собрана
        logger.logger.error(
            "Ошибка при сборе и отправке телеметрии"
        )  # Логируем ошибку при сборе и отправке телеметрии
        print(
            "Ошибка при сборе и отправке телеметрии"
        )  # Выводим сообщение об ошибке при сборе и отправке телеметрии


def restart():  # Функция для перезапуска программы
    root.destroy()  # Закрываем окно
    root.quit()  # Закрываем программу


# Настраиваем основные цвета и стили
style = ttk.Style()  # Создаем объект стиля
style.configure(".", font=("Segoe UI", 10))  # Настраиваем шрифт для всех виджетов
style.configure("TNotebook.Tab", font=("Segoe UI", 10))  # Настраиваем шрифт для вкладок

# Настраиваем стиль для кнопок
style.configure(
    "Custom.TButton",
    font=("Segoe UI", 10),  # Настраиваем шрифт для кнопок
    padding=5,  # Отступы внутри кнопки
    relief="solid",  # Делаем обводку видимой
    borderwidth=1,  # Делаем обводку видимой
)

# Настраиваем стиль для вкладок
style.configure(
    "TNotebook.Tab",
    padding=[10, 5],  # Отступы внутри вкладок
    font=("Segoe UI", 10),  # Настраиваем шрифт для вкладок
)

# Создаем пустой словарь для хранения переменных состояния чекбоксов
checkboxes = {}

# Список доступных шрифтов
font_family_values = [
    "scode18",
    "Segoe UI",
    "Rust",
    "Foxy",
    "Frizon",
    "Velocity",
    "Roboto",
    "Montserrat",
    "Lato",
    "Open Sans",
    "Nunito",
    "Arial",
    "Times New Roman",
    "Verdana",
    "Georgia",
    "Courier New",
    "Ubuntu",
    "Ubuntu Mono",
    "Ubuntu Condensed",
    "Ubuntu Light",
    "Ubuntu Bold",
    "System",
    "Terminal",
    "Small Fonts",
    "Fixedsys",
    "hooge 05_53",
    "hooge 05_54",
    "hooge 05_55",
]

# Инициализация всех переменных
font_size_var = tk.IntVar(value=12)  # Переменная для хранения размера шрифта
theme_var = tk.StringVar(
    value=config["General"]["theme"]
)  # Переменная для хранения темы
search_entry_var = tk.StringVar()  # Переменная для хранения поискового запроса
execute_function_var = tk.StringVar(
    value="Выполнить"
    if "Execute" not in config or "execute_function" not in config["Execute"]
    else config["Execute"]["execute_function"]
)  # Переменная для хранения функции выполнения
config_file_var = tk.StringVar()  # Переменная для хранения файла конфигурации
font_family_var = tk.StringVar(
    value=config["General"]["font_family"]
)  # Переменная для хранения шрифта

# Инициализация списка файлов конфигурации
config_file_values = (
    [f for f in os.listdir("Configs") if f.endswith(".bat")]
    if os.path.exists("Configs")
    else []
)

# Получаем размер поля конфигурации из настроек
width = int(float(config["General"].get("size_of_the_config_field", "1.5")) * 30)

# Загружаем состояние подсказок из конфигурации
if "General" not in config:  # Если General нет в конфигурации
    config["General"] = {}  # Создаем пустой словарь для General
if "tooltips_enabled" not in config["General"]:  # Если tooltips_enabled нет в General
    config["General"]["tooltips_enabled"] = (
        "True"  # Устанавливаем tooltips_enabled в True
    )
tooltip_control_var = tk.StringVar(
    value="Включено"
    if config["General"].getboolean("tooltips_enabled", True)
    else "Выключено"
)  # Переменная для хранения состояния подсказок
tooltips_enabled = config["General"].getboolean(
    "tooltips_enabled", True
)  # Получаем состояние подсказок

# Переменные для хранения текущих значений шрифта и темы
checkbox_current_font = (
    config["General"]["font_family"],
    int(config["General"]["checkbox_font_size"]),
)  # Переменная для хранения текущего шрифта и размера шрифта для чекбоксов
current_font = (
    config["General"]["font_family"],
    int(config["General"]["font_size"]),
)  # Переменная для хранения текущего шрифта и размера шрифта
current_theme = config["General"]["theme"]  # Переменная для хранения темы

# Создаем главный контейнер
main_container = ttk.Frame(root)  # Создаем главный контейнер
main_container.pack(
    fill="both", expand=True, padx=20, pady=20
)  # Упаковываем главный контейнер

# Создаем верхнюю панель
top_panel = ttk.Frame(main_container)  # Создаем верхнюю панель
top_panel.pack(fill="x", pady=(0, 20))  # Упаковываем верхнюю панель

# Создаем логотип и заголовок
title_frame = ttk.Frame(top_panel)  # Создаем логотип и заголовок
title_frame.pack(side="left")  # Упаковываем логотип и заголовок

title_label = ttk.Label(
    title_frame, text="All Tweaker", font=("Segoe UI", 24, "bold")
)  # Создаем заголовок
title_label.pack(side="left")  # Упаковываем заголовок

version_label = ttk.Label(
    title_frame, text=version, font=("Segoe UI", 12)
)  # Создаем версию
version_label.pack(side="left", padx=(10, 0), pady=(10, 0))  # Упаковываем версию

# Создаем правую часть верхней панели
top_right_panel = ttk.Frame(top_panel)  # Создаем правую часть верхней панели
top_right_panel.pack(side="right", fill="y")  # Упаковываем правую часть верхней панели

# Поле поиска с иконкой
search_frame = ttk.Frame(top_right_panel)  # Создаем поле поиска с иконкой
search_frame.pack(side="left", padx=(0, 10))  # Упаковываем поле поиска с иконкой

"""
+------------------------------------+
| Функция для фильтрации чекбоксов   |
| на основе поискового запроса       |
+------------------------------------+
"""


def filter_checkboxes(
    *args,
):  # Функция для фильтрации чекбоксов на основе поискового запроса
    search_text = search_entry_var.get().lower()  # Получаем поисковый запрос
    if (
        search_text == "поиск..."
    ):  # Если текст равен "поиск...", считаем что поиск пустой
        search_text = ""  # Если текст равен "поиск...", считаем что поиск пустой

    # Проходим по всем вкладкам
    for tab_id in tab_control.tabs():  # Проходим по всем вкладкам
        tab_frame = tab_control.children[tab_id.split(".")[-1]]  # Получаем вкладку

        # Если вкладка не загружена, загружаем её
        if (
            not hasattr(tab_frame, "tab_info") or not tab_frame.tab_info["loaded"]
        ):  # Если вкладка не загружена, загружаем её
            if hasattr(tab_frame, "tab_info"):  # Если вкладка загружена, загружаем её
                create_tab_content(
                    tab_frame.tab_info["name"],
                    tab_frame,
                    tab_frame.tab_info["checkbox_names"],
                )  # Загружаем вкладку
                tab_frame.tab_info["loaded"] = (
                    True  # Устанавливаем флаг загрузки в True
                )

        # Получаем все чекбоксы на вкладке
        for (
            widget
        ) in tab_frame.winfo_children():  # Проходим по всем виджетам на вкладке
            if isinstance(widget, ttk.Frame):  # Ищем canvas_frame
                for (
                    inner_widget
                ) in widget.winfo_children():  # Проходим по всем виджетам на вкладке
                    if isinstance(inner_widget, tk.Canvas):  # Находим canvas
                        canvas = inner_widget  # Получаем canvas
                        inner_frame = canvas.children[
                            "!frame"
                        ]  # Получаем внутренний фрейм
                        for checkbox in (
                            inner_frame.winfo_children()
                        ):  # Проходим по всем виджетам на вкладке
                            if isinstance(
                                checkbox, ttk.Checkbutton
                            ):  # Если виджет является чекбоксом
                                # Показываем или скрываем чекбокс в зависимости от поискового запроса
                                if (
                                    search_text
                                    and search_text not in checkbox["text"].lower()
                                ):  # Если поисковый запрос не пустой и не содержит текст чекбокса
                                    checkbox.grid_remove()  # Скрываем чекбокс
                                else:  # Если поисковый запрос не пустой и содержит текст чекбокса
                                    checkbox.grid()  # Показываем чекбокс

        # Обновляем прокрутку для каждой вкладки
        if (
            hasattr(tab_frame, "tab_info") and tab_frame.tab_info["loaded"]
        ):  # Если вкладка загружена
            for (
                widget
            ) in tab_frame.winfo_children():  # Проходим по всем виджетам на вкладке
                if isinstance(widget, ttk.Frame):  # Если виджет является фреймом
                    for inner_widget in (
                        widget.winfo_children()
                    ):  # Проходим по всем виджетам на вкладке
                        if isinstance(
                            inner_widget, tk.Canvas
                        ):  # Если виджет является canvas
                            inner_widget.config(
                                scrollregion=inner_widget.bbox("all")
                            )  # Обновляем прокрутку для каждой вкладки


# Поле поиска
search_entry = ttk.Entry(
    search_frame,  # Создаем поле поиска
    textvariable=search_entry_var,  # Связываем поле поиска с переменной поискового запроса
    width=30,  # Ширина поля поиска
    font=("Segoe UI", 10),  # Шрифт поля поиска
    style="TEntry",
)  # Применяем новый стиль
search_entry.pack(side="left")  # Упаковываем поле поиска
search_entry.insert(0, "Поиск...")  # Вставляем текст "Поиск..." в поле поиска

# Привязываем события к полю поиска
search_entry_var.trace("w", filter_checkboxes)  # Отслеживаем изменения в поле поиска
search_entry.bind(
    "<FocusIn>",
    lambda e: search_entry.delete(0, "end")
    if search_entry.get() == "Поиск..."
    else None,
)  # Привязываем событие к полю поиска
search_entry.bind(
    "<FocusOut>",
    lambda e: (search_entry.insert(0, "Поиск..."), filter_checkboxes())
    if search_entry.get() == ""
    else None,
)  # Привязываем событие к полю поиска


# Кнопка "Выделить все"
def switch_to_select():
    # Получаем текущую активную вкладку
    current_tab = tab_control.select()
    if not current_tab:
        return

    # Получаем имя текущей вкладки напрямую из tab_control
    current_tab_name = tab_control.tab(current_tab, "text")

    # Выделяем чекбоксы только в текущей вкладке
    for checkbox_name, checkbox_var in checkboxes.items():
        if get_tab_name(checkbox_name) == current_tab_name:
            checkbox_var.set(True)


select_all_button = ttk.Button(
    top_right_panel,
    text="Выделить все",
    bootstyle="warning-outline",
    command=switch_to_select,
)  # Создаем кнопку "Выделить все"
select_all_button.pack(side="left", padx=5)  # Упаковываем кнопку "Выделить все"


# Кнопка "Донат"
def open_donat():
    import webbrowser

    webbrowser.open("https://www.tinkoff.ru/cf/2VBH9zSztcW")
    donat_button.pack_forget()  # Убираем кнопку после нажатия
    # отключаем рекламу в конфигурации
    config["General"]["ad_enabled"] = (
        "False"  # Используем строку вместо булева значения
    )
    with open("user_data//settings.ini", "w", encoding="cp1251") as configfile:
        config.write(configfile)


# проверяем включена ли реклама в конфигурации
if config["General"].getboolean("ad_enabled", True):
    donat_button = ttk.Button(
        top_right_panel, text="Донат", bootstyle="warning-outline", command=open_donat
    )
    donat_button.pack(side="left", padx=5)
else:
    # donat_button.pack_forget()
    pass


# Кнопка "Реклама"
def open_youtube():
    import webbrowser

    webbrowser.open("https://shre.su/0KO3")
    ad_button.pack_forget()  # Убираем кнопку после нажатия
    # отключаем рекламу в конфигурации
    config["General"]["ad_enabled"] = (
        "False"  # Используем строку вместо булева значения
    )
    with open("user_data//settings.ini", "w", encoding="cp1251") as configfile:
        config.write(configfile)


# проверяем включена ли реклама в конфигурации
if config["General"].getboolean("ad_enabled", True):
    ad_button = ttk.Button(
        top_right_panel,
        text="Бесплатно поддержать",
        bootstyle="info-outline",
        command=open_youtube,
    )
    ad_button.pack(side="left", padx=5)
else:
    # ad_button.pack_forget()
    pass

# Кнопки управления
execute_button = ttk.Button(
    top_right_panel, text="Выполнить", bootstyle="success-outline", command=execute_old
)  # Создаем кнопку "Выполнить"
execute_button.pack(side="left", padx=5)  # Упаковываем кнопку "Выполнить"


# Кнопка "Перезагрузка Windows"
def restart_windows():
    question = messagebox.askyesno(
        "Перезагрузка Windows", "Вы уверены, что хотите перезагрузить Windows?"
    )
    if question:
        os.system("shutdown /r /t 0")


# Кнопка "Свернуть"
def minimize_window():
    root.iconify()


# Кнопка "Свернуть"
minimize_button = ttk.Button(
    top_right_panel, text="_", bootstyle="danger-outline", command=minimize_window
)  # Создаем кнопку "Свернуть"
minimize_button.pack(side="left", padx=5)  # Упаковываем кнопку "Свернуть"


# Кнопка "Restore"
def restore_window():
    # если программа в полноэкранном режиме, то свернуть
    if root.attributes("-fullscreen"):
        root.attributes("-fullscreen", False)
    # если программа в обычном режиме, то развернуть
    else:
        root.attributes("-fullscreen", True)


# Кнопка "Restore"
restore_button = ttk.Button(
    top_right_panel, text=" ", bootstyle="danger-outline", command=restore_window
)  # Создаем кнопку "Restore"
restore_button.pack(side="left", padx=5)  # Упаковываем кнопку "Restore"

# Кнопка "Выйти"
exit_button = ttk.Button(
    top_right_panel, text="X", bootstyle="danger-outline", command=restart
)  # Создаем кнопку "Выйти"
exit_button.pack(side="left", padx=5)  # Упаковываем кнопку "Выйти"

# Создаем контейнер для вкладок и боковой панели
content_container = ttk.Frame(
    main_container
)  # Создаем контейнер для вкладок и боковой панели
content_container.pack(
    fill="both", expand=True
)  # Упаковываем контейнер для вкладок и боковой панели

# Создаем боковую панель для быстрого доступа
sidebar = ttk.Frame(
    content_container, style="Card.TFrame"
)  # Создаем боковую панель для быстрого доступа
sidebar.pack(
    side="left", fill="y", padx=(0, 20)
)  # Упаковываем боковую панель для быстрого доступа

"""
+------------------------------------+
| Функция для обновления значения    |
| функции выполнения в конфигурации  |
+------------------------------------+
"""


def update_execute_function(event=None):
    config.set(
        "Execute", "execute_function", execute_function_var.get()
    )  # Обновляем значение функции выполнения в конфигурации
    with open(
        "user_data//settings.ini", "w", encoding="cp1251"
    ) as configfile:  # Запись в ANSI
        config.write(configfile)  # Запись в ANSI


"""
+------------------------------------+
| Функция для обновления состояния   |
| подсказок                          |
+------------------------------------+
"""


def update_tooltip_state(*args):  # Функция для обновления состояния подсказок
    try:  # Попробуем обновить состояние подсказок
        global tooltips_enabled  # Объявляем переменную tooltips_enabled
        old_value = tooltips_enabled  # Сохраняем старое значение tooltips_enabled
        tooltips_enabled = (
            tooltip_control_var.get() == "Включено"
        )  # Обновляем значение tooltips_enabled
        config["General"]["tooltips_enabled"] = str(
            tooltips_enabled
        )  # Обновляем значение tooltips_enabled в конфигурации
        with open(
            "user_data//settings.ini", "w", encoding="cp1251"
        ) as configfile:  # Запись в ANSI
            config.write(configfile)  # Запись в ANSI
        logger.log_settings_change(
            "tooltips_enabled", old_value, tooltips_enabled
        )  # Логируем изменение состояния подсказок
    except Exception as e:  # Если возникает ошибка
        logger.log_error(
            "Ошибка при обновлении состояния подсказок", exc_info=e
        )  # Логируем ошибку


"""
+------------------------------------+
| Функция для обновления стиля       |
| элементов интерфейса с учетом      |
| заданного шрифта                   |
+------------------------------------+
"""


def update_font_style():
    style = ttk.Style()  # Создаем объект стиля
    # Обновляем стили без кастомных цветов
    style.configure("TLabel", font=current_font)  # Обновляем стиль для Label
    style.configure("TButton", font=current_font)  # Обновляем стиль для Button
    style.configure(
        "TCheckbutton", font=checkbox_current_font
    )  # Изменено на стандартный стиль
    style.configure("TCombobox", font=current_font)  # Обновляем стиль для Combobox
    style.configure(
        "TNotebook.Tab", font=current_font
    )  # Обновляем стиль для Notebook.Tab
    style.configure(
        "Custom.TButton", font=current_font
    )  # Обновляем стиль для Custom.TButton

    root.update()  # Обновляем окно


"""
+------------------------------------+
| Функция для обновления текущей     |
| темы интерфейса                    |
+------------------------------------+
"""


# функция для обновления стиля кнопок при смене на любые темы
def update_button_style():
    # Создаем новый стиль для кнопок
    style.configure("Icon.TButton", font=("Segoe UI", 16), padding=10, width=3)

    # Список светлых тем
    light_themes = [
        "cosmo",
        "flatly",
        "litera",
        "minty",
        "lumen",
        "sandstone",
        "yeti",
        "pulse",
        "united",
        "morph",
        "journal",
        "simplex",
        "cerculean",
        "green",
    ]

    # Настраиваем цвета в зависимости от темы
    if current_theme in light_themes:
        style.configure("Icon.TButton", background="#f0f0f0", foreground="black")
    if current_theme == "wincry_warning":
        style.configure("Icon.TButton", background="#1a1a1a", foreground="#f0ad4e")
    else:
        style.configure("Icon.TButton", background="#1a1a1a", foreground="white")


def update_theme(event=None):  # Функция для обновления темы интерфейса
    try:  # Попробуем обновить тему интерфейса
        global current_theme  # Объявляем переменную current_theme
        new_theme = theme_var.get()  # Получаем новое значение темы
        if (
            new_theme != current_theme
        ):  # Если новое значение темы не равно текущему значению темы
            old_theme = current_theme  # Сохраняем старое значение темы

            # Обновляем остальные настройки
            update_colors()  # Обновляем цвета
            update_font()  # Обновляем шрифт
            config["General"]["theme"] = (
                new_theme  # Обновляем значение темы в конфигурации
            )
            with open(
                "user_data//settings.ini", "w", encoding="cp1251"
            ) as configfile:  # Запись в ANSI
                config.write(configfile)  # Запись в ANSI
            logger.log_settings_change(
                "theme", old_theme, new_theme
            )  # Логируем изменение темы

            # перезапускаем программу
            reload_program()
    except Exception as e:  # Если возникает ошибка
        logger.log_error("Ошибка при обновлении темы", exc_info=e)  # Логируем ошибку


"""
+------------------------------------+
| Функция для обновления текущей     |
| темы интерфейса                    |
+------------------------------------+
"""


def update_font(event=None):  # Функция для обновления шрифта
    try:  # Попробуем обновить шрифт
        global checkbox_current_font  # Объявляем переменную checkbox_current_font
        font_family = font_family_var.get()  # Получаем новое значение шрифта
        checkbox_font_size = font_size_var.get()  # Получаем новое значение шрифта
        old_font = checkbox_current_font  # Сохраняем старое значение шрифта
        checkbox_current_font = (
            font_family,
            checkbox_font_size,
        )  # Обновляем значение шрифта

        global current_font  # Объявляем переменную current_font
        current_font = (
            font_family,
            int(config["General"]["font_size"]),
        )  # Обновляем значение шрифта

        update_font_style()  # Обновляем стиль шрифта
        config["General"]["font_family"] = (
            font_family  # Обновляем значение шрифта в конфигурации
        )
        config["General"]["checkbox_font_size"] = str(
            checkbox_font_size
        )  # Обновляем значение шрифта в конфигурации
        with open(
            "user_data//settings.ini", "w", encoding="cp1251"
        ) as configfile:  # Запись в ANSI
            config.write(configfile)  # Запись в ANSI
        logger.log_settings_change(
            "font_settings", old_font, checkbox_current_font
        )  # Логируем изменение шрифта
        root.update_idletasks()  # Обновляем окно
        root.update()  # Обновляем окно
    except Exception as e:  # Если возникает ошибка
        logger.log_error("Ошибка при обновлении шрифта", exc_info=e)  # Логируем ошибку


def create_tab_content(
    tab_name, tab_frame, checkbox_names
):  # Функция для создания содержимого вкладки
    # Очищаем существующее содержимое вкладки
    for widget in tab_frame.winfo_children():  # Проходим по всем виджетам на вкладке
        widget.destroy()  # Удаляем виджет

    # Создаем основной контейнер для вкладки
    main_container = ttk.Frame(tab_frame)  # Создаем основной контейнер для вкладки
    main_container.pack(
        fill=tk.BOTH, expand=True
    )  # Упаковываем основной контейнер для вкладки

    # Создаем фрейм для поиска
    search_frame = ttk.Frame(main_container)
    search_frame.pack(fill="x", padx=10, pady=(20, 5))

    # Создаем поле поиска
    search_var = tk.StringVar()
    search_entry = ttk.Entry(
        search_frame, textvariable=search_var, font=("Segoe UI", 10)
    )
    search_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))

    # Создаем кнопку поиска
    search_button = ttk.Button(search_frame, text="Поиск", bootstyle="info-outline")
    # search_button.pack(side='right')

    # Создаем канвас с вертикальным и горизонтальным скроллбарами
    canvas = tk.Canvas(main_container)  # Создаем канвас

    # Создаем вертикальный скроллбар
    v_scrollbar = ttk.Scrollbar(
        main_container, orient=tk.VERTICAL, command=canvas.yview
    )  # Создаем вертикальный скроллбар
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Упаковываем вертикальный скроллбар

    # Создаем горизонтальный скроллбар
    h_scrollbar = ttk.Scrollbar(
        tab_frame, orient=tk.HORIZONTAL, command=canvas.xview
    )  # Создаем горизонтальный скроллбар
    h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)  # Упаковываем горизонтальный скроллбар

    # Размещаем канвас
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Упаковываем канвас

    # Настраиваем привязку скроллбаров к холсту
    canvas.configure(
        xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set
    )  # Настраиваем привязку скроллбаров к холсту

    # Создаем внутренний фрейм для контента
    inner_frame = ttk.Frame(canvas)  # Создаем внутренний фрейм для контента
    canvas_window = canvas.create_window(
        (0, 0), window=inner_frame, anchor="nw"
    )  # Создаем окно для внутреннего фрейма

    # Функция для обновления области прокрутки
    def configure_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))  # Обновляем область прокрутки
        # Устанавливаем ширину окна канваса равной ширине внутреннего фрейма или канваса (что больше)
        canvas.itemconfig(
            canvas_window, width=max(inner_frame.winfo_reqwidth(), canvas.winfo_width())
        )  # Устанавливаем ширину окна канваса равной ширине внутреннего фрейма или канваса (что больше)

    # Функция для обработки изменения размера холста
    def configure_canvas(event):
        canvas.itemconfig(
            canvas_window, width=event.width
        )  # Устанавливаем ширину окна канваса равной ширине внутреннего фрейма или канваса (что больше)

    # Функция для прокрутки колесиком мыши
    def on_mousewheel(event):
        # Горизонтальная прокрутка при Shift
        if hasattr(event, "state") and (event.state == 1 or event.state & 0x1):
            if event.num == 5 or event.delta == -120:
                canvas.xview_scroll(1, "units")
            elif event.num == 4 or event.delta == 120:
                canvas.xview_scroll(-1, "units")
            elif event.delta == -1:
                canvas.xview_scroll(1, "units")
            elif event.delta == 1:
                canvas.xview_scroll(-1, "units")
        else:
            # Вертикальная прокрутка
            if event.num == 5 or event.delta == -120:
                canvas.yview_scroll(1, "units")
            elif event.num == 4 or event.delta == 120:
                canvas.yview_scroll(-1, "units")
            elif event.delta == -1:
                canvas.yview_scroll(1, "units")
            elif event.delta == 1:
                canvas.yview_scroll(-1, "units")

    # Для Linux: отдельные обработчики для Shift+Button-4/5
    def on_shift_button4(event):
        canvas.xview_scroll(-1, "units")

    def on_shift_button5(event):
        canvas.xview_scroll(1, "units")

    # Привязываем обработчики событий
    inner_frame.bind("<Configure>", configure_scroll_region)
    canvas.bind("<Configure>", configure_canvas)

    # Прокрутка колесиком мыши (Windows/Mac)
    canvas.bind("<Enter>", lambda e: canvas.focus_set())
    canvas.bind("<MouseWheel>", on_mousewheel)
    # Прокрутка колесиком мыши (Linux)
    canvas.bind("<Button-4>", on_mousewheel)
    canvas.bind("<Button-5>", on_mousewheel)
    # Горизонтальная прокрутка с Shift (Linux)
    canvas.bind("<Shift-Button-4>", on_shift_button4)
    canvas.bind("<Shift-Button-5>", on_shift_button5)
    # Также для inner_frame (если мышь над чекбоксами)
    inner_frame.bind("<MouseWheel>", on_mousewheel)
    inner_frame.bind("<Button-4>", on_mousewheel)
    inner_frame.bind("<Button-5>", on_mousewheel)
    inner_frame.bind("<Shift-Button-4>", on_shift_button4)
    inner_frame.bind("<Shift-Button-5>", on_shift_button5)

    # Получаем количество колонок из конфига или используем значение по умолчанию
    num_columns = config.getint(
        "Columns", tab_name, fallback=config.getint("Columns", "default", fallback=3)
    )  # Получаем количество колонок из конфига или используем значение по умолчанию

    # Создаем фрейм для чекбоксов с отступами
    checkboxes_frame = ttk.Frame(inner_frame)
    checkboxes_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Создаем чекбоксы
    for i, checkbox_name in enumerate(checkbox_names):  # Проходим по всем чекбоксам
        if checkbox_name.strip():  # Если чекбокс не пустой
            checkbox_var = tk.BooleanVar()  # Создаем переменную для чекбокса
            checkbox = ttk.Checkbutton(
                checkboxes_frame,
                text=checkbox_name,
                variable=checkbox_var,
                style="Custom.TCheckbutton",
            )  # Создаем чекбокс
            checkbox.grid(
                row=i // num_columns,
                column=i % num_columns,
                sticky="w",
                padx=10,
                pady=5,
            )  # Упаковываем чекбокс
            checkboxes[checkbox_name] = (
                checkbox_var  # Добавляем переменную для чекбокса в словарь
            )

            filepath = f"tweaks//{tab_name}//{checkbox_name}"  # Получаем путь к файлу
            ToolTip(checkbox, filepath)  # Добавляем подсказку к чекбоксу
        else:  # Если чекбокс пустой
            placeholder = ttk.Label(
                checkboxes_frame, text="", width=3
            )  # Создаем placeholder
            placeholder.grid(
                row=i // num_columns,
                column=i % num_columns,
                sticky="w",
                padx=10,
                pady=5,
            )  # Упаковываем placeholder

    # Функция для фильтрации чекбоксов
    def filter_checkboxes(*args):
        search_text = search_var.get().lower()
        for widget in checkboxes_frame.winfo_children():
            if isinstance(widget, ttk.Checkbutton):
                if search_text in widget.cget("text").lower():
                    widget.grid()
                else:
                    widget.grid_remove()

    # Привязываем функцию фильтрации к изменению текста в поле поиска
    search_var.trace("w", filter_checkboxes)
    search_button.config(command=lambda: filter_checkboxes())

    # Обновляем размеры и конфигурацию прокрутки
    inner_frame.update_idletasks()  # Обновляем размеры и конфигурацию прокрутки
    canvas.config(
        scrollregion=canvas.bbox("all")
    )  # Обновляем размеры и конфигурацию прокрутки

    # Устанавливаем минимальный размер для внутреннего фрейма
    inner_frame.grid_columnconfigure(
        num_columns - 1, weight=1
    )  # Устанавливаем минимальный размер для внутреннего фрейма


"""
+------------------------------------+
| Функция для подтверждения          |
| переключения вкладки               |
+------------------------------------+
"""


def confirm_switch_tab(target_function):
    """Функция для подтверждения переключения вкладки"""
    # Проверяем, есть ли выбранные чекбоксы
    selected_checkboxes = [name for name, var in checkboxes.items() if var.get()]

    if selected_checkboxes:
        # Создаем диалоговое окно подтверждения
        dialog = tk.Toplevel(root)
        dialog.title("Предупреждение")
        dialog.geometry("400x150")
        dialog.transient(root)
        dialog.grab_set()

        # Центрируем окно
        dialog.update_idletasks()
        width = dialog.winfo_width()
        height = dialog.winfo_height()
        x = (dialog.winfo_screenwidth() // 2) - (width // 2)
        y = (dialog.winfo_screenheight() // 2) - (height // 2)
        dialog.geometry("{}x{}+{}+{}".format(width, height, x, y))

        # Добавляем сообщение
        message = ttk.Label(
            dialog,
            text="У вас есть несохраненные изменения.\nХотите продолжить?",
            font=("Segoe UI", 10),
            justify="center",
        )
        message.pack(pady=20)

        # Фрейм для кнопок
        button_frame = ttk.Frame(dialog)
        button_frame.pack(pady=10)

        def on_confirm():
            dialog.destroy()
            target_function()

        def on_cancel():
            dialog.destroy()

        # Кнопки
        confirm_button = ttk.Button(
            button_frame,
            text="Продолжить",
            command=on_confirm,
            bootstyle="success-outline",
        )
        confirm_button.pack(side="left", padx=5)

        cancel_button = ttk.Button(
            button_frame, text="Отмена", command=on_cancel, bootstyle="danger-outline"
        )
        cancel_button.pack(side="left", padx=5)

        # Устанавливаем фокус на кнопку отмены
        cancel_button.focus_set()

        # Ждем, пока окно будет закрыто
        dialog.wait_window()
    else:
        # Если нет выбранных чекбоксов, просто переключаемся
        target_function()


"""
+------------------------------------+
| Функция для переключения на        |
| главные вкладки                    |
+------------------------------------+
"""


def switch_to_main():
    # Удаляем все существующие вкладки
    for tab in tab_control.tabs():
        tab_control.forget(tab)

    # Вкладка Быстрая оптимизация
    config_tab = ttk.Frame(tab_control)
    tab_control.add(config_tab, text="Быстрая оптимизация")

    config_frame = ttk.Frame(config_tab)    
    config_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Список конфигураций с описаниями и стилями
    configs = [
        {
            "name": "Базовая оптимизация",
            "bootstyle": "success-outline",
            "description": """Базовый набор оптимизаций для улучшения производительности Windows.
            
• Оптимизация служб Windows
• Очистка временных файлов
• Отключение ненужных компонентов
• Базовая настройка системы
• Оптимизация автозагрузки

Рекомендуется для начинающих пользователей.""",
        },
        {
            "name": "Основная оптимизация",
            "bootstyle": "info-outline",
            "description": """Расширенный набор оптимизаций для заметного улучшения производительности.
            
• Оптимизация всех служб Windows
• Глубокая очистка системы
• Отключение ненужных компонентов
• Настройка производительности
• Оптимизация автозагрузки
• Настройка визуальных эффектов
• Оптимизация памяти

Рекомендуется для большинства пользователей.""",
        },
        {
            "name": "Оптимизация от Хауди Хо",
            "bootstyle": "warning-outline",
            "description": """Полноценный набор оптимизаций для удаления лишнего и улучшения работы системы.
            
• Отключение телеметрии
• Деактивация ненужных служб
• Устранение бесполезных виджетов в Windows
• Очистка фоновых процессов
• Удаление встроенных UWP-приложений
• Очистка логов системы

Рекомендуется для большинства пользователей.""",
        },
        {
            "name": "Углубленная оптимизация",
            "bootstyle": "warning-outline",
            "description": """Продвинутый набор оптимизаций для максимальной производительности.
            
• Глубокая оптимизация всех служб
• Агрессивная очистка системы
• Отключение всех ненужных компонентов
• Максимальная настройка производительности
• Оптимизация всех системных параметров
• Отключение визуальных эффектов
• Настройка приоритетов процессов
• Оптимизация сети

Для опытных пользователей.""",
        },
        {
            "name": "Максимальная оптимизация",
            "bootstyle": "danger-outline",
            "description": """Экстремальный набор оптимизаций для достижения пиковой производительности.
            
• Полная оптимизация всех служб
• Максимальная очистка системы
• Отключение всех ненужных компонентов
• Экстремальная настройка производительности
• Оптимизация всех системных параметров
• Отключение всех визуальных эффектов
• Настройка приоритетов процессов
• Оптимизация сети и дисков
• Настройка реестра

Только для опытных пользователей!""",
        },
        {
            "name": "Радикальная оптимизация",
            "bootstyle": "dark-outline",
            "description": """Максимальный набор оптимизаций для достижения пиковой производительности.
            
• Глубокая оптимизация всех служб
• Агрессивная очистка системы
• Отключение всех ненужных компонентов
• Максимальная настройка производительности
• Оптимизация всех системных параметров
• Отключение визуальных эффектов
• Настройка приоритетов процессов
• Оптимизация сети и дисков
• Настройка реестра
• Отключение всех ненужных функций

ВНИМАНИЕ: Используйте только если вы уверены в своих действиях!""",
        }
    ]

    def run_config(config_name):
        config_path = os.path.join("Configs", f"{config_name}.bat")
        if os.path.exists(config_path):
            subprocess.call([config_path], shell=True)
        else:
            print(f"Файл конфигурации {config_path} не найден")

    # Создаем фрейм для кнопок
    buttons_frame = ttk.Frame(config_frame)
    buttons_frame.pack(fill="both", expand=True, pady=20)

    # Создаем сетку для размещения кнопок
    for i, config in enumerate(configs):
        row = i // 3  # Определяем номер строки
        col = i % 3   # Определяем номер колонки
        
        # Создаем LabelFrame для кнопки и описания со стилем danger-outline
        button_frame = ttk.LabelFrame(buttons_frame, text=config["name"]) # Используем LabelFrame
        button_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        
        # Создаем кнопку с соответствующим bootstyle
        btn = ttk.Button(
            button_frame,
            text=config["name"],
            width=25,
            bootstyle=config["bootstyle"],
            command=lambda c=config["name"]: run_config(c)
        )
        btn.pack(pady=(10, 5), padx=10) # Немного корректируем отступы

        # Создаем текст описания
        description = ttk.Label(
            button_frame,
            text=config["description"],
            wraplength=300,  # Уменьшаем ширину текста для колонок
            justify="left",
            font=("Segoe UI", 10)
        )
        description.pack(fill="x", expand=True, padx=10, pady=(0, 10)) # Немного корректируем отступы

    # Настраиваем веса колонок для равномерного распределения
    for i in range(3):
        buttons_frame.grid_columnconfigure(i, weight=1)
    
    # Настраиваем веса строк для равномерного распределения
    for i in range((len(configs) + 2) // 3): # Вычисляем количество строк
        buttons_frame.grid_rowconfigure(i, weight=1)

    # Создаем основной контейнер для главной вкладки
    main_tab = ttk.Frame(tab_control)
    tab_control.add(main_tab, text="Главная")

    # Создаем верхний фрейм для трех колонок
    top_frame = ttk.Frame(main_tab)
    top_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Левая колонка (приветствие, быстрые действия, статистика)
    welcome_left = ttk.Frame(top_frame)
    welcome_left.pack(side="left", fill="y", padx=(0, 5))

    # Центральная колонка (информация о системе)
    system_info = ttk.LabelFrame(top_frame, text="Информация о системе", padding=5)
    system_info.pack(side="left", fill="x", anchor="n", padx=5)
    system_info.pack(anchor="n", padx=20, pady=20)

    # Правая колонка (история версий и советы)
    right_column = ttk.Frame(top_frame)
    right_column.pack(side="left", fill="both", padx=(5, 0))
    right_column.pack(anchor="n", pady=20, fill="both", expand=True)

    # Добавляем приветствие в левую колонку
    welcome_frame = ttk.Frame(welcome_left)
    welcome_frame.pack(fill="x", pady=(0, 20))

    # Добавляем иконку и заголовок
    title_frame = ttk.Frame(welcome_left)
    title_frame.pack(fill="x", pady=(0, 10))

    all_wincry_theme = ["wincry", "ruslanchik", "wincry_warning", "revi_os"]
    if current_theme in all_wincry_theme:
        icon_label = ttk.Label(
            title_frame, text="🚀", font=("Segoe UI", 32), foreground="#ff1744"
        )
    else:
        icon_label = ttk.Label(title_frame, text="🚀", font=("Segoe UI", 32))
    icon_label.pack(side="left", padx=(0, 10))

    username = getpass.getuser()
    if current_theme == "ruslanchik" or current_theme == "wincry_warning" or current_theme == "revi_os":
        foreground_for_title_frame = "#f0ad4e"
    else:
        foreground_for_title_frame = "#ffffff"
    anton_users = ['User', 'Anton', 'Admin']
    if username in anton_users:
        title = ttk.Label(
            title_frame,
            text="Добро пожаловать, Антон",
            font=("Segoe UI", 24, "bold"),
            foreground=foreground_for_title_frame,
        )
        # foreground='#32FBE2')
        title.pack(side="left")
    else:
        title = ttk.Label(
            title_frame,
            text=f"Добро пожаловать, {username}",
            font=("Segoe UI", 24, "bold"),
            foreground=foreground_for_title_frame,
        )
        # foreground='#32FBE2')
        title.pack(side="left")

    # Добавляем описание программы
    if current_theme == "ruslanchik" or current_theme == "wincry_warning" or current_theme == "revi_os":
        foreground_for_description = "#f0ad4e"
    else:
        foreground_for_description = "#888888"
    description = ttk.Label(
        welcome_left,
        text="All Tweaker - мощный инструмент для оптимизации Windows на 98-99%",
        font=("Segoe UI", 12),
        foreground=foreground_for_description,
    )
    description.pack(fill="x", pady=(0, 10))

    # Создаем фрейм для быстрых действий
    quick_actions = ttk.LabelFrame(welcome_left, text="Быстрые действия", padding=10)
    quick_actions.pack(fill="x", pady=(0, 10))

    # Создаем сетку кнопок быстрых действий
    actions_frame = ttk.Frame(quick_actions)
    actions_frame.pack(fill="x")

    # Список быстрых действий
    quick_buttons = [
        ("⚡ Оптимизация", switch_to_optimization),
        ("⚜️ Исправления", switch_to_fixes),
        ("📦 Другое", switch_to_other),
        ("☠️ Очистка", switch_to_clean),
        ("⚙️ Настройки", switch_to_settings),
        ("☕ Поддержать", open_donat),
    ]

    # Создаем кнопки быстрых действий
    for i, (text, command) in enumerate(quick_buttons):
        btn = ttk.Button(
            actions_frame,
            text=text,
            command=command,
            style="Category.TButton",
            width=20,
        )
        btn.grid(row=i // 2, column=i % 2, padx=5, pady=5, sticky="ew")
    # Если тема wincry_warning, то меняем цвет кнопок на оранжевый
    if current_theme == "wincry_warning":
        for button in actions_frame.winfo_children():
            if isinstance(button, ttk.Button):
                button.config(bootstyle="warning-outline")

    # Настраиваем сетку
    actions_frame.grid_columnconfigure(0, weight=1)
    actions_frame.grid_columnconfigure(1, weight=1)

    # Добавляем статистику использования
    stats_frame = ttk.LabelFrame(
        welcome_left, text="Статистика использования", padding=10
    )
    stats_frame.pack(fill="x", pady=(0, 10))

    try:
        # Получаем статистику использования
        import platform
        import psutil
        import socket
        import wmi
        import GPUtil
        from datetime import datetime

        # Время работы системы
        boot_time = datetime.fromtimestamp(psutil.boot_time())
        uptime = datetime.now() - boot_time
        uptime_str = f"Время работы системы: {uptime.days} дн. {uptime.seconds // 3600} ч. {(uptime.seconds // 60) % 60} мин."

        # Использование RAM
        ram = psutil.virtual_memory()
        ram_str = f"Использование RAM: {ram.percent}%"

        # Свободное место на диске C:
        disk = psutil.disk_usage("C:\\")
        disk_str = f"Свободно на диске C: {disk.free / (1024**3):.1f} GB"

        # Создаем метки со статистикой
        stats = [uptime_str, ram_str, disk_str]
        if current_theme == "ruslanchik" or current_theme == "wincry_warning" or current_theme == "revi_os":
            for stat in stats:
                ttk.Label(
                    stats_frame, text=stat, font=("Segoe UI", 10), foreground="#f0ad4e"
                ).pack(fill="x", pady=2)
        else:
            for stat in stats:
                ttk.Label(
                    stats_frame, text=stat, font=("Segoe UI", 10), foreground="#32FBE2"
                ).pack(fill="x", pady=2)

    except Exception as e:
        print(f"Не удалось получить статистику: {str(e)}")
        ttk.Label(
            stats_frame,
            text=f"Не удалось получить статистику: {str(e)}",
            font=("Segoe UI", 10),
            foreground="red",
        ).pack(fill="x")

    # --- Левая колонка: советы по оптимизации (ОТДЕЛЬНЫЙ ФРЕЙМ) ---
    tips_frame = ttk.LabelFrame(welcome_left, text="Советы по оптимизации", padding=10)
    tips_frame.pack(fill="x", pady=(0, 0), anchor="n")
    tips = [
        "• Регулярно очищайте временные файлы",
        "• Обновляйте драйверы для лучшей производительности",
        "• Используйте режим высокой производительности",
        "• Отключайте ненужные службы Windows",
        "• Отключайте программы из автозагрузки",
        "• Настраивайте параметры визуальных эффектов",
        "• Проверяйте настройки файла подкачки",
        "• Отключайте встроенную рекламу и сбор данных",
    ]
    if current_theme == "wincry_warning":
        foreground_for_tips = "#f0ad4e"
    else:
        foreground_for_tips = "#888888"
    for tip in tips:
        ttk.Label(
            tips_frame, text=tip, font=("Segoe UI", 10), foreground=foreground_for_tips
        ).pack(fill="x", pady=2)

    input_lag_frame = ttk.LabelFrame(welcome_left, text="Тест задержки мыши", padding=10)
    input_lag_frame.pack(fill="x", pady=(10, 0), anchor="n")

    import time
    import statistics

    # Делаем переменные глобальными
    global lag_times
    lag_times = []

    def test_mouse_lag():
        global lag_times
        start_time = time.time()
        # Сразу обновляем интерфейс
        test_button.configure(text="Тестирование...")
        result_label.configure(text="Измерение задержки...")
        # Принудительно обновляем интерфейс
        input_lag_frame.update()
        # Замеряем время после обновления
        end_time = time.time()
        lag_time = (end_time - start_time) * 1000  # Конвертируем в миллисекунды
        lag_times.append(lag_time)
        
        if len(lag_times) >= 5:
            avg_lag = statistics.mean(lag_times)
            min_lag = min(lag_times)
            max_lag = max(lag_times)
            result_label.configure(text=f"Средняя задержка: {avg_lag:.1f} мс\nМинимальная: {min_lag:.1f} мс\nМаксимальная: {max_lag:.1f} мс")
            lag_times = []
        else:
            result_label.configure(text=f"Задержка: {lag_time:.1f} мс\nОсталось тестов: {5 - len(lag_times)}")
            
        test_button.configure(text="Начать тест")
        
    test_button = ttk.Button(input_lag_frame, text="Начать тест", command=test_mouse_lag, bootstyle="outline")
    test_button.pack(pady=5)

    result_label = ttk.Label(input_lag_frame, text="Нажмите кнопку для начала теста")
    result_label.pack(pady=5)

    # def run_benchmark():
    #     import time
    #     import random
    #     import math
        
    #     # Создаем список для хранения результатов
    #     results = []
        
    #     # Тест CPU - вычисление простых чисел
    #     start_time = time.time()
    #     for i in range(100000):
    #         math.sqrt(i)
    #     cpu_time = time.time() - start_time
    #     results.append(f"CPU тест: {cpu_time:.2f} сек")
        
    #     # Тест памяти - создание и сортировка большого списка
    #     start_time = time.time()
    #     test_list = [random.random() for _ in range(100000)]
    #     test_list.sort()
    #     memory_time = time.time() - start_time
    #     results.append(f"Тест памяти: {memory_time:.2f} сек")
        
    #     # Обновляем метку с результатами
    #     result_label.configure(text="\n".join(results))
    
    # benchmark_button = ttk.Button(input_lag_frame, text="Запустить бенчмарк", command=run_benchmark, bootstyle="outline")
    # benchmark_button.pack(pady=5)

    def run_benchmark():
        import time
        import random
        import math
        import psutil
        import platform
        import numpy as np
        from concurrent.futures import ThreadPoolExecutor
        import tkinter as tk
        from tkinter import ttk
        
        # Создаем новое окно для результатов
        benchmark_window = tk.Toplevel()
        benchmark_window.title("Результаты бенчмарка")
        benchmark_window.geometry("600x400")
        
        # Создаем фрейм с прокруткой
        main_frame = ttk.Frame(benchmark_window)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Создаем текстовое поле с прокруткой
        text_widget = tk.Text(main_frame, wrap=tk.WORD, font=("Consolas", 10))
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)
        
        # Размещаем элементы
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Кнопка сохранения результатов
        def save_results():
            try:
                with open("benchmark_results.txt", "w", encoding="utf-8") as f:
                    f.write(text_widget.get("1.0", tk.END))
                text_widget.insert(tk.END, "\n\nРезультаты сохранены в файл benchmark_results.txt")
            except Exception as e:
                text_widget.insert(tk.END, f"\n\nОшибка при сохранении: {e}")
        
        save_button = ttk.Button(benchmark_window, text="Сохранить результаты", command=save_results)
        save_button.pack(pady=5)
        
        # Функция для добавления текста в окно
        def append_text(text):
            text_widget.insert(tk.END, text + "\n")
            text_widget.see(tk.END)  # Прокрутка к последней строке
            benchmark_window.update()  # Обновление окна
        
        # Получаем информацию о системе
        append_text("=== Информация о системе ===")
        append_text(f"Процессор: {platform.processor()}")
        append_text(f"Ядер: {psutil.cpu_count(logical=True)}")
        append_text(f"Оперативная память: {psutil.virtual_memory().total / (1024**3):.1f} ГБ")
        append_text("")
        
        # Тест CPU - вычисление простых чисел (однопоточный)
        append_text("=== Тест CPU (однопоточный) ===")
        start_time = time.time()
        for i in range(1000000):
            math.sqrt(i)
        cpu_time = time.time() - start_time
        append_text(f"Вычисление квадратных корней: {cpu_time:.2f} сек")
        
        # Тест CPU - многопоточные вычисления
        append_text("\n=== Тест CPU (многопоточный) ===")
        def cpu_work():
            return sum(math.sqrt(i) for i in range(100000))
        
        start_time = time.time()
        with ThreadPoolExecutor(max_workers=psutil.cpu_count()) as executor:
            list(executor.map(lambda _: cpu_work(), range(psutil.cpu_count())))
        multi_cpu_time = time.time() - start_time
        append_text(f"Многопоточные вычисления: {multi_cpu_time:.2f} сек")
        
        # Тест памяти
        append_text("\n=== Тест памяти ===")
        # Тест на запись
        start_time = time.time()
        test_array = np.random.random(10000000)
        write_time = time.time() - start_time
        append_text(f"Запись массива (10M элементов): {write_time:.2f} сек")
        
        # Тест на чтение
        start_time = time.time()
        _ = test_array.sum()
        read_time = time.time() - start_time
        append_text(f"Чтение массива: {read_time:.2f} сек")
        
        # Тест на сортировку
        start_time = time.time()
        np.sort(test_array)
        sort_time = time.time() - start_time
        append_text(f"Сортировка массива: {sort_time:.2f} сек")
        
        # Тест на копирование
        start_time = time.time()
        _ = test_array.copy()
        copy_time = time.time() - start_time
        append_text(f"Копирование массива: {copy_time:.2f} сек")
        
        # Тест на многопоточную обработку
        append_text("\n=== Тест многопоточной обработки ===")
        def process_chunk(chunk):
            return np.sum(chunk)
        
        start_time = time.time()
        chunk_size = len(test_array) // psutil.cpu_count()
        chunks = [test_array[i:i + chunk_size] for i in range(0, len(test_array), chunk_size)]
        with ThreadPoolExecutor(max_workers=psutil.cpu_count()) as executor:
            list(executor.map(process_chunk, chunks))
        parallel_time = time.time() - start_time
        append_text(f"Многопоточная обработка: {parallel_time:.2f} сек")
        
        # Делаем окно модальным
        benchmark_window.transient(benchmark_window.master)
        benchmark_window.grab_set()
        benchmark_window.wait_window()

    benchmark_button = ttk.Button(input_lag_frame, text="Запустить бенчмарк", command=run_benchmark, bootstyle="outline")
    benchmark_button.pack(pady=5)

    # Получаем информацию о системе
    try:
        from system_info_display import create_system_info_display

        create_system_info_display(system_info)
        # system_info.pack(anchor='n', padx=20, pady=20)
    except Exception as e:
        error_label = ttk.Label(
            system_info,
            text="Не удалось получить информацию о системе",
            font=("Segoe UI", 10),
            foreground="red",
        )
        error_label.pack(fill="x", pady=(0, 10))

    # --- Правая колонка: история версий ---
    history_frame = ttk.LabelFrame(right_column, text="История версий", padding=5)
    history_frame.pack(
        fill="x", pady=(0, 10), anchor="n"
    )  # anchor='n' для прижатия к верху

    version_history = [
        (
            "Версия 8 (текущая):",
            [
                "• Полностью переработанный пользовательский интерфейс с боковой панелью и динамической загрузкой вкладок",
                "• Улучшенная система подсказок с отображением содержимого скриптов",
                "• Расширенные настройки электропитания с таблицей производительности",
                "• Новая система управления темами оформления с редактором тем",
                "• Улучшенная работа с конфигурационными файлами и фильтрация чекбоксов по поиску",
                "• Оптимизация производительности приложения с поддержкой прокрутки колесом мыши",
                '• Добавлена новая вкладка "Настройки" с возможностью редактирования шрифтов, тем и подсказок',
                '• Добавлены разделы "О программе" и "Версия" с историей изменений',
                '• Добавлены новые темы оформления',
            ],
        ),
        (
            "Версия 7:",
            [
                "• Добавлена поддержка конфигурационного файла settings.ini",
                "• Базовая система подсказок с всплывающими окнами",
                "• Улучшена производительность за счет модульной структуры",
                "• Исправлены ошибки в выполнении скриптов и управлении интерфейсом",
            ],
        ),
        (
            "Версия 6:",
            [
                "• Добавлена структура папок для твиков с использованием get_tab_name",
                "• Улучшен интерфейс с прокруткой вкладок через Canvas и Scrollbar",
                "• Оптимизация кода с выделением функций для управления вкладками",
            ],
        ),
        (
            "Версия 5:",
            [
                "• Добавлена поддержка динамических тем оформления",
                "• Введение настройки шрифтов через выпадающие списки и ползунок",
                "• Улучшен интерфейс с прокруткой вкладок",
                "• Базовая модульная структура с импортом tabs",
                "",
                "• Разделение на основные категории твиков",
                "• Добавление скриптов для удаления телеметрии",
                "• Первые инструменты очистки временных файлов",
                "• Базовые настройки электропитания",
                "• Ручное управление системными службами",
            ],
        ),
        (
            "Версия 1-4:",
            [
                "• Базовый функционал с выполнением скриптов",
                "• Простой интерфейс с вкладками и чекбоксами",
                "• Фиксированная тема оформления (vapor)",
                "• Отсутствие конфигурации и дополнительных настроек",
                "",
                "• Ручная реализация базовых твиков реестра",
                "• Удаление встроенных UWP-приложений (Xbox, Cortana, OneDrive)",
                "• Отключение телеметрии и сбор данных",
                "• Базовые инструменты очистки временных файлов и кэшей",
                "• Управление системными службами и фоновыми процессами",
                "• Интеграция твиков из W10Privacy и ShutUp10",
                "• Начальная работа с электропитанием и производительностью",
                "• Очистка очереди обновлений Windows",
                "• Открытая архитектура с просмотром исходных скриптов",
                "• Базовые настройки отключения виджетов и панели задач",
                "• Первые шаги восстановления системных компонентов",
                "• Фиксация основных ошибок оптимизации Windows 10/11",
                "• Ручное управление реестром через .reg файлы",
                "• Создание базовых скриптов для исправления системных ошибок",
            ],
        ),
    ]

    for version, changes in version_history:
        version_label = ttk.Label(
            history_frame, text=version, font=("Segoe UI", 12, "bold")
        )
        version_label.pack(anchor="w", pady=(10, 5))
        for change in changes:
            change_label = ttk.Label(
                history_frame, text=change, font=("Segoe UI", 10, "italic")
            )
            change_label.pack(anchor="w", padx=20, pady=2, fill="both", expand=True)

    # Создаем вкладку бэкапа
    backup_tab.create_backup_tab(
        tab_control, export_full_registry, import_registry_backup
    )

    # Проходим по всем элементам словаря tabs_main
    for tab_name, checkbox_names in tabs_main.items():
        if tab_name != "Главная":  # Пропускаем главную вкладку, так как она уже создана
            tab = ttk.Frame(tab_control)
            tab_control.add(tab, text=tab_name)
            create_tab_content(tab_name, tab, checkbox_names)

    # Проверяем, есть ли вкладки в tab_control
    if tab_control.tabs():
        tab_control.select(0)


"""
+------------------------------------+
| Функция для переключения на        |
| вкладку с обновлениями             |
+------------------------------------+
"""


def switch_to_update():
    # Удаляем все существующие вкладки
    for tab in tab_control.tabs():
        tab_control.forget(tab)
    # Добавляем новые вкладки из tabs_update
    for tab_name, checkbox_names in tabs_update.items():
        tab_frame = ttk.Frame(tab_control)
        tab_control.add(tab_frame, text=tab_name)
        # Создаем метку-заполнитель
        placeholder = ttk.Label(
            tab_frame,
            text="Загрузка содержимого...",
            font=("Segoe UI", 12),
            foreground="#32FBE2",
        )
        placeholder.pack(expand=True)
        # Сохраняем информацию о вкладке
        tab_frame.tab_info = {
            "name": tab_name,
            "checkbox_names": checkbox_names,
            "loaded": False,
        }
    # Выбираем первую вкладку
    if tab_control.tabs():
        tab_control.select(0)


"""
+------------------------------------+
| Функция для переключения на        |
| вкладки с драйверами               |
+------------------------------------+
"""


def switch_to_drivers():
    # Удаляем все существующие вкладки
    for tab in tab_control.tabs():
        tab_control.forget(tab)

    # Добавляем новые вкладки из tabs_1
    for tab_name, checkbox_names in tabs_1.items():
        tab_frame = ttk.Frame(tab_control)
        tab_control.add(tab_frame, text=tab_name)

        # Создаем метку-заполнитель
        placeholder = ttk.Label(
            tab_frame,
            text="Загрузка содержимого...",
            font=("Segoe UI", 12),
            foreground="#666666",
        )
        placeholder.pack(expand=True)

        # Сохраняем информацию о вкладке
        tab_frame.tab_info = {
            "name": tab_name,
            "checkbox_names": checkbox_names,
            "loaded": False,
        }

    # Выбираем первую вкладку
    if tab_control.tabs():
        tab_control.select(0)


"""
+------------------------------------+
| Функция для переключения на        |
| вкладку оптимизации                |
+------------------------------------+
"""


def switch_to_optimization():
    # Удаляем все существующие вкладки
    for tab in tab_control.tabs():
        tab_control.forget(tab)

    # Добавляем новые вкладки из tabs
    for tab_name, checkbox_names in tabs.items():
        tab_frame = ttk.Frame(tab_control)
        tab_control.add(tab_frame, text=tab_name)

        # Создаем метку-заполнитель
        placeholder = ttk.Label(
            tab_frame,
            text="Загрузка содержимого...",
        font=("Segoe UI", 12),
            foreground="#32FBE2",
        )
        placeholder.pack(expand=True)

        # Сохраняем информацию о вкладке
        tab_frame.tab_info = {
            "name": tab_name,
            "checkbox_names": checkbox_names,
            "loaded": False,
        }

    # Выбираем первую вкладку
    if tab_control.tabs():
        tab_control.select(0)


"""
+------------------------------------+
| Функция для переключения на        |
| вкладку электропитания             |
+------------------------------------+
"""


def switch_to_power():
    # Удаляем все существующие вкладки
    for tab in tab_control.tabs():
        tab_control.forget(tab)

    # Добавляем специальную вкладку с таблицей
    power_tab = create_power_tab()
    tab_control.add(power_tab, text="Электропитание")

    # Добавляем остальные вкладки из tabs_2 (если нужно)
    for tab_name, checkbox_names in tabs_2.items():
        if tab_name != "Электропитание":  # Пропускаем, если уже добавили
            tab_frame = ttk.Frame(tab_control)
            tab_control.add(tab_frame, text=tab_name)

            placeholder = ttk.Label(
                tab_frame,
                text="Загрузка содержимого...",
                font=("Segoe UI", 12),
                foreground="#32FBE2",
            )
            placeholder.pack(expand=True)

            tab_frame.tab_info = {
                "name": tab_name,
                "checkbox_names": checkbox_names,
                "loaded": False,
            }

    # Выбираем вкладку с таблицей
    tab_control.select(power_tab)


"""
+------------------------------------+
| Функция для переключения на        |
| вкладку с исправлениями            |
+------------------------------------+
"""


def switch_to_fixes():
    # Удаляем все существующие вкладки
    for tab in tab_control.tabs():
        tab_control.forget(tab)

    # Создаем вкладку исправлений
    from tweaks.fixes_tab import create_fixes_tab

    fixes_tab = create_fixes_tab(tab_control)

    # Выбираем вкладку исправлений
    tab_control.select(fixes_tab)


"""
+------------------------------------+
| Функция для переключения на        |
| вкладку с очисткой                 |
+------------------------------------+
"""


def switch_to_clean():
    # Удаляем все существующие вкладки
    for tab in tab_control.tabs():
        tab_control.forget(tab)

    # Добавляем новые вкладки из tabs_4
    for tab_name, checkbox_names in tabs_4.items():
        tab_frame = ttk.Frame(tab_control)
        tab_control.add(tab_frame, text=tab_name)

        # Создаем метку-заполнитель
        placeholder = ttk.Label(
            tab_frame,
            text="Загрузка содержимого...",
        font=("Segoe UI", 12),
            foreground="#32FBE2",
        )
        placeholder.pack(expand=True)

        # Сохраняем информацию о вкладке
        tab_frame.tab_info = {
            "name": tab_name,
            "checkbox_names": checkbox_names,
            "loaded": False,
        }

    # Выбираем первую вкладку
    if tab_control.tabs():
        tab_control.select(0)


"""
+------------------------------------+
| Функция для переключения на        |
| вкладку с другими функциями        |
+------------------------------------+
"""


def switch_to_other():
    # Удаляем все существующие вкладки
    for tab in tab_control.tabs():
        tab_control.forget(tab)

    # Добавляем новые вкладки из tabs_5
    for tab_name, checkbox_names in tabs_5.items():
        tab_frame = ttk.Frame(tab_control)
        tab_control.add(tab_frame, text=tab_name)

        # Создаем метку-заполнитель
        placeholder = ttk.Label(
            tab_frame,
            text="Загрузка содержимого...",
            font=("Segoe UI", 12),
            foreground="#32FBE2",
        )
        placeholder.pack(expand=True)

        # Сохраняем информацию о вкладке
        tab_frame.tab_info = {
            "name": tab_name,
            "checkbox_names": checkbox_names,
            "loaded": False,
        }

    # Выбираем первую вкладку
    if tab_control.tabs():
        tab_control.select(0)


"""
+------------------------------------+
| Функция для переключения на        |
| вкладку QQNWR                      |
+------------------------------------+
"""


def switch_to_qqnwr():
    # Удаляем все существующие вкладки
    for tab in tab_control.tabs():
        tab_control.forget(tab)

    # Добавляем новые вкладки из tabs_qqnwr
    for tab_name, checkbox_names in tabs_qqnwr.items():
        tab_frame = ttk.Frame(tab_control)
        tab_control.add(tab_frame, text=tab_name)

        # Создаем метку-заполнитель
        placeholder = ttk.Label(
            tab_frame,
            text="Загрузка содержимого...",
            font=("Segoe UI", 12),
            foreground="#32FBE2",
        )
        placeholder.pack(expand=True)

        # Сохраняем информацию о вкладке
        tab_frame.tab_info = {
            "name": tab_name,
            "checkbox_names": checkbox_names,
            "loaded": False,
        }

    # Выбираем первую вкладку
    if tab_control.tabs():
        tab_control.select(0)


"""
+------------------------------------+
| Функция для отображения информации |
| о программе                        |
+------------------------------------+
"""


def switch_to_about():
    # Удаляем все существующие вкладки
    for tab in tab_control.tabs():
        tab_control.forget(tab)

    # Создаем вкладку "О программе"
    about_tab = ttk.Frame(tab_control)
    tab_control.add(about_tab, text="О программе")

    # Создаем контейнер для содержимого
    content_frame = ttk.Frame(about_tab)
    content_frame.pack(expand=True, fill="both", padx=20, pady=20)

    # Добавляем информацию о программе
    title = ttk.Label(content_frame, text="All Tweaker", font=("Segoe UI", 24, "bold"))
    title.pack(pady=(0, 10))

    description = ttk.Label(
        content_frame,
        text="Программа для оптимизации и настройки Windows",
        font=("Segoe UI", 12),
    )
    description.pack(pady=(0, 20))

    # Список функций и возможностей
    features = [
        "Интерфейс и удобство использования:",
        "• Современный пользовательский интерфейс с боковой панелью",
        "• Динамическая загрузка вкладок",
        "• Система подсказок с просмотром содержимого скриптов",
        "• Поддержка прокрутки колесом мыши",
        "• Фильтрация чекбоксов через поиск",
        "• Настраиваемые шрифты и темы оформления",
        "• Встроенный редактор тем",
        '• Тема "cyberpunk" и другие темы оформления',
        "• Конфигурационный файл settings.ini",
        '• Вкладка "Настройки" для кастомизации',
        "• Управление отправкой телеметрии при закрытии",
        "",
        "Основной функционал:",
        "• 12 основных категорий (Приватность, Оптимизация, Очистка и др.)",
        "• Поддержка всех типов твиков (.bat, .reg, .ps1, .exe)",
        "• Создание и выполнение конфигурационных файлов",
        "• Древовидная структура категорий",
        "• Открытая архитектура с доступом к исходным скриптам",
        "• Автоматическое обновление токенов Dropbox",
        "• Расширенная система телеметрии",
        "",
        "Оптимизация системы:",
        "• Настройка производительности Windows",
        "• Управление службами и процессами",
        "• Оптимизация электропитания",
        "• Настройка виртуальной памяти",
        "• Управление драйверами",
        "• Очистка системы от мусора",
        "",
        "Безопасность и приватность:",
        "• Отключение телеметрии Windows",
        "• Настройка брандмауэра",
        "• Управление правами доступа",
        "• Шифрование данных",
        "• Резервное копирование настроек",
        "• Защита от вредоносного ПО",
        "",
        "Кастомизация:",
        "• Настройка контекстного меню",
        "• Управление автозагрузкой",
        "• Настройка рабочего стола",
        "• Персонализация панели задач",
        '• Настройка меню "Пуск"',
        "• Управление значками рабочего стола",
        "",
        "Дополнительные возможности:",
        "• Интеграция с Dropbox",
        "• Система логирования",
        "• Экспорт/импорт настроек",
        "• Автоматическое создание резервных копий",
        "• Поддержка нескольких языков",
        "• Расширенная система помощи",
    ]

    for feature in features:
        feature_label = ttk.Label(content_frame, text=feature, font=("Segoe UI", 10))
        feature_label.pack(anchor="w", pady=2)

    # Добавляем информацию о разработчике
    developer_info = ttk.Label(
        content_frame,
        text="\nGitHub: scode18\nтгк: https://t.me/all_tweaker",
        font=("Segoe UI", 10),
    )
    developer_info.pack(pady=(20, 0))


"""
+------------------------------------+
| Функция для отображения информации |
| о версии программы                 |
+------------------------------------+
"""


def switch_to_version():
    # Удаляем все существующие вкладки
    for tab in tab_control.tabs():
        tab_control.forget(tab)

    # Создаем вкладку версии
    version_tab = ttk.Frame(tab_control)
    tab_control.add(version_tab, text="Версия")

    # Создаем контейнер для содержимого с прокруткой
    canvas = tk.Canvas(version_tab)
    scrollbar = ttk.Scrollbar(version_tab, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    # Настройка прокрутки
    scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Упаковка элементов
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Привязка колесика мыши
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", on_mousewheel)

    # Переносим весь существующий контент в scrollable_frame
    # version_title = ttk.Label(scrollable_frame,
    #                          text='All Tweaker v8.0',
    #                          font=('Segoe UI', 24, 'bold'),
    #                          foreground='#32FBE2')
    # version_title.pack(pady=(0, 20))

    # История версий
    version_history = [
        (
            "Версия 8 Beta 63 (текущая):",
            [
                "• Добавлена поддержка конфигурационного файла settings.ini",
                "• Базовая система подсказок с всплывающими окнами",
                "• Улучшена производительность за счет модульной структуры",
                "• Исправлены ошибки в выполнении скриптов и управлении интерфейсом",
                "• Добавлен выбор начальной вкладки при запуске",
                "• Реализовано удаление элементов в интеграторе",
                "• Добавлен экспорт и импорт настроек программы",
                "• Внедрена система всплывающих подсказок",
                "• Добавлена вкладка с информацией о системе",
                "• Реализована вкладка исправления проблем",
                '• Добавлена вкладка "О системе"',
                "• Внедрена система телеметрии с настройками",
                "• Добавлена структура папок для твиков с использованием get_tab_name",
                "• Улучшен интерфейс с прокруткой вкладок через Canvas и Scrollbar",
                "• Оптимизация кода с выделением функций для управления вкладками",
                "",
                "• Автоматизация ручных твиков через .bat скрипты",
                "• Добавление терапии после обновлений Windows",
                "• Первые версии хардкор-чисток (3 уровня)",
                "• Интеграция W10Privacy и SimpleDnsCrypt",
                "• Базовые скрипты для исправления системных ошибок",
                "• Внедрение структуры папок для категорий",
                "• Добавление .reg файлов для редактирования реестра",
                "• Первые профили электропитания (Bitsum, Balanced)",
                "• Интеграция DnsJumper и базового TCPOptimizer",
                "• Начало работы с кастомизацией интерфейса",
            ],
        ),
        (
            "Версия 8 beta v.2 (текущая):",
            [
                "• Полностью переработанный пользовательский интерфейс с боковой панелью и динамической загрузкой вкладок",
                "• Улучшенная система подсказок с отображением содержимого скриптов",
                "• Расширенные настройки электропитания с таблицей производительности",
                "• Новая система управления темами оформления с редактором тем",
                "• Улучшенная работа с конфигурационными файлами и фильтрация чекбоксов по поиску",
                "• Оптимизация производительности приложения с поддержкой прокрутки колесом мыши",
                '• Добавлена новая вкладка "Настройки" с возможностью редактирования шрифтов, тем и подсказок',
                '• Добавлены разделы "О программе" и "Версия" с историей изменений',
                '• Добавлена новая тема оформления "cyberpunk"',
                "",
                "• Полная реструктуризация на 12 категорий: Приватность, Оптимизация, Очистка, Электропитание, Обновления, Программы и др.",
                "• Расширенные инструменты удаления компонентов (Xbox, Edge, OneDrive, 50+ приложений)",
                "• Глубокая оптимизация сети: TCPOptimizer, DnsJumper, скрипты снижения пинга",
                "• 35+ профилей электропитания (Adamx, Amit, GGOS, Khorvie, Zoyata)",
                "• Система терапии после обновлений с 15+ подпунктами",
                "• Хардкор-чистка (3 уровня, Winsxs, кэши обновлений, временные файлы)",
                "• Интеграция профессиональных инструментов: O&O ShutUp10++, Dism++, Mem Reduct",
                "• Расширенная кастомизация: темы Windows 11, контекстное меню, трей, иконки",
                "• 50+ скриптов для исправления системных проблем (драйверы, Bluetooth, Store)",
                "• Поддержка всех типов твиков: .bat, .reg, .ps1, .exe",
            ],
        ),
        (
            "Версия 8 beta v.1:",
            [
                "• Переработанный пользовательский интерфейс с центральным фреймом",
                "• Расширенная структура вкладок с горизонтальной прокруткой",
                "• Улучшена поддержка типов файлов (.bat, .ps1, .reg)",
                "• Добавлена возможность создания и выполнения конфигурационных файлов",
                "• Поддержка динамических настроек шрифтов и тем через settings.ini",
                "",
                "• Базовое разделение на категории с древовидной структурой",
                "• Первые версии комплексных чисток системы",
                "• Интеграция базовых сетевых оптимизаций",
                "• Система управления электропитанием через .pow файлы",
                "• Начало работы с удалением системных компонентов",
            ],
        ),
        (
            "Версия 7:",
            [
                "• Добавлена поддержка конфигурационного файла settings.ini",
                "• Базовая система подсказок с всплывающими окнами",
                "• Улучшена производительность за счет модульной структуры",
                "• Исправлены ошибки в выполнении скриптов и управлении интерфейсом",
                "",
                "• Автоматизация ручных твиков через .bat скрипты",
                "• Добавление терапии после обновлений Windows",
                "• Первые версии хардкор-чисток (3 уровня)",
                "• Интеграция W10Privacy и SimpleDnsCrypt",
                "• Базовые скрипты для исправления системных ошибок",
            ],
        ),
        (
            "Версия 6:",
            [
                "• Добавлена структура папок для твиков с использованием get_tab_name",
                "• Улучшен интерфейс с прокруткой вкладок через Canvas и Scrollbar",
                "• Оптимизация кода с выделением функций для управления вкладками",
                "",
                "• Внедрение структуры папок для категорий",
                "• Добавление .reg файлов для редактирования реестра",
                "• Первые профили электропитания (Bitsum, Balanced)",
                "• Интеграция DnsJumper и базового TCPOptimizer",
                "• Начало работы с кастомизацией интерфейса",
            ],
        ),
        (
            "Версия 5:",
            [
                "• Добавлена поддержка динамических тем оформления",
                "• Введение настройки шрифтов через выпадающие списки и ползунок",
                "• Улучшен интерфейс с прокруткой вкладок",
                "• Базовая модульная структура с импортом tabs",
                "",
                "• Разделение на основные категории твиков",
                "• Добавление скриптов для удаления телеметрии",
                "• Первые инструменты очистки временных файлов",
                "• Базовые настройки электропитания",
                "• Ручное управление системными службами",
            ],
        ),
        (
            "Версия 1-4:",
            [
                "• Базовый функционал с выполнением скриптов",
                "• Простой интерфейс с вкладками и чекбоксами",
                "• Фиксированная тема оформления (vapor)",
                "• Отсутствие конфигурации и дополнительных настроек",
                "",
                "• Ручная реализация базовых твиков реестра",
                "• Удаление встроенных UWP-приложений (Xbox, Cortana, OneDrive)",
                "• Отключение телеметрии и сбор данных",
                "• Базовые инструменты очистки временных файлов и кэшей",
                "• Управление системными службами и фоновыми процессами",
                "• Интеграция твиков из W10Privacy и ShutUp10",
                "• Начальная работа с электропитанием и производительностью",
                "• Очистка очереди обновлений Windows",
                "• Открытая архитектура с просмотром исходных скриптов",
                "• Базовые настройки отключения виджетов и панели задач",
                "• Первые шаги восстановления системных компонентов",
                "• Фиксация основных ошибок оптимизации Windows 10/11",
                "• Ручное управление реестром через .reg файлы",
                "• Создание базовых скриптов для исправления системных ошибок",
            ],
        ),
    ]

    for version, changes in version_history:
        version_label = ttk.Label(
            scrollable_frame, text=version, font=("Segoe UI", 12, "bold")
        )
        version_label.pack(anchor="w", pady=(10, 5))

        for change in changes:
            change_label = ttk.Label(
                scrollable_frame, text=change, font=("Segoe UI", 10)
            )
            change_label.pack(anchor="w", padx=20, pady=2)

    # release_info = ttk.Label(scrollable_frame,
    #                         text='\nДата релиза текущей версии: Март 2024',
    #                         font=('Segoe UI', 10),
    #                         foreground='#32FBE2')
    # release_info.pack(pady=(20, 0))


def switch_to_settings():
    # Удаляем все существующие вкладки
    for tab in tab_control.tabs():
        tab_control.forget(tab)

    # Создаем вкладку основных настроек
    settings1_tab = ttk.Frame(tab_control)
    tab_control.add(settings1_tab, text="Настройки")

    # Создаем основной контейнер с отступами
    settings_frame = ttk.Frame(settings1_tab, padding=20)
    settings_frame.pack(fill="both", expand=True)

    # Заголовок настроек
    settings_title = ttk.Label(
        settings_frame, text="Настройки приложения", font=("Segoe UI", 16, "bold")
    )
    settings_title.pack(anchor="w", pady=(0, 20))

    # Контейнер для двух колонок
    columns_container = ttk.Frame(settings_frame)
    columns_container.pack(fill="both", expand=True)

    # Левая колонка (основные настройки)
    left_column = ttk.Frame(columns_container)
    left_column.pack(side="left", fill="both", expand=True, padx=(0, 15))

    # Правая колонка (настройка колонок)
    right_column = ttk.Frame(columns_container)
    right_column.pack(side="right", fill="both", expand=True)

    # Группируем настройки в секции
    appearance_section = ttk.LabelFrame(left_column, text="Внешний вид", padding=15)
    appearance_section.pack(fill="x", pady=(0, 15))

    ttk.Label(appearance_section, text="Шрифт:", font=("Segoe UI", 10)).pack(
        anchor="w", pady=(0, 5)
    )
    font_family_dropdown = ttk.Combobox(
        appearance_section,
        textvariable=font_family_var,
        values=font_family_values,
        width=30,
    )
    font_family_dropdown.pack(anchor="w", pady=(0, 10))

    ttk.Label(appearance_section, text="Размер шрифта:", font=("Segoe UI", 10)).pack(
        anchor="w", pady=(0, 5)
    )
    font_size_slider = ttk.Scale(
        appearance_section,
        variable=font_size_var,
        from_=8,
        to=12,
        orient="horizontal",
        length=200,
    )
    font_size_slider.pack(anchor="w", pady=(0, 10))

    ttk.Label(appearance_section, text="Тема оформления:", font=("Segoe UI", 10)).pack(
        anchor="w", pady=(0, 5)
    )
    theme_dropdown = ttk.Combobox(
        appearance_section,
        textvariable=theme_var,
        values=root.style.theme_names(),
        width=30,
    )
    theme_dropdown.pack(anchor="w", pady=(0, 10))

    # Секция редактора тем
    theme_editor_frame = ttk.Frame(appearance_section)
    theme_editor_frame.pack(fill="x", pady=(10, 0))

    ttk.Label(theme_editor_frame, text="Редактор тем:", font=("Segoe UI", 10)).pack(
        side="left", padx=(0, 10)
    )

    theme_editor_btn = ttk.Button(
        theme_editor_frame,
        text="Открыть редактор",
        bootstyle="danger-outline",
        command=lambda: subprocess.run(["python", "-m", "ttkcreator"]),
    )
    theme_editor_btn.pack(side="left")

    # Секция дополнительных настроек
    additional_section = ttk.LabelFrame(left_column, text="Дополнительно", padding=15)
    additional_section.pack(fill="x", pady=(0, 15))

    ttk.Label(additional_section, text="Подсказки:", font=("Segoe UI", 10)).pack(
        anchor="w", pady=(0, 5)
    )
    tooltip_control_dropdown = ttk.Combobox(
        additional_section,
        textvariable=tooltip_control_var,
        values=["Включено", "Выключено"],
        width=30,
    )
    tooltip_control_dropdown.pack(anchor="w", pady=(0, 10))

    # Создаем переменную для хранения состояния отправки телеметрии при закрытии
    send_telemetry_on_close_var = tk.StringVar(
        value="Включено"
        if config.getboolean("Telemetry", "send_on_close", fallback=True)
        else "Выключено"
    )

    # Выпадающий список для выбора отправки телеметрии при закрытии
    ttk.Label(
        additional_section, text="Отправлять телеметрию:", font=("Segoe UI", 10)
    ).pack(anchor="w", pady=(0, 5))
    telemetry_on_close_dropdown = ttk.Combobox(
        additional_section,
        textvariable=send_telemetry_on_close_var,
        values=["Включено", "Выключено"],
        width=30,
    )
    telemetry_on_close_dropdown.pack(anchor="w", pady=(0, 10))

    # Функция для обновления настройки отправки телеметрии при закрытии
    def update_telemetry_on_close(event=None):
        new_value = send_telemetry_on_close_var.get() == "Включено"
        config["Telemetry"]["send_on_close"] = str(new_value)
        with open("user_data//settings.ini", "w", encoding="cp1251") as configfile:
            config.write(configfile)

    # Привязываем событие выбора
    telemetry_on_close_dropdown.bind("<<ComboboxSelected>>", update_telemetry_on_close)

    # Новая функция для обновления полноэкранного режима
    def update_fullscreen(event=None):
        new_value = fullscreen_var.get() == "Включено"
        root.attributes("-fullscreen", new_value)
        config["Window"]["fullscreen"] = str(new_value)
        with open("user_data//settings.ini", "w", encoding="cp1251") as configfile:
            config.write(configfile)
        if not new_value:
            root.geometry("1280x720")

    fullscreen_options = ["Включено", "Выключено"]
    ttk.Label(
        additional_section, text="Полноэкранный режим:", font=("Segoe UI", 10)
    ).pack(anchor="w", pady=(0, 5))
    fullscreen_dropdown = ttk.Combobox(
        additional_section,
        textvariable=fullscreen_var,
        values=fullscreen_options,
        width=30,
    )
    fullscreen_dropdown.pack(anchor="w", pady=(0, 10))

    # Привязываем событие выбора
    fullscreen_dropdown.bind("<<ComboboxSelected>>", update_fullscreen)

    # Привязываем события к элементам управления
    font_family_dropdown.bind("<<ComboboxSelected>>", update_font)
    font_size_slider.bind("<ButtonRelease-1>", update_font)
    theme_dropdown.bind("<<ComboboxSelected>>", update_theme)
    tooltip_control_dropdown.bind("<<ComboboxSelected>>", update_tooltip_state)

    # Секция управления конфигурациями в левой колонке
    config_section = ttk.LabelFrame(
        left_column, text="Управление конфигурациями", padding=15
    )
    config_section.pack(fill="x", pady=(0, 15))

    # Выпадающий список файлов конфигурации
    config_file_dropdown = ttk.Combobox(
        config_section,
        textvariable=config_file_var,
        values=config_file_values,
        width=width,
        font=("Segoe UI", 10),
    )
    config_file_dropdown.pack(side="left", padx=5)

    # Кнопка выполнения конфига
    execute_config_button = ttk.Button(
        config_section,
        text="Выполнить конфиг",
        bootstyle="danger-outline",
        command=execute_config,
    )
    execute_config_button.pack(side="left", padx=5)

    # Секция настроек колонок в левой колонке
    columns_settings_frame = ttk.LabelFrame(
        left_column, text="Настройки колонок", padding=15
    )
    columns_settings_frame.pack(fill="x", pady=(0, 15))

    # Кнопка открытия настроек колонок
    open_columns_settings_button = ttk.Button(
        columns_settings_frame,
        text="Открыть настройки колонок",
        bootstyle="danger-outline",
        command=open_columns_settings_window,
    )
    open_columns_settings_button.pack(side="left", padx=5)

    # Добавляем вкладку телеметрии в правую колонку
    telemetry_section = ttk.LabelFrame(right_column, text="Телеметрия", padding=15)
    telemetry_section.pack(fill="x", expand=False)

    # Заголовок
    ttk.Label(
        telemetry_section, text="Отправка телеметрии", font=("Segoe UI", 14, "bold")
    ).pack(anchor="w", pady=(0, 5))

    # Старое описание
    old_description_text = """Отправка данных о работе программы и настроек для улучшения функциональности и внешнего вида.

Отправляемые данные:
• Ошибки при запуске программы
• Лог-файлы (logs)
• Настройки All Tweaker (settings.ini)
• Экспортированные настройки (Configs/Exports)
• Конфигурации твиков (Configs)
• Файлы интегратора (context_menu)
• Все файлы из папки telemetry
• Сообщения об успешном запуске программы

Эти данные помогут улучшить работу программы, исправить возможные проблемы, а также внешний вид и функциональность."""

    # Описание
    description_text = """Отправка данных о работе программы и настроек для улучшения функциональности и внешнего вида.

Отправляемые данные:

• Сообщения об успешном запуске программы
• Сообщения об ошибках
• Лог-файлы
• Настройки All Tweaker
• Запущенные твики
• Время запуска
• Имя пользователя и версия Windows

Эти данные помогут улучшить работу программы, исправить возможные проблемы, а также внешний вид и функциональность."""

    ttk.Label(
        telemetry_section,
        text=description_text,
        font=("Segoe UI", 10),
        wraplength=500,
        justify="left",
    ).pack(anchor="w", pady=(0, 10))

    # def collect_and_send():
    #     from telemetry.telemetry_manager import TelemetryManager
    #     manager = TelemetryManager()
    #     if manager.collect_telemetry_data():
    #         print("Телеметрия успешно собрана и отправлена")
    #     else:
    #         print("Ошибка при сборе и отправке телеметрии")

    ttk.Button(
        telemetry_section,
        text="Отправить телеметрию",
        bootstyle="success-outline",
        command=collect_and_send,
    ).pack(pady=5)

    # Добавляем фрейм для отправки сообщений разработчику
    feedback_section = ttk.LabelFrame(right_column, text="Обратная связь", padding=15)
    feedback_section.pack(fill="x", expand=False, pady=(15, 0))

    # Заголовок
    ttk.Label(
        feedback_section,
        text="Отправить сообщение разработчику",
        font=("Segoe UI", 14, "bold"),
    ).pack(anchor="w", pady=(0, 5))

    # Описание
    ttk.Label(
        feedback_section,
        text="Вы можете отправить сообщение разработчику с предложениями по улучшению программы или сообщением об ошибках.",
        font=("Segoe UI", 10),
        wraplength=500,
        justify="left",
    ).pack(anchor="w", pady=(0, 10))

    # Создаем текстовое поле для сообщения
    message_text = tk.Text(feedback_section, height=5, width=50, font=("Segoe UI", 10))
    message_text.pack(fill="x", pady=(0, 10))

    # Создаем фрейм для кнопок загрузки файлов
    file_buttons_frame = ttk.Frame(feedback_section)
    file_buttons_frame.pack(fill="x", pady=(0, 10))

    # Глобальные переменные для хранения путей к файлам
    global attached_file, attached_image
    attached_file = None
    attached_image = None

    # Функция для загрузки файла
    def attach_file():
        global attached_file
        file_path = filedialog.askopenfilename(
            title="Выберите файл", filetypes=[("Все файлы", "*.*")]
        )
        if file_path:
            attached_file = file_path
            print(f"Файл прикреплен: {os.path.basename(file_path)}")

    # Функция для загрузки изображения
    def attach_image():
        global attached_image
        image_path = filedialog.askopenfilename(
            title="Выберите изображение",
            filetypes=[("Изображения", "*.png *.jpg *.jpeg *.bmp *.gif")],
        )
        if image_path:
            attached_image = image_path
            print(f"Изображение прикреплено: {os.path.basename(image_path)}")

    # Кнопка для загрузки файла
    ttk.Button(
        file_buttons_frame,
        text="Прикрепить файл",
        bootstyle="info-outline",
        command=attach_file,
    ).pack(side="left", padx=5)

    # Кнопка для загрузки изображения
    ttk.Button(
        file_buttons_frame,
        text="Прикрепить изображение",
        bootstyle="info-outline",
        command=attach_image,
    ).pack(side="left", padx=5)

    # Функция для отправки сообщения
    def send_feedback():
        global attached_file, attached_image
        message = message_text.get("1.0", "end-1c").strip()
        if not message and not attached_file and not attached_image:
            print("Предупреждение: Пожалуйста, введите сообщение или прикрепите файл")
            return

        try:
            from telemetry.telemetry_manager import TelemetryManager

            manager = TelemetryManager()

            # Логируем начало отправки обратной связи
            logger.logger.info("Отправка обратной связи...")

            # Отправляем сообщение с префиксом "Обратная связь от пользователя:"
            # собираем информацию о пользователе
            user_info = (
                f"👤 Пользователь: #{os.getenv('USERNAME', 'unknown')}\n"
                f"💻 Версия All Tweaker: All Tweaker {version}\n"
                f"🐍 Python версия: {sys.version}\n"
            )

            # объединяем информацию с сообщением от пользователя
            full_message = f"Обратная связь от пользователя:\n{message}\n\n{user_info}"

            # отправляем сообщение
            if manager.send_message(full_message):
                logger.logger.info("Сообщение обратной связи успешно отправлено")
                print("Сообщение успешно отправлено!")

                # Отправляем файл, если он прикреплен
                if attached_file:
                    if manager.send_telegram(attached_file):
                        logger.logger.info(
                            f"Файл {os.path.basename(attached_file)} успешно отправлен"
                        )
                        print("Файл успешно отправлен!")
                    else:
                        logger.logger.error(
                            f"Ошибка отправки файла {os.path.basename(attached_file)}"
                        )
                        print("Ошибка: Не удалось отправить файл")

                # Отправляем изображение, если оно прикреплено
                if attached_image:
                    if manager.send_telegram(attached_image):
                        logger.logger.info(
                            f"Изображение {os.path.basename(attached_image)} успешно отправлено"
                        )
                        print("Изображение успешно отправлено!")
                    else:
                        logger.logger.error(
                            f"Ошибка отправки изображения {os.path.basename(attached_image)}"
                        )
                        print("Ошибка: Не удалось отправить изображение")

                # Очищаем форму
                message_text.delete("1.0", "end")
                attached_file = None
                attached_image = None
            else:
                logger.logger.error("Ошибка отправки сообщения обратной связи")
                print("Ошибка: Не удалось отправить сообщение")
        except Exception as e:
            logger.logger.error(f"Ошибка при отправке обратной связи: {str(e)}")
            print(f"Ошибка: Произошла ошибка при отправке: {str(e)}")

    # Кнопка отправки доната
    ttk.Button(
        file_buttons_frame,
        text="Отправить донат",
        bootstyle="warning-outline",
        command=open_donat,
    ).pack(side="left", padx=5)

    # Кнопка отправки сообщения
    ttk.Button(
        file_buttons_frame,
        text="Отправить сообщение",
        bootstyle="success-outline",
        command=send_feedback,
    ).pack(side="left", padx=5)

    # Кнопка для выбора сборки Windows
    ttk.Button(
        file_buttons_frame,
        text="Проголовать",
        bootstyle="success-outline",
        command=lambda: WindowsVoteWindow(root),
    ).pack(side="left", padx=5)

    # Добавляем фрейм для кнопок экспорта/импорта в правую колонку
    import_export_section = ttk.LabelFrame(
        right_column, text="Импорт/Экспорт", padding=15
    )
    import_export_section.pack(fill="x", expand=False, pady=(15, 0))

    # Добавляем фрейм для кнопок экспорта/импорта
    settings_buttons_frame = ttk.Frame(import_export_section)
    settings_buttons_frame.pack(fill="x", pady=(0, 0))

    # Кнопка экспорта настроек
    export_button = ttk.Button(
        settings_buttons_frame,
        text="Экспорт настроек",
        bootstyle="success-outline",
        command=export_settings,
    )
    export_button.pack(side="left", padx=5)

    # Кнопка импорта настроек
    import_button = ttk.Button(
        settings_buttons_frame,
        text="Импорт настроек",
        bootstyle="success-outline",
        command=lambda: import_settings() and root.destroy() and root.quit(),
    )
    import_button.pack(side="left", padx=5)

    # Настройка начальной вкладки
    ttk.Label(
        additional_section, text="Начальная вкладка:", font=("Segoe UI", 10)
    ).pack(anchor="w", pady=(0, 5))
    initial_tab_dropdown = ttk.Combobox(
        additional_section,
        textvariable=initial_tab_var,
        values=[
            "Главная",
            "Оптимизация",
            "Драйверы",
            "Электропитание",
            "Другое",
            "QQNWR",
            "Очистка",
            "Исправления",
            "Настройки",
            "Антон GPT",
            "Обновления",
            "О программе",
            "О системе",
            "Версия",
        ],
        width=30,
    )
    initial_tab_dropdown.pack(anchor="w", pady=(0, 10))

    def update_initial_tab(event=None):
        # Словарь для сопоставления пользовательских названий с именами функций
        tab_mapping = {
            "Главная": "switch_to_main_wrapper",
            "Оптимизация": "switch_to_optimization_wrapper",
            "Драйверы": "switch_to_drivers_wrapper",
            "Электропитание": "switch_to_power_wrapper",
            "Другое": "switch_to_other_wrapper",
            "QQNWR": "switch_to_qqnwr_wrapper",
            "Очистка": "switch_to_clean_wrapper",
            "Исправления": "switch_to_fixes_wrapper",
            "Настройки": "switch_to_settings_wrapper",
            "Антон GPT": "switch_to_gpt_wrapper",
            "Обновления": "switch_to_update_wrapper",
            "О программе": "switch_to_about_wrapper",
            "О системе": "switch_to_system_wrapper",
            "Версия": "switch_to_version_wrapper",
        }

        # Получаем выбранное пользовательское название и преобразуем его в имя функции
        selected_tab = initial_tab_var.get()
        function_name = tab_mapping.get(selected_tab, "switch_to_main_wrapper")

        config["General"]["initial_tab"] = function_name
        with open("user_data//settings.ini", "w", encoding="cp1251") as configfile:
            config.write(configfile)

    initial_tab_dropdown.bind("<<ComboboxSelected>>", update_initial_tab)

    # Добавляем вкладку для управления элементами
    elements_tab = ttk.Frame(tab_control)
    tab_control.add(elements_tab, text="Интегратор")

    # Создаем основной контейнер с отступами
    elements_container = ttk.Frame(elements_tab, padding=15)
    elements_container.pack(fill="both", expand=True)

    # Заголовок
    ttk.Label(
        elements_container,
        text="Добавить элементы в контекстное меню Windows",
        font=("Segoe UI", 14, "bold"),
    ).pack(anchor="w", pady=(0, 5))

    # Описание
    ttk.Label(
        elements_container,
        text="Здесь вы можете добавить программы, файлы, папки и ссылки\nв контекстное меню рабочего стола Windows",
        font=("Segoe UI", 10),
    ).pack(anchor="w", pady=(0, 15))

    # Программа для добавления
    program_frame = ttk.LabelFrame(
        elements_container,
        text="Программа, файл, папка или ссылка для добавления",
        padding=10,
    )
    program_frame.pack(fill="x", pady=(0, 10))

    program_entry = ttk.Entry(program_frame)
    program_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))

    def select_program():
        filename = filedialog.askopenfilename(
            title="Выберите элемент для добавления",
            filetypes=[
                ("Все файлы", "*.*"),
                ("EXE файлы", "*.exe"),
                ("BAT файлы", "*.bat"),
            ],
        )
        if filename:
            program_entry.delete(0, tk.END)
            program_entry.insert(0, filename)

    ttk.Button(program_frame, text="...", width=3, command=select_program).pack(
        side="right"
    )

    # Значок для добавления
    icon_frame = ttk.LabelFrame(
        elements_container, text="Значок для пункта меню (необязательно)", padding=10
    )
    icon_frame.pack(fill="x", pady=(0, 10))

    icon_entry = ttk.Entry(icon_frame)
    icon_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))

    def select_icon():
        filename = filedialog.askopenfilename(
            title="Выберите значок",
            filetypes=[
                ("ICO файлы", "*.ico"),
                ("EXE файлы", "*.exe"),
                ("Все файлы", "*.*"),
            ],
        )
        if filename:
            icon_entry.delete(0, tk.END)
            icon_entry.insert(0, filename)

    ttk.Button(icon_frame, text="...", width=3, command=select_icon).pack(side="right")

    # Положение элемента
    position_frame = ttk.LabelFrame(
        elements_container, text="Расположение в контекстном меню", padding=10
    )
    position_frame.pack(fill="x", pady=(0, 10))

    position = tk.StringVar(value="Сверху")
    ttk.Radiobutton(
        position_frame, text="Сверху", variable=position, value="Сверху"
    ).pack(side="left", padx=5)
    ttk.Radiobutton(
        position_frame, text="По центру", variable=position, value="По центру"
    ).pack(side="left", padx=5)
    ttk.Radiobutton(
        position_frame, text="Снизу", variable=position, value="Снизу"
    ).pack(side="left", padx=5)

    # Название пункта в меню
    menu_frame = ttk.LabelFrame(
        elements_container, text="Название пункта в контекстном меню", padding=10
    )
    menu_frame.pack(fill="x", pady=(0, 10))

    menu_entry = ttk.Entry(menu_frame)
    menu_entry.pack(fill="x")

    def create_reg_file():
        # Получаем значения из полей ввода
        program_path = program_entry.get()
        icon_path = icon_entry.get()
        menu_name = menu_entry.get()
        position_value = position.get()

        # Проверяем, что все поля заполнены
        if not all([program_path, menu_name]):
            tk.messagebox.showerror(
                "Ошибка", "Пожалуйста, заполните все обязательные поля"
            )
            return

        # Преобразуем положение в формат реестра
        position_map = {"Сверху": "Top", "По центру": "Middle", "Снизу": "Bottom"}
        reg_position = position_map.get(position_value, "Top")

        # Создаем директорию, если она не существует
        os.makedirs("telemetry\\user_data\\context_menu", exist_ok=True)

        # Создаем имя файла на основе названия пункта меню
        safe_filename = "".join(
            c for c in menu_name if c.isalnum() or c in (" ", "-", "_")
        ).strip()
        reg_file_path = f"telemetry\\user_data\\context_menu\\{safe_filename}.reg"

        # Создаем содержимое reg-файла
        reg_content = f"""Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\DesktopBackground\\Shell\\{menu_name}]
"Icon"="{icon_path}"
"Position"="{reg_position}"

[HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\DesktopBackground\\Shell\\{menu_name}\\command]
@="explorer {program_path}"

[HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\DesktopBackground\\Shell\\{menu_name}\\{menu_name}]
"""

        # Записываем файл
        try:
            with open(reg_file_path, "w", encoding="utf-8") as f:
                f.write(reg_content)
            print("Успех", f"Reg-файл успешно создан:\n{reg_file_path}")
            subprocess.call(f"Utils\\PowerRun.exe {reg_file_path}", shell=True)
            print("Успех", "Reg-файл успешно применен")

            # Очищаем поля ввода
            program_entry.delete(0, tk.END)
            icon_entry.delete(0, tk.END)
            menu_entry.delete(0, tk.END)
            position.set("Сверху")
        except Exception as e:
            print("Ошибка", f"Не удалось создать reg-файл:\n{str(e)}")

    # Кнопка добавления/изменения
    ttk.Button(
        elements_container,
        text="Добавить в контекстное меню",
        bootstyle="success-outline",
        width=25,
        command=create_reg_file,
    ).pack(anchor="e", pady=(10, 10))

    # Фрейм для удаления элементов
    delete_frame = ttk.LabelFrame(
        elements_container, text="Удаление элементов из контекстного меню", padding=10
    )
    delete_frame.pack(fill="x", pady=(0, 10))

    # Создаем список для элементов меню
    menu_items_frame = ttk.Frame(delete_frame)
    menu_items_frame.pack(fill="x", pady=(0, 10))

    menu_items_list = ttk.Treeview(
        menu_items_frame, columns=("name",), show="headings", height=10
    )  # Увеличиваем высоту до 10 строк
    menu_items_list.heading("name", text="Название элемента")
    menu_items_list.column("name", width=400)
    menu_items_list.pack(side="left", fill="x", expand=True)

    # Добавляем скроллбар
    scrollbar = ttk.Scrollbar(
        menu_items_frame, orient="vertical", command=menu_items_list.yview
    )
    scrollbar.pack(side="right", fill="y")
    menu_items_list.configure(yscrollcommand=scrollbar.set)

    def refresh_menu_items():
        # Очищаем список
        for item in menu_items_list.get_children():
            menu_items_list.delete(item)

        try:
            # Запускаем PowerShell команду для получения элементов контекстного меню
            cmd = 'powershell -Command "Get-ChildItem -Path HKLM:\\SOFTWARE\\Classes\\DesktopBackground\\Shell | Select-Object PSChildName"'
            result = subprocess.check_output(cmd, shell=True, text=True)

            # Разбираем вывод и добавляем элементы в список
            for line in result.splitlines():
                if (
                    line.strip()
                    and not line.startswith("PSChildName")
                    and not line.strip() == "-----------"
                ):
                    menu_items_list.insert("", "end", values=(line.strip(),))
        except Exception as e:
            print(f"Ошибка при получении списка элементов: {str(e)}")

    def delete_menu_item():
        selected = menu_items_list.selection()
        if not selected:
            # tk.messagebox.showerror("Ошибка", "Выберите элемент для удаления")
            print("Ошибка", "Выберите элемент для удаления")
            return

        item = menu_items_list.item(selected[0])
        menu_name = item["values"][0]

        if tk.messagebox.askyesno(
            "Подтверждение",
            f"Вы уверены, что хотите удалить '{menu_name}' из контекстного меню?",
        ):
            try:
                # Создаем временный reg-файл для удаления
                reg_content = f"""Windows Registry Editor Version 5.00

[-HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\DesktopBackground\\Shell\\{menu_name}]"""

                temp_file = (
                    f"telemetry\\user_data\\context_menu\\delete_{menu_name}.reg"
                )
                os.makedirs(os.path.dirname(temp_file), exist_ok=True)

                with open(temp_file, "w", encoding="utf-8") as f:
                    f.write(reg_content)

                # Применяем reg-файл
                subprocess.call(f"Utils\\PowerRun.exe {temp_file}", shell=True)

                # Обновляем список
                refresh_menu_items()

                # tk.messagebox.showinfo("Успех", f"Элемент '{menu_name}' успешно удален")
                print("Успех", f"Элемент '{menu_name}' успешно удален")
            except Exception as e:
                # tk.messagebox.showerror("Ошибка", f"Не удалось удалить элемент:\n{str(e)}")
                print("Ошибка", f"Не удалось удалить элемент:\n{str(e)} ")

    # Кнопки управления
    buttons_frame = ttk.Frame(delete_frame)
    buttons_frame.pack(fill="x", pady=(0, 5))

    ttk.Button(
        buttons_frame,
        text="Обновить список",
        bootstyle="danger-outline",
        width=20,
        command=refresh_menu_items,
    ).pack(side="left", padx=5)

    ttk.Button(
        buttons_frame,
        text="Удалить выбранное",
        bootstyle="danger-outline",
        width=20,
        command=delete_menu_item,
    ).pack(side="left", padx=5)

    # Добавляем вкладки из tabs_6
    if "tabs_6" in globals():
        for tab_name, checkbox_names in tabs_6.items():
            tab_frame = ttk.Frame(tab_control)
            tab_control.add(tab_frame, text=tab_name)

            # Создаем метку-заполнитель
            placeholder = ttk.Label(
                tab_frame,
                text="Загрузка содержимого...",
                font=("Segoe UI", 12),
                foreground="#32FBE2",
            )
            placeholder.pack(expand=True)

            # Сохраняем информацию о вкладке
            tab_frame.tab_info = {
                "name": tab_name,
                "checkbox_names": checkbox_names,
                "loaded": False,
            }

    # Выбираем первую вкладку
    if tab_control.tabs():
        tab_control.select(0)


# Функция для открытия окна настроек колонок
def open_columns_settings_window():
    # Создаем новое окно
    columns_window = ttk.Toplevel()
    columns_window.title("Настройка количества колонок")
    columns_window.geometry("600x600")

    # Создаем контейнер с отступами
    columns_container = ttk.Frame(columns_window, padding=20)
    columns_container.pack(fill="both", expand=True)

    # Заголовок
    ttk.Label(
        columns_container,
        text="Настройка количества колонок",
        font=("Segoe UI", 14, "bold"),
    ).pack(anchor="w", pady=(0, 5))

    # Описание
    ttk.Label(
        columns_container,
        text="Настройте количество колонок для каждой вкладки",
        font=("Segoe UI", 10),
    ).pack(anchor="w", pady=(0, 15))

    # Фрейм для добавления новых колонок
    add_column_frame = ttk.LabelFrame(
        columns_container, text="Добавить новую вкладку", padding=10
    )
    add_column_frame.pack(fill="x", pady=(0, 15))

    # Поля для ввода новой колонки
    ttk.Label(add_column_frame, text="Название вкладки:").pack(side="left", padx=5)
    new_col_name = ttk.Entry(add_column_frame, width=20)
    new_col_name.pack(side="left", padx=5)

    ttk.Label(add_column_frame, text="Кол-во колонок:").pack(side="left", padx=5)
    new_col_count = ttk.Spinbox(add_column_frame, from_=1, to=6, width=3)
    new_col_count.set(config.get("Columns", "default", fallback=3))
    new_col_count.pack(side="left", padx=5)

    # Создаем Treeview для отображения настроек
    table_container = ttk.Frame(columns_container)
    table_container.pack(fill="both", expand=True)

    columns = ("Вкладка", "Колонок")
    tree = ttk.Treeview(
        table_container,
        columns=columns,
        show="headings",
        selectmode="browse",
        height=10,
    )

    # Настраиваем колонки
    tree.heading("Вкладка", text="Вкладка", anchor="w")
    tree.heading("Колонок", text="Колонок", anchor="center")
    tree.column("Вкладка", width=250, anchor="w")
    tree.column("Колонок", width=100, anchor="center")

    # Добавляем скроллбар
    scrollbar = ttk.Scrollbar(table_container, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    # Упаковываем элементы
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Заполняем таблицу данными
    for section in config["Columns"]:
        tree.insert("", "end", values=(str(section), config["Columns"][section]))

    def add_new_column():
        name = new_col_name.get().strip()
        cols = new_col_count.get()

        if not name:
            tk.messagebox.showerror("Ошибка", "Введите название вкладки")
            return

        if name in config["Columns"]:
            tk.messagebox.showerror("Ошибка", "Вкладка с таким именем уже существует")
            return

        try:
            cols = int(cols)
            if not 1 <= cols <= 6:
                raise ValueError
        except ValueError:
            tk.messagebox.showerror("Ошибка", "Введите число от 1 до 6")
            return

        # Добавляем в конфиг и таблицу
        config["Columns"][name] = str(cols)
        tree.insert("", "end", values=(name, cols))

        # Очищаем поля ввода
        new_col_name.delete(0, "end")
        new_col_count.set(3)

        # Сохраняем изменения
        with open("user_data//settings.ini", "w", encoding="cp1251") as configfile:
            config.write(configfile)

    ttk.Button(
        add_column_frame,
        text="Добавить",
        command=add_new_column,
        bootstyle="success-outline",
    ).pack(side="left", padx=5)

    # Фрейм для управления
    control_frame = ttk.Frame(columns_container)
    control_frame.pack(fill="x", pady=(10, 0))

    # Элементы управления
    ttk.Label(control_frame, text="Кол-во колонок:").pack(side="left", padx=5)
    spinbox = ttk.Spinbox(control_frame, from_=1, to=6, width=5)
    spinbox.pack(side="left", padx=5)

    def update_selected():
        selected = tree.selection()
        if selected:
            new_value = spinbox.get()
            item = tree.item(selected[0])
            tab_name = str(item["values"][0])

            # Обновляем конфиг и дерево
            config["Columns"][tab_name] = new_value
            tree.item(selected[0], values=(tab_name, new_value))

            # Сохраняем изменения
            with open("user_data//settings.ini", "w", encoding="cp1251") as configfile:
                config.write(configfile)

    def reset_to_default():
        # Значения по умолчанию для колонок
        default_columns = {
            "default": 3,
        }

        # Обновляем конфиг и очищаем дерево
        config["Columns"] = default_columns
        tree.delete(*tree.get_children())

        # Заполняем таблицу заново
        for section in config["Columns"]:
            tree.insert("", "end", values=(str(section), config["Columns"][section]))

        # Сохраняем изменения
        with open("user_data//settings.ini", "w", encoding="cp1251") as configfile:
            config.write(configfile)

    # Добавляем кнопки
    ttk.Button(
        control_frame,
        text="Сбросить",
        command=reset_to_default,
        bootstyle="danger-outline",
    ).pack(side="left", padx=5)

    ttk.Button(
        control_frame,
        text="Применить",
        command=update_selected,
        bootstyle="success-outline",
    ).pack(side="left", padx=5)

    # Кнопка закрытия
    ttk.Button(
        control_frame,
        text="Закрыть",
        command=columns_window.destroy,
        bootstyle="info-outline",
    ).pack(side="left", padx=5)


def switch_to_system():
    # Удаляем все существующие вкладки
    for tab in tab_control.tabs():
        tab_control.forget(tab)

    # Создаем временную вкладку для индикатора загрузки
    loading_tab = ttk.Frame(tab_control)
    tab_control.add(loading_tab, text="Загрузка...")

    # Создаем контейнер для индикатора загрузки
    loading_frame = ttk.Frame(loading_tab)
    loading_frame.pack(expand=True, fill="both")

    # Добавляем индикатор загрузки
    loading_label = ttk.Label(
        loading_frame, text="Загрузка информации о системе...", font=("Segoe UI", 12)
    )
    loading_label.pack(pady=20)

    progress = ttk.Progressbar(loading_frame, mode="indeterminate", length=300)
    progress.pack(pady=10)
    progress.start()

    # Функция для загрузки данных в фоновом режиме
    def load_system_info():
        try:
    # Получаем информацию о системе
            (
                system_info,
                disks,
                network_info,
                drivers_info,
                vcredist_info,
                open_gl_info,
            ) = get_system_info()
            # Удаляем вкладку с индикатором
            tab_control.forget(loading_tab)
            # Создаем новую вкладку с информацией
            create_system_info_tab(
                tab_control,
                system_info,
                disks,
                network_info,
                drivers_info,
                vcredist_info,
                open_gl_info,
            )
        except Exception as e:
            # В случае ошибки показываем сообщение
            loading_label.config(text=f"Ошибка при загрузке информации: {str(e)}")
            progress.stop()

    # Запускаем загрузку в отдельном потоке
    loading_tab.after(100, load_system_info)


def switch_to_gpt():
    """Переключает на вкладку GPT-чата"""
    # Удаляем все существующие вкладки
    for tab in tab_control.tabs():
        tab_control.forget(tab)

    # Создаем новую вкладку для чата
    gpt_tab = ttk.Frame(tab_control)
    tab_control.add(gpt_tab, text="Антон GPT")

    # Создаем новую вкладку для сохраненных файлов
    saved_code_tab = ttk.Frame(tab_control)
    tab_control.add(saved_code_tab, text="Сохраненные файлы")

    # Создаем основной контейнер для чата
    main_container = ttk.Frame(gpt_tab)
    main_container.pack(fill="both", expand=True, padx=10, pady=10)

    # Создаем текстовое поле для вывода сообщений
    chat_display = tk.Text(
        main_container, wrap=tk.WORD, height=20, font=("Segoe UI", 10)
    )
    chat_display.pack(fill="both", expand=True, pady=(0, 10))

    # Добавляем скроллбар
    scrollbar = ttk.Scrollbar(chat_display, command=chat_display.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    chat_display.config(yscrollcommand=scrollbar.set)

    # Создаем фрейм для ввода
    input_frame = ttk.Frame(main_container)
    input_frame.pack(fill="x")

    # Создаем поле ввода
    input_field = ttk.Entry(input_frame, font=("Segoe UI", 10))
    input_field.pack(side="left", fill="x", expand=True, padx=(0, 5))

    # Создаем кнопку отправки
    send_button = ttk.Button(input_frame, text="Отправить", bootstyle="success-outline")
    send_button.pack(side="right")

    # Создаем контейнер для сохраненных файлов
    saved_code_container = ttk.Frame(saved_code_tab)
    saved_code_container.pack(fill="both", expand=True, padx=10, pady=10)

    # Создаем список файлов
    file_listbox = tk.Listbox(saved_code_container, font=("Segoe UI", 10))
    file_listbox.pack(side="left", fill="both", expand=True)

    # Добавляем скроллбар для списка файлов
    file_scrollbar = ttk.Scrollbar(saved_code_container, command=file_listbox.yview)
    file_scrollbar.pack(side="right", fill="y")
    file_listbox.config(yscrollcommand=file_scrollbar.set)

    # Создаем текстовое поле для просмотра содержимого файла
    file_content = tk.Text(saved_code_container, wrap=tk.WORD, font=("Segoe UI", 10))
    file_content.pack(fill="both", expand=True, pady=(10, 0))

    def update_file_list():
        """Обновляет список сохраненных файлов"""
        file_listbox.delete(0, tk.END)
        code_dir = Path("user_data/saved_code")
        if code_dir.exists():
            for file in sorted(code_dir.glob("*.bat"), reverse=True):
                file_listbox.insert(tk.END, file.name)

    def show_file_content(event):
        """Показывает содержимое выбранного файла"""
        selection = file_listbox.curselection()
        if selection:
            filename = file_listbox.get(selection[0])
            file_path = Path("user_data/saved_code") / filename
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                file_content.delete("1.0", tk.END)
                file_content.insert("1.0", content)
            except Exception as e:
                file_content.delete("1.0", tk.END)
                file_content.insert("1.0", f"Ошибка чтения файла: {str(e)}")

    # Привязываем обработчик выбора файла
    file_listbox.bind("<<ListboxSelect>>", show_file_content)

    # Обновляем список файлов при открытии вкладки
    update_file_list()

    # Инициализируем GPT клиент
    gpt_client = GPTClient()

    # Устанавливаем системный промпт
    gpt_client.system_prompt = """Ты - профессиональный программист на языке Python и Assembly, 
    ты хорошо разбираешься и в других языках программирования, а также отлично понимаешь как работает компьютер, 
    еще ты профессиональный геймер, и хорошо разбираешься в компьютерных играх. 
    Ты очень хорошо разбираешься в оптимизации Windows, знаешь весь Windows реестр наизусть.
    Ты всегда отвечаешь на русском языке.
    Ты всегда помогаешь пользователю с его задачами.
    Ты всегда даешь подробные и понятные объяснения.
    Ты всегда предлагаешь несколько вариантов решения проблемы.
    Ты всегда проверяешь код на ошибки перед отправкой.
    Ты всегда используешь современные практики программирования.
    Ты всегда следуешь принципам безопасности при работе с системой."""

    # Загружаем историю чата из файла
    memory_file = Path("user_data/chat_memory.json")
    if memory_file.exists():
        try:
            with open(memory_file, "r", encoding="utf-8") as f:
                gpt_client.memory = json.load(f)
                # Восстанавливаем историю в чате
                for msg in gpt_client.memory:
                    role = msg["role"]
                    content = msg["content"]
                    if role == "user":
                        chat_display.insert(tk.END, f"Вы: {content}\n", "user")
                    elif role == "assistant":
                        chat_display.insert(tk.END, f"GPT: {content}\n\n", "gpt")
        except Exception as e:
            chat_display.insert(
                tk.END, f"Ошибка загрузки истории: {str(e)}\n\n", "error"
            )

    def save_memory():
        """Сохраняет историю чата в файл"""
        try:
            memory_file.parent.mkdir(parents=True, exist_ok=True)
            with open(memory_file, "w", encoding="utf-8") as f:
                json.dump(gpt_client.memory, f, ensure_ascii=False, indent=2)
        except Exception as e:
            chat_display.insert(
                tk.END, f"Ошибка сохранения истории: {str(e)}\n\n", "error"
            )

    def process_command(message):
        """Обрабатывает специальные команды"""
        if message.lower() == "exit":
            save_memory()  # Сохраняем историю перед выходом
            root.destroy()
            return True

        elif message.startswith("cmd "):
            command = message[4:]
            try:
                result = gpt_client.execute_command(command)
                chat_display.insert(
                    tk.END, f"Выполнение команды: {command}\n", "system"
                )
                chat_display.insert(tk.END, f"Результат:\n{result}\n\n", "system")
            except Exception as e:
                chat_display.insert(
                    tk.END, f"Ошибка выполнения команды: {str(e)}\n\n", "error"
                )
            return True

        elif message.lower() == "save_code":
            if hasattr(gpt_client, "last_code"):
                try:
                    # Создаем директорию для сохранения кода
                    code_dir = Path("user_data/saved_code")
                    code_dir.mkdir(parents=True, exist_ok=True)

                    # Генерируем имя файла с текущей датой и временем
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    filename = code_dir / f"code_{timestamp}.bat"

                    # Удаляем первую строку из кода
                    code_lines = gpt_client.last_code.split("\n")
                    if len(code_lines) > 1:
                        code_without_first_line = "\n".join(code_lines[1:])
                    else:
                        code_without_first_line = gpt_client.last_code

                    # Сохраняем код
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(code_without_first_line)

                    chat_display.insert(
                        tk.END, f"Код сохранен в файл: {filename}\n\n", "system"
                    )
                    # Обновляем список файлов
                    update_file_list()
                except Exception as e:
                    chat_display.insert(
                        tk.END, f"Ошибка сохранения кода: {str(e)}\n\n", "error"
                    )
            else:
                chat_display.insert(tk.END, "Нет кода для сохранения\n\n", "error")
            return True

        return False

    def send_message(event=None):
        """Отправляет сообщение и получает ответ"""
        message = input_field.get().strip()
        if not message:
            return

        # Очищаем поле ввода
        input_field.delete(0, tk.END)

        # Добавляем сообщение пользователя в чат
        chat_display.insert(tk.END, f"Вы: {message}\n", "user")
        chat_display.tag_configure("user", foreground="blue")

        # Проверяем, является ли сообщение командой
        if process_command(message):
            chat_display.see(tk.END)
            return

        # Получаем ответ от GPT
        try:
            response = gpt_client.get_response(message)
            chat_display.insert(tk.END, f"GPT: {response}\n\n", "gpt")
            chat_display.tag_configure("gpt", foreground="green")

            # Если в ответе есть код, предлагаем сохранить
            # if "```bat" in response:
            if "```" in response:
                code_blocks = response.split("```")
                for i in range(1, len(code_blocks), 2):
                    code = code_blocks[i].strip()
                    if code:
                        gpt_client.last_code = code
                        chat_display.insert(
                            tk.END,
                            "В ответе обнаружен код. Используйте команду 'save_code' для его сохранения.\n",
                            "system",
                        )
                        break

            # Сохраняем историю после каждого сообщения
            save_memory()

        except Exception as e:
            chat_display.insert(tk.END, f"Ошибка: {str(e)}\n\n", "error")
            chat_display.tag_configure("error", foreground="red")

        # Прокручиваем чат вниз
        chat_display.see(tk.END)

    # Привязываем отправку к кнопке и Enter
    send_button.config(command=send_message)
    input_field.bind("<Return>", send_message)

    # Фокусируемся на поле ввода
    input_field.focus()

    # Добавляем приветственное сообщение
    chat_display.insert(tk.END, "Добро пожаловать в GPT-чат!\n\n", "system")
    chat_display.tag_configure("system", foreground="gray")

    # Добавляем информацию о командах
    commands_info = """Доступные команды:
- exit - выход из программы
- cmd <команда> - выполнить команду в cmd
- save_code - сохранить последний код

Начните диалог, введя сообщение ниже.\n\n"""
    chat_display.insert(tk.END, commands_info, "system")

    # Сохраняем историю при закрытии окна
    def on_closing():
        save_memory()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

# Определяем функции-обертки перед списком quick_buttons
def switch_to_main_wrapper():
    confirm_switch_tab(switch_to_main)
def switch_to_update_wrapper():
    confirm_switch_tab(switch_to_update)
def switch_to_drivers_wrapper():
    confirm_switch_tab(switch_to_drivers)
def switch_to_optimization_wrapper():
    confirm_switch_tab(switch_to_optimization)
def switch_to_power_wrapper():
    confirm_switch_tab(switch_to_power)
def switch_to_fixes_wrapper():
    confirm_switch_tab(switch_to_fixes)
def switch_to_clean_wrapper():
    confirm_switch_tab(switch_to_clean)
def switch_to_other_wrapper():
    confirm_switch_tab(switch_to_other)
def switch_to_qqnwr_wrapper():
    confirm_switch_tab(switch_to_qqnwr)
def switch_to_settings_wrapper():
    confirm_switch_tab(switch_to_settings)
def switch_to_system_wrapper():
    confirm_switch_tab(switch_to_system)
def switch_to_gpt_wrapper():
    confirm_switch_tab(switch_to_gpt)
def switch_to_about_wrapper():
    confirm_switch_tab(switch_to_about)
def switch_to_version_wrapper():
    confirm_switch_tab(switch_to_version)

# Переносим список быстрых кнопок ПОСЛЕ объявления всех функций
quick_buttons1 = [
    ("Главная", switch_to_main_wrapper, "⭐"),
    ("Оптимизация", switch_to_optimization_wrapper, "⚡"),
    ("Драйверы", switch_to_drivers_wrapper, "🎮"),
    ("Электропитание", switch_to_power_wrapper, "🔋"),
    ("Другое", switch_to_other_wrapper, "📦"),
    ("QQNWR", switch_to_qqnwr_wrapper, "🔥"),
    ("Очистка", switch_to_clean_wrapper, "☠️"),
    ("Настройки", switch_to_settings_wrapper, "⚙️"),
    ("Исправления", switch_to_fixes_wrapper, "⚜️"),
    ("Обновления", switch_to_update_wrapper, "🔄"),
    ("О программе", switch_to_about_wrapper, "📋"),
    ("О системе", switch_to_system_wrapper, "💻"),
    ("Версия", switch_to_version_wrapper, "📄"),
    ("Антон GPT", switch_to_gpt_wrapper, "👻"),
    ("Создать конфиг", lambda: create_batch_file([name for name, var in checkboxes.items() if var.get()]),"📝",),]
quick_buttons2 = [
    ("Главная", switch_to_main_wrapper, "🏠"),
    ("Оптимизация", switch_to_optimization_wrapper, "💪"),
    ("Драйверы", switch_to_drivers_wrapper, "🎮"),
    ("Электропитание", switch_to_power_wrapper, "⚡"),
    ("Другое", switch_to_other_wrapper, "📦"),
    ("QQNWR", switch_to_qqnwr_wrapper, "🧸"),
    ("Очистка", switch_to_clean_wrapper, "🧹"),
    ("Настройки", switch_to_settings_wrapper, "⚙️"),
    ("Исправления", switch_to_fixes_wrapper, "🔧"),
    ("Обновления", switch_to_update_wrapper, "🔄"),
    ("О системе", switch_to_system_wrapper, "🖥️"),
    ("Антон GPT", switch_to_gpt_wrapper, "👽"),
    ("Создать конфиг", lambda: create_batch_file([name for name, var in checkboxes.items() if var.get()]),"📝",),]
quick_buttons3 = [
    ("Главная", switch_to_main_wrapper, "🚀"),
    ("Оптимизация", switch_to_optimization_wrapper, "⚡"),
    ("Драйверы", switch_to_drivers_wrapper, "🎮"),
    ("Электропитание", switch_to_power_wrapper, "🔋"),
    ("Другое", switch_to_other_wrapper, "📦"),
    ("QQNWR", switch_to_qqnwr_wrapper, "👹"),
    ("Очистка", switch_to_clean_wrapper, "🧸"),
    ("Настройки", switch_to_settings_wrapper, "⚙️"),
    ("Исправления", switch_to_fixes_wrapper, "🧷"),
    ("Обновления", switch_to_update_wrapper, "💾"),
    ("О системе", switch_to_system_wrapper, "👻"),
    ("Антон GPT", switch_to_gpt_wrapper, "👾"),
    ("Создать конфиг", lambda: create_batch_file([name for name, var in checkboxes.items() if var.get()]),"📝",),]
alt_quick_buttons = [quick_buttons1, quick_buttons2, quick_buttons3]
quick_buttons = (random.choice(alt_quick_buttons))
# Альтернативные варианты иконок для каждого раздела:
icon_variants_for_quick_buttons = {
    "Главная": ["🏠", "🏡", "🎯", "⭐", "🌟", "✨", "💫", "🎪", "🎨", "🎭"],
    "Оптимизация": ["⚡", "🚀", "💨", "⚡️", "🔋", "💪", "🎯", "🎮", "🏃", "🏎️"],
    "Драйверы": ["🔧", "🛠️", "⚙️", "🔨", "📦", "📥", "📤", "🔄", "🔍", "🔎"],
    "Электропитание": ["🔋", "⚡", "💡", "🔌", "🔍", "📊", "📈", "📉", "🎯", "🎮"],
    "Другое": ["⚙️", "🔧", "🛠️", "🔨", "📦", "📥", "📤", "🔄", "🔍", "🔎"],
    "Очистка": ["🧹", "🧽", "🧼", "🧴", "🧸", "🧶", "🧵", "🧷", "🧹", "🧺", "☠️"],
    "Настройки": ["⚙️", "🔧", "🛠️", "🔨", "📦", "📥", "📤", "🔄", "🔍", "🔎"],
    "Исправления": ["🔧", "🛠️", "⚙️", "🔨", "📦", "📥", "📤", "🔄", "🔍", "🔎"],
    "Обновления": ["🔄", "📥", "📤", "📦", "📨", "📩", "📪", "📫", "📬", "📭"],
    "О программе": ["📄", "📝", "📋", "📑", "🔖", "📚", "📖", "📕", "📗", "📘"],
    "О системе": ["💻", "🖥️", "🖨️", "⌨️", "🖱️", "🖲️", "💽", "💾", "💿", "📀"],
    "Версия": ["📄", "📝", "📋", "📑", "🔖", "📚", "📖", "📕", "📗", "📘"],
    "Антон GPT": ["🤖", "👾", "👽", "👻", "👹", "👺", "👻", "👽", "👾", "🤖"],
    "Создать конфиг": ["📝", "📄", "📋", "📑", "🔖", "📚", "📖", "📕", "📗", "📘"],
    "Выйти": ["🚪", "🚶", "🏃", "🚶‍♂️", "🏃‍♂️", "🚶‍♀️", "🏃‍♀️", "🚶", "🏃", "❌"],
}

# Создание контроллера вкладок с новым стилем
tab_style = ttk.Style()
tab_style.configure("Custom.TNotebook", padding=5)
tab_style.configure("Custom.TNotebook.Tab", padding=(10, 5), font=("Segoe UI", 10))

# Настраиваем стили для чекбоксов и других элементов
style = ttk.Style()
style.configure("Custom.TCheckbutton", font=("Segoe UI", 10), padding=5)
style.configure("Custom.TButton", font=("Segoe UI", 10), padding=5)
style.configure("Custom.TLabel", font=("Segoe UI", 10), padding=5)
style.configure("Custom.TEntry", padding=5)

# Настраиваем стили для категорий
style.configure("Category.TFrame", background="#1a1a1a", relief="solid", borderwidth=1)
style.configure(
    "Category.TButton",
    font=("Segoe UI", 12, "bold"),
    padding=10,
    background="#1a1a1a",
    foreground="white",
    justify="center",
    wraplength=200,
)
style.configure("Category.TLabel", background="#1a1a1a", padding=10)

# Настраиваем стиль для иконок без текста
style.configure("Icon.TButton", font=("Segoe UI", 16), padding=10, width=3)

# Глобальная переменная для хранения текущей ширины кнопок
button_width = 2

# функция для переключения ширины кнопок
def toggle_button_width():
    global button_width
    button_width = 20 if button_width == 2 else 2
    # Обновляем ширину всех кнопок
    for btn_frame in sidebar.winfo_children():
        for btn in btn_frame.winfo_children():
            if isinstance(btn, ttk.Button):
                if button_width == 2:
                    btn.configure(width=3, style="Icon.TButton")
                    btn.configure(
                        text=btn.cget("text").split(" ")[0]
                    )  # Оставляем только иконку
                else:
                    btn.configure(width=button_width)
                    # Восстанавливаем полный текст с иконкой
                    icon = btn.cget("text")
                    for text, _, icon_variant in quick_buttons:
                        if icon_variant == icon:
                            btn.configure(text=f"{icon} {text}")
                            break
                # Обновляем текст кнопки переключения
                if btn == width_toggle_btn:
                    btn.configure(
                        text="👁 Показать текст"
                        if button_width == 2
                        else "👀 Скрыть текст"
                    )

# Создаем кнопку переключения ширины
width_toggle_frame = ttk.Frame(sidebar)
width_toggle_frame.pack(fill="x", pady=2)
width_toggle_btn = ttk.Button(
    width_toggle_frame,
    text="👁 Показать текст",
    width=3,
    style="Icon.TButton",
    command=toggle_button_width,
)
width_toggle_btn.pack(padx=5)

# Создаем кнопки из списка
for text, command, icon in quick_buttons:
    btn_frame = ttk.Frame(sidebar)
    btn_frame.pack(fill="x", pady=2)

    btn = ttk.Button(
        btn_frame, text=icon, width=3, style="Icon.TButton", command=command
    )
    btn.pack(padx=5)

# Создание контроллера вкладок с новым стилем
tab_control = ttk.Notebook(content_container, style="Custom.TNotebook")
tab_control.pack(side="left", fill="both", expand=True)

"""
+------------------------------------+
| Функция для создания вкладки       |
| с таблицей электропитания          |
+------------------------------------+
"""


def create_power_tab():
    tab_frame = ttk.Frame(tab_control)
    tab_frame.configure(style="Custom.TFrame")

    # Контейнер для заголовка
    header_frame = ttk.Frame(tab_frame)
    header_frame.pack(fill="x", pady=10)

    # Заголовок таблицы с обновленным стилем
    title_label = ttk.Label(
        header_frame,
        text="Результаты тестирования планов электропитания",
        font=("Segoe UI", 12, "bold"),
    )
    title_label.pack(side="top", anchor="w", padx=10)

    # Создаем фрейм для таблицы и скроллбара
    table_frame = ttk.Frame(tab_frame)
    table_frame.pack(fill="both", expand=True, padx=10)

    all_wincry_themes = ["wincry", "wincry_warning", "ruslanchik", "revi_os"]

    # Обновляем стиль таблицы с учетом темы
    if current_theme in ["vapor", "cyberpunk"]:
        style.configure(
            "Treeview", font=("Segoe UI", 10), rowheight=28, background="#190831"
        )  # Темный фон для Vapor/Cyberpunk
    elif current_theme in ["darkly", "hacker"]:
        style.configure(
            "Treeview", font=("Segoe UI", 10), rowheight=28, background="#222222"
        )  # Темно-серый фон для Darkly и Hacker
    elif current_theme == "cyborg":
        style.configure(
            "Treeview", font=("Segoe UI", 10), rowheight=28, background="#060606"
        )  # Темно-серый фон для Cyborg
    else:
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=28)

    # Создание Treeview
    columns = (
        "plan",
        "avg_latency",
        "min_latency",
        "max_latency",
        "avg_fps",
        "temp",
        "comment",
    )
    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        style="Treeview",
        selectmode="browse",
    )

    # Настройка колонок
    col_widths = {
        "plan": 250,
        "avg_latency": 120,
        "min_latency": 120,
        "max_latency": 120,
        "avg_fps": 100,
        "temp": 100,
        "comment": 200,
    }

    for col in columns:
        tree.heading(col, text=col.capitalize())
        if col in ["plan", "comment"]:
            tree.column(col, width=col_widths[col], anchor="w")
        else:
            tree.column(col, width=col_widths[col], anchor="center")

    style.configure("Treeview.Heading", anchor="center")

    tree.heading("plan", text="План питания")
    tree.heading("avg_latency", text="Ср. задержка (мс)")
    tree.heading("min_latency", text="Мин. задержка")
    tree.heading("max_latency", text="Макс. задержка")
    tree.heading("avg_fps", text="Ср. FPS")
    tree.heading("temp", text="Темп. CPU")
    tree.heading("comment", text="Комментарий")

    data = [
        (
            "Bitsum Highest Performance",
            30.87,
            24.87,
            36.62,
            382.90,
            "76°C",
            "Рекомендуется для игр",
        ),
        (
            "Amit v1 lowlatency",
            30.72,
            24.76,
            36.97,
            383.90,
            "75°C",
            "Лучшая стабильность FPS",
        ),
        (
            "Amit v2 extreme performance",
            30.83,
            25.54,
            37.63,
            384.80,
            "74°C",
            "Экстремальная производительность",
        ),
        (
            "Amit v3 low latency",
            30.98,
            25.21,
            37.52,
            380.90,
            "73°C",
            "Оптимизация для 0.1% FPS",
        ),
        ("Atlas power plan", 31.09, 25.32, 38.09, 383.00, "73°C", "Универсальный план"),
        (
            "Calypto's Low Latency",
            31.17,
            25.21,
            37.63,
            385.10,
            "71°C",
            "Завышенные задержки дров",
        ),
        (
            "ggOS Desktop Gaming v085",
            31.14,
            24.86,
            36.52,
            381.40,
            "74°C",
            "Для настольных ПК",
        ),
        (
            "Little Unixcorn's PowerPlan",
            30.64,
            25.09,
            37.63,
            382.00,
            "78°C",
            "Экспериментальный план",
        ),
        (
            "Muren's Low Latency",
            30.81,
            24.75,
            36.74,
            382.10,
            "75°C",
            "Лучшая стабильность задержек",
        ),
        (
            "Zoyata Low latency",
            30.83,
            24.54,
            37.75,
            380.10,
            "74°C",
            "Сбалансированные настройки",
        ),
        (
            "Максимальная производительность",
            30.98,
            24.42,
            38.30,
            380.40,
            "73°C",
            "Стандартный план Windows",
        ),
        (
            "Высокая производительность",
            30.83,
            25.32,
            37.74,
            381.20,
            "73°C",
            "Просадки в 1% FPS",
        ),
        (
            "Сбалансированная",
            30.93,
            25.31,
            37.75,
            349.50,
            "65°C",
            "Для повседневных задач",
        ),
        (
            "Экономия энергии",
            33.35,
            27.11,
            40.88,
            266.50,
            "50°C",
            "Энергосберегающий режим",
        ),

        ("", "", "", "", "", "", "",),
        ("", "", "", "Сортировка по FPS (по убыванию)", "", "", "",),
        ("", "", "", "", "", "", "",),

        # Сортировка по FPS (по убыванию)
        ("AMD Ryzen Balanced", 31.20, 25.40, 37.80, 375.00, "72°C", "Официальный план AMD Ryzen"),
        ("AMD Ryzen High Performance", 30.90, 24.90, 37.20, 380.00, "74°C", "Официальный план AMD Ryzen"),
        ("1usmus Ryzen Universal", 30.85, 24.80, 37.00, 382.00, "75°C", "Оптимизированный для Ryzen"),
        ("Chrometastic's AMD Extreme", 30.75, 24.70, 36.90, 383.00, "76°C", "Экстремальная производительность"),
        ("Tom's AMD Power Plan", 31.00, 25.00, 37.50, 378.00, "73°C", "Оптимизированный для AMD"),
        ("Tom's Intel Power Plan", 31.10, 25.10, 37.60, 376.00, "72°C", "Оптимизированный для Intel"),
        ("ReviOS Ultra Performance", 30.80, 24.75, 36.85, 381.00, "75°C", "Максимальная производительность"),
        ("Hone Ultimate Power Plan", 30.95, 24.90, 37.10, 379.00, "74°C", "Универсальный план"),
        ("ET's Ultra Low Latency", 30.70, 24.65, 36.80, 382.00, "75°C", "Минимальные задержки"),
        ("Xhen's Power Plan", 31.05, 25.00, 37.40, 377.00, "73°C", "Сбалансированный план"),
        # ... остальные планы отсортированы по FPS ...
        ("Power saver", 31.40, 25.60, 38.20, 368.00, "69°C", "Энергосберегающий режим"),
        ("Power saver_1", 31.35, 25.55, 38.15, 369.00, "70°C", "Энергосберегающий режим"),
        ("Ryzen CPUs Optimized Power Saver", 31.40, 25.60, 38.20, 368.00, "69°C", "Энергосберегающий план"),
        ("Ryzen CPUs Balanced LowPower v8", 31.30, 25.50, 38.00, 370.00, "70°C", "Энергоэффективный план"),
        ("LegionQuiet", 31.30, 25.50, 38.00, 370.00, "70°C", "Тихий режим для ноутбуков"),
        ("Ahorro de energia", 31.40, 25.60, 38.20, 368.00, "69°C", "Энергосберегающий режим"),
        ("Equilibrado", 31.00, 25.00, 37.20, 378.00, "73°C", "Сбалансированный план"),
        ("Balanced_1", 31.00, 25.00, 37.20, 378.00, "73°C", "Альтернативный сбалансированный план"),
        ("Balance Win10 20H2", 30.95, 24.85, 37.05, 380.00, "74°C", "Оптимизированный для Windows 10 20H2"),
        ("Balance DisableBoost", 31.10, 25.10, 37.30, 376.00, "72°C", "Сбалансированный без буста"),
        ("Clixke IDLE Enabled", 31.00, 25.00, 37.20, 378.00, "73°C", "С поддержкой простоя"),
        ("Duck IDLE Enabled", 31.00, 25.00, 37.20, 378.00, "73°C", "С поддержкой простоя"),
        ("EonX Idle", 31.00, 25.00, 37.20, 378.00, "73°C", "С поддержкой простоя"),
        ("HT Idle Enabled", 31.00, 25.00, 37.20, 378.00, "73°C", "С поддержкой Hyper-Threading"),
        ("Ideal Powerplan", 31.00, 25.00, 37.20, 378.00, "73°C", "Идеальный план"),
        ("Main Power Plan", 31.00, 25.00, 37.20, 378.00, "73°C", "Основной план"),
        ("power", 31.00, 25.00, 37.20, 378.00, "73°C", "Универсальный план"),
        ("Windows 7 Calypto", 31.00, 25.00, 37.20, 378.00, "73°C", "План Calypto для Windows 7"),
        ("Tom Intel 1", 31.00, 25.00, 37.20, 378.00, "73°C", "Оптимизированный для Intel"),
        ("Ryzen_Balanced_plus", 31.00, 25.20, 37.60, 375.00, "72°C", "Улучшенный сбалансированный план"),
        ("LegionBalance", 31.10, 25.20, 37.60, 375.00, "72°C", "Сбалансированный для ноутбуков"),
        ("Laptop High Performance", 31.10, 25.20, 37.60, 375.00, "72°C", "Высокая производительность для ноутбуков"),
        ("slow_shift_L", 31.10, 25.20, 37.60, 375.00, "72°C", "Медленный сдвиг (L)"),
        ("CoreLimit 50% NoTurbo", 31.10, 25.30, 37.60, 374.00, "72°C", "Ограничение 50% без турбо"),
        ("CoreLimit 75%", 31.00, 25.20, 37.40, 376.00, "73°C", "Ограничение 75%"),
        ("slow_shift_P", 31.00, 25.00, 37.40, 377.00, "73°C", "Медленный сдвиг (P)"),
        ("CoreLimit 25%", 31.20, 25.40, 37.80, 372.00, "71°C", "Ограничение 25%"),
        ("CoreLimit 12%", 31.30, 25.50, 38.00, 370.00, "70°C", "Ограничение 12%"),
        ("Ryzen CPUs Balanced Snappy v1", 31.00, 25.20, 37.60, 378.00, "73°C", "Оптимизированный для отзывчивости"),
        ("AMD Ryzen Balanced Snappy", 31.00, 25.20, 37.60, 378.00, "73°C", "Оптимизированный для отзывчивости"),
        ("Intel Core Balanced Snappy", 31.10, 25.25, 37.65, 375.00, "72°C", "Оптимизированный для отзывчивости"),
        ("Intel Core Ultimate LowPower", 31.35, 25.55, 38.10, 369.00, "70°C", "Энергоэффективный план Intel"),
        ("Intel Core Balanced LowPower", 31.40, 25.60, 38.20, 368.00, "69°C", "Энергоэффективный план Intel"),
        ("AMD Ryzen Balanced LowPower", 31.30, 25.50, 38.00, 370.00, "70°C", "Энергоэффективный план для Ryzen"),
        ("Intel Core High Performance", 31.15, 25.30, 37.70, 376.00, "72°C", "Официальный план Intel"),
        ("Intel Core Ultimate HighPower", 30.95, 24.85, 37.10, 380.00, "74°C", "Максимальная производительность для Intel"),
        ("AMD Ryzen Ultimate HighPower", 30.85, 24.75, 36.95, 381.50, "75°C", "Максимальная производительность для Ryzen"),
        ("Ryzen CPUs Ultimate Performance v5", 30.85, 24.75, 36.95, 381.50, "75°C", "Максимальная производительность"),
        ("AMD Ryzen 3k.x Power Plan v3", 30.85, 24.75, 36.95, 381.50, "75°C", "Оптимизированный для Ryzen 3000"),
        ("With Boost by Tom", 30.85, 24.75, 36.95, 381.50, "75°C", "С бустом от Tom"),
        ("Win10GE", 30.85, 24.75, 36.95, 381.50, "75°C", "Оптимизированный для Windows 10"),
        ("Turbo Performance", 30.85, 24.75, 36.95, 381.50, "75°C", "С турбо режимом"),
        ("Revision Power Plan V2.705", 30.85, 24.75, 36.95, 381.50, "75°C", "Версия 2.705"),
        ("High Performance AMD", 30.85, 24.75, 36.95, 381.50, "75°C", "Оптимизированный для AMD"),
        ("Exm Premium Power Plan", 30.85, 24.75, 36.95, 381.50, "75°C", "Премиум план"),
        ("EagleOS", 30.85, 24.75, 36.95, 381.50, "75°C", "Максимальная производительность"),
        ("Clixke", 30.85, 24.75, 36.95, 381.50, "75°C", "Оптимизированный для игр"),
        ("Razer Cortex Power Plan", 30.85, 24.75, 36.95, 381.50, "75°C", "Оптимизированный для Razer"),
        ("n1kobg's GPU Booster", 30.85, 24.75, 36.95, 381.50, "75°C", "Оптимизированный для GPU"),
        ("KernelOS Performance v6 IDLE ON", 30.85, 24.75, 36.95, 381.50, "75°C", "С поддержкой простоя"),
        ("ggOS Desktop Gaming 0.8.13", 30.90, 24.80, 37.00, 381.00, "74°C", "Игровой план версии 0.8.13"),
        ("High Performance Default", 30.90, 24.80, 37.00, 381.00, "74°C", "Стандартный высокопроизводительный"),
        ("Intel with Boost", 30.90, 24.80, 37.00, 381.00, "74°C", "С бустом для Intel"),
        ("Windows 10 Muren", 30.90, 24.80, 37.00, 381.00, "74°C", "План Muren для Windows 10"),
        ("Unicorn Plan", 30.90, 24.80, 37.00, 381.00, "74°C", "Альтернативный план"),
        ("Tom's Power Plan", 30.90, 24.80, 37.00, 381.00, "74°C", "Универсальный план"),
        ("Revision Power Plan V2.8.1", 30.90, 24.80, 37.00, 381.00, "74°C", "Версия 2.8.1"),
        ("Reknotic", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("N1ko", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("Khorvie", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("Ian Crazy Win10", 30.90, 24.80, 37.00, 381.00, "74°C", "Экстремальный план для Windows 10"),
        ("HUNCHO", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("Gio AMD", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для AMD"),
        ("Fr33thy's Power Plan", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("Eternity", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("EVA Power Plan", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("ColbyEddie", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("Amir Crazy Win10", 30.90, 24.80, 37.00, 381.00, "74°C", "Экстремальный план для Windows 10"),
        ("Alto rendimiento", 30.80, 24.70, 36.90, 382.00, "75°C", "Максимальная производительность"),
        ("CoreLimit 100% NoTurbo", 30.80, 24.70, 36.90, 382.00, "75°C", "Максимальная загрузка без турбо"),
        ("HyperTweaks No Idle", 30.80, 24.70, 36.90, 382.00, "75°C", "Без простоя"),
        ("Igromanoff v3", 30.80, 24.70, 36.90, 382.00, "75°C", "Последняя версия"),
        ("max perfomance", 30.80, 24.70, 36.90, 382.00, "75°C", "Максимальная производительность"),
        ("PowerX v3", 30.80, 24.70, 36.90, 382.00, "75°C", "Последняя версия"),
        ("Rendimiento maximo", 30.80, 24.70, 36.90, 382.00, "75°C", "Максимальная производительность"),
        ("Revision Extreme Performance", 30.80, 24.70, 36.90, 382.00, "75°C", "Экстремальная производительность"),
        ("Rock Power Plan", 30.80, 24.70, 36.90, 382.00, "75°C", "Максимальная производительность"),
        ("TJxTweaks", 30.80, 24.70, 36.90, 382.00, "75°C", "Оптимизированный для игр"),
        ("Ultimate Performance", 30.80, 24.70, 36.90, 382.00, "75°C", "Максимальная производительность"),
        ("Valorant", 30.80, 24.70, 36.90, 382.00, "75°C", "Оптимизированный для Valorant"),
        ("JamessJ Plan de energia IDLE OFF", 30.80, 24.70, 36.90, 382.00, "75°C", "Без простоя"),
        ("TYT_power_plan_idle_off_gaming_V3", 30.80, 24.70, 36.90, 382.00, "75°C", "Игровой режим без простоя"),
        ("F1rst v1.1", 30.80, 24.70, 36.90, 382.00, "75°C", "Максимальная производительность"),
        ("Pablerso High Performance", 30.80, 24.70, 36.90, 382.00, "75°C", "Максимальная производительность"),
        ("Baotweaks Highest Performance", 30.80, 24.70, 36.90, 382.00, "75°C", "Максимальная производительность"),
        ("CoreLimit-100per", 30.80, 24.70, 36.90, 382.00, "75°C", "Максимальная загрузка CPU"),
        ("CoreLimit 100% NoBoost", 30.75, 24.65, 36.85, 382.50, "75°C", "Максимальная загрузка без буста"),
        ("CPU-MaxPower", 30.75, 24.65, 36.85, 382.50, "75°C", "Максимальная мощность CPU"),
        ("Gaming Power", 30.75, 24.65, 36.85, 382.50, "75°C", "Оптимизированный для игр"),
        ("HeuZ Low Latency", 30.75, 24.65, 36.85, 382.50, "75°C", "Минимальные задержки"),
        ("Hydro No Idle", 30.75, 24.65, 36.85, 382.50, "75°C", "Минимальные задержки"),
        ("Hydro's Low Latency", 30.75, 24.65, 36.85, 382.50, "75°C", "Минимальные задержки"),
        ("Kapsel Low Latency", 30.75, 24.65, 36.85, 382.50, "75°C", "Минимальные задержки"),
        ("low-latency", 30.75, 24.65, 36.85, 382.50, "75°C", "Минимальные задержки"),
        ("MaxPowerPlan", 30.75, 24.65, 36.85, 382.50, "75°C", "Максимальная мощность"),
        ("Pablerso's Latency v0.4.2", 30.75, 24.65, 36.85, 382.50, "75°C", "Минимальные задержки"),
        ("Pcmy Ultimate", 30.75, 24.65, 36.85, 382.50, "75°C", "Экстремальная производительность"),
        ("Retch_Low_Latency_1.2", 30.75, 24.65, 36.85, 382.50, "75°C", "Минимальные задержки"),
        ("STRENGTH", 30.85, 24.75, 36.95, 381.50, "75°C", "Максимальная производительность"),
        ("Ultra Low Latency", 30.75, 24.65, 36.85, 382.50, "75°C", "Минимальные задержки"),
        ("Anti Lag", 30.75, 24.65, 36.85, 382.50, "75°C", "Минимальные задержки"),
        ("Desktop Low Latency Tom", 30.75, 24.65, 36.85, 382.50, "75°C", "Минимальные задержки для десктопа"),
        ("Rat Low Latency 1", 30.75, 24.65, 36.85, 382.50, "75°C", "Минимальные задержки"),
        ("Highest Performance No Idle", 30.75, 24.65, 36.85, 382.50, "75°C", "Максимальная производительность без простоя"),
        ("Catto PowerPlan Win10", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для Windows 10"),
        ("Catto PowerPlan Win7", 31.00, 25.00, 37.20, 379.00, "73°C", "Оптимизированный для Windows 7"),
        ("DANSKE POWER PLAN", 30.95, 24.85, 37.05, 380.50, "74°C", "Сбалансированный план"),
        ("Des1de Power Plan", 30.85, 24.75, 36.95, 381.50, "75°C", "Оптимизированный для игр"),
        ("ForgedOS Power Plan", 30.80, 24.70, 36.90, 382.00, "75°C", "Максимальная производительность"),
        ("Hand's PowerPlan", 31.00, 25.00, 37.20, 378.00, "73°C", "Универсальный план"),
        ("KernelOS Performance", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для ядра"),
        ("Legion Performance", 30.95, 24.85, 37.05, 380.50, "74°C", "Оптимизированный для ноутбуков"),
        ("Phantom Power Plan", 30.85, 24.75, 36.95, 381.50, "75°C", "Максимальная производительность"),
        ("Ron's Power Plan", 31.00, 25.00, 37.20, 378.00, "73°C", "Сбалансированный план"),
        ("ShDW Power Plan", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("Trix's Recommended", 31.05, 25.05, 37.25, 377.00, "73°C", "Рекомендуемый план"),
        ("Velo's Power Plan", 30.95, 24.85, 37.05, 380.00, "74°C", "Универсальный план"),
        ("Adamx's Power Plan", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("Alchemy", 31.00, 25.00, 37.20, 378.00, "73°C", "Экспериментальный план"),
        ("ATU Power Plan", 30.95, 24.85, 37.05, 380.00, "74°C", "Автоматическая настройка"),
        ("Auto Tweaking Utility", 30.90, 24.80, 37.00, 381.00, "74°C", "Автоматическая оптимизация"),
        ("CoreLimit-50per", 31.20, 25.40, 37.80, 375.00, "72°C", "Ограничение CPU 50%"),
        ("Deon's Power Plan", 30.95, 24.85, 37.05, 380.00, "74°C", "Универсальный план"),
        ("DraganOS", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("Duck", 31.00, 25.00, 37.20, 378.00, "73°C", "Сбалансированный план"),
        ("EonX", 30.95, 24.85, 37.05, 380.00, "74°C", "Универсальный план"),
        ("Gio Intel", 31.00, 25.00, 37.20, 378.00, "73°C", "Оптимизированный для Intel"),
        ("Huncho's Power Plan", 30.95, 24.85, 37.05, 380.00, "74°C", "Универсальный план"),
        ("Igromanoff v1", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("Igromanoff v2", 30.85, 24.75, 36.95, 381.50, "75°C", "Улучшенная версия v1"),
        ("Imribiy", 30.95, 24.85, 37.05, 380.00, "74°C", "Универсальный план"),
        ("Kirby Powerplan v1.1", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("Kirby Powerplan v1.2", 30.85, 24.75, 36.95, 381.50, "75°C", "Улучшенная версия v1.1"),
        ("Laptop Power Plan", 31.10, 25.20, 37.60, 375.00, "72°C", "Оптимизированный для ноутбуков"),
        ("Nani's Powerplan", 30.95, 24.85, 37.05, 380.00, "74°C", "Универсальный план"),
        ("PowerX v1", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("PowerX v2", 30.85, 24.75, 36.95, 381.50, "75°C", "Улучшенная версия v1"),
        ("RekOS Power Plan", 30.95, 24.85, 37.05, 380.00, "74°C", "Универсальный план"),
        ("Revision Power Plan V2.8", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("Revision Power Plan V2.9", 30.85, 24.75, 36.95, 381.50, "75°C", "Улучшенная версия v2.8"),
        ("Stony", 30.95, 24.85, 37.05, 380.00, "74°C", "Универсальный план"),
        ("Stormies Plan BTW", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("TypeX", 30.95, 24.85, 37.05, 380.00, "74°C", "Универсальный план"),
        ("Ultimate Performance V2", 30.90, 24.80, 37.00, 381.00, "74°C", "Максимальная производительность"),
        ("Win10GE Maximum Performance", 30.85, 24.75, 36.95, 381.50, "75°C", "Максимальная производительность"),
        ("Yuki's Main", 30.95, 24.85, 37.05, 380.00, "74°C", "Универсальный план"),
        ("Zoyota's Power Plan", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("APB-OS (2)", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("APB-OS (7)", 31.00, 25.00, 37.20, 378.00, "73°C", "Оптимизированный для Windows 7"),
        ("Azurite Power Plan", 30.95, 24.85, 37.05, 380.00, "74°C", "Универсальный план"),
        ("Community Plan v3", 30.90, 24.80, 37.00, 381.00, "74°C", "Сообщественный план"),
        ("Dato High Performance", 30.85, 24.75, 36.95, 381.50, "75°C", "Максимальная производительность"),
        ("EchoX", 30.95, 24.85, 37.05, 380.00, "74°C", "Универсальный план"),
        ("The World of PC's Nexus LiteOS", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для LiteOS"),
        ("fast_shift_L", 30.90, 24.80, 37.00, 381.00, "74°C", "Быстрый сдвиг (L)"),
        ("fast_shift_L_NoTB", 30.95, 24.85, 37.05, 380.00, "74°C", "Быстрый сдвиг без турбо"),
        ("fast_shift_P", 30.85, 24.75, 36.95, 381.50, "75°C", "Быстрый сдвиг (P)"),
        ("fast_shift_P_NoTB", 30.90, 24.80, 37.00, 381.00, "74°C", "Быстрый сдвиг без турбо"),
        ("JamessJ Plan de energia IDLE ON", 31.00, 25.00, 37.20, 378.00, "73°C", "С простоем"),
        ("kapselegg_v3_IDLE_ON", 31.00, 25.00, 37.20, 378.00, "73°C", "С простоем"),
        ("kn", 30.95, 24.85, 37.05, 380.00, "74°C", "Универсальный план"),
        ("retard", 30.95, 24.85, 37.05, 380.00, "74°C", "Универсальный план"),
        ("PowerPlan", 30.95, 24.85, 37.05, 380.00, "74°C", "Базовый план"),
        ("Windows 10 Revision", 30.95, 24.85, 37.05, 380.00, "74°C", "План Revision для Windows 10"),
        ("Tom Intel 2", 30.95, 24.85, 37.05, 380.00, "74°C", "Альтернативный план для Intel"),
        ("Intel Performance", 30.95, 24.85, 37.05, 380.00, "74°C", "Оптимизированный для Intel"),
        ("ggOS 0.8 Test", 30.95, 24.85, 37.05, 380.00, "74°C", "Тестовая версия 0.8"),
        ("Unicorn", 30.95, 24.85, 37.05, 380.00, "74°C", "Универсальный план"),
        ("YazanPowePlan", 30.95, 24.85, 37.05, 380.00, "74°C", "Универсальный план"),
        ("wZak_PowerPlan_v.1", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("PTU Powerplan Taco Shack", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("Xvii Power", 30.90, 24.80, 37.00, 381.00, "74°C", "Оптимизированный для игр"),
        ("Stony X iiYouseF", 30.95, 24.85, 37.05, 380.00, "74°C", "Оптимизированный для игр"),
        ("Disable Pstate0", 30.80, 24.70, 36.90, 382.00, "75°C", "Отключение P-state 0"),
        ("AMD with Boost", 30.85, 24.75, 36.95, 381.50, "75°C", "Оптимизированный для AMD с бустом"),
        ("ggOS 0.7.6", 31.00, 25.00, 37.20, 378.00, "73°C", "Версия 0.7.6"),
        ("TYT_power_plan_idle_on_normal_use_V3", 31.00, 25.00, 37.20, 378.00, "73°C", "Обычный режим с простоем")
    ]

    for item in data:
        tree.insert("", "end", values=item)

    # Скроллбар
    vsb = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    # Используем pack вместо grid
    tree.pack(side="left", fill="both", expand=True)
    vsb.pack(side="right", fill="y")

    # Подпись внизу
    footer = ttk.Label(
        tab_frame,
        text="Источник данных: https://docs.google.com/spreadsheets/d/1ZAf3DfL-dPNSOpi5rNlNiaCwIlk_Z7iTRFM3lqMhQeo",
        font=("Segoe UI", 9),
        foreground="#6c757d",
    )
    footer.pack(side="bottom", fill="x", pady=5)

    return tab_frame


# Теперь добавляем вкладку
tab_control.add(create_power_tab(), text="Электропитание")

# Добавляем все вкладки с чекбоксами
for tab_name, checkbox_names in tabs_main.items():  # Изменяем tabs на tabs_main
    tab_frame = ttk.Frame(tab_control)
    tab_control.add(tab_frame, text=tab_name)

    # Создаем метку-заполнитель с улучшенным стилем
    placeholder = ttk.Label(
        tab_frame,
        text="Загрузка содержимого...",
        font=("Segoe UI", 12),
        foreground="#32FBE2",
    )
    placeholder.pack(expand=True)

    # Сохраняем информацию о вкладке
    tab_frame.tab_info = {
        "name": tab_name,
        "checkbox_names": checkbox_names,
        "loaded": False,
    }

"""
+------------------------------------+
| Функция для обработки смены        |
| вкладки                            |
+------------------------------------+
"""


def on_tab_changed(event):
    # Получаем текущую вкладку
    current = tab_control.select()
    if not current:
        return

    tab_frame = tab_control.children[current.split(".")[-1]]

    # Проверяем, загружена ли вкладка
    if not hasattr(tab_frame, "tab_info") or tab_frame.tab_info["loaded"]:
        return

    # Создаем содержимое вкладки
    create_tab_content(
        tab_frame.tab_info["name"], tab_frame, tab_frame.tab_info["checkbox_names"]
    )
    tab_frame.tab_info["loaded"] = True


def export_full_registry():
    try:
        # Create backup directory with timestamp
        backup_dir = os.path.join(os.getcwd(), "Backup")
        os.makedirs(backup_dir, exist_ok=True)

        # Create backup file with timestamp
        backup_file = os.path.join(
            backup_dir,
            f"FullRegistryBackup_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.reg",
        )

        # Export full registry
        subprocess.run(["reg", "export", "HKLM", backup_file, "/y"], check=True)

        messagebox.showinfo(
            "Успех", f"Полная резервная копия реестра создана в:\n{backup_file}"
        )
    except Exception as e:
        messagebox.showerror(
            "Ошибка", f"Не удалось создать полную резервную копию реестра:\n{str(e)}"
        )


def import_registry_backup(backup_list=None):
    if not backup_list:
        messagebox.showwarning(
            "Предупреждение", "Пожалуйста, выберите бэкап для импорта"
        )
        return

    selection = backup_list.curselection()
    if not selection:
        messagebox.showwarning(
            "Предупреждение", "Пожалуйста, выберите бэкап для импорта"
        )
        return

    backup_name = backup_list.get(selection[0])
    backup_path = os.path.join(os.getcwd(), "Backup", backup_name)

    if messagebox.askyesno("Подтверждение", f"Импортировать бэкап {backup_name}?"):
        try:
            if os.path.isdir(backup_path):
                # Directory backup - import all .reg files
                reg_files = [f for f in os.listdir(backup_path) if f.endswith(".reg")]
                for reg_file in reg_files:
                    full_path = os.path.join(backup_path, reg_file)
                    subprocess.run(["reg", "import", full_path], check=True)
            else:
                # Single file backup
                subprocess.run(["reg", "import", backup_path], check=True)

            messagebox.showinfo("Успех", "Бэкап успешно импортирован")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось импортировать бэкап: {str(e)}")


def update_backup_list(backup_list):
    """Обновляет список бэкапов в интерфейсе"""
    if not backup_list:
        return

    # Очищаем список перед обновлением
    backup_list.delete(0, tk.END)

    # Проверяем наличие директории с бэкапами
    backup_dir = os.path.join(os.getcwd(), "Backup")
    if not os.path.exists(backup_dir):
        return

    # Получаем список всех элементов в директории
    try:
        items = os.listdir(backup_dir)
    except Exception as e:
        print(f"Ошибка при чтении директории бэкапов: {e}")
        return

    # Разделяем директории и файлы
    dir_backups = [
        d
        for d in items
        if os.path.isdir(os.path.join(backup_dir, d))
        and d.startswith("RegistryBackup_")
    ]

    file_backups = [
        f
        for f in items
        if os.path.isfile(os.path.join(backup_dir, f))
        and f.startswith("FullRegistryBackup_")
    ]

    # Сортируем оба списка
    dir_backups.sort(reverse=True)
    file_backups.sort(reverse=True)

    # Добавляем сначала директории
    for backup in dir_backups:
        backup_list.insert(tk.END, backup)

    # Затем добавляем файлы
    for backup in file_backups:
        backup_list.insert(tk.END, backup)


# Привязываем обработчик к событию смены вкладки
tab_control.bind("<<NotebookTabChanged>>", on_tab_changed)

# Получаем функцию для начальной вкладки
initial_tab_func = globals().get(
    config.get("General", "initial_tab", fallback="switch_to_main")
)
if initial_tab_func:
    # Проверяем, требует ли функция аргумент tab_control
    import inspect

    if len(inspect.signature(initial_tab_func).parameters) == 1:
        initial_tab_func(tab_control)
    else:
        initial_tab_func()

# Вызываем функцию для установки начального стиля компонентов интерфейса
update_font_style()

# Список темных тем
dark_themes = [
    "cyberpunk",
    "hacker",
    "palenight",
    "darklysuperhero",
    "solar",
    "cyborg",
    "vapor",
]

# Если тема темная, то настраиваем стиль для иконок
# if current_theme in dark_themes:
#     # настраиваем стиль для иконок
#     style.configure('Icon.TButton',
#                     background='#1a1a1a',
#                     foreground='white')
update_button_style()

# def reload_program(event=None):
#     root.destroy()
#     import sys
#     import subprocess
#     subprocess.run([sys.executable] + sys.argv)

# if config["General"].getboolean("ad_enabled", True):
#     open_random_site(10)

# при нажатии кнопки F5, вызываем функцию reload_program
root.bind("<F5>", reload_program)

# Запуск главного цикла приложения для отображения окна
logger.log_program_start()  # Логируем запуск программы
root.mainloop()  # Запускаем главный цикл обработки событий, чтобы интерфейс оставался открытым
logger.log_program_exit()  # Логируем завершение программы
root.mainloop()  # Запускаем главный цикл обработки событий, чтобы интерфейс оставался открытым
logger.log_program_exit()  # Логируем завершение программы
update_button_style()