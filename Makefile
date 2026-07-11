SKILLS_DIR ?= $(if $(CURSOR_SKILLS_DIR),$(CURSOR_SKILLS_DIR),$(HOME)/.cursor/skills)
TRAE_SKILLS_DIR ?= $(HOME)/.trae/skills
TRAE_CN_SKILLS_DIR ?= $(HOME)/.trae-cn/skills
SKILLS := $(patsubst %/SKILL.md,%,$(wildcard */SKILL.md))

.DEFAULT_GOAL := help
.PHONY: help install uninstall list catalog check
.PHONY: install-trae uninstall-trae list-trae
.PHONY: install-trae-cn uninstall-trae-cn list-trae-cn

help: ## Show available make targets
	@printf "%-20s %s\n" "target" "description"
	@printf "%-20s %s\n" "------" "-----------"
	@grep -E '^[a-zA-Z0-9_-]+:.*?##' "$(firstword $(MAKEFILE_LIST))" | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-20s %s\n", $$1, $$2}'

install: ## Install skills into SKILLS_DIR (default: ~/.cursor/skills)
	@mkdir -p "$(SKILLS_DIR)"
	@count=0; \
	for skill in $(SKILLS); do \
		ln -sfn "$(CURDIR)/$$skill" "$(SKILLS_DIR)/$$skill"; \
		count=$$((count + 1)); \
	done; \
	echo "Installed $$count skills into $(SKILLS_DIR)"

uninstall: ## Remove this repo's skill links from SKILLS_DIR
	@if [ ! -d "$(SKILLS_DIR)" ]; then \
		echo "No skills directory: $(SKILLS_DIR)"; \
		exit 0; \
	fi
	@count=0; \
	for skill in $(SKILLS); do \
		link="$(SKILLS_DIR)/$$skill"; \
		target="$(CURDIR)/$$skill"; \
		if [ -L "$$link" ] && [ "$$(readlink "$$link")" = "$$target" ]; then \
			rm "$$link"; \
			count=$$((count + 1)); \
		fi; \
	done; \
	echo "Removed $$count skills from $(SKILLS_DIR)"

list: ## List skills and whether they are linked in SKILLS_DIR
	@printf "%-22s %-9s %s\n" "skill" "linked" "path"
	@printf "%-22s %-9s %s\n" "-----" "------" "----"
	@for skill in $(SKILLS); do \
		link="$(SKILLS_DIR)/$$skill"; \
		target="$(CURDIR)/$$skill"; \
		if [ -L "$$link" ] && [ "$$(readlink "$$link")" = "$$target" ]; then \
			linked="yes"; \
		else \
			linked="no"; \
		fi; \
		printf "%-22s %-9s %s\n" "$$skill" "$$linked" "$$target"; \
	done

install-trae: ## Install skills into ~/.trae/skills
	@$(MAKE) --no-print-directory install SKILLS_DIR="$(TRAE_SKILLS_DIR)"

uninstall-trae: ## Remove this repo's links from ~/.trae/skills
	@$(MAKE) --no-print-directory uninstall SKILLS_DIR="$(TRAE_SKILLS_DIR)"

list-trae: ## List link status for ~/.trae/skills
	@$(MAKE) --no-print-directory list SKILLS_DIR="$(TRAE_SKILLS_DIR)"

install-trae-cn: ## Install skills into ~/.trae-cn/skills
	@$(MAKE) --no-print-directory install SKILLS_DIR="$(TRAE_CN_SKILLS_DIR)"

uninstall-trae-cn: ## Remove this repo's links from ~/.trae-cn/skills
	@$(MAKE) --no-print-directory uninstall SKILLS_DIR="$(TRAE_CN_SKILLS_DIR)"

list-trae-cn: ## List link status for ~/.trae-cn/skills
	@$(MAKE) --no-print-directory list SKILLS_DIR="$(TRAE_CN_SKILLS_DIR)"

catalog: ## Regenerate the README skills catalog
	@python3 tools/catalog_skills.py --write

check: ## Validate skill metadata, links, and README catalog
	@python3 tools/check_skills.py
