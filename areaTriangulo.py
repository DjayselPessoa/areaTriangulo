ativo = True

while ativo:
    try:
        base = float(input("Informe a base do seu triângulo: "))
        altura = float(input("Informe a altura do seu triângulo : "))
        print("Escolha a unidade de medida\n")
        unidadeMedida = float(input("mm ->1\ncm -> 2\nm -> 3\nkm -> 4\n-> "))
        resultado = (base * altura) / 2
        resultado = round(resultado, 2)
        if not 1 <= unidadeMedida <= 4:
            raise ValueError("ERRO - esta opção não existe!")
            
        else:
            if unidadeMedida == 1:
                print(f"\nÁrea do triângulo: {base} * {altura} / 2 = {resultado} mm\n")
                break
            elif unidadeMedida == 2:
                print(f"\nÁrea do triângulo: {base} * {altura} / 2 = {resultado} cm\n")
                break
            elif unidadeMedida == 3:
                print(f"\nÁrea do triângulo: {base} * {altura} / 2 = {resultado} m\n")
                break
            elif unidadeMedida == 4:
                print(f"\nÁrea do triângulo: {base} * {altura} / 2 = {resultado} km\n")
                break
    except ValueError as e:
        print("\n", e)

print("Informe agora os dados para obtenção do volume do cilindro: ")
raioCilindro = float(input("raio(r) -> "))
alturaCilindro = float(input("altura(h) -> "))

volume = (3.14 * (raioCilindro ** 2)) * alturaCilindro
print(f"Volume do Cilindro: 3.14 * r² * h = {volume}³")
