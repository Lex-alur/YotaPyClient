# Это не я тупой или код странно написан, это для тех, кто захочет переписать...
def help_mode():
    sep, lsep, head, rsep = help_beautifer()
    print(sep+
          "\n"+lsep+" "+head+" "+rsep+
          "\n"+sep+
          "\n"
          "\nОписание:"
          "\n  Достаточно удобный, на взгляд автора, python3 консольный клиент"
          "\n  для управления настройками вашего модема Yota."
          "\n"
          "\nАвторы:"
          "\n  Основано на коде Виктора Шамакова: 'github.com/ReminoR/yota-change-speed'"
          "\n  Автор: @lex_alur (VK|INST|TG)"
          "\n"
          "\n"+sep+
          "\n"
          "\nИспользование:"
          "\n  python yota.py /go   [/log_off] [/head_off]"
          "\n"
          "\n  python yota.py       [/get [tarif/days]] [/set <tarif>] [/up] [/down]"
          "\n                       [/account <login/email/bank_account/phone> <password>]"
          "\n                       [/setup [/account <login//emailbank_account/phone> <password>]]"
          "\n                       [/device <number>] [/get_devices] [/get_tariffs]"
          "\n                       [/return] [/debug] [/log_off] [/head_off] [/requirements]"
          "\n"
          "\nПредупреждения:"
          "\n  Неизвестные аргументы запуска - скрипт игнорирует."
          "\n  При не правильном написании известных аргументов - кидает ошибку и возвращает '0'."
          "\n"
          "\n"+sep+
          "\n"
          "\nДоступные аргументы:"
          "\n  /go                  Функция автопродления бесплатного доступа."
          "\n                         !Находится в разработке! "
          "\n                         Нажимает продолжить на странице-заглушке, которая всплывает"
          "\n                           на бесплатном режиме по несколько раз в день."
          "\n                         Сложно проверять, буду рад фидбеку от любого, кто это читает."
          '\n                         Прописана "в приоритете", потому, при запуске скрипта с этим'
          '\n                           аргументом, происходит обход основного кода после проверки'
          '\n                           всех переданных аргументов, таким образом данная функция'
          '\n                           не должна сильно грузить систему. В задумке - запускать'
          '\n                           скрипт с этой функцией каждые 10/30 минут.'
          "\n                         Для ускорения работы советуется использовать"
          "\n                           с аргументом '/log_off."
          "\n                         Возвращает: [1/0/error_response/(error_type, error_log)]"
          "\n"
          "\n  /get [tarif/days]    Получить текущие условия подключения."
          "\n  /g [tarif/days]        По умолчанию выводит и возвращает тариф и количество дней."
          "\n                         tarif - Выводит и возвращает только тариф."
          "\n                         days - Выводит и возвращает только оставшееся количество дней."
          "\n                         Возвращает: [(tarif, days)/tarif/days]"
          "\n"
          "\n  /set <tarif>         Сменить тариф на заданный."
          "\n  /s <tarif>             Доступные тарифы можно узнать командой '/get_tariffs'."
          "\n                         Возвращает: [1/0]"
          "\n"
          "\n  /up                  Поднимает скорость."
          "\n  /u                     В случае, если у вас уже установлена максимальная скорость"
          "\n                           - кидает ошибку и возвращает '0'."
          "\n                         Возвращает: [1/0]"
          "\n"
          "\n  /down                Опускает скорость на минимальную оплачиваемую."
          "\n  /d                     В случае, если у вас уже установлена минимальная оплачиваемая"
          "\n                           - кидает ошибку и возвращает '0'."
          "\n                         В случае, если у вас уже установленна бесплатная"
          "\n                           - кидает ошибку и возвращает '0'."
          "\n                         Возвращает: [1/0]"
          "\n"
          "\n  /account <login/email/bank_account/phone> <password>"
          "\n  /acc <l> <p>         Позволяет использовать скрипт без файла конфигурации."
          "\n                         Также ускоряет создание файла конфигурации командой '/setup'."
          "\n                         login - логин, по которому можно войти в аккаунт."
          "\n                         email - почта, подключенная к аккаунту."
          "\n                         bank_account - номер лицевого счета."
          "\n                         phone - номер телефона, привязанный к аккаунту."
          "\n                           В формате +78005553535"
          "\n"
          "\n  /setup [/account <login/email/bank_account/phone> <password>]"
          "\n                       Вызов мастера настройки, создает файл конфигурации" 
          "\n                       в директрории скрипта."
          "\n                         Можно вызвать совместно с командой '/account'."
          "\n                         Возвращает: [1/0]"
          "\n"
          "\n  /device <number>     Команда выбора устройства для конфигурации."
          "\n  /de <number>           По умолчанию выбрано первое устройство."
          "\n                         Список доступных устройств можно узнать командой '/get_devices'."
          "\n"
          "\n  /get_devices         Выводит список доступных устройств."
          "\n  /gd                    Возвращает: Список доступных устройств."          
          "\n"
          "\n  /get_tariffs [/device <number>]"
          "\n  /gt                  Выводит список доступных тарифов для устройства."
          "\n                         По умолчанию выбрано первое устройство."
          "\n                         Возвращает: Список доступных тарифов." 
          "\n  /return              Включает возврат значений при выполнении скрипта."
          "\n  /r"          
          "\n"
          "\n  /debug               Активирует дебаг режим, тем самым отключая защиту от ошибок."
          "\n  /db                    Также в данном режиме команда '/set' не выполняет смены тарифа."
          "\n"
          "\n  /log_off             Отключает весь вывод в консоль, но, при выполнении,"
          "\n  /lo                  скрипт продолжает возвращать определенные значения,"
          "\n                       если использовался аргумент '/return'."
          "\n"
          "\n  /head_off            Отключает вывод шапки с названием и разделителя при завершении."
          "\n  /ho"
          "\n"
          "\n  /requirements        Выводит зависимости скрипта."
          "\n"
          "\n  /?                   Пожалуй, в обьяснении не нуждается..."
          "\n  /h"
          "\n  /help"
          "\n  -h"
          "\n  -help"
          "\n  --h"
          "\n  --help"
          "\n"
          "\n"+sep)
