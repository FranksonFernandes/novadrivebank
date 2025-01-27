consulta_sql = '''
SELECT C.PROFISSAO,
	   C.TEMPOPROFISSAO,
	   C.RENDA,
	   C.TIPORESIDENCIA, 
	   C.ESCOLARIDADE,
	   C.SCORE,
	   EXTRACT(YEAR FROM AGE (C.DATANASCIMENTO)) AS IDADE,
	   C.DEPENDENTES,
	   C.ESTADOCIVIL,
	   PF.NOMECOMERCIAL AS PRODUTO,
	   PC.VALORSOLICITADO,
	   PC.VALORTOTALBEM ,
	   CASE 
		   WHEN COUNT(P.STATUS) FILTER (WHERE P.STATUS = 'VENCIDO') > 0 THEN 'RUIM'
	   		ELSE 'BOM' END AS CLASSE
	   	FROM CLIENTES C
	   	JOIN PEDIDOCREDITO PC ON (C.CLIENTEID = PC.CLIENTEID)  
	   	JOIN PRODUTOSFINANCIADOS PF ON (PC.PRODUTOID = PF.PRODUTOID)
	   	LEFT JOIN PARCELASCREDITO P ON (PC.SOLICITACAOID = P.SOLICITACAOID)
	   	WHERE PC.STATUS = 'Aprovado' 
	   	group by c.clienteid, pf.nomecomercial, pc.valorsolicitado, pc.valortotalbem  


'''