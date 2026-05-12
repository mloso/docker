---
title: 'Использование не-root пользователя'
---

Давайте вернемся к приложению yt-dlp, с которым мы в последний раз работали в [Части 2](http://localhost:8000/part-2/1-migrating-to-docker-compose#volumes-in-docker-compose).

Приложение могло бы, в теории, сбежать из контейнера из-за ошибки в Docker или ядре Linux. Чтобы смягчить эту проблему безопасности, мы добавим не-root пользователя в наш контейнер и запустим наш процесс от имени этого пользователя. Другой вариант — сопоставить root пользователя с высоким, несуществующим id пользователя на хосте с помощью https://docs.docker.com/engine/security/userns-remap/, и это можно использовать, если вы должны использовать root внутри контейнера.

Dockerfile, который мы сделали в [Части 1](/part-1/section-4), был таким:

```dockerfile
FROM ubuntu:22.04

WORKDIR /mydir

RUN apt-get update && apt-get install -y curl python3
RUN curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
RUN chmod a+x /usr/local/bin/yt-dlp

ENTRYPOINT ["/usr/local/bin/yt-dlp"]
```

Мы добавим пользователя с именем _appuser_ с помощью следующей команды

```dockerfile
RUN useradd -m appuser
```

После этого мы меняем пользователя с помощью директивы [USER](https://docs.docker.com/engine/reference/builder/#user) — так что все команды после этой строки будут выполняться от имени нашего нового пользователя, включая `CMD` и `ENTRYPOINT`.

```dockerfile
FROM ubuntu:22.04

WORKDIR /mydir

RUN apt-get update && apt-get install -y curl python3
RUN curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
RUN chmod a+x /usr/local/bin/yt-dlp

RUN useradd -m appuser
USER appuser

ENTRYPOINT ["/usr/local/bin/yt-dlp"]
```

`WORKDIR` переименован в /usr/videos, так как это имеет больше смысла, так как видео будут загружаться туда. Когда мы запускаем этот образ без bind mount нашей локальной директории:

```console
$ docker  run yt-dlp https://www.youtube.com/watch?v=XsqlHHTGQrw

... 

[info] XsqlHHTGQrw: Downloading 1 format(s): 22
[download] Unable to open file: [Errno 13] Permission denied: 'Master's Programme in Computer Science | University of Helsinki [XsqlHHTGQrw].mp4.part'. Retrying (1/3)...
[download] Unable to open file: [Errno 13] Permission denied: 'Master's Programme in Computer Science | University of Helsinki [XsqlHHTGQrw].mp4.part'. Retrying (2/3)...
[download] Unable to open file: [Errno 13] Permission denied: 'Master's Programme in Computer Science | University of Helsinki [XsqlHHTGQrw].mp4.part'. Retrying (3/3)...

ERROR: unable to open for writing: [Errno 13] Permission denied: 'Master's Programme in Computer Science | University of Helsinki [XsqlHHTGQrw].mp4.part'
```

Мы видим, что наш пользователь `appuser` не имеет доступа для записи в файловую систему контейнера. Это можно исправить с помощью `chown` или не исправлять вообще, если предполагаемое использование — всегда иметь `/mydir`, смонтированный с хоста. Монтируя директорию, приложение работает как задумано.

Если мы хотим дать пользователю `appuser` разрешение на запись внутри контейнера, изменение разрешения должно быть сделано, пока мы все еще выполняемся как root, то есть перед использованием директивы `USER` для смены пользователя:

```dockerfile
FROM ubuntu:22.04

# ...

WORKDIR /mydir

# create the appuser
RUN useradd -m appuser

# change the owner of current dir to appuser
RUN chown appuser .

# now we can change the user
USER appuser

ENTRYPOINT ["/usr/local/bin/yt-dlp"]
```

## Упражнение 3.5

:::caution Обязательное Упражнение 3.5

  В упражнениях [1.12](/part-1/section-6#exercises-111-114) и [1.13](/part-1/section-6#exercises-111-114) мы создали Dockerfiles для [frontend](https://github.com/docker-hy/material-applications/tree/main/example-frontend) и [backend](https://github.com/docker-hy/material-applications/tree/main/example-backend).

  Проблемы безопасности с пользователем, являющимся root, серьезны для примера frontend и backend, так как контейнеры для веб-сервисов должны быть доступны через Интернет.

  Убедитесь, что контейнеры запускают свои процессы от имени не-root пользователя.

  Образ backend основан на [Alpine Linux](https://www.alpinelinux.org/), который не поддерживает команду `useradd`. Google, несомненно, поможет вам найти способ создать пользователя в образе на основе `alpine`.

  Отправьте Dockerfiles.

:::