def log(status, price="0", days="0"):
    if (log_off == 0):
        '''
        Привет, я не знаю зачем я это делаю, но мне нравится,
        что бы перед каждым обращением софта к юзеру - выводилось определенное значение, 
        которое содержало бы какую-либо внутреннюю логику...
        Потому вот:
            [E] - Error
            [D] - Debug
            [S] - Success/System
            [L] - Loading
            [C] - Creating
            [A] - Логи получения доступа - Accessing
        
        Если, вдруг, вам не нравится мой стиль логгирования - я заранее позаботился, и вынес
        все логи в список ниже. Потому вы можете просто переписать все, что душе угодно)  
        
        '''

        if status == "title" and head_off == 0:
            return print(title())
        elif status == "exit" and head_off == 0:
            return print("\n" + help_beautifer()[0])

        elif status == "blocking_check":
            print("[A] Проверка блокировки...")
        elif status == "blocking_not_found":
            print("[A] Блокировка отсутствует.")
        elif status == "blocking_founded":
            print("[A] Блокировка обнаружена! Снятие...")
        elif status == "blocking_removed":
            print("[A] Блокировка снята!")
        elif status == "blocking_error":
            print("[A] Произошла ошибка!")


        elif status == "error":
            print('[E] Произошла неведомая ошибка, досвиданья)\n[E] (Можете запустить скрипт с аргументом "/debug", что бы выявить причину)')
        elif status == "arg_error":
            print("[E] Переданы не правильные аргументы!\n[E] Перезапустите скрипт, убедившись в правильности написания.")
        elif status == "data_error":
            print("[E] Ошибка! Проблемы с конфигурационным файлом."
                  "\n[E]      Убедитесь в его целостности."
                  "\n[E]       или"
                  "\n[E]      Выполните повторную настройку через аргумент запуска '/setup'."
                  "\n[E]       или"
                  "\n[E]      Запускайте скрипт с аргументом '/account'.")
        elif status == "change_tarif_error":
            print("[E] Переход устройства '" + device_name() + "' на тариф за " + str(price) + ' рублей - не был произведен!')
        elif status == "tariff_max":
            print("[E] На устройстве '" + device_name() + "' уже установлен максимальный тариф!")
        elif status == "tariff_min_paid":
            print("[E] На устройстве '" + device_name() + "' уже установлен минимальный платный тариф!")
        elif status == "tariff_min":
            print("[E] На устройстве '" + device_name() + "' уже установлен бесплатный тариф!")

        elif status == "change_tarif_pass":
            print("[D] Переход устройства '" + device_name() + "' на тариф за " + str(price) + ' рублей - пропущен.')
        elif status == "debug_start":
            print("[D] Запущен debug режим.")

        elif status == "change_tarif_succes":
            print("[S] Переход устройства '" + device_name() + "' на тариф за " + str(price) + ' рублей - прошел успешно!')
        elif status == "get_all_stat":
            print("[S] На устройстве '" + device_name() + "' активен тариф за " + str(price) + ' рублей, осталось ' + str(days) + '.')
        elif status == "get_all_stat_noprice":
            print("[S] На устройстве '" + device_name() + "' выбран неизвестный тариф, код: " + str(
                price) + ', зато осталось ' + str(days) + '.')
        elif status == "get_days":
            print('[S] Осталось ' + str(days) + '.')
        elif status == "get_price":
            print("[S] На устройстве '" + device_name() + "' активен тариф за " + str(price) + " рублей.")
        elif status == "get_price_error":
            print("[S] На устройстве '" + device_name() + "' выбран неизвестный тариф, код: " + str(price))
        elif status == "config_file_created":
            print("[S] Конфигурационный файл создан!")
        elif status == "get_devices":
            print("[S] Доступные устройства: " + str(price)[1:-1] + ", обращайтесь по номерам.")
        elif status == "get_tariffs":
            print("[S] Доступные для устройства '" + device_name() + "' тарифы: " + str(price)[1:-1] + ".")

        elif status == "setup_wizard":
            print("[L] Мастер настройки запущен...")
        elif status == "getting_bank_account":
            print("[L] Получение номера лицевого счета...")
        elif status == "get_auth_page":
            print('[L] Получение страницы авторизации...')
        elif status == "auth":
            print('[L] Авторизация...')
        elif status == "get_tarif_page":
            print('[L] Получение страницы с тарифами...')

        elif status == "tariffs_received":
            print("[C] Тарифы получены...")
        elif status == "create_config_file":
            print("[C] Создание внутреннего конфига...")
        elif status == "device_recording":
            print("[C] Запись устройств во внутренний конфиг...")
        elif status == "tariff_recording":
            print("[C] Запись тарифов во внутренний конфиг...")
        elif status == "saving_config_file":
            print("[C] Сохранение внутреннего конфига в конфигурационного файла...")

