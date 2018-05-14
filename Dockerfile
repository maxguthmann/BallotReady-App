FROM python:3.4-alpine
ADD . /code
WORKDIR /code
RUN apk update && \
 apk add postgresql-libs && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r flask.txt --no-cache-dir && \
 apk --purge del .build-deps
CMD ["python","application.py"]