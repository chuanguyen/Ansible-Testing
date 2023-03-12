# Define default action when "make" is run by itself
.DEFAULT_GOAL :=all
all: lint baseline

# Lint the Ansible playbook for any errors
.PHONY: lint
lint:
	@echo "************ Starting Ansible Linting ************"
	@ansible-lint setup.yml
	@echo "************ Completed Ansible Linting ************"

.PHONY: baseline
baseline:
	@echo "************ Starting Ansible Baseline ************"
	@ansible-playbook -K -k setup.yml
	@echo "************ Completed Ansible Baseline ************"

.PHONY: baseline_test
baseline_test:
	@echo "************ Starting Ansible Baseline Test ************"
	@ansible-playbook --check -K -k setup.yml
	@echo "************ Completed Ansible Baseline Test ************"

.PHONY: ansible-playbook
ansible-playbook:
	@docker container rm ansible 1>/dev/null 2> /dev/null || true
	@docker run -it --name ansible -v $(shell pwd)/ansible:/ansible -v $(shell pwd)/ssh:/home/ansible/.ssh chua:ansible $(ANSIBLE_ARGS)
	@docker container rm ansible 1>/dev/null 2> /dev/null || true