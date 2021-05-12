<?php

namespace Alura\Solid\Model;

class Curso implements Pontuavel
{
	private $nome;
	private $videos;
	private $feedbacks;

	/**
	* undocumented function
	*
	* @return void
	*/
	public function __construct(string $nome)
	{
		$this->nome = $nome;
		$this->videos = [];
		$this->feedbacks = [];
	}

	public function receberFeedback(Feedback $feedback): void
	{
		$this->feedbacks[] = $feedback;
	}

	public function adicionarVideo(Video $video)
	{
		if ($video->minutosDeDuracao() < 3) {
			throw new \DomainException('video muito curto');
		}

		$this->videos[] = $video;
	}

	public function recuperarVideos(): array
	{
		return $this->videos;
	}

	public function recuperarPontuacao(): int
	{
		return 100;
	}
}
