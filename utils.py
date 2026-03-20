def format_float(value, decimals=2):
    """Retorna string formatada com número de casas decimais."""
    return f"{value:.{decimals}f}"

def validate_positive(value, default):
    """Garante que o valor seja positivo, senão usa default."""
    return value if value > 0 else default

