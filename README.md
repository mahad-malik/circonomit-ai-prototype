# Circonomit AI Prototype

This repository contains a prototype demonstrating the integration of local vector databases, Neo4j graph storage, and AI-powered summarization and entity extraction, designed as part of an AI-driven knowledge management system for Circonomit.

---

## Project Overview

The prototype processes business texts by:
- Extracting named entities (e.g., money amounts, dates) using spaCy.
- Embedding the text into vectors stored locally for efficient similarity search.
- Storing extracted entities and relationships in a Neo4j graph database.
- Generating AI-based summaries and context-aware reasoning using Google’s Gemini large language model.
- Providing an interactive Streamlit app to showcase input processing and results.

---

## Features

- **Entity Extraction:** Named entity recognition with spaCy.
- **Vector Embeddings:** Text embedded and stored in a local vector database.
- **Graph Storage:** Entities stored and linked in Neo4j.
- **AI Summarization:** Summaries generated with OpenAI GPT.
- **Interactive UI:** Streamlit frontend for easy demonstration.

---

## Getting Started

### Prerequisites

- Python 3.8+
- Neo4j Desktop or Aura (running instance)
- OpenAI API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
