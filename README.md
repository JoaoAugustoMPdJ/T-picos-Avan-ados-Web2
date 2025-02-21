### **Resumo do Projeto**

Este projeto é uma aplicação web desenvolvida com **Flask**, **HTML**, **CSS** e **JavaScript** para resolver problemas matemáticos, como equações algébricas e cálculos geométricos, utilizando uma API de inteligência artificial integrada com a **OpenAI**. O usuário pode interagir com a IA para resolver problemas matemáticos, com explicações detalhadas e soluções passo a passo.

---

### **Tecnologias Utilizadas**
1. **Python**: Linguagem principal para a construção da aplicação web e back-end.
2. **Flask**: Framework leve para criar a API que processa as solicitações do usuário.
3. **OpenAI**: Usada para resolver problemas matemáticos e gerar explicações detalhadas.
4. **HTML/CSS**: Usados para criar o front-end da aplicação com uma interface limpa e amigável.
5. **JavaScript**: Responsável por enviar os dados para a API e atualizar a interface com as respostas.
6. **SymPy**: Biblioteca para resolução simbólica de equações matemáticas.

---

### **Como Funciona o Projeto**
1. **Estrutura dos Dados e Fluxo de Trabalho**:
   - O front-end permite que o usuário insira um tipo de problema (equação ou geometria) e um texto descrevendo o problema.
   - O back-end recebe essa entrada, utiliza a API do OpenAI para processar a questão e retorna a solução, resultados e passos explicativos.
   - A solução e os passos são exibidos dinamicamente na interface do usuário.

2. **Estrutura da Aplicação**:
   - **HTML**: A página possui um formulário onde o usuário pode escolher o tipo de problema e fornecer a entrada. Os resultados são exibidos em uma área abaixo do formulário.
   - **CSS**: O design foi estilizado para remeter à Grécia Antiga e à Matemática, com fontes e cores que evocam um clima clássico e acadêmico.
   - **JavaScript**: Realiza as requisições ao back-end, recebendo e exibindo os dados processados.

3. **Rota no Back-End**:
   - **POST /resolver**: Recebe a entrada do usuário e processa o problema utilizando o OpenAI para gerar a solução e os passos necessários.
   
4. **Exibição das Respostas**:
   - A solução e os passos são apresentados no front-end de forma clara, com cada passo explicado e detalhado para o entendimento do usuário.

---

### **Passos para Montar o Projeto**
1. **Configuração Inicial**:
   - O projeto foi iniciado com a configuração de um servidor Flask simples para processar as requisições.
   - A chave de API do OpenAI foi configurada para permitir a comunicação com a IA que resolve os problemas matemáticos.

2. **Front-End**:
   - O HTML foi estruturado com um formulário simples para inserir o tipo de problema e a descrição.
   - O CSS foi adaptado para criar uma aparência que remete à Grécia Antiga, utilizando fontes clássicas e tons sóbrios.
   - O JavaScript foi implementado para enviar os dados para o back-end e receber as respostas da IA.

3. **Back-End**:
   - O Flask recebe a requisição, faz a interação com a OpenAI para resolver o problema e envia os resultados de volta para o front-end.
   - A biblioteca SymPy foi utilizada para resolver equações algébricas e cálculos geométricos de forma simbólica.

---

### **Como Usar**
1. **Instale as Dependências**:
   Certifique-se de que o arquivo `requirements.txt` possui as seguintes dependências:
   ```
   Flask
   openai
   sympy
   ```

2. **Obtenha a chave da API do OpenAI**:
   - Registre-se na [OpenAI](https://platform.openai.com/signup) e gere sua chave da API.
   - Insira sua chave da API no arquivo `app.py` para permitir a comunicação com o modelo GPT.

3. **Execute a API**:
   No terminal, execute o servidor Flask:
   ```bash
   python app.py
   ```

4. **Acesse o Front-End**:
   - Abra o arquivo `index.html` no seu navegador ou acesse a URL gerada pelo Flask (geralmente `http://127.0.0.1:5000/`).

5. **Interaja com a Aplicação**:
   - Escolha o tipo de problema (Equação ou Geometria).
   - Digite o problema (por exemplo, `2x + 5 = 15` ou `raio = 5`).
   - Clique em "Enviar" para obter a solução e os passos.

---

### **Por que Essas Tecnologias?**
- **Flask**: Simples, rápido e ideal para criar APIs de back-end.
- **OpenAI**: Potente para gerar soluções matemáticas complexas e explicações detalhadas.
- **SymPy**: Facilita a resolução de problemas algébricos e geométricos de forma simbólica.
- **HTML/CSS**: Utilizados para criar uma interface de usuário acessível e com apelo estético relacionado à Matemática e à Grécia Antiga.
- **JavaScript**: Proporciona uma experiência interativa e dinâmica ao usuário, fazendo a comunicação assíncrona com o back-end.

---

### **Possíveis Melhorias Futuras**
- **Validação de Entrada**: Implementar uma verificação mais robusta para garantir que os problemas inseridos sejam válidos.
- **Personalização de Estilo**: Expandir o design com mais referências à Matemática clássica e antigas civilizações.
- **Expansão de Funcionalidades**: Incluir mais tipos de problemas matemáticos e opções de personalização da solução (ex: gráficos, explicações alternativas).

---

### **Conclusão**
Este projeto oferece uma maneira interessante e interativa de resolver problemas matemáticos com o auxílio da inteligência artificial. A combinação do Flask, OpenAI, e uma interface bem projetada permite que usuários de diferentes níveis de conhecimento possam aprender e entender matemática de uma maneira acessível.
