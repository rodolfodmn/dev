<?php

namespace Alura\DesignPattern\EstadosOrcamento;

use Alura\DesignPattern\Orcamento;

class Aprovado extends EstadoOrcamento
{
	public function calculaDescontoExtra(Orcamento $orcamento): float
	{
		return $orcamento->valor * 0.2;
	}

	public function finaliza(Orcamento $orcamento)
	{
		$orcamento->estadoAtual = new Finalizado();
	}
}
