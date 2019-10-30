# Imports Backend
 Aplicação onde valida arquivos csv conforme leiaute.
       
           
 ### PostgreSQL
 
 - ###### Instalação no Ubuntu
       sudo apt update
       sudo apt install postgresql postgresql-contrib
 - ###### Visualizando versão postgreSQL
       sudo -u postgres psql -c "SELECT version();"
 - ###### Acessando postgres e visualizando databases criados
       sudo su – postgres
       psql -l
 - ###### Acessando ambiente com psql e criando database
       psql
       CREATE DATABASE imports_file;
 - ###### Conectando database e visualizando tabelas
       \c imports_file
       \dt


 ### Python 3.7
    
 - ###### Instalação no Ubuntu
       sudo apt update
       sudo apt install software-properties-common
       sudo add-apt-repository ppa:deadsnakes/ppa
       sudo apt install python3.7
       python3.7 --version

 ### Virtualenv

 - ###### Instalação no Ubuntu:
       sudo apt install python3-venv	
       sudo apt install python-virtualenv
 - ###### Criando ambiente:
       sudo virtualenv --python=python3.7 venv
 - ###### Ativando ambiente:
       source venv/bin/activate


 ### Projeto Imports

 - ###### Instalando depedências do PostgreSQL para Python
       sudo apt-get install libpq-dev
       sudo apt-get install python3-Psycopg2
       sudo apt-get install python3-pip
       sudo pip3 install Psycopg2
 - ###### Instalando dependências
       sudo chmod 777 -R imports_backend
       pip install -r requirements.txt
 - ###### Iniciando serviço:
       python manage.py migrate
       python manage.py runserver


 ### Fontes de pesquisas

 - ###### Lista
       - Instalação do Python 3.7: https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/
       
       - Instalação do Psycopg2 com Python3: https://www.codevoila.com/post/2/python3-connect-postgresql-with-psycopg2-on-ubuntu
       
       - Integração Django com PostgreSQL: https://medium.com/@lucas_souto/integrando-django-com-postgresql-58b3520ddf6e
       
       - Criando Projeto Django: https://docs.djangoproject.com/en/2.2/intro/tutorial01/
       
       - Configurando Ambiente Virtual: https://tutorial.djangogirls.org/pt/installation/
