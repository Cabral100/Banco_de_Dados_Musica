DROP TABLE IF EXISTS Avaliacoes CASCADE;
DROP TABLE IF EXISTS Musicas_Playlists CASCADE;
DROP TABLE IF EXISTS Reproducoes CASCADE;
DROP TABLE IF EXISTS Playlists CASCADE;
DROP TABLE IF EXISTS Musicas CASCADE;
DROP TABLE IF EXISTS Albuns CASCADE;
DROP TABLE IF EXISTS Artistas CASCADE;
DROP TABLE IF EXISTS Usuarios CASCADE;
DROP TABLE IF EXISTS Planos CASCADE;

-- Planos
CREATE TABLE Planos (
    id_plano SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(5,2) NOT NULL
);

-- Usuários
CREATE TABLE Usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    plano_id INT,
    FOREIGN KEY (plano_id) REFERENCES Planos(id_plano)
);

-- Artistas
CREATE TABLE Artistas (
    id_artista SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    nacionalidade VARCHAR(100)
);

-- Álbuns
CREATE TABLE Albuns (
    id_album SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    ano_lancamento INT,
    id_artista INT,
    FOREIGN KEY (id_artista) REFERENCES Artistas(id_artista)
);

-- Músicas
CREATE TABLE Musicas (
    id_musica SERIAL PRIMARY KEY,
    titulo VARCHAR(255),
    duracao TIME,
    genero VARCHAR(100),
    id_album INT,
    FOREIGN KEY (id_album) REFERENCES Albuns(id_album)
);

-- Playlists
CREATE TABLE Playlists (
    id_playlist SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    id_usuario INT,
    data_criacao DATE,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Musicas_Playlists (n:n)
CREATE TABLE Musicas_Playlists (
    id_musica INT,
    id_playlist INT,
    ordem INT,
    PRIMARY KEY (id_musica, id_playlist),
    FOREIGN KEY (id_musica) REFERENCES Musicas(id_musica),
    FOREIGN KEY (id_playlist) REFERENCES Playlists(id_playlist)
);

-- Reproducoes (Histórico)
CREATE TABLE Reproducoes (
    id_reproducao SERIAL PRIMARY KEY,
    id_usuario INT,
    id_musica INT,
    data_hora TIMESTAMP,
    dispositivo VARCHAR(100),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_musica) REFERENCES Musicas(id_musica)
);

-- Avaliações
CREATE TABLE Avaliacoes (
    id_avaliacao SERIAL PRIMARY KEY,
    id_usuario INT,
    id_musica INT,
    nota INT,
    comentario TEXT,
    data_avaliacao DATE,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_musica) REFERENCES Musicas(id_musica)
);
