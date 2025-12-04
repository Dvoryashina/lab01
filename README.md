<div align="center">

# Лабораторная работа №1

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com)
[![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)](https://www.markdownguide.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)

</div>

## Салют :wave:

Данная лабораторная работа посвящена изучению систем обмена данными и основам работы с Git и GitHub.

## Описание

В рамках лабораторной работы изучаются базовые навыки работы с системой контроля версий Git:
- Инициализация репозитория
- Создание коммитов с GPG подписью
- Работа с удалённым репозиторием
- Создание веток и pull requests
- Разрешение конфликтов через rebase и merge

## Технологический стек

- **Python** - язык программирования
- **Typer** - фреймворк для создания CLI приложений
- **Git** - система контроля версий
- **GitHub CLI (gh)** - инструмент для работы с GitHub
- **GnuPG** - инструмент для цифровой подписи коммитов

## Структура проекта

```
lab01/
├── .gitignore          # Правила игнорирования файлов
├── LICENSE             # Лицензия MIT
├── CODE_OF_CONDUCT.md  # Кодекс поведения
├── CONTRIBUTING.md     # Руководство для контрибьюторов
├── SECURITY.md         # Политика безопасности
├── NOTICE.md           # Уведомления о зависимостях
├── README.md           # Документация проекта
└── typersteel.py       # CLI приложение на базе Typer
```

## Использование

### Установка зависимостей

```bash
pip install typer
```

### Запуск приложения

```bash
# Простое приветствие
python typersteel.py "Ирина"

# Формальное приветствие с фамилией
python typersteel.py "Ирина" --lastname "Дворяшина" --formal
```

## Выполненные задачи

- [x] Регистрация на GitHub
- [x] Генерация SSH-ключа и добавление в GitHub
- [x] Создание Personal Token с правами "gist"
- [x] Генерация GnuPG ключа для подписания коммитов
- [x] Настройка глобальных переменных окружения Git
- [x] Установка и авторизация в GitHub CLI
- [x] Создание `.gitignore`
- [x] Реализация CLI приложения `typersteel.py`
- [x] Оформление README.md
- [x] Работа с ветками (patch1, patch2)
- [x] Создание и слияние Pull Requests
- [x] Публикация gist отчета

## Конфигурация Git

```bash
# Глобальные настройки пользователя
git config --global user.name "Irina Dvoryashina"
git config --global user.email "7gsc9zrnyv@privaterelay.appleid.com"

# Настройка GPG подписи
git config --global user.signingkey "47D4A84867BD8F8E"
git config --global commit.gpgsign true
```

## Цифровая подпись коммитов

### GnuPG vs S/MIME

В данном проекте используется **GnuPG (GPG)** для подписи коммитов. Существует альтернатива - **S/MIME** через инструмент `smimesign`.

#### GnuPG (используется в проекте)
- **Преимущества:**
  - Открытый стандарт, широко используемый в сообществе разработчиков
  - Нативная поддержка в Git
  - Децентрализованная модель доверия (Web of Trust)
  - Бесплатные самоподписанные сертификаты

- **Недостатки:**
  - Более сложная настройка для новичков
  - Требует управления ключами вручную

#### S/MIME (smimesign)
- **Преимущества:**
  - Использует X.509 сертификаты (как HTTPS)
  - Интеграция с корпоративными PKI инфраструктурами
  - Автоматическая верификация через цепочку сертификатов
  - Удобно для организаций с существующей PKI

- **Недостатки:**
  - Требует приобретения или выпуска сертификата от CA
  - Менее распространён в open-source сообществе
  - Зависимость от центров сертификации

**Вывод:** Для учебных и open-source проектов GnuPG является предпочтительным выбором благодаря простоте получения ключей и широкой поддержке сообщества.

### Проверка подписи коммитов

```bash
# Просмотр последнего коммита с проверкой подписи
git log --show-signature -1

# Проверка всех коммитов
git log --show-signature

# Просмотр информации о GPG ключе
gpg --list-secret-keys --keyid-format=long
```

## История разработки

### Pull Requests
- **PR #1**: [Улучшения кода typersteel.py](https://github.com/Dvoryashina/lab01/pull/1) - добавлена документация и комментарии
- **PR #2**: [Рефакторинг: улучшен стиль кода](https://github.com/Dvoryashina/lab01/pull/2) - улучшена структура и модульность

### Ветки
- `master` - основная ветка с финальным кодом
- `patch1` - ветка с улучшениями документации (merged)
- `patch2` - ветка с рефакторингом кода (merged)

## Ссылки

- **Репозиторий:** https://github.com/Dvoryashina/lab01
- **Gist отчет:** https://gist.github.com/Dvoryashina/9072f567c385a9da63378fac795ccf14

## Автор

**Дворяшина Ирина**

---

<div align="center">

*Лабораторная работа выполнена в рамках курса по анализу рисков*

</div>
