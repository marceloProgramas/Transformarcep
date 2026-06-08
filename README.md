# 🐍 Firestore Geo-Populator - Carga Automática de Locais

![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-%23039BE5.svg?style=for-the-badge&logo=firebase)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![Pandas](https://shields.io)

## 📝 Descrição do Projeto
O **Firestore Geo-Populator** é uma ferramenta de automação desenvolvida em Python para realizar a ingestão de dados geográficos estruturados diretamente no Cloud Firestore. O objetivo principal é servir como um pipeline de dados eficiente (backend/scripts), permitindo cadastrar em massa pontos de interesse, locais de coleta ou coordenadas sem depender de inserções manuais pelo console.

Desenvolvido com foco em **segurança e integridade de tipos**, o script se conecta ao banco de dados utilizando credenciais administrativas privadas e converte dados decimais de latitude e longitude em objetos geográficos nativos do ecossistema Google.

## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **SDK Oficial:** `firebase-admin` (Gerenciamento de credenciais e ciclo de vida)
* **Engine de Dados:** `google-cloud-firestore` (Manipulação e persistência avançada NoSQL)
* **Mapeamento de Tipos:** Ingestão nativa usando `GeoPoint`

## 📊 Diferenciais e Aprendizados
O projeto foi desenhado seguindo os padrões recomendados pelo Google para comunicação Server-Side segura:
* **Persistência de Tipos Geográficos:** Mapeamento correto de tuplas de coordenadas em objetos `GeoPoint` válidos, garantindo compatibilidade instantânea com frontends em React/Leaflet.
* **Segurança Administrativa Compartimentada:** Uso do mecanismo de chaves privadas `.json` (Service Accounts), isolando as credenciais de backend para que nunca sejam expostas no código do cliente.
* **Camada Adaptativa de Dados:** Algoritmo focado no padrão NoSQL, permitindo o envio flexível de dados opcionais (como o campo `obs`) sem quebrar a estrutura ou o esquema da coleção.

## 🔧 Como Executar

1. Prepare o ambiente virtual e instale as dependências:
   ```bash
   pip install firebase-admin google-cloud-firestore
   ```
2. Obtenha o arquivo de chave privada (Service Account) no console do Firebase e salve-o na raiz do projeto com o nome de locais-das-tampinhas-firebase-adminsdk-fbsvc-50ddff0e8b.json.

3 .Execute o script principal para popular o banco de dados:
  ```Bash
  python main.py
  ```
