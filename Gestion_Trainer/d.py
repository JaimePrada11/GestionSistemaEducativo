def main():
    n_universidades = int(input("Ingrese la cantidad de universidades: "))
    resultado_general = {"aceptan": 0, "rechazan": 0, "empates": 0}

    for _ in range(n_universidades):
        nombre = input("\nNombre de la universidad: ")
        votos = {"A": 0, "R": 0, "N": 0, "B": 0}

        while True:
            voto = input("Ingrese el voto (A, R, N, B o X para terminar): ").strip().upper()
            if voto == "X":
                break
            if voto in votos:
                votos[voto] += 1

        print(f"\nResultados de {nombre}:")
        print(f"Aceptar: {votos['A']}")
        print(f"Rechazar: {votos['R']}")
        print(f"Nulo: {votos['N']}")
        print(f"Blanco: {votos['B']}")

        if votos["A"] > votos["R"]:
            resultado_general["aceptan"] += 1
        elif votos["R"] > votos["A"]:
            resultado_general["rechazan"] += 1
        else:
            resultado_general["empates"] += 1

    print("\nResultados finales:")
    print(f"Universidades que aceptan: {resultado_general['aceptan']}")
    print(f"Universidades que rechazan: {resultado_general['rechazan']}")
    print(f"Universidades con empate: {resultado_general['empates']}")

main()