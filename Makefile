.PHONY: help install dev build test lint format clean backend-dev backend-install

help:
	@echo "HEAVE Development Commands"
	@echo "=========================="
	@echo "make install       - Install frontend dependencies"
	@echo "make backend-install - Install backend dependencies"
	@echo "make dev           - Start development server"
	@echo "make build         - Build for production"
	@echo "make test          - Run tests"
	@echo "make lint          - Run linter"
	@echo "make format        - Format code"
	@echo "make clean         - Clean build artifacts"
	@echo "make backend-dev   - Start backend dev server"

install:
	npm install

backend-install:
	cd backend && pip install -r requirements.txt

dev:
	npm run dev

build:
	npm run build

test:
	npm run test

test-ui:
	npm run test:ui

test-coverage:
	npm run test:coverage

lint:
	npm run lint

lint-fix:
	npm run lint:fix

format:
	npm run format

format-check:
	npm run format:check

type-check:
	npm run type-check

clean:
	rm -rf dist/ node_modules/ .eslintcache .turbo/ coverage/
	cd backend && rm -rf __pycache__ .pytest_cache/ .mypy_cache/ build/ dist/ *.egg-info

backend-dev:
	cd backend && python main.py
