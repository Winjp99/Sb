import os
import modules.check as check
from colorama import Back, Fore, Style
from modules import banner, control

check.dependency()
check.check_started()
check.check_update()

# Konfigurasi Cloudflare
CLOUDFLARE_TUNNEL_COMMAND = "cloudflared tunnel --url http://localhost:2525"

PORT = 2525

while True:
    banner.banner()
    control.run_php_server(PORT)

    # Menjalankan Cloudflare Tunnel
    os.system(CLOUDFLARE_TUNNEL_COMMAND)

    try:
        input(" " + Fore.WHITE + Back.RED + "If You Want Exit And Turn Off localhost / press enter or CTRL+C " + Style.RESET_ALL)
        control.kill_php_proc()
        exit()

    except KeyboardInterrupt:
        control.kill_php_proc()
        exit()
