<?php

namespace Alura\DesignPatern\AcoesAoGerarPedido;

use Alura\DesignPattern\Pedido;

class EnviarPedidoPorEmail implements AcaoAposGerarPedido
{
	public function executaAcao(Pedido $pedido): void
	{
		echo 'Gerando log de geração de pedido';
	}
}
