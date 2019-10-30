# Imports Backend
 Aplicação onde valida arquivos csv conforme layout.
       
           
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
 
 - ###### Instalando dependências
       sudo chmod 777 -R imports_backend
       pip install -r requirements.txt
 - ###### Iniciando Serviço:
       python manage.py runserver