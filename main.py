import subprocess
from typing import List, Union

class WiFiScanner:
    @classmethod
    # Выполняет команду и возвращает результат в виде списка
    def execute_command(cls, command: List[str]) -> List[str]:
        try:
            # Выполняет команду и декодирует результат
            result = subprocess.check_output(command).decode("UTF-8", errors="backslashreplace")
            return result.split('\n')
        except subprocess.CalledProcessError as e:
            # Логирование ошибки и возврат пустого списка при возникновении ошибки
            print(f"Ошибка выполнения команды: {e}")
            return []

    @classmethod
    # Получает список всех профилей WiFi
    def get_wifi_profiles(cls) -> List[str]:
        command = ["netsh", "wlan", "show", "profiles"]
        output = cls.execute_command(command)

        # Извлекает имена профилей из вывода команды
        profiles = [
            line.split(":")[1].strip()
            for line in output
            if "All User Profile" in line
        ]

        return profiles

    @classmethod
    # Получает информацию о профиле WiFi, включая пароль
    def get_profile_info(cls, profile: str) -> str:
        command = ["netsh", "wlan", "show", "profile", profile, "key=clear"]
        output = cls.execute_command(command)

        # Извлекает пароль из вывода команды
        password_info = [
            line.split(":")[1].strip()
            for line in output
            if "Key Content" in line
        ]

        # Форматирует вывод с именем профиля и паролем, если он есть
        return "{:<30}|  {:<}".format(profile, password_info[0] if password_info else "Пароль не найден")

    @classmethod
    # Выводит информацию о каждом профиле WiFi в консоль
    def display_profiles(cls) -> None:
        profiles = cls.get_wifi_profiles()

        if not profiles:
            print("Профили WiFi не найдены или служба недоступна.")
            return

        print("{:<30}|  {:<}".format("SSID", "Пароль"))
        print("-" * 50)

        # Проходит по каждому профилю и выводит информацию
        for profile in profiles:
            print(cls.get_profile_info(profile))

def run():
    wifi_scanner = WiFiScanner()
    wifi_scanner.display_profiles()

if __name__ == "__main__":
    run()
