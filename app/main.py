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
    status = "passed" if errors else "failed"
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": status
    }


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file_path = path, errors = errors)
            for path, errors in linter_report.items()]