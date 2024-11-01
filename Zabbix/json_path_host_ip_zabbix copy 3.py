## ## парсим JSON zabbix export хостов

import json
import pandas as pd
# Укажите путь к файлу JSON с двойными обратными слешами или префиксом `r`
json_file_path = r"C:\Users\Downloads\Untitled-5.json"


# Чтение JSON из файла
with open(json_file_path, "r") as json_file:
    json_data = json.load(json_file)

# Получаем значения hosts.host и hosts.interfaces.ip
hosts = json_data["zabbix_export"]["hosts"]
# Создаем список для хранения данных
rows = []
for host in hosts:
    host_name = host["host"]
    groups_name = [groups['name'] for groups in host.get('groups', [])]
    templates = [template['name'] for template in host.get('templates', [])]
    #interfaces = host["interfaces"]

    # Списки для хранения всех IP и типов интерфейсов
    interfaces_ips = []
    interfaces_types = []
    if 'interfaces' in host and len(host['interfaces']) > 0:
            for interface in host['interfaces']:
                interfaces_ips.append(interface.get('ip', 'N/A'))
                interfaces_types.append(interface.get('type', 'N/A'))
                
                # Если IP отсутствует, указываем 'N/A'
                # Здесь можно добавить дополнительную логику для типа интерфейса,
                # если у вас есть информация о доступных типах интерфейсов.

    #ЗАМЕНА N/A на AGENT
    # if 'interfaces' in host and len(host['interfaces']) > 0:
    #         for interface in host['interfaces']:
    #             ip_address=(interface.get('ip', 'N/A'))
    #             interface_type = (interface.get('type', 'N/A'))

    #             interfaces_ips.append(ip_address)
            
    #             # Проверка на наличие типа
    #             if interface_type == 'N/A' and ip_address != 'N/A':
    #                 interfaces_types.append('AGENT')
    #             else:
    #                 interfaces_types.append(interface_type)

    # Преобразуем списки в строки
    interfaces_ip = ', '.join(interfaces_ips) if interfaces_ips else 'N/A'
    interfaces_type = ', '.join(interfaces_types) if interfaces_types else 'N/A'
    groups_name_str = ', '.join(groups_name) if groups_name else 'N/A'
    # Формируем строку
    rows.append({
        'host_name': host_name,
        'interfaces_ip': interfaces_ip,
        'interfaces_type': interfaces_type,
        'groups_name': groups_name_str,
        'templates': ', '.join(templates)
    })
# Создаем DataFrame и сохраняем в Excel
    df = pd.DataFrame(rows)
    df.to_excel('hosts_data.xlsx', index=False)
    #print(f"Host: {host_name}, Groups: {groups_name}, IP: {interfaces_ip}, TYPE1:{interfaces_type}, templates: {templates}")
print("Данные успешно сохранены в hosts_data.xlsx")
    # print(f"Host: {host_name}, IP: {ips}")

