
# EN
**GenWiFiProfileDumper** is a tool designed to extract and display saved WiFi profiles and their passwords on Windows systems. The program utilizes the `netsh` command-line tool to scan for available WiFi profiles and their credentials.


## Features
- Extracts and lists all available WiFi profiles on a Windows machine.
- Retrieves and displays the password for each profile (if available).
- Simple and easy-to-use interface with formatted output.
- Useful for system administrators or network security enthusiasts.


## Requirements
- **Operating System**: Windows
- **Python**: Version 3.6 or higher


## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/geniuszly/GenWiFiProfileDumper
    ```
2. **Navigate to the project directory**:
    ```bash
    cd GenWiFiProfileDumper
    ```
3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```


## Usage
1. Open a terminal and navigate to the project directory
2. Run the script:
    ```bash
    python main.py
    ```
3. The program will list all saved WiFi profiles and their passwords (if available).

> **Note**: You may need to run the script as an administrator to ensure all profiles are accessible.


## Example Output
```
SSID                          |  Пароль
--------------------------------------------------
LanNet-5234                  |  12345672q
WLANOffice                   |  44643yghre3t3
```

---

## Troubleshooting
- **No Profiles Found**: Ensure the `WLAN AutoConfig` service is running.
- **Permission Denied**: Run the script with administrator privileges.


# RU
**GenWiFiProfileDumper** — это инструмент, предназначенный для извлечения и отображения сохраненных профилей WiFi и их паролей на системах Windows. Программа использует командную утилиту `netsh` для сканирования доступных WiFi профилей и их данных.



## Функции
- Извлекает и перечисляет все доступные профили WiFi на Windows.
- Получает и отображает пароль для каждого профиля (если он доступен).
- Простой и удобный интерфейс с форматированным выводом.
- Полезно для системных администраторов или специалистов по сетевой безопасности.


## Требования
- **Операционная система**: Windows
- **Python**: Версия 3.6 или выше


## Установка
1. **Клонируйте репозиторий**:
    ```bash
    git clone https://github.com/geniuszly/GenWiFiProfileDumper
    ```
2. **Перейдите в директорию проекта**:
    ```bash
    cd GenWiFiProfileDumper
    ```
3. **Установите необходимые пакеты**:
    ```bash
    pip install -r requirements.txt
    ```

---

## Использование
1. Откройте терминал и перейдите в директорию проекта
2. Запустите скрипт:
    ```bash
    python main.py
    ```
3. Программа выведет список всех сохраненных профилей WiFi и их паролей (если они доступны).

> **Примечание**: Возможно, вам потребуется запустить скрипт от имени администратора для доступа ко всем профилям.

---

## Пример вывода
```
SSID                          |  Пароль
--------------------------------------------------
LanNet-5234                  |  12345672q
WLANOffice                   |  44643yghre3t3
```

---

## Устранение неполадок
- **Профили не найдены**: Убедитесь, что служба `WLAN AutoConfig` запущена.
- **Отказано в доступе**: Запустите скрипт с правами администратора.

