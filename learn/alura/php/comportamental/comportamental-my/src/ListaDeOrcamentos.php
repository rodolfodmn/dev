<?php

namespace Alura\DesignPattern;

class ListaDeOrcamentos implements \IteratorAggregate
{
	private array $orcamento;

	public function __construct()
	{
		$this->orcamentos = [];
	}

	public function addOrcamento(Orcamento $orcamento)
	{
		$this->orcamentos[] = $orcamento;
	}

	public function getIterator()
	{
		return new \ArrayIterator($this->orcamento);
	}
}
