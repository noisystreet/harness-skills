CURSOR_SKILLS_DIR ?= $(HOME)/.cursor/skills
SKILLS := $(patsubst %/SKILL.md,%,$(wildcard */SKILL.md))

.DEFAULT_GOAL := list
.PHONY: install uninstall list check

install:
	@mkdir -p "$(CURSOR_SKILLS_DIR)"
	@count=0; \
	for skill in $(SKILLS); do \
		ln -sfn "$(CURDIR)/$$skill" "$(CURSOR_SKILLS_DIR)/$$skill"; \
		count=$$((count + 1)); \
	done; \
	echo "Installed $$count skills into $(CURSOR_SKILLS_DIR)"

uninstall:
	@if [ ! -d "$(CURSOR_SKILLS_DIR)" ]; then \
		echo "No skills directory: $(CURSOR_SKILLS_DIR)"; \
		exit 0; \
	fi
	@count=0; \
	for skill in $(SKILLS); do \
		link="$(CURSOR_SKILLS_DIR)/$$skill"; \
		target="$(CURDIR)/$$skill"; \
		if [ -L "$$link" ] && [ "$$(readlink "$$link")" = "$$target" ]; then \
			rm "$$link"; \
			count=$$((count + 1)); \
		fi; \
	done; \
	echo "Removed $$count skills from $(CURSOR_SKILLS_DIR)"

list:
	@printf "%-22s %-9s %s\n" "skill" "linked" "path"
	@printf "%-22s %-9s %s\n" "-----" "------" "----"
	@for skill in $(SKILLS); do \
		link="$(CURSOR_SKILLS_DIR)/$$skill"; \
		target="$(CURDIR)/$$skill"; \
		if [ -L "$$link" ] && [ "$$(readlink "$$link")" = "$$target" ]; then \
			linked="yes"; \
		else \
			linked="no"; \
		fi; \
		printf "%-22s %-9s %s\n" "$$skill" "$$linked" "$$target"; \
	done

check:
	@python3 tools/check_skills.py
