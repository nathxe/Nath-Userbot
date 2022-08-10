#==============×==============#
#      Created by: Alfa-Ex
#=========× Ayiin ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b nath-Userbot https://github.com/nathxe/Nath-Userbot /home/nathuserbot/ \
    && chmod 777 /home/alxeluserbot \
    && mkdir /home/nathuserbot/bin/

COPY ./sample_config.env ./config.env* /home/nathuserbot/

WORKDIR /home/nathuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
