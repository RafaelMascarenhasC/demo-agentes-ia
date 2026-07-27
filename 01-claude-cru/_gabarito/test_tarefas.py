"""Testes do mini gerenciador de tarefas."""
import unittest

from tarefas import adicionar, concluir, remover, pendentes


class TestTarefas(unittest.TestCase):
    def setUp(self):
        self.tarefas = []
        adicionar(self.tarefas, "estudar")
        adicionar(self.tarefas, "treinar")

    def test_adicionar_cria_tarefa_pendente(self):
        self.assertEqual(len(self.tarefas), 2)
        self.assertFalse(self.tarefas[0]["feita"])

    def test_concluir_marca_a_tarefa_certa(self):
        concluir(self.tarefas, 0)
        self.assertTrue(self.tarefas[0]["feita"])
        self.assertFalse(self.tarefas[1]["feita"])

    def test_remover_tira_a_tarefa(self):
        remover(self.tarefas, 0)
        self.assertEqual(len(self.tarefas), 1)
        self.assertEqual(self.tarefas[0]["titulo"], "treinar")

    def test_pendentes_ignora_as_feitas(self):
        concluir(self.tarefas, 0)
        self.assertEqual(len(pendentes(self.tarefas)), 1)


if __name__ == "__main__":
    unittest.main()
