# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de requisitos
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação
COPY . .

# Exponha a porta que a aplicação irá rodar
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "run.py"] 