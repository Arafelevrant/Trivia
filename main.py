import requests
import json
import random

def mostrar_menu():
    print("\n" + "="*40)
    print("   TRIVIA INTERACTIVA DE NÚMEROS")
    print("="*40)
    print("\n1. Obtener trivia de un número específico")
    print("2. Obtener trivia aleatoria")
    print("3. Adivinar el número de una trivia")
    print("4. Ver trivia del día")
    print("5. Salir")
    return input("\nSelecciona una opción (1-5): ")

def obtener_trivia(numero=None):
    base_url = "http://numbersapi.com/"
    try:
        if numero is None:
            url = f"{base_url}random?json"
        else:
            url = f"{base_url}{numero}?json"
        
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return json.loads(response.text)
    except Exception as e:
        print(f"\n⚠️ Error al obtener trivia: {e}")
        return None

def trivia_especifica():
    while True:
        try:
            num = input("\nIngresa un número (o 'q' para volver): ")
            if num.lower() == 'q':
                return
            
            trivia = obtener_trivia(num)
            if trivia:
                print(f"\n🔢 Trivia del número {trivia['number']}:")
                print(f"📖 {trivia['text']}")
        except ValueError:
            print("Por favor ingresa un número válido.")

def trivia_aleatoria():
    trivia = obtener_trivia()
    if trivia:
        print(f"\n🎲 Trivia aleatoria:")
        print(f"🔢 Número: {trivia['number']}")
        print(f"📖 {trivia['text']}")

def adivina_numero():
    trivia = obtener_trivia()
    if not trivia:
        return
    
    print("\n🤔 ADIVINA EL NÚMERO")
    print(f"\nPista: {trivia['text']}")
    
    intentos = 3
    while intentos > 0:
        try:
            guess = int(input(f"\n¿Qué número crees que es? ({intentos} intentos restantes): "))
            if guess == trivia['number']:
                print(f"\n🎉 ¡Correcto! Era el número {trivia['number']}")
                return
            else:
                intentos -= 1
                print("❌ Incorrecto. Sigue intentando.")
        except ValueError:
            print("Por favor ingresa un número válido.")
    
    print(f"\n😢 Lo siento, el número era {trivia['number']}")

def trivia_del_dia():
    # Usamos el día del mes como número "especial"
    from datetime import datetime
    dia_actual = datetime.now().day
    trivia = obtener_trivia(dia_actual)
    if trivia:
        print(f"\n📅 Trivia del día (día {dia_actual} del mes):")
        print(f"📖 {trivia['text']}")

def main():
    print("\nBienvenido a la trivia numérica interactiva!")
    print("Descubre datos curiosos sobre números a través de la NumbersAPI.")
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            trivia_especifica()
        elif opcion == "2":
            trivia_aleatoria()
        elif opcion == "3":
            adivina_numero()
        elif opcion == "4":
            trivia_del_dia()
        elif opcion == "5":
            print("\n¡Gracias por jugar con las trivias numéricas! Hasta pronto.")
            break
        else:
            print("\nOpción no válida. Por favor elige del 1 al 5.")

if __name__ == "__main__":
    # Verificar conexión a internet y disponibilidad de la API
    try:
        test = requests.get("http://numbersapi.com/1?json", timeout=5)
        main()
    except requests.ConnectionError:
        print("Error: No hay conexión a internet o la API no está disponible.")
    except Exception as e:
        print(f"Error inesperado: {e}")