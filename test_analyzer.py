import pytest
from text_analyzer import analyze_text

def test_successful_analysis(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("Text analysis is great! Аналіз тексту — це great.", encoding="utf-8")
    
    result = analyze_text(str(test_file))
    
    assert "error" not in result
    assert result["word_count"] == 8
    assert result["frequency"]["great"] == 2
    assert result["frequency"]["аналіз"] == 1

def test_empty_file_handling(tmp_path):
    test_file = tmp_path / "empty.txt"
    test_file.write_text("   \n\t  ", encoding="utf-8")
    
    result = analyze_text(str(test_file))
    
    assert "error" in result
    assert result["error"] == "Помилка: Файл порожній."

def test_file_not_found_handling():
    result = analyze_text("non_existent_document.txt")
    
    assert "error" in result
    assert result["error"] == "Помилка: Файл не знайдено."