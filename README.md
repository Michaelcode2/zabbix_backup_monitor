# zabbix_backup_monitor
Backup minitoring with zabbix

Скрипт дозволяє автоматизувати моніторинг бекапів за допомогою Zabbix.
скрипт аналізує вміст директорії на наявність бекапів та передає на Zabbix сервер інформацію.

Вміст директорії "zabbix" розміщується у каталозі /etc/zabbix сервера з агентом zabbix

файл count.txt розміщується у директорії бекапів бази даних.
Параметр ArchivePeriod=3 вказує на період архівації у днях.
Запобігає зпрацюванню аларми Zabbix якщо період архівації більше 1 дня.

**На агенті zabbix-agent додаємо інформацію про бэкапи**

Додаємо ітеми в агент zabbix через UserParameter.
Створюємо файл /etc//zabbix//zabbix_agentd.d/backup_info.conf наступного вмісту:
.UserParameter=backup.discovery[*],//etc/zabbix/scripts/backup-discovery.sh
UserParameter=backup.size[*],//etc/zabbix/scripts/analize-size.sh $1
UserParameter=backup.time[*],//etc/zabbix/scripts/analize-time.sh $1

Перезапускаємо агента і перевіряємо. Для початку автоматичне виявлення папок.
#  zabbix_agentd -t backup.discovery
У виводі побачимо список папок в json форматі, як при ручному запуску скрипта. Далі перевіримо вивод інформації про самі бекапи.
#  zabbix_agentd -t backup.size[dedic-nodes-BCH-01]
backup.size[dedic-nodes-BCH-01] [t|496211]
#  zabbix_agentd -t backup.time[dedic-nodes-BCH-01]
backup.time[dedic-nodes-BCH-01] [t|81]

Якщо отримаємо актуальну інформацію, значить все ОК. Можемо переходити на zabbix-server.

**На сервері ZABBIX**

На сервері Zabbix додаємо шаблон моніторинга
zbx_export_templates.xml

Додаються 2 трігери.
- Просрочений бекап
- Бекап нульового розміру