# Блок глобальных переменных, задаются из аргументов, позже с ними взаимодействует весь код
# =========================================================================================
# Переменная версии скрипта
src_ver = '1.3'

# Переменная раннего прерывания
interrupt = 0

# Переменные режимов
log_off = 0
head_off = 0
debug = 0
get_mode = 0
get_price_mode = 0
get_days_mode = 0
set_mode = 0
price = 0
setup = 0
account = 0
get_devices_mode = 0
get_tariffs_mode = 0
return_mode = 0
speed_up_mode = 0
speed_down_mode = 0

# Переменная устройства по умолчанию
device = 1

# Переменные для хранения пользовательских данных
auth_data = {}
login = 0
password = 0
# =========================================================================================

from requests import Session, get
from bs4 import BeautifulSoup
from json import loads, load, dumps
from sys import argv
from os import chdir
from os.path import dirname, abspath
from re import findall

# Нужно для запуска не из папки со скриптом
# (сменяет рабочую директорию на директорию скрипта, для нормального взаимодействия с конфигом)
chdir(dirname(abspath(__file__)))

# Инициализация веб клиента
session = Session()
headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
domain = 'https://my.yota.ru'
url_tariff_page = 'https://my.yota.ru/selfcare/devices'
access_page = 'http://hello.yota.ru/light/'

