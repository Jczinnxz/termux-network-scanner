import nmap

def menu():
    print("-" * 30)
    print("   MENU DE REDE - TERMUX   ")
    print("-" * 30)
    print("1. Escaneamento Simples (Rápido)")
    print("2. Descobrir Dispositivos na Rede (Ping)")
    print("3. Detecção de SO e Versões (Completo)")
    print("4. Escanear Porta Específica")
    print("5. Sair")
    print("-" * 30)

def executar():
    nm = nmap.PortScanner()
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            ip = input("Digite o IP ou Host (ex: google.com): ")
            print(f"\n[+] Escaneando {ip}...")
            nm.scan(ip, '1-1024', '-v')
            for host in nm.all_hosts():
                print(f"Host: {host} | Estado: {nm[host].state()}")
        
        elif opcao == '2':
            rede = input("Digite a rede (ex: 192.168.1.0/24): ")
            print("\n[+] Buscando dispositivos ativos...")
            nm.scan(hosts=rede, arguments='-sn')
            for host in nm.all_hosts():
                print(f"Dispositivo Online: {host} - {nm[host].hostname()}")

        elif opcao == '3':
            ip = input("Digite o IP: ")
            print("\n[+] Executando escaneamento agressivo (Aguarde)...")
            nm.scan(ip, arguments='-sV -T4')
            for host in nm.all_hosts():
                for proto in nm[host].all_protocols():
                    print(f"Protocolo: {proto}")
                    portas = nm[host][proto].keys()
                    for p in portas:
                        print(f"Porta: {p} | Serviço: {nm[host][proto][p]['product']}")

        elif opcao == '4':
            ip = input("IP: ")
            porta = input("Porta: ")
            nm.scan(ip, porta)
            estado = nm[ip]['tcp'][int(porta)]['state']
            print(f"\nA porta {porta} no IP {ip} está: {estado.upper()}")

        elif opcao == '5':
            print("Saindo... Até logo!")
            break
        
        else:
            print("\n[!] Opção inválida. Tente novamente.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    executar()
          
