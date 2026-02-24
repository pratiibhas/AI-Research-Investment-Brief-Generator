# AI-Research-Investment-Brief-Generator

### What it does:
User enters:
“Analyze HDFC Bank and give me an investment brief.”
1. Our multi-agent system will:
2. Search latest news (using google_search tool)
3. Fetch financial data (custom tool)
4. Analyze sentiment from news (custom tool)

## Overview
This project implements a multi-agent system using Google ADK to generate AI-powered investment briefs for publicly traded companies.

## Architecture
- Root Agent: InvestmentOrchestrator
- Sub Agents:
  - NewsResearchAgent
  - FinancialAnalysisAgent
  - ReportGeneratorAgent

## Tools
- Built-in google_search tool
- Custom Tools:
  - analyze_sentiment
  - fetch_stock_data
  - generate_markdown_report

## Setup

1. Create virtual environment
2. Install dependencies:
   pip install -r requirements.txt
3. Add .env:
   GOOGLE_API_KEY=your_key_here

## Run

CLI Mode:
adk run investment_agent

Web Mode:
adk web
