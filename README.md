# Дипломный проект: My Cloud

Развернутое приложение - 
<details>
 <summary>Для развертывания локально:</summary>
<details>
<summary>Backend:</summary>

1. -  Переходим в папку, 
2. - Создаем и активируем окружение,    
3. - Ставим зависимости,
4. - Создаем базу данных, с учетом настроек указанных в файле .env
5. - Мигрируем
6. - Создаем суперпользователя согласно файлу .env
`python manage.py create_superuser` 
7. - Запускаем сервер 
`python manage.py runserver`
</details>
<details>
<summary>Frontend:</summary>

1. -   В файле `.env` вместо {url} указываем url полученный в терминале от бэка , 
2. - Устанавливаем зависимости: `npm i`,    
3. - Запускаемся `npm run dev`
</details>
</details>
<details>
    <summary>Для развертывания на сервере</summary>
    
</details>
