import json

# Укажите путь к файлу JSON с двойными обратными слешами или префиксом `r`
json_file_path = r"C:\Users\artem.venikov\Downloads\Untitled-5.json"


# Чтение JSON из файла
with open(json_file_path, "r") as json_file:
    json_data = json.load(json_file)

# Получаем значения hosts.host и hosts.interfaces.ip
hosts = json_data["zabbix_export"]["hosts"]

for host in hosts:
    host_name = host["host"]
    interfaces = host["interfaces"]
    
    for interface in interfaces:
        ips = [interface["ip"] for interface in interfaces]

    print(f"Host: {host_name}, IP: {ips}")

    # print(f"Host: {host_name}, IP: {ips}")

