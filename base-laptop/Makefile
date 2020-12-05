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

.PHONY: undervolt
undervolt:
	@echo "************ Starting Ansible Undervolt ************"
	@ansible-playbook -K -k -t "undervolt" setup.yml
	@echo "************ Completed Ansible Undervolt ************"
