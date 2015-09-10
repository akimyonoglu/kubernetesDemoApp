FROM alpine

RUN apk add --update python && rm -rf /var/cache/apk/*

WORKDIR /src
ADD ./src .

CMD ["python", "-m", "SimpleHTTPServer", "8082"]
