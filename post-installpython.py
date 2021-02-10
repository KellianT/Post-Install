import os


#!/bin/bash
os.system( "echo 'UBUNTU POST-INSTALL SCRIPT' > log.txt")
os.system( "echo 'Updating APT...' >> log.txt")
os.system( "sudo apt-get update >> log.txt ")
os.system( "echo 'Installing base packages' >> log.txt ")
os.system( "sudo apt-get install --yes git git-extras build-essential python3-pip htop glances >> log.txt" )
os.system( "echo 'Installing Visual Studio code' >> log.txt " )
os.system("sudo sudo snap install code >> log.txt " )
os.system( "echo 'Installing Discord' >> log.txt " )
os.system( "sudo sudo snap install discord >> log.txt " )


# On importe le module os afin d'accéder à la commande os.system qui permet de traduire en langage python des commandes bash.