SELECT p.nome AS plano, COUNT(u.id_usuario) AS total_usuarios
FROM planos p
LEFT JOIN usuarios u ON p.id_plano = u.plano_id
GROUP BY p.nome;
