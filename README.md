# AI-Research-Investment-Brief-Generator

### What it does:
User enters:
“Analyze HDFC Bank and give me an investment brief.”
Our multi-agent system will:
1. Search latest news (using google_search tool)
2. Fetch financial data (custom tool)
3. Analyze sentiment from news (custom tool)

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
  - sentiment_tool
  - stock_tool
  - report_tool

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

## Example prompt :
Generate a detailed investment brief for HDFC Bank (HDFCBANK.NS).
Include recent news sentiment, current stock price, 30-day return, volatility, and a short investment outlook.
