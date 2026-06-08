# 🐍 Transformador de CEPs e Pontos de Coleta

![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-%23039BE5.svg?style=for-the-badge&logo=firebase)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-005571.svg?style=for-the-badge&logo=python&logoColor=white)

## 📝 Descrição do Projeto
O **Transformador de CEPs e Pontos de Coleta** (referenciado no código como o ecossistema "Locais das Tampinhas") é uma ferramenta automatizada desenvolvida em Python para estruturação, enriquecimento e ingestão em lote (*bulk ingestion*) de dados geográficos no **Google Cloud Firestore**. 

O sistema funciona como um pipeline ETL (Extract, Transform, Load) simplificado e modularizado:
1. **Extração (E):** Lê dados estruturados de uma planilha Excel (`planilha.xlsx`) usando Pandas.
2. **Transformação (T):** Consulta uma API pública de geolocalização (`AwesomeAPI`) para converter CEPs textuais em coordenadas geográficas precisas (Latitude e Longitude), tratando erros de conexão e registros inexistentes.
3. **Carga (L):** Estrutura as informações de forma limpa, mapeando as coordenadas para objetos espaciais nativos `GeoPoint` e persistindo os dados no Firestore através de autenticação administrativa segura.

## 🚀 Tecnologias e Bibliotecas Utilizadas
* **Linguagem:** Python 3.x
* **Manipulação de Dados:** `pandas` e `openpyxl` (para extração do arquivo Excel).
* **Consumo de APIs:** `requests` (para comunicação HTTP síncrona com tratamento de timeouts).
* **SDK Cloud:** `firebase-admin` (Gerenciamento de credenciais e ciclo de vida do app).
* **Engine de Banco de Dados:** `google-cloud-firestore` (Persistência NoSQL nativa e mapeamento espacial por `GeoPoint`).

## 📁 Arquitetura do Projeto
O projeto é estruturado de forma modularizada em três blocos lógicos principais:

### 1. Script Principal (`main.py`)
Responsável por orquestrar o fluxo de dados, abrindo a planilha, iterando por suas linhas de forma linear e invocando os módulos de transformação e envio.

### 2. Módulo de Transformação e Geocodificação (`transform.py`)
Realiza a limpeza do CEP (removendo hifens e espaços) e consome os dados da API pública para retornar um par de floats formatados como latitude e longitude.

### 3. Módulo de Conexão e Envio (`enviar.py`)
Inicializa o SDK administrativo do Firebase utilizando chaves privadas criptografadas e envia os dicionários estruturados ao Firestore NoSQL.

## 📊 Diferenciais e Aprendizados

* **Mapeamento Geoespacial Nativo:** O uso do `GeoPoint` permite que plataformas de mapas (como Leaflet, Google Maps API ou Mapbox) leiam diretamente os metadados salvos no Firestore, viabilizando consultas por raio de proximidade diretamente no banco de dados.
* **Resiliência e Comunicação HTTP:** Implementação de cláusulas de `timeout` na requisição HTTP e captura isolada de exceções, evitando travamentos (*deadlocks*) do script caso a internet caia no meio do processamento em massa.
* **Segurança Baseada em Service Account:** O script emprega autenticação Server-to-Server baseada em RBAC (Role-Based Access Control). A chave privada isola o privilégio de escrita do backend, impedindo que o cliente web/mobile tenha chaves de gravação irrestritas.
* **Camada Adaptativa NoSQL:** O código mapeia campos opcionais (como o parâmetro `obs`), respeitando o esquema livre (*schema-less*) do Firestore e poupando espaço de armazenamento nos documentos que não possuem observações.

## 🔧 Como Executar

### 1. Pré-requisitos
Certifique-se de ter o Python 3.8+ instalado e prepare um ambiente virtual (ativando-o via terminal com `source venv/bin/activate` no Linux/macOS ou `venv\Scripts\activate` no Windows).

### 2. Instalação das Dependências
Instale todos os pacotes requeridos utilizando o gerenciador `pip` (pacotes: `firebase-admin`, `google-cloud-firestore`, `pandas`, `requests`, `openpyxl`).

### 3. Configuração de Credenciais e Arquivos
1. Acesse o **Console do Firebase** > Configurações do Projeto > Contas de Serviço.
2. Gere uma nova chave privada gerando um arquivo `.json`.
3. Renomeie e salve este arquivo na raiz do seu projeto com o nome exato esperado pelo script: `locais-das-tampinhas-firebase-adminsdk-fbsvc-50ddff0e8b.json`.
4. Crie ou posicione sua planilha Excel com o nome `planilha.xlsx` na raiz do projeto. Ela obrigatoriamente deve conter as colunas: `nome`, `endereço`, `cep`, `horario` e `obs`.

### 4. Execução
Com o ambiente configurado, basta executar o arquivo principal `main.py` no seu terminal.

[Volte ao inicio](https://github.com/marceloProgramas)
