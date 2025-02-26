### **Resumo do Projeto**

Este projeto é uma aplicação web desenvolvida com **Flask**, **HTML**, **CSS** e **JavaScript** para resolver equações matemáticas do primeiro grau utilizando a biblioteca **SymPy**. O usuário pode inserir uma equação e obter a solução diretamente na interface, que é simples e intuitiva. O projeto foi projetado para ser leve, eficiente e fácil de usar, com um design que remete à matemática e à lógica.

---

### **Tecnologias Utilizadas**
1. **Python**: Linguagem principal para a construção da aplicação web e back-end.
2. **Flask**: Framework leve para criar a API que processa as solicitações do usuário.
3. **SymPy**: Biblioteca para resolução simbólica de equações matemáticas.
4. **HTML/CSS**: Usados para criar o front-end da aplicação com uma interface limpa e amigável.
5. **JavaScript**: Responsável por enviar os dados para a API e atualizar a interface com as respostas.
6. **Flask-CORS**: Permite que o front-end se comunique com o back-end, mesmo em domínios diferentes.

---

### **Como Funciona o Projeto**
1. **Estrutura dos Dados e Fluxo de Trabalho**:
   - O front-end permite que o usuário insira uma equação do primeiro grau (ex: `2x + 3 = 7`).
   - O back-end recebe essa entrada, valida e processa a equação utilizando o SymPy.
   - A solução é retornada e exibida dinamicamente na interface do usuário.

2. **Estrutura da Aplicação**:
   - **HTML**: A página possui um campo de entrada onde o usuário pode digitar a equação. Os resultados são exibidos em uma área abaixo do campo.
   - **CSS**: O design foi estilizado com cores que remetem à matemática, como tons de azul (lógica) e laranja (criatividade).
   - **JavaScript**: Realiza as requisições ao back-end, recebendo e exibindo a solução da equação.

3. **Rota no Back-End**:
   - **POST /resolver**: Recebe a equação do usuário, valida e resolve utilizando o SymPy.

4. **Exibição das Respostas**:
   - A solução é apresentada no front-end de forma clara e direta, com uma mensagem explicativa (ex: `A solução é x = 2`).

---

### **Passos para Montar o Projeto**
1. **Configuração Inicial**:
   - O projeto foi iniciado com a configuração de um servidor Flask simples para processar as requisições.
   - O SymPy foi configurado para resolver equações do primeiro grau de forma simbólica.

2. **Front-End**:
   - O HTML foi estruturado com um campo de entrada simples para a equação.
   - O CSS foi adaptado para criar uma aparência limpa e moderna, com cores que remetem à matemática.
   - O JavaScript foi implementado para enviar os dados para o back-end e receber a solução.

3. **Back-End**:
   - O Flask recebe a requisição, valida a entrada, resolve a equação com o SymPy e envia a solução de volta para o front-end.

---

### **Como Usar**
1. **Instale as Dependências**:
   Certifique-se de que o arquivo `requirements.txt` possui as seguintes dependências:
   ```
   Flask
   sympy
   flask-cors
   ```

2. **Execute a API**:
   No terminal, execute o servidor Flask:
   ```bash
   python app.py
   ```

3. **Acesse o Front-End**:
   - Abra o arquivo `index.html` no seu navegador ou acesse a URL gerada pelo Flask (geralmente `http://127.0.0.1:5000/`).

4. **Interaja com a Aplicação**:
   - Digite uma equação do primeiro grau (ex: `2x + 3 = 7`).
   - Clique em "Resolver" para obter a solução.

---

### **Por que Essas Tecnologias?**
- **Flask**: Simples, rápido e ideal para criar APIs de back-end.
- **SymPy**: Facilita a resolução de equações matemáticas de forma simbólica e precisa.
- **HTML/CSS**: Utilizados para criar uma interface de usuário acessível e com apelo estético relacionado à matemática.
- **JavaScript**: Proporciona uma experiência interativa e dinâmica ao usuário, fazendo a comunicação assíncrona com o back-end.
- **Flask-CORS**: Permite que o front-end se comunique com o back-end sem problemas de CORS.

---

### **Possíveis Melhorias Futuras**
- **Validação de Entrada**: Implementar uma verificação mais robusta para garantir que as equações inseridas sejam válidas.
- **Expansão de Funcionalidades**: Incluir suporte para outros tipos de equações (ex: quadráticas, cúbicas) e cálculos geométricos.
- **Explicações Detalhadas**: Adicionar uma funcionalidade para gerar explicações passo a passo sobre como a equação foi resolvida.
- **Gráficos**: Incluir gráficos para visualizar a equação e sua solução.

---

### **Conclusão**
Este projeto oferece uma maneira simples e eficiente de resolver equações do primeiro grau utilizando tecnologias modernas e acessíveis. A combinação do Flask, SymPy e uma interface bem projetada permite que usuários de diferentes níveis de conhecimento possam resolver problemas matemáticos de forma rápida e intuitiva.
