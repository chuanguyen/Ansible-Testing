sudo pacman -Syu --noconfirm
sudo pacman -S --noconfirm --needed ansible
ansible-playbook setup.yml --check
