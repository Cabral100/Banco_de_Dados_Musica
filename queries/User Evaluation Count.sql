SELECT u.nome, COUNT(a.id_avaliacao) AS total_avaliacoes
FROM usuarios u
JOIN avaliacoes a ON u.id_usuario = a.id_usuario
GROUP BY u.nome
HAVING COUNT(a.id_avaliacao) > 5;
