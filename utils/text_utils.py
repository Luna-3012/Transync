from language_tool_python import LanguageTool

def correct_text(text, lang_code='en'):
    try:
        tool = LanguageTool(lang_code)
        return tool.correct(text)
    except:
        return text
    