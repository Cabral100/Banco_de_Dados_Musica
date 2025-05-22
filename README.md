# Projeto 2 - Banco de Dados para um Sistema de Streaming de Música 🎵

## Integrantes do grupo
- **Guilherme Morais Escudeiro** - RA: 24.123.005-1
- **Gustavo Mendes Franco Lapin Atui** – RA: 24.123.072-1
- **Lucas Tonoli Cabral Duarte** - RA: 24.123.032-5

---

## Descrição do Projeto

Este projeto tem como objetivo o desenvolvimento de um sistema de banco de dados para uma plataforma de streaming musical. O banco de dados foi projetado para armazenar e gerenciar eficientemente informações como:

- Usuários  
- Artistas  
- Álbuns  
- Músicas  
- Gêneros musicais  
- Playlists  
- Execuções de faixas (histórico de reprodução)  
- Avaliações feitas pelos usuários  

Além disso, o projeto contempla a geração automatizada de dados fictícios, verificação de integridade e consultas SQL para simular o funcionamento real da plataforma.

---

## Introdução

A proposta deste trabalho é simular um ambiente real de banco de dados voltado para serviços de streaming musical, utilizando técnicas de modelagem conceitual, normalização até a 3FN, e consultas em SQL para extração e cruzamento de dados.

---

## Metodologia

O desenvolvimento do projeto foi dividido nas seguintes etapas:

1. **Modelagem Conceitual** – construção do Modelo Entidade-Relacionamento (MER);  
2. **Modelagem Lógica** – conversão para o Modelo Relacional em 3FN;  
3. **Implementação** – criação das tabelas utilizando DDL em SQL;  
4. **Geração de Dados** – uso da biblioteca `Faker` com Python para gerar dados fictícios e realistas;  
5. **Validação de Dados** – verificação de integridade referencial, coerência entre dados e ausência de redundância;  
6. **Consultas (queries)** – desenvolvimento de queries para atender a casos de uso típicos de uma plataforma de streaming.

---

## Consultas (Queries SQL)

### Consultas principais implementadas:

1. **Músicas mais tocadas por usuário**  
   Lista as músicas mais ouvidas por um determinado usuário com contagem de execuções.

2. **Playlists de um usuário com duração total**  
   Exibe as playlists criadas por um usuário e o tempo total de reprodução de cada uma.

3. **Músicas de um artista em um determinado período**  
   Filtra as faixas lançadas por um artista entre datas específicas.

4. **Gêneros mais ouvidos por faixa etária**  
   Agrupa execuções por faixa etária dos usuários para mostrar os gêneros musicais mais populares por grupo.

5. **Média de avaliações por música**  
   Mostra a média de avaliações recebidas por cada faixa.

6. **Artistas com mais músicas em playlists públicas**  
   Lista os artistas com mais faixas adicionadas a playlists públicas.

7. **Usuários que nunca criaram uma playlist**  
   Identifica os usuários que utilizam a plataforma, mas nunca criaram uma playlist.

8. **Álbuns com mais faixas**  
   Exibe os álbuns com maior número de músicas cadastradas.

9. **Músicas que nunca foram ouvidas**  
   Identifica músicas cadastradas na plataforma, mas que nunca foram executadas por nenhum usuário.

10. **Top 5 usuários que mais ouviram música no mês atual**  
   Lista os 5 usuários com maior tempo total de execução de músicas no mês corrente.

---

## Como Executar o Projeto

Primeiramente, utilize o arquivo ddl.sql para gerar as tabelas, após isso, utilize o código bd_codigo.py para gerar os dados de seu database, para isso, preencha o arquivo .env com suas váriaveis de acesso. Depois sinta-se a vontade para utilizar as outras queries disponíveis.

---

# Modelos

## 3FN
![image](https://github.com/user-attachments/assets/a0f73945-21aa-416a-9974-ddc18972a508)

## MER
![image](https://github.com/user-attachments/assets/b0f8d88a-4f71-4611-9358-522d6e2d92f9)
