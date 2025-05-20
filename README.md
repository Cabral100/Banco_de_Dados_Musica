# Projeto 2 - Banco de Dados para um Sistema de Streaming de Música

## Integrantes do grupo

- **Guilherme Morais Escudeiro** - RA: 24.123.005-1  
- **Gustavo Mendes Franco Lapin Atui** – RA: 24.123.072-1  
- **Lucas Tonoli Cabral Duarte** - RA: 24.123.032-5

---

## 📌 Descrição do Projeto

Desenvolvimento de um sistema de banco de dados para uma plataforma de **streaming de música**, com modelagem, criação das tabelas, inserção automatizada de dados e consultas SQL para análise.

---

## 🎯 Objetivos

- Criar um modelo de banco de dados funcional e escalável;
- Utilizar boas práticas de modelagem e normalização (3FN);
- Gerar dados fictícios realistas com Python e Faker;
- Executar queries para análise e extração de insights.

---

## 🔧 Metodologia

1. **Modelagem Conceitual**  
   Entidades e relacionamentos no formato MER.

2. **Modelagem Lógica (3FN)**  
   Conversão para modelo relacional normalizado.

3. **Implementação Física (DDL)**  
   Criação de tabelas no PostgreSQL.

4. **Geração de Dados (Python + Faker)**  
   Script para povoamento automatizado do banco.

5. **Consultas SQL**  
   Extração e análise de dados com queries otimizadas.

---

## 🧱 Principais Entidades

- `usuarios (id, nome, email, plano_id, nascimento)`
- `planos (id, nome, preco)`
- `artistas (id, nome, nacionalidade)`
- `albuns (id, titulo, ano, artista_id)`
- `musicas (id, titulo, duracao, genero, album_id)`
- `reproducoes (id, usuario_id, musica_id, data_hora, dispositivo)`
- `avaliacoes (id, usuario_id, musica_id, nota, comentario)`
- `playlists (id, nome, usuario_id)`
- `musicas_playlists (playlist_id, musica_id)`

---

## 🖼 Modelo Relacional

![Modelo Relacional](./dd2d0d57-85eb-4cd3-bcbe-95468ead4553.png)

---

## 🧪 Consultas SQL

### ✅ Consultas obrigatórias

```sql
-- 1. Soma e média das durações de músicas por gênero
SELECT genero, SUM(duracao), AVG(duracao) FROM musicas GROUP BY genero;

-- 2. Avaliações feitas por usuários
SELECT u.nome, m.titulo, a.nota, a.comentario 
FROM avaliacoes a
JOIN usuarios u ON u.id = a.usuario_id
JOIN musicas m ON m.id = a.musica_id;

-- 3. Usuários com seus planos
SELECT u.nome, p.nome AS plano
FROM usuarios u
JOIN planos p ON u.plano_id = p.id;

-- 4. Músicas de um álbum de um artista específico
SELECT m.titulo 
FROM musicas m
JOIN albuns a ON m.album_id = a.id
JOIN artistas ar ON a.artista_id = ar.id
WHERE ar.nome = 'Nome do Artista' AND a.titulo = 'Nome do Álbum';

-- 5. Álbuns lançados a partir de 2015
SELECT * FROM albuns WHERE ano >= 2015;
