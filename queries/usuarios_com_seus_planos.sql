SELECT u.nome AS usuario, p.nome AS plano, p.preco
FROM usuarios u
JOIN planos p ON u.plano_id = p.id_plano;
