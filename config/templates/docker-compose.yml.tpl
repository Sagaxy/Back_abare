services:
  postgres:
    image: postgres:13
    container_name: (PROJECT_NAME)-db-c
    volumes:
      - postgres-(PROJECT_NAME)-data:/var/lib/postgresql/data
    networks:
      - (PROJECT_NAME)-network
    ports:
      - "(DB_PORT):5432"
    environment:
      POSTGRES_USER: (DB_USER)
      POSTGRES_PASSWORD: (DB_PASSWORD)
      POSTGRES_DB: (DB_NAME)
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 4G
    restart: always

  api:
    build: 
      context: .
      dockerfile: Dockerfile
    container_name: (PROJECT_NAME)-api-c
    volumes:
      - ./src/logs/history:/app/logs/history
    networks:
      - (PROJECT_NAME)-network
    ports:
      - "(PORT):(PORT)"

networks:
  (PROJECT_NAME)-network:
    name: (PROJECT_NAME)-network
    driver: bridge

volumes:
  postgres-(PROJECT_NAME)-data: