from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from typing import List, Dict
import json

app = FastAPI(
    title="P2P Cards AI Module",
    description="AI-powered PDF processing for flashcard generation",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене указать конкретные домены
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "P2P Cards AI Module"}

@app.get("/health")
async def health_check():
    return {
        "status": "OK", 
        "message": "AI Module is running!",
        "service": "PDF Processing AI",
        "version": "1.0.0"
    }

@app.post("/process-pdf")
async def process_pdf(file: UploadFile = File(...)):
    """
    Process PDF file and extract content for flashcard generation
    """
    try:
        # Проверяем что файл - PDF
        if not file.filename.lower().endswith('.pdf'):
            raise HTTPException(status_code=400, detail="File must be a PDF")
        
        # Здесь будет логика обработки PDF и извлечения текста
        # Пока возвращаем заглушку
        return {
            "status": "success",
            "message": "PDF received successfully",
            "filename": file.filename,
            "cards_generated": 0,
            "content_preview": "PDF processing logic will be implemented here",
            "next_steps": [
                "Extract text from PDF",
                "Identify key concepts and definitions", 
                "Generate question-answer pairs",
                "Apply NLP for content analysis"
            ]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")

@app.get("/api/info")
async def api_info():
    """Информация о доступных эндпоинтах AI модуля"""
    return {
        "module": "AI PDF Processor",
        "endpoints": {
            "health": "/health",
            "process_pdf": "/process-pdf",
            "info": "/api/info"
        },
        "capabilities": [
            "PDF text extraction",
            "Content analysis",
            "Flashcard generation (planned)",
            "NLP processing (planned)"
        ]
    }

if __name__ == "__main__":
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
       
    )