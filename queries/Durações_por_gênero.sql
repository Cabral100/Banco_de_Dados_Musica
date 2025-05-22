SELECT genero, AVG(duracao) AS duracao_media
FROM musicas
GROUP BY genero;
