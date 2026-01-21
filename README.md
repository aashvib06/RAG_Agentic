# Agentic PDF-based RAG System

This project implements a Retrieval-Augmented Generation (RAG) system over research PDFs,
augmented with simple agentic decision-making.

The goal is to explore how retrieval quality, context construction, and adaptive control
affect the reliability of LLM-generated research summaries.

## Key Features
- PDF ingestion using LangChain document loaders
- Semantic retrieval with FAISS and sentence-transformer embeddings
- Local LLM inference using Ollama (no paid APIs)
- Agentic logic to adapt retrieval depth based on context sufficiency
- Modular design for research experimentation

## High-Level Architecture

PDFs → Chunking → Embeddings → FAISS Retrieval  
→ Agent decides if context is sufficient  
→ LLM synthesizes grounded response

## Intended Use
This codebase is intended for:
- Research internships
- Academic experimentation with RAG systems
- Studying hallucination, recall, and retrieval trade-offs

## Requirements
- Python 3.9+
- Ollama installed and running
- A local model pulled (e.g. `mistral`)
