import returned_users_for_Akbar_q as q
import os
import smtplib
import sys
import shutil
import pyperclip
import re
from itertools import groupby
import time
from multiprocessing import Pool, Value
from numpy import split

# Добавляем необходимые подклассы - MIME-типы
import mimetypes                                            # Импорт класса для обработки неизвестных MIME-типов, базирующихся на расширении файла
from email import encoders                                  # Импортируем энкодер
from email.mime.base import MIMEBase                        # Общий тип
from email.mime.text import MIMEText                        # Текст/HTML
from email.mime.image import MIMEImage                      # Изображения
from email.mime.audio import MIMEAudio                      # Аудио
from email.mime.multipart import MIMEMultipart              # Многокомпонентный объект

from ets.ets_mysql_lib import MysqlConnection as mc
from ets.ets_excel_creator import Excel

import pandas as pd
from pandas import DataFrame

from datetime import datetime as dt, timedelta as td

import settings_file


def add_quotes(a):
    return f"'{str(a)}'"


def make_line(itr):
    return add_quotes("', '".join(itr))


def get_data_from_db(cnx, query, as_dict=False, **kwargs):
    connect = mc(connection=cnx)
    with connect.open() as c:
        result = c.execute_query(query, dicted=as_dict)
    return result


def get_data_from_db_firm(cnx, query, as_dict=False, **kwargs):
    connect = mc(connection=cnx)
    with connect.open() as c:
        result = c.execute_query(query.format(**kwargs), dicted=as_dict)
    return result

def get_organization_ids():
    organization_ids_1 = get_data_from_db(mc.MS_FABRIKANT_LOG_1, q.get_ids_in_logs_1, as_dict=True) 
    organization_ids_2 = get_data_from_db(mc.MS_FABRIKANT_LOG_2, q.get_ids_in_logs_2, as_dict=True) 
    organization_ids = organization_ids_1 + organization_ids_2

    if organization_ids:
        organization_ids = [{k: str(v) for d in ids for k, v in d.items()}
                            for _, ids in groupby(sorted(organization_ids, key=lambda x: x['firm_id']), lambda x: x['firm_id'])]
            
        organization_ids = {
            'organization_ids': ','.join([add_quotes(d['firm_id']) for d in organization_ids]),
        }
        
        return organization_ids
    

def get_firm_info(organization_ids):
    query_to_type = {
        'Информация по ID': q.get_firm_info,
    }
        
    for type, query in query_to_type.items():
        yield type, DataFrame(get_data_from_db_firm(mc.MS_FABRIKANT_FIRM, query, as_dict=True, **organization_ids))



def make_report(gen_data, work_dir, task_name):
    excel_file = Excel()
    for type, pd_data in gen_data:
        if pd_data.empty:
            print(f'{type} -')
            continue
        excel_list = excel_file.create_list(type)
        excel_list.write_data_from_iter(
            pd_data.to_records(index=False).tolist(), top_line=pd_data.columns.values.tolist())
        excel_list.set_default_column_width(150)
        print(f'{type} +')

    os.chdir(work_dir)
    file_name = excel_file.save_file('.', file_name=f'{str(task_name)}')
    print(f'\nСоздан файл {file_name}')


def process_attachement(msg, files):                        # Функция по обработке списка, добавляемых к сообщению файлов
    for f in files:
        if os.path.isfile(f):                               # Если файл существует
            attach_file(msg,f)                              # Добавляем файл к сообщению
        elif os.path.exists(f):                             # Если путь не файл и существует, значит - папка
            dir = os.listdir(f)                             # Получаем список файлов в папке
            for file in dir:                                # Перебираем все файлы и...
                attach_file(msg,f+"/"+file)                 # ...добавляем каждый файл к сообщению

def attach_file(msg, filepath):                             # Функция по добавлению конкретного файла к сообщению
    filename = os.path.basename(filepath)                   # Получаем только имя файла
    ctype, encoding = mimetypes.guess_type(filepath)        # Определяем тип файла на основе его расширения
    if ctype is None or encoding is not None:               # Если тип файла не определяется
        ctype = 'application/octet-stream'                  # Будем использовать общий тип
    maintype, subtype = ctype.split('/', 1)                 # Получаем тип и подтип
    if maintype == 'text':                                  # Если текстовый файл
        with open(filepath) as fp:                          # Открываем файл для чтения
            file = MIMEText(fp.read(), _subtype=subtype)    # Используем тип MIMEText
            fp.close()                                      # После использования файл обязательно нужно закрыть
    elif maintype == 'image':                               # Если изображение
        with open(filepath, 'rb') as fp:
            file = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
    elif maintype == 'audio':                               # Если аудио
        with open(filepath, 'rb') as fp:
            file = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
    else:                                                   # Неизвестный тип файла
        with open(filepath, 'rb') as fp:
            file = MIMEBase(maintype, subtype)              # Используем общий MIME-тип
            file.set_payload(fp.read())                     # Добавляем содержимое общего типа (полезную нагрузку)
            fp.close()
            encoders.encode_base64(file)                    # Содержимое должно кодироваться как Base64
    file.add_header('Content-Disposition', 'attachment', filename=filename) # Добавляем заголовки
    msg.attach(file)                                        # Присоединяем файл к сообщению  


def main():
    WORK_DIR = r"C:/Users/e.golikov/Отчёт для Акбара"
    os.chdir(WORK_DIR)
    participant_ids = get_organization_ids()

    gen_data = get_firm_info(participant_ids)
    task_name = "Отчёт_по_организациям"
    make_report(gen_data, WORK_DIR, task_name)

    # addr_from Адресат
    # addr_to Получатель
    # password Пароль
    msg = MIMEMultipart()                                # Создаем сообщение
    msg['From'] = addr_from                              # Адресат
    msg['To'] = addr_to                                  # Получатель
    msg['Subject'] = 'Отчёт по организациям'             # Тема сообщения
    body = "В приложении находится отчёт по организациям."    # Текст сообщения
    msg.attach(MIMEText(body, 'plain'))                  # Добавляем в сообщение текст
    process_attachement(msg, files)
    server = smtplib.SMTP('mail.fabrikant.ru', 587)      # Создаем объект SMTP
    server.starttls()                                    # Начинаем шифрованный обмен по TLS
    server.login(addr_from, password)                    # Получаем доступ
    server.send_message(msg)                             # Отправляем сообщение
    server.quit()                                        # Выходим

files = ["C:/Users/e.golikov/Отчёт для Акбара/Отчёт_по_организациям.xls"]  # Список файлов, если вложений нет, то files=[]

if __name__ == '__main__':
    main()