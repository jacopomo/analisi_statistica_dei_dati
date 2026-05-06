RM = rm -rf
PYTHON = python3
MKDIR = mkdir -p

MAIN = analisi_statistica_dei_dati
PY_DIR = scripts
SRC_DIR = src/asd/interval_estimation

OUT_DIR = .build
STAMP_DIR = .stamps
REQUIRED_DIRS = $(OUT_DIR) images tables code

LATEXMK = latexmk -pdf -shell-escape -interaction=nonstopmode -halt-on-error -auxdir=$(OUT_DIR) -silent

VERSION := $(shell git describe --tags --always --abbrev=0)

# ------------------------
SOURCES = $(wildcard $(PY_DIR)/*.py) $(wildcard $(SRC_DIR)/*.py)
STAMPS = $(patsubst %.py,$(STAMP_DIR)/%.stamp,$(notdir $(SOURCES)))

# ------------------------
all: build

build: $(REQUIRED_DIRS) $(STAMPS) version
	$(LATEXMK) -jobname=$(MAIN) $(MAIN).tex

production: $(REQUIRED_DIRS) $(STAMPS) version
	$(LATEXMK) -jobname=production_$(MAIN) \
		-pdflatex='pdflatex %O "\def\draft{0}\input{%S}"' \
		$(MAIN).tex

$(STAMP_DIR)/%.stamp: $(PY_DIR)/%.py | $(STAMP_DIR)
	$(PYTHON) $<
	@echo "Executed $<" > $@

$(STAMP_DIR)/%.stamp: $(SRC_DIR)/%.py | $(STAMP_DIR)
	$(PYTHON) $<
	@echo "Executed $<" > $@

$(REQUIRED_DIRS) $(STAMP_DIR):
	$(MKDIR) $@

version: | $(OUT_DIR)
	printf '\\newcommand{\\version}{%s}\n' "$(VERSION)" > $(OUT_DIR)/version.tex

clean:
	$(LATEXMK) -c
	$(RM) $(OUT_DIR) $(STAMP_DIR)

cleanall: clean
	$(LATEXMK) -C
	$(RM) $(MAIN).pdf production_$(MAIN).pdf