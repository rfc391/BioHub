
.PHONY: all install build-linux build-macos build-windows docker-airgap clean

all: install

install:
	@echo "Installing BioHub in secure mode..."
	bash scripts/install.sh

build-linux:
	@echo "Building Linux standalone executable..."
	pyinstaller --onefile scripts/biohub.spec

build-macos:
	@echo "Building macOS executable..."
	ARCHFLAGS="-arch x86_64" pyinstaller --onefile scripts/biohub.spec

build-windows:
	@echo "Building Windows executable..."
	wine pyinstaller --onefile scripts/biohub.spec

docker-airgap:
	@echo "Building Docker container for airgapped use..."
	docker build -t biohub-airgap .

clean:
	rm -rf __pycache__ dist build *.spec
	rm -rf logs/*
