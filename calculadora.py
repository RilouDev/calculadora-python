while True:
    print("Calculadora de formas geométricas")
    print("\n1 - Círculo\n2 - Triângulo\n3 - Retângulo\n4 - Quadrado\n5 - Trapézio\n6 - Losango")
    forma = int(input("Escolha a forma geométrica (1-6): "))

    if forma == 1:
        raio = float(input("Digite o raio do círculo: "))
        area = 3.14 * raio ** 2
        print("A área do círculo é:", area)

    elif forma == 2:
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        area = (base * altura) / 2
        print("A área do triângulo é:", area)

    elif forma == 3:
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area = base * altura
        print("A área do retângulo é:", area)

    elif forma == 4:
        lado = float(input("Digite o lado do quadrado: "))
        area = lado ** 2
        print("A área do quadrado é:", area)

    elif forma == 5:
        base_maior = float(input("Digite a base maior do trapézio: "))
        base_menor = float(input("Digite a base menor do trapézio: "))
        altura = float(input("Digite a altura do trapézio: "))
        area = ((base_maior + base_menor) * altura) / 2
        print("A área do trapézio é:", area)

    elif forma == 6:
        diagonal_maior = float(input("Digite a diagonal maior do losango: "))
        diagonal_menor = float(input("Digite a diagonal menor do losango: "))
        area = (diagonal_maior * diagonal_menor) / 2
        print("A área do losango é:", area)

    else:
        print("Opção inválida. Por favor, escolha um número entre 1 e 6.")

    continuar = input("Deseja calcular outra forma? (s/n): ").strip().lower()
    if continuar != 's':
        print("Programa encerrado.")
        break