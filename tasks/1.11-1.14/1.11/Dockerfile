FROM amazoncorretto:17-alpine

WORKDIR /app

COPY spring-example-project .

RUN ./mvnw package

CMD ["java", "-jar", "./target/docker-example-1.1.3.jar"]
