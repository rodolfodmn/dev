<?php

namespace Alura\DesignPattern;

use Alura\DesignPattern\EstadosOrcamento\EmAprovacao;
use Alura\DesignPattern\EstadosOrcamento\EstadosOrcamento;

class Orcamento
{
	public int $quantidadeItens;
	public float $valor;
	public EstadosOrcamento $estadoAtual;

	public function __construct()
	{
		$this->estadoAtual = new EmAprovacao();
	}

	public function aplicaDescontoExtra()
	{
		$this->valor -= $this->estadoAtual->calculaDescontoExtra($this);
	}

	public function aprova()
	{
		$this->estadoAtual->aprova($this);
	}

	public function reprova() 
	{
		$this->estadoAtual->aprova($this);
	}

	public function finaliza()
	{
		$this->estadoAtual->finaliza($this);
	}
}