# Функция авто-продления бесплатного периода
def yota_get_acces():
    log('blocking_check')
    try:
        r = get(access_page, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        form = soup.find(id="activate-form")
        log('blocking_founded')

        try:
            url_get_access = access_page + form.get('action')
            access_data = {
                'accept_lte': form.select('input[name="accept_lte"]')[0].get('value'),
                'redirurl': form.select('input[name="redirurl"]')[0].get('value'),
                'city': form.select('input[name="city"]')[0].get('value'),
                'connection_type': form.select('input[name="connection_type"]')[0].get('value'),
                'service_id': form.select('input[name="service_id"]')[0].get('value'),
            }

            access = session.post(url_get_access, access_data, headers=headers)

            if (str(access) == "<Response [200]>"):
                log('blocking_removed')
                if log_off: print(1)
                return 1
            else:
                log('blocking_error')
                if log_off: print(access.text)
                return access.text
        except Exception as e:
            log('blocking_error')
            if log_off: print(e.__class__, e.data)
            return e.__class__, e.data
    except Exception:
        log('blocking_not_found')
        if log_off: print(0)
        return 0

# Функция основного сценария
def main():
    log("title")

    auth_url = get_auth_page()
    if account:
        auth(auth_url, login, password)
    else: auth(auth_url, auth_data['login'], auth_data['password'])
    tarif_page = get_tarif_page()

    if account:
        globals()['auth_data'] = get_account_config(tarif_page)

        if get_devices_mode: return get_devices()

    if set_mode:
        tarif = change_tarif(tarif_page, price)

        if (str(tarif) == "0"):
            return 0
        elif get_mode: return get_tarif(tarif)
        else: return 1
    elif get_mode: return get_tarif(tarif_page)
    elif speed_up_mode or speed_down_mode: return speed_up_down(tarif_page)

# Функции для работы с конфигами
def get_account_config(tarif_page):
    # Получение тарифов
    sliderData = findall('sliderData = {(.*)}', str(tarif_page))[0]
    sliderData = "{" + sliderData + "}"
    sliderData = loads(sliderData)
    log("tariffs_received")

    # Создание конфига без тарифов
    log("create_config_file")
    newdict = dict(login=login, password=password, devices=None)

    # Запись устройств в конфиг
    log("device_recording")
    devices = findall('device-title">\n.*?(\w.*?)\n', str(tarif_page))
    newdict["devices"] = dict.fromkeys(devices)


    # Запись тарифов
    log("tariff_recording")

    for device_num in range(0, len(devices)):
        newdict["devices"][devices[device_num]] = {}
        for tarif in sliderData[list(sliderData.keys())[device_num]]['steps']:
            newdict["devices"][devices[device_num]].setdefault(tarif['amountNumber'], tarif['code'])

    return newdict

def setup_wizard():
    log("title")
    log("setup_wizard")
    global login, password
    if (login == 0 and password == 0):
        login = input("[I] Введите логин/почту/лицевой счет/номер телефона в формате +78005553535: ")
        password = input("[I] Введите пароль: ")

    #Аутентификация
    auth_url = get_auth_page()
    auth(auth_url, login, password)
    tarif_page = get_tarif_page()

    newdict = get_account_config(tarif_page)

    # Сохранение конфигурационного файла
    log("saving_config_file")
    data = dumps(newdict, indent=4)

    f = open('data.json', 'w')
    f.write(data)
    f.close()

    log("config_file_created")
    return 1

# Функции вывода доступных устройств/тарифов
def get_devices():
    devices = list(auth_data['devices'].keys())
    log('get_devices', str(devices))
    return devices

def get_tariffs():
    tariffs = list(auth_data['devices'][list(auth_data['devices'].keys())[device-1]].keys())
    log('get_tariffs', str(tariffs))
    return tariffs

# Функции управления тарифом
def get_tarif(html):
    device_name = list(auth_data['devices'].keys())[int(device)-1]

    price = 0
    days = 0
    pattern = r'="(POS-.*?-\d\d\d\d)(?:.|\s)*?period".*?"(.*?)"(?:.|\s)*?device-title">(?:.|\s)*?(\w.*?)\n'
    for device_conf in findall(pattern, html):
        if(device_conf[2] == device_name):
            price = device_conf[0]
            days = device_conf[1]

    if get_days_mode:
        log("get_days", "0", days)
        return days
    else:
        is_price = False
        for tarif_data in auth_data['devices'][device_name].items():
            if(tarif_data[1] == price):
                price = tarif_data[0]
                is_price = True

        if get_price_mode:
            if is_price: log("get_price", price)
            else: log("get_price_error", price)
            return price
        else:
            if is_price: log("get_all_stat", price, days)
            else: log("get_all_stat_noprice", price, days)
            return price, days

def change_tarif(html, price):
    device_name = list(auth_data['devices'].keys())[int(device)-1]
    tariff = auth_data['devices'][device_name][str(price)]

    pattern = r'<form action=(?:.|\s)*?<\/form>'
    html = findall(pattern, html)

    for device_conf in html:
        if findall(device_name, device_conf):
            html = device_conf

    soup = BeautifulSoup(html, 'html.parser')
    form = soup.find(class_="tariff-choice-form")

    url_change_tarif = domain + form.get('action')
    tarif_data = {
        'product': form.select('input[name="product"]')[0].get('value'),
        'offerCode': tariff,
        'areOffersAvailable': form.select('input[name="offerCode"]')[0].get('value'),
        'period': form.select('input[name="period"]')[0].get('value'),
        'status': form.select('input[name="status"]')[0].get('value'),
        'autoprolong': form.select('input[name="autoprolong"]')[0].get('value'),
        'isSlot': form.select('input[name="isSlot"]')[0].get('value'),
        'finished': form.select('input[name="finished"]')[0].get('value'),
        'blocked': form.select('input[name="blocked"]')[0].get('value'),
        'freeQuotaActive': form.select('input[name="freeQuotaActive"]')[0].get('value'),
        'pimpaPosition': form.select('input[name="pimpaPosition"]')[0].get('value'),
        'specialOffersExpanded': form.select('input[name="resourceId"]')[0].get('value'),
        'resourceId': form.select('input[name="specialOffersExpanded"]')[0].get('value'),
        'currentDevice': form.select('input[name="currentDevice"]')[0].get('value'),
        'username': '',
        'isDisablingAutoprolong': 'false'
    }

    if (debug == 0):
        tarif = session.post(url_change_tarif, tarif_data, headers=headers)

        # <Response [500]> - ошибка
        # <Response [200]> - норм
        if (str(tarif) == "<Response [200]>"):
            log("change_tarif_succes", price)
            return tarif.text
        else:
            log("change_tarif_error", price)
            return 0
    else:
        log("change_tarif_pass", price)
        return html

def speed_up_down(html):
    tariffs = get_tariffs()
    tariff = get_tarif(html)[0]
    # tariff = '900'

    if(speed_up_mode and tariffs.index(tariff) == len(tariffs)-1):
        log("tariff_max")
        return 0
    elif(speed_down_mode and tariffs[tariffs.index(tariff)-1] == "0"):
        log("tariff_min_paid")
        return 0
    elif(speed_down_mode and tariff == "0"):
        log("tariff_min")
        return 0
    else:
        if speed_up_mode: tariff = tariffs[tariffs.index(tariff)+1]
        else: tariff = tariffs[tariffs.index(tariff) - 1]

        if (str(change_tarif(html, tariff)) == "0"): return 0
        else: return 1

# Аутентификация на сайте
def get_auth_page():
    url = 'https://my.yota.ru'
    r = get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    form = soup.find(class_="b-b2c-auth__tab")

    log("get_auth_page")
    action = form.get('action')

    return action

def get_bank(id, type):
    # Получение лиц. счета
    log("getting_bank_account")
    if type == "phone": bank_url = 'https://my.yota.ru/selfcare/login/getUidByPhone'
    elif type == "mail": bank_url = 'https://my.yota.ru/selfcare/login/getUidByMail'
    bank_account = session.post(bank_url, {'value': id}, headers=headers).text[3:]
    return bank_account

def auth(url, login, password):
    if len(findall(r'\+', login)) == 1:
        login = get_bank(login[1:], "phone")
    elif len(findall('@', login)) == 1:
        login = get_bank(login, "mail")
    globals()['login'] = login

    auth_data = {
        'IDToken1': login,
        'IDToken2': password,
        'goto': 'https%3A%2F%2Fmy.yota.ru%3A443%2Fselfcare%2FloginSuccess',
        'gotoOnFail': 'https%3A%2F%2Fmy.yota.ru%3A443%2Fselfcare%2FloginError',
        'org': 'customer',
        'ForceAuth': 'true',
        'login': login,
        'password': password
    }

    log("auth")
    session.post(url, auth_data, headers=headers)

def get_tarif_page():
    log("get_tarif_page")
    r = session.get(url_tariff_page, headers=headers)
    return r.text

# Выводит зависимости
def requirements_setup():
    print(""
          "Не факт, что они реально нужны, но,"
          "\nесли будет ругаться на модули - можете попробовать эти)"
          "\n"
          "\n  beautifulsoup4==4.6.1"
          "\n  bs4==0.0.1"
          "\n  certifi==2018.4.16"
          "\n  chardet==3.0.4"
          "\n  idna==2.7"
          "\n  lxml==4.2.3"
          "\n  requests==2.19.1"
          "\n  urllib3==1.23"
          "")

# Украшалки
def help_beautifer():
    from shutil import get_terminal_size
    columns  = get_terminal_size((80, 20))[0]

    sep = ''
    for n in range(1,columns):
        sep += '='

    head = "YotaPyClient - Version "+src_ver
    lsep = ''
    rsep = ''

    for n in range(1,(columns - len(head) - 2)//2):
        lsep += ']'
        rsep += '['

    for n in range(0,columns-(3+len(head)+len(lsep)*2)):
        rsep += '['

    return sep, lsep, head, rsep

def title():
    sep, lsep, head, rsep = help_beautifer()
    return sep + "\n" + lsep + " " + head + " " + rsep + "\n" + sep + "\n"

def main_exit(code):
    log("exit")
    exit(code)

def device_name():
    return list(auth_data['devices'].keys())[device - 1]

# Функция запуска
if __name__ == "__main__":
    if(len(argv)>1):
        i = 0
        while i < len(argv)-1:
            i += 1
            arg = argv[i]

            try:
                if (arg == "/go" and interrupt != "h"): interrupt = 'a'
                elif (arg == "/?" or arg == "-h" or arg == "--h" or arg == "-help" or arg == "--help" or arg == "/h" or arg == "/help"): interrupt = "h"
                elif (arg == "/requirements" and interrupt != "h" and interrupt != "a"): interrupt = "r"

                elif (arg == "/log_off" or arg == "/lo"): log_off = 1
                elif (arg == "/head_off" or arg == "/ho"): head_off = 1
                elif (arg == "/setup"): setup = 1
                elif (arg == "/return" or arg == "/r"): return_mode = 1
                elif (arg == "/get_devices" or arg == "/gd"): get_devices_mode = 1
                elif (arg == "/get_tariffs" or arg == "/gt"): get_tariffs_mode = 1
                elif (arg == "/up" or arg == "/u"): speed_up_mode = 1
                elif (arg == "/down" or arg == "/d"): speed_down_mode = 1

                elif (arg == "/debug" or arg == "/db"):
                    log("debug_start")
                    debug = 1
                elif (arg == "/account" or arg == "/acc"):
                    i += 1
                    login = argv[i]
                    i += 1
                    password = argv[i]
                    account = 1
                elif (arg == "/device" or arg == "/de"):
                    i += 1
                    device = int(argv[i])
                elif (arg == "/set" or arg == "/s"):
                    i += 1
                    price = argv[i]
                    set_mode = 1
                elif (arg == "/get" or arg == "/g"):
                    get_mode = 1
                    try:
                        if(argv[i+1] == "price" or argv[i+1] == "days"):
                            i += 1
                            if(argv[i] == "price"): get_price_mode = 1
                            elif(argv[i] == "days"): get_days_mode = 1
                    except: pass
            except Exception:
                log("arg_error")
                exit(0)

        if interrupt:
            if interrupt == "a":
                log('title')
                main_exit(yota_get_acces())
            elif interrupt == "h":
                help_mode()
                exit(0)
            else:
                log('title')
                requirements_setup()
                main_exit(0)

        if setup:
            ret = setup_wizard()
            if return_mode: main_exit(ret)
            else: main_exit(1)

        if account == 0:
            try:
                with open("./data.json", "r") as read_file:
                    auth_data = load(read_file)
            except:
                log("data_error")
                main_exit(0)

        if get_devices_mode and account == 0:
            ret = get_devices()
            if return_mode: main_exit(ret)
            else: main_exit(0)
        elif get_tariffs_mode and account == 0:
            ret = get_tariffs()
            if return_mode: main_exit(ret)
            else: main_exit(0)
        elif debug:
            print(main())
        else:
            try:
                ret = main()
                if return_mode: main_exit(ret)
                else:
                    if ret: main_exit(1)
                    else: main_exit(0)
            except Exception:
                log("error")
                main_exit(0)
    else:
        help_mode()