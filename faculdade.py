from datetime import datetime

# ==========================================
# CONFIGURAÇÃO DO HORÁRIO
# ==========================================

horario = {
    "segunda": [
        ("18:30 - 19:20", "Coding", "Prof. SAMARA LIMA DE SOUZA"),
        ("19:20 - 20:10", "Coding", "Prof. SAMARA LIMA DE SOUZA"),
        ("20:10 - 21:00", "Coding", "Prof. SAMARA LIMA DE SOUZA"),
        ("21:00 - 21:50", "Coding", "Prof. SAMARA LIMA DE SOUZA"),
    ],

    "terça": [
        (
            "18:30 - 19:20",
            "Engenharia de Requisitos, Teste e Qualidade de Software",
            "Prof. RODRIGO SILVA MARQUES"
        ),
        (
            "19:20 - 20:10",
            "Engenharia de Requisitos, Teste e Qualidade de Software",
            "Prof. RODRIGO SILVA MARQUES"
        ),
        (
            "20:10 - 21:00",
            "Engenharia de Requisitos, Teste e Qualidade de Software",
            "Prof. RODRIGO SILVA MARQUES"
        ),
        ("21:00 - 21:50", "Atividades Práticas Interdisciplinares de Extensão I", "Prof. RODRIGO SILVA MARQUES"),
    ],

    "quarta": [
        ("19:00 - 20:00", "Inteligência Artificial Aplicada", ""),
        ("20:00 - 21:00", "Inteligência Artificial Aplicada", ""),
        ("21:00 - 22:00", "Inteligência Artificial Aplicada", ""),
    ],

    "quinta": [
        ("18:30 - 19:20", "Banco de Dados", "Prof. LENA VEIGA E SILVA"),
        ("19:20 - 20:10", "Banco de Dados", "Prof. LENA VEIGA E SILVA"),
        ("20:10 - 21:00", "Desenvolvimento de Aplicações para Internet", "Prof. MARCELO HELY DA SILVA OLIVEIRA"),
        ("21:00 - 21:50", "Desenvolvimento de Aplicações para Internet", "Prof. MARCELO HELY DA SILVA OLIVEIRA"),
    ],

    "sexta": [
        ("18:30 - 19:20", "Front-End Frameworks", "Prof. ANDRE AVELINO DA SILVA NETO"),
        ("19:20 - 20:10", "Front-End Frameworks", "Prof. ANDRE AVELINO DA SILVA NETO"),
        ("20:10 - 21:00", "Front-End Frameworks", "Prof. ANDRE AVELINO DA SILVA NETO"),
        ("21:00 - 21:50", "Desenvolvimento de Aplicações para Internet", "Prof. MARCELO HELY DA SILVA OLIVEIRA"),
    ],

    "sábado": [],

    "domingo": []
}


# ==========================================
# DIAS DA SEMANA
# ==========================================

dias = [
    "segunda",
    "terça",
    "quarta",
    "quinta",
    "sexta",
    "sábado",
    "domingo"
]


# ==========================================
# FUNÇÕES
# ==========================================

def limpar_tela():
    print("\033[2J\033[H", end="")


def mostrar_dia(dia):
    limpar_tela()

    print("=" * 70)
    print("                    HORÁRIO DA FACULDADE")
    print("=" * 70)
    print()

    print(f"📅 {dia.upper()}")
    print("-" * 70)

    aulas = horario.get(dia, [])

    if not aulas:
        print("🎉 Nenhuma aula hoje!")
        return

    for hora, disciplina, professor in aulas:
        print()
        print(f"⏰ {hora}")
        print(f"📚 {disciplina}")

        if professor:
            print(f"👨‍🏫 {professor}")

        print("-" * 70)


def mostrar_semana():
    limpar_tela()

    print("=" * 70)
    print("                    HORÁRIO DA FACULDADE")
    print("=" * 70)

    for dia in dias:
        print()
        print(f"📅 {dia.upper()}")
        print("-" * 70)

        aulas = horario.get(dia, [])

        if not aulas:
            print("   Sem aulas")
            continue

        for hora, disciplina, professor in aulas:
            print(f"⏰ {hora}  |  {disciplina}")

    print()
    print("=" * 70)


def menu():
    while True:
        limpar_tela()

        agora = datetime.now()
        dia_atual = dias[agora.weekday()]

        print("=" * 70)
        print("                 🎓 HORÁRIO DA FACULDADE")
        print("=" * 70)

        print()
        print(f"Hoje: {dia_atual.upper()}")
        print(f"Data: {agora.strftime('%d/%m/%Y')}")
        print()

        print("1 - 📅 Ver aulas de hoje")
        print("2 - 📖 Ver semana completa")
        print("3 - 📕 Segunda-feira")
        print("4 - 📕 Terça-feira")
        print("5 - 📕 Quarta-feira")
        print("6 - 📕 Quinta-feira")
        print("7 - 📕 Sexta-feira")
        print("8 - 📕 Sábado")
        print("9 - 📕 Domingo")
        print("0 - ❌ Sair")

        print()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_dia(dia_atual)
            input("\nPressione ENTER para voltar...")

        elif opcao == "2":
            mostrar_semana()
            input("\nPressione ENTER para voltar...")

        elif opcao in ["3", "4", "5", "6", "7", "8", "9"]:
            indice = int(opcao) - 3
            mostrar_dia(dias[indice])
            input("\nPressione ENTER para voltar...")

        elif opcao == "0":
            print("\nAté mais! 👋")
            break

        else:
            input("\n❌ Opção inválida. Pressione ENTER...")


# ==========================================
# INICIAR PROGRAMA
# ==========================================

if __name__ == "__main__":
    menu()
