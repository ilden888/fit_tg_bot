#  Fit TG Bot

**Fit TG Bot** — это Telegram-бот для фитнес-тренера Ольги Илющихиной, написанный на Python. Проект помогает автоматизировать взаимодействие с клиентами и ведение тренировочного процесса.

##  Возможности

*    **Управление тренировками**: Получение и отслеживание планов тренировок.
*    **Питание**: Рекомендации или расчет КБЖУ.
*    **Уведомления**: Напоминания о занятиях.
*    **Обратная связь**: Прямая связь с тренером.

##  Технологический стек

*   **Язык**: Python 3.x
*   **Telegram API**: `pyTelegramBotAPI` (Telebot)
*   **Конфигурация**: `python-dotenv`

##  Установка и запуск

1.  **Клонируйте репозиторий**
    ```bash
    git clone https://github.com/username/fit_tg_bot.git
    cd fit_tg_bot
    ```

2.  **Создайте виртуальное окружение**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/macOS
    source venv/bin/activate
    ```

3.  **Установите зависимости**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Настройка**
    Создайте файл `.env` на основе `.env.example` и добавьте туда токен бота:
    ```bash
    cp .env.example .env
    ```

5.  **Запуск**
    ```bash
    python fit_bot.py
    ```
