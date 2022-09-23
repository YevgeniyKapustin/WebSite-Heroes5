### Сайт по героям 5

https://kapusta.eu.pythonanywhere.com

Сайт собирает статистику отправляемую пользователями в форме отчёта об игре.
После отправки сведений об игре проводится расчёт статистики и ее обновление,
которое можно увидеть на главной странице.

Так же у сайта есть API написанное с помощью DjangoRestFramework, которое
позволяет получить данные статистики, ее получение реализовано в другом
моем проекте - https://github.com/Kapusta-fairy/VKBot-Vanessa

### APi
Получение статистики игроков:
https://kapusta.eu.pythonanywhere.com/api/players_stats
Получение статистики фракций:
https://kapusta.eu.pythonanywhere.com/api/fractions_stats
