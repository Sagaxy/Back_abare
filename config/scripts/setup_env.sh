echo "Setting up enviroment for $6 project"
echo "---------------------"
echo "Database Info"
echo "> DB USER: $1"
echo "> DB PASSWORD: $2"
echo "> DB HOST: $3"
echo "> DB PORT: $4"
echo "> DB NAME: $5"
echo "---------------------"
echo "Project Info"
echo "> PROJECT NAME: $6"
echo "> MODE: $7"
echo "> PORT: $8"
echo "> VERSION: $9"
echo "---------------------"
echo "CORS Configurations"
echo "> ORIGINS: ${10}"
echo "> CREDENTIALS: ${11}"
echo "> METHODS: ${12}"
echo "> HEADERS: ${13}"
echo "---------------------"

cp config/templates/.env.tpl .env
sed -i "s/(DB_USER)/$1/g" .env
sed -i "s/(DB_PASSWORD)/$2/g" .env
sed -i "s/(DB_HOST)/$3/g" .env
sed -i "s/(DB_PORT)/$4/g" .env
sed -i "s/(DB_NAME)/$5/g" .env
sed -i "s/(PROJECT_NAME)/$6/g" .env
sed -i "s/(MODE)/$7/g" .env
sed -i "s/(PORT)/$8/g" .env
sed -i "s/(VERSION)/$9/g" .env
sed -i "s/(CORS_ALLOW_ORIGINS)/${10}/g" .env
sed -i "s/(CORS_ALLOW_CREDENTIALS)/${11}/g" .env
sed -i "s/(CORS_ALLOW_METHODS)/${12}/g" .env
sed -i "s/(CORS_ALLOW_HEADERS)/${13}/g" .env

cp config/templates/Dockerfile.tpl Dockerfile
sed -i "s/(PORT)/$8/g" Dockerfile

cp config/templates/docker-compose.yml.tpl docker-compose.yml
sed -i "s/(DB_USER)/$1/g" docker-compose.yml
sed -i "s/(DB_PASSWORD)/$2/g" docker-compose.yml
sed -i "s/(DB_PORT)/$4/g" docker-compose.yml
sed -i "s/(DB_NAME)/$5/g" docker-compose.yml
sed -i "s/(PROJECT_NAME)/$6/g" docker-compose.yml
sed -i "s/(PORT)/$8/g" docker-compose.yml