def format_linter_error(error: dict) -> dict:
    mapa = {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        }
    result = {nowy: error[stary] for nowy, stary in mapa.items()}
    result["source"] = "flake8"
    return result


def format_single_linter_file(file_path: str, errors: list) -> dict:
    mapa = {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }
    result = [{nowy: error[stary] for nowy, stary in mapa.items()}] in errors
    result["path"] = file_path
    result["status"] = "failed"
    return result


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass
