### **Resumo do Projeto**

Este projeto é uma API RESTful simples desenvolvida com **Flask** e integrada com **Swagger** (via `flask-restx`) para gerenciar usuários armazenados em um arquivo JSON.

---

### **Tecnologias Utilizadas**
1. **Python**: Linguagem principal para construir a aplicação.
2. **Flask**: Framework leve para criar APIs e aplicações web.
3. **Flask-RESTX**: Extensão para documentar e estruturar APIs, fornecendo integração com Swagger.
4. **JSON**: Usado como "banco de dados" para persistir os dados de usuários de forma simples e legível.

---

### **Como Funciona o Projeto**
1. **Estrutura dos Dados**:
   - Os dados dos usuários são armazenados em um arquivo `users.json`, simulando um banco de dados.
   - Cada usuário possui os campos:
     - `id` (gerado automaticamente).
     - `name` (obrigatório).

2. **Endpoints Disponíveis**:
   - **GET /users**: Retorna todos os usuários registrados.
   - **POST /users**: Adiciona um novo usuário, recebendo um JSON com o campo `name`.

3. **Swagger para Documentação**:
   - O Swagger, acessível via navegador, apresenta uma interface gráfica para explorar e testar a API.
   - URL: [http://127.0.0.1:5000/swagger-ui/](http://127.0.0.1:5000/swagger-ui/)

4. **Funções Internas**:
   - `read_users()`: Lê os usuários do arquivo JSON.
   - `write_users(users)`: Salva os usuários no arquivo JSON.

---

### **Passos para Montar o Projeto**
1. **Configuração Inicial**:
   - Criado um arquivo Python (`app.py`) para implementar a lógica da API.
   - Adicionado um arquivo `users.json` para armazenar os dados.

2. **Definição do Modelo**:
   - `flask-restx` é usado para descrever a estrutura do usuário (apenas `name` obrigatório).

3. **Endpoints REST**:
   - Construídos com a biblioteca Flask para receber e responder às solicitações HTTP.

4. **Documentação Automática**:
   - Com `flask-restx`, o Swagger foi configurado para gerar documentação interativa com base nos endpoints criados.

---

### **Como Usar**
1. **Instale as Dependências**:
   Certifique-se de que o arquivo `requirements.txt` possui as seguintes dependências:
   ```
   Flask
   flask-restx
   ```

2. **Execute a API**:
   No terminal:
   ```bash
   python app.py
   ```

3. **Acesse e Teste**:
   - Use o **Postman** ou o **Swagger** para testar os endpoints:
     - **GET /users**: Retorna os usuários.
     - **POST /users**: Adiciona um novo usuário enviando um JSON como:
       ```json
       {
           "name": "João"
       }
       ```

---

### **Por que Essas Tecnologias?**
- **Flask**: Simples, fácil de aprender e perfeito para APIs pequenas.
- **JSON**: Ideal para simular banco de dados em projetos iniciais.
- **Swagger**: Facilita o teste e a visualização da API, tornando o projeto mais acessível para iniciantes.
