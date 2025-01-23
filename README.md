### Descrição do Projeto

Este projeto é um chatbot interativo desenvolvido usando a biblioteca `Streamlit` para a interface do usuário e a biblioteca `LangChain` para integração com modelos de linguagem da Amazon. O objetivo do projeto é criar um assistente virtual que possa responder perguntas e realizar tarefas com base nas entradas do usuário.

### Ferramentas Utilizadas

1. **Streamlit**:
   - Usado para criar a interface do usuário do chatbot.
   - Permite a criação rápida e fácil de uma aplicação web interativa.
   - Principais funções utilizadas: `st.chat_input`, `st.chat_message`, `st.markdown`, `st.session_state`.

2. **LangChain**:
   - Biblioteca utilizada para integrar modelos de linguagem da Amazon.
   - Facilita a criação de cadeias de conversação e o gerenciamento de memória de conversação.
   - Principais classes utilizadas: `ChatBedrock`, `ConversationSummaryBufferMemory`, `ConversationChain`.

3. **Transformers**:
   - Biblioteca necessária para o tokenizador utilizado pelo modelo de linguagem.
   - Instalada via `pip install transformers`.

4. **Logging**:
   - Utilizado para registrar informações de depuração e monitorar a entrada e saída do modelo.
   - Configurado para registrar informações no nível `INFO`.

### Estrutura do Código

1. **chat.py**:
   - Contém as funções principais para invocar o modelo de linguagem (`titan_llm`), criar a memória de conversação (`create_memory`) e obter respostas do chatbot (`get_chat_response`).
   - Utiliza a classe `ChatBedrock` para interagir com o modelo de linguagem da Amazon.

2. **chatFront.py**:
   - Contém a interface de usuário desenvolvida com `Streamlit`.
   - Gerencia o histórico de conversas e exibe as mensagens do usuário e do assistente virtual.
   - Chama a função `get_chat_response` para obter respostas detalhadas do modelo de linguagem.

### Como Executar

1. Instale as dependências necessárias:
   ```powershell
   pip install streamlit langchain transformers
   ```

2. Execute o script `chatFront.py`:
   ```powershell
   & "C:/Users/Aminah Makhoul/AppData/Local/Programs/Python/Python312/python.exe" "c:/Users/Aminah Makhoul/Downloads/CHAT/chatFront.py"
   ```

3. Acesse a aplicação web gerada pelo `Streamlit` e interaja com o chatbot.

Este projeto demonstra como integrar modelos de linguagem avançados em uma aplicação web interativa, utilizando ferramentas modernas e eficientes.
# chatBot
